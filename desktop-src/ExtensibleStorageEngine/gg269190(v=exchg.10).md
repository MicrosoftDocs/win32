---
title: JetUpdate2 Function
TOCTitle: JetUpdate2 Function
ms:assetid: 125f372c-9c4c-4be8-b0df-bbf53d79e90b
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/Gg269190(v=EXCHG.10)
ms:contentKeyID: 32765493
ms.date: 04/11/2016
ms.topic: article
api_name: 
- JetUpdate2
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

# JetUpdate2 Function


_**Applies to:** Windows | Windows Server_

## JetUpdate2 Function

The **JetUpdate2** function performs an update operation including inserting a new row into a table or updating an existing row. This function contains a list of *grbit* options that can be set while performing an update. Deleting a table row is performed by calling [JetDelete](gg269315\(v=exchg.10\).md).

**Windows Server 2003:  JetUpdate2** is introduced in Windows Server 2003.

**JetUpdate2** is the final step in performing an insert or an update. The update is begun by calling [JetPrepareUpdate](gg269339\(v=exchg.10\).md) and then by calling [JetSetColumn](gg294137\(v=exchg.10\).md) or [JetSetColumns](gg294050\(v=exchg.10\).md) one or more times to set the record state. Finally, **JetUpdate2** is called to complete the update operation. Indexes are updated only by [JetUpdate](gg269288\(v=exchg.10\).md) or **JetUpdate2**, and not during [JetSetColumn](gg294137\(v=exchg.10\).md) or [JetSetColumns](gg294050\(v=exchg.10\).md).

```cpp
    JET_ERR JET_API JetUpdate2(
      __in          JET_SESID sesid,
      __in          JET_TABLEID tableid,
      __out_opt     void* pvBookmark,
      __in          unsigned long cbBookmark,
      __out_opt     unsigned long* pcbActual,
      __in            const JET_GRBIT grbit
    );
```

### Parameters

*sesid*

The session to use for this call.

*tableid*

The cursor to use for this call.

*pvBookmark*

Pointer to a returned bookmark for an inserted row.

*cbBookmark*

Size of the buffer pointed to by *pvBookmark*.

*pcbActual*

The returned size of the bookmark for the inserted row returned in *pvBookmark*.

*grbit*

A group of bits that contain the options to be used for this call, which include zero or more of the following.

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
<td><p>JET_bitUpdateCheckESE97Compatibility</p></td>
<td><p>This flag causes the update to return an error if the update would not have been possible in the Windows 2000 version of ESE, which enforced a smaller maximum number of multi-valued column instances in each record than later versions of ESE. This is important only for applications that wish to replicate data between applications hosted on Windows 2000 and applications hosted on Windows Server 2003, or later versions of ESE. It should not be necessary for most applications.</p></td>
</tr>
</tbody>
</table>


### Return Value

