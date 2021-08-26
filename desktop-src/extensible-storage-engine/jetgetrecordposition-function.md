---
description: "Learn more about: JetGetRecordPosition Function"
title: JetGetRecordPosition Function
TOCTitle: JetGetRecordPosition Function
ms:assetid: 811d9e68-0594-4f70-b854-c3ec966b2705
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269316(v=EXCHG.10)
ms:contentKeyID: 32765606
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetGetRecordPosition
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

# JetGetRecordPosition Function


_**Applies to:** Windows | Windows Server_

## JetGetRecordPosition Function

The **JetGetRecordPosition** function returns the fractional position of the current record in the current index in the form of a [JET_RECPOS](./jet-recpos-structure.md) structure. This structure describes fractional positions in terms of an approximate number of index entries before the current record and an approximate total number of entries in the index.

```cpp
    JET_ERR JET_API JetGetRecordPosition(
      __in          JET_SESID sesid,
      __in          JET_TABLEID tableid,
      __out         JET_RECPOS* precpos,
      __in          unsigned long cbRecpos
    );
```

### Parameters

*sesid*

The session to use for this call.

*tableid*

The cursor to use for this call.

*precpos*

The description of the fraction to use in getting the position of the current record in the current index.

*cbRecpos*

The size of memory allocated at *precpos*.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errNotInitialized</p> | <p>It is not possible to complete the operation because the instance that is associated with the session has not been initialized yet.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>The operation cannot complete because all activity on the instance that is associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>This operation cannot complete because the instance, associated with the session, encountered a fatal error. It is required that access to all data be revoked in order to protect the integrity of that data.</p><p><strong>Windows 2000:</strong>  This error will not be returned by the Windows 2000 operating system.</p> | 
| <p>JET_errInvalidParameter</p> | <p>The size of the allocated memory at <em>precpos</em> is not a sufficient size.</p> | 
| <p>JET_errNoCurrentRecord</p> | <p>The cursor is not currently on a record and cannot return a position.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>It is not possible to complete the operation because a restore operation is in progress on the instance that is associated with the session.</p> | 
| <p>JET_errSessionSharingViolation</p> | <p>The same session cannot be used for more than one thread at the same time.</p><p><strong>Windows 2000:</strong>  This error will not be returned by the Windows 2000 operating system.</p> | 
| <p>JET_errTermInProgress</p> | <p>The operation cannot complete because the instance associated with the session is being shut down.</p> | 



On success, the approximate number of index entries preceding the current record in the index are returned in precpos-\>centriesLT. 1 is returned in precpos-\>centriesInRange. The approximate number of entries in the index is returned in precpos-\>centriesTotal.

On failure, no changes are made to memory allocated at *precpos*.

#### Remarks

This operation returns varying data when updates occur continuously on the table. The changes in the values will not always match expectations based on knowledge of the updates, since the values are approximations based on physical properties of the index. Transactional isolation does not apply to positions from **JetGetRecordPosition** since the values depend on physical properties of the index that are not transaction isolated.

[JET_RECPOS](./jet-recpos-structure.md) should not be used to describe a record within a table or to reposition a record close to an existing record. Instead, bookmarks for an existing record should be retrieved and then used to reposition the same record.

#### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See Also

[JET_COLUMNID](./jet-columnid.md)  
[JET_ERR](./jet-err.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JET_RECPOS](./jet-recpos-structure.md)  
[JET_SETINFO](./jet-setinfo-structure.md)  
[JetGotoPosition](./jetgotoposition-function.md)  
[JetStopService](./jetstopservice-function.md)
