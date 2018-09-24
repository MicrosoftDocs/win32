---
title: JetOSSnapshotAbort Function
TOCTitle: JetOSSnapshotAbort Function
ms:assetid: 629455af-b526-4366-9b9a-112757f72c32
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/Gg269265(v=EXCHG.10)
ms:contentKeyID: 32765567
ms.date: 04/11/2016
mtps_version: v=EXCHG.10
api_name: 
- JetOSSnapshotAbort
topic_type: 
- apiref
- kbArticle
api_type: 
- COM
- DLLExport
api_location: 
- ESENT.DLL
ROBOTS: INDEX,FOLLOW

---

# JetOSSnapshotAbort Function


_**Applies to:** Windows | Windows Server_

## JetOSSnapshotAbort Function

The **JetOSSnapshotAbort** function notifies the engine that it can resume normal IO operations after a freeze period ended with a failed snapshot.

**Windows Server 2003:**  **JetOSSnapshotAbort** is introduced in Windows Server 2003.

    JET_ERR JET_API JetOSSnapshotAbort(
      __in          const JET_OSSNAPID snapId,
      __in          const JET_GRBIT grbit
    );

### Parameters

*snapId*

The identifier of the snapshot session.

*grbit*

The options for this call. This parameter is reserved for future use and the only valid value supported is 0 (zero).

### Return Value

This function returns the [JET\_ERR](gg294092\(v=exchg.10\).md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](gg269184\(v=exchg.10\).md) and [Error Handling Parameters](gg269173\(v=exchg.10\).md).

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
<td><p>JET_errInvalidParameter</p></td>
<td><p>The snapshot session is invalid or the grbit parameter is invalid.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errOSSnapshotInvalidSnapId</p></td>
<td><p>The identifier for the snapshot session is not valid.</p></td>
</tr>
</tbody>
</table>


If this function succeeds, the snapshot session will end and the normal engine behavior will resume. A new snapshot session can be started at a later point.

If this function fails, the snapshot session will not be aborted.

#### Remarks

This function should be called instead of [JetOSSnapshotThaw](gg269229\(v=exchg.10\).md) to inform the engine that the snapshot was aborted for reasons that don't relate to the engine. This information can be used later to help issue event log messages about the snapshot session or to help determine other appropriate actions.

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
<td><p>Requires Windows Server 2008 or Windows Server 2003.</p></td>
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

[JET\_ERR](gg294092\(v=exchg.10\).md)  
[JET\_OSSNAPID](gg269325\(v=exchg.10\).md)  
[JetOSSnapshotFreeze](gg269332\(v=exchg.10\).md)  
[JetOSSnapshotPrepare](gg269224\(v=exchg.10\).md)  
[JetOSSnapshotThaw](gg269229\(v=exchg.10\).md)

