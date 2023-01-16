# Email-Sync

# Spark-Submit Command:
spark-submit --packages org.elasticsearch:elasticsearch-spark-30_2.12:8.6.0 --master local main.py




23/01/15 23:13:35 INFO SharedState: Setting hive.metastore.warehouse.dir ('null') to the value of spark.sql.warehouse.dir.
23/01/15 23:13:35 INFO SharedState: Warehouse path is 'file:/Users/nitin/Projects/Python/PySpark/Email-Sync/spark-warehouse'.
23/01/15 23:13:39 INFO CodeGenerator: Code generated in 345.627792 ms
23/01/15 23:13:39 INFO SparkContext: Starting job: showString at NativeMethodAccessorImpl.java:0
23/01/15 23:13:39 INFO DAGScheduler: Got job 0 (showString at NativeMethodAccessorImpl.java:0) with 1 output partitions
23/01/15 23:13:39 INFO DAGScheduler: Final stage: ResultStage 0 (showString at NativeMethodAccessorImpl.java:0)
23/01/15 23:13:39 INFO DAGScheduler: Parents of final stage: List()
23/01/15 23:13:39 INFO DAGScheduler: Missing parents: List()
23/01/15 23:13:39 INFO DAGScheduler: Submitting ResultStage 0 (MapPartitionsRDD[6] at showString at NativeMethodAccessorImpl.java:0), which has no missing parents
23/01/15 23:13:39 INFO MemoryStore: Block broadcast_0 stored as values in memory (estimated size 12.5 KiB, free 434.4 MiB)
23/01/15 23:13:39 INFO MemoryStore: Block broadcast_0_piece0 stored as bytes in memory (estimated size 6.7 KiB, free 434.4 MiB)
23/01/15 23:13:39 INFO BlockManagerInfo: Added broadcast_0_piece0 in memory on nitins-air-2.domain.name:63336 (size: 6.7 KiB, free: 434.4 MiB)
23/01/15 23:13:39 INFO SparkContext: Created broadcast 0 from broadcast at DAGScheduler.scala:1513
23/01/15 23:13:39 INFO DAGScheduler: Submitting 1 missing tasks from ResultStage 0 (MapPartitionsRDD[6] at showString at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0))
23/01/15 23:13:39 INFO TaskSchedulerImpl: Adding task set 0.0 with 1 tasks resource profile 0
23/01/15 23:13:39 INFO TaskSetManager: Starting task 0.0 in stage 0.0 (TID 0) (nitins-air-2.domain.name, executor driver, partition 0, PROCESS_LOCAL, 663252 bytes) taskResourceAssignments Map()
23/01/15 23:13:40 INFO Executor: Running task 0.0 in stage 0.0 (TID 0)
23/01/15 23:13:40 INFO Executor: Finished task 0.0 in stage 0.0 (TID 0). 4350 bytes result sent to driver
23/01/15 23:13:40 INFO TaskSetManager: Finished task 0.0 in stage 0.0 (TID 0) in 788 ms on nitins-air-2.domain.name (executor driver) (1/1)
23/01/15 23:13:40 INFO TaskSchedulerImpl: Removed TaskSet 0.0, whose tasks have all completed, from pool 
23/01/15 23:13:40 INFO PythonAccumulatorV2: Connected to AccumulatorServer at host: 127.0.0.1 port: 63380
23/01/15 23:13:40 INFO DAGScheduler: ResultStage 0 (showString at NativeMethodAccessorImpl.java:0) finished in 1.398 s
23/01/15 23:13:40 INFO DAGScheduler: Job 0 is finished. Cancelling potential speculative or zombie tasks for this job
23/01/15 23:13:40 INFO TaskSchedulerImpl: Killing all running tasks in stage 0: Stage finished
23/01/15 23:13:40 INFO DAGScheduler: Job 0 finished: showString at NativeMethodAccessorImpl.java:0, took 1.471106 s
23/01/15 23:13:40 INFO CodeGenerator: Code generated in 47.073458 ms
+----------------+--------------------+-------------+
|        threadId|             snippet|         date|
+----------------+--------------------+-------------+
|185aa2672fce2c43|Hello Mahendra, I...|1673596923000|
|185ade800f815e4b|Your Daily Work S...|1673659940000|
|185aa2672fce2c43|Hello Mahendra, I...|1673596923000|
|185a9bd18d77c972|CAUTION: This ema...|1673590019000|
|185a8c345dedc804|Your Daily Work S...|1673573647000|
|185a7135dae3a98b|Hi Mahendra, It w...|1673545340000|
|185a7135dae3a98b|Hi Mahendra, It w...|1673545340000|
|185a70d383846e33|Collaborate bette...|1673544938000|
|185a6f7f3a1ec98a|Bring everyone to...|1673543518000|
|185a6babbbd1146a|Join us on Januar...|1673539517000|
|185a6a5822c9ce55|Thank you for con...|1673538118000|
|185a6a5778a4a1e4|CAUTION: This ema...|1673538117000|
|185a53345135b4eb|CAUTION: This ema...|1673513877000|
|185a533426840960|Thank you for con...|1673513877000|
|185a39dba0dcc200|Your Daily Work S...|1673487301000|
|185a332b77c3b079|Hi Mahendra, Warm...|1673480286000|
|185a21470c858195|Simple tips for s...|1673461525000|
|185a1ea91c54a2f1|Why reply when yo...|1673458746000|
|185a10b4476553fc|Hello Mahendra, B...|1673444147000|
|185a10b4476553fc|Hello Mahendra, B...|1673444147000|
+----------------+--------------------+-------------+
only showing top 20 rows

23/01/15 23:13:41 INFO CodeGenerator: Code generated in 39.968917 ms
23/01/15 23:13:41 INFO DAGScheduler: Registering RDD 8 (count at NativeMethodAccessorImpl.java:0) as input to shuffle 0
23/01/15 23:13:41 INFO DAGScheduler: Got map stage job 1 (count at NativeMethodAccessorImpl.java:0) with 1 output partitions
23/01/15 23:13:41 INFO DAGScheduler: Final stage: ShuffleMapStage 1 (count at NativeMethodAccessorImpl.java:0)
23/01/15 23:13:41 INFO DAGScheduler: Parents of final stage: List()
23/01/15 23:13:41 INFO DAGScheduler: Missing parents: List()
23/01/15 23:13:41 INFO DAGScheduler: Submitting ShuffleMapStage 1 (MapPartitionsRDD[8] at count at NativeMethodAccessorImpl.java:0), which has no missing parents
23/01/15 23:13:41 INFO MemoryStore: Block broadcast_1 stored as values in memory (estimated size 15.8 KiB, free 434.4 MiB)
23/01/15 23:13:41 INFO MemoryStore: Block broadcast_1_piece0 stored as bytes in memory (estimated size 8.4 KiB, free 434.4 MiB)
23/01/15 23:13:41 INFO BlockManagerInfo: Added broadcast_1_piece0 in memory on nitins-air-2.domain.name:63336 (size: 8.4 KiB, free: 434.4 MiB)
23/01/15 23:13:41 INFO SparkContext: Created broadcast 1 from broadcast at DAGScheduler.scala:1513
23/01/15 23:13:41 INFO DAGScheduler: Submitting 1 missing tasks from ShuffleMapStage 1 (MapPartitionsRDD[8] at count at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0))
23/01/15 23:13:41 INFO TaskSchedulerImpl: Adding task set 1.0 with 1 tasks resource profile 0
23/01/15 23:13:41 INFO BlockManagerInfo: Removed broadcast_0_piece0 on nitins-air-2.domain.name:63336 in memory (size: 6.7 KiB, free: 434.4 MiB)
23/01/15 23:13:41 INFO TaskSetManager: Starting task 0.0 in stage 1.0 (TID 1) (nitins-air-2.domain.name, executor driver, partition 0, PROCESS_LOCAL, 663241 bytes) taskResourceAssignments Map()
23/01/15 23:13:41 INFO Executor: Running task 0.0 in stage 1.0 (TID 1)
23/01/15 23:13:41 INFO PythonRunner: Times: total = 46, boot = 4, init = 39, finish = 3
23/01/15 23:13:41 INFO Executor: Finished task 0.0 in stage 1.0 (TID 1). 2327 bytes result sent to driver
23/01/15 23:13:41 INFO TaskSetManager: Finished task 0.0 in stage 1.0 (TID 1) in 192 ms on nitins-air-2.domain.name (executor driver) (1/1)
23/01/15 23:13:41 INFO TaskSchedulerImpl: Removed TaskSet 1.0, whose tasks have all completed, from pool 
23/01/15 23:13:41 INFO DAGScheduler: ShuffleMapStage 1 (count at NativeMethodAccessorImpl.java:0) finished in 0.249 s
23/01/15 23:13:41 INFO DAGScheduler: looking for newly runnable stages
23/01/15 23:13:41 INFO DAGScheduler: running: Set()
23/01/15 23:13:41 INFO DAGScheduler: waiting: Set()
23/01/15 23:13:41 INFO DAGScheduler: failed: Set()
23/01/15 23:13:41 INFO CodeGenerator: Code generated in 38.577583 ms
23/01/15 23:13:41 INFO SparkContext: Starting job: count at NativeMethodAccessorImpl.java:0
23/01/15 23:13:41 INFO DAGScheduler: Got job 2 (count at NativeMethodAccessorImpl.java:0) with 1 output partitions
23/01/15 23:13:41 INFO DAGScheduler: Final stage: ResultStage 3 (count at NativeMethodAccessorImpl.java:0)
23/01/15 23:13:41 INFO DAGScheduler: Parents of final stage: List(ShuffleMapStage 2)
23/01/15 23:13:41 INFO DAGScheduler: Missing parents: List()
23/01/15 23:13:41 INFO DAGScheduler: Submitting ResultStage 3 (MapPartitionsRDD[11] at count at NativeMethodAccessorImpl.java:0), which has no missing parents
23/01/15 23:13:41 INFO MemoryStore: Block broadcast_2 stored as values in memory (estimated size 11.1 KiB, free 434.4 MiB)
23/01/15 23:13:41 INFO MemoryStore: Block broadcast_2_piece0 stored as bytes in memory (estimated size 5.5 KiB, free 434.4 MiB)
23/01/15 23:13:41 INFO BlockManagerInfo: Removed broadcast_1_piece0 on nitins-air-2.domain.name:63336 in memory (size: 8.4 KiB, free: 434.4 MiB)
23/01/15 23:13:41 INFO BlockManagerInfo: Added broadcast_2_piece0 in memory on nitins-air-2.domain.name:63336 (size: 5.5 KiB, free: 434.4 MiB)
23/01/15 23:13:41 INFO SparkContext: Created broadcast 2 from broadcast at DAGScheduler.scala:1513
23/01/15 23:13:41 INFO DAGScheduler: Submitting 1 missing tasks from ResultStage 3 (MapPartitionsRDD[11] at count at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0))
23/01/15 23:13:41 INFO TaskSchedulerImpl: Adding task set 3.0 with 1 tasks resource profile 0
23/01/15 23:13:41 INFO TaskSetManager: Starting task 0.0 in stage 3.0 (TID 2) (nitins-air-2.domain.name, executor driver, partition 0, NODE_LOCAL, 4453 bytes) taskResourceAssignments Map()
23/01/15 23:13:41 INFO Executor: Running task 0.0 in stage 3.0 (TID 2)
23/01/15 23:13:41 INFO ShuffleBlockFetcherIterator: Getting 1 (60.0 B) non-empty blocks including 1 (60.0 B) local and 0 (0.0 B) host-local and 0 (0.0 B) push-merged-local and 0 (0.0 B) remote blocks
23/01/15 23:13:41 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 13 ms
23/01/15 23:13:41 INFO Executor: Finished task 0.0 in stage 3.0 (TID 2). 2656 bytes result sent to driver
23/01/15 23:13:41 INFO TaskSetManager: Finished task 0.0 in stage 3.0 (TID 2) in 115 ms on nitins-air-2.domain.name (executor driver) (1/1)
23/01/15 23:13:41 INFO TaskSchedulerImpl: Removed TaskSet 3.0, whose tasks have all completed, from pool 
23/01/15 23:13:41 INFO DAGScheduler: ResultStage 3 (count at NativeMethodAccessorImpl.java:0) finished in 0.223 s
23/01/15 23:13:41 INFO DAGScheduler: Job 2 is finished. Cancelling potential speculative or zombie tasks for this job
23/01/15 23:13:41 INFO TaskSchedulerImpl: Killing all running tasks in stage 3: Stage finished
23/01/15 23:13:41 INFO DAGScheduler: Job 2 finished: count at NativeMethodAccessorImpl.java:0, took 0.255510 s
3096
23/01/15 23:13:42 INFO Version: Elasticsearch Hadoop v8.6.0 [da4f3c3f20]
23/01/15 23:13:42 WARN Resource: Detected type name in resource [email_sync/_doc]. Type names are deprecated and will be removed in a later release.
23/01/15 23:13:42 INFO SparkContext: Starting job: runJob at EsSparkSQL.scala:103
23/01/15 23:13:42 INFO DAGScheduler: Got job 3 (runJob at EsSparkSQL.scala:103) with 1 output partitions
23/01/15 23:13:42 INFO DAGScheduler: Final stage: ResultStage 4 (runJob at EsSparkSQL.scala:103)
23/01/15 23:13:42 INFO DAGScheduler: Parents of final stage: List()
23/01/15 23:13:42 INFO DAGScheduler: Missing parents: List()
23/01/15 23:13:42 INFO DAGScheduler: Submitting ResultStage 4 (MapPartitionsRDD[15] at rdd at EsSparkSQL.scala:103), which has no missing parents
23/01/15 23:13:42 INFO MemoryStore: Block broadcast_3 stored as values in memory (estimated size 38.7 KiB, free 434.3 MiB)
23/01/15 23:13:42 INFO MemoryStore: Block broadcast_3_piece0 stored as bytes in memory (estimated size 14.3 KiB, free 434.3 MiB)
23/01/15 23:13:42 INFO BlockManagerInfo: Added broadcast_3_piece0 in memory on nitins-air-2.domain.name:63336 (size: 14.3 KiB, free: 434.4 MiB)
23/01/15 23:13:42 INFO BlockManagerInfo: Removed broadcast_2_piece0 on nitins-air-2.domain.name:63336 in memory (size: 5.5 KiB, free: 434.4 MiB)
23/01/15 23:13:42 INFO SparkContext: Created broadcast 3 from broadcast at DAGScheduler.scala:1513
23/01/15 23:13:42 INFO DAGScheduler: Submitting 1 missing tasks from ResultStage 4 (MapPartitionsRDD[15] at rdd at EsSparkSQL.scala:103) (first 15 tasks are for partitions Vector(0))
23/01/15 23:13:42 INFO TaskSchedulerImpl: Adding task set 4.0 with 1 tasks resource profile 0
23/01/15 23:13:43 INFO TaskSetManager: Starting task 0.0 in stage 4.0 (TID 3) (nitins-air-2.domain.name, executor driver, partition 0, PROCESS_LOCAL, 663252 bytes) taskResourceAssignments Map()
23/01/15 23:13:43 INFO Executor: Running task 0.0 in stage 4.0 (TID 3)
23/01/15 23:13:43 WARN Resource: Detected type name in resource [email_sync/_doc]. Type names are deprecated and will be removed in a later release.
23/01/15 23:13:43 INFO EsDataFrameWriter: Writing to [email_sync/_doc]
23/01/15 23:13:43 WARN Resource: Detected type name in resource [email_sync/_doc]. Type names are deprecated and will be removed in a later release.
23/01/15 23:13:43 WARN Resource: Detected type name in resource [email_sync/_doc]. Type names are deprecated and will be removed in a later release.
23/01/15 23:13:43 WARN Resource: Detected type name in resource [email_sync/_doc]. Type names are deprecated and will be removed in a later release.
23/01/15 23:13:43 WARN Resource: Detected type name in resource [email_sync/_doc]. Type names are deprecated and will be removed in a later release.
23/01/15 23:13:43 WARN Resource: Detected type name in resource [email_sync/_doc]. Type names are deprecated and will be removed in a later release.
23/01/15 23:13:44 INFO PythonRunner: Times: total = 49, boot = -1597, init = 1644, finish = 2
23/01/15 23:13:44 INFO Executor: Finished task 0.0 in stage 4.0 (TID 3). 1703 bytes result sent to driver
23/01/15 23:13:44 INFO TaskSetManager: Finished task 0.0 in stage 4.0 (TID 3) in 1868 ms on nitins-air-2.domain.name (executor driver) (1/1)
23/01/15 23:13:44 INFO TaskSchedulerImpl: Removed TaskSet 4.0, whose tasks have all completed, from pool 
23/01/15 23:13:44 INFO DAGScheduler: ResultStage 4 (runJob at EsSparkSQL.scala:103) finished in 2.006 s
23/01/15 23:13:44 INFO DAGScheduler: Job 3 is finished. Cancelling potential speculative or zombie tasks for this job
23/01/15 23:13:44 INFO TaskSchedulerImpl: Killing all running tasks in stage 4: Stage finished
23/01/15 23:13:44 INFO DAGScheduler: Job 3 finished: runJob at EsSparkSQL.scala:103, took 2.028176 s
None
23/01/15 23:13:45 INFO SparkContext: Invoking stop() from shutdown hook
23/01/15 23:13:45 INFO SparkUI: Stopped Spark web UI at http://nitins-air-2.domain.name:4041
23/01/15 23:13:45 INFO MapOutputTrackerMasterEndpoint: MapOutputTrackerMasterEndpoint stopped!
23/01/15 23:13:45 INFO MemoryStore: MemoryStore cleared
23/01/15 23:13:45 INFO BlockManager: BlockManager stopped
23/01/15 23:13:45 INFO BlockManagerMaster: BlockManagerMaster stopped
23/01/15 23:13:45 INFO OutputCommitCoordinator$OutputCommitCoordinatorEndpoint: OutputCommitCoordinator stopped!
23/01/15 23:13:45 INFO SparkContext: Successfully stopped SparkContext
23/01/15 23:13:45 INFO ShutdownHookManager: Shutdown hook called
23/01/15 23:13:45 INFO ShutdownHookManager: Deleting directory /private/var/folders/zx/q1yh50757p79dswgtkyj_n_r0000gn/T/spark-202a05c9-0af5-4196-8cfa-d8804642673f
23/01/15 23:13:45 INFO ShutdownHookManager: Deleting directory /private/var/folders/zx/q1yh50757p79dswgtkyj_n_r0000gn/T/spark-bd49192a-bfa2-427f-8141-408a3acf25d4
23/01/15 23:13:45 INFO ShutdownHookManager: Deleting directory /private/var/folders/zx/q1yh50757p79dswgtkyj_n_r0000gn/T/spark-bd49192a-bfa2-427f-8141-408a3acf25d4/pyspark-4e9fbc44-31c0-474d-ba31-e9188c55e4c7



