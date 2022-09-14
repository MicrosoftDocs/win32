---
description: "Learn more about: Resource Parameters"
title: Resource Parameters
TOCTitle: Resource Parameters
ms:assetid: 1f61845a-ffa5-4894-9fe0-a58737b3b54e
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269201(v=EXCHG.10)
ms:contentKeyID: 32765504
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

# Resource Parameters


_**Applies to:** Windows | Windows Server_

## Resource Parameters

This topic contains parameters that are used for resources.

*JET_paramCachedClosedTables*  
125  

This parameter controls the number of B+ Tree resources cached by the instance after the tables they represent have been closed by the application.

Large values for this parameter will cause the database engine to use more memory but will increase the speed with which a large number of tables can be opened randomly by the application. This is useful for applications that have a schema with a very large number of tables.


| Label | Value |
|--------|-------|
| <p>Default Value:</p> | <p>64</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p>1 – 2147483647</p> | 
| <p>Scope:</p> | <p>Instance</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>No</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>Yes</p> | 
| <p>Affects Resources:</p> | <p>Yes</p> | 
| <p>Availability:</p> | <p>Windows Vista and later releases</p> | 



*JET_paramDisablePerfmon*  
107  

This parameter can be used to prevent the database engine from publishing data about its performance to Windows. This can be done to reduce the service thread activity of the database engine.


| Label | Value |
|--------|-------|
| <p>Default Value:</p> | <p>False</p> | 
| <p>Type:</p> | <p>Boolean</p> | 
| <p>Valid Range:</p> | <p>False, True</p> | 
| <p>Scope:</p> | <p>Global</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>No</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>No</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>No</p> | 
| <p>Affects Resources:</p> | <p>Yes</p> | 
| <p>Availability:</p> | <p>Windows Vista and later releases</p> | 



*JET_paramGlobalMinVerPages*  
81  

This parameter allows applications that operate in multi-instance mode to pre-allocate memory for version pages in a global pool to emulate the older behavior. This is useful in case the application wishes to guarantee that transactions of a certain size can succeed later on even if memory becomes scarce.

**Windows 2000:**  Enough memory to back all version pages is always reserved at [JetInit](./jetinit-function.md) time.

**Windows XP:**  As of Windows XP, this is still true when in single instance mode. However, version page memory is dynamically allocated when in multi-instance mode.


| Label | Value |
|--------|-------|
| <p>Default Value:</p> | <p>64</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p>1 – 2147483647</p> | 
| <p>Scope:</p> | <p>Global</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>No</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>No</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>Yes</p> | 
| <p>Affects Performance:</p> | <p>No</p> | 
| <p>Affects Resources:</p> | <p>Yes</p> | 
| <p>Availability:</p> | <p>Windows XP and later releases</p> | 



*JET_paramMaxCursors*  
8  

This parameter reserves the requested number of cursor resources for use by an instance. A cursor resource directly corresponds to a [JET_TABLEID](./jet-tableid.md) data type. This setting will affect how many cursors can be used at the same time. A cursor resource cannot be shared by different sessions so this parameter must be set to a large enough value so that each session can use as many cursors as are required.

**Windows 2000, Windows XP and Windows Server 2003:**  Large values for this parameter will consume address space and may increase memory usage.


| Label | Value |
|--------|-------|
| <p>Default Value:</p> | <p>1024</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p>0 – 2147483647</p> | 
| <p>Scope:</p> | <p>Instance</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>No</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>No</p> | 
| <p>Affects Resources:</p> | <p>Yes</p> | 
| <p>Availability:</p> | <p>All</p> | 



*JET_paramMaxInstances*  
104  

This parameter controls the maximum number of instances that can be created in a single process.


| Label | Value |
|--------|-------|
| <p>Default Value:</p> | <p>16</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p>1-1024</p> | 
| <p>Scope:</p> | <p>Global</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>No</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>No</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>Yes</p> | 
| <p>Affects Resources:</p> | <p>Yes</p> | 
| <p>Availability:</p> | <p>Windows XP and later releases</p> | 



*JET_paramMaxOpenTables*  
6  

This parameter reserves the requested number of B+ Tree resources for use by an instance. This setting will affect how many tables can be used at the same time. This parameter needs to be set relative to the physical schema of the databases in use by the database engine, so this setting is not as straightforward as it could be.

