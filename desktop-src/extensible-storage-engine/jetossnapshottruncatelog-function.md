---
description: "Learn more about: JetOSSnapshotTruncateLog Function"
title: JetOSSnapshotTruncateLog Function
TOCTitle: JetOSSnapshotTruncateLog Function
ms:assetid: 3df8f5b2-8083-49b7-a325-fd13187f785c
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269231(v=EXCHG.10)
ms:contentKeyID: 32765533
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetOSSnapshotTruncateLog
topic_type: 
- apiref
- kbArticle
api_type: 
- DLLExport
- COM
api_location: 
- ESENT.DLL
ROBOTS: INDEX,FOLLOW

---

# JetOSSnapshotTruncateLog Function


_**Applies to:** Windows | Windows Server_

## JetOSSnapshotTruncateLog Function

The **JetOSSnapshotTruncateLog** function enables log truncation for all instances that are part of the snapshot session.

**Windows Vista:**  **JetOSSnapshotTruncateLog** is introduced in Windows Vista.

```cpp
    JET_ERR JET_API JetOSSnapshotTruncateLog(
      __in          const JET_OSSNAPID snapId,
      __in          const JET_GRBIT grbit
    );
```

### Parameters

*snapId*

The identifier of the snapshot session.

*grbit*

The options for this call. This parameter can have a combination of the following values.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Value</p></th>
<th><p>Meaning</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>JET_bitAllDatabasesSnapshot</p></td>
<td><p>All the databases are attached so the storage engine can compute and do the log truncation.</p></td>
</tr>
<tr class="even">
<td><p>0 (zero)</p></td>
<td><p>No truncation will occur.</p></td>
</tr>
</tbody>
</table>


### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Return code</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>JET_errSuccess</p></td>
<td><p>The operation completed successfully.</p></td>
</tr>
<tr class="even">
<td><p>JET_errInvalidGrbit</p></td>
<td><p>The <em>grbit</em> parameter is invalid.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errOSSnapshotInvalidSequence</p></td>
<td><p>The snapshot session is not in the state in which a truncation can occur. Possible causes are:</p>
<ul>
<li><p>the call is done after the snapshot session timed-out</p></li>
<li><p>the session was specified as a copy snapshot</p></li>
</ul></td>
</tr>
</tbody>
</table>


On success, the log files for one or all the instances part of the snapshot session will be truncated, if possible.

#### Remarks

This function should be called only if the snapshot was created with the JET_bitContinueAfterThaw option. Otherwise, the snapshot session would have ended after the [JetOSSnapshotThaw](./jetossnapshotthaw-function.md) call.

#### Requirements

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
<tr class="even">
<td><p><strong>Library</strong></p></td>
<td><p>Use ESENT.lib.</p></td>
</tr>
<tr class="odd">
<td><p><strong>DLL</strong></p></td>
<td><p>Requires ESENT.dll.</p></td>
</tr>
</tbody>
</table>


#### See Also

[Error Handling Parameters](./error-handling-parameters.md)  
[Extensible Storage Engine Errors](./extensible-storage-engine-errors.md)  
[JET_ERR](./jet-err.md)  
[JetOSSnapshotEnd](./jetossnapshotend-function.md)  
[JetOSSnapshotFreeze](./jetossnapshotfreeze-function.md)  
[JetOSSnapshotPrepare](./jetossnapshotprepare-function.md)  
[JetOSSnapshotThaw](./jetossnapshotthaw-function.md)
