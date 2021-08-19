---
description: "Learn more about: JetGetColumnInfo Function"
title: JetGetColumnInfo Function
TOCTitle: JetGetColumnInfo Function
ms:assetid: 2db024e9-2784-4fb2-84b2-fef7ae518938
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269215(v=EXCHG.10)
ms:contentKeyID: 32765518
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetGetColumnInfoA
- JetGetColumnInfoW
- JetGetColumnInfo
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

# JetGetColumnInfo Function


_**Applies to:** Windows | Windows Server_

## JetGetColumnInfo Function

The **JetGetColumnInfo** function retrieves information about a column.

```cpp
    JET_ERR JET_API JetGetColumnInfo(
      __in          JET_SESID sesid,
      __in          JET_DBID dbid,
      __in          const tchar* szTableName,
      __in          const tchar* szColumnName,
      __out         void* pvResult,
      __in          unsigned long cbMax,
      __in          unsigned long InfoLevel
    );
```

### Parameters

*sesid*

The database session context to use for the API call.

*dbid*

Identifies, along with *szTableName*, the table that contains the column from which the information is retrieved.

*szTableName*

Identifies, along with *dbid*, the table that contains the column from which the information is retrieved.

*szColumnName*

The name of the column that information is fetched for.

*pvResult*

Pointer to a buffer that will receive the information. The type of the buffer is dependent on *InfoLevel*. The caller must be configured to align the buffer appropriately.

*cbMax*

The size, in bytes, of the buffer that is passed in *pvResult*.

*InfoLevel*

The type of information to retrieve for the column that is specified by *szColumnName*. The format of the data stored in *pvResult* is dependent on this parameter. For the schema of the temporary table, see [JET_COLUMNLIST](./jet-columnlist-structure.md).

These *InfoLevels* are differentiated by:

  - JET_ColInfoListSortColumnid will sort the temporary table by *columnid*.

  - JET_ColInfoListCompact will compact the output. For more information about the compact output, see [JET_COLUMNLIST](./jet-columnlist-structure.md).

The following options are available for use with this parameter.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_ColInfo</p> | <p>JET_ColInfo and JET_ColInfoByColid both retrieve the same information. <em>pvResult</em> is interpreted as a <a href="gg294130(v=exchg.10).md">JET_COLUMNDEF</a>, and the fields of the <a href="gg294130(v=exchg.10).md">JET_COLUMNDEF</a> structure are filled in appropriately.</p> | 
| <p>JET_ColInfoBase</p> | <p><em>pvResult</em> is interpreted as a <a href="gg269194(v=exchg.10).md">JET_COLUMNBASE</a> structure. This is similar to a <a href="gg294130(v=exchg.10).md">JET_COLUMNDEF</a> structure. If this function succeeds, the structure is populated with appropriate values. If this function fails, the structure contains undefined data.</p> | 
| <p>JET_ColInfoByColid</p> | <p>Like JET_ColInfo, <em>pvResult</em> is interpreted as a <a href="gg294130(v=exchg.10).md">JET_COLUMNDEF</a>, except this <em>InfoLevel</em> indicates that the requested column (<em>szColumName</em>) is not the string column name, but a pointer to a <a href="gg294104(v=exchg.10).md">JET_COLUMNID</a>.</p> | 
| <p>JET_ColInfoList</p> | <p><em>pvResult</em> is interpreted as a <a href="gg269228(v=exchg.10).md">JET_COLUMNLIST</a> structure. If this function succeeds, the structure is populated with appropriate values. A temporary table is opened and is identified by the <strong>tableid</strong> member of the <a href="gg269228(v=exchg.10).md">JET_COLUMNLIST</a> structure. The table must be closed with <a href="gg294087(v=exchg.10).md">JetCloseTable</a>. If this function fails, the structure contains undefined data.</p> | 
| <p>JET_ColInfoListCompact</p> | <p>Same as JET_ColInfoList.</p> | 
| <p>JET_ColInfoListSortColumnid</p> | <p>Same as JET_ColInfoList; however the resulting table is sorted by columnid, instead of column name.</p> | 
| <p>JET_ColInfoSysTabCursor</p> | <p>JET_ColInfoSysTabCursor is deprecated, and use of it will return JET_errFeatureNotAvailable.</p> | 
| <p>JET_ColInfoBaseByColId</p> | <p>Like JET_ColInfoBase, <em>pvResult</em> is interpreted as a <a href="gg269194(v=exchg.10).md">JET_COLUMNBASE</a>, except this <em>InfoLevel</em> indicates that requested column (<em>szColumName</em>) is not the string column name, but a pointer to a <a href="gg294104(v=exchg.10).md">JET_COLUMNID</a>.</p><p><strong>Windows Vista:  </strong>This value is introduced in Windows Vista.</p> | 
| <p>JET_ColInfoGrbitNonDerivedColumnsOnly</p> | <p>Only return non-derived columns (if the table is derived from a template).</p><p>This value can be logically or'd into the <em>InfoLevel</em>, when the base <em>InfoLevel</em> is JET_ColInfoList.</p><p><strong>Windows Vista:  </strong>This value is introduced Windows Vista.</p> | 
| <p>JET_ColInfoGrbitMinimalInfo</p> | <p>Only return the column name and columnid of each column.</p><p>This value can be logically or'd into the <em>InfoLevel</em>, when the base <em>InfoLevel</em> is JET_ColInfoList.</p><p><strong>Windows Vista:  </strong>This value is introduced in Windows Vista.</p> | 
| <p>JET_ColInfoGrbitSortByColumnid</p> | <p>Sort returned column list by columnid (default is to sort list by column name).</p><p>This value can be logically or'd into the <em>InfoLevel</em>, when the base <em>InfoLevel</em> is JET_ColInfoList.</p><p><strong>Windows Vista:  </strong>This value is introduced in Windows Vista.</p> | 



### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errColumnNotFound</p> | <p>The column named <em>szColumnName</em> was not found in the table.</p> | 
| <p>JET_errFeatureNotAvailable</p> | <p>A bad <em>InfoLevel</em> was specified.</p> | 
| <p>JET_errInvalidName</p> | <p>This error can be returned if:</p><ul><li><p>A bad name for <em>szTableName</em> was given.</p></li><li><p>A bad name for <em>szColumnName</em> was given.</p></li></ul> | 
| <p>JET_errInvalidParameter</p> | <p>This error can be returned if:</p><ul><li><p>A bad <em>InfoLevel</em> was specified.</p></li><li><p>A NULL <em>szTableName</em> was passed in.</p></li><li><p>The buffer is too small.</p></li></ul> | 



#### Remarks

[JetGetTableColumnInfo](./jetgettablecolumninfo-function.md) and **JetGetColumnInfo** both retrieve information about a column. The difference between them is how the table is identified:

  - [JetGetTableColumnInfo](./jetgettablecolumninfo-function.md) identifies a table by *tableid*.

  - **JetGetColumnInfo** identifies a table by *dbid* and *szTableName* combination.

When retrieving data with JET_ColInfoList, JET_ColInfoListSortColumnid, or JET_ColInfoListCompact, a temporary table will be opened. The temporary table contains data, and the [JET_COLUMNLIST](./jet-columnlist-structure.md) structure contains sufficient information to traverse the temporary table. The temporary table must be closed with [JetCloseTable](./jetclosetable-function.md).

#### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JetGetColumnInfoW</strong> (Unicode) and <strong>JetGetColumnInfoA</strong> (ANSI).</p> | 



#### See Also

[Error Handling Parameters](./error-handling-parameters.md)  
[Extensible Storage Engine Errors](./extensible-storage-engine-errors.md)  
[JET_COLUMNBASE](./jet-columnbase-structure.md)  
[JET_COLUMNDEF](./jet-columndef-structure.md)  
[JET_COLUMNID](./jet-columnid.md)  
[JET_COLUMNLIST](./jet-columnlist-structure.md)  
[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JetCloseTable](./jetclosetable-function.md)  
[JetGetTableColumnInfo](./jetgettablecolumninfo-function.md)
