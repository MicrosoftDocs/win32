---
description: "Learn more about: Database Cache Parameters"
title: Database Cache Parameters
TOCTitle: Database Cache Parameters
ms:assetid: 715e5495-0cd8-430f-bf21-509cf03bfbfd
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269293(v=EXCHG.10)
ms:contentKeyID: 32765585
ms.date: 04/11/2016
ms.topic: reference
api_name: 
topic_type: 
- apiref
- kbArticle
api_type: 
- COM
api_location: 
ROBOTS: INDEX,FOLLOW

---

# Database Cache Parameters


_**Applies to:** Windows | Windows Server_

## Database Cache Parameters

This topic contains parameters that are used for the database cache.

*JET_paramBatchIOBufferMax*  
22  

This parameter controls the size of an auxiliary part of the database page cache that is used to simulate scatter gather I/O when it is otherwise not available. The size is in database pages.

**Windows XP and later:**  This parameter is obsolete and does not affect the operation of the database engine.


| 
|
| <p>Default Value:</p> | <p>256</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p>0, 2 – 2147483647</p> | 
| <p>Scope:</p> | <p>Global</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>No</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>No</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>Yes</p> | 
| <p>Affects Resources:</p> | <p>Yes</p> | 
| <p>Availability:</p> | <p>All</p> | 



*JET_paramCacheSize*  
41  

This parameter can be used to control the size of the database page cache at run time. Ordinarily, the cache will automatically tune its size as a function of database and machine activity levels. If the application sets this parameter to zero, then the cache will tune its own size in this manner. However, if the application sets this parameter to a non-zero value then the cache will adjust itself to that target size (in database pages). The cache will then hold its size at that threshold until given a new size or until it is released to choose its own size.

**Note**  The cache size is still subject to the limits imposed by **JET_paramCacheSizeMin** and **JET_paramCacheSizeMax**.

When this parameter is read, the actual size of the cache in database pages is returned. This size can be used by the application as an input to drive its manual adjustment of the cache size.


| 
|
| <p>Default Value:</p> | <p>Special</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p><strong>Windows 2000:</strong>  1 – 1048575</p><p><strong>Windows XP:</strong>  1 – 4294967295</p> | 
| <p>Scope:</p> | <p>Global</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>Yes</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>Yes</p> | 
| <p>Affects Resources:</p> | <p>Yes</p> | 
| <p>Availability:</p> | <p>All</p> | 



*JET_paramCacheSizeMin*  
60  

This parameter configures the minimum size of the database page cache. The size is in database pages.

By default, the database cache will automatically adjust its size between the limits set by **JET_paramCacheSizeMin** and **JET_paramCacheSizeMax**.

**Windows 2000:**  On Windows 2000, this parameter should be set to a value roughly equal to four times the number of threads that will be inside the ESE API at the same time. This is required to avoid deadlocks caused by an insufficient number of database page cache buffers to perform complex operations like B+ Tree splits.

**Windows XP and later:**  The cache manager will automatically set its own minimum cache size to avoid deadlocks.


| 
|
| <p>Default Value:</p> | <p><strong>Windows 2000:</strong>  64</p><p><strong>Windows XP:</strong>  1</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p><strong>Windows 2000:</strong>  1 – 1048575</p><p><strong>Windows XP:</strong>  1 – 4294967295</p> | 
| <p>Scope:</p> | <p>Global</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p><strong>Windows 2000:</strong>  No</p><p><strong>Windows XP:</strong>  Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p><strong>Windows 2000:</strong>  No</p><p><strong>Windows XP:</strong>  Yes</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>Yes</p> | 
| <p>Affects Resources:</p> | <p>Yes</p> | 
| <p>Availability:</p> | <p>All</p> | 



*JET_paramCacheSizeMax*  
23  

This parameter configures the maximum size of the database page cache. The size is in database pages.

By default, the database cache will automatically adjust its size between the limits set by **JET_paramCacheSizeMin** and **JET_paramCacheSizeMax**.

**Note**   If this parameter is left to its default value, then the maximum size of the cache will be set to the size of physical memory when [JetInit](./jetinit-function.md) is called.

**Windows Vista:**  As of Windows Vista, the default value of this parameter was changed to clarify this behavior.


