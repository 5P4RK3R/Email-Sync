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