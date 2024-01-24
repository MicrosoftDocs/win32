---
description: "Learn more about: JetUpdate Function"
title: JetUpdate Function
TOCTitle: JetUpdate Function
ms:assetid: 6c9a53d0-46bc-403b-bdba-9020e023c14a
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269288(v=EXCHG.10)
ms:contentKeyID: 32765580
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetUpdate
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

# JetUpdate Function


_**Applies to:** Windows | Windows Server_

## JetUpdate Function

The **JetUpdate** function performs an update operation including inserting a new row into a table or updating an existing row. Deleting a table row is performed by calling [JetDelete](./jetdelete-function.md).

**JetUpdate** is the final step in performing an insert or an update. The update is begun by calling [JetPrepareUpdate](./jetprepareupdate-function.md) and then by calling [JetSetColumn](./jetsetcolumn-function.md) or [JetSetColumns](./jetsetcolumns-function.md) one or more times to set the record state. Finally, **JetUpdate** is called to complete the update operation. Indexes are updated only by **JetUpdate** or [JetUpdate2](./jetupdate2-function.md), and not during [JetSetColumn](./jetsetcolumn-function.md) or [JetSetColumns](./jetsetcolumns-function.md).

```cpp
    JET_ERR JET_API JetUpdate(
      __in          JET_SESID sesid,
      __in          JET_TABLEID tableid,
      __out_opt     void* pvBookmark,
      __in          unsigned long cbBookmark,
      __out_opt     unsigned long* pcbActual
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

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errBufferTooSmall</p> | <p>The given buffer for the record bookmark is not sufficiently large enough to store the record bookmark.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p> | 
| <p>JET_errColumnIllegalNull</p> | <p>Same as JET_errNullInvalid.</p> | 
| <p>JET_errDiskFull</p> | <p>The update operation requires database file growth, or log file allocation, but the disk drive where the database file or log series resides is full. Alternatively, the database file is on a FAT32 formatted volume and the database file is already 4GBytes, the per file limit for FAT32.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data.</p><p><strong>Windows XP:</strong>  This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errInvalidParameter</p> | <p>The given <em>prep</em> parameter in the <a href="gg269339(v=exchg.10).md">JetPrepareUpdate</a> function is not a valid flag.</p> | 
| <p>JET_errKeyDuplicate</p> | <p>An index key for this record is a duplicate of another index key for another record already in the table and the index does not allow duplicates.</p> | 
| <p>JET_errKeyTruncated</p> | <p>The inserted or updated record has one or more indices for which the generated key would have exceeded the maximum allowable size. As a result, the operation has failed to prevent key truncation.</p> | 
| <p>JET_errMultiValuedIndexViolation</p> | <p>The inserted or updated record has an indexed multi-value column with two or more values that are identical within the maximum length key size set for the index. As a result, the record has two identical entries in the index which is invalid.</p> | 
| <p>JET_errNotInitialized</p> | <p>It is not possible to complete the operation because the instance associated with the session has not been initialized yet.</p> | 
| <p>JET_errNullInvalid</p> | <p>One or more columns in the record to be inserted or in the updated state of a record being replace is <strong>NULL</strong> which violates the defined constraint for those columns.</p> | 
| <p>JET_errNullKeyDisallowed</p> | <p>One or more indexes are defined not to allow a <strong>NULL</strong> key and the inserted or updated state of a record being replaced violates this defined constraint.</p> | 
| <p>JET_errRecordPrimaryChanged</p> | <p>A record replacement operation has updated the primary key. Updates to primary key columns must be done through deleting the existing record and inserting a new record with the desired data.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p> | 
| <p>JET_errSessionSharingViolation</p> | <p>The same session cannot be used for more than one thread at the same time.</p><p><strong>Windows XP:</strong>  This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errTermInProgress</p> | <p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p> | 
| <p>JET_errTransReadOnly</p> | <p>It is illegal to attempt an update when inside the scope of a read only transaction. A read only transaction is a transaction that has been started using a call to <a href="gg269268(v=exchg.10).md">JetBeginTransaction2</a> with JET_bitTransactionReadOnly.</p><p><strong>Windows XP:</strong>  This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errUpdateNotPrepared</p> | <p><a href="gg269339(v=exchg.10).md">JetPrepareUpdate</a> was called with JET_prepCancel but the cursor was not in the prepared state.</p> | 
| <p>JET_errVersionStoreOutOfMemory</p> | <p>The operation failed because there is not enough memory to retain transactional information about the update.</p> | 
| <p>JET_errWriteConflict</p> | <p>Another session has previously locked the record for update. The update attempted by this session will fail.</p> | 



On success, the open update operation on the cursor is completed. If an auto-increment column is defined for the table, then this value is set for inserted records. If a version column is defined for the table, then its value is initialized for newly inserted records, or incremented each time a record is replaced. All indexes, including clustered and non-clustered indexes are updated.

On failure, no changes of any kind are made to the database. Before insert and before replace callback functions may have been called, but after insert and after replace callbacks will not have been called, since the latter cannot cause an update to fail. The cursor copy buffer is left in its prepared state, so that the opportunity exists to incrementally correct the problems that caused errors and retry the update operation.

#### Remarks

Callback functions can be registered to be called before or after insert, and before or after update.

Record size limitations are enforced by [JetSetColumn](./jetsetcolumn-function.md), and not in general by **JetUpdate**.

It is important to understand the impact of performing a large number of update operations inside of a single transaction. Each update to the database must be tracked by the database engine in the version store. The version store holds a live record of all the different versions of each record or index entry in the database that can be seen by all active transactions. These versions are used to support the multi-versioned concurrency control in use by the database engine to support transactions using snapshot isolation. Once the database engine has exhausted the resources used to store these versions then it can no longer accept further changes until some transactions have concluded to allow these resources to be reclaimed. When the engine is in this state, all updates will fail with JET_errVersionStoreOutOfMemory. The resources available to the database engine to store these versions can be controlled using [JetSetSystemParameter](./jetsetsystemparameter-function.md) with [JET_paramMaxVerPages](./resource-parameters.md) and [JET_paramGlobalMinVerPages](./resource-parameters.md).

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
[JetDelete](./jetdelete-function.md)  
[JetPrepareUpdate](./jetprepareupdate-function.md)  
[JetRegisterCallback](./jetregistercallback-function.md)  
[JetRetrieveColumn](./jetretrievecolumn-function.md)  
[JetRetrieveColumns](./jetretrievecolumns-function.md)  
[JetSetColumn](./jetsetcolumn-function.md)  
[JetSetColumns](./jetsetcolumns-function.md)  
[JetSetSystemParameter](./jetsetsystemparameter-function.md)  
[System Parameters](./extensible-storage-engine-system-parameters.md)
