---
description: "Learn more about: JET_COLUMNBASE Structure"
title: JET_COLUMNBASE Structure
TOCTitle: JET_COLUMNBASE Structure
ms:assetid: 171275c3-966d-409d-ad20-a8f240f7500d
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269194(v=EXCHG.10)
ms:contentKeyID: 32765497
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

# JET_COLUMNBASE Structure


_**Applies to:** Windows | Windows Server_

## JET_COLUMNBASE Structure

The **JET_COLUMNBASE** structure describes the parameters of a base column. The [JetGetColumnInfo](./jetgetcolumninfo-function.md) and [JetGetTableColumnInfo](./jetgettablecolumninfo-function.md) functions use the **JET_COLUMNBASE** structure.

```cpp
    typedef struct {
      unsigned long cbStruct;
      JET_COLUMNID columnid;
      JET_COLTYP coltyp;
      unsigned short wCountry;
      unsigned short langid;
      unsigned short cp;
      unsigned short wFiller;
      unsigned long cbMax;
      JET_GRBIT grbit;
      tchar szBaseTableName[256];
      tchar szBaseColumnName[256];
    } JET_COLUMNBASE;
```

### Members

**cbStruct**

The size of this structure, in bytes. Set **cbStruct** to sizeof( JET_COLUMNBASE ).

**columnid**

Reserved. Set **columnid** to 0 (zero).

**coltyp**

The type of the column (for example, text, binary, or numerical). For more information, see [JET_COLTYP](./jet-coltyp.md).

**wCountry**

Reserved. Set to 0 (zero).

**langid**

Reserved. Set to 0 (zero).

**cp**

The code page for the column. The only valid values for text columns are English (1252) and Unicode (1200). A value of zero means the default will be used (English, 1252). If the column is not a text column, the code page is automatically set to zero.

**wFiller**

Reserved. Set to 0 (zero).

**cbMax**

The maximum length, in bytes, of a variable-length column, or the actual length, in bytes, of a fixed-length column.

**grbit**

