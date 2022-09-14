---
description: "Learn more about: JetSetDatabaseSize Function"
title: JetSetDatabaseSize Function
TOCTitle: JetSetDatabaseSize Function
ms:assetid: 4a87bf43-c8f7-4966-9f1f-68c16d1cb558
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269242(v=EXCHG.10)
ms:contentKeyID: 32765544
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetSetDatabaseSizeW
- JetSetDatabaseSize
- JetSetDatabaseSizeA
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

# JetSetDatabaseSize Function


_**Applies to:** Windows | Windows Server_

## JetSetDatabaseSize Function

The **JetSetDatabaseSize** function sets the size of an unopened database file.

```cpp
    JET_ERR JET_API JetSetDatabaseSize(
      __in          JET_SESID sesid,
      __in          JET_PCSTR szDatabaseName,
      __in          unsigned long cpg,
      __out         unsigned long* pcpgReal
    );
```

### Parameters

*sesid*

Identifies the database session context to use for the API call.

*szDatabaseName*

Identifies the name of the database file whose size is to be altered.

*cpg*

Specifies the desired size of the database, in pages.

*pcpgReal*

Pointer to a number that receives the size of the database, in pages, after the API call. If the API call was unsuccessful, the contents of *pcpgReal* are undefined.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errDatabaseInconsistent<br />JET_errDatabaseDirtyShutdown</p> | <p>JET_errDatabaseInconsistent and JET_errDatabaseDirtyShutdown are the same numeric value. The database whose size is to be adjusted must be in a clean shutdown, known as a consistent state. An inconsistent database is not corrupted, but it requires log files to be replayed.</p> | 
| <p>JET_errDatabaseInvalidPath</p> | <p><em>szDatabaseName</em> must not be an empty, non-NULL string.</p> | 
| <p>JET_errDiskFull</p> | <p>There is insufficient free space on the volume to perform the grow operation. <strong>JetSetDatabaseSize</strong> may also return many file-related errors, including, but not limited to:</p><ul><li><p>JET_errDiskIO</p></li><li><p>JET_errFileNotFound</p></li><li><p>JET_errInvalidPath</p></li><li><p>JET_errFileAccessDenied</p></li><li><p>JET_errOutOfFileHandles</p></li></ul> | 
| <p>JET_errInvalidParameter</p> | <p>One of the reasons this error may be returned is if <em>cpg</em> does meet the minimum database size. The current minimum database size is 256 pages.</p> | 
| <p>JET_errOutOfMemory</p> | <p>The system is low on memory resources.</p> | 



#### Remarks

If **JetSetDatabaseSize** is called prior to inserting large amounts of data, the database file will be grown in one operation. This will reduce the likelihood of the database file becoming fragmented at the file system level, and also reduce the number of times the database file has to be grown. Growing the database file once can be faster than growing it several times.

Only growing the file is currently supported. To shrink a file, use the defragmentation feature of the esentutl.exe utility program.

If *cpg* is smaller than the current size of the database, the operation will be ignored. If *cpg* is less than the minimum database size (currently 256 pages), it will return JET_errInvalidParameter.

To set the size of a database that is opened, see [JetGrowDatabase](./jetgrowdatabase-function.md).

The file size may not match the number of pages returned in *pcpgReal*. There are two additional reserved pages that may not be counted in *pcpgReal*.

#### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JetSetDatabaseSizeW</strong> (Unicode) and <strong>JetSetDatabaseSizeA</strong> (ANSI).</p> | 



#### See Also

[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JET_OBJECTINFO](./jet-objectinfo-structure.md)  
[JET_OBJECTLIST](./jet-objectlist-structure.md)  
[JetGrowDatabase](./jetgrowdatabase-function.md)
