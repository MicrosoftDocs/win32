---
description: "Learn more about: JetAttachDatabase2 Function"
title: JetAttachDatabase2 Function
TOCTitle: JetAttachDatabase2 Function
ms:assetid: 8667f3fc-d178-49f1-9474-f09352614f92
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269322(v=EXCHG.10)
ms:contentKeyID: 32765612
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetAttachDatabase2A
- JetAttachDatabase2
- JetAttachDatabase2W
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

# JetAttachDatabase2 Function


_**Applies to:** Windows | Windows Server_

## JetAttachDatabase2 Function

The **JetAttachDatabase2** function attaches a database file for use with a database instance and specifies a maximum size for that database. In order to use the database, it will need to be subsequently opened with [JetOpenDatabase](./jetopendatabase-function.md).

```cpp
    JET_ERR JET_API JetAttachDatabase2(
      __in          JET_SESID sesid,
      __in          const tchar* szFilename,
      __in          const unsigned long cpgDatabaseSizeMax,
      __in          JET_GRBIT grbit
    );
```

### Parameters

*sesid*

The database session context that will be used for the API call.

*szFilename*

The name of the database to attach.

*cpgDatabaseSizeMax*

The maximum size, in database pages, for database. The default database page size is 4 kilobytes, which can be changed using the [JetSetSystemParameter](./jetsetsystemparameter-function.md) function prior to creating a database.

Passing zero means that there is no maximum enforced by the database engine.

*grbit*

A group of bits that contain the options to be used for this call, which include zero or more of the following:

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
<td><p>JET_bitDbDeleteCorruptIndexes</p></td>
<td><p>If <a href="gg269337(v=exchg.10).md">JET_paramEnableIndexChecking</a> has been set, all indexes over Unicode data will be deleted. See the Remarks section for more details.</p></td>
</tr>
<tr class="even">
<td><p>JET_bitDbDeleteUnicodeIndexes</p></td>
<td><p>All indexes over Unicode data will be deleted, regardless of the setting of <a href="gg269337(v=exchg.10).md">JET_paramEnableIndexChecking</a>. See the Remarks section for more details.</p></td>
</tr>
<tr class="odd">
<td><p>JET_bitDbReadOnly</p></td>
<td><p>Prevents modifications to the database.</p></td>
</tr>
<tr class="even">
<td><p>JET_bitDbUpgrade</p></td>
<td><p>Reserved for future use.</p></td>
</tr>
</tbody>
</table>


### Return Value

The function returns one of the [JET_ERR](./jet-err.md) error codes. The following are the most commonly returned. (For a complete list of errors for this API, see [Extensible Storage Engine Error Codes](./extensible-storage-engine-error-codes.md).)

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
<td><p>Attaching a database is not allowed during a backup.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errDatabaseFileReadOnly</p></td>
<td><p>The database file specified by <em>szFilename</em> must be writable. The Read-Only attribute must not be set, and the running process must have sufficient privileges to write to the file.</p></td>
</tr>
<tr class="even">
<td><p>JET_errDatabaseInUse</p></td>
<td><p>The database file is already opened by another process.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errDatabaseInvalidPath</p></td>
<td><p>An invalid path was given in <em>szFilename</em>. <em>szFilename</em> must be non-NULL and refer to a valid path.</p></td>
</tr>
<tr class="even">
<td><p>JET_errDatabaseSharingViolation</p></td>
<td><p>The database file has already been attached by a different session.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errFileNotFound</p></td>
<td><p>The file given in <em>szFilename</em> does not exist.</p></td>
</tr>
<tr class="even">
<td><p>JET_errPrimaryIndexCorrupted</p></td>
<td><p>There is an error with the primary index. This may be from physical corruption (such as disk or memory corruption). It may also be returned when attaching a database last modified on an older operating system and the primary index is over a column with Unicode data. See the remarks for more information on indexes over Unicode data.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errSecondaryIndexCorrupted</p></td>
<td><p>There is an error with a secondary index. This may be from physical corruption (such as disk or memory corruption). It may also be returned when attaching a database last modified on an older operating system and a secondary index is over a column with Unicode data. See the remarks for more information on indexes over Unicode data. Secondary indexes are completely rebuilt when a database is defragmented with an offline utility using the following command: <strong>esentutl -d</strong>.</p></td>
</tr>
<tr class="even">
<td><p>JET_errTooManyAttachedDatabases</p></td>
<td><p>Only a finite number of databases can be attached per instance. The limit is currently seven databases per instance.</p></td>
</tr>
<tr class="odd">
<td><p>JET_wrnDatabaseAttached</p></td>
<td><p>A nonfatal warning indicating that the database file has already been attached by this session.</p></td>
</tr>
</tbody>
</table>


#### Remarks

The database file is detached using [JetDetachDatabase](./jetdetachdatabase-function.md) or [JetDetachDatabase2](./jetdetachdatabase2-function.md).

See [JetAttachDatabase](./jetattachdatabase-function.md) for remarks.

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
<td><p>Implemented as <strong>JetAttachDatabase2W</strong> (Unicode) and <strong>JetAttachDatabase2A</strong> (ANSI).</p></td>
</tr>
</tbody>
</table>


#### See Also

[Extensible Storage Engine Files](./extensible-storage-engine-files.md)  
[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JetAttachDatabase](./jetattachdatabase-function.md)  
[JetCreateDatabase](./jetcreatedatabase-function.md)  
[JetOpenDatabase](./jetopendatabase-function.md)  
[JetSetSystemParameter](./jetsetsystemparameter-function.md)
