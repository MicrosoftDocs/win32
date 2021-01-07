---
description: "Learn more about: JetGetTableInfo Function"
title: JetGetTableInfo Function
TOCTitle: JetGetTableInfo Function
ms:assetid: 0602186c-b5c3-44b5-87df-482680442afd
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269177(v=EXCHG.10)
ms:contentKeyID: 32765480
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetGetTableInfoW
- JetGetTableInfo
- JetGetTableInfoA
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

# JetGetTableInfo Function


_**Applies to:** Windows | Windows Server_

## JetGetTableInfo Function

The **JetGetTableInfo** function retrieves various pieces of information about a table in a database.

```cpp
    JET_ERR JET_API JetGetTableInfo(
      __in          JET_SESID sesid,
      __in          JET_TABLEID tableid,
      __out         void* pvResult,
      __in          unsigned long cbMax,
      __in          unsigned long InfoLevel
    );
```

### Parameters

*sesid*

The database session context to use for the API call.

*tableid*

The table that the information applies to.

*pvResult*

Pointer to a buffer that will receive the information. The type of the buffer is dependent on *InfoLevel*. It is the responsibility of the caller to align the buffer appropriately.

*cbMax*

The size, in bytes, of the buffer that was passed in *pvResult*.

*InfoLevel*

The type of information that will be retrieved for the table that is specified by *tableid*. The format of the data that is stored in *pvResult* is dependent on *InfoLevel*.

