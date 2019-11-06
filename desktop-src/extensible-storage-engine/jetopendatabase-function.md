---
title: JetOpenDatabase Function
TOCTitle: JetOpenDatabase Function
ms:assetid: 7764f0c2-6795-4b93-be3d-f6830cdce369
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/Gg269299(v=EXCHG.10)
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

The **JetOpenDatabase** function opens a previously attached database, using the [JetAttachDatabase](gg294074\(v=exchg.10\).md) or [JetAttachDatabase2](gg269322\(v=exchg.10\).md) functions, for use with a database session. This function can be called multiple times for the same database.

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

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Value</p></th>
<th><p>Meaning</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>JET_bitDbExclusive</p></td>
<td><p>Allows only a single session to attach a database. Normally, several sessions can open a database.</p></td>
</tr>
<tr class="even">
<td><p>JET_bitDbReadOnly</p></td>
<td><p>Prevents modifications to the database.</p></td>
</tr>
</tbody>
</table>


### Return Value

This function returns the [JET_ERR](gg294092\(v=exchg.10\).md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](gg269184\(v=exchg.10\).md) and [Error Handling Parameters](gg269173\(v=exchg.10\).md).

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Return code</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>JET_errSuccess</p></td>
<td><p>The operation completed successfully.</p></td>
</tr>
<tr class="even">
<td><p>JET_errDatabaseInUse</p></td>
<td><p>Exclusive access was requested, but could not be granted.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errDatabaseInvalidPath</p></td>
<td><p>An invalid path was given in <em>szFilename</em>. <em>szFilename</em> must be non-NULL and refer to a valid file.</p></td>
</tr>
<tr class="even">
<td><p>JET_errDatabaseLocked</p></td>
<td><p>Another session has already opened the database exclusively (using JET_bitDbExclusive).</p></td>
</tr>
<tr class="odd">
<td><p>JET_errDatabaseNotFound</p></td>
<td><p>The database was not previously attached (See <a href="gg294074(v=exchg.10).md">JetAttachDatabase</a>).</p></td>
</tr>
<tr class="even">
<td><p>JET_errInvalidDatabase</p></td>
<td><p>An attempt was made to open a file that is not a valid database file.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errOneDatabasePerSession</p></td>
<td><p>An attempt was made to open more than one database, and <a href="gg269337(v=exchg.10).md">JET_paramOneDatabasePerSession</a> was set. For more information, see <a href="gg294139(v=exchg.10).md">System Parameters</a>.</p></td>
</tr>
<tr class="even">
<td><p>JET_wrnFileOpenReadOnly</p></td>
<td><p>The file was attached as read-only, but <strong>JetOpenDatabase</strong> did not pass JET_bitDbReadOnly. The database is still opened with read-only access.</p></td>
</tr>
</tbody>
</table>


#### Requirements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Client</strong></p></td>
<td><p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p></td>
</tr>
<tr class="even">
<td><p><strong>Server</strong></p></td>
<td><p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Header</strong></p></td>
<td><p>Declared in Esent.h.</p></td>
</tr>
<tr class="even">
<td><p><strong>Library</strong></p></td>
<td><p>Use ESENT.lib.</p></td>
</tr>
<tr class="odd">
<td><p><strong>DLL</strong></p></td>
<td><p>Requires ESENT.dll.</p></td>
</tr>
<tr class="even">
<td><p><strong>Unicode</strong></p></td>
<td><p>Implemented as <strong>JetOpenDatabaseW</strong> (Unicode) and <strong>JetOpenDatabaseA</strong> (ANSI).</p></td>
</tr>
</tbody>
</table>


#### See Also

[JET_ERR](gg294092\(v=exchg.10\).md)  
[JET_GRBIT](gg294066\(v=exchg.10\).md)  
[JET_SESID](gg269253\(v=exchg.10\).md)  
[JET_TABLEID](gg269182\(v=exchg.10\).md)  
[JetAttachDatabase](gg294074\(v=exchg.10\).md)  
[JetAttachDatabase2](gg269322\(v=exchg.10\).md)  
[JetSetSystemParameter](gg294044\(v=exchg.10\).md)  
[System Parameters](gg294139\(v=exchg.10\).md)

