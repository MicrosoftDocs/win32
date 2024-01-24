---
description: "Learn more about: JetSetColumnDefaultValue Function"
title: JetSetColumnDefaultValue Function
TOCTitle: JetSetColumnDefaultValue Function
ms:assetid: 74bfaf50-6c2e-4907-b931-d50ad314b552
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269295(v=EXCHG.10)
ms:contentKeyID: 32765587
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetSetColumnDefaultValue
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

# JetSetColumnDefaultValue Function


_**Applies to:** Windows | Windows Server_

## JetSetColumnDefaultValue Function

The **JetSetColumnDefaultValue** function can be used to change the default value of an existing column.

```cpp
    JET_ERR JET_API JetSetColumnDefaultValue(
      __in          JET_SESID sesid,
      __in          JET_DBID dbid,
      __in          JET_PCSTR szTableName,
      __in          JET_PCSTR szColumnName,
      __in          const void* pvData,
      __in          const unsigned long cbData,
      __in          const JET_GRBIT grbit
    );
```

### Parameters

*sesid*

The session to use for this call.

*dbid*

The database to use for this call.

*szTableName*

The name of the table containing the column that will be affected.

*szColumnName*

The name of the column whose default value will be changed.

*pvData*

The input buffer containing the new default value.

*cbData*

The size of the input buffer containing the new default value.

*grbit*

Reserved for future use.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p> | 
| <p>JET_errColumnIllegalNull</p> | <p>Same as JET_errNullInvalid.</p> | 
| <p>JET_errColumnInUse</p> | <p>This specified column is currently in use by an index.</p><p><strong>JetSetColumnDefaultValue</strong> cannot change the default value of a column that is referenced in the definition of an index. This is because doing so could change the contents of the index.</p> | 
| <p>JET_errColumnNotFound</p> | <p>This specified column does not exist for this table.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data. This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errInvalidDatabaseId</p> | <p>The specified database ID was invalid.</p> | 
| <p>JET_errInvalidName</p> | <p>One of the specified object names was invalid. All object names must conform to the same set of rules. These rules are as follows:</p><ul><li><p>Object names must be composed of ASCII characters.</p></li><li><p>Object names must be at least one character in length.</p></li><li><p>Object names may not exceed JET_cbNameMost (64) characters in length.</p></li><li><p>Object names may not begin with a space.</p></li><li><p>Object names may not contain ASCII control characters (0x00 through 0x1F).</p></li><li><p>Object names may not contain an exclamation point (!), period (.), left bracket ([), or right bracket (]) character.</p></li><li><p>Once validated, only the portion of the string up to the first space (if any) will be used for the object name. This means that object names may not contain a space either.</p></li></ul> | 
| <p>JET_errNotInitialized</p> | <p>It is not possible to complete the operation because the instance associated with the session has not been initialized yet.</p> | 
| <p>JET_errNullInvalid</p> | <p>The column could not be set to NULL. This happens for <strong>JetSetColumnDefaultValue</strong> when:</p><ul><li><p><em>cbData</em> is zero.</p></li><li><p><strong>pvData</strong> is NULL.</p></li></ul><p>Therefore, it is not possible to set the default value of a column (back) to NULL or to a zero length value.</p> | 
| <p>JET_errObjectNotFound</p> | <p>This specified table does not exist for this database.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p> | 
| <p>JET_errSessionSharingViolation</p> | <p>The same session cannot be used for more than one thread at the same time. This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errTableInUse</p> | <p>This specified table is in use by another session.</p><p><strong>JetSetColumnDefaultValue</strong> requires exclusive access to a table in order to change the default value of the column for releases prior to Windows Server 2003.</p> | 
| <p>JET_errTermInProgress</p> | <p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p> | 
| <p>JET_errTransReadOnly</p> | <p>It is illegal to attempt an update when inside the scope of a read only transaction. A read only transaction is a transaction that has been started using a call to <a href="gg269268(v=exchg.10).md">JetBeginTransaction2</a> with JET_bitTransactionReadOnly. This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errWriteConflict</p> | <p>Another session has previously locked the record for update. The update attempted by this session will fail.</p> | 



On success, the default value of the specified column in the given table in the given database is permanently changed to the new default value.

On failure, no change to the database state will occur.

#### Remarks

It is not possible to change the default value of a column in a template table.

The database engine will silently truncate the default value of a column to 255 bytes for long text and long binary columns.

#### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JetSetColumnDefaultValueW</strong> (Unicode) and <strong>JetSetColumnDefaultValueA</strong> (ANSI).</p> | 



#### See Also

[JET_DBID](./jet-dbid.md)  
[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_SESID](./jet-sesid.md)  
[JetBeginTransaction2](./jetbegintransaction2-function.md)  
[JetStopService](./jetstopservice-function.md)
