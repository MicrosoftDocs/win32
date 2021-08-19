---
description: "Learn more about: JetIndexRecordCount Function"
title: JetIndexRecordCount Function
TOCTitle: JetIndexRecordCount Function
ms:assetid: 62d39738-cd91-4cfb-9483-f4a2dd845d9a
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269267(v=EXCHG.10)
ms:contentKeyID: 32765569
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetIndexRecordCount
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

# JetIndexRecordCount Function


_**Applies to:** Windows | Windows Server_

## JetIndexRecordCount Function

The **JetIndexRecordCount** function counts the number of entries in the current index from the current position forward. The current position is included in the count. The count can be greater than the total number of records in the table if the current index is over a multi-valued column and instances of the column have multiple-values. If the table is empty, then 0 will be returned for the count.

```cpp
    JET_ERR JET_API JetIndexRecordCount(
      __in          JET_SESID sesid,
      __in          JET_TABLEID tableid,
      __out         unsigned long* pcrec,
      __in          unsigned long crecMax
    );
```

### Parameters

*sesid*

The session to use for this call.

*tableid*

The cursor to use for this call.

*pcrec*

The pointer to an unsigned long value to receive the count.

*crecMax*

The maximum number of records to count. A *crecMax* value of 0 indicates that the count is unlimited.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>The operation cannot complete because all activity on the instance that is associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>The operation cannot complete because the instance that is associated with the session encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data.</p><p><strong>Windows XP:</strong>  This return value is introduced in Windows XP.</p> | 
| <p>JET_errNoCurrentRecord</p> | <p>The cursor is not currently on a record and the table is not empty.</p><p><strong>Windows XP, Windows Server 2003, Windows 2000 Server, and Windows 2000 Professional:</strong>  If the cursor is positioned on an empty index or index range then <strong>JetIndexRecordCount</strong> erroneously returns JET_errNoCurrentRecord.</p> | 
| <p>JET_errNotInitialized</p> | <p>The operation cannot complete because the instance that is associated with the session has not yet been initialized.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>The operation cannot complete because a restore operation is in progress on the instance that is associated with the session.</p> | 
| <p>JET_errSessionSharingViolation</p> | <p>The same session cannot be used for more than one thread at the same time.</p><p><strong>Windows XP:</strong>  This return value is introduced in Windows XP.</p> | 
| <p>JET_errTermInProgress</p> | <p>The operation cannot complete because the instance that is associated with the session is being shut down.</p> | 



If this function succeeds, the exact number of index entries including the current position and up to *crecMax* (if it is not 0), is returned in the unsigned long pointed to by *pcrec*.

If this function fails, no changes are made to memory allocated at *precpos*.

#### Remarks

If the table is not empty, then the cursor should be positioned onto the record from which to begin the count. The count will include this record, and count forward up to the given limit in *crecMax*. If *crecMax* is 0 then the operation will continue counting until the end of the index.

Index ranges can be used to construct artificial end-of-index limitations for the count. In this way, subranges of an index can be counted exactly. The cursor should be positioned to the first row in the range. The end of the range key should be made and then [JetSetIndexRange](./jetsetindexrange-function.md) should be used to set the upper range, either inclusively or exclusively. Lastly, **JetIndexRecordCount** should be called to exactly count the range.

**JetIndexRecordCount** obeys transaction semantics and returns a count that is accurate for this particular session in its current transactional state.

**JetIndexRecordCount** accesses index leaf pages in order to exactly count entries. Consequently, it can perform a great deal of I/O and can be slow. The *crecMax* limitation should be used to prevent excessive load. If a range is large, then it might be possible to count the range in an approximated fashion using [JetGetRecordPosition](./jetgetrecordposition-function.md).

**Windows XP, Windows Server 2003, Windows 2000 Server, and Windows 2000 Professional:**  If the cursor is positioned on an empty index or index range then **JetIndexRecordCount** erroneously returns JET_errNoCurrentRecord rather than returning a record count of zero. The application should check to see if the index or index range is empty in this case.

#### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See Also

[JET_ERR](./jet-err.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JetGetRecordPosition](./jetgetrecordposition-function.md)  
[JetSetIndexRange](./jetsetindexrange-function.md)  
[JetStopService](./jetstopservice-function.md)
