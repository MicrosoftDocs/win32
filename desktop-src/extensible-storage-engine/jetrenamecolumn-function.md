---
description: "Learn more about: JetRenameColumn Function"
title: JetRenameColumn Function
TOCTitle: JetRenameColumn Function
ms:assetid: 30967765-355b-417c-b0d6-8b59e677cc98
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269218(v=EXCHG.10)
ms:contentKeyID: 32765521
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetRenameColumn
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

# JetRenameColumn Function


_**Applies to:** Windows | Windows Server_

## JetRenameColumn Function

The **JetRenameColumn** function can be used to change the name of an existing column on a table.

**Windows XP:**  **JetRenameColumn** is introduced in Windows XP.

```cpp
    JET_ERR JET_API JetRenameColumn(
      __in          JET_SESID sesid,
      __in          JET_TABLEID tableid,
      __in          JET_PCSTR szName,
      __in          JET_PCSTR szNameNew,
      __in          JET_GRBIT grbit
    );
```

### Parameters

*sesid*

The session to use for this call.

*tableid*

The cursor to use for this call.

*szName*

The current name of the column that will be renamed.

*szNameNew*

The new name for the column that will be renamed.

*grbit*

This parameter must be 0.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p> | 
| <p>JET_errColumnNotFound</p> | <p>This specified column does not exist for this table.</p> | 
| <p>JET_errInvalidName</p> | <p>One of the specified object names was invalid. All object names must conform to the same set of rules. These rules are as follows:</p><ul><li><p>Object names must be composed of ASCII characters.</p></li><li><p>Object names must be at least one character in length.</p></li><li><p>Object names may not exceed JET_cbNameMost (64) characters in length.</p></li><li><p>Object names may not begin with a space - object names may not contain ASCII control characters (0x00 through 0x1F).</p></li><li><p>Object names may not contain an exclamation point (!), period (.), left bracket ([), or right bracket (]) character.</p></li><li><p>Once validated, only the portion of the string up to the first space (if any) will be used for the object name. This effectively means that object names may not contain a space either.</p></li></ul> | 
| <p>JET_errInvalidParameter</p> | <p>One of the parameters provided contained an unexpected value or contained a value that did not make sense when combined with the value of another parameter. This can happen for <strong>JetRenameColumn</strong> when:</p><ul><li><p><em>szName</em> is NULL.</p></li><li><p><em>szNameNew</em> is NULL.</p></li></ul> | 
| <p>JET_errInstanceUnavailable</p> | <p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data. This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errInTransaction</p> | <p>This operation may only be performed when the session is not currently inside a transaction.</p> | 
| <p>JET_errNotInitialized</p> | <p>It is not possible to complete the operation because the instance associated with the session has not been initialized yet.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p> | 
| <p>JET_errSessionSharingViolation</p> | <p>The same session cannot be used for more than one thread at the same time. This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errTermInProgress</p> | <p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p> | 
| <p>JET_errTransReadOnly</p> | <p>An update cannot be done while inside the scope of a read-only transaction. A read-only transaction is a transaction that has been started using a call to <a href="gg269268(v=exchg.10).md">JetBeginTransaction2</a> with JET_bitTransactionReadOnly. This error will only be returned by Windows XP and later releases.</p> | 



On success, the name of the specified column in the table associated with the cursor is permanently changed to the new name. Any indexes that reference that column will also be updated.

On failure, no change to the database state will occur.

#### Remarks

The column rename operation is unusual because, unlike other schema operations, it is not carried out as a transaction. When a column in a given table is renamed in one session then any other session using that table will see the change immediately, even if they are in a transaction that would prevent that session from seeing any other change made by the session doing the rename operation.

The column ID of a column is not affected by the rename operation.

#### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista or Windows XP.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008 or Windows Server 2003.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JetRenameColumnW</strong> (Unicode) and <strong>JetRenameColumnA</strong> (ANSI).</p> | 



#### See Also

[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JetBeginTransaction2](./jetbegintransaction2-function.md)
