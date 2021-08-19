---
description: "Learn more about: JetOpenDatabase Function"
title: JetOpenDatabase Function
TOCTitle: JetOpenDatabase Function
ms:assetid: 7764f0c2-6795-4b93-be3d-f6830cdce369
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269299(v=EXCHG.10)
ms:contentKeyID: 32765591
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetOpenDatabase
- JetOpenDatabaseW
- JetOpenDatabaseA
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

# JetOpenDatabase Function


_**Applies to:** Windows | Windows Server_

## JetOpenDatabase Function

The **JetOpenDatabase** function opens a previously attached database, using the [JetAttachDatabase](./jetattachdatabase-function.md) or [JetAttachDatabase2](./jetattachdatabase2-function.md) functions, for use with a database session. This function can be called multiple times for the same database.

```cpp
    JET_ERR JET_API JetOpenDatabase(
      __in          JET_SESID sesid,
      __in          const tchar* szFilename,
      __in_opt      const tchar* szConnect,
      __out         JET_DBID* pdbid,
      __in          JET_GRBIT grbit
    );
```

### Parameters

*sesid*

The database session context to use for the API call.

*szFilename*

The name of the database to open.

*szConnect*

Reserved. Set to NULL.

*pdbid*

Pointer to a buffer that, on a successful call, contains the identifier of the database. If the call fails, the value is undefined.

*grbit*

A group of bits that specify zero or more of the following options.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitDbExclusive</p> | <p>Allows only a single session to attach a database. Normally, several sessions can open a database.</p> | 
| <p>JET_bitDbReadOnly</p> | <p>Prevents modifications to the database.</p> | 



### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errDatabaseInUse</p> | <p>Exclusive access was requested, but could not be granted.</p> | 
| <p>JET_errDatabaseInvalidPath</p> | <p>An invalid path was given in <em>szFilename</em>. <em>szFilename</em> must be non-NULL and refer to a valid file.</p> | 
| <p>JET_errDatabaseLocked</p> | <p>Another session has already opened the database exclusively (using JET_bitDbExclusive).</p> | 
| <p>JET_errDatabaseNotFound</p> | <p>The database was not previously attached (See <a href="gg294074(v=exchg.10).md">JetAttachDatabase</a>).</p> | 
| <p>JET_errInvalidDatabase</p> | <p>An attempt was made to open a file that is not a valid database file.</p> | 
| <p>JET_errOneDatabasePerSession</p> | <p>An attempt was made to open more than one database, and <a href="gg269337(v=exchg.10).md">JET_paramOneDatabasePerSession</a> was set. For more information, see <a href="gg294139(v=exchg.10).md">System Parameters</a>.</p> | 
| <p>JET_wrnFileOpenReadOnly</p> | <p>The file was attached as read-only, but <strong>JetOpenDatabase</strong> did not pass JET_bitDbReadOnly. The database is still opened with read-only access.</p> | 



#### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JetOpenDatabaseW</strong> (Unicode) and <strong>JetOpenDatabaseA</strong> (ANSI).</p> | 



#### See Also

[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JetAttachDatabase](./jetattachdatabase-function.md)  
[JetAttachDatabase2](./jetattachdatabase2-function.md)  
[JetSetSystemParameter](./jetsetsystemparameter-function.md)  
[System Parameters](./extensible-storage-engine-system-parameters.md)
