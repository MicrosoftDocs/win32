---
description: "Learn more about: JetGetDatabaseFileInfo Function"
title: JetGetDatabaseFileInfo Function
TOCTitle: JetGetDatabaseFileInfo Function
ms:assetid: 457079d9-46c9-4da0-a35b-0c11fca7ed5b
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269239(v=EXCHG.10)
ms:contentKeyID: 32765541
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetGetDatabaseFileInfo
- JetGetDatabaseFileInfoW
- JetGetDatabaseFileInfoA
topic_type: 
- kbArticle
- apiref
api_type: 
- COM
- DLLExport
api_location: 
- ESENT.DLL
ROBOTS: INDEX,FOLLOW

---

# JetGetDatabaseFileInfo Function


_**Applies to:** Windows | Windows Server_

## JetGetDatabaseFileInfo Function

The **JetGetDatabaseFileInfo** function retrieves various types of information about the database. This API can be called while a database is attached or online (with [JetGetDatabaseInfo](./jetgetdatabaseinfo-function.md)) or while the database or database engine is offline (with **JetGetDatabaseFileInfo**).

```cpp
    JET_ERR JET_API JetGetDatabaseFileInfo(
      __in          const tchar* szDatabaseName,
      __out         void* pvResult,
      __in          unsigned long cbMax,
      __in          unsigned long InfoLevel
    );
```

### Parameters

*szDatabaseName*

The path of the database from which to retrieve the information.

*pvResult*

Pointer to a buffer that will receive the specified information. The size of the buffer, in bytes, is passed in *cbMax*.

If this function fails, the contents of *pvResult* are undefined.

The information stored in *pvResult* depends on *InfoLevel*.

*cbMax*

The size, in bytes, of the buffer passed in *pvResult*.

*InfoLevel*

*InfoLevel* specifies which type of information should be retrieved about the specified database. It affects how *pvResult* is interpreted. Some *InfoLevel* objects are available only in the offline (**JetGetDatabaseFileInfo**) or online ([JetGetDatabaseInfo](./jetgetdatabaseinfo-function.md)) version of the API.

If the *pvResult* buffer provided is too small, either JET_errInvalidBufferSize or JET_errBufferTooSmall will be returned, depending on the *InfoLevel*.