This function returns the [JET_ERR](gg294092\(v=exchg.10\).md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](gg269184\(v=exchg.10\).md) and [Error Handling Parameters](gg269173\(v=exchg.10\).md).

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
<td><p>JET_errBufferTooSmall</p></td>
<td><p>The given buffer for the record bookmark is not sufficiently large enough to store the record bookmark.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errClientRequestToStopJetService</p></td>
<td><p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p></td>
</tr>
<tr class="even">
<td><p>JET_errDiskFull</p></td>
<td><p>The update operation requires database file growth, or log file allocation, but the disk drive where the database file or log series resides is full. Alternatively, the database file is on a FAT32 formatted volume and the database file is already 4GBytes, the per file limit for FAT32.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errInstanceUnavailable</p></td>
<td><p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data.</p>
<p><strong>Windows XP:</strong>  This error will only be returned by Windows XP and later releases.</p></td>
</tr>
<tr class="even">
<td><p>JET_errInvalidParameter</p></td>
<td><p>The given <em>prep</em> parameter in the <a href="gg269339(v=exchg.10).md">JetPrepareUpdate</a> function is not a valid flag.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errKeyDuplicate</p></td>
<td><p>An index key for this record is a duplicate of another index key for another record already in the table and the index does not allow duplicates.</p></td>
</tr>
<tr class="even">
<td><p>JET_errKeyTruncated</p></td>
<td><p>The inserted or updated record has one or more indices for which the generated key would have exceeded the maximum allowable size. As a result, the operation has failed to prevent key truncation.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errMultiValuedIndexViolation</p></td>
<td><p>The inserted or updated record has an indexed multi-value column with two or more values that are identical within the maximum length key size set for the index. As a result, the record has two identical entries in the index which is invalid.</p></td>
</tr>
<tr class="even">
<td><p>JET_errNotInitialized</p></td>
<td><p>It is not possible to complete the operation because the instance associated with the session has not been initialized yet.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errNullInvalid</p></td>
<td><p>One or more columns in the record to be inserted or in the updated state of a record being replace is <strong>NULL</strong> which violates the defined constraint for those columns.</p></td>
</tr>
<tr class="even">
<td><p>JET_errNullKeyDisallowed</p></td>
<td><p>One or more indexes are defined not to allow a <strong>NULL</strong> key and the inserted or updated state of a record being replaced violates this defined constraint.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errRecordPrimaryChanged</p></td>
<td><p>A record replacement operation has updated the primary key. Updates to primary key columns must be done through deleting the existing record and inserting a new record with the desired data.</p></td>
</tr>
<tr class="even">
<td><p>JET_errRestoreInProgress</p></td>
<td><p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errSessionSharingViolation</p></td>
<td><p>The same session cannot be used for more than one thread at the same time.</p>
<p><strong>Windows XP:</strong>  This error will only be returned by Windows XP and later releases.</p></td>
</tr>
<tr class="even">
<td><p>JET_errTermInProgress</p></td>
<td><p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errUpdateNotPrepared</p></td>
<td><p><a href="gg269339(v=exchg.10).md">JetPrepareUpdate</a> was called with JET_prepCancel but the cursor was not in the prepared state.</p></td>
</tr>
<tr class="even">
<td><p>JET_errWriteConflict</p></td>
<td><p>A record replacement operation for which a write lock was not already allocated can encounter a write conflict at the time of update.</p></td>
</tr>
</tbody>
</table>


On success, the open update operation on the cursor is completed. If an auto-increment column is defined for the table, then this value is set for inserted records. If a version column is defined for the table, then its value is initialized for newly inserted records, or incremented each time a record is replaced. All indexes, including clustered and non-clustered indexes are updated.

On failure, no changes of any kind are made to the database. Before insert and before replace callback functions may have been called, but after insert and after replace callbacks will not have been called, since the latter cannot cause an update to fail. The cursor copy buffer is left in its prepared state, so that the opportunity exists to incrementally correct the problems that caused errors and retry the update operation.

#### Remarks

Record size limitations are enforced by [JetSetColumn](gg294137\(v=exchg.10\).md), and not in general by [JetUpdate](gg269288\(v=exchg.10\).md). The only exception is when the JET_bitUpdateCheckESE97Compatibility compatibility flag is being used. In this case, the whole record is checked since an individual [JetSetColumn](gg294137\(v=exchg.10\).md) operation that exceeded the limit may be compensated by a subsequent call to [JetSetColumn](gg294137\(v=exchg.10\).md).

See the Remarks section in [JetUpdate](gg269288\(v=exchg.10\).md) for more information.

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

[JET_ERR](gg294092\(v=exchg.10\).md)  
[JET_SESID](gg269253\(v=exchg.10\).md)  
[JET_TABLEID](gg269182\(v=exchg.10\).md)  
[JetDelete](gg269315\(v=exchg.10\).md)  
[JetPrepareUpdate](gg269339\(v=exchg.10\).md)  
[JetRegisterCallback](gg269175\(v=exchg.10\).md)  
[JetRetrieveColumn](gg269198\(v=exchg.10\).md)  
[JetRetrieveColumns](gg294135\(v=exchg.10\).md)  
[JetSetColumn](gg294137\(v=exchg.10\).md)  
[JetSetColumns](gg294050\(v=exchg.10\).md)

