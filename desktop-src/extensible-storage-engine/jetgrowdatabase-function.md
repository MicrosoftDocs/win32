---
description: "Learn more about: JetGrowDatabase Function"
title: JetGrowDatabase Function
TOCTitle: JetGrowDatabase Function
ms:assetid: d9719991-6c80-4dcb-a1d6-f0c7de61f459
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294109(v=EXCHG.10)
ms:contentKeyID: 32765724
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetGrowDatabase
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

# JetGrowDatabase Function


_**Applies to:** Windows | Windows Server_

## JetGrowDatabase Function

The **JetGrowDatabase** function extends the size of a database that is currently open.

```cpp
    JET_ERR JET_API JetGrowDatabase(
      __in          JET_SESID sesid,
      __in          JET_DBID dbid,
      __in          unsigned long cpg,
      __in          unsigned long* pcpgReal
    );
```

### Parameters

*sesid*

The database session context to use for the API call.

*dbid*

The database that will be extended.

*cpg*

The desired size of the database, in pages.

*pcpgReal*

Pointer to a number that receives the size of the database, in pages, after the API call. If the API call fails, the contents of *pcpgReal* are undefined.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errDiskFull</p> | <p>There is insufficient free space on the volume to perform the grow operation.</p> | 
| <p>JET_errDiskIO</p> | <p>A file-related error was returned by <a href="gg269242(v=exchg.10).md">JetSetDatabaseSize</a>. For more information about other file-related errors that might be returned, see <a href="gg269242(v=exchg.10).md">JetSetDatabaseSize</a>.</p> | 



#### Remarks

If **JetGrowDatabase** is called prior to inserting large amounts of data, the database file will be grown in one operation. This will reduce the likelihood of the database file becoming fragmented at the file system level, and also reduce the number of times the database file has to be grown. Growing the database file once can be faster than growing it several times.

Only growing the file is currently supported. To shrink a file, use the defragmentation feature of the **esentutl.exe** utility program.

To set the size of a database that is not opened, see [JetSetDatabaseSize](./jetsetdatabasesize-function.md).

The file size might not match the number of pages that are returned in *pcpgReal*. There are two additional reserved pages that might not be counted in *pcpgReal*.

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
[JET_GRBIT](./jet-grbit.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JET_OBJECTINFO](./jet-objectinfo-structure.md)  
[JET_OBJECTLIST](./jet-objectlist-structure.md)  
[JetSetDatabaseSize](./jetsetdatabasesize-function.md)
