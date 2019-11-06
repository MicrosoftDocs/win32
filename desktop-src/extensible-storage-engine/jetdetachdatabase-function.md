---
title: JetDetachDatabase Function
TOCTitle: JetDetachDatabase Function
ms:assetid: 629f19e5-99f3-425a-b6ba-de18daec7efe
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/Gg269266(v=EXCHG.10)
ms:contentKeyID: 32765568
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetDetachDatabaseW
- JetDetachDatabase
- JetDetachDatabaseA
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

# JetDetachDatabase Function


_**Applies to:** Windows | Windows Server_

## JetDetachDatabase Function

The **JetDetachDatabase** function releases a database file that was previously attached to a database session.

```cpp
    JET_ERR JET_API JetDetachDatabase(
      __in          JET_SESID sesid,
      __in          const tchar* szFilename
    );
```

### Parameters

*sesid*

The database session context to use for the API call.

*szFilename*

The name of the database to detach. If *szFilename* is **NULL** or an empty string, all databases attached to *sesid* will be detached.

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
<td><p>JET_errBackupInProgress</p></td>
<td><p>The database is being backed up, and cannot be detached.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errDatabaseInUse</p></td>
<td><p>The database has been opened by <a href="gg269299(v=exchg.10).md">JetOpenDatabase</a>. Databases must be closed prior to detaching.</p></td>
</tr>
<tr class="even">
<td><p>JET_errDatabaseNotFound</p></td>
<td><p>The database was not previously attached (See <a href="gg294074(v=exchg.10).md">JetAttachDatabase</a> or <a href="gg269322(v=exchg.10).md">JetAttachDatabase2</a>).</p></td>
</tr>
<tr class="odd">
<td><p>JET_errInTransaction</p></td>
<td><p>An attempt was made to detach a database while in a transaction.</p></td>
</tr>
</tbody>
</table>


#### Remarks

If an attached database was opened (with [JetAttachDatabase](gg294074\(v=exchg.10\).md)), it must be closed with [JetCloseDatabase](gg294123\(v=exchg.10\).md) prior to detaching.

Windows 2000 only: Databases which have not been detached prior to calling [JetTerm](gg269298\(v=exchg.10\).md) will automatically be re-attached when [JetInit](gg294068\(v=exchg.10\).md) is next called.

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
<td><p>Implemented as <strong>JetDetachDatabaseW</strong> (Unicode) and <strong>JetDetachDatabaseA</strong> (ANSI).</p></td>
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
[JetCreateDatabase](gg269212\(v=exchg.10\).md)  
[JetCreateDatabase2](gg269208\(v=exchg.10\).md)  
[JetCloseDatabase](gg294123\(v=exchg.10\).md)  
[JetTerm](gg269298\(v=exchg.10\).md)

