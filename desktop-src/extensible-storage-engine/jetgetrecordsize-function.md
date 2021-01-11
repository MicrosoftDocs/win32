---
description: "Learn more about: JetGetRecordSize Function"
title: JetGetRecordSize Function
TOCTitle: JetGetRecordSize Function
ms:assetid: a28567ed-c732-4509-9f8d-6f8104f62a86
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294045(v=EXCHG.10)
ms:contentKeyID: 32765644
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetGetRecordSize
topic_type: 
- kbArticle
- apiref
api_type: 
- COM
- DLLExport
api_location: 
- ESENT.DLL
ROBOTS: INDEX,FOLLOW

---

# JetGetRecordSize Function


_**Applies to:** Windows | Windows Server_

## JetGetRecordSize Function

The **JetGetRecordSize** function retrieves record size information from the desired location.

**Windows Vista:  JetGetRecordSize** is introduced in Windows Vista.

```cpp
    JET_ERR JET_API JetGetRecordSize(
      __in          JET_SESID sesid,
      __in          JET_TABLEID tableid,
      __out         JET_RECSIZE* precsize,
      __in          const JET_GRBIT grbit
    );
```

### Parameters

*sesid*

Identifies the database session context that will be used for the API call.

*tableid*

Identifies the table or cursor that will be used for the API call. The cursor must be positioned on a record, or have an update prepared.

*precsize*

A pointer to an output buffer for the [JET_RECSIZE](./jet-recsize-structure.md) structure.

*grbit*

This is one or more of the following values.

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
<td><p>JET_bitRecordSizeInCopyBuffer</p></td>
<td><p>This retrieves the size of the record that is in the copy buffer prepared for update. Otherwise, the <em>tableid</em> or cursor must be positioned on a record, and that record will be used.</p></td>
</tr>
<tr class="even">
<td><p>JET_bitRecordSizeRunningTotal</p></td>
<td><p>When this bit is specified, the <a href="gg294072(v=exchg.10).md">JET_RECSIZE</a> is not zeroed before filling the contents, effectively acting as an accumulation of the statistics for multiple records visited or updated.</p></td>
</tr>
<tr class="odd">
<td><p>JET_bitRecordSizeLocal</p></td>
<td><p>This causes the API to ignore non-intrinsic Long Values. For example, only the local record on the page will be used.</p></td>
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
<td><p>One of the requested options was invalid or not implemented. This error will be returned by the <strong>JetGetRecordSize</strong> function when an illegal <em>grbit</em> is specified.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errNotInitialized</p></td>
<td><p>It is not possible to complete the operation because the instance associated with the session has not been initialized.</p></td>
</tr>
<tr class="even">
<td><p>JET_errClientRequestToStopJetService</p></td>
<td><p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errInstanceUnavailable</p></td>
<td><p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data.</p>
<p><strong>Windows XP:</strong>  JET_errInstanceUnavailable will only be returned by Windows XP and later releases.</p></td>
</tr>
<tr class="even">
<td><p>JET_errTermInProgress</p></td>
<td><p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errRestoreInProgress</p></td>
<td><p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p></td>
</tr>
<tr class="even">
<td><p>JET_errSessionSharingViolation</p></td>
<td><p>It is illegal to use the same session from more than one thread at the same time.</p>
<p><strong>Windows XP:</strong>  JET_errInstanceUnavailable will only be returned by Windows XP and later releases.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errNoCurrentRecord</p></td>
<td><p>This can happen if the cursor was positioned incorrectly.</p></td>
</tr>
<tr class="even">
<td><p>JET_errRecordDeleted</p></td>
<td><p>If the cursor was not positioned in a transaction, this can happen if another thread deletes the record out from under this session.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errInvalidParameter</p></td>
<td><p>This can be returned if a <strong>NULL</strong><em>precsize</em> was passed.</p></td>
</tr>
</tbody>
</table>


#### Remarks

The size of the key accumulated in the **cbOverhead** field of [JET_RECSIZE](./jet-recsize-structure.md), is affected by JET_bitRecordSizeInCopyBuffer. If this bit is specified, the key size accumulated in the **cbOverhead** field is the full key size. If this bit is not used, then the key size accumulated will not include any size saved due to key prefix compression.

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

[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_SESID](./jet-sesid.md)  
[JET_RECSIZE](./jet-recsize-structure.md)  
[JET_TABLEID](./jet-tableid.md)