In general, you will need two resources plus one resource per secondary index per table in concurrent use by the application.

**Windows 2000, Windows XP and Windows Server 2003:**  Large values for this parameter will consume address space and may increase memory usage.


| Label | Value |
|--------|-------|
| <p>Default Value:</p> | <p>300</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p>0 – 2147483647</p> | 
| <p>Scope:</p> | <p>Instance</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>No</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>No</p> | 
| <p>Affects Resources:</p> | <p>Yes</p> | 
| <p>Availability:</p> | <p>All</p> | 



*JET_paramMaxSessions*  
5  

This parameter reserves the requested number of session resources for use by an instance. A session resource directly corresponds to a [JET_SESID](./jet-sesid.md) data type. This setting will affect how many sessions can be used at the same time.

**Windows 2000, Windows XP and Windows Server 2003:**  Large values for this parameter will consume address space and may increase memory usage.


| Label | Value |
|--------|-------|
| <p>Default Value:</p> | <p>16</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p>0 – 30000</p> | 
| <p>Scope:</p> | <p>Instance</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>No</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>No</p> | 
| <p>Affects Resources:</p> | <p>Yes</p> | 
| <p>Availability:</p> | <p>All</p> | 



*JET_paramMaxTemporaryTables*  
10  

This parameter reserves the requested number of temporary table resources for use by an instance. This setting will affect how many temporary tables can be used at the same time.

**Windows 2000, Windows XP and Windows Server 2003:**  Large values for this parameter will consume address space and may increase memory usage.

**Windows XP and later:**  If this system parameter is set to zero then no temporary database will be created and any activity that requires use of the temporary database will fail. This setting can be useful to avoid the I/O required to create the temporary database if it is known that it will not be used.

**Note**  The use of a temporary table also requires a cursor resource.


| Label | Value |
|--------|-------|
| <p>Default Value:</p> | <p>20</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p>0 – 2147483647</p> | 
| <p>Scope:</p> | <p>Instance</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>No</p> | 
| <p>Affects Physical Layout:</p> | <p>Yes</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>No</p> | 
| <p>Affects Resources:</p> | <p>Yes</p> | 
| <p>Availability:</p> | <p>All</p> | 



*JET_paramMaxVerPages*  
9  

This parameter reserves the requested number of version store pages for use by an instance. The version store holds a live record of all the different versions of each record or index entry in the database that can be seen by all active transactions. These versions are used to support the multi-versioned concurrency control in use by the database engine to support transactions using snapshot isolation. This setting will affect how many updates can be held in memory at a time. This in turn will affect either the maximum number of updates a single transaction can perform, the maximum duration a transaction can be held open, the maximum concurrent load of updating transactions on the system, or a combination of these.

Each version store page as configured by this parameter is 16KB in size on 32-bit machines, and 32KB on 64-bit machines.

**Windows Vista and later:**  The version store page size can be read and changed via JET_paramVerPageSize.

**Windows 2000, Windows XP and Windows Server 2003:**  Large values for this parameter will consume address space and may increase memory usage.

**Note**  This is by far the most common resource to be exhausted by the database engine. Careful attention must be paid to the setting of the system parameter and to the transactional load of the application to avoid exhausting this resource under normal operation. When this resource is exhausted, updates to the database will be rejected with JET_errVersionStoreOutOfMemory. To release some of these resources, the oldest outstanding transaction must be aborted.


| Label | Value |
|--------|-------|
| <p>Default Value:</p> | <p>64</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p>1 – 2147483647</p> | 
| <p>Scope:</p> | <p>Instance</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>No</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>Yes</p> | 
| <p>Affects Performance:</p> | <p>No</p> | 
| <p>Affects Resources:</p> | <p>Yes</p> | 
| <p>Availability:</p> | <p>All</p> | 



*JET_paramPageHintCacheSize*  
101  

This parameter controls the size of a special cache used to accelerate the lookup of B+ Tree child page pointers in the database page cache. The size of the cache is in bytes.