The following options can be set for this parameter:

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
<td><p>JET_TblInfo</p></td>
<td><p><em>pvResult</em> is interpreted as a <a href="gg269353(v=exchg.10).md">JET_OBJECTINFO</a> structure. If the method succeeds, the <a href="gg269353(v=exchg.10).md">JET_OBJECTINFO</a> structure is filled in with the appropriate data. If it fails, the contents are undefined.</p></td>
</tr>
<tr class="even">
<td><p>JET_TblInfoDbid</p></td>
<td><p><em>pvResult</em> is treated as an array of two <a href="gg269248(v=exchg.10).md">JET_DBID</a> objects. The database identifier of the database that owns the table is stored in this array twice.</p></td>
</tr>
<tr class="odd">
<td><p>JET_TblInfoDumpTable</p></td>
<td><p>JET_TblInfoDumpTable is deprecated. The API will return JET_errFeatureNotAvailable.</p></td>
</tr>
<tr class="even">
<td><p>JET_TblInfoName</p></td>
<td><p>JET_TblInfoName retrieves the name of the table and stores it in <em>pvResult</em>. If the buffer is too small, the behavior is undefined.</p></td>
</tr>
<tr class="odd">
<td><p>JET_TblInfoMostMany</p></td>
<td><p>JET_TblInfoMostMany retrieves the name of the table and stores it in <em>pvResult</em>. If the buffer is too small, the behavior is undefined.</p></td>
</tr>
<tr class="even">
<td><p>JET_TblInfoOLC</p></td>
<td><p>JET_TblInfoOLC is deprecated. The API will return JET_errFeatureNotAvailable.</p></td>
</tr>
<tr class="odd">
<td><p>JET_TblInfoRvt</p></td>
<td><p>JET_TblInfoRvt is deprecated. The API will return JET_errQueryNotSupported.</p></td>
</tr>
<tr class="even">
<td><p>JET_TblInfoResetOLC</p></td>
<td><p>JET_TblInfoResetOLC is deprecated. The API will return JET_errFeatureNotAvailable.</p></td>
</tr>
<tr class="odd">
<td><p>JET_TblInfoSpaceAlloc</p></td>
<td><p><em>pvResult</em> is interpreted as an array of two ULONGs:</p>
<ul>
<li><p>The first <strong>ULONG</strong> is the number of pages in the table.</p></li>
<li><p>The second <strong>ULONG</strong> is the target density of pages for the table.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>JET_TblInfoSpaceAvailable</p></td>
<td><p><em>pvResult</em> is interpreted as a <strong>ULONG</strong>. The <strong>ULONG</strong> is the sum of the number of pages that are available in the table, its indexes, and the long value tree.</p></td>
</tr>
<tr class="odd">
<td><p>JET_TblInfoSpaceOwned</p></td>
<td><p><em>pvResult</em> is interpreted as a <strong>ULONG</strong>. The <strong>ULONG</strong> is the sum of the number of pages that are owned by the table (including its indexes, and the long value tree and any available pages therein).</p></td>
</tr>
<tr class="even">
<td><p>JET_TblInfoSpaceUsage</p></td>
<td><p>The behavior of the API depends on how large the buffer that is passed to the API is. Two <em>cbMax</em> values must be at least ( 2 * sizeof( ULONG ) ).</p>
<ul>
<li><p>If <em>cbMax</em> is ( 2 * sizeof( ULONG ) ), <em>pvResult</em> is interpreted as an array of two ULONGs:</p>
<ul>
<li><p>The first <strong>ULONG</strong> is the number of Owned Extents of the table.</p></li>
<li><p>The second <strong>ULONG</strong> is the number of Available Extents of the table.</p></li>
</ul></li>
<li><p><em>pvResult</em> is interpreted as an array of:</p>
<ul>
<li><p>The first <strong>ULONG</strong> is the number of Owned Extents of the table.</p></li>
<li><p>The second <strong>ULONG</strong> is the number of Available Extents of the table.</p></li>
</ul></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>JET_TblInfoTemplateTableName</p></td>
<td><p><em>pvResult</em> is interpreted as a string buffer. The buffer must be at least JET_cbNameMost + 1, including the terminating <strong>NULL</strong>. If the table is a derived table, the buffer will be filled in with the name of the table from which the derived table inherited its DDL. If the table is not a derived table, the buffer will an empty string.</p></td>
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
<td><p>The buffer was too small.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errFeatureNotAvailable</p></td>
<td><p>A deprecated <em>InfoLevel</em> was specified.</p></td>
</tr>
<tr class="even">
<td><p>JET_errInvalidBufferSize</p></td>
<td><p>The buffer was not the right size.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errInvalidOperation</p></td>
<td><p>The table that was passed in was a temporary table, and the requested <em>InfoLevel</em> cannot be retrieved for a temporary table.</p></td>
</tr>
<tr class="even">
<td><p>JET_errObjectNotFound</p></td>
<td><p>The table that was passed in was a temporary table, and the requested <em>InfoLevel</em> cannot be retrieved for a temporary table.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errQueryNotSupported</p></td>
<td><p>The <em>InfoLevel</em> is not supported.</p></td>
</tr>
<tr class="even">
<td><p>JET_errTableInUse</p></td>
<td><p>The table is being used by another database operation.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errTableLocked</p></td>
<td><p>The table is locked by another database operation.</p></td>
</tr>
<tr class="even">
<td><p>JET_wrnTableInUseBySystem</p></td>
<td><p>The table is being used by the system. This warning is nonfatal.</p></td>
</tr>
</tbody>
</table>


#### Remarks

Some pieces of information are not valid for temporary tables (See [JetOpenTempTable](./jetopentemptable-function.md)).

The table statistics include the number of records and the number of pages in the clustered index (that is, the index containing the record data). The index statistics are accessed separately by name, using [JetGetIndexInfo](./jetgetindexinfo-function.md) or [JetGetTableIndexInfo](./jetgettableindexinfo-function.md).

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
<td><p>Implemented as <strong>JetGetTableInfoW</strong> (Unicode) and <strong>JetGetTableInfoA</strong> (ANSI).</p></td>
</tr>
</tbody>
</table>


#### See Also

[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JET_OBJECTINFO](./jet-objectinfo-structure.md)  
[JetGetIndexInfo](./jetgetindexinfo-function.md)  
[JetGetObjectInfo](./jetgetobjectinfo-function.md)  
[JetGetTableIndexInfo](./jetgettableindexinfo-function.md)  
[JetOpenTempTable](./jetopentemptable-function.md)
