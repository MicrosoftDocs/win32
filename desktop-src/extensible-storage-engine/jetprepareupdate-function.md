---
description: "Learn more about: JetPrepareUpdate Function"
title: JetPrepareUpdate Function
TOCTitle: JetPrepareUpdate Function
ms:assetid: 90cbaa83-47f2-4a65-b561-3bdecb7fd95a
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269339(v=EXCHG.10)
ms:contentKeyID: 32765628
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetPrepareUpdate
topic_type: 
- kbArticle
- apiref
api_type: 
- DLLExport
- COM
api_location: 
- ESENT.DLL
ROBOTS: INDEX,FOLLOW

---

# JetPrepareUpdate Function


_**Applies to:** Windows | Windows Server_

## JetPrepareUpdate Function

The **JetPrepareUpdate** function is the first operation in performing an update, for the purposes of inserting a new record or replacing an existing record with new values. Updates are done by calling **JetPrepareUpdate**, then calling [JetSetColumn](./jetsetcolumn-function.md) or [JetSetColumns](./jetsetcolumns-function.md) zero or more times and finally by calling [JetUpdate](./jetupdate-function.md) to complete the operation. **JetPrepareUpdate** and [JetUpdate](./jetupdate-function.md) set the boundaries for an update operation and are important in having only the final update state of a record entered into indexes. This is both more efficient, but also required in cases where data must match a valid state through more than on set column operation.

There are a few different options for inserting or replacing records and they are described in more detail below.

```cpp
    JET_ERR JET_API JetPrepareUpdate(
      __in          JET_SESID sesid,
      __in          JET_TABLEID tableid,
      __in          unsigned long prep
    );
```

### Parameters

*sesid*

The session to use for this call.

*tableid*

The cursor to use for this call.

*prep*

The options that can be used to prepare for an update, which include the following.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_prepCancel</p> | <p>This flag causes <strong>JetPrepareUpdate</strong> to cancel the update for this cursor.</p> | 
| <p>JET_prepInsert</p> | <p>This flag causes the cursor to prepare for an insert of a new record. All the data is initialized to the default state for the record. If the table has an auto-increment column, then a new value is assigned to this record regardless of whether the update ultimately succeeds, fails or is cancelled.</p> | 
| <p>JET_prepInsertCopy</p> | <p>This flag causes the cursor to prepare for an insert of a copy of the existing record. There must be a current record if this option is used. The initial state of the new record is copied from the current record. Long values that are stored off-record are virtually copied.</p> | 
| <p>JET_prepInsertCopyDeleteOriginal</p> | <p>This flag causes the cursor to prepare for an insert of the same record, and a delete or the original record. It is used in cases in which the primary key has changed.</p> | 
| <p>JET_prepReplace</p> | <p>This flag causes the cursor to prepare for a replace of the current record. If the table has a version column, then the version column is set to the next value in its sequence. If this update does not complete, then the version value in the record will be unaffected. An update lock is taken on the record to prevent other sessions from updating this record before this session completes.</p> | 
| <p>JET_prepReplaceNoLock</p> | <p>This flag is similar to JET_prepReplace, but no lock is taken to prevent other sessions from updating this record. Instead, this session may receive JET_errWriteConflict when it calls <a href="gg269288(v=exchg.10).md">JetUpdate</a> to complete the update.</p> | 



### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errAlreadyPrepared</p> | <p><strong>JetPrepareUpdate</strong> was called with a valid flag for prep but not JET_prepCancel and the cursor was already in the prepared state.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data. This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errInvalidParameter</p> | <p>The given prep flag is not a valid flag.</p> | 
| <p>JET_errNotInitialized</p> | <p>It is not possible to complete the operation because the instance associated with the session has not been initialized yet.</p> | 
| <p>JET_errNotInTransaction</p> | <p><strong>JetPrepareUpdate</strong> was called to replace a record which had SLV columns. SLV columns. Please note that SLV columns are a feature not intended for general usage. This feature is used to support the Microsoft Exchange infrastructure and is not intended to be used in your application.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p> | 
| <p>JET_errRollbackError</p> | <p><strong>JetPrepareUpdate</strong> was called with JET_prepCancel but could not rollback all of the changes made to columns of type JET_coltypLongText and/or columns of type JET_coltypLongBinary.</p> | 
| <p>JET_errSessionSharingViolation</p> | <p>This flag cannot be used with the same session from more than one thread at the same time. This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errTermInProgress</p> | <p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p> | 
| <p>JET_errUpdateNotPrepared</p> | <p><strong>JetPrepareUpdate</strong> was called with JET_prepCancel but the cursor was not in the prepared state.</p> | 



On success, the cursor is changed to the prepared state for the purpose of the desired update, or in the case of JET_prepCancel, the cursor is reverted to the non-prepared state and any changes are discarded.

On failure, the cursor state is left unchanged. If the failure was JET_errRollbackError then the cursor state is changed to the non-prepared state but not all of the changes have been reverted.

#### Remarks

Inserting a copy of a record is an important optimization when records share data of type JET_coltypLongText and/or JET_coltypLongBinary. This data is stored off-record when large and it is possible for multiple records to share the same physical representation of the data. In this case, the data can be updated from either record, but doing so will cause the data to be burst such that each record has its own copy. It is not possible to change data in one record by a modification from another record. Also, it is not possible to block an update of one record by an update of another record. This is a central feature to ESE and is known as Record Level Locking.

[JetUpdate](./jetupdate-function.md) operations which fail leave the cursor in the update prepared state. This is to permit correction to some errors, such as a wrong column value, without requiring the update state to be recreated. This means that in all cases where a cursor abandons an update, it must explicitly call **JetPrepareUpdate** with JET_prepCancel.

#### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See Also

[JET_ERR](./jet-err.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JetRetrieveColumn](./jetretrievecolumn-function.md)  
[JetSetColumn](./jetsetcolumn-function.md)  
[JetUpdate](./jetupdate-function.md)
