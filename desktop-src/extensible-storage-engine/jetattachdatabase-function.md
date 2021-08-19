---
description: "Learn more about: JetAttachDatabase Function"
title: JetAttachDatabase Function
TOCTitle: JetAttachDatabase Function
ms:assetid: bc4c9a76-203c-424a-ac17-f096e3a6e04e
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294074(v=EXCHG.10)
ms:contentKeyID: 32765689
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetAttachDatabase
- JetAttachDatabaseW
- JetAttachDatabaseA
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

# JetAttachDatabase Function


_**Applies to:** Windows | Windows Server_

## JetAttachDatabase Function

The **JetAttachDatabase** function attaches a database file for use with a database instance. In order to use the database, it will need to be subsequently opened with [JetOpenDatabase](./jetopendatabase-function.md).

```cpp
    JET_ERR JET_API JetAttachDatabase(
      __in          JET_SESID sesid,
      __in          const tchar* szFilename,
      __in          JET_GRBIT grbit
    );
```

### Parameters

*sesid*

The database session context to use for the API call.

*szFilename*

The name of the database to attach.

*grbit*

A group of bits that specify zero or more of the following options.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitDbDeleteCorruptIndexes</p> | <p>If <a href="gg269337(v=exchg.10).md">JET_paramEnableIndexChecking</a> has been set, all indexes over Unicode data will be deleted. See the Remarks section for more details.</p> | 
| <p>JET_bitDbDeleteUnicodeIndexes</p> | <p>All indexes over Unicode data will be deleted, regardless of the setting of <a href="gg269337(v=exchg.10).md">JET_paramEnableIndexChecking</a>. See the Remarks section for more details.</p> | 
| <p>JET_bitDbUpgrade</p> | <p>Obsolete. Do not use.</p> | 
| <p>JET_bitDbReadOnly</p> | <p>Prevents modifications to the database.</p> | 



### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errBackupInProgress</p> | <p>Attaching a database is not allowed during a backup.</p> | 
| <p>JET_errDatabaseFileReadOnly</p> | <p>The database file specified by <em>szFilename</em> must be writable. The Read-Only attribute must not be set, and the running process must have sufficient privileges to write to the file.</p> | 
| <p>JET_errDatabaseInUse</p> | <p>The database file is already opened by another process.</p> | 
| <p>JET_errDatabaseInvalidPath</p> | <p>An invalid path was given in <em>szFilename</em>. <em>szFilename</em> must be non-NULL and refer to a valid path.</p> | 
| <p>JET_errDatabaseSharingViolation</p> | <p>The database file has already been attached by a different session.</p> | 
| <p>JET_errFileAccessDenied</p> | <p>The database engine cannot open the database file. The file may be in use by another process or the caller may not have sufficient privileges to open the file.</p> | 
| <p>JET_errFileNotFound</p> | <p>The file given in <em>szFilename</em> does not exist.</p> | 
| <p>JET_errPrimaryIndexCorrupted</p> | <p>There is an error with the primary index. This may be from physical corruption (such as disk or memory corruption). It may also be returned when attaching a database last modified on an older operating system and the primary index is over a column with Unicode data. See the remarks for more information on indexes over Unicode data.</p> | 
| <p>JET_errSecondaryIndexCorrupted</p> | <p>There is an error with a secondary index. This may be from physical corruption (such as disk or memory corruption). It may also be returned when attaching a database last modified on an older operating system and a secondary index is over a column with Unicode data. See the remarks for more information on indexes over Unicode data. Secondary indexes are completely rebuilt when a database is defragmented with an offline utility using the following command: <strong>esentutl -d</strong>.</p> | 
| <p>JET_errTooManyAttachedDatabases</p> | <p>Only a finite number of databases can be attached per instance. The limit is currently seven databases per instance.</p> | 
| <p>JET_wrnDatabaseAttached</p> | <p>A nonfatal warning indicating that the database file has already been attached by this session.</p> | 



#### Remarks

Calling **JetAttachDatabase** is equivalent to calling [JetAttachDatabase2](./jetattachdatabase2-function.md) and passing a value of zero, meaning there is no limit, for the *cpgDatabaseSizeMax* parameter.

Attaching a writable database (that is, if JET_bitDbReadOnly was not specified in the *grbit* parameter) will open the file exclusively at the operating system level. No other process will be able open the file. It is possible for multiple processes to attach a single database by opening them in read-only mode.

The database file is detached using [JetDetachDatabase](./jetdetachdatabase-function.md) or [JetDetachDatabase2](./jetdetachdatabase2-function.md).

Index-checking parameters

Different versions of Windows normalize Unicode text in different ways. That means indexes built under one version of Windows may not work on other versions.

Prior to Windows Server 2003, when the operating system version changed (including installation of a Service Pack), every index over Unicode data was in a potentially corrupt state.

Indexes created in Windows Server 2003 and later are flagged with the version of Unicode normalization with which they were built. Older indexes contain no version information. Most Unicode normalization changes consist of adding new characters, code points which were previously undefined are now defined and normalize differently. Thus, if binary data is stored in a Unicode column, it will normalize differently as new code points are defined.

As of Windows Server 2003, the ESE database engine tracks Unicode index entries that contain undefined code points. These can be used to fix an index when the set of defined Unicode characters changes.

These parameters control what happens when the ESE database engine attaches to a database that was last used under a different build of the operating system. The operating system version is stamped in the database header.

If [JET_paramEnableIndexChecking](./database-parameters.md) is set to **TRUE**, and the database contains potentially corrupt indexes:

  - **JetAttachDatabase** will delete the potentially corrupt indexes if *grbit* contains JET_bitDbDeleteCorruptIndexes

  - **JetAttachDatabase**will return an error if *grbit* does not contain JET_bitDbDeleteCorruptIndexes and there are indexes which need deletion.

If [JET_paramEnableIndexChecking](./database-parameters.md) is set to **FALSE**:

  - **JetAttachDatabase** will ignore potentially corrupt indexes, and return JET_errSuccess (assuming there were no other errors).

Windows Server 2003 and later: If [JET_paramEnableIndexChecking](./database-parameters.md) has not been reset, the internal fixup table will be used to fixup index entries. This may not fix all index corruptions but will be transparent to the application.

If the database was attached as read-only the index cannot be fixed or deleted. In this case, the API will instead return an error, such as JET_errSecondaryIndexCorrupted or JET_errPrimaryIndexCorrupted.

#### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JetAddColumnW</strong> (Unicode) and <strong>JetAddColumnA</strong> (ANSI).</p> | 



#### See Also

[Extensible Storage Engine Files](./extensible-storage-engine-files.md)  
[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JetAttachDatabase2](./jetattachdatabase2-function.md)  
[JetCreateDatabase](./jetcreatedatabase-function.md)  
[JetDetachDatabase](./jetdetachdatabase-function.md)  
[JetDetachDatabase2](./jetdetachdatabase2-function.md)  
[JetOpenDatabase](./jetopendatabase-function.md)  
[JetSetSystemParameter](./jetsetsystemparameter-function.md)
