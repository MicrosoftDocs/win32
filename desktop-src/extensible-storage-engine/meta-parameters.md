---
description: "Learn more about: Meta Parameters"
title: Meta Parameters
TOCTitle: Meta Parameters
ms:assetid: 947e9342-7916-4e62-85e5-2d18805000c0
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269346(v=EXCHG.10)
ms:contentKeyID: 32765634
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

# Meta Parameters


_**Applies to:** Windows | Windows Server_

## Meta Parameters

This topic contains parameters that are used to control other parameters.

JET_paramConfiguration  
129  
This parameter exposes multiple sets of default values for the entire set of system parameters. When this parameter is set to a specific configuration, all system parameter values are reset to their default values for that configuration. If the configuration is set for a specific instance then global system parameters will not be reset to their default values.

In addition, the parameter itself can have other effects on the behavior of the database engine.

At this time, there are two supported configurations:

  - Small Configuration (0): The database engine is optimized for memory use.

  - Legacy Configuration (1): The database engine has its traditional defaults.

Small Configuration changes the defaults of the following system parameters to the specified values:


| <p>System Parameter</p> | <p>New Default Value</p> | 
|-------------------------|--------------------------|
| <p>JET_paramMaxSessions</p> | <p>30000</p> | 
| <p>JET_paramMaxOpenTables</p> | <p>2147483647</p> | 
| <p>JET_paramMaxCursors</p> | <p>2147483647</p> | 
| <p>JET_paramMaxVerPages</p> | <p>2147483647</p> | 
| <p>JET_paramMaxTemporaryTables</p> | <p>2147483647</p> | 
| <p>JET_paramLogFileSize</p> | <p>64</p> | 
| <p>JET_paramLogBuffers</p> | <p>1</p> | 
| <p>JET_paramDbExtensionSize</p> | <p>16</p> | 
| <p>JET_paramPageTempDBMin</p> | <p>14</p> | 
| <p>JET_paramCacheSizeMax</p> | <p>16</p> | 
| <p>JET_paramCheckpointDepthMax</p> | <p>65536</p> | 
| <p>JET_paramLRUKHistoryMax</p> | <p>10</p> | 
| <p>JET_paramOutstandingIOMax</p> | <p>16</p> | 
| <p>JET_paramStartFlushThreshold</p> | <p>1</p> | 
| <p>JET_paramStopFlushThreshold</p> | <p>2</p> | 
| <p>JET_paramNoInformationEvent</p> | <p>1</p> | 
| <p>JET_paramCacheSizeMin</p> | <p>16</p> | 
| <p>JET_paramPreferredVerPages</p> | <p>2147483647</p> | 
| <p>JET_paramLogFileCreateAsynch</p> | <p>0</p> | 
| <p>JET_paramGlobalMinVerPages</p> | <p>1</p> | 
| <p>JET_paramPageHintCacheSize</p> | <p>32</p> | 
| <p>JET_paramDisablePerfmon</p> | <p>1</p> | 
| <p>JET_paramEnableFileCache</p> | <p>1</p> | 
| <p>JET_paramEnableViewCache</p> | <p>1</p> | 
| <p>JET_paramVerPageSize</p> | <p>1024</p> | 
| <p>JET_paramEnableAdvanced</p> | <p>0</p> | 
| <p>JET_paramCheckpointIOMax</p> | <p>8</p> | 



Small Configuration also has several other effects on the database engine, including:

  - All resources managed by system parameters are allocated from the heap as needed

  - Other internal resources used by the database engine are scaled down in size

  - Various maintenance activities are scaled back to avoid background thread activity


| 
|
| <p>Default Value:</p> | <p>1 (Legacy)</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p>0 – 1</p> | 
| <p>Scope:</p> | <p>Instance</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>No</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>Yes</p> | 
| <p>Affects Resources:</p> | <p>Yes</p> | 
| <p>Availability:</p> | <p>Starting with Windows Server 2008 and Windows Vista</p> | 



JET_paramEnableAdvanced  
130  
This parameter is used to control when the database engine accepts or rejects changes to a subset of the system parameters. This parameter is used in conjunction with JET_paramConfiguration to prevent some system parameters from being set away from the selected configuration's defaults.

The following system parameters will be protected from being set when this parameter is set to False:

  - JET_paramMaxSessionsfon

  - JET_paramMaxOpenTables

  - JET_paramPreferredMaxOpenTables

  - JET_paramMaxCursors

  - JET_paramMaxVerPages

  - JET_paramMaxTemporaryTables

  - JET_paramLogBuffers

  - JET_paramWaitLogFlush

  - JET_paramLogCheckpointPeriod

  - JET_paramLogWaitingUserMax

  - JET_paramDbExtensionSize

  - JET_paramPageTempDBMin

  - JET_paramPageFragment

  - JET_paramBatchIOBufferMax

  - JET_paramCacheSizeMax

  - JET_paramLRUKCorrInterval

  - JET_paramLRUKHistoryMax

  - JET_paramLRUKPolicy

  - JET_paramLRUKTimeout

  - JET_paramLRUKTrxCorrInterval

  - JET_paramOutstandingIOMax

  - JET_paramStartFlushThreshold

  - JET_paramStopFlushThreshold

  - JET_paramCacheSize

  - JET_paramCacheSizeMin

  - JET_paramPreferredVerPages

  - JET_paramBackupChunkSize

  - JET_paramBackupOutstandingReads

  - JET_paramLogFileCreateAsynch

  - JET_paramRecordUpgradeDirtyLevel

  - JET_paramGlobalMinVerPages

  - JET_paramPageHintCacheSize

  - JET_paramVersionStoreTaskQueueMax

  - JET_paramDBAPageAvailMin

  - JET_paramMaxRandomIOSize

  - JET_paramCachedClosedTables

  - JET_paramEnableFileCache

  - JET_paramEnableViewCache

  - JET_paramVerPageSize

  - JET_paramCheckpointIOMax


| 
|
| <p>Default Value:</p> | <p>True</p> | 
| <p>Type:</p> | <p>Boolean</p> | 
| <p>Valid Range:</p> | <p>False, True</p> | 
| <p>Scope:</p> | <p>Instance</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>Yes</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>No</p> | 
| <p>Affects Resources:</p> | <p>No</p> | 
| <p>Availability:</p> | <p>Starting with Windows Server 2008 and Windows Vista</p> | 



### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 



### See Also

[JetCreateInstance](./jetcreateinstance-function.md)  
[JetInit](./jetinit-function.md)
