---
description: "Learn more about: JET_INDEXLIST Structure"
title: JET_INDEXLIST Structure
TOCTitle: JET_INDEXLIST Structure
ms:assetid: 0c092b48-e583-49f3-8f5e-1428a84d9265
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269185(v=EXCHG.10)
ms:contentKeyID: 32765488
ms.date: 04/11/2016
ms.topic: reference
api_name: 
topic_type: 
- apiref
- kbArticle
api_type: 
- COM
api_location: 
ROBOTS: INDEX,FOLLOW

---

# JET_INDEXLIST Structure


_**Applies to:** Windows | Windows Server_

## JET_INDEXLIST Structure

The **JET_INDEXLIST** structure contains the necessary information to traverse a temporary table that is created by the [JetGetIndexInfo](./jetgetindexinfo-function.md) or [JetGetTableIndexInfo](./jetgettableindexinfo-function.md) functions. Each row in the temporary table describes a column of an index.

```cpp
    typedef struct {
      unsigned long cbStruct;
      JET_TABLEID tableid;
      gned long cRecord;
      JET_COLUMNID columnidindexname;
      JET_COLUMNID columnidgrbitIndex;
      JET_COLUMNID columnidcKey;
      JET_COLUMNID columnidcEntry;
      JET_COLUMNID columnidcPage;
      JET_COLUMNID columnidcColumn;
      JET_COLUMNID columnidiColumn;
      JET_COLUMNID columnidcolumnid;
      JET_COLUMNID columnidcoltyp;
      JET_COLUMNID columnidCountry;
      JET_COLUMNID columnidLangid;
      JET_COLUMNID columnidCp;
      JET_COLUMNID columnidCollate;
      JET_COLUMNID columnidgrbitColumn;
      JET_COLUMNID columnidcolumnname;
      JET_COLUMNID columnidLCMapFlags;
    } JET_INDEXLIST;
```

### Members

**cbStruct**

The size of the structure in bytes. The API call will update this field, so the caller should ensure that this value matches sizeof( JET_INDEXLIST ).

**tableid**

The table identifier of the temporary table that was created. It is the responsibility of the caller to close the table.

**cRecord**

The number of records in the temporary table that was created.

**columnidindexname**

The column identifier of the name of the index.

This column is a [JET_coltypText](./jet-coltyp.md).

**columnidgrbitIndex**

The column identifier of the *grbits* used on the index. See [JET_INDEXCREATE](./jet-indexcreate-structure.md) for a list of valid bits.

This column is a [JET_coltypLong](./jet-coltyp.md).

**columnidcKey**

The column identifier of the number of keys in the index.

This column is a [JET_coltypLong](./jet-coltyp.md).

**columnidcEntry**

The column identifier of the number of entries in the index.

This column is a [JET_coltypLong](./jet-coltyp.md).

**columnidcPage**

The column identifier of the number of pages the index uses.This column is a [JET_coltypLong](./jet-coltyp.md).

**columnidcColumn**

The column identifier of the total number of columns that the index spans.

This column is a [JET_coltypLong](./jet-coltyp.md).

**columnidiColumn**

The column identifier of the number of the columns in the index. For more information, see the Remarks section of this topic.

This column is a [JET_coltypLong](./jet-coltyp.md).

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
<td><p>cIndexInfoCols<br />
15</p></td>
<td><p>Specifies that 15 columns are allowed.</p></td>
</tr>
<tr class="even">
<td><p>cColumnInfoCols<br />
14</p></td>
<td><p>Specifies that 14 columns are allowed.</p></td>
</tr>
<tr class="odd">
<td><p>cObjectInfoCols<br />
9</p></td>
<td><p>Specifies that 9 columns are allowed.</p></td>
</tr>
</tbody>
</table>


**columnidcolumnid**

The column identifier of the column that is indexed.For more information, see the Remarks section of this topic. This column is a [JET_coltypLong](./jet-coltyp.md).

**columnidcoltyp**

The column identifier of the coltyp of the column which is indexed. For more information, see the Remarks section of this topic. This column is a [JET_coltypLong](./jet-coltyp.md).

**columnidCountry**

The column identifier of the country code of the column that is indexed. The country code is deprecated.

This column is a [JET_coltypShort](./jet-coltyp.md).

**columnidLangid**

The column identifier of the language identifier (LCID) under which the index was created. For more information, see [JET_INDEXCREATE](./jet-indexcreate-structure.md).

This column is a [JET_coltypShort](./jet-coltyp.md).

**columnidCp**

The column identifier of the code page under which the index was created. For more information, see [JET_COLUMNCREATE](./jet-columncreate-structure.md).

This column is a [JET_coltypShort](./jet-coltyp.md).

**columnidCollate**

The column identifier of the collation sequence under which the index was created. The collation sequence is deprecated.

This column is a [JET_coltypShort](./jet-coltyp.md).

**columnidgrbitColumn**

The column identifier of the *grbits* that apply to the order of the column in the index.

The data for this column can be ordered as JET_bitKeyAscending or JET_bitKeyDescending. This column is a [JET_coltypLong](./jet-coltyp.md). For example, an index defined as "-column1\\0+column2\\0" will have JET_bitKeyDescending for "column1", and JET_bitKeyAscending for "column2".

The following options are valid for this member.

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
<td><p>JET_bitKeyAscending</p></td>
<td><p>An index segment in ascending order.</p></td>
</tr>
<tr class="even">
<td><p>JET_bitKeyDescending</p></td>
<td><p>An index segment in descending order.</p></td>
</tr>
</tbody>
</table>


**columnidcolumnname**

The column identifier of the name of the column.

This column is a [JET_coltypText](./jet-coltyp.md).

**columnidLCMapFlags**

The column identifier of the flags that are used to create the index. For more information, see the **dwMapFlags** section of [JET_UNICODEINDEX](./jet-unicodeindex-structure.md).

This column is a [JET_coltypLong](./jet-coltyp.md).

### Remarks

Each row in the temporary table corresponds to a column in a particular index.

For example, the index "+A\\0+B\\0+C\\0+D\\0+E\\0" is more than five columns, and it will occupy five rows in the temporary table. Each of these five rows will have a value of 5 in the column that is identified by columnid column. But each row will have a different value for columnid column, ranging from 0 to 4.

The number of keys in a particular index corresponds to the number of unique values for which a caller can seek and get an exact match. The number of entries is the number of rows that an index matches. If an index has a uniqueness constraint, then the number of keys is equal to the number of entries. For example, if a table contains the following information and an index is created over the column named "key", then there are three keys (100, 200, and 500), but there are four entries ("this", "is", "an", and "example").

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Key</p></th>
<th><p>Entry</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>100</p></td>
<td><p>&quot;this&quot;</p></td>
</tr>
<tr class="even">
<td><p>100</p></td>
<td><p>&quot;is&quot;</p></td>
</tr>
<tr class="odd">
<td><p>200</p></td>
<td><p>&quot;an&quot;</p></td>
</tr>
<tr class="even">
<td><p>500</p></td>
<td><p>&quot;example&quot;</p></td>
</tr>
</tbody>
</table>


### Requirements

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
</tbody>
</table>


### See Also

[JET_COLTYP](./jet-coltyp.md)  
[JET_COLUMNCREATE](./jet-columncreate-structure.md)  
[JET_COLUMNID](./jet-columnid.md)  
[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_INDEXCREATE](./jet-indexcreate-structure.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JET_UNICODEINDEX](./jet-unicodeindex-structure.md)  
[JetGetIndexInfo](./jetgetindexinfo-function.md)  
[JetGetTableIndexInfo](./jetgettableindexinfo-function.md)