Options for the column, including zero or more of the following values.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitColumnFixed</p> | <p>The column is fixed and occupies the same amount of space in a row regardless of how much data it contains. JET_bitColumnFixed cannot be combined with JET_bitColumnTagged, and cannot be used when the <strong>coltyp</strong> member is set to <strong>JET_coltypLongText</strong> or <strong>JET_coltypLongBinary</strong>.</p> | 
| <p>JET_bitColumnTagged</p> | <p>The column is tagged and occupies space in the database only if it contains data. JET_bitColumnTagged cannot be combined with JET_bitColumnFixed, JET_bitColumnVersion, or JET_bitColumnEscrowUpdate.</p> | 
| <p>JET_bitColumnNotNULL</p> | <p>The column must not be set to a <strong>NULL</strong> value.</p><p>JET_bitColumnNotNULL cannot be combined with JET_bitColumnUserDefinedDefault.</p> | 
| <p>JET_bitColumnVersion</p> | <p>The column is a version column that specifies the version of the row. The value of this column starts at zero and is automatically incremented for each update of the row.</p><p>JET_bitColumnVersion can be used only when the <strong>coltyp</strong> member is set to <strong>JET_coltypLong</strong> and cannot be combined with JET_bitColumnAutoincrement, JET_bitColumnEscrowUpdate, JET_bitColumnTagged, or JET_bitColumnUserDefinedDefault.</p> | 
| <p>JET_bitColumnAutoincrement</p> | <p>The column is automatically incremented. The number is an increasing number, and is guaranteed to be unique within a table. The numbers, however, may not be sequential. For example, if five rows are inserted into a table, the automatically incremented column could contain the values { 1, 2, 6, 7, 8 }.</p><p>JET_bitColumnAutoincrement can be used only when the <strong>coltyp</strong> member is set to <strong>JET_coltypLong</strong> or <strong>JET_coltypCurrency</strong> and cannot be combined with JET_bitColumnEscrowUpdate, JET_bitColumnUserDefinedDefault, or JET_bitColumnVersion.</p><p><strong>Windows 2000:  </strong>JET_bitColumnVersion can be used only when the <strong>coltyp</strong> member is set to <strong>JET_coltypLong</strong>.</p> | 
| <p>JET_bitColumnUpdatable</p> | <p>Valid only for calls to <a href="gg269215(v=exchg.10).md">JetGetColumnInfo</a>. JET_bitColumnUpdatable cannot be combined with JET_bitColumnUserDefinedDefault.</p> | 
| <p>JET_bitColumnTTKey</p> | <p>Valid only on calls to <a href="gg294118(v=exchg.10).md">JetOpenTable</a>.</p> | 
| <p>JET_bitColumnTTDescending</p> | <p>Valid only on calls to <a href="gg269211(v=exchg.10).md">JetOpenTempTable</a>.</p> | 
| <p>JET_bitColumnMultiValued</p> | <p>The column can be multi-valued. A multi-valued column can have zero, one, or more values associated with it. The various values in a multi-valued column are identified by a number in the <strong>itagSequence</strong> member of various structures, for example, <a href="gg294049(v=exchg.10).md">JET_RETINFO</a>, <a href="gg294090(v=exchg.10).md">JET_SETINFO</a>, <a href="gg269233(v=exchg.10).md">JET_SETCOLUMN</a>, <a href="gg269334(v=exchg.10).md">JET_RETRIEVECOLUMN</a>, <a href="gg294052(v=exchg.10).md">JET_ENUMCOLUMNVALUE</a>. Multi-valued columns must be tagged columns; that is, they may not be fixed-length or variable-length columns.</p> | 
| <p>JET_bitColumnEscrowUpdate</p> | <p>Specifies that a column is an escrow update column that can be updated concurrently by different sessions with <a href="gg294125(v=exchg.10).md">JetEscrowUpdate</a> and will have transactional consistency.</p><ul><li><p>An escrow update column can be created only when the table is empty.</p></li></ul><ul><li><p>For an escrow update column, the <strong>coltyp</strong> member must be set to <strong>JET_coltypLong.</strong></p></li></ul><ul><li><p>An escrow update column must have a default value (that is <strong>cbDefault</strong> must be positive).</p></li></ul><ul><li><p>JET_bitColumnEscrowUpdate cannot be combined with JET_bitColumnTagged, JET_bitColumnVersion, or JET_bitColumnAutoincrement.</p></li></ul> | 
| <p>JET_bitColumnUnversioned</p> | <p>The column is created without a version number. This means that other transactions attempting to add a column with the same name will fail. JET_bitColumnUnversioned is used only with <a href="gg294122(v=exchg.10).md">JetAddColumn</a>. It cannot be used within a transaction.</p> | 
| <p>JET_bitColumnMaybeNull</p> | <p>Reserved for future use.</p><p>JET_bitColumnMaybeNull cannot be combined with JET_bitColumnUserDefinedDefault.</p> | 
| <p>JET_bitColumnFinalize</p> | <p>Do not use. Use JET_bitColumnDeleteOnZero instead.</p><p>The column can be finalized. A column that can be finalized is an escrow update column that causes the row to be deleted when the column reaches zero. Future versions may invoke a callback function instead (See <a href="gg294098(v=exchg.10).md">JET_CALLBACK</a>). A column that can be finalized must be an escrow update column. JET_bitColumnFinalize cannot be combined with JET_bitColumnUserDefinedDefault.</p> | 
| <p>JET_bitColumnUserDefinedDefault</p> | <p>The default value for a column will be provided by a callback function. See <a href="gg294098(v=exchg.10).md">JET_CALLBACK</a>. A column that has a user-defined default must be a tagged column. If JET_bitColumnUserDefinedDefault is specified, the <strong>pvDefault</strong> must point to a <a href="gg269200(v=exchg.10).md">JET_USERDEFINEDDEFAULT</a> structure, and <strong>cbDefault</strong> must be set to sizeof( JET_USERDEFINEDDEFAULT ).</p><p>JET_bitColumnUserDefinedDefault cannot be combined with JET_bitColumnFixed, JET_bitColumnNotNULL, JET_bitColumnVersion, JET_bitColumnAutoincrement, JET_bitColumnUpdatable, JET_bitColumnEscrowUpdate, JET_bitColumnFinalize, JET_bitColumnDeleteOnZero, or JET_bitColumnMaybeNull.</p> | 
| <p>JET_bitColumnDeleteOnZero</p> | <p>The column is an escrow update column and when it reaches zero, the record will be deleted. A common use for delete-on-zero columns is as reference count fields. When the number of references fall to zero, the record is deleted. A delete-on-zero column must be an escrow update column.</p><p>JET_bitColumnDeleteOnZero replaces JET_bitColumnFinalize.</p><p>JET_bitColumnDeleteOnZero cannot be combined with JET_bitColumnFinalize or JET_bitColumnUserDefinedDefault, and cannot be used with user-defined default columns.</p> | 



**szBaseTableName**

The table from which the current table inherits its DDL.

**szBaseColumnName**

The name of the column in the template table.

### Remarks

**JET_COLUMNBASE** contains much of the same information as [JET_COLUMNDEF](./jet-columndef-structure.md), but it adds string fields to describe the base table (if a hierarchical DDL was used).

### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JET_COLUMNBASE_W</strong> (Unicode) and <strong>JET_COLUMNBASE_A</strong> (ANSI).</p> | 



### See Also

[JET_CALLBACK](./jet-callback-callback-function.md)  
[JET_COLTYP](./jet-coltyp.md)  
[JET_COLUMNDEF](./jet-columndef-structure.md)  
[JET_COLUMNID](./jet-columnid.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JET_USERDEFINEDDEFAULT](./jet-userdefineddefault-structure.md)  
[JetGetColumnInfo](./jetgetcolumninfo-function.md)  
[JetGetTableColumnInfo](./jetgettablecolumninfo-function.md)  
[JetRenameColumn](./jetrenamecolumn-function.md)
