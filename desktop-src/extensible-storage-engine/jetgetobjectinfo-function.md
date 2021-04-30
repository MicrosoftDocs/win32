---
description: "Learn more about: JetGetObjectInfo Function"
title: JetGetObjectInfo Function
TOCTitle: JetGetObjectInfo Function
ms:assetid: 3e069c61-6dab-4b79-8bf2-7844d017598f
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269232(v=EXCHG.10)
ms:contentKeyID: 32765534
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetGetObjectInfo
- JetGetObjectInfoA
- JetGetObjectInfoW
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

# JetGetObjectInfo Function


_**Applies to:** Windows | Windows Server_

## JetGetObjectInfo Function

The **JetGetObjectInfo** function retrieves information about database objects. Currently, only tables are supported. [JetGetTableInfo](./jetgettableinfo-function.md) can be used to fetch more information than **JetGetObjectInfo**.

```cpp
    JET_ERR JET_API JetGetObjectInfo(
      __in          JET_SESID sesid,
      __in          JET_DBID dbid,
      __in          JET_OBJTYP objtyp,
      __in_opt      const tchar* szContainerName,
      __in_opt      const tchar* szObjectName,
      __out         void* pvResult,
      __in          unsigned long cbMax,
      __in          unsigned long InfoLevel
    );
```

### Parameters

*sesid*

The database session context to use.

*dbid*

The database from which the information is retrieved.

*objtyp*

The objects that contain information to be retrieved. Currently, only JET_objtypNil and JET_objtypTable are supported, both of which behave identically. Only tables will be retrieved.

*szContainerName*

This parameter is reserved for future use and passes **NULL**. The name of the types of objects about which to retrieve information.

*szObjectName*

The name of the object that contains information to retrieve. When *InfoLevel* uses the JET_ObjInfoList or JET_ObjInfoListNoStats options to retrieve a list of all objects, this value should be **NULL** or an empty string.

Only table names are currently supported.

*pvResult*

Pointer to a buffer which receives the specified information.

The size of the buffer, in bytes, is passed in *cbMax*. On failure the contents of *pvResult* are undefined.

The information that is stored in *pvResult* depends on *InfoLevel*.

*cbMax*

The size, in bytes, of the buffer passed in *pvResult*.

*InfoLevel*

Specifies which type of information to retrieve for the specified object. It affects how *pvResult* is interpreted.

The following options are available to set for this parameter.

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
<td><p>JET_ObjInfo</p></td>
<td><p><em>pvResult</em> is interpreted as a <a href="gg269353(v=exchg.10).md">JET_OBJECTINFO</a> structure.</p>
<p>The <a href="gg269353(v=exchg.10).md">JET_OBJECTINFO</a> structure is populated with information pertaining to the object that is named in <em>szObjectName</em>.</p>
<p>If the caller does not want to know the number of records and pages for the object, consider using JET_ObjInfoNoStats information level, which might be faster since statistics are not included.</p></td>
</tr>
<tr class="even">
<td><p>JET_ObjInfoList</p></td>
<td><p><em>pvResult</em> is interpreted as a <a href="gg269348(v=exchg.10).md">JET_OBJECTLIST</a> structure. Information about all objects is retrieved. A temporary table will be created, and the information that is necessary to traverse the temporary table is described in the <a href="gg269348(v=exchg.10).md">JET_OBJECTLIST</a> structure. For more information, see <a href="gg269348(v=exchg.10).md">JET_OBJECTLIST</a>. If the caller does not want to know the number of records and pages for the object, consider using JET_ObjInfoListNoStats, which might be faster.</p></td>
</tr>
<tr class="odd">
<td><p>JET_ObjInfoListACM</p></td>
<td><p>Deprecated and not currently supported.</p></td>
</tr>
<tr class="even">
<td><p>JET_ObjInfoListNoStats</p></td>
<td><p><em>pvResult</em> is interpreted as a <a href="gg269348(v=exchg.10).md">JET_OBJECTLIST</a> structure. Information about all objects is retrieved. A temporary table will be created, and the information that is necessary to traverse the temporary table is described in the <a href="gg269348(v=exchg.10).md">JET_OBJECTLIST</a> structure. For more information, see <a href="gg269348(v=exchg.10).md">JET_OBJECTLIST</a>. JET_ObjInfoListNoStats is identical to JET_ObjInfoList, except that the columns that report the number of records (<em>columnidcRecord</em>) and pages (<em>columnidcPage</em>) will not be updated.</p></td>
</tr>
<tr class="odd">
<td><p>JET_ObjInfoMax</p></td>
<td><p><em>pvResult</em> is interpreted as a <a href="gg269353(v=exchg.10).md">JET_OBJECTINFO</a>. The maximum size of the object is in pages. Currently only tables will be returned.</p></td>
</tr>
<tr class="even">
<td><p>JET_ObjInfoNoStats</p></td>
<td><p><em>pvResult</em> is interpreted as a <a href="gg269353(v=exchg.10).md">JET_OBJECTINFO</a>. Information about only the object given in <em>szObjectName</em> will be retrieved.</p>
<p>The <a href="gg269353(v=exchg.10).md">JET_OBJECTINFO</a> structure will be populated with information pertaining to the object that is named in <em>szObjectName</em>.</p>
<p>JET_ObjInfoNoStats is identical to JET_ObjInfo, except that the fields that report the number of records and pages are set to zero.</p></td>
</tr>
<tr class="odd">
<td><p>JET_ObjInfoRulesLoaded</p></td>
<td><p>Deprecated and not currently supported.</p></td>
</tr>
<tr class="even">
<td><p>JET_ObjInfoSysTabCursor</p></td>
<td><p>Deprecated and not currently supported.</p></td>
</tr>
<tr class="odd">
<td><p>JET_ObjInfoSysTabReadOnly</p></td>
<td><p>Deprecated and not currently supported.</p></td>
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
<td><p>The size of the buffer given in <em>cbMax</em> was too small to hold the desired information.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errInvalidName</p></td>
<td><p>An invalid name was given in <em>szObjectName</em> or <em>szContainerName</em>.</p></td>
</tr>
<tr class="even">
<td><p>JET_errInvalidParameter</p></td>
<td><p>A bad parameter was given. It is possible that a bad level was passed in to <em>InfoLevel</em>.</p></td>
</tr>
</tbody>
</table>


#### Remarks

If **JetGetObjectInfo** successfully creates a temporary table (for example, JET_ObjInfoList or JET_ObjInfoNoStats), the caller is responsible for closing the temporary table with [JetCloseTable](./jetclosetable-function.md).

**JetGetObjectInfo** currently only supports retrieving information about tables.

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
<td><p>Implemented as <strong>JetGetObjectInfoW</strong> (Unicode) and <strong>JetGetObjectInfoA</strong> (ANSI).</p></td>
</tr>
</tbody>
</table>


#### See Also

[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_OBJTYP](./jet-objtyp.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JET_OBJECTINFO](./jet-objectinfo-structure.md)  
[JET_OBJECTLIST](./jet-objectlist-structure.md)  
[JetCloseTable](./jetclosetable-function.md)  
[JetGetTableInfo](./jetgettableinfo-function.md)
