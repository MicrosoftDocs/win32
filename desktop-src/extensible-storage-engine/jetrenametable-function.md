---
description: "Learn more about: JetRenameTable Function"
title: JetRenameTable Function
TOCTitle: JetRenameTable Function
ms:assetid: face9341-58e3-450b-980d-08eb1dc3e9d2
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294142(v=EXCHG.10)
ms:contentKeyID: 32765756
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetRenameTableW
- JetRenameTableA
- JetRenameTable
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

# JetRenameTable Function


_**Applies to:** Windows | Windows Server_

## JetRenameTable Function

The **JetRenameTable** function can be used to change the name of an existing table.

```cpp
    JET_ERR JET_API JetRenameTable(
      __in          JET_SESID sesid,
      __in          JET_DBID dbid,
      __in          const tchar* szName,
      __in          const tchar* szNameNew
    );
```

### Parameters

*sesid*

The session to use for this call.

*dbid*

The database to use for this call.

*szName*

The current name of the table that will be renamed.

*szNameNew*

The new name for the table that will be renamed.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data. This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errInvalidDatabase</p> | <p>The specified database was invalid.</p><p>This error is only returned in Windows 2000 when a table rename operation is attempted on the temporary database. JET_errInvalidDatabaseId is returned for this case in later releases.</p> | 
| <p>JET_errInvalidDatabaseId</p> | <p>The specified database ID was invalid.</p> | 
| <p>JET_errInvalidName</p> | <p>One of the specified object names was invalid. All object names must conform to the same set of rules. These rules are as follows:</p><ul><li><p>Object names must be composed of ASCII characters.</p></li><li><p>Object names must be at least one character in length.</p></li><li><p>Object names may not exceed JET_cbNameMost (64) characters in length.</p></li><li><p>Object names may not begin with a space.</p></li><li><p>Object names may not contain ASCII control characters (0x00 through 0x1F).</p></li><li><p>Object names may not contain an exclamation point (!), period (.), left bracket ([), or right bracket (]) character - once validated, only the portion of the string up to the first space (if any) will be used for the object name. This effectively means that object names may not contain a space either.</p></li></ul> | 
| <p>JET_errInvalidParameter</p> | <p>One of the parameters provided contained an unexpected value or contained a value that did not make sense when combined with the value of another parameter. This can happen for <strong>JetRenameTable</strong> when:</p><ul><li><p><em>szName</em> is NULL.</p></li><li><p><em>szNameNew</em> is NULL.</p></li></ul> | 
| <p>JET_errNotInitialized</p> | <p>It is not possible to complete the operation because the instance associated with the session has not been initialized yet.</p> | 
| <p>JET_errObjectNotFound</p> | <p>This specified table does not exist for this database.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p> | 
| <p>JET_errSessionSharingViolation</p> | <p>The same session cannot be used for more than one thread at the same time. This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errTermInProgress</p> | <p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p> | 
| <p>JET_errTransReadOnly</p> | <p>An update cannot be done while inside the scope of a read-only transaction. A read-only transaction is a transaction that has been started using a call to <a href="gg269268(v=exchg.10).md">JetBeginTransaction2</a> with JET_bitTransactionReadOnly.</p><p>This error will only be returned by Windows XP and later releases.</p> | 



On success, the name of the specified table in the given database is permanently changed to the new name.

On failure, no change to the database state will occur.

#### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JetRenameTableW</strong> (Unicode) and <strong>JetRenameTableA</strong> (ANSI).</p> | 



#### See Also

[JET_DBID](./jet-dbid.md)  
[JET_ERR](./jet-err.md)  
[JET_SESID](./jet-sesid.md)  
[JetBeginTransaction2](./jetbegintransaction2-function.md)