| 
|
| <p>Default Value:</p> | <p><strong>Windows 2000, Windows XP and Windows Server 2003:</strong>  512</p><p><strong>Windows Vista:</strong>  2000000000</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p><strong>Windows 2000:</strong>  1 – 1048575</p><p><strong>Windows XP:</strong>  1 – 4294967295</p> | 
| <p>Scope:</p> | <p>Global</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p><strong>Windows 2000:</strong>  No</p><p><strong>Windows XP:</strong>  Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p><strong>Windows XP and Windows 2000:</strong>  No</p><p><strong>Windows Vista and Windows Server 2003:</strong>  Yes</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>Yes</p> | 
| <p>Affects Resources:</p> | <p>Yes</p> | 
| <p>Availability:</p> | <p>All</p> | 



*JET_paramCheckpointDepthMax*  
24 

This parameter controls how aggressively database pages are flushed from the database page cache to minimize the amount of time it will take to recover from a crash. The parameter is a threshold in bytes for about how many transaction log files will need to be replayed after a crash.

If circular logging is enabled using [JET_paramCircularLog](./transaction-log-parameters.md) then this parameter will also control the approximate amount of transaction log files that will be retained on disk.

It is important that this parameter not be set too low. As the value of this parameter approaches zero, the cache will become more and more aggressive when flushing database pages to disk. This not only results in an increased number of writes to the database files but it also indirectly causes an increased number of reads to those files as well. This can cause very significant performance problems in some cases. Unfortunately, setting the smallest optimal value for this parameter can only be done using experimentation with the target application.


| 
|
| <p>Default Value:</p> | <p>20971520</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p><strong>Windows 2000, Windows XP and Windows Server 2003:</strong>  0 – 2147483647</p><p><strong>Windows Vista:</strong>  All Values</p> | 
| <p>Scope:</p> | <p><strong>Windows 2000, Windows XP and Windows Server 2003:</strong> This parameter is global.</p><p><strong>Windows Vista:</strong>  This parameter is per instance.</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>Yes</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>Yes</p> | 
| <p>Affects Performance:</p> | <p>Yes</p> | 
| <p>Affects Resources:</p> | <p>Yes</p> | 
| <p>Availability:</p> | <p>All</p> | 



*JET_paramCheckpointIOMax*  
135  

This parameter controls the maximum number of concurrent writes that the database engine will use to flush modified database pages for the purpose of advancing the checkpoint. The value of this parameter can be used to balance the speed with which the checkpoint can be advanced versus the negative impact this process will have on the response time for other I/O operations to the disks holding the database.


| 
|
| <p>Default Value:</p> | <p>96</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p>8 – 1024</p> | 
| <p>Scope:</p> | <p>Global</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>Yes</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>Yes</p> | 
| <p>Affects Resources:</p> | <p>No</p> | 
| <p>Availability:</p> | <p>Windows Vista and later</p> | 



*JET_paramEnableViewCache*  
127  

When this parameter is **True**, the database engine will use database data directly from the Windows file cache rather than copying the cached data into its own private memory. Any database data that is modified will still be cached in private memory.

The intent of this mode is to further reduce the amount of private memory used by the database engine to cache database data.

The view cache may only be used if the use of the Windows file cache is enabled by setting JET_paramEnableFileCache to **True**.


| 
|
| <p>Default Value:</p> | <p>False</p> | 
| <p>Type:</p> | <p>Boolean</p> | 
| <p>Valid Range:</p> | <p>False, True</p> | 
| <p>Scope:</p> | <p>Global</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>No</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>No</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>Yes</p> | 
| <p>Affects Resources:</p> | <p>Yes</p> | 
| <p>Availability:</p> | <p>Windows Vista and later</p> | 



*JET_paramLRUKCorrInterval*  
25  

This parameter sets the time interval in microseconds over which two database page accesses are considered to be correlated. This correlation interval controls the sensitivity of the cache's page replacement algorithm (LRU-K) to successive page accesses. This in turn will affect which pages it chooses to keep cached.


| 
|
| <p>Default Value:</p> | <p>128000</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p><strong>Windows 2000, Windows XP and Windows Server 2003: </strong>    0 – 2147483647</p><p><strong>Windows Vista:</strong>  All Values</p> | 
| <p>Scope:</p> | <p>Global</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>No</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>No</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>Yes</p> | 
| <p>Affects Resources:</p> | <p>No</p> | 
| <p>Availability:</p> | <p>All</p> | 



*JET_paramLRUKHistoryMax*  
26  

This parameter sets the maximum number of non cached database pages for which database page access times will be retained. These history records allow the cache's page replacement algorithm (LRU-K) to more accurately detect popular pages that were wrongly evicted from the database page cache.

**Windows XP and Windows Server 2003:**  This parameter is ignored on Windows XP and Windows Server 2003 and does not affect the operation of the database engine.


