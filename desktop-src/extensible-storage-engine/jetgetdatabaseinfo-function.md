---
description: "Learn more about: JetGetDatabaseInfo Function"
title: JetGetDatabaseInfo Function
TOCTitle: JetGetDatabaseInfo Function
ms:assetid: bd3f92d0-7e98-4aa6-87c5-1c2760cbd1b5
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294076(v=EXCHG.10)
ms:contentKeyID: 32765691
ms.date: 04/11/2016
ms.topic: reference
api_name: 
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

# JetGetDatabaseInfo Function


_**Applies to:** Windows | Windows Server_

## JetGetDatabaseInfo Function

The **JetGetDatabaseInfo** function retrieves various types of information about the database. This API can be called while a database is attached or online (with **JetGetDatabaseInfo**) or while the database or database engine is offline (with [JetGetDatabaseFileInfo](./jetgetdatabasefileinfo-function.md)).

```cpp
    JET_ERR JET_API JetGetDatabaseInfo(
      __in          JET_SESID sesid,
      __in          JET_DBID dbid,
      __out         void* pvResult,
      __in          unsigned long cbMax,
      __in          unsigned long InfoLevel
    );
```

### Parameters

*sesid*

The session to use for this call.

*dbid*

The [JET_DBID](./jet-dbid.md) for the database to retrieve the information from.

*pvResult*

Pointer to a buffer which will receive the specified information. The size of the buffer, in bytes, is passed in *cbMax*.

On failure the contents of *pvResult* are undefined.

The information stored in *pvResult* depends on *InfoLevel*.

*cbMax*

The size, in bytes, of the buffer that was passed in *pvResult*.

*InfoLevel*

*InfoLevel* specifies which type of information should be retrieved about the specified database. It affects how *pvResult* is interpreted. Some *InfoLevel* are available only in the offline ([JetGetDatabaseFileInfo](./jetgetdatabasefileinfo-function.md)) or online (**JetGetDatabaseInfo**) version of the API.