<table>
<colgroup>
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th><p>Value</p></th>
<th><p>Meaning</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>JET_DbInfoFilesize</p></td>
<td><p><em>pvResult</em> will be interpreted as a QWORD (8 bytes). Returns the size of the database in bytes.</p></td>
</tr>
<tr class="even">
<td><p>JET_DbInfoUpgrade</p></td>
<td><p><em>pvResult</em> will be interpreted as a <a href="gg294114(v=exchg.10).md">JET_DBINFOUPGRADE</a>. The <a href="gg294114(v=exchg.10).md">JET_DBINFOUPGRADE</a> structure will be populated with information pertaining to the specified database.</p></td>
</tr>
<tr class="odd">
<td><p>JET_DbInfoMisc</p></td>
<td><p><em>pvResult</em> will be interpreted as a <a href="gg294147(v=exchg.10).md">JET_DBINFOMISC</a>. The <a href="gg294147(v=exchg.10).md">JET_DBINFOMISC</a> structure will be populated with information pertaining to the specified database.</p></td>
</tr>
<tr class="even">
<td><p>JET_DbInfoDBInUse</p></td>
<td><p><em>pvResult</em> will be interpreted as a BOOL (4 bytes). This will return whether the database engine currently has any open or attached databases.</p>
<p><strong>Windows XP:  </strong>This value is introduced in Windows XP.</p></td>
</tr>
<tr class="odd">
<td><p>JET_DbInfoPageSize</p></td>
<td><p><em>pvResult</em> will be interpreted as a unsigned long. This will return the page size of the database in bytes.</p>
<p><strong>Windows XP:  </strong>This value is introduced in Windows XP.</p></td>
</tr>
<tr class="even">
<td><p>JET_DbInfoCp</p></td>
<td><p>These <em>InfoLevels</em> are not yet supported and return default values. Do not use these <em>InfoLevels</em>.</p></td>
</tr>
<tr class="odd">
<td><p>JET_DbInfoCountry</p></td>
<td><p>These <em>InfoLevels</em> are not yet supported and return default values. Do not use these <em>InfoLevels</em>.</p></td>
</tr>
<tr class="even">
<td><p>JET_DbInfoCollate</p></td>
<td><p>Same as JET_DbInfoCp.</p></td>
</tr>
<tr class="odd">
<td><p>JET_DbInfoIsam</p></td>
<td><p>These <em>InfoLevels</em> are deprecated and are not currently supported. Do not use these <em>InfoLevels</em>.</p></td>
</tr>
<tr class="even">
<td><p>JET_DbInfoConnect</p></td>
<td><p>Same as JET_DbInfoIsam.</p></td>
</tr>
<tr class="odd">
<td><p>JET_DbInfoFileType</p></td>
<td><p><strong>Windows Vista:  </strong>This <em>InfoLevel</em> value is introduced in Windows Vista.</p>
<p><em>pvResult</em> will be treated as a pointer to a DWORD. Returns an enumeration value, indicating what kind of file the engine considers this to be. File types are listed in the following table. For more information about these types of files and their usage to the engine, see <a href="gg294069(v=exchg.10).md">Extensible Storage Engine Files</a>.</p>
<div class="tableSection">
<table>
<colgroup>
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th><p>Value</p></th>
<th><p>Meaning</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>JET_filetypeUnknown</p></td>
<td><p>The type of file is unknown, or not an ESE file type.</p></td>
</tr>
<tr class="even">
<td><p>JET_filetypeDatabase</p></td>
<td><p>The file is a database file.</p></td>
</tr>
<tr class="odd">
<td><p>JET_filetypeLog</p></td>
<td><p>The file is a transaction log file.</p></td>
</tr>
<tr class="even">
<td><p>JET_filetypeCheckpoint</p></td>
<td><p>The file is a checkpoint file.</p></td>
</tr>
<tr class="odd">
<td><p>JET_filetypeTempDatabase</p></td>
<td><p>The file is a temporary database file.</p></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
</tbody>
</table>


### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).

<table>
<colgroup>
<col  />
<col  />
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
<td><p>JET_errFeatureNotAvailable</p></td>
<td><p>The <em>InfoLevel</em> requested was JET_DbInfoIsam. This is not supported.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errBufferTooSmall</p></td>
<td><p>The buffer that is given in <em>cbMax</em> is too small for the desired information.</p></td>
</tr>
<tr class="even">
<td><p>JET_errInvalidBufferSize</p></td>
<td><p>The buffer that is given in <em>cbMax</em> is not the correct size for the desired information.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errInvalidParameter</p></td>
<td><p>One of the parameters that was provided contained an unexpected value, or the combination of several parameter values yielded an unexpected result. This error will be returned by <a href="gg294076(v=exchg.10).md">JetGetDatabaseInfo</a> when the DBID provided is not a valid (attached) database. This error will be returned by <strong>JetGetDatabaseFileInfo</strong> and <a href="gg294076(v=exchg.10).md">JetGetDatabaseInfo</a> when an <em>InfoLevel</em> requested is not supported by that version of the function.</p></td>
</tr>
</tbody>
</table>


If this function succeeds, the requested data will be returned in the output buffer.

If this function fails, the output buffer will be in an undefined state.

#### Requirements

<table>
<colgroup>
<col  />
<col  />
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
<td><p>Implemented as <strong>JetGetDatabaseFileInfoW</strong> (Unicode) and <strong>JetGetDatabaseFileInfoA</strong> (ANSI).</p></td>
</tr>
</tbody>
</table>


#### See Also

[JET_ERR](./jet-err.md)  
[JET_DBINFOMISC](./jet-dbinfomisc-structure.md)  
[JET_DBINFOUPGRADE](./jet-dbinfoupgrade-structure.md)  
[JetGetDatabaseInfo](./jetgetdatabaseinfo-function.md)