| Label | Value |
|--------|-------|
| <p>Default Value:</p> | <p>262144</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p>0 – 2147483647</p> | 
| <p>Scope:</p> | <p>Global</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>Yes</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>Yes</p> | 
| <p>Affects Resources:</p> | <p>Yes</p> | 
| <p>Availability:</p> | <p>Windows XP and later releases</p> | 



*JET_paramPreferredMaxOpenTables*  
7  

This parameter attempts to keep the number of B+ Tree resources in use below the specified threshold.

If this parameter is set to zero then it will default to 100% of **JET_paramMaxOpenTables**.

**Windows Vista and later:**  This parameter is obsolete and does not affect the operation of the database engine. Applications should use JET_paramMaxCachedClosedTables instead.


| Label | Value |
|--------|-------|
| <p>Default Value:</p> | <p>0 (100% of <strong>JET_paramMaxOpenTables</strong>)</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p>0 – 2147483647</p> | 
| <p>Scope:</p> | <p>Instance</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>No</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>Yes</p> | 
| <p>Affects Resources:</p> | <p>Yes</p> | 
| <p>Availability:</p> | <p>All</p> | 



*JET_paramPreferredVerPages*  
63  

This parameter represents a threshold relative to **JET_paramMaxVerPages** that controls the discretionary use of version pages by the database engine. If the size of the version store exceeds this threshold then any information that is only used for optional background tasks, such as reclaiming deleted space in the database, is instead sacrificed to preserve room for transactional information.

**Windows 2000, Windows XP and Windows Server 2003:**  Setting this parameter to zero would set the threshold to be 90% of **JET_paramMaxVerPages**.

**Windows Vista and later:**  This is no longer supported and the default value of this parameter was changed to clarify its behavior.

Each version store page as configured by this parameter is 16KB in size on 32-bit machines, and 32KB on 64-bit machines.

**Windows Vista and later:**  The version store page size can be read and changed via JET_paramVerPageSize.

**Note**  If the database engine operates above this threshold too often then it is possible for the database to degrade in performance. This happens because the background processes that clean up the database cannot function without the optional information that is thrown away in this scenario. Online or offline defragmentation will counteract this effect.


| Label | Value |
|--------|-------|
| <p>Default Value:</p> | <p><strong>Windows 2000, Windows XP and Windows Server 2003:</strong>  0 (90% of JET_paramMaxVerPages)</p><p><strong>Windows Vista:</strong>  58</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p>1 – 2147483647</p> | 
| <p>Scope:</p> | <p>Instance</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>Yes</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>Yes</p> | 
| <p>Affects Performance:</p> | <p>Yes</p> | 
| <p>Affects Resources:</p> | <p>Yes</p> | 
| <p>Availability:</p> | <p>All</p> | 



*JET_paramVerPageSize*  
128  

This parameter controls the size of the version store pages used by the database engine to hold transactional information. The value of this parameter is the unit size for all the other system parameters that are in terms of version pages (e.g. JET_paramMaxVerPages).

The database engine may choose to use a larger version store page size than requested.


| Label | Value |
|--------|-------|
| <p>Default Value:</p> | <p>16384</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p>1024, 2048, 4096, 8192, 16384, 32768, 65536</p> | 
| <p>Scope:</p> | <p>Global</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>No</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>No</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>No</p> | 
| <p>Affects Resources:</p> | <p>Yes</p> | 
| <p>Availability:</p> | <p>Windows Vista and later</p> | 



*JET_paramVersionStoreTaskQueueMax*  
105  

This parameter controls the number of background cleanup work items that can be queued to the database engine thread pool at any one time.


| Label | Value |
|--------|-------|
| <p>Default Value:</p> | <p>32</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p><strong>Windows XP and Windows Server 2003:  </strong>  1 – 63</p><p><strong>Windows Vista:</strong>  1 – 127</p> | 
| <p>Scope:</p> | <p>Instance</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p><strong>Windows XP and Windows Server 2003:  </strong>  No</p><p><strong>Windows Vista:</strong>  Yes</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>Yes</p> | 
| <p>Affects Resources:</p> | <p>Yes</p> | 
| <p>Availability:</p> | <p>Windows XP and later releases</p> | 



### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 



### See Also

[JetCreateInstance](./jetcreateinstance-function.md)  
[JetInit](./jetinit-function.md)
