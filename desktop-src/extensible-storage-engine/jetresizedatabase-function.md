---
description: "Learn more about: JetResizeDatabase Function"
title: JetResizeDatabase Function
TOCTitle: JetResizeDatabase Function
ms:assetid: b6420de7-acff-480e-838b-f0e5acc29c65
ms:mtpsurl: https://msdn.microsoft.com/library/JJ835047(v=EXCHG.10)
ms:contentKeyID: 49894669
ms.date: 04/11/2016
ms.topic: reference
dev_langs:
- c++
api_name: 
- JetResizeDatabase
topic_type: 
- apiref
- kbArticle
api_type: 
- DLLExport
api_location: 
- ESENT.DLL
ROBOTS: INDEX,FOLLOW

---

# JetResizeDatabase Function


_**Applies to:** Windows | Windows Server_

The **JetResizeDatabase** function extends or shrinks the size of a database that is currently open.

The **JetResizeDatabase** function was introduced in the Windows 8 operating system.

``` c++
JET_ERR JET_API JetResizeDatabase(
  __in          JET_SESID sesid,
  __in          JET_DBID dbid,
  __in          unsigned long cpg,
  __out         unsigned long* pcpgActual,
  __in          const JET_GRBIT grbit
);
```

### Parameters

*sesid*

The database session context to use for the API call.

*dbid*

The database that will be extended.

*cpg*

The requested size of the database, in pages.

*pcpgActual*

A pointer to a number that receives the size of the database, in pages, after the API call. If the API call fails, the contents of *pcpgActual* parameter are undefined.

*grbit*

A group of bits that specifies zero or more of the values listed in the following table.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitResizeDatabaseOnlyGrow</p> | <p>Only grow the database. If the resize call would shrink the database, do nothing.</p> | 



### Return value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the return codes listed in the following table. For more information about the possible Extensible Storage Engine (ESE) errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errDiskFull</p> | <p>There is insufficient free space on the volume to perform the grow operation.</p> | 
| <p>JET_errDiskIO</p> | <p>A file-related error was returned by the <a href="gg269242(v=exchg.10).md">JetSetDatabaseSize</a> function. For more information about other file-related errors that might be returned, see <a href="gg269242(v=exchg.10).md">JetSetDatabaseSize</a>.</p> | 



#### Remarks

If the **JetResizeDatabase** function is called prior to inserting large amounts of data, the database file will be grown in one operation. This will reduce the likelihood of the database file becoming fragmented at the file system level, and also reduce the number of times the database file has to be grown. Growing the database file once can be faster than growing it several times.

To set the size of a database that is not opened, see [JetSetDatabaseSize](./jetsetdatabasesize-function.md).

The file size might not match the number of pages that are returned in the *pcpgReal* parameter. Two additional reserved pages might not be counted in the *pcpgReal* parameter.

#### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows 8.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2012.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See also

[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JET_OBJECTINFO](./jet-objectinfo-structure.md)  
[JET_OBJECTLIST](./jet-objectlist-structure.md)  
[JetSetDatabaseSize](./jetsetdatabasesize-function.md)
