---
title: Meta Parameters
TOCTitle: Meta Parameters
ms:assetid: 947e9342-7916-4e62-85e5-2d18805000c0
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/Gg269346(v=EXCHG.10)
ms:contentKeyID: 32765634
ms.date: 04/11/2016
ms.topic: article
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

JET\_paramConfiguration  
129  
This parameter exposes multiple sets of default values for the entire set of system parameters. When this parameter is set to a specific configuration, all system parameter values are reset to their default values for that configuration. If the configuration is set for a specific instance then global system parameters will not be reset to their default values.

In addition, the parameter itself can have other effects on the behavior of the database engine.

At this time, there are two supported configurations:

  - Small Configuration (0): The database engine is optimized for memory use.

  - Legacy Configuration (1): The database engine has its traditional defaults.

Small Configuration changes the defaults of the following system parameters to the specified values:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>System Parameter</p></th>
<th><p>New Default Value</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>JET_paramMaxSessions</p></td>
<td><p>30000</p></td>
</tr>
<tr class="even">
<td><p>JET_paramMaxOpenTables</p></td>
<td><p>2147483647</p></td>
</tr>
<tr class="odd">
<td><p>JET_paramMaxCursors</p></td>
<td><p>2147483647</p></td>
</tr>
<tr class="even">
<td><p>JET_paramMaxVerPages</p></td>
<td><p>2147483647</p></td>
</tr>
<tr class="odd">
<td><p>JET_paramMaxTemporaryTables</p></td>
<td><p>2147483647</p></td>
</tr>
<tr class="even">
<td><p>JET_paramLogFileSize</p></td>
<td><p>64</p></td>
</tr>
<tr class="odd">
<td><p>JET_paramLogBuffers</p></td>
<td><p>1</p></td>
</tr>
<tr class="even">
<td><p>JET_paramDbExtensionSize</p></td>
<td><p>16</p></td>
</tr>
<tr class="odd">
<td><p>JET_paramPageTempDBMin</p></td>
<td><p>14</p></td>
</tr>
<tr class="even">
<td><p>JET_paramCacheSizeMax</p></td>
<td><p>16</p></td>
</tr>
<tr class="odd">
<td><p>JET_paramCheckpointDepthMax</p></td>
<td><p>65536</p></td>
</tr>
<tr class="even">
<td><p>JET_paramLRUKHistoryMax</p></td>
<td><p>10</p></td>
</tr>
<tr class="odd">
<td><p>JET_paramOutstandingIOMax</p></td>
<td><p>16</p></td>
</tr>
<tr class="even">
<td><p>JET_paramStartFlushThreshold</p></td>
<td><p>1</p></td>
</tr>
<tr class="odd">
<td><p>JET_paramStopFlushThreshold</p></td>
<td><p>2</p></td>
</tr>
<tr class="even">
<td><p>JET_paramNoInformationEvent</p></td>
<td><p>1</p></td>
</tr>
<tr class="odd">
<td><p>JET_paramCacheSizeMin</p></td>
<td><p>16</p></td>
</tr>
<tr class="even">
<td><p>JET_paramPreferredVerPages</p></td>
<td><p>2147483647</p></td>
</tr>
<tr class="odd">
<td><p>JET_paramLogFileCreateAsynch</p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p>JET_paramGlobalMinVerPages</p></td>
<td><p>1</p></td>
</tr>
<tr class="odd">
<td><p>JET_paramPageHintCacheSize</p></td>
<td><p>32</p></td>
</tr>
<tr class="even">
<td><p>JET_paramDisablePerfmon</p></td>
<td><p>1</p></td>
</tr>
<tr class="odd">
<td><p>JET_paramEnableFileCache</p></td>
<td><p>1</p></td>
</tr>
<tr class="even">
<td><p>JET_paramEnableViewCache</p></td>
<td><p>1</p></td>
</tr>
<tr class="odd">
<td><p>JET_paramVerPageSize</p></td>
<td><p>1024</p></td>
</tr>
<tr class="even">
<td><p>JET_paramEnableAdvanced</p></td>
<td><p>0</p></td>
</tr>
<tr class="odd">
<td><p>JET_paramCheckpointIOMax</p></td>
<td><p>8</p></td>
</tr>
</tbody>
</table>