{
  "id": "185aa2672fce2c43",
  "historyId": "323270",
  "messages": [
    {
      "id": "185aa2672fce2c43",
      "threadId": "185aa2672fce2c43",
      "labelIds": [
        "UNREAD",
        "IMPORTANT",
        "CATEGORY_UPDATES",
        "INBOX"
      ],
      "snippet": "Hello Mahendra, I am Mrunal from AWS Premium Support!! It was really nice talking to you over chat today. Please find the summary of our chat below: You reached out to us as you had queries regarding",
      "payload": {
        "partId": "",
        "mimeType": "multipart/alternative",
        "filename": "",
        "headers": [
          {
            "name": "Delivered-To",
            "value": "mahendra@spiceblue.co"
          },
          {
            "name": "Received",
            "value": "by 2002:a05:6a10:dba7:b0:361:1249:b4ae with SMTP id uv39csp228220pxb;        Fri, 13 Jan 2023 00:02:04 -0800 (PST)"
          },
          {
            "name": "X-Google-Smtp-Source",
            "value": "AMrXdXtrQ7n5hVQVk+N2CBuHhkDr1MS4hdQMEZwDsgh3BEzZGb9DVK+noktxAwsBaH9KgFa32LoD"
          },
          {
            "name": "X-Received",
            "value": "by 2002:a05:622a:6106:b0:3b0:2fa:8a90 with SMTP id hg6-20020a05622a610600b003b002fa8a90mr13910472qtb.8.1673596924527;        Fri, 13 Jan 2023 00:02:04 -0800 (PST)"
          },
          {
            "name": "ARC-Seal",
            "value": "i=1; a=rsa-sha256; t=1673596924; cv=none;        d=google.com; s=arc-20160816;        b=XAv067GyTxmlnzC3AhP8LnFybJGEKSXQPOrnkUkbRblOUB4guCvAQTWtpY3DGMPz4S         Q+jmyQYPS9m1Zfia7pxKrMDCbjmzmz+QyY13Yg+ZZOAHFw1bhcJvwJbqrmRF4e+pCYgi         Nlssjl6oEkn69mZ+8tXL1kSWYMVofWB91KXvt27xWuwu3ajwX8BR7KWr3P5X7UT9x4o5         KhwtXrNEz+tiBQe4NPTgVqQAnl8GaOyMl9mxH55HWXJrwniWq7P9yaH9MIfdTcg4tbkF         mUS3SReT7wsEspPyVP28isleirG+3m6I+EHl1u3ZzCckEDRowzhCWJBMXYRUv2nLdqA9         Iaag=="
          },
          {
            "name": "ARC-Message-Signature",
            "value": "i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;        h=feedback-id:date:message-id:mime-version:subject:cc:to:from         :dkim-signature:dkim-signature;        bh=u8htKkg65W7/DmVpGYwpK3U0hRQb1qYf7M4DM/qVNz8=;        b=F8TTiax8sfFxT3aruI48p9I4f8D1UNWCStV//2o/xffyDZbeoazffhLiAsZcTyx20t         5cmMzZlg+RGKcligdeFILojn2cnHq5ChP38NfivriNJdp9yyxGN+dLXWSuUegv7qLnsI         kXkKFKUXORI//avmxHWYKwvB4kXFzI7gFuoZSRZaFybuc5bMDWW5xUes1i9KMRz4lp5p         ySD1RQQZXSXOTTIelGlvssnJAM+RysWwg+SjCXvVquGMjiZ2LKIxG7rbMleyo+U2wFoj         9zpy1mk0S5Uwc4bRDh0UuEOrFjmkCiAXGvS2PCjq5rEX2I8tG+RZlUc3XoydvCb9g0Vo         4EJQ=="
          },
          {
            "name": "ARC-Authentication-Results",
            "value": "i=1; mx.google.com;       dkim=pass header.i=@amazon.com header.s=benmzc5omgrgqjsu3tg2d2m7nez6lzho header.b='FHP/NuUj';       dkim=pass header.i=@amazonses.com header.s=6gbrjpgwjskckoa6a5zn6fwqkn67xbtw header.b=lmzbhFuf;       spf=pass (google.com: domain of 01000185aa266cb8-61921dea-476c-4f47-9eba-8738c3700626-000000@amazonses.com designates 54.240.11.37 as permitted sender) smtp.mailfrom=01000185aa266cb8-61921dea-476c-4f47-9eba-8738c3700626-000000@amazonses.com;       dmarc=pass (p=QUARANTINE sp=QUARANTINE dis=NONE) header.from=amazon.com"
          },
          {
            "name": "Return-Path",
            "value": "<01000185aa266cb8-61921dea-476c-4f47-9eba-8738c3700626-000000@amazonses.com>"
          },
          {
            "name": "Received",
            "value": "from a11-37.smtp-out.amazonses.com (a11-37.smtp-out.amazonses.com. [54.240.11.37])        by mx.google.com with ESMTPS id h17-20020ac846d1000000b003aea693ca72si7832204qto.5.2023.01.13.00.02.04        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-GCM-SHA256 bits=128/128);        Fri, 13 Jan 2023 00:02:04 -0800 (PST)"
          },
          {
            "name": "Received-SPF",
            "value": "pass (google.com: domain of 01000185aa266cb8-61921dea-476c-4f47-9eba-8738c3700626-000000@amazonses.com designates 54.240.11.37 as permitted sender) client-ip=54.240.11.37;"
          },
          {
            "name": "Authentication-Results",
            "value": "mx.google.com;       dkim=pass header.i=@amazon.com header.s=benmzc5omgrgqjsu3tg2d2m7nez6lzho header.b='FHP/NuUj';       dkim=pass header.i=@amazonses.com header.s=6gbrjpgwjskckoa6a5zn6fwqkn67xbtw header.b=lmzbhFuf;       spf=pass (google.com: domain of 01000185aa266cb8-61921dea-476c-4f47-9eba-8738c3700626-000000@amazonses.com designates 54.240.11.37 as permitted sender) smtp.mailfrom=01000185aa266cb8-61921dea-476c-4f47-9eba-8738c3700626-000000@amazonses.com;       dmarc=pass (p=QUARANTINE sp=QUARANTINE dis=NONE) header.from=amazon.com"
          },
          {
            "name": "DKIM-Signature",
            "value": "v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple; s=benmzc5omgrgqjsu3tg2d2m7nez6lzho; d=amazon.com; t=1673596923; h=From:To:Cc:Subject:MIME-Version:Content-Type:Message-ID:Date; bh=tmPIuVw5iKqVMGT4uKNi4AWjsErugVN6BKJwaNHgBIE=; b=FHP/NuUj+KqQWMquAsUa/9hg8TJq97ayOcI9aIIzurKADzMYf3FdnJZwD+xX79QB yCcufiHAlOAIZDkJWk8rQ9wUDQ081cuKcRVyk3tVfBKlM+KgIreqJzuzAgV4yhMBoe4 DWxMrL8aPWdmT3mQOUAJVNwAmN3S/EKhTPg3i/N4="
          },
          {
            "name": "DKIM-Signature",
            "value": "v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple; s=6gbrjpgwjskckoa6a5zn6fwqkn67xbtw; d=amazonses.com; t=1673596923; h=From:To:Cc:Subject:MIME-Version:Content-Type:Message-ID:Date:Feedback-ID; bh=tmPIuVw5iKqVMGT4uKNi4AWjsErugVN6BKJwaNHgBIE=; b=lmzbhFufPww3V4crNAmSk0iuxm8YU6SwkkYRW+r49PR3SxBpiA9WcLFQk5WGB//z ppilRr2ZPW+vdwuamblUKNk4Aj4byroA8vwHNTWhdKO8wMUbQjIBY1j9WrOvHC2T0HA 4IlT0lC6j925ZpK/mOT+mz9GLel33HiS35RuuIWA="
          },
          {
            "name": "From",
            "value": "Amazon Web Services <no-reply-aws@amazon.com>"
          },
          {
            "name": "To",
            "value": "prem@spiceblue.co"
          },
          {
            "name": "Cc",
            "value": "mahendra@spiceblue.co"
          },
          {
            "name": "Subject",
            "value": "RE:[CASE 11744859211] Chat: Restore Snapshot"
          },
          {
            "name": "MIME-Version",
            "value": "1.0"
          },
          {
            "name": "Content-Type",
            "value": "multipart/alternative; boundary='----=_Part_1085120_1020681126.1673596923068'"
          },
          {
            "name": "Message-ID",
            "value": "<01000185aa266cb8-61921dea-476c-4f47-9eba-8738c3700626-000000@email.amazonses.com>"
          },
          {
            "name": "Date",
            "value": "Fri, 13 Jan 2023 08:02:03 +0000"
          },
          {
            "name": "Feedback-ID",
            "value": "1.us-east-1.huE3KBUlbB3jXEGPu3NtaNXYRdURNu75MKOqRLEVhr4=:AmazonSES"
          },
          {
            "name": "X-SES-Outgoing",
            "value": "2023.01.13-54.240.11.37"
          }
        ],
        "body": {
          "size": 0
        },
        "parts": [
          {
            "partId": "0",
            "mimeType": "text/plain",
            "filename": "",
            "headers": [
              {
                "name": "Content-Type",
                "value": "text/plain; charset=UTF-8"
              },
              {
                "name": "Content-Transfer-Encoding",
                "value": "quoted-printable"
              }
            ],
            "body": {
              "size": 2260,
              "data": "SGVsbG8gTWFoZW5kcmEsDQoNCkkgYW0gTXJ1bmFsIGZyb20gQVdTIFByZW1pdW0gU3VwcG9ydCEhDQoNCkl0IHdhcyByZWFsbHkgbmljZSB0YWxraW5nIHRvIHlvdSBvdmVyIGNoYXQgdG9kYXkuIFBsZWFzZSBmaW5kIHRoZSBzdW1tYXJ5IG9mIG91ciBjaGF0IGJlbG93Og0KDQpZb3UgcmVhY2hlZCBvdXQgdG8gdXMgYXMgeW91IGhhZCBxdWVyaWVzIHJlZ2FyZGluZyBPcGVuc2VhcmNoIG1pZ3JhdGlvbiwgeW91IHdlcmUgYWJsZSB0byBwZXJmb3JtIGl0IGZvciAyLzQgZG9tYWlucyBhbmQgZmFjaW5nIGlzc3VlIHdpdGggdGhlIG90aGVyIHR3by4gDQoNCldlIGZvbGxvd2VkIHRoZSBzdGVwcyBhbmQgbG9va2VkIGZvciBwb3NzaWJsZSBlcnJvcnMuIEkgd291bGQgbGlrZSB0byBpbmZvcm0geW91IHRoYXQgSSBoYXZlIHN0YXJ0ZWQgcmVwbGljYXRpbmcgdGhlIHNjZW5hcmlvIGF0IG15IGVuZCBhbmQgSSBhbSBhbHNvIGluIHRvdWNoIHdpdGggdGhlIHByZXZpb3VzIGVuZ2luZWVyIHJlZ2FyZGluZyB0aGlzIGlzc3VlLiANCg0KUGxlYXNlIGJlIGFzc3VyZWQgdGhhdCBhbnkga2luZCBvZiB1cGRhdGUgd291bGQgYmUgcGFzc2VkIG9uIHRvIHlvdSBpbW1lZGlhdGVseS4gDQoNClVudGlsIHRoYW4gSSB3b3VsZCBrZWVwIHRoZSBjYXNlIGluIFwiUGVuZGluZyBBbWF6b24gQWN0aW9uXCIuDQoNClNob3VsZCB5b3UgaGF2ZSBhbnkgY29uY2VybnMgcGxlYXNlIGZlZWwgZnJlZSB0byByZWFjaCBvdXQgdG8gdXMgYW5kIHdlIHdpbGwgYmUgZ2xhZCB0byBhc3Npc3QgeW91IGZ1cnRoZXIuDQoNClRoYW5rIHlvdSENCg0KV2UgdmFsdWUgeW91ciBmZWVkYmFjay4gUGxlYXNlIHNoYXJlIHlvdXIgZXhwZXJpZW5jZSBieSByYXRpbmcgdGhpcyBhbmQgb3RoZXIgY29ycmVzcG9uZGVuY2VzIGluIHRoZSBBV1MgU3VwcG9ydCBDZW50ZXIuIFlvdSBjYW4gcmF0ZSBhIGNvcnJlc3BvbmRlbmNlIGJ5IHNlbGVjdGluZyB0aGUgc3RhcnMgaW4gdGhlIHRvcCByaWdodCBjb3JuZXIgb2YgdGhlIGNvcnJlc3BvbmRlbmNlLg0KDQpCZXN0IHJlZ2FyZHMsDQpNcnVuYWwgIEsuDQpBbWF6b24gV2ViIFNlcnZpY2VzDQogID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQ0KDQogIFRvIHNoYXJlIHlvdXIgZXhwZXJpZW5jZSBvciBjb250YWN0IHVzIGFnYWluIGFib3V0IHRoaXMgY2FzZSwgcGxlYXNlIHJldHVybiB0byB0aGUgQVdTIFN1cHBvcnQgQ2VudGVyIHVzaW5nIHRoZSBmb2xsb3dpbmcgVVJMOiBodHRwczovL2NvbnNvbGUuYXdzLmFtYXpvbi5jb20vc3VwcG9ydC9ob21lIy9jYXNlLz9kaXNwbGF5SWQ9MTE3NDQ4NTkyMTEmbGFuZ3VhZ2U9ZW4NCg0KICBOb3RlLCB0aGlzIGUtbWFpbCB3YXMgc2VudCBmcm9tIGFuIGFkZHJlc3MgdGhhdCBjYW5ub3QgYWNjZXB0IGluY29taW5nIGUtbWFpbHMuDQogIFRvIHJlc3BvbmQgdG8gdGhpcyBjYXNlLCBwbGVhc2UgZm9sbG93IHRoZSBsaW5rIGFib3ZlIHRvIHJlc3BvbmQgZnJvbSB5b3VyIEFXUyBTdXBwb3J0IENlbnRlci4NCg0KICA9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0NCg0KICBEb27igJl0IG1pc3MgbWVzc2FnZXMgZnJvbSBBV1MgU3VwcG9ydCB3aGVuIHlvdSBuZWVkIGhlbHAhIFVwZGF0ZSB5b3VyIGNvbnRhY3QgaW5mb3JtYXRpb246DQogIGh0dHBzOi8vY29uc29sZS5hd3MuYW1hem9uLmNvbS9iaWxsaW5nL2hvbWUjL2FjY291bnQNCg0KICBJZiB5b3UgcmVjZWl2ZSBhbiBlcnJvciBtZXNzYWdlIHdoZW4gdmlzaXRpbmcgdGhlIGNvbnRhY3QgaW5mb3JtYXRpb24gcGFnZSwgdmlzaXQ6DQogIGh0dHBzOi8vYXdzLmFtYXpvbi5jb20vcHJlbWl1bXN1cHBvcnQva25vd2xlZGdlLWNlbnRlci9pYW0tYmlsbGluZy1hY2Nlc3MvDQoNCiAgQVdTIFN1cHBvcnQ6DQogIGh0dHBzOi8vYXdzLmFtYXpvbi5jb20vcHJlbWl1bXN1cHBvcnQva25vd2xlZGdlLWNlbnRlci8NCg0KICBBV1MgRG9jdW1lbnRhdGlvbjoNCiAgaHR0cHM6Ly9kb2NzLmF3cy5hbWF6b24uY29tLw0KDQogIEFXUyBDb3N0IE1hbmFnZW1lbnQ6DQogIGh0dHBzOi8vYXdzLmFtYXpvbi5jb20vYXdzLWNvc3QtbWFuYWdlbWVudC8NCg0KICBBV1MgVHJhaW5pbmc6DQogIGh0dHA6Ly9hd3MuYW1hem9uLmNvbS90cmFpbmluZy8NCg0KICBBV1MgTWFuYWdlZCBTZXJ2aWNlczoNCiAgaHR0cHM6Ly9hd3MuYW1hem9uLmNvbS9tYW5hZ2VkLXNlcnZpY2VzLw=="
            }
          },
          {
            "partId": "1",
            "mimeType": "text/html",
            "filename": "",
            "headers": [
              {
                "name": "Content-Type",
                "value": "text/html; charset=UTF-8"
              },
              {
                "name": "Content-Transfer-Encoding",
                "value": "quoted-printable"
              }
            ],
            "body": {
              "size": 4503,
              "data": "PCFET0NUWVBFIGh0bWw-PHA-SGVsbG8gTWFoZW5kcmEsPGJyLz48YnIvPkkgYW0gTXJ1bmFsIGZyb20gQVdTIFByZW1pdW0gU3VwcG9ydCEhPGJyLz48YnIvPkl0IHdhcyByZWFsbHkgbmljZSB0YWxraW5nIHRvIHlvdSBvdmVyIGNoYXQgdG9kYXkuIFBsZWFzZSBmaW5kIHRoZSBzdW1tYXJ5IG9mIG91ciBjaGF0IGJlbG93Ojxici8-PGJyLz5Zb3UgcmVhY2hlZCBvdXQgdG8gdXMgYXMgeW91IGhhZCBxdWVyaWVzIHJlZ2FyZGluZyBPcGVuc2VhcmNoIG1pZ3JhdGlvbiwgeW91IHdlcmUgYWJsZSB0byBwZXJmb3JtIGl0IGZvciAyLzQgZG9tYWlucyBhbmQgZmFjaW5nIGlzc3VlIHdpdGggdGhlIG90aGVyIHR3by4gPGJyLz48YnIvPldlIGZvbGxvd2VkIHRoZSBzdGVwcyBhbmQgbG9va2VkIGZvciBwb3NzaWJsZSBlcnJvcnMuIEkgd291bGQgbGlrZSB0byBpbmZvcm0geW91IHRoYXQgSSBoYXZlIHN0YXJ0ZWQgcmVwbGljYXRpbmcgdGhlIHNjZW5hcmlvIGF0IG15IGVuZCBhbmQgSSBhbSBhbHNvIGluIHRvdWNoIHdpdGggdGhlIHByZXZpb3VzIGVuZ2luZWVyIHJlZ2FyZGluZyB0aGlzIGlzc3VlLiA8YnIvPjxici8-UGxlYXNlIGJlIGFzc3VyZWQgdGhhdCBhbnkga2luZCBvZiB1cGRhdGUgd291bGQgYmUgcGFzc2VkIG9uIHRvIHlvdSBpbW1lZGlhdGVseS4gPGJyLz48YnIvPlVudGlsIHRoYW4gSSB3b3VsZCBrZWVwIHRoZSBjYXNlIGluIFwmIzM0O1BlbmRpbmcgQW1hem9uIEFjdGlvblwmIzM0Oy48YnIvPjxici8-U2hvdWxkIHlvdSBoYXZlIGFueSBjb25jZXJucyBwbGVhc2UgZmVlbCBmcmVlIHRvIHJlYWNoIG91dCB0byB1cyBhbmQgd2Ugd2lsbCBiZSBnbGFkIHRvIGFzc2lzdCB5b3UgZnVydGhlci48YnIvPjxici8-VGhhbmsgeW91ITxici8-PGJyLz5XZSB2YWx1ZSB5b3VyIGZlZWRiYWNrLiBQbGVhc2Ugc2hhcmUgeW91ciBleHBlcmllbmNlIGJ5IHJhdGluZyB0aGlzIGFuZCBvdGhlciBjb3JyZXNwb25kZW5jZXMgaW4gdGhlIEFXUyBTdXBwb3J0IENlbnRlci4gWW91IGNhbiByYXRlIGEgY29ycmVzcG9uZGVuY2UgYnkgc2VsZWN0aW5nIHRoZSBzdGFycyBpbiB0aGUgdG9wIHJpZ2h0IGNvcm5lciBvZiB0aGUgY29ycmVzcG9uZGVuY2UuPGJyLz48YnIvPkJlc3QgcmVnYXJkcyw8YnIvPk1ydW5hbCAgSy48YnIvPkFtYXpvbiBXZWIgU2VydmljZXM8YnIvPjxici8-DQogICAgICA8L3A-PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09DQogIA0KICA8cD4NCiAgICBUbyBzaGFyZSB5b3VyIGV4cGVyaWVuY2Ugb3IgY29udGFjdCB1cyBhZ2FpbiBhYm91dCB0aGlzIGNhc2UsIHBsZWFzZSByZXR1cm4gdG8gdGhlIEFXUyBTdXBwb3J0IENlbnRlciB1c2luZyB0aGUgZm9sbG93aW5nIFVSTDogPGEgaHJlZj0iaHR0cHM6Ly9rcWh3YjdmdC5yLnVzLWVhc3QtMS5hd3N0cmFjay5tZS9MMC9odHRwczolMkYlMkZjb25zb2xlLmF3cy5hbWF6b24uY29tJTJGc3VwcG9ydCUyRmhvbWUlMjMlMkZjYXNlJTJGJTNGZGlzcGxheUlkPTExNzQ0ODU5MjExJTI2bGFuZ3VhZ2U9ZW4vMS8wMTAwMDE4NWFhMjY2Y2I4LTYxOTIxZGVhLTQ3NmMtNGY0Ny05ZWJhLTg3MzhjMzcwMDYyNi0wMDAwMDAvWHFlYlk4aHVnZTlTbk9FbjVGd2x1cEVtZEo0PTMwNCI-aHR0cHM6Ly9jb25zb2xlLmF3cy5hbWF6b24uY29tL3N1cHBvcnQvaG9tZSMvY2FzZS8_ZGlzcGxheUlkPTExNzQ0ODU5MjExJmFtcDtsYW5ndWFnZT1lbjwvYT4NCiAgPC9wPg0KICA8cD4NCiAgICBOb3RlLCB0aGlzIGUtbWFpbCB3YXMgc2VudCBmcm9tIGFuIGFkZHJlc3MgdGhhdCBjYW5ub3QgYWNjZXB0IGluY29taW5nIGUtbWFpbHMuDQogICAgVG8gcmVzcG9uZCB0byB0aGlzIGNhc2UsIHBsZWFzZSBmb2xsb3cgdGhlIGxpbmsgYWJvdmUgdG8gcmVzcG9uZCBmcm9tIHlvdXIgQVdTIFN1cHBvcnQgQ2VudGVyLg0KICA8L3A-DQogIDxwPg0KICAgID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQ0KICA8L3A-DQogIDxwPg0KICAgIERvbuKAmXQgbWlzcyBtZXNzYWdlcyBmcm9tIEFXUyBTdXBwb3J0IHdoZW4geW91IG5lZWQgaGVscCEgVXBkYXRlIHlvdXIgY29udGFjdCBpbmZvcm1hdGlvbjo8YnIvPg0KICAgIDxhIGhyZWY9Imh0dHBzOi8va3Fod2I3ZnQuci51cy1lYXN0LTEuYXdzdHJhY2subWUvTDAvaHR0cHM6JTJGJTJGY29uc29sZS5hd3MuYW1hem9uLmNvbSUyRmJpbGxpbmclMkZob21lJTIzJTJGYWNjb3VudC8xLzAxMDAwMTg1YWEyNjZjYjgtNjE5MjFkZWEtNDc2Yy00ZjQ3LTllYmEtODczOGMzNzAwNjI2LTAwMDAwMC8yM05ZSVh2QUMtQUY0Tm5mNWI0VjNHYzJSS1E9MzA0Ij5odHRwczovL2NvbnNvbGUuYXdzLmFtYXpvbi5jb20vYmlsbGluZy9ob21lIy9hY2NvdW50PC9hPg0KICA8L3A-DQogIDxwPg0KICAgIElmIHlvdSByZWNlaXZlIGFuIGVycm9yIG1lc3NhZ2Ugd2hlbiB2aXNpdGluZyB0aGUgY29udGFjdCBpbmZvcm1hdGlvbiBwYWdlLCB2aXNpdDo8YnIvPg0KICAgIDxhIGhyZWY9Imh0dHBzOi8va3Fod2I3ZnQuci51cy1lYXN0LTEuYXdzdHJhY2subWUvTDAvaHR0cHM6JTJGJTJGYXdzLmFtYXpvbi5jb20lMkZwcmVtaXVtc3VwcG9ydCUyRmtub3dsZWRnZS1jZW50ZXIlMkZpYW0tYmlsbGluZy1hY2Nlc3MlMkYvMS8wMTAwMDE4NWFhMjY2Y2I4LTYxOTIxZGVhLTQ3NmMtNGY0Ny05ZWJhLTg3MzhjMzcwMDYyNi0wMDAwMDAvYWl0T2ZBVVlHZHFoVUVZZEd5d3dUTzk2eUVZPTMwNCI-aHR0cHM6Ly9hd3MuYW1hem9uLmNvbS9wcmVtaXVtc3VwcG9ydC9rbm93bGVkZ2UtY2VudGVyL2lhbS1iaWxsaW5nLWFjY2Vzcy88L2E-DQogIDwvcD4NCiAgPHA-DQogICAgQVdTIFN1cHBvcnQ6PGJyLz4NCiAgICA8YSBocmVmPSJodHRwczovL2txaHdiN2Z0LnIudXMtZWFzdC0xLmF3c3RyYWNrLm1lL0wwL2h0dHBzOiUyRiUyRmF3cy5hbWF6b24uY29tJTJGcHJlbWl1bXN1cHBvcnQlMkZrbm93bGVkZ2UtY2VudGVyJTJGLzEvMDEwMDAxODVhYTI2NmNiOC02MTkyMWRlYS00NzZjLTRmNDctOWViYS04NzM4YzM3MDA2MjYtMDAwMDAwL25Rb2Rjbmt6RFNJa2JReWVneURHb0VGWEFwMD0zMDQiPmh0dHBzOi8vYXdzLmFtYXpvbi5jb20vcHJlbWl1bXN1cHBvcnQva25vd2xlZGdlLWNlbnRlci88L2E-DQogIDwvcD4NCiAgPHA-DQogICAgQVdTIERvY3VtZW50YXRpb246PGJyLz4NCiAgICA8YSBocmVmPSJodHRwczovL2txaHdiN2Z0LnIudXMtZWFzdC0xLmF3c3RyYWNrLm1lL0wwL2h0dHBzOiUyRiUyRmRvY3MuYXdzLmFtYXpvbi5jb20lMkYvMS8wMTAwMDE4NWFhMjY2Y2I4LTYxOTIxZGVhLTQ3NmMtNGY0Ny05ZWJhLTg3MzhjMzcwMDYyNi0wMDAwMDAvWTNubFRJRGZ1WG9TUy1DWldsbnN1UFZ4SkhrPTMwNCI-aHR0cHM6Ly9kb2NzLmF3cy5hbWF6b24uY29tLzwvYT4NCiAgPC9wPg0KICA8cD4NCiAgICBBV1MgQ29zdCBNYW5hZ2VtZW50Ojxici8-DQogICAgPGEgaHJlZj0iaHR0cHM6Ly9rcWh3YjdmdC5yLnVzLWVhc3QtMS5hd3N0cmFjay5tZS9MMC9odHRwczolMkYlMkZhd3MuYW1hem9uLmNvbSUyRmF3cy1jb3N0LW1hbmFnZW1lbnQlMkYvMS8wMTAwMDE4NWFhMjY2Y2I4LTYxOTIxZGVhLTQ3NmMtNGY0Ny05ZWJhLTg3MzhjMzcwMDYyNi0wMDAwMDAvai1WaFhRNkN6d0puZVFTTHBmM3E2SmoxRHJBPTMwNCI-aHR0cHM6Ly9hd3MuYW1hem9uLmNvbS9hd3MtY29zdC1tYW5hZ2VtZW50LzwvYT4NCiAgPC9wPg0KICA8cD4NCiAgICBBV1MgVHJhaW5pbmc6PGJyLz4NCiAgICA8YSBocmVmPSJodHRwOi8va3Fod2I3ZnQuci51cy1lYXN0LTEuYXdzdHJhY2subWUvTDAvaHR0cDolMkYlMkZhd3MuYW1hem9uLmNvbSUyRnRyYWluaW5nJTJGLzEvMDEwMDAxODVhYTI2NmNiOC02MTkyMWRlYS00NzZjLTRmNDctOWViYS04NzM4YzM3MDA2MjYtMDAwMDAwL1JrczdoYzR0blRsTjFsWEhkZWViZ1ItZ0V3WT0zMDQiPmh0dHA6Ly9hd3MuYW1hem9uLmNvbS90cmFpbmluZy88L2E-DQogIDwvcD4NCiAgPHA-DQogICAgQVdTIE1hbmFnZWQgU2VydmljZXM6PGJyLz4NCiAgICA8YSBocmVmPSJodHRwczovL2txaHdiN2Z0LnIudXMtZWFzdC0xLmF3c3RyYWNrLm1lL0wwL2h0dHBzOiUyRiUyRmF3cy5hbWF6b24uY29tJTJGbWFuYWdlZC1zZXJ2aWNlcyUyRi8xLzAxMDAwMTg1YWEyNjZjYjgtNjE5MjFkZWEtNDc2Yy00ZjQ3LTllYmEtODczOGMzNzAwNjI2LTAwMDAwMC9rakJFcjZ4NFBiLVJWbTN1SnF6U2ltcHZzQ0U9MzA0Ij5odHRwczovL2F3cy5hbWF6b24uY29tL21hbmFnZWQtc2VydmljZXMvPC9hPg0KICA8cD48aW1nIGFsdD0iIiBzcmM9Imh0dHBzOi8va3Fod2I3ZnQuci51cy1lYXN0LTEuYXdzdHJhY2subWUvSTAvMDEwMDAxODVhYTI2NmNiOC02MTkyMWRlYS00NzZjLTRmNDctOWViYS04NzM4YzM3MDA2MjYtMDAwMDAwL2IzeEJoV0pEdjViQjI0U1ZkZkVUcEQzQk9sND0zMDQiIHN0eWxlPSJkaXNwbGF5OiBub25lOyB3aWR0aDogMXB4OyBoZWlnaHQ6IDFweDsiPg0K"
            }
          }
        ]
      },
      "sizeEstimate": 12673,
      "historyId": "322935",
      "internalDate": "1673596923000"
    },
    {
      "id": "185af8cdc323cae4",
      "threadId": "185aa2672fce2c43",
      "labelIds": [
        "UNREAD",
        "IMPORTANT",
        "CATEGORY_UPDATES",
        "INBOX"
      ],
      "snippet": "Hello Mahendra, Thank you so much for your continued patience. In order to understand the scenario I tried replicating this at my end. You were able to perform the migration successfully for 2/4",
      "payload": {
        "partId": "",
        "mimeType": "multipart/alternative",
        "filename": "",
        "headers": [
          {
            "name": "Delivered-To",
            "value": "mahendra@spiceblue.co"
          },
          {
            "name": "Received",
            "value": "by 2002:a05:6a10:dba7:b0:361:1249:b4ae with SMTP id uv39csp204343pxb;        Sat, 14 Jan 2023 01:12:02 -0800 (PST)"
          },
          {
            "name": "X-Google-Smtp-Source",
            "value": "AMrXdXsr7S1/stJ23tbWaJUiU3fy08sMq20BJqzPcTWMtbI9XU2oNPgG3FNvBUmvcajBTStsKaes"
          },
          {
            "name": "X-Received",
            "value": "by 2002:ac8:7957:0:b0:3ad:903d:3ed4 with SMTP id r23-20020ac87957000000b003ad903d3ed4mr27761611qtt.59.1673687522753;        Sat, 14 Jan 2023 01:12:02 -0800 (PST)"
          },
          {
            "name": "ARC-Seal",
            "value": "i=1; a=rsa-sha256; t=1673687522; cv=none;        d=google.com; s=arc-20160816;        b=kQmjvXVUn1qJuiwX+G27tAzdIIIVbKI4KukenB9lneTm53HgSrJYab5w79p5yugd5h         6XjGtcg/q8YFWf9dOaYRURhur/JNXx3YmO+Zupw1vJeiU1bAexqw8t8kVpf+WHjt7Ek4         fr65nQ7wslM4Ej0xzP46UVApK0TiYpaCI1Yn3+gz1n85LCpYwRzc87Q3FdZAVSnDVmkG         25V9P+lHzJXgoZSQqtsIIS8aDY2KUdDTQiQ4QBbrq9pfC8i4pvBYy+FuW2zMKv3Ssz+q         cLLD9Z5CahRvG8yKtI4axE5R1iwAgeY5e9HWfV2XqH3mpNY7GGXWDmxLMx660atEgQNW         TgWw=="
          },
          {
            "name": "ARC-Message-Signature",
            "value": "i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;        h=feedback-id:date:message-id:mime-version:subject:cc:to:from         :dkim-signature:dkim-signature;        bh=zZd4QKGHJbIFUh55bLN/dw7J56uVztaC7CMUuLt3RDA=;        b=Uu5nNu2fa8L9bEJbMiGaTNo6vqte2Gbl0Z+HXuzyCxGt5EIeEwhmWXnKlUlGI+BIdH         5jmKW2yKB5YYi6IaL+lWQoqXS/9CDU95rslFuxA0SRi5XiaG9ulOJCrL+lSwlrqQb5me         aWbUsM6/ycWdPrMmf9nJForMCLAmbIULBUG8GOoyxo5L1YzE8+wqNmlo4NV6XTYzO01l         tBof8O33Fr2CpPN7APVon1AMDFcYlvLXg/v13WhasgstKvtrfVFEobNu9dhQE3tJYxQI         jPxq9iBkGhEQDprwn2wv5OG5A87CFbZjAXG6hLpeFzqp+NU08HozkdPoNBgcaZBVcUVw         3sAw=="
          },
          {
            "name": "ARC-Authentication-Results",
            "value": "i=1; mx.google.com;       dkim=pass header.i=@amazon.com header.s=benmzc5omgrgqjsu3tg2d2m7nez6lzho header.b=MgOmU0Wu;       dkim=pass header.i=@amazonses.com header.s=6gbrjpgwjskckoa6a5zn6fwqkn67xbtw header.b=JzJHLAhW;       spf=pass (google.com: domain of 01000185af8cd940-2d25a5be-7c93-434a-9fca-7d0554172324-000000@amazonses.com designates 54.240.11.31 as permitted sender) smtp.mailfrom=01000185af8cd940-2d25a5be-7c93-434a-9fca-7d0554172324-000000@amazonses.com;       dmarc=pass (p=QUARANTINE sp=QUARANTINE dis=NONE) header.from=amazon.com"
          },
          {
            "name": "Return-Path",
            "value": "<01000185af8cd940-2d25a5be-7c93-434a-9fca-7d0554172324-000000@amazonses.com>"
          },
          {
            "name": "Received",
            "value": "from a11-31.smtp-out.amazonses.com (a11-31.smtp-out.amazonses.com. [54.240.11.31])        by mx.google.com with ESMTPS id i10-20020ac813ca000000b003a5f9a090easi13580210qtj.182.2023.01.14.01.12.02        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-GCM-SHA256 bits=128/128);        Sat, 14 Jan 2023 01:12:02 -0800 (PST)"
          },
          {
            "name": "Received-SPF",
            "value": "pass (google.com: domain of 01000185af8cd940-2d25a5be-7c93-434a-9fca-7d0554172324-000000@amazonses.com designates 54.240.11.31 as permitted sender) client-ip=54.240.11.31;"
          },
          {
            "name": "Authentication-Results",
            "value": "mx.google.com;       dkim=pass header.i=@amazon.com header.s=benmzc5omgrgqjsu3tg2d2m7nez6lzho header.b=MgOmU0Wu;       dkim=pass header.i=@amazonses.com header.s=6gbrjpgwjskckoa6a5zn6fwqkn67xbtw header.b=JzJHLAhW;       spf=pass (google.com: domain of 01000185af8cd940-2d25a5be-7c93-434a-9fca-7d0554172324-000000@amazonses.com designates 54.240.11.31 as permitted sender) smtp.mailfrom=01000185af8cd940-2d25a5be-7c93-434a-9fca-7d0554172324-000000@amazonses.com;       dmarc=pass (p=QUARANTINE sp=QUARANTINE dis=NONE) header.from=amazon.com"
          },
          {
            "name": "DKIM-Signature",
            "value": "v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple; s=benmzc5omgrgqjsu3tg2d2m7nez6lzho; d=amazon.com; t=1673687521; h=From:To:Cc:Subject:MIME-Version:Content-Type:Message-ID:Date; bh=rofE5BWjiUhrKZpRwZBox2OTpqzMcPGVUnpTC5jd3bA=; b=MgOmU0Wu/Z0teJD5lrgE/gjmPi4VjGmIfee1FtfOVlZyurwkXhmjwCJ0wkkmEaEJ kPkGnLoPs5kKLI/2TMqTS1Vs8eaPoX93qLWHYlkogFVZmz8jGYbCKAOUGb0G3e/6I10 FPQIwYCtGmd1WcAn7s+mizD60rfCsNM1034ZwTmM="
          },
          {
            "name": "DKIM-Signature",
            "value": "v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple; s=6gbrjpgwjskckoa6a5zn6fwqkn67xbtw; d=amazonses.com; t=1673687521; h=From:To:Cc:Subject:MIME-Version:Content-Type:Message-ID:Date:Feedback-ID; bh=rofE5BWjiUhrKZpRwZBox2OTpqzMcPGVUnpTC5jd3bA=; b=JzJHLAhWo/NhsFXMBGeLMS/t4LPLSEIHldjzvyVkb/frQw11DsNqozRXvOFhyo8Q 34QeFkh/JqBhDOgPm4JPENcxNoUlwBARRTbPM2zXPtjOX5+4Cr0bEIXqbdoW5CftvLR b6addz/XXIHl/8UsGkdhRVYMn2VTzuIEsxjiD98A="
          },
          {
            "name": "From",
            "value": "Amazon Web Services <no-reply-aws@amazon.com>"
          },
          {
            "name": "To",
            "value": "prem@spiceblue.co"
          },
          {
            "name": "Cc",
            "value": "mahendra@spiceblue.co"
          },
          {
            "name": "Subject",
            "value": "RE:[CASE 11744859211] Chat: Restore Snapshot"
          },
          {
            "name": "MIME-Version",
            "value": "1.0"
          },
          {
            "name": "Content-Type",
            "value": "multipart/alternative; boundary='----=_Part_1737370_110369069.1673687521604'"
          },
          {
            "name": "Message-ID",
            "value": "<01000185af8cd940-2d25a5be-7c93-434a-9fca-7d0554172324-000000@email.amazonses.com>"
          },
          {
            "name": "Date",
            "value": "Sat, 14 Jan 2023 09:12:01 +0000"
          },
          {
            "name": "Feedback-ID",
            "value": "1.us-east-1.huE3KBUlbB3jXEGPu3NtaNXYRdURNu75MKOqRLEVhr4=:AmazonSES"
          },
          {
            "name": "X-SES-Outgoing",
            "value": "2023.01.14-54.240.11.31"
          }
        ],
        "body": {
          "size": 0
        },
        "parts": [
          {
            "partId": "0",
            "mimeType": "text/plain",
            "filename": "",
            "headers": [
              {
                "name": "Content-Type",
                "value": "text/plain; charset=UTF-8"
              },
              {
                "name": "Content-Transfer-Encoding",
                "value": "quoted-printable"
              }
            ],
            "body": {
              "size": 11478,
              "data": "SGVsbG8gTWFoZW5kcmEsDQoNClRoYW5rIHlvdSBzbyBtdWNoIGZvciB5b3VyIGNvbnRpbnVlZCBwYXRpZW5jZS4NCg0KSW4gb3JkZXIgdG8gdW5kZXJzdGFuZCB0aGUgc2NlbmFyaW8gSSB0cmllZCByZXBsaWNhdGluZyB0aGlzIGF0IG15IGVuZC4NCg0KWW91IHdlcmUgYWJsZSB0byBwZXJmb3JtIHRoZSBtaWdyYXRpb24gc3VjY2Vzc2Z1bGx5IGZvciAyLzQgZG9tYWlucyBhbmQgZmFjaW5nIGlzc3VlIHdpdGggdGhlIG90aGVyIHR3by4gSSB3b3VsZCByZXF1ZXN0IHlvdSB0byBnbyB0aHJvdWdoIHRoZSBzdGVwcyBmb3IgdGhlIGRvbWFpbnMgeW91IGFyZSBmYWNpbmcgdGhlIGlzc3VlIHdpdGguIEJlbG93IGFyZSB0aGUgZGV0YWlsZWQgc3RlcHMgZm9yIHRoZSBPcGVuc2VhcmNoIHNuYXBzaG90IG1pZ3JhdGlvbi4gDQoNCklmIHRoZSBwcm9ibGVtIHN0aWxsIHBlcnNpc3RzLCBwbGVhc2UgZmVlbCBmcmVlIHRvIHJlYWNoIGJhY2sgdG8gdXMgYW5kIHdlIHdpbGwgYmUgZ2xhZCB0byBhc3Npc3QgeW91IGZ1cnRoZXIuDQoNCktpbmRseSBsZXQgbWUga25vdyBhYm91dCB5b3VyIGF2YWlsYWJpbGl0eSBzbyB3ZSBjYW4gc2V0IHVwIGEgbWVldGluZy4gUGxlYXNlIG5vdGUgdGhhdCBteSBjdXJyZW50IHNoaWZ0IGlzIGZyb20gTW9uZGF5IHRvIEZyaWRheSAwNC4wMCBhbSB0byAxMC4zMGFtIFVUQyBhbmQgaWYgaW4gY2FzZSB5b3UgcmVxdWlyZSBhbnkgaW1tZWRpYXRlIGFzc2lzdGFuY2UgZHVyaW5nIG15IG9mZi1zaGlmdCBob3VycyBmZWVsIGZyZWUgdG8gcmFpc2UgYSBjaGF0L2NhbGwgYW5kIGFuIGVuZ2luZWVyIGZyb20gT3BlbnNlYXJjaCB0ZWFtIHdpbGwgYmUgaGFwcHkgdG8gYXNzaXN0IHlvdS4NCg0KPT09PVJFUExJQ0FUSU9OIFNURVBTPT09PQ0KDQoxLiBDcmVhdGVkIGEgRkdBQyBlbmFibGVkIEFtYXpvbiBPcGVuc2VhcmNoIGNsdXN0ZXIgaW4gYWNjb3VudCBBLg0KMi4gQ3JlYXRlZCBhbiBTMyBidWNrZXQgaW4gYWNjb3VudCBBLg0KMy4gQ3JlYXRlZCBhbm90aGVyIEZHQUMgZW5hYmxlZCBBbWF6b24gT3BlbnNlYXJjaCBjbHVzdGVyIGluIGFjY291bnQgQi4NCjQuIENyZWF0ZWQgb25lIGVjMiBpbnN0YW5jZSBpbiBlYWNoIEFXUyBhY2NvdW50IHRvIHJlZ2lzdGVyIHRoZSBzbmFwc2hvdCByZXBvc2l0b3J5Lg0KDQotLS0tLS1QcmUtcmVxdWlzaXRlcy0tLS0tLS0NCg0KQmVsb3cgYXJlIHRoZSBwcmVyZXF1aXNpdGVzIHRvIGZvbGxvdyB3aGlsZSByZXN0b3Jpbmcgc25hcHNob3Qgb2YgQWNjb3VudCBBIE9wZW5TZWFyY2ggZG9tYWluIGZyb20gQWNjb3VudCBBIFMzIHRvIEFjY291bnQgQiBPcGVuc2VhcmNoIGRvbWFpbjoNCg0KU3RlcCAxOiBDcmVhdGUgXCJTM1NuYXBzaG90UG9saWN5XCIgaW4gQWNjb3VudCBBDQoNCnsNCiAgICBcIlZlcnNpb25cIjogXCIyMDEyLTEwLTE3XCIsDQogICAgXCJTdGF0ZW1lbnRcIjogWw0KICAgICAgICB7DQogICAgICAgICAgICBcIkFjdGlvblwiOiBbDQogICAgICAgICAgICAgICAgXCJzMzpMaXN0QnVja2V0XCINCiAgICAgICAgICAgIF0sDQogICAgICAgICAgICBcIkVmZmVjdFwiOiBcIkFsbG93XCIsDQogICAgICAgICAgICBcIlJlc291cmNlXCI6IFsNCiAgICAgICAgICAgICAgICBcImFybjphd3M6czM6Ojo8czMtQnVja2V0LW5hbWUtb2YtYWNjb3VudC1BPlwiDQogICAgICAgICAgICBdDQogICAgICAgIH0sDQogICAgICAgIHsNCiAgICAgICAgICAgIFwiQWN0aW9uXCI6IFsNCiAgICAgICAgICAgICAgICBcInMzOkdldE9iamVjdFwiLA0KICAgICAgICAgICAgICAgIFwiczM6UHV0T2JqZWN0XCIsDQogICAgICAgICAgICAgICAgXCJzMzpEZWxldGVPYmplY3RcIg0KICAgICAgICAgICAgXSwNCiAgICAgICAgICAgIFwiRWZmZWN0XCI6IFwiQWxsb3dcIiwNCiAgICAgICAgICAgIFwiUmVzb3VyY2VcIjogWw0KICAgICAgICAgICAgICAgIFwiYXJuOmF3czpzMzo6OjxzMy1CdWNrZXQtbmFtZS1vZi1hY2NvdW50LUE-L1wiDQogICAgICAgICAgICBdDQogICAgICAgIH0NCiAgICBdDQp9DQoNClN0ZXAgMjogQ3JlYXRlIFwiVGhlU25hcHNob3RSb2xlXCIgaW4gQWNjb3VudCBBIGFuZCBhdHRhY2ggdGhlIGFib3ZlIHBvbGljeSB0byB0aGF0IHJvbGUgYW5kIGVkaXQgdHJ1c3QgcmVsYXRpb25zaGlwIGFzIGJlbG93Og0KDQp7DQogIFwiVmVyc2lvblwiOiBcIjIwMTItMTAtMTdcIiwNCiAgXCJTdGF0ZW1lbnRcIjogWw0KICAgIHsNCiAgICAgIFwiU2lkXCI6IFwiXCIsDQogICAgICBcIkVmZmVjdFwiOiBcIkFsbG93XCIsDQogICAgICBcIlByaW5jaXBhbFwiOiB7DQogICAgICAgIFwiU2VydmljZVwiOiBcImVzLmFtYXpvbmF3cy5jb20gKGh0dHA6Ly9lcy5hbWF6b25hd3MuY29tLykgIOKAnA0KICAgICAgfSwNCiAgICAgIFwiQWN0aW9uXCI6IFwic3RzOkFzc3VtZVJvbGVcIg0KICAgIH0NCiAgXQ0KfQ0KDQpTdGVwIDM6IENyZWF0ZSBhbiBJQU0gUm9sZSBmb3IgRUMyIHdpdGggYmVsb3cgcG9saWN5IGFuZCB0cnVzdCByZWxhdGlvbnNoaXAgdG8gYWNjZXNzIHRoZSBvcGVuc2VhcmNoIGRvbWFpbiBhbmQgUzMgYnVja2V0IGZvciBtYW51YWwgc25hcHNob3Q6DQoNCuKGkiBJQU0gUG9saWN5DQoNCnsNCiAgICBcIlZlcnNpb25cIjogXCIyMDEyLTEwLTE3XCIsDQogICAgXCJTdGF0ZW1lbnRcIjogWw0KICAgICAgICB7DQogICAgICAgICAgICBcIkVmZmVjdFwiOiBcIkFsbG93XCIsDQogICAgICAgICAgICBcIkFjdGlvblwiOiBcImlhbTpQYXNzUm9sZVwiLA0KICAgICAgICAgICAgXCJSZXNvdXJjZVwiOiBcImFybjphd3M6aWFtOjo8QWNjb3VudC1BLW51bWJlcj46cm9sZS9UaGVTbmFwc2hvdFJvbGVcIg0KICAgICAgICB9LA0KICAgICAgICB7DQogICAgICAgICAgICBcIkVmZmVjdFwiOiBcIkFsbG93XCIsDQogICAgICAgICAgICBcIkFjdGlvblwiOiBcImVzOkVTSHR0cFB1dFwiLA0KICAgICAgICAgICAgXCJSZXNvdXJjZVwiOiBcImFybjphd3M6ZXM6dXMtZWFzdC0xOjxBY2NvdW50LUEtbnVtYmVyPjpkb21haW4vdGVzdC1kb21haW4tYS9cIg0KICAgICAgICB9DQogICAgXQ0KfQ0KDQrihpIgVHJ1c3QgUmVsYXRpb25zaGlwDQoNCnsNCiAgXCJWZXJzaW9uXCI6IFwiMjAxMi0xMC0xN1wiLA0KICBcIlN0YXRlbWVudFwiOiBbDQogICAgew0KICAgICAgXCJFZmZlY3RcIjogXCJBbGxvd1wiLA0KICAgICAgXCJQcmluY2lwYWxcIjogew0KICAgICAgICBcIlNlcnZpY2VcIjogXCJlYzIuYW1hem9uYXdzLmNvbSAoaHR0cDovL2VjMi5hbWF6b25hd3MuY29tLykgIOKAnA0KICAgICAgfSwNCiAgICAgIFwiQWN0aW9uXCI6IFwic3RzOkFzc3VtZVJvbGVcIg0KICAgIH0NCiAgXQ0KfQ0KDQpTdGVwIDQ6IFJlcGVhdCB0aGUgYWJvdmUgc3RlcHMgaW4gQWNjb3VudCBCLCBidXQgZG8gcmVtZW1iZXIgdGhhdCB0aGUgXCJTM1NuYXBzaG90UG9saWN5XCIgd2lsbCByZW1haW4gc2FtZSBhcyB3ZSB3YW50IHRvIHVzZSBTMyBidWNrZXQgb2YgQWNjb3VudCBBIGluIEFjY291bnQgQi4NCg0KYSkgQWNjb3VudCBCIFwiUzNTbmFwc2hvdFBvbGljeVwiDQoNCnsNCiAgICBcIlZlcnNpb25cIjogXCIyMDEyLTEwLTE3XCIsDQogICAgXCJTdGF0ZW1lbnRcIjogWw0KICAgICAgICB7DQogICAgICAgICAgICBcIkFjdGlvblwiOiBbDQogICAgICAgICAgICAgICAgXCJzMzpMaXN0QnVja2V0XCINCiAgICAgICAgICAgIF0sDQogICAgICAgICAgICBcIkVmZmVjdFwiOiBcIkFsbG93XCIsDQogICAgICAgICAgICBcIlJlc291cmNlXCI6IFsNCiAgICAgICAgICAgICAgICBcImFybjphd3M6czM6Ojo8czMtQnVja2V0LW5hbWUtb2YtYWNjb3VudC1BPlwiDQogICAgICAgICAgICBdDQogICAgICAgIH0sDQogICAgICAgIHsNCiAgICAgICAgICAgIFwiQWN0aW9uXCI6IFsNCiAgICAgICAgICAgICAgICBcInMzOkdldE9iamVjdFwiLA0KICAgICAgICAgICAgICAgIFwiczM6UHV0T2JqZWN0XCIsDQogICAgICAgICAgICAgICAgXCJzMzpEZWxldGVPYmplY3RcIg0KICAgICAgICAgICAgXSwNCiAgICAgICAgICAgIFwiRWZmZWN0XCI6IFwiQWxsb3dcIiwNCiAgICAgICAgICAgIFwiUmVzb3VyY2VcIjogWw0KICAgICAgICAgICAgICAgIFwiYXJuOmF3czpzMzo6OjxzMy1CdWNrZXQtbmFtZS1vZi1hY2NvdW50LUE-L1wiDQogICAgICAgICAgICBdDQogICAgICAgIH0NCiAgICBdDQp9DQoNCmIpIEFjY291bnQgQiBcIlRoZVNuYXBzaG90Um9sZVwiIHdpdGggYWJvdmUgcG9saWN5IGFuZCB0cnVzdCByZWxhdGlvbnNoaXAgYXMgYmVsb3c6DQoNCnsNCiAgXCJWZXJzaW9uXCI6IFwiMjAxMi0xMC0xN1wiLA0KICBcIlN0YXRlbWVudFwiOiBbDQogICAgew0KICAgICAgXCJTaWRcIjogXCJcIiwNCiAgICAgIFwiRWZmZWN0XCI6IFwiQWxsb3dcIiwNCiAgICAgIFwiUHJpbmNpcGFsXCI6IHsNCiAgICAgICAgXCJTZXJ2aWNlXCI6IFwiZXMuYW1hem9uYXdzLmNvbSAoaHR0cDovL2VzLmFtYXpvbmF3cy5jb20vKSAg4oCcDQogICAgICB9LA0KICAgICAgXCJBY3Rpb25cIjogXCJzdHM6QXNzdW1lUm9sZVwiDQogICAgfQ0KICBdDQp9DQoNCmMpIEFjY291bnQgQjogRUMyIEluc3RhbmNlIElBTSBSb2xlIHdpdGggYmVsb3cgcG9saWN5IGFuZCB0cnVzdCByZWxhdGlvbnNoaXAgdG8gYWNjZXNzIHRoZSBTMyBCdWNrZXQgYW5kIHRoZSBPcGVuc2VhcmNoIGRvbWFpbiBpbiBBY2NvdW50IEI6DQrihpIgSUFNIFBvbGljeQ0KDQp7DQogICAgXCJWZXJzaW9uXCI6IFwiMjAxMi0xMC0xN1wiLA0KICAgIFwiU3RhdGVtZW50XCI6IFsNCiAgICAgICAgew0KICAgICAgICAgICAgXCJFZmZlY3RcIjogXCJBbGxvd1wiLA0KICAgICAgICAgICAgXCJBY3Rpb25cIjogXCJpYW06UGFzc1JvbGVcIiwNCiAgICAgICAgICAgIFwiUmVzb3VyY2VcIjogXCJhcm46YXdzOmlhbTo6PEFjY291bnQtQi1udW1iZXI-OnJvbGUvVGhlU25hcHNob3RSb2xlXCINCiAgICAgICAgfSwNCiAgICAgICAgew0KICAgICAgICAgICAgXCJFZmZlY3RcIjogXCJBbGxvd1wiLA0KICAgICAgICAgICAgXCJBY3Rpb25cIjogXCJlczpFU0h0dHBQdXRcIiwNCiAgICAgICAgICAgIFwiUmVzb3VyY2VcIjogXCJhcm46YXdzOmVzOnVzLWVhc3QtMTo8QWNjb3VudC1CLW51bWJlcj46ZG9tYWluL3Rlc3QtZG9tYWluLWIvXCINCiAgICAgICAgfQ0KICAgIF0NCn0NCg0K4oaSIFRydXN0IFJlbGF0aW9uc2hpcA0KDQp7DQogIFwiVmVyc2lvblwiOiBcIjIwMTItMTAtMTdcIiwNCiAgXCJTdGF0ZW1lbnRcIjogWw0KICAgIHsNCiAgICAgIFwiRWZmZWN0XCI6IFwiQWxsb3dcIiwNCiAgICAgIFwiUHJpbmNpcGFsXCI6IHsNCiAgICAgICAgXCJTZXJ2aWNlXCI6IFwiZWMyLmFtYXpvbmF3cy5jb20gKGh0dHA6Ly9lYzIuYW1hem9uYXdzLmNvbS8pICDigJwNCiAgICAgIH0sDQogICAgICBcIkFjdGlvblwiOiBcInN0czpBc3N1bWVSb2xlXCINCiAgICB9DQogIF0NCn0NCg0KU3RlcCA1OiBUaGUgRmluYWwgc3RlcCB3aWxsIGFsbG93IGFjY2VzcyBmcm9tIEFjY291bnQgQiB0byBBY2NvdW50IEEgUzMgYnVja2V0Og0KDQrihpIgRWRpdCBBY2NvdW50IEEgUzMgQnVja2V0IGFjY2VzcyBwb2xpY3k6DQoNCnsNCiAgICBcIlZlcnNpb25cIjogXCIyMDEyLTEwLTE3XCIsDQogICAgXCJJZFwiOiBcIlBvbGljeTE1NjgwMDEwMTA3NDZcIiwNCiAgICBcIlN0YXRlbWVudFwiOiBbDQogICAgICAgIHsNCiAgICAgICAgICAgIFwiU2lkXCI6IFwiU3RtdDE1NjgwMDA3MTI1MzFcIiwNCiAgICAgICAgICAgIFwiRWZmZWN0XCI6IFwiQWxsb3dcIiwNCiAgICAgICAgICAgIFwiUHJpbmNpcGFsXCI6IHsNCiAgICAgICAgICAgICAgICBcIkFXU1wiOiBcImFybjphd3M6aWFtOjo8QWNjb3VudC1CLW51bWJlcj46cm9sZS9UaGVTbmFwc2hvdFJvbGVcIg0KICAgICAgICAgICAgfSwNCiAgICAgICAgICAgIFwiQWN0aW9uXCI6IFwiczM6XCIsDQogICAgICAgICAgICBcIlJlc291cmNlXCI6IFsNCiAgICAgICAgICAgICAgICBcImFybjphd3M6czM6Ojo8czMtQnVja2V0LW5hbWUtb2YtYWNjb3VudC1BPlwiLA0KICAgICAgICAgICAgICAgIFwiYXJuOmF3czpzMzo6OjxzMy1CdWNrZXQtbmFtZS1vZi1hY2NvdW50LUE-L1wiDQogICAgICAgICAgICBdDQogICAgICAgIH0NCiAgICBdDQp9DQoNCj09Tm93IG1vdmluZyB0byB0aGUgcmVnaXN0ZXIgc25hcHNob3QgcmVwb3NpdG9yeSBzdGVwczo9PQ0KDQpGcm9tIEFjY291bnQgQSAtDQotLS0tLS0tLS0tLS0tLS0tLS0tLS0NClN0ZXAgMSAtICBMYXVuY2ggYW4gRUMyIGluc3RhbmNlIGFuZCB0dGFjaCBJQU0gUm9sZSBjcmVhdGVkIGZvciBFQzIgaW4gc3RlcCAzIG9mIHByZXJlcXVpc2l0ZXMuDQoNClN0ZXAgMiAtIE1hcHBlZCB0aGUgSUFNIHJvbGUgXCJBbWF6b25PcGVuU2VhcmNoU2VydmljZVNuYXBzaG90c1wiIHRvICdhbGxfYWNjZXNzJyBhbmQgJ21hbmFnZV9zbmFwc2hvdHMnIGFzIGJhY2tlbmQgcm9sZSBpbiBPcGVuc2VhcmNoIERhc2hvYm9hcmRzIFNlY3VyaXR5IHNldHRpbmdzDQoNClN0ZXAgMyAtIFJlZ2lzdGVyIFNuYXBzaG90IHJlcG9zaXRvcnkgb2YgQWNjb3VudCBBIE9wZW5zZWFyY2ggZG9tYWluIGluIFMzIGJ1Y2tldCB1c2luZyBJQU0gcm9sZSBjcmVhdGVkIGluIHN0ZXAgMi4NCg0KSSBoYXZlIHVzZWQgYmVsb3cgcHl0aG9uIHNjcmlwdCB0byByZWdpc3RlciBTMyBzbmFwc2hvdCByZXBvc2l0b3J5IGZvciBtYW51YWwgc25hcHNob3RzOg0KPT09PT09PT09PT09PT09PT09PT09PT09PT0NCiQgY2F0IGVzLXNuYXBzaG90LnB5ICANCg0KaW1wb3J0IGJvdG8zDQppbXBvcnQgcmVxdWVzdHMNCmZyb20gcmVxdWVzdHNfYXdzNGF1dGggaW1wb3J0IEFXUzRBdXRoDQoNCmhvc3QgPSAnJyAjIGluY2x1ZGUgaHR0cHM6Ly8gYW5kIHRyYWlsaW5nIC8NCnJlZ2lvbiA9ICd1cy1lYXN0LTEnICMgZS5nLiB1cy13ZXN0LTENCnNlcnZpY2UgPSAnZXMnDQpjcmVkZW50aWFscyA9IGJvdG8zLlNlc3Npb24oKS5nZXRfY3JlZGVudGlhbHMoKQ0KYXdzYXV0aCA9IEFXUzRBdXRoKGNyZWRlbnRpYWxzLmFjY2Vzc19rZXksIGNyZWRlbnRpYWxzLnNlY3JldF9rZXksIHJlZ2lvbiwgc2VydmljZSwgc2Vzc2lvbl90b2tlbj1jcmVkZW50aWFscy50b2tlbikNCg0KI1JlZ2lzdGVyIHJlcG9zaXRvcnkNCg0KcGF0aCA9ICdfc25hcHNob3QvbXktc25hcHNob3QtcmVwbycgIyB0aGUgRWxhc3RpY3NlYXJjaCBBUEkgZW5kcG9pbnQNCnVybCA9IGhvc3QgKyBwYXRoDQoNCnBheWxvYWQgPSB7DQogIFwidHlwZVwiOiBcInMzXCIsDQogIFwic2V0dGluZ3NcIjogew0KICAgIFwiYnVja2V0XCI6IFwiPFMzLWJ1Y2tldC1uYW1lLWluLWFjY291bnQtQT5cIiwNCiAgICBcInJlZ2lvblwiOiBcInVzLWVhc3QtMVwiLA0KICAgIFwiYmFzZV9wYXRoXCI6IFwiZXNfc25hcHNob3RzXCIsDQogICAgXCJyb2xlX2FyblwiOiBcImFybjphd3M6aWFtOjo8YWNjb3VudC1BLW51bWJlcj46cm9sZS9UaGVTbmFwc2hvdFJvbGVcIg0KICB9DQp9DQoNCmhlYWRlcnMgPSB7XCJDb250ZW50LVR5cGVcIjogXCJhcHBsaWNhdGlvbi9qc29uXCJ9DQoNCnIgPSByZXF1ZXN0cy5wdXQodXJsLCBhdXRoPWF3c2F1dGgsIGpzb249cGF5bG9hZCwgaGVhZGVycz1oZWFkZXJzKQ0KDQpwcmludChyLnN0YXR1c19jb2RlKQ0KcHJpbnQoci50ZXh0KQ0KPT09PT09PT09PT09PT09PT09PT0NCg0KU3RlcCA0IC0gVmVyaWZ5IHVzaW5nIGJlbG93IEFQSSBjYWxsLCB3aGF0IGFsbCByZXBvc2l0b3JpZXMgYXJlIHJlZ2lzdGVyZWQgd2l0aCBPcGVuc2VhcmNoIGNsdXN0ZXINCg0K4oaSIEdFVCBfY2F0L3JlcG9zaXRvcmllcw0KDQpTdGVwIDUgLSBUbyB0YWtlIHNuYXBzaG90IHVzZSBmb2xsb3dpbmcgQVBJDQoNCuKGkiBQVVQgX3NuYXBzaG90LzxyZXBvLW5hbWU-LzxzbmFwc2hvdC1uYW1lPg0KDQpTdGVwIDYgLSBUbyBnZXQgbGlzdCBvZiBhbGwgc25hcHNob3RzDQoNCuKGkiBHRVQgX3NuYXBzaG90LzxyZXBvLW5hbWU-L19hbGwNCg0KRnJvbSBBY2NvdW50IEIgLSANCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQ0KU3RlcCAxIC0gIExhdW5jaCBhbiBFQzIgaW5zdGFuY2UgYW5kIGF0dGFjaCBJQU0gUm9sZSBjcmVhdGVkIGZvciBFQzIgaW4gc3RlcCAzIG9mIHByZXJlcXVpc2l0ZXMuDQoNClN0ZXAgMiAtIE1hcHBlZCB0aGUgSUFNIHJvbGUgXCJBbWF6b25PcGVuU2VhcmNoU2VydmljZVNuYXBzaG90c1wiIHRvICdhbGxfYWNjZXNzJyBhbmQgJ21hbmFnZV9zbmFwc2hvdHMnIGFzIGJhY2tlbmQgcm9sZSBpbiBPcGVuc2VhcmNoIERhc2hvYm9hcmRzIFNlY3VyaXR5IHNldHRpbmdzDQoNClN0ZXAgMyAtIFJlZ2lzdGVyIFNuYXBzaG90IHJlcG9zaXRvcnkgb2YgQWNjb3VudCBBIE9wZW5zZWFyY2ggZG9tYWluIGluIFMzIGJ1Y2tldCB1c2luZyBJQU0gcm9sZSBjcmVhdGVkIGluIHN0ZXAgNChiKS4NCg0KSSBoYXZlIHVzZWQgYmVsb3cgcHl0aG9uIHNjcmlwdCB0byByZWdpc3RlciBTMyBzbmFwc2hvdCByZXBvc2l0b3J5IGZvciBtYW51YWwgc25hcHNob3RzOg0KPT09PT09PT09PT09PT09PT09PT09PT09PT09DQokIGNhdCBlcy1zbmFwc2hvdC5weSAgDQoNCmltcG9ydCBib3RvMw0KaW1wb3J0IHJlcXVlc3RzDQpmcm9tIHJlcXVlc3RzX2F3czRhdXRoIGltcG9ydCBBV1M0QXV0aA0KDQpob3N0ID0gJycgIyBpbmNsdWRlIGh0dHBzOi8vIGFuZCB0cmFpbGluZyAvDQpyZWdpb24gPSAndXMtZWFzdC0xJyAjIGUuZy4gdXMtd2VzdC0xDQpzZXJ2aWNlID0gJ2VzJw0KY3JlZGVudGlhbHMgPSBib3RvMy5TZXNzaW9uKCkuZ2V0X2NyZWRlbnRpYWxzKCkNCmF3c2F1dGggPSBBV1M0QXV0aChjcmVkZW50aWFscy5hY2Nlc3Nfa2V5LCBjcmVkZW50aWFscy5zZWNyZXRfa2V5LCByZWdpb24sIHNlcnZpY2UsIHNlc3Npb25fdG9rZW49Y3JlZGVudGlhbHMudG9rZW4pDQoNCiNSZWdpc3RlciByZXBvc2l0b3J5DQoNCnBhdGggPSAnX3NuYXBzaG90L215LXNuYXBzaG90LXJlcG8nICMgdGhlIEVsYXN0aWNzZWFyY2ggQVBJIGVuZHBvaW50DQp1cmwgPSBob3N0ICsgcGF0aA0KDQpwYXlsb2FkID0gew0KICBcInR5cGVcIjogXCJzM1wiLA0KICBcInNldHRpbmdzXCI6IHsNCiAgICBcImJ1Y2tldFwiOiBcIjxTMy1idWNrZXQtbmFtZS1pbi1hY2NvdW50LUE-XCIsDQogICAgXCJyZWdpb25cIjogXCJ1cy1lYXN0LTFcIiwNCiAgICBcImJhc2VfcGF0aFwiOiBcImVzX3NuYXBzaG90c1wiLA0KICAgIFwicm9sZV9hcm5cIjogXCJhcm46YXdzOmlhbTo6PGFjY291bnQtQi1udW1iZXI-OnJvbGUvVGhlU25hcHNob3RSb2xlXCINCiAgfQ0KfQ0KDQpoZWFkZXJzID0ge1wiQ29udGVudC1UeXBlXCI6IFwiYXBwbGljYXRpb24vanNvblwifQ0KDQpyID0gcmVxdWVzdHMucHV0KHVybCwgYXV0aD1hd3NhdXRoLCBqc29uPXBheWxvYWQsIGhlYWRlcnM9aGVhZGVycykNCg0KcHJpbnQoci5zdGF0dXNfY29kZSkNCnByaW50KHIudGV4dCkNCj09PT09PT09PT09PT09PT09PT09PQ0KDQoNClN0ZXAgNCAtIFZlcmlmeSB1c2luZyBiZWxvdyBBUEkgY2FsbCwgd2hhdCBhbGwgcmVwb3NpdG9yaWVzIGFyZSByZWdpc3RlcmVkIHdpdGggT3BlbnNlYXJjaCBjbHVzdGVyDQoNCuKGkiBHRVQgX2NhdC9yZXBvc2l0b3JpZXMNCg0KU3RlcCA1IC0gVG8gZ2V0IGxpc3Qgb2YgYWxsIHNuYXBzaG90cw0KR0VUIF9zbmFwc2hvdC88cmVwby1uYW1lPi9fYWxsDQoNClN0ZXAgNiAtIFRvIHJlc3RvcmUgc25hcHNob3QNClBPU1QgX3NuYXBzaG90LzxyZXBvLW5hbWU-LzxzbmFwc2hvdC1uYW1lPi9fcmVzdG9yZQ0KPT09PT09PT09PT09PT09PT09PT09DQoNCkFmdGVyIGZvbGxvd2luZyB0aGVzZSBzdGVwcyB5b3Ugc2hvdWxkIGJlIHN1Y2Nlc3NmdWxseSBhYmxlIHRvIG1pZ3JhdGUgZGF0YSBmcm9tIG9uZSBhY2NvdW50IHRvIGFub3RoZXIuDQoNCkkgaG9wZSB0aGUgYWJvdmUgaW5mb3JtYXRpb24gaXMgdXNlZnVsLiBJZiB5b3UgaGF2ZSBhbnkgb3RoZXIgY29uY2VybnMvcXVlcmllcyByZWxhdGVkIHRvIHRoZSBzYW1lLCBwbGVhc2UgZmVlbCBmcmVlIHRvIHJlYWNoIGJhY2sgdG8gbWUgYW5kIEkgd2lsbCBiZSBnbGFkIHRvIGFzc2lzdC4NCg0KVGhhbmsgeW91IQ0KDQpXZSB2YWx1ZSB5b3VyIGZlZWRiYWNrLiBQbGVhc2Ugc2hhcmUgeW91ciBleHBlcmllbmNlIGJ5IHJhdGluZyB0aGlzIGFuZCBvdGhlciBjb3JyZXNwb25kZW5jZXMgaW4gdGhlIEFXUyBTdXBwb3J0IENlbnRlci4gWW91IGNhbiByYXRlIGEgY29ycmVzcG9uZGVuY2UgYnkgc2VsZWN0aW5nIHRoZSBzdGFycyBpbiB0aGUgdG9wIHJpZ2h0IGNvcm5lciBvZiB0aGUgY29ycmVzcG9uZGVuY2UuDQoNCkJlc3QgcmVnYXJkcywNCk1ydW5hbCAgSy4NCkFtYXpvbiBXZWIgU2VydmljZXMNCiAgPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09DQoNCiAgVG8gc2hhcmUgeW91ciBleHBlcmllbmNlIG9yIGNvbnRhY3QgdXMgYWdhaW4gYWJvdXQgdGhpcyBjYXNlLCBwbGVhc2UgcmV0dXJuIHRvIHRoZSBBV1MgU3VwcG9ydCBDZW50ZXIgdXNpbmcgdGhlIGZvbGxvd2luZyBVUkw6IGh0dHBzOi8vY29uc29sZS5hd3MuYW1hem9uLmNvbS9zdXBwb3J0L2hvbWUjL2Nhc2UvP2Rpc3BsYXlJZD0xMTc0NDg1OTIxMSZsYW5ndWFnZT1lbg0KDQogIE5vdGUsIHRoaXMgZS1tYWlsIHdhcyBzZW50IGZyb20gYW4gYWRkcmVzcyB0aGF0IGNhbm5vdCBhY2NlcHQgaW5jb21pbmcgZS1tYWlscy4NCiAgVG8gcmVzcG9uZCB0byB0aGlzIGNhc2UsIHBsZWFzZSBmb2xsb3cgdGhlIGxpbmsgYWJvdmUgdG8gcmVzcG9uZCBmcm9tIHlvdXIgQVdTIFN1cHBvcnQgQ2VudGVyLg0KDQogID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQ0KDQogIERvbuKAmXQgbWlzcyBtZXNzYWdlcyBmcm9tIEFXUyBTdXBwb3J0IHdoZW4geW91IG5lZWQgaGVscCEgVXBkYXRlIHlvdXIgY29udGFjdCBpbmZvcm1hdGlvbjoNCiAgaHR0cHM6Ly9jb25zb2xlLmF3cy5hbWF6b24uY29tL2JpbGxpbmcvaG9tZSMvYWNjb3VudA0KDQogIElmIHlvdSByZWNlaXZlIGFuIGVycm9yIG1lc3NhZ2Ugd2hlbiB2aXNpdGluZyB0aGUgY29udGFjdCBpbmZvcm1hdGlvbiBwYWdlLCB2aXNpdDoNCiAgaHR0cHM6Ly9hd3MuYW1hem9uLmNvbS9wcmVtaXVtc3VwcG9ydC9rbm93bGVkZ2UtY2VudGVyL2lhbS1iaWxsaW5nLWFjY2Vzcy8NCg0KICBBV1MgU3VwcG9ydDoNCiAgaHR0cHM6Ly9hd3MuYW1hem9uLmNvbS9wcmVtaXVtc3VwcG9ydC9rbm93bGVkZ2UtY2VudGVyLw0KDQogIEFXUyBEb2N1bWVudGF0aW9uOg0KICBodHRwczovL2RvY3MuYXdzLmFtYXpvbi5jb20vDQoNCiAgQVdTIENvc3QgTWFuYWdlbWVudDoNCiAgaHR0cHM6Ly9hd3MuYW1hem9uLmNvbS9hd3MtY29zdC1tYW5hZ2VtZW50Lw0KDQogIEFXUyBUcmFpbmluZzoNCiAgaHR0cDovL2F3cy5hbWF6b24uY29tL3RyYWluaW5nLw0KDQogIEFXUyBNYW5hZ2VkIFNlcnZpY2VzOg0KICBodHRwczovL2F3cy5hbWF6b24uY29tL21hbmFnZWQtc2VydmljZXMv"
            }
          },
          {
            "partId": "1",
            "mimeType": "text/html",
            "filename": "",
            "headers": [
              {
                "name": "Content-Type",
                "value": "text/html; charset=UTF-8"
              },
              {
                "name": "Content-Transfer-Encoding",
                "value": "quoted-printable"
              }
            ],
            "body": {
              "size": 16110,
              "data": "PCFET0NUWVBFIGh0bWw-PHA-SGVsbG8gTWFoZW5kcmEsPGJyLz48YnIvPlRoYW5rIHlvdSBzbyBtdWNoIGZvciB5b3VyIGNvbnRpbnVlZCBwYXRpZW5jZS48YnIvPjxici8-SW4gb3JkZXIgdG8gdW5kZXJzdGFuZCB0aGUgc2NlbmFyaW8gSSB0cmllZCByZXBsaWNhdGluZyB0aGlzIGF0IG15IGVuZC48YnIvPjxici8-WW91IHdlcmUgYWJsZSB0byBwZXJmb3JtIHRoZSBtaWdyYXRpb24gc3VjY2Vzc2Z1bGx5IGZvciAyLzQgZG9tYWlucyBhbmQgZmFjaW5nIGlzc3VlIHdpdGggdGhlIG90aGVyIHR3by4gSSB3b3VsZCByZXF1ZXN0IHlvdSB0byBnbyB0aHJvdWdoIHRoZSBzdGVwcyBmb3IgdGhlIGRvbWFpbnMgeW91IGFyZSBmYWNpbmcgdGhlIGlzc3VlIHdpdGguIEJlbG93IGFyZSB0aGUgZGV0YWlsZWQgc3RlcHMgZm9yIHRoZSBPcGVuc2VhcmNoIHNuYXBzaG90IG1pZ3JhdGlvbi4gPGJyLz48YnIvPklmIHRoZSBwcm9ibGVtIHN0aWxsIHBlcnNpc3RzLCBwbGVhc2UgZmVlbCBmcmVlIHRvIHJlYWNoIGJhY2sgdG8gdXMgYW5kIHdlIHdpbGwgYmUgZ2xhZCB0byBhc3Npc3QgeW91IGZ1cnRoZXIuPGJyLz48YnIvPktpbmRseSBsZXQgbWUga25vdyBhYm91dCB5b3VyIGF2YWlsYWJpbGl0eSBzbyB3ZSBjYW4gc2V0IHVwIGEgbWVldGluZy4gUGxlYXNlIG5vdGUgdGhhdCBteSBjdXJyZW50IHNoaWZ0IGlzIGZyb20gTW9uZGF5IHRvIEZyaWRheSAwNC4wMCBhbSB0byAxMC4zMGFtIFVUQyBhbmQgaWYgaW4gY2FzZSB5b3UgcmVxdWlyZSBhbnkgaW1tZWRpYXRlIGFzc2lzdGFuY2UgZHVyaW5nIG15IG9mZi1zaGlmdCBob3VycyBmZWVsIGZyZWUgdG8gcmFpc2UgYSBjaGF0L2NhbGwgYW5kIGFuIGVuZ2luZWVyIGZyb20gT3BlbnNlYXJjaCB0ZWFtIHdpbGwgYmUgaGFwcHkgdG8gYXNzaXN0IHlvdS48YnIvPjxici8-PT09PVJFUExJQ0FUSU9OIFNURVBTPT09PTxici8-PGJyLz4xLiBDcmVhdGVkIGEgRkdBQyBlbmFibGVkIEFtYXpvbiBPcGVuc2VhcmNoIGNsdXN0ZXIgaW4gYWNjb3VudCBBLjxici8-Mi4gQ3JlYXRlZCBhbiBTMyBidWNrZXQgaW4gYWNjb3VudCBBLjxici8-My4gQ3JlYXRlZCBhbm90aGVyIEZHQUMgZW5hYmxlZCBBbWF6b24gT3BlbnNlYXJjaCBjbHVzdGVyIGluIGFjY291bnQgQi48YnIvPjQuIENyZWF0ZWQgb25lIGVjMiBpbnN0YW5jZSBpbiBlYWNoIEFXUyBhY2NvdW50IHRvIHJlZ2lzdGVyIHRoZSBzbmFwc2hvdCByZXBvc2l0b3J5Ljxici8-PGJyLz4tLS0tLS1QcmUtcmVxdWlzaXRlcy0tLS0tLS08YnIvPjxici8-QmVsb3cgYXJlIHRoZSBwcmVyZXF1aXNpdGVzIHRvIGZvbGxvdyB3aGlsZSByZXN0b3Jpbmcgc25hcHNob3Qgb2YgQWNjb3VudCBBIE9wZW5TZWFyY2ggZG9tYWluIGZyb20gQWNjb3VudCBBIFMzIHRvIEFjY291bnQgQiBPcGVuc2VhcmNoIGRvbWFpbjo8YnIvPjxici8-U3RlcCAxOiBDcmVhdGUgXCYjMzQ7UzNTbmFwc2hvdFBvbGljeVwmIzM0OyBpbiBBY2NvdW50IEE8YnIvPjxici8-ezxici8-ICAgIFwmIzM0O1ZlcnNpb25cJiMzNDs6IFwmIzM0OzIwMTItMTAtMTdcJiMzNDssPGJyLz4gICAgXCYjMzQ7U3RhdGVtZW50XCYjMzQ7OiBbPGJyLz4gICAgICAgIHs8YnIvPiAgICAgICAgICAgIFwmIzM0O0FjdGlvblwmIzM0OzogWzxici8-ICAgICAgICAgICAgICAgIFwmIzM0O3MzOkxpc3RCdWNrZXRcJiMzNDs8YnIvPiAgICAgICAgICAgIF0sPGJyLz4gICAgICAgICAgICBcJiMzNDtFZmZlY3RcJiMzNDs6IFwmIzM0O0FsbG93XCYjMzQ7LDxici8-ICAgICAgICAgICAgXCYjMzQ7UmVzb3VyY2VcJiMzNDs6IFs8YnIvPiAgICAgICAgICAgICAgICBcJiMzNDthcm46YXdzOnMzOjo6Jmx0O3MzLUJ1Y2tldC1uYW1lLW9mLWFjY291bnQtQSZndDtcJiMzNDs8YnIvPiAgICAgICAgICAgIF08YnIvPiAgICAgICAgfSw8YnIvPiAgICAgICAgezxici8-ICAgICAgICAgICAgXCYjMzQ7QWN0aW9uXCYjMzQ7OiBbPGJyLz4gICAgICAgICAgICAgICAgXCYjMzQ7czM6R2V0T2JqZWN0XCYjMzQ7LDxici8-ICAgICAgICAgICAgICAgIFwmIzM0O3MzOlB1dE9iamVjdFwmIzM0Oyw8YnIvPiAgICAgICAgICAgICAgICBcJiMzNDtzMzpEZWxldGVPYmplY3RcJiMzNDs8YnIvPiAgICAgICAgICAgIF0sPGJyLz4gICAgICAgICAgICBcJiMzNDtFZmZlY3RcJiMzNDs6IFwmIzM0O0FsbG93XCYjMzQ7LDxici8-ICAgICAgICAgICAgXCYjMzQ7UmVzb3VyY2VcJiMzNDs6IFs8YnIvPiAgICAgICAgICAgICAgICBcJiMzNDthcm46YXdzOnMzOjo6Jmx0O3MzLUJ1Y2tldC1uYW1lLW9mLWFjY291bnQtQSZndDsvXCYjMzQ7PGJyLz4gICAgICAgICAgICBdPGJyLz4gICAgICAgIH08YnIvPiAgICBdPGJyLz59PGJyLz48YnIvPlN0ZXAgMjogQ3JlYXRlIFwmIzM0O1RoZVNuYXBzaG90Um9sZVwmIzM0OyBpbiBBY2NvdW50IEEgYW5kIGF0dGFjaCB0aGUgYWJvdmUgcG9saWN5IHRvIHRoYXQgcm9sZSBhbmQgZWRpdCB0cnVzdCByZWxhdGlvbnNoaXAgYXMgYmVsb3c6PGJyLz48YnIvPns8YnIvPiAgXCYjMzQ7VmVyc2lvblwmIzM0OzogXCYjMzQ7MjAxMi0xMC0xN1wmIzM0Oyw8YnIvPiAgXCYjMzQ7U3RhdGVtZW50XCYjMzQ7OiBbPGJyLz4gICAgezxici8-ICAgICAgXCYjMzQ7U2lkXCYjMzQ7OiBcJiMzNDtcJiMzNDssPGJyLz4gICAgICBcJiMzNDtFZmZlY3RcJiMzNDs6IFwmIzM0O0FsbG93XCYjMzQ7LDxici8-ICAgICAgXCYjMzQ7UHJpbmNpcGFsXCYjMzQ7OiB7PGJyLz4gICAgICAgIFwmIzM0O1NlcnZpY2VcJiMzNDs6IFwmIzM0O2VzLmFtYXpvbmF3cy5jb20gKGh0dHA6Ly9lcy5hbWF6b25hd3MuY29tLykgIOKAnDxici8-ICAgICAgfSw8YnIvPiAgICAgIFwmIzM0O0FjdGlvblwmIzM0OzogXCYjMzQ7c3RzOkFzc3VtZVJvbGVcJiMzNDs8YnIvPiAgICB9PGJyLz4gIF08YnIvPn08YnIvPjxici8-U3RlcCAzOiBDcmVhdGUgYW4gSUFNIFJvbGUgZm9yIEVDMiB3aXRoIGJlbG93IHBvbGljeSBhbmQgdHJ1c3QgcmVsYXRpb25zaGlwIHRvIGFjY2VzcyB0aGUgb3BlbnNlYXJjaCBkb21haW4gYW5kIFMzIGJ1Y2tldCBmb3IgbWFudWFsIHNuYXBzaG90Ojxici8-PGJyLz7ihpIgSUFNIFBvbGljeTxici8-PGJyLz57PGJyLz4gICAgXCYjMzQ7VmVyc2lvblwmIzM0OzogXCYjMzQ7MjAxMi0xMC0xN1wmIzM0Oyw8YnIvPiAgICBcJiMzNDtTdGF0ZW1lbnRcJiMzNDs6IFs8YnIvPiAgICAgICAgezxici8-ICAgICAgICAgICAgXCYjMzQ7RWZmZWN0XCYjMzQ7OiBcJiMzNDtBbGxvd1wmIzM0Oyw8YnIvPiAgICAgICAgICAgIFwmIzM0O0FjdGlvblwmIzM0OzogXCYjMzQ7aWFtOlBhc3NSb2xlXCYjMzQ7LDxici8-ICAgICAgICAgICAgXCYjMzQ7UmVzb3VyY2VcJiMzNDs6IFwmIzM0O2Fybjphd3M6aWFtOjombHQ7QWNjb3VudC1BLW51bWJlciZndDs6cm9sZS9UaGVTbmFwc2hvdFJvbGVcJiMzNDs8YnIvPiAgICAgICAgfSw8YnIvPiAgICAgICAgezxici8-ICAgICAgICAgICAgXCYjMzQ7RWZmZWN0XCYjMzQ7OiBcJiMzNDtBbGxvd1wmIzM0Oyw8YnIvPiAgICAgICAgICAgIFwmIzM0O0FjdGlvblwmIzM0OzogXCYjMzQ7ZXM6RVNIdHRwUHV0XCYjMzQ7LDxici8-ICAgICAgICAgICAgXCYjMzQ7UmVzb3VyY2VcJiMzNDs6IFwmIzM0O2Fybjphd3M6ZXM6dXMtZWFzdC0xOiZsdDtBY2NvdW50LUEtbnVtYmVyJmd0Ozpkb21haW4vdGVzdC1kb21haW4tYS9cJiMzNDs8YnIvPiAgICAgICAgfTxici8-ICAgIF08YnIvPn08YnIvPjxici8-4oaSIFRydXN0IFJlbGF0aW9uc2hpcDxici8-PGJyLz57PGJyLz4gIFwmIzM0O1ZlcnNpb25cJiMzNDs6IFwmIzM0OzIwMTItMTAtMTdcJiMzNDssPGJyLz4gIFwmIzM0O1N0YXRlbWVudFwmIzM0OzogWzxici8-ICAgIHs8YnIvPiAgICAgIFwmIzM0O0VmZmVjdFwmIzM0OzogXCYjMzQ7QWxsb3dcJiMzNDssPGJyLz4gICAgICBcJiMzNDtQcmluY2lwYWxcJiMzNDs6IHs8YnIvPiAgICAgICAgXCYjMzQ7U2VydmljZVwmIzM0OzogXCYjMzQ7ZWMyLmFtYXpvbmF3cy5jb20gKGh0dHA6Ly9lYzIuYW1hem9uYXdzLmNvbS8pICDigJw8YnIvPiAgICAgIH0sPGJyLz4gICAgICBcJiMzNDtBY3Rpb25cJiMzNDs6IFwmIzM0O3N0czpBc3N1bWVSb2xlXCYjMzQ7PGJyLz4gICAgfTxici8-ICBdPGJyLz59PGJyLz48YnIvPlN0ZXAgNDogUmVwZWF0IHRoZSBhYm92ZSBzdGVwcyBpbiBBY2NvdW50IEIsIGJ1dCBkbyByZW1lbWJlciB0aGF0IHRoZSBcJiMzNDtTM1NuYXBzaG90UG9saWN5XCYjMzQ7IHdpbGwgcmVtYWluIHNhbWUgYXMgd2Ugd2FudCB0byB1c2UgUzMgYnVja2V0IG9mIEFjY291bnQgQSBpbiBBY2NvdW50IEIuPGJyLz48YnIvPmEpIEFjY291bnQgQiBcJiMzNDtTM1NuYXBzaG90UG9saWN5XCYjMzQ7PGJyLz48YnIvPns8YnIvPiAgICBcJiMzNDtWZXJzaW9uXCYjMzQ7OiBcJiMzNDsyMDEyLTEwLTE3XCYjMzQ7LDxici8-ICAgIFwmIzM0O1N0YXRlbWVudFwmIzM0OzogWzxici8-ICAgICAgICB7PGJyLz4gICAgICAgICAgICBcJiMzNDtBY3Rpb25cJiMzNDs6IFs8YnIvPiAgICAgICAgICAgICAgICBcJiMzNDtzMzpMaXN0QnVja2V0XCYjMzQ7PGJyLz4gICAgICAgICAgICBdLDxici8-ICAgICAgICAgICAgXCYjMzQ7RWZmZWN0XCYjMzQ7OiBcJiMzNDtBbGxvd1wmIzM0Oyw8YnIvPiAgICAgICAgICAgIFwmIzM0O1Jlc291cmNlXCYjMzQ7OiBbPGJyLz4gICAgICAgICAgICAgICAgXCYjMzQ7YXJuOmF3czpzMzo6OiZsdDtzMy1CdWNrZXQtbmFtZS1vZi1hY2NvdW50LUEmZ3Q7XCYjMzQ7PGJyLz4gICAgICAgICAgICBdPGJyLz4gICAgICAgIH0sPGJyLz4gICAgICAgIHs8YnIvPiAgICAgICAgICAgIFwmIzM0O0FjdGlvblwmIzM0OzogWzxici8-ICAgICAgICAgICAgICAgIFwmIzM0O3MzOkdldE9iamVjdFwmIzM0Oyw8YnIvPiAgICAgICAgICAgICAgICBcJiMzNDtzMzpQdXRPYmplY3RcJiMzNDssPGJyLz4gICAgICAgICAgICAgICAgXCYjMzQ7czM6RGVsZXRlT2JqZWN0XCYjMzQ7PGJyLz4gICAgICAgICAgICBdLDxici8-ICAgICAgICAgICAgXCYjMzQ7RWZmZWN0XCYjMzQ7OiBcJiMzNDtBbGxvd1wmIzM0Oyw8YnIvPiAgICAgICAgICAgIFwmIzM0O1Jlc291cmNlXCYjMzQ7OiBbPGJyLz4gICAgICAgICAgICAgICAgXCYjMzQ7YXJuOmF3czpzMzo6OiZsdDtzMy1CdWNrZXQtbmFtZS1vZi1hY2NvdW50LUEmZ3Q7L1wmIzM0Ozxici8-ICAgICAgICAgICAgXTxici8-ICAgICAgICB9PGJyLz4gICAgXTxici8-fTxici8-PGJyLz5iKSBBY2NvdW50IEIgXCYjMzQ7VGhlU25hcHNob3RSb2xlXCYjMzQ7IHdpdGggYWJvdmUgcG9saWN5IGFuZCB0cnVzdCByZWxhdGlvbnNoaXAgYXMgYmVsb3c6PGJyLz48YnIvPns8YnIvPiAgXCYjMzQ7VmVyc2lvblwmIzM0OzogXCYjMzQ7MjAxMi0xMC0xN1wmIzM0Oyw8YnIvPiAgXCYjMzQ7U3RhdGVtZW50XCYjMzQ7OiBbPGJyLz4gICAgezxici8-ICAgICAgXCYjMzQ7U2lkXCYjMzQ7OiBcJiMzNDtcJiMzNDssPGJyLz4gICAgICBcJiMzNDtFZmZlY3RcJiMzNDs6IFwmIzM0O0FsbG93XCYjMzQ7LDxici8-ICAgICAgXCYjMzQ7UHJpbmNpcGFsXCYjMzQ7OiB7PGJyLz4gICAgICAgIFwmIzM0O1NlcnZpY2VcJiMzNDs6IFwmIzM0O2VzLmFtYXpvbmF3cy5jb20gKGh0dHA6Ly9lcy5hbWF6b25hd3MuY29tLykgIOKAnDxici8-ICAgICAgfSw8YnIvPiAgICAgIFwmIzM0O0FjdGlvblwmIzM0OzogXCYjMzQ7c3RzOkFzc3VtZVJvbGVcJiMzNDs8YnIvPiAgICB9PGJyLz4gIF08YnIvPn08YnIvPjxici8-YykgQWNjb3VudCBCOiBFQzIgSW5zdGFuY2UgSUFNIFJvbGUgd2l0aCBiZWxvdyBwb2xpY3kgYW5kIHRydXN0IHJlbGF0aW9uc2hpcCB0byBhY2Nlc3MgdGhlIFMzIEJ1Y2tldCBhbmQgdGhlIE9wZW5zZWFyY2ggZG9tYWluIGluIEFjY291bnQgQjo8YnIvPuKGkiBJQU0gUG9saWN5PGJyLz48YnIvPns8YnIvPiAgICBcJiMzNDtWZXJzaW9uXCYjMzQ7OiBcJiMzNDsyMDEyLTEwLTE3XCYjMzQ7LDxici8-ICAgIFwmIzM0O1N0YXRlbWVudFwmIzM0OzogWzxici8-ICAgICAgICB7PGJyLz4gICAgICAgICAgICBcJiMzNDtFZmZlY3RcJiMzNDs6IFwmIzM0O0FsbG93XCYjMzQ7LDxici8-ICAgICAgICAgICAgXCYjMzQ7QWN0aW9uXCYjMzQ7OiBcJiMzNDtpYW06UGFzc1JvbGVcJiMzNDssPGJyLz4gICAgICAgICAgICBcJiMzNDtSZXNvdXJjZVwmIzM0OzogXCYjMzQ7YXJuOmF3czppYW06OiZsdDtBY2NvdW50LUItbnVtYmVyJmd0Ozpyb2xlL1RoZVNuYXBzaG90Um9sZVwmIzM0Ozxici8-ICAgICAgICB9LDxici8-ICAgICAgICB7PGJyLz4gICAgICAgICAgICBcJiMzNDtFZmZlY3RcJiMzNDs6IFwmIzM0O0FsbG93XCYjMzQ7LDxici8-ICAgICAgICAgICAgXCYjMzQ7QWN0aW9uXCYjMzQ7OiBcJiMzNDtlczpFU0h0dHBQdXRcJiMzNDssPGJyLz4gICAgICAgICAgICBcJiMzNDtSZXNvdXJjZVwmIzM0OzogXCYjMzQ7YXJuOmF3czplczp1cy1lYXN0LTE6Jmx0O0FjY291bnQtQi1udW1iZXImZ3Q7OmRvbWFpbi90ZXN0LWRvbWFpbi1iL1wmIzM0Ozxici8-ICAgICAgICB9PGJyLz4gICAgXTxici8-fTxici8-PGJyLz7ihpIgVHJ1c3QgUmVsYXRpb25zaGlwPGJyLz48YnIvPns8YnIvPiAgXCYjMzQ7VmVyc2lvblwmIzM0OzogXCYjMzQ7MjAxMi0xMC0xN1wmIzM0Oyw8YnIvPiAgXCYjMzQ7U3RhdGVtZW50XCYjMzQ7OiBbPGJyLz4gICAgezxici8-ICAgICAgXCYjMzQ7RWZmZWN0XCYjMzQ7OiBcJiMzNDtBbGxvd1wmIzM0Oyw8YnIvPiAgICAgIFwmIzM0O1ByaW5jaXBhbFwmIzM0Ozogezxici8-ICAgICAgICBcJiMzNDtTZXJ2aWNlXCYjMzQ7OiBcJiMzNDtlYzIuYW1hem9uYXdzLmNvbSAoaHR0cDovL2VjMi5hbWF6b25hd3MuY29tLykgIOKAnDxici8-ICAgICAgfSw8YnIvPiAgICAgIFwmIzM0O0FjdGlvblwmIzM0OzogXCYjMzQ7c3RzOkFzc3VtZVJvbGVcJiMzNDs8YnIvPiAgICB9PGJyLz4gIF08YnIvPn08YnIvPjxici8-U3RlcCA1OiBUaGUgRmluYWwgc3RlcCB3aWxsIGFsbG93IGFjY2VzcyBmcm9tIEFjY291bnQgQiB0byBBY2NvdW50IEEgUzMgYnVja2V0Ojxici8-PGJyLz7ihpIgRWRpdCBBY2NvdW50IEEgUzMgQnVja2V0IGFjY2VzcyBwb2xpY3k6PGJyLz48YnIvPns8YnIvPiAgICBcJiMzNDtWZXJzaW9uXCYjMzQ7OiBcJiMzNDsyMDEyLTEwLTE3XCYjMzQ7LDxici8-ICAgIFwmIzM0O0lkXCYjMzQ7OiBcJiMzNDtQb2xpY3kxNTY4MDAxMDEwNzQ2XCYjMzQ7LDxici8-ICAgIFwmIzM0O1N0YXRlbWVudFwmIzM0OzogWzxici8-ICAgICAgICB7PGJyLz4gICAgICAgICAgICBcJiMzNDtTaWRcJiMzNDs6IFwmIzM0O1N0bXQxNTY4MDAwNzEyNTMxXCYjMzQ7LDxici8-ICAgICAgICAgICAgXCYjMzQ7RWZmZWN0XCYjMzQ7OiBcJiMzNDtBbGxvd1wmIzM0Oyw8YnIvPiAgICAgICAgICAgIFwmIzM0O1ByaW5jaXBhbFwmIzM0Ozogezxici8-ICAgICAgICAgICAgICAgIFwmIzM0O0FXU1wmIzM0OzogXCYjMzQ7YXJuOmF3czppYW06OiZsdDtBY2NvdW50LUItbnVtYmVyJmd0Ozpyb2xlL1RoZVNuYXBzaG90Um9sZVwmIzM0Ozxici8-ICAgICAgICAgICAgfSw8YnIvPiAgICAgICAgICAgIFwmIzM0O0FjdGlvblwmIzM0OzogXCYjMzQ7czM6XCYjMzQ7LDxici8-ICAgICAgICAgICAgXCYjMzQ7UmVzb3VyY2VcJiMzNDs6IFs8YnIvPiAgICAgICAgICAgICAgICBcJiMzNDthcm46YXdzOnMzOjo6Jmx0O3MzLUJ1Y2tldC1uYW1lLW9mLWFjY291bnQtQSZndDtcJiMzNDssPGJyLz4gICAgICAgICAgICAgICAgXCYjMzQ7YXJuOmF3czpzMzo6OiZsdDtzMy1CdWNrZXQtbmFtZS1vZi1hY2NvdW50LUEmZ3Q7L1wmIzM0Ozxici8-ICAgICAgICAgICAgXTxici8-ICAgICAgICB9PGJyLz4gICAgXTxici8-fTxici8-PGJyLz49PU5vdyBtb3ZpbmcgdG8gdGhlIHJlZ2lzdGVyIHNuYXBzaG90IHJlcG9zaXRvcnkgc3RlcHM6PT08YnIvPjxici8-RnJvbSBBY2NvdW50IEEgLTxici8-LS0tLS0tLS0tLS0tLS0tLS0tLS0tPGJyLz5TdGVwIDEgLSAgTGF1bmNoIGFuIEVDMiBpbnN0YW5jZSBhbmQgdHRhY2ggSUFNIFJvbGUgY3JlYXRlZCBmb3IgRUMyIGluIHN0ZXAgMyBvZiBwcmVyZXF1aXNpdGVzLjxici8-PGJyLz5TdGVwIDIgLSBNYXBwZWQgdGhlIElBTSByb2xlIFwmIzM0O0FtYXpvbk9wZW5TZWFyY2hTZXJ2aWNlU25hcHNob3RzXCYjMzQ7IHRvICYjMzk7YWxsX2FjY2VzcyYjMzk7IGFuZCAmIzM5O21hbmFnZV9zbmFwc2hvdHMmIzM5OyBhcyBiYWNrZW5kIHJvbGUgaW4gT3BlbnNlYXJjaCBEYXNob2JvYXJkcyBTZWN1cml0eSBzZXR0aW5nczxici8-PGJyLz5TdGVwIDMgLSBSZWdpc3RlciBTbmFwc2hvdCByZXBvc2l0b3J5IG9mIEFjY291bnQgQSBPcGVuc2VhcmNoIGRvbWFpbiBpbiBTMyBidWNrZXQgdXNpbmcgSUFNIHJvbGUgY3JlYXRlZCBpbiBzdGVwIDIuPGJyLz48YnIvPkkgaGF2ZSB1c2VkIGJlbG93IHB5dGhvbiBzY3JpcHQgdG8gcmVnaXN0ZXIgUzMgc25hcHNob3QgcmVwb3NpdG9yeSBmb3IgbWFudWFsIHNuYXBzaG90czo8YnIvPj09PT09PT09PT09PT09PT09PT09PT09PT09PGJyLz4kIGNhdCBlcy1zbmFwc2hvdC5weSAgPGJyLz48YnIvPmltcG9ydCBib3RvMzxici8-aW1wb3J0IHJlcXVlc3RzPGJyLz5mcm9tIHJlcXVlc3RzX2F3czRhdXRoIGltcG9ydCBBV1M0QXV0aDxici8-PGJyLz5ob3N0ID0gJiMzOTsmIzM5OyAjIGluY2x1ZGUgaHR0cHM6Ly8gYW5kIHRyYWlsaW5nIC88YnIvPnJlZ2lvbiA9ICYjMzk7dXMtZWFzdC0xJiMzOTsgIyBlLmcuIHVzLXdlc3QtMTxici8-c2VydmljZSA9ICYjMzk7ZXMmIzM5Ozxici8-Y3JlZGVudGlhbHMgPSBib3RvMy5TZXNzaW9uKCkuZ2V0X2NyZWRlbnRpYWxzKCk8YnIvPmF3c2F1dGggPSBBV1M0QXV0aChjcmVkZW50aWFscy5hY2Nlc3Nfa2V5LCBjcmVkZW50aWFscy5zZWNyZXRfa2V5LCByZWdpb24sIHNlcnZpY2UsIHNlc3Npb25fdG9rZW49Y3JlZGVudGlhbHMudG9rZW4pPGJyLz48YnIvPiNSZWdpc3RlciByZXBvc2l0b3J5PGJyLz48YnIvPnBhdGggPSAmIzM5O19zbmFwc2hvdC9teS1zbmFwc2hvdC1yZXBvJiMzOTsgIyB0aGUgRWxhc3RpY3NlYXJjaCBBUEkgZW5kcG9pbnQ8YnIvPnVybCA9IGhvc3QgKyBwYXRoPGJyLz48YnIvPnBheWxvYWQgPSB7PGJyLz4gIFwmIzM0O3R5cGVcJiMzNDs6IFwmIzM0O3MzXCYjMzQ7LDxici8-ICBcJiMzNDtzZXR0aW5nc1wmIzM0Ozogezxici8-ICAgIFwmIzM0O2J1Y2tldFwmIzM0OzogXCYjMzQ7Jmx0O1MzLWJ1Y2tldC1uYW1lLWluLWFjY291bnQtQSZndDtcJiMzNDssPGJyLz4gICAgXCYjMzQ7cmVnaW9uXCYjMzQ7OiBcJiMzNDt1cy1lYXN0LTFcJiMzNDssPGJyLz4gICAgXCYjMzQ7YmFzZV9wYXRoXCYjMzQ7OiBcJiMzNDtlc19zbmFwc2hvdHNcJiMzNDssPGJyLz4gICAgXCYjMzQ7cm9sZV9hcm5cJiMzNDs6IFwmIzM0O2Fybjphd3M6aWFtOjombHQ7YWNjb3VudC1BLW51bWJlciZndDs6cm9sZS9UaGVTbmFwc2hvdFJvbGVcJiMzNDs8YnIvPiAgfTxici8-fTxici8-PGJyLz5oZWFkZXJzID0ge1wmIzM0O0NvbnRlbnQtVHlwZVwmIzM0OzogXCYjMzQ7YXBwbGljYXRpb24vanNvblwmIzM0O308YnIvPjxici8-ciA9IHJlcXVlc3RzLnB1dCh1cmwsIGF1dGg9YXdzYXV0aCwganNvbj1wYXlsb2FkLCBoZWFkZXJzPWhlYWRlcnMpPGJyLz48YnIvPnByaW50KHIuc3RhdHVzX2NvZGUpPGJyLz5wcmludChyLnRleHQpPGJyLz49PT09PT09PT09PT09PT09PT09PTxici8-PGJyLz5TdGVwIDQgLSBWZXJpZnkgdXNpbmcgYmVsb3cgQVBJIGNhbGwsIHdoYXQgYWxsIHJlcG9zaXRvcmllcyBhcmUgcmVnaXN0ZXJlZCB3aXRoIE9wZW5zZWFyY2ggY2x1c3Rlcjxici8-PGJyLz7ihpIgR0VUIF9jYXQvcmVwb3NpdG9yaWVzPGJyLz48YnIvPlN0ZXAgNSAtIFRvIHRha2Ugc25hcHNob3QgdXNlIGZvbGxvd2luZyBBUEk8YnIvPjxici8-4oaSIFBVVCBfc25hcHNob3QvJmx0O3JlcG8tbmFtZSZndDsvJmx0O3NuYXBzaG90LW5hbWUmZ3Q7PGJyLz48YnIvPlN0ZXAgNiAtIFRvIGdldCBsaXN0IG9mIGFsbCBzbmFwc2hvdHM8YnIvPjxici8-4oaSIEdFVCBfc25hcHNob3QvJmx0O3JlcG8tbmFtZSZndDsvX2FsbDxici8-PGJyLz5Gcm9tIEFjY291bnQgQiAtIDxici8-LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tPGJyLz5TdGVwIDEgLSAgTGF1bmNoIGFuIEVDMiBpbnN0YW5jZSBhbmQgYXR0YWNoIElBTSBSb2xlIGNyZWF0ZWQgZm9yIEVDMiBpbiBzdGVwIDMgb2YgcHJlcmVxdWlzaXRlcy48YnIvPjxici8-U3RlcCAyIC0gTWFwcGVkIHRoZSBJQU0gcm9sZSBcJiMzNDtBbWF6b25PcGVuU2VhcmNoU2VydmljZVNuYXBzaG90c1wmIzM0OyB0byAmIzM5O2FsbF9hY2Nlc3MmIzM5OyBhbmQgJiMzOTttYW5hZ2Vfc25hcHNob3RzJiMzOTsgYXMgYmFja2VuZCByb2xlIGluIE9wZW5zZWFyY2ggRGFzaG9ib2FyZHMgU2VjdXJpdHkgc2V0dGluZ3M8YnIvPjxici8-U3RlcCAzIC0gUmVnaXN0ZXIgU25hcHNob3QgcmVwb3NpdG9yeSBvZiBBY2NvdW50IEEgT3BlbnNlYXJjaCBkb21haW4gaW4gUzMgYnVja2V0IHVzaW5nIElBTSByb2xlIGNyZWF0ZWQgaW4gc3RlcCA0KGIpLjxici8-PGJyLz5JIGhhdmUgdXNlZCBiZWxvdyBweXRob24gc2NyaXB0IHRvIHJlZ2lzdGVyIFMzIHNuYXBzaG90IHJlcG9zaXRvcnkgZm9yIG1hbnVhbCBzbmFwc2hvdHM6PGJyLz49PT09PT09PT09PT09PT09PT09PT09PT09PT08YnIvPiQgY2F0IGVzLXNuYXBzaG90LnB5ICA8YnIvPjxici8-aW1wb3J0IGJvdG8zPGJyLz5pbXBvcnQgcmVxdWVzdHM8YnIvPmZyb20gcmVxdWVzdHNfYXdzNGF1dGggaW1wb3J0IEFXUzRBdXRoPGJyLz48YnIvPmhvc3QgPSAmIzM5OyYjMzk7ICMgaW5jbHVkZSBodHRwczovLyBhbmQgdHJhaWxpbmcgLzxici8-cmVnaW9uID0gJiMzOTt1cy1lYXN0LTEmIzM5OyAjIGUuZy4gdXMtd2VzdC0xPGJyLz5zZXJ2aWNlID0gJiMzOTtlcyYjMzk7PGJyLz5jcmVkZW50aWFscyA9IGJvdG8zLlNlc3Npb24oKS5nZXRfY3JlZGVudGlhbHMoKTxici8-YXdzYXV0aCA9IEFXUzRBdXRoKGNyZWRlbnRpYWxzLmFjY2Vzc19rZXksIGNyZWRlbnRpYWxzLnNlY3JldF9rZXksIHJlZ2lvbiwgc2VydmljZSwgc2Vzc2lvbl90b2tlbj1jcmVkZW50aWFscy50b2tlbik8YnIvPjxici8-I1JlZ2lzdGVyIHJlcG9zaXRvcnk8YnIvPjxici8-cGF0aCA9ICYjMzk7X3NuYXBzaG90L215LXNuYXBzaG90LXJlcG8mIzM5OyAjIHRoZSBFbGFzdGljc2VhcmNoIEFQSSBlbmRwb2ludDxici8-dXJsID0gaG9zdCArIHBhdGg8YnIvPjxici8-cGF5bG9hZCA9IHs8YnIvPiAgXCYjMzQ7dHlwZVwmIzM0OzogXCYjMzQ7czNcJiMzNDssPGJyLz4gIFwmIzM0O3NldHRpbmdzXCYjMzQ7OiB7PGJyLz4gICAgXCYjMzQ7YnVja2V0XCYjMzQ7OiBcJiMzNDsmbHQ7UzMtYnVja2V0LW5hbWUtaW4tYWNjb3VudC1BJmd0O1wmIzM0Oyw8YnIvPiAgICBcJiMzNDtyZWdpb25cJiMzNDs6IFwmIzM0O3VzLWVhc3QtMVwmIzM0Oyw8YnIvPiAgICBcJiMzNDtiYXNlX3BhdGhcJiMzNDs6IFwmIzM0O2VzX3NuYXBzaG90c1wmIzM0Oyw8YnIvPiAgICBcJiMzNDtyb2xlX2FyblwmIzM0OzogXCYjMzQ7YXJuOmF3czppYW06OiZsdDthY2NvdW50LUItbnVtYmVyJmd0Ozpyb2xlL1RoZVNuYXBzaG90Um9sZVwmIzM0Ozxici8-ICB9PGJyLz59PGJyLz48YnIvPmhlYWRlcnMgPSB7XCYjMzQ7Q29udGVudC1UeXBlXCYjMzQ7OiBcJiMzNDthcHBsaWNhdGlvbi9qc29uXCYjMzQ7fTxici8-PGJyLz5yID0gcmVxdWVzdHMucHV0KHVybCwgYXV0aD1hd3NhdXRoLCBqc29uPXBheWxvYWQsIGhlYWRlcnM9aGVhZGVycyk8YnIvPjxici8-cHJpbnQoci5zdGF0dXNfY29kZSk8YnIvPnByaW50KHIudGV4dCk8YnIvPj09PT09PT09PT09PT09PT09PT09PTxici8-PGJyLz48YnIvPlN0ZXAgNCAtIFZlcmlmeSB1c2luZyBiZWxvdyBBUEkgY2FsbCwgd2hhdCBhbGwgcmVwb3NpdG9yaWVzIGFyZSByZWdpc3RlcmVkIHdpdGggT3BlbnNlYXJjaCBjbHVzdGVyPGJyLz48YnIvPuKGkiBHRVQgX2NhdC9yZXBvc2l0b3JpZXM8YnIvPjxici8-U3RlcCA1IC0gVG8gZ2V0IGxpc3Qgb2YgYWxsIHNuYXBzaG90czxici8-R0VUIF9zbmFwc2hvdC8mbHQ7cmVwby1uYW1lJmd0Oy9fYWxsPGJyLz48YnIvPlN0ZXAgNiAtIFRvIHJlc3RvcmUgc25hcHNob3Q8YnIvPlBPU1QgX3NuYXBzaG90LyZsdDtyZXBvLW5hbWUmZ3Q7LyZsdDtzbmFwc2hvdC1uYW1lJmd0Oy9fcmVzdG9yZTxici8-PT09PT09PT09PT09PT09PT09PT09PGJyLz48YnIvPkFmdGVyIGZvbGxvd2luZyB0aGVzZSBzdGVwcyB5b3Ugc2hvdWxkIGJlIHN1Y2Nlc3NmdWxseSBhYmxlIHRvIG1pZ3JhdGUgZGF0YSBmcm9tIG9uZSBhY2NvdW50IHRvIGFub3RoZXIuPGJyLz48YnIvPkkgaG9wZSB0aGUgYWJvdmUgaW5mb3JtYXRpb24gaXMgdXNlZnVsLiBJZiB5b3UgaGF2ZSBhbnkgb3RoZXIgY29uY2VybnMvcXVlcmllcyByZWxhdGVkIHRvIHRoZSBzYW1lLCBwbGVhc2UgZmVlbCBmcmVlIHRvIHJlYWNoIGJhY2sgdG8gbWUgYW5kIEkgd2lsbCBiZSBnbGFkIHRvIGFzc2lzdC48YnIvPjxici8-VGhhbmsgeW91ITxici8-PGJyLz5XZSB2YWx1ZSB5b3VyIGZlZWRiYWNrLiBQbGVhc2Ugc2hhcmUgeW91ciBleHBlcmllbmNlIGJ5IHJhdGluZyB0aGlzIGFuZCBvdGhlciBjb3JyZXNwb25kZW5jZXMgaW4gdGhlIEFXUyBTdXBwb3J0IENlbnRlci4gWW91IGNhbiByYXRlIGEgY29ycmVzcG9uZGVuY2UgYnkgc2VsZWN0aW5nIHRoZSBzdGFycyBpbiB0aGUgdG9wIHJpZ2h0IGNvcm5lciBvZiB0aGUgY29ycmVzcG9uZGVuY2UuPGJyLz48YnIvPkJlc3QgcmVnYXJkcyw8YnIvPk1ydW5hbCAgSy48YnIvPkFtYXpvbiBXZWIgU2VydmljZXM8YnIvPjxici8-DQogICAgICA8L3A-PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09DQogIA0KICA8cD4NCiAgICBUbyBzaGFyZSB5b3VyIGV4cGVyaWVuY2Ugb3IgY29udGFjdCB1cyBhZ2FpbiBhYm91dCB0aGlzIGNhc2UsIHBsZWFzZSByZXR1cm4gdG8gdGhlIEFXUyBTdXBwb3J0IENlbnRlciB1c2luZyB0aGUgZm9sbG93aW5nIFVSTDogPGEgaHJlZj0iaHR0cHM6Ly9rcWh3YjdmdC5yLnVzLWVhc3QtMS5hd3N0cmFjay5tZS9MMC9odHRwczolMkYlMkZjb25zb2xlLmF3cy5hbWF6b24uY29tJTJGc3VwcG9ydCUyRmhvbWUlMjMlMkZjYXNlJTJGJTNGZGlzcGxheUlkPTExNzQ0ODU5MjExJTI2bGFuZ3VhZ2U9ZW4vMS8wMTAwMDE4NWFmOGNkOTQwLTJkMjVhNWJlLTdjOTMtNDM0YS05ZmNhLTdkMDU1NDE3MjMyNC0wMDAwMDAveEJlUzNUb1pyV0k4YnNvT0MyMDlZTDU3UHNNPTMwNCI-aHR0cHM6Ly9jb25zb2xlLmF3cy5hbWF6b24uY29tL3N1cHBvcnQvaG9tZSMvY2FzZS8_ZGlzcGxheUlkPTExNzQ0ODU5MjExJmFtcDtsYW5ndWFnZT1lbjwvYT4NCiAgPC9wPg0KICA8cD4NCiAgICBOb3RlLCB0aGlzIGUtbWFpbCB3YXMgc2VudCBmcm9tIGFuIGFkZHJlc3MgdGhhdCBjYW5ub3QgYWNjZXB0IGluY29taW5nIGUtbWFpbHMuDQogICAgVG8gcmVzcG9uZCB0byB0aGlzIGNhc2UsIHBsZWFzZSBmb2xsb3cgdGhlIGxpbmsgYWJvdmUgdG8gcmVzcG9uZCBmcm9tIHlvdXIgQVdTIFN1cHBvcnQgQ2VudGVyLg0KICA8L3A-DQogIDxwPg0KICAgID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQ0KICA8L3A-DQogIDxwPg0KICAgIERvbuKAmXQgbWlzcyBtZXNzYWdlcyBmcm9tIEFXUyBTdXBwb3J0IHdoZW4geW91IG5lZWQgaGVscCEgVXBkYXRlIHlvdXIgY29udGFjdCBpbmZvcm1hdGlvbjo8YnIvPg0KICAgIDxhIGhyZWY9Imh0dHBzOi8va3Fod2I3ZnQuci51cy1lYXN0LTEuYXdzdHJhY2subWUvTDAvaHR0cHM6JTJGJTJGY29uc29sZS5hd3MuYW1hem9uLmNvbSUyRmJpbGxpbmclMkZob21lJTIzJTJGYWNjb3VudC8xLzAxMDAwMTg1YWY4Y2Q5NDAtMmQyNWE1YmUtN2M5My00MzRhLTlmY2EtN2QwNTU0MTcyMzI0LTAwMDAwMC8tdGtHVkM0S3N4WldINm5UT3ZoOFFXaDNoUWM9MzA0Ij5odHRwczovL2NvbnNvbGUuYXdzLmFtYXpvbi5jb20vYmlsbGluZy9ob21lIy9hY2NvdW50PC9hPg0KICA8L3A-DQogIDxwPg0KICAgIElmIHlvdSByZWNlaXZlIGFuIGVycm9yIG1lc3NhZ2Ugd2hlbiB2aXNpdGluZyB0aGUgY29udGFjdCBpbmZvcm1hdGlvbiBwYWdlLCB2aXNpdDo8YnIvPg0KICAgIDxhIGhyZWY9Imh0dHBzOi8va3Fod2I3ZnQuci51cy1lYXN0LTEuYXdzdHJhY2subWUvTDAvaHR0cHM6JTJGJTJGYXdzLmFtYXpvbi5jb20lMkZwcmVtaXVtc3VwcG9ydCUyRmtub3dsZWRnZS1jZW50ZXIlMkZpYW0tYmlsbGluZy1hY2Nlc3MlMkYvMS8wMTAwMDE4NWFmOGNkOTQwLTJkMjVhNWJlLTdjOTMtNDM0YS05ZmNhLTdkMDU1NDE3MjMyNC0wMDAwMDAvNkxCVjA5WTlNUHBCNG9sVTMyN3p3dDdXemVFPTMwNCI-aHR0cHM6Ly9hd3MuYW1hem9uLmNvbS9wcmVtaXVtc3VwcG9ydC9rbm93bGVkZ2UtY2VudGVyL2lhbS1iaWxsaW5nLWFjY2Vzcy88L2E-DQogIDwvcD4NCiAgPHA-DQogICAgQVdTIFN1cHBvcnQ6PGJyLz4NCiAgICA8YSBocmVmPSJodHRwczovL2txaHdiN2Z0LnIudXMtZWFzdC0xLmF3c3RyYWNrLm1lL0wwL2h0dHBzOiUyRiUyRmF3cy5hbWF6b24uY29tJTJGcHJlbWl1bXN1cHBvcnQlMkZrbm93bGVkZ2UtY2VudGVyJTJGLzEvMDEwMDAxODVhZjhjZDk0MC0yZDI1YTViZS03YzkzLTQzNGEtOWZjYS03ZDA1NTQxNzIzMjQtMDAwMDAwL0tkem10WmN2M0Z2ZkI5aEhuaG4xaXBvdFZ6ST0zMDQiPmh0dHBzOi8vYXdzLmFtYXpvbi5jb20vcHJlbWl1bXN1cHBvcnQva25vd2xlZGdlLWNlbnRlci88L2E-DQogIDwvcD4NCiAgPHA-DQogICAgQVdTIERvY3VtZW50YXRpb246PGJyLz4NCiAgICA8YSBocmVmPSJodHRwczovL2txaHdiN2Z0LnIudXMtZWFzdC0xLmF3c3RyYWNrLm1lL0wwL2h0dHBzOiUyRiUyRmRvY3MuYXdzLmFtYXpvbi5jb20lMkYvMS8wMTAwMDE4NWFmOGNkOTQwLTJkMjVhNWJlLTdjOTMtNDM0YS05ZmNhLTdkMDU1NDE3MjMyNC0wMDAwMDAvVkk3NmRjZVkxeGxlWFlvd0tkOGR4ZG40SE9BPTMwNCI-aHR0cHM6Ly9kb2NzLmF3cy5hbWF6b24uY29tLzwvYT4NCiAgPC9wPg0KICA8cD4NCiAgICBBV1MgQ29zdCBNYW5hZ2VtZW50Ojxici8-DQogICAgPGEgaHJlZj0iaHR0cHM6Ly9rcWh3YjdmdC5yLnVzLWVhc3QtMS5hd3N0cmFjay5tZS9MMC9odHRwczolMkYlMkZhd3MuYW1hem9uLmNvbSUyRmF3cy1jb3N0LW1hbmFnZW1lbnQlMkYvMS8wMTAwMDE4NWFmOGNkOTQwLTJkMjVhNWJlLTdjOTMtNDM0YS05ZmNhLTdkMDU1NDE3MjMyNC0wMDAwMDAvellLRm56RFh6QXBYRlc0OG50WWNRcHBja2prPTMwNCI-aHR0cHM6Ly9hd3MuYW1hem9uLmNvbS9hd3MtY29zdC1tYW5hZ2VtZW50LzwvYT4NCiAgPC9wPg0KICA8cD4NCiAgICBBV1MgVHJhaW5pbmc6PGJyLz4NCiAgICA8YSBocmVmPSJodHRwOi8va3Fod2I3ZnQuci51cy1lYXN0LTEuYXdzdHJhY2subWUvTDAvaHR0cDolMkYlMkZhd3MuYW1hem9uLmNvbSUyRnRyYWluaW5nJTJGLzEvMDEwMDAxODVhZjhjZDk0MC0yZDI1YTViZS03YzkzLTQzNGEtOWZjYS03ZDA1NTQxNzIzMjQtMDAwMDAwL044dW9ncEpkcTlKWi1lQXZKVnJnZG9lVkd4WT0zMDQiPmh0dHA6Ly9hd3MuYW1hem9uLmNvbS90cmFpbmluZy88L2E-DQogIDwvcD4NCiAgPHA-DQogICAgQVdTIE1hbmFnZWQgU2VydmljZXM6PGJyLz4NCiAgICA8YSBocmVmPSJodHRwczovL2txaHdiN2Z0LnIudXMtZWFzdC0xLmF3c3RyYWNrLm1lL0wwL2h0dHBzOiUyRiUyRmF3cy5hbWF6b24uY29tJTJGbWFuYWdlZC1zZXJ2aWNlcyUyRi8xLzAxMDAwMTg1YWY4Y2Q5NDAtMmQyNWE1YmUtN2M5My00MzRhLTlmY2EtN2QwNTU0MTcyMzI0LTAwMDAwMC9oY2xwaV9NLUJ4ckE2c2xfRlZXTXVoLTN1Yjg9MzA0Ij5odHRwczovL2F3cy5hbWF6b24uY29tL21hbmFnZWQtc2VydmljZXMvPC9hPg0KICA8cD48aW1nIGFsdD0iIiBzcmM9Imh0dHBzOi8va3Fod2I3ZnQuci51cy1lYXN0LTEuYXdzdHJhY2subWUvSTAvMDEwMDAxODVhZjhjZDk0MC0yZDI1YTViZS03YzkzLTQzNGEtOWZjYS03ZDA1NTQxNzIzMjQtMDAwMDAwL2RrYjBZanItY3hjZ0ZLZUdKOTBJQzZuTXdGbz0zMDQiIHN0eWxlPSJkaXNwbGF5OiBub25lOyB3aWR0aDogMXB4OyBoZWlnaHQ6IDFweDsiPg0K"
            }
          }
        ]
      },
      "sizeEstimate": 34864,
      "historyId": "323270",
      "internalDate": "1673687521000"
    }
  ]
}