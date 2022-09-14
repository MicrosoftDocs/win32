---
description: "Learn more about: JetOpenTable Function"
title: JetOpenTable Function
TOCTitle: JetOpenTable Function
ms:assetid: ded6348c-a82a-49bc-8a5d-e40ed5d6315c
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294118(v=EXCHG.10)
ms:contentKeyID: 32765732
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetOpenTable
- JetOpenTableW
- JetOpenTableA
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

# JetOpenTable Function


_**Applies to:** Windows | Windows Server_

## JetOpenTable Function

The **JetOpenTable** function opens a cursor on a previously created table.

```cpp
    JET_ERR JET_API JetOpenTable(
      __in          JET_SESID sesid,
      __in          JET_DBID dbid,
      __in          const tchar* szTableName,
      __in_opt      const void* pvParameters,
      __in          unsigned long cbParameters,
      __in          JET_GRBIT grbit,
      __out         JET_TABLEID* ptableid
    );
```

### Parameters

*sesid*

The database session context to use.

*dbid*

The database identifier to use to find the table.

*szTableName*

The name of the table to open.

*pvParameters*

Deprecated. Set to **NULL**.

*cbParameters*

Deprecated. Set to 0 (zero).

*grbit*

A group of bits specifying zero or more of the following options.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitTableDenyRead</p> | <p>The table cannot be opened for read-access by another database session.</p> | 
| <p>JET_bitTableDenyWrite</p> | <p>The table cannot be opened for write-access by another database session.</p> | 
| <p>JET_bitTableNoCache</p> | <p>Do not cache the pages for this table.</p> | 
| <p>JET_bitTablePermitDDL</p> | <p>Allows DDL modification on tables flagged as FixedDDL. This option must be used with the JET_bitTableDenyRead option.</p> | 
| <p>JET_bitTablePreread</p> | <p>Provides a hint that the table is probably not in the buffer cache, and that pre-reading may be beneficial to performance.</p> | 
| <p>JET_bitTableReadOnly</p> | <p>Requests read-only access to the table.</p> | 
| <p>JET_bitTableSequential</p> | <p>The table should be very aggressively prefetched from disk because the application will be scanning it sequentially.</p> | 
| <p>JET_bitTableUpdatable</p> | <p>Requests write-access to the table.</p> | 



*ptableid*

On success, points to the identifier of the table. On failure, the contents for *ptableid* are undefined.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errInvalidDatabaseId</p> | <p><em>dbid</em> is not a valid database identifier.</p> | 
| <p>JET_errInvalidgrbit</p> | <p>A bad combination of <em>grbit</em> was passed in.</p> | 
| <p>JET_errInvalidName</p> | <p>The name given in <em>szTableName</em> is invalid.</p><p>For more information about valid table names, see the <em>szTableName</em> parameter in <a href="gg269210(v=exchg.10).md">JetCreateTable</a>.</p> | 
| <p>JET_errObjectNotFound</p> | <p>An attempt was made to open a table that does not exist in the database.</p> | 
| <p>JET_errOutOfCursors</p> | <p>The operation failed because the engine cannot allocate the resources required to open a new cursor. See the Remarks section.</p> | 
| <p>JET_errTableInUse</p> | <p>The table is being used by another database operation.</p> | 
| <p>JET_wrnTableInUseBySystem</p> | <p>A nonfatal warning indicating that the table is being used by the system.</p> | 
| <p>JET_errTableLocked</p> | <p>The table is locked by another database operation.</p> | 
| <p>JET_errTooManyOpenTables</p> | <p>An attempt was made to open too many unique tables at once. See the Remarks section.</p> | 



#### Remarks

Tables opened with **JetOpenTable** should usually be closed with [JetCloseTable](./jetclosetable-function.md). The exception to this rule happens when **JetOpenTable** is called in a transaction and the transaction is rolled back (with [JetRollback](./jetrollback-function.md)). When rolling back a transaction, the table is automatically closed. In this case, it is an error to close the table with [JetCloseTable](./jetclosetable-function.md).

It is legal to open system tables with **JetOpenTable** (for example, MSysObjects, MSysUnicodeFixup). The schema of the system tables may change, so accessing system tables is discouraged. The number of unique tables that can be opened simultaneously is affected directly by *JET_paramMaxOpenTables*. If the table is currently open then a new cursor will be created on the table. Cursor resources are configured using [JetSetSystemParameter](./jetsetsystemparameter-function.md) with *JET_paramMaxCursors*. Also see [JetDupCursor](./jetdupcursor-function.md).

#### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JetOpenTableW</strong> (Unicode) and <strong>JetOpenTableA</strong> (ANSI).</p> | 



#### See Also

[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JetCloseTable](./jetclosetable-function.md)  
[JetDupCursor](./jetdupcursor-function.md)  
[JetRollback](./jetrollback-function.md)  
[JetSetSystemParameter](./jetsetsystemparameter-function.md)  
[Resource Parameters](./resource-parameters.md)