Small Configuration also has several other effects on the database engine, including:

  - All resources managed by system parameters are allocated from the heap as needed

  - Other internal resources used by the database engine are scaled down in size

  - Various maintenance activities are scaled back to avoid background thread activity

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Default Value:</p></td>
<td><p>1 (Legacy)</p></td>
</tr>
<tr class="even">
<td><p>Type:</p></td>
<td><p>Integer</p></td>
</tr>
<tr class="odd">
<td><p>Valid Range:</p></td>
<td><p>0 – 1</p></td>
</tr>
<tr class="even">
<td><p>Scope:</p></td>
<td><p>Instance</p></td>
</tr>
<tr class="odd">
<td><p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p></td>
<td><p>No</p></td>
</tr>
<tr class="odd">
<td><p>Affects Physical Layout:</p></td>
<td><p>No</p></td>
</tr>
<tr class="even">
<td><p>Affects Reliability:</p></td>
<td><p>No</p></td>
</tr>
<tr class="odd">
<td><p>Affects Performance:</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p>Affects Resources:</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p>Availability:</p></td>
<td><p>Starting with Windows Server 2008 and Windows Vista</p></td>
</tr>
</tbody>
</table>


JET\_paramEnableAdvanced  
130  
This parameter is used to control when the database engine accepts or rejects changes to a subset of the system parameters. This parameter is used in conjunction with JET\_paramConfiguration to prevent some system parameters from being set away from the selected configuration's defaults.

The following system parameters will be protected from being set when this parameter is set to False:

  - JET\_paramMaxSessionsfon

  - JET\_paramMaxOpenTables

  - JET\_paramPreferredMaxOpenTables

  - JET\_paramMaxCursors

  - JET\_paramMaxVerPages

  - JET\_paramMaxTemporaryTables

  - JET\_paramLogBuffers

  - JET\_paramWaitLogFlush

  - JET\_paramLogCheckpointPeriod

  - JET\_paramLogWaitingUserMax

  - JET\_paramDbExtensionSize

  - JET\_paramPageTempDBMin

  - JET\_paramPageFragment

  - JET\_paramBatchIOBufferMax

  - JET\_paramCacheSizeMax

  - JET\_paramLRUKCorrInterval

  - JET\_paramLRUKHistoryMax

  - JET\_paramLRUKPolicy

  - JET\_paramLRUKTimeout

  - JET\_paramLRUKTrxCorrInterval

  - JET\_paramOutstandingIOMax

  - JET\_paramStartFlushThreshold

  - JET\_paramStopFlushThreshold

  - JET\_paramCacheSize

  - JET\_paramCacheSizeMin

  - JET\_paramPreferredVerPages

  - JET\_paramBackupChunkSize

  - JET\_paramBackupOutstandingReads

  - JET\_paramLogFileCreateAsynch

  - JET\_paramRecordUpgradeDirtyLevel

  - JET\_paramGlobalMinVerPages

  - JET\_paramPageHintCacheSize

  - JET\_paramVersionStoreTaskQueueMax

  - JET\_paramDBAPageAvailMin

  - JET\_paramMaxRandomIOSize

  - JET\_paramCachedClosedTables

  - JET\_paramEnableFileCache

  - JET\_paramEnableViewCache

  - JET\_paramVerPageSize

  - JET\_paramCheckpointIOMax

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Default Value:</p></td>
<td><p>True</p></td>
</tr>
<tr class="even">
<td><p>Type:</p></td>
<td><p>Boolean</p></td>
</tr>
<tr class="odd">
<td><p>Valid Range:</p></td>
<td><p>False, True</p></td>
</tr>
<tr class="even">
<td><p>Scope:</p></td>
<td><p>Instance</p></td>
</tr>
<tr class="odd">
<td><p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p>Affects Physical Layout:</p></td>
<td><p>No</p></td>
</tr>
<tr class="even">
<td><p>Affects Reliability:</p></td>
<td><p>No</p></td>
</tr>
<tr class="odd">
<td><p>Affects Performance:</p></td>
<td><p>No</p></td>
</tr>
<tr class="even">
<td><p>Affects Resources:</p></td>
<td><p>No</p></td>
</tr>
<tr class="odd">
<td><p>Availability:</p></td>
<td><p>Starting with Windows Server 2008 and Windows Vista</p></td>
</tr>
</tbody>
</table>


### Requirements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Client</strong></p></td>
<td><p>Requires Windows Vista.</p></td>
</tr>
<tr class="even">
<td><p><strong>Server</strong></p></td>
<td><p>Requires Windows Server 2008.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Header</strong></p></td>
<td><p>Declared in Esent.h.</p></td>
</tr>
</tbody>
</table>


### See Also

[JetCreateInstance](gg269354\(v=exchg.10\).md)  
[JetInit](gg294068\(v=exchg.10\).md)