| 
|
| <p>Default Value:</p> | <p><strong>Windows 2000:</strong>  1024</p><p><strong>Windows Vista:</strong>  100000</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p><strong>Windows 2000:</strong>  0 – 4194303</p><p><strong>Windows Vista:</strong>  All Values</p> | 
| <p>Scope:</p> | <p>Global</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>No</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>No</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>Yes</p> | 
| <p>Affects Resources:</p> | <p>Yes</p> | 
| <p>Availability:</p> | <p>All</p> | 



*JET_paramLRUKPolicy*  
27  

This parameter configures the number of database page accesses that are considered for determining the usefulness of the page. This parameter is essentially the K in LRU-K, the database page cache's page replacement algorithm.


| 
|
| <p>Default Value:</p> | <p>2</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p>1-2</p> | 
| <p>Scope:</p> | <p>Global</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>No</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>No</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>Yes</p> | 
| <p>Affects Resources:</p> | <p>No</p> | 
| <p>Availability:</p> | <p>All</p> | 



*JET_paramLRUKTimeout*  
28

This parameter indicates the period of time in seconds after which a page in the database page cache is considered to have lost a page access for the purpose of considering the usefulness of the page.


| 
|
| <p>Default Value:</p> | <p>100</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p><strong>Windows 2000, Windows XP and Windows Server 2003:</strong>  1 – 2147483647</p><p><strong>Windows Vista:</strong>   1 – 4294967295</p> | 
| <p>Scope:</p> | <p>Global</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>No</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>No</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>Yes</p> | 
| <p>Affects Resources:</p> | <p>No</p> | 
| <p>Availability:</p> | <p>All</p> | 



*JET_paramLRUKTrxCorrInterval*  
29  

This parameter is obsolete and does not affect the operation of the database engine.

*JET_paramStartFlushThreshold*  
31  

This parameter controls when the database page cache begins evicting pages from the cache to make room for pages that are not cached. When the number of page buffers in the cache drops below this threshold then a background process will be started to replenish that pool of available buffers. This threshold is always relative to the maximum cache size as set by **JET_paramCacheSizeMax**. This threshold must also always be less than the stop threshold as set by **JET_paramStopFlushThreshold**.

The distance height of the start threshold will determine the response time that the database page cache must have to produce available buffers before the application needs them. A high start threshold will give the background process more time to react. However, a high start threshold implies a higher stop threshold and that will reduce the effective size of the database page cache for modified pages (Windows 2000) or for all pages (Windows XP and later).


| 
|
| <p>Default Value:</p> | <p><strong>Windows 2000, Windows XP and Windows Server 2003:</strong>  5 (1%)</p><p><strong>Windows Vista:</strong>  20000000 (1%)</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p><strong>Windows 2000:</strong>  1 – 1048575</p><p><strong>Windows XP:</strong>  1 – 4294967295</p><p><strong>Windows Vista:</strong>  All Values</p> | 
| <p>Scope:</p> | <p>Global</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>Yes</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>Yes</p> | 
| <p>Affects Resources:</p> | <p>Yes</p> | 
| <p>Availability:</p> | <p>All</p> | 



*JET_paramStopFlushThreshold*  
32  

This parameter controls when the database page cache ends evicting pages from the cache to make room for pages that are not cached. When the number of page buffers in the cache rises above this threshold then the background process that was started to replenish that pool of available buffers is stopped. This threshold is always relative to the maximum cache size as set by **JET_paramCacheSizeMax**. This threshold must also always be greater than the start threshold as set by **JET_paramStartFlushThreshold**.

The distance between the start threshold and the stop threshold affects the efficiency with which database pages are flushed by the background process. A larger gap will make it more likely that writes to neighboring pages may be combined. However, a high stop threshold will reduce the effective size of the database page cache for modified pages (Windows 2000) or for all pages (Windows XP and later).


| 
|
| <p>Default Value:</p> | <p><strong>Windows 2000, Windows XP and Windows Server 2003:</strong>  10 (2%)</p><p><strong>Windows Vista:</strong>  40000000 (2%)</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p><strong>Windows 2000:</strong>  1 – 1048575</p><p><strong>Windows XP:</strong>  1 – 4294967295</p><p><strong>Windows Vista:</strong>  All Values</p> | 
| <p>Scope:</p> | <p>Global</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>Yes</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>Yes</p> | 
| <p>Affects Resources:</p> | <p>Yes</p> | 
| <p>Availability:</p> | <p>All</p> | 



### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 



### See Also

[JetCreateInstance](./jetcreateinstance-function.md)  
[JetInit](./jetinit-function.md)
