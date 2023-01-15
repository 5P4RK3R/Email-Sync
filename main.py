import httplib2
import traceback
from googleapiclient import discovery
from oauth2client.client import AccessTokenCredentials
from pyspark.sql import SparkSession
from os import getenv
from pprint import pprint
from tqdm import tqdm
import pandas as pd
from pyspark.conf import SparkConf
from pyspark.context import SparkContext
from pyspark.sql import SparkSession

conf = SparkConf()
conf.setMaster("local").setAppName("Email Sync")
# conf.set("es.index.auto.create", "true")
conf.set("es.nodes", "localhost")  # name of my docker container, you might keep localhost
conf.set("es.port", "9200")

sc = SparkContext(conf=conf)
spark = SparkSession(sc)
access_token = getenv("access_token")
pprint(access_token)
access_token = "ya29.a0AX9GBdWmWSWQlhUdDwMTHp_sXnx1rYsEPWQYjiJ31leJj7QFGlSm5Ru_Mx-fMDeFl507PfbFgBy5mz8GFzWOhwTGteVImuAbsvRAHUKBBsofOsZVlVdO9K-1U8ki9dlqHQtX7_c2fK1Jvyt4Ufn-4E4I01s2aCgYKATwSARISFQHUCsbCAmfNZCMaBmX2M1Hh-x0ykQ0163"
credentials = AccessTokenCredentials(access_token, "my-user-agent/1.0")
http = httplib2.Http()
http = credentials.authorize(http)
service = discovery.build("gmail", "v1", http=http)
messages = service.users().messages().list(userId='me', maxResults=500).execute()
messageIds = messages.get("messages")
# print(messages)
print(len(messageIds))

def get_next_page_msg(mssg_list, results):

    if 'nextPageToken' in results:
        results = (
            service.users()
            .messages()
            .list(userId='me',pageToken=results["nextPageToken"])
            .execute()
        )
        # results = (
        #     service.users()
        #     .messages()
        #     .list(userId=email, q=query, pageToken=results["nextPageToken"],includeSpamTrash=True, maxResults=10000)
        #     .execute()
        # )
        mssg_list.extend(results["messages"])
        return get_next_page_msg(mssg_list, results)
        # if len(results.get("messages",[])):
        #     mssg_list.extend(results.get("messages"))
        #     return get_next_page_msg(mssg_list, results)
        # else:
        #     return mssg_list

    else:
        return mssg_list

messageIds = get_next_page_msg(messageIds, messages)
print(messageIds)
print(len(messageIds))
def getThread(thread):
    return [(msg["threadId"],msg["snippet"],msg["internalDate"]) for msg in service.users().threads().get(userId='me', id=thread["threadId"],format='full').execute().get("messages")]
# service.users().threads().get(userId='me', id=message["threadId"],format='full')
# print(service.users().threads().get(userId='me', id="185aa2672fce2c43",format='full').execute())
# spark = SparkSession.builder.getOrCreate()

# df = spark.createDataFrame()
# # ds = pd.DataFrame({"snippet":[msg["snippet"] for msg in service.users().threads().get(userId='me', id=message["threadId"],format='full').execute().get("messages")] for message in messages})
# # df = spark.createDataFrame(ds)
# df = spark.createDataFrame([service.users().threads().get(userId='me', id=message["threadId"],format='full').execute().get("messages") for message in messageIds], schema=['id','threadId','snippet'])
# df = spark.createDataFrame([[message["threadId"]] for message in messageIds], schema=['threadId'])
df = spark.createDataFrame([getThread(message)[0] for message in messageIds], schema=['threadId','snippet','date'])
df.show()
print(df.count())

res = df.write.format("org.elasticsearch.spark.sql").option("es.nodes", "http://localhost:9200").option("es.resource", "email_sync/_doc")
# Write the DataFrame to an Elasticsearch index
try:
    pprint(res.save("email_sync/data"))
    # df.write.format("org.elasticsearch.spark.sql").option("es.nodes", "http://localhost:9200").option("es.resource", "email_sync/_doc").save()
except Exception as e:
    print(e,traceback.format_exc())
# df.write.format("org.elasticsearch.spark.sql").option("es.nodes", "http://localhost:9200").option("es.resource", "email_sync/_doc").save()