---
description: "Learn more about: JetDelete Function"
title: JetDelete Function
TOCTitle: JetDelete Function
ms:assetid: 807de5ba-2f4b-4779-ab29-a1f094beecc1
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269315(v=EXCHG.10)
ms:contentKeyID: 32765605
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetDelete
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

# JetDelete Function


_**Applies to:** Windows | Windows Server_

## JetDelete Function

The **JetDelete** function deletes the current record in a database table.

```cpp
    JET_ERR JET_API JetDelete(
      __in          JET_SESID sesid,
      __in          JET_TABLEID tableid
    );
```

### Parameters

*sesid*

The database session context that will be used for the API call.

*tableid*

The cursor on a database table. The current row will be deleted.

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
<td><p>JET_errCallbackFailed</p></td>
<td><p>The callback function failed in some manner. For example, access violations in callback functions are caught and translated into JET_errCallbackFailed. This error will only be returned by Windows XP and later.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errClientRequestToStopJetService</p></td>
<td><p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p></td>
</tr>
<tr class="even">
<td><p>JET_errIllegalOperation</p></td>
<td><p>The cursor specified by <em>tableid</em> does not support deletion. See the Remarks section.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errInstanceUnavailable</p></td>
<td><p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data. This error will only be returned by Windows XP and later releases.</p></td>
</tr>
<tr class="even">
<td><p>JET_errNoCurrentRecord</p></td>
<td><p>The cursor specified by <em>tableid</em> is not on a record.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errNotInitialized</p></td>
<td><p>It is not possible to complete the operation because the instance associated with the session has not been initialized yet.</p></td>
</tr>
<tr class="even">
<td><p>JET_errRestoreInProgress</p></td>
<td><p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errPermissionDenied</p></td>
<td><p>The database engine does not have sufficient permissions to delete the record. This may happen if the database file was opened with read-only access.</p></td>
</tr>
<tr class="even">
<td><p>JET_errRollbackError</p></td>
<td><p>An update buffer (see <a href="gg269339(v=exchg.10).md">JetPrepareUpdate</a>) exists, but not all of the changes made to columns of type JET_coltypLongText and/or columns of type JET_coltypLongBinary could be rolled back.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errSessionSharingViolation</p></td>
<td><p>It is illegal to use the same session from more than one thread at the same time. This error will only be returned by Windows XP and later releases.</p></td>
</tr>
<tr class="even">
<td><p>JET_errTermInProgress</p></td>
<td><p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errTransReadOnly</p></td>
<td><p>The transaction is a read-only transaction, and does not support deletes.</p></td>
</tr>
<tr class="even">
<td><p>JET_errVersionStoreOutOfMemory</p></td>
<td><p>The operation failed because there is not enough memory to retain transactional information about the update.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errWriteConflict</p></td>
<td><p>Another session has previously locked the record for update. The update attempted by this session will fail.</p></td>
</tr>
</tbody>
</table>


On success, the currency is left just before the next record. If the deleted record was the last in the table, the currency is left at the end of the table (that is, after the new last record). If the deleted record was the only record in the table, the currency is set to the beginning.

The appropriate indexes are automatically updated.

If an update is prepared (using [JetPrepareUpdate](./jetprepareupdate-function.md)), it will be canceled. The update buffer will be reset.

On failure, the currency remains unchanged. If an update is prepared (see [JetPrepareUpdate](./jetprepareupdate-function.md)), the update buffer may be reset.

#### Remarks

Not all tables support deletion of rows. A temporary table does not normally support deletion of rows. Deletion of records may be enabled on temporary tables for many reasons, some of which are:

  - JET_bitTTUpdatable was specified during creation.

  - Large temporary tables can support deletion if they were created with JET_bitTTScrollable or JET_bitTTIndexed. The threshold at which a temporary table becomes "large" is currently 64 kilobytes, but it may be changed in future releases.

Windows XP and later. Callback functions can be invoked by **JetDelete**, including JET_cbtypBeforeDelete and JET_cbtypAfterDelete.

It is important to understand the impact of performing a large number of update operations inside of a single transaction. Each update to the database must be tracked by the database engine in the version store. The version store holds a live record of all the different versions of each record or index entry in the database that can be seen by all active transactions. These versions are used to support the multi-versioned concurrency control in use by the database engine to support transactions using snapshot isolation. Once the database engine has exhausted the resources used to store these versions then it can no longer accept further changes until some transactions have concluded to allow these resources to be reclaimed. When the engine is in this state, all updates will fail with JET_errVersionStoreOutOfMemory. The resources available to the database engine to store these versions can be controlled using [JetSetSystemParameter](./jetsetsystemparameter-function.md) with *JET_paramMaxVerPages* and *JET_paramGlobalMinVerPages*.

#### Requirements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Client</strong></p></td>
<td><p>Requires Windows Vista, Windows XP or Windows 2000 Professional.</p></td>
</tr>
<tr class="even">
<td><p><strong>Server</strong></p></td>
<td><p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p></td>
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
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JetOpenTempTable](./jetopentemptable-function.md)  
[JetPrepareUpdate](./jetprepareupdate-function.md)  
[System Parameters](./extensible-storage-engine-system-parameters.md)