If the *pvResult* buffer provided is too small, either JET_errInvalidBufferSize or JET_errBufferTooSmall will be returned depending on the *InfoLevel*.

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
<td><p>JET_DbInfoCollate</p></td>
<td><p>Not yet supported and return default values. Do not use.</p></td>
</tr>
<tr class="even">
<td><p>JET_DbInfoConnect</p></td>
<td><p>These <em>InfoLevels</em> are deprecated and are not currently supported. Do not use.</p></td>
</tr>
<tr class="odd">
<td><p>JET_DbInfoCountry</p></td>
<td><p>Not yet supported and return default values. Do not use.</p></td>
</tr>
<tr class="even">
<td><p>JET_DbInfoCp</p></td>
<td><p>Not yet supported and return default values. Do not use.</p></td>
</tr>
<tr class="odd">
<td><p>JET_DbInfoFilename</p></td>
<td><p><em>pvResult</em> will be interpreted as a string buffer (char *). A MAX_PATH buffer is suggested, however not required. If the buffer is not long enough, JET_errBufferTooSmall will be returned. The string will be populated with the path of the database for this DBID.</p></td>
</tr>
<tr class="even">
<td><p>JET_DbInfoFilesize</p></td>
<td><p><em>pvResult</em> will be interpreted as a DWORD (4 bytes). Returns the size of the database in pages.</p></td>
</tr>
<tr class="odd">
<td><p>JET_DbInfoIsam</p></td>
<td><p>These <em>InfoLevels</em> are deprecated and are not currently supported. Do not use.</p></td>
</tr>
<tr class="even">
<td><p>JET_DbInfoLCID</p></td>
<td><p>(Windows XP and later) This <em>InfoLevel</em> was originally specified as: JET_DbInfoLangid (Windows 2000)</p>
<p><em>pvResult</em> will be interpreted as a long. This returns the Locale identifier (LCID) associate with this database.</p></td>
</tr>
<tr class="odd">
<td><p>JET_DbInfoMisc</p></td>
<td><p><em>pvResult</em> will be interpreted as a <a href="gg294147(v=exchg.10).md">JET_DBINFOMISC</a>. The <a href="gg294147(v=exchg.10).md">JET_DBINFOMISC</a> structure will be populated with information pertaining to the database specified.</p></td>
</tr>
<tr class="even">
<td><p>JET_DbInfoOptions</p></td>
<td><p><em>pvResult</em> will be interpreted as a <a href="gg294066(v=exchg.10).md">JET_GRBIT</a> (DWORD). This returns whether the database is opened in exclusive mode. If the database is in exclusive mode JET_bitDbExclusive will be set in the <a href="gg294066(v=exchg.10).md">JET_GRBIT</a> provided, otherwise zero is set. Note other database <em>grbit</em> options for <a href="gg294074(v=exchg.10).md">JetAttachDatabase</a> and <a href="gg269299(v=exchg.10).md">JetOpenDatabase</a> are not returned.</p></td>
</tr>
<tr class="odd">
<td><p>JET_DbInfoPageSize</p></td>
<td><p>Available only on Windows XP and later. <em>pvResult</em> will be interpreted as a unsigned long. This will return the page size of the database in bytes.</p></td>
</tr>
<tr class="even">
<td><p>JET_DbInfoSpaceAvailable</p></td>
<td><p><em>pvResult</em> will be interpreted as a DWORD. This returns the available space for the database in pages.</p></td>
</tr>
<tr class="odd">
<td><p>JET_DbInfoSpaceOwned</p></td>
<td><p><em>pvResult</em> will be interpreted as a DWORD. This returns the owned space for the database in pages.</p></td>
</tr>
<tr class="even">
<td><p>JET_DbInfoTransactions</p></td>
<td><p><em>pvResult</em> will be interpreted as a long. This will return one greater than the maximum level to which transactions can be nested. If <a href="gg294083(v=exchg.10).md">JetBeginTransaction</a> is called (in a nesting fashion, that is, on the same session, without a commit or rollback) as many times as this value, on the last call JET_errTransTooDeep will be returned from <a href="gg294083(v=exchg.10).md">JetBeginTransaction</a>. Note the value in Windows 2000, Windows XP, and Windows Server 2003 is 7.</p></td>
</tr>
<tr class="odd">
<td><p>JET_DbInfoVersion</p></td>
<td><p><em>pvResult</em> will be interpreted as a long. This returns the database engine's native major version. This value is 0x620 for Windows 2000, Windows XP, and Windows Server 2003.</p></td>
</tr>
</tbody>
</table>


### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).

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
<td><p>JET_errBufferTooSmall</p></td>
<td><p>The size of the buffer given in <em>cbMax</em> was too small (or not correct) to hold the desired information.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errFeatureNotAvailable</p></td>
<td><p>The <em>InfoLevel</em> requested was JET_DbInfoIsam. This is not supported.</p></td>
</tr>
<tr class="even">
<td><p>JET_errInvalidBufferSize</p></td>
<td><p>The size of the buffer given in <em>cbMax</em> was too small (or not correct) to hold the desired information.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errInvalidParameter</p></td>
<td><p>One of the parameters provided contained an unexpected value or contained a value that did not make sense when combined with the value of another parameter. This error will be returned by <strong>JetGetDatabaseInfo</strong> when the <a href="gg269248(v=exchg.10).md">JET_DBID</a> provided is not a valid (attached) database. This error will be returned by <a href="gg269239(v=exchg.10).md">JetGetDatabaseFileInfo</a> and <strong>JetGetDatabaseInfo</strong> when an <em>InfoLevel</em> requested is not supported by that version of the function.</p></td>
</tr>
</tbody>
</table>


On success, the requested data will be returned in the output buffer.

On failure, the output buffer will be in an undefined state.

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
<td><p>Implemented as <strong>JetGetDatabaseInfoW</strong> (Unicode) and <strong>JetGetDatabaseInfoA</strong> (ANSI).</p></td>
</tr>
</tbody>
</table>


#### See Also

[JET_DBID](./jet-dbid.md)  
[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_SESID](./jet-sesid.md)  
[JET_DBINFOMISC](./jet-dbinfomisc-structure.md)  
[JET_DBINFOUPGRADE](./jet-dbinfoupgrade-structure.md)  
[JetGetDatabaseFileInfo](./jetgetdatabasefileinfo-function.md)
