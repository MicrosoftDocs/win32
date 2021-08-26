---
description: "Learn more about: JET_COLUMNDEF Structure"
title: JET_COLUMNDEF Structure
TOCTitle: JET_COLUMNDEF Structure
ms:assetid: ee1fc473-bff5-438e-98ae-247de12e76f9
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294130(v=EXCHG.10)
ms:contentKeyID: 32765744
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

# JET_COLUMNDEF Structure


_**Applies to:** Windows | Windows Server_

## JET_COLUMNDEF Structure

The **JET_COLUMNDEF** structure defines the data that can be stored in a column.

```cpp
    typedef struct {
      unsigned long cbStruct;
      JET_COLUMNID columnid;
      JET_COLTYP coltyp;
      unsigned short wCountry;
      unsigned short langid;
      unsigned short cp;
      unsigned short wCollate;
      unsigned long cbMax;
      JET_GRBIT grbit;
    } JET_COLUMNDEF;
```

### Members

**cbStruct**

The size of the structure, in bytes. It must be set to sizeof( JET_COLUMNDEF).

**columnid**

Reserved. **columnid** must be set to 0 (zero).

**coltyp**

The type of the column (for example, text, binary, or numerical). For more information, see [JET_COLTYP](./jet-coltyp.md).

**wCountry**

Reserved. **wCountry** must be set to 0 (zero).

**langid**

Obsolete. **langid** should be set to 0 (zero).

**cp**

The code page for the column. The only valid values for text columns are English (1252) and Unicode (1200). A value of zero means the default will be used (English, 1252). If the column is not a text column, the code page automatically gets set to zero.

**wCollate**

Reserved. **wCollate** must be set to 0 (zero).

**cbMax**

The maximum length, in bytes, of a variable-length column, or the length of a fixed-length column.

**grbit**

A group of bits that contain the options to be used for this call, which include zero or more of the following values.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitColumnFixed</p> | <p>The column will be fixed. It will always use the same amount of space in a row, regardless of how much data is being stored in the column. JET_bitColumnFixed cannot be used with JET_bitColumnTagged. This bit cannot be used with long values (that is <strong>JET_coltypLongText</strong> and <strong>JET_coltypLongBinary</strong>).</p> | 
| <p>JET_bitColumnTagged</p> | <p>The column will be tagged. Tagged columns do not take up any space in the database if they do not contain data. This bit cannot be used with JET_bitColumnFixed.</p> | 
| <p>JET_bitColumnNotNULL</p> | <p>The column must never be set to a NULL value.</p> | 
| <p>JET_bitColumnVersion</p> | <p>The column is a version column that specifies the version of the row. The value of this column starts at zero and will be automatically incremented for each update on the row.</p><p>This bit can only be applied to <strong>JET_coltypLong</strong> columns. This bit cannot be used with JET_bitColumnAutoincrement, JET_bitColumnEscrowUpdate, or JET_bitColumnTagged.</p> | 
| <p>JET_bitColumnAutoincrement</p> | <p>The column will automatically be incremented. The number is an increasing number, and is guaranteed to be unique within a table. The numbers, however, might not be continuous. For example, if five rows are inserted into a table, the "autoincrement" column could contain the values { 1, 2, 6, 7, 8 }. This bit can only be used on columns of type <strong>JET_coltypLong</strong> or <strong>JET_coltypCurrency</strong>.</p><p><strong>Windows 2000:  </strong>In Windows 2000, this bit can only be used on columns of type <strong>JET_coltypLong</strong>.</p> | 
| <p>JET_bitColumnUpdatable</p> | <p>This bit is valid only on calls to <a href="gg269215(v=exchg.10).md">JetGetColumnInfo</a>.</p> | 
| <p>JET_bitColumnTTKey</p> | <p>This bit is valid only on calls to <a href="gg294118(v=exchg.10).md">JetOpenTable</a>.</p> | 
| <p>JET_bitColumnTTDescending</p> | <p>This bit is valid only on calls to <a href="gg269211(v=exchg.10).md">JetOpenTempTable</a>.</p> | 
| <p>JET_bitColumnMultiValued</p> | <p>The column can be multi-valued. A multi-valued column can have zero, one, or more values associated with it. The various values in a multi-valued column are identified by a number called the <strong>itagSequence</strong> member, which belongs to various structures, including: <a href="gg294049(v=exchg.10).md">JET_RETINFO</a>, <a href="gg294090(v=exchg.10).md">JET_SETINFO</a>, <a href="gg269233(v=exchg.10).md">JET_SETCOLUMN</a>, <a href="gg269334(v=exchg.10).md">JET_RETRIEVECOLUMN</a>, and <a href="gg294052(v=exchg.10).md">JET_ENUMCOLUMNVALUE</a>. Multi-valued columns must be tagged columns; that is, they cannot be fixed-length or variable-length columns.</p> | 
| <p>JET_bitColumnEscrowUpdate</p> | <p>Specifies that a column is an escrow update column. An escrow update column can be updated concurrently by different sessions with <a href="gg294125(v=exchg.10).md">JetEscrowUpdate</a> and will maintain transactional consistency. An escrow update column must also meet the following conditions:</p><ul><li><p>An escrow update column can be created only when the table is empty.</p></li></ul><ul><li><p>An escrow update column must be of type <strong>JET_coltypLong</strong>.</p></li></ul><ul><li><p>An escrow update column must have a default value (that is <strong>cbDefault</strong> must be positive).</p></li></ul><ul><li><p>JET_bitColumnEscrowUpdate cannot be used in conjunction with JET_bitColumnTagged, JET_bitColumnVersion, or JET_bitColumnAutoincrement.</p></li></ul> | 
| <p>JET_bitColumnUnversioned</p> | <p>The column will be created in an without version information. This means that other transactions that attempt to add a column with the same name will fail. This bit is only useful with <a href="gg294122(v=exchg.10).md">JetAddColumn</a>. It cannot be used within a transaction.</p> | 
| <p>JET_bitColumnMaybeNull</p> | <p>Reserved for future use.</p> | 
| <p>JET_bitColumnFinalize</p> | <p>Use JET_bitColumnDeleteOnZero instead of JET_bitColumnFinalize. JET_bitColumnFinalize that a column can be finalized. When a column that can be finalized has an escrow update column that reaches zero, the row will be deleted. Future versions might invoke a callback function instead (For more information, see <a href="gg294098(v=exchg.10).md">JET_CALLBACK</a>). A column that can be finalized must be an escrow update column. JET_bitColumnFinalize cannot be used with JET_bitColumnUserDefinedDefault.</p> | 
| <p>JET_bitColumnUserDefinedDefault</p> | <p>The default value for a column will be provided by a callback function. See <a href="gg294098(v=exchg.10).md">JET_CALLBACK</a>. A column that has a user-defined default must be a tagged column. Specifying JET_bitColumnUserDefinedDefault means that <strong>pvDefault</strong> must point to a <a href="gg269200(v=exchg.10).md">JET_USERDEFINEDDEFAULT</a> structure, and <strong>cbDefault</strong> must be set to sizeof( <a href="gg269200(v=exchg.10).md">JET_USERDEFINEDDEFAULT</a> ).</p><ul><li><p>JET_bitColumnUserDefinedDefault cannot be used in conjunction with JET_bitColumnFixed, JET_bitColumnNotNULL, JET_bitColumnVersion, JET_bitColumnAutoincrement, JET_bitColumnUpdatable, JET_bitColumnEscrowUpdate, JET_bitColumnFinalize, JET_bitColumnDeleteOnZero, or JET_bitColumnMaybeNull.</p></li></ul> | 
| <p>JET_bitColumnDeleteOnZero</p> | <p>The column is an escrow update column, and when it reaches zero, the record will be deleted. A common use for a column that can be finalized is to use it as a reference count field, and when the field reaches zero the record gets deleted. JET_bitColumnDeleteOnZero is related to JET_bitColumnFinalize. A Delete-on-zero column must be an escrow update column. JET_bitColumnDeleteOnZero cannot be used with JET_bitColumnFinalize. JET_bitColumnDeleteOnZero cannot be used with user defined default columns.</p> | 



### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 



### See Also

[JET_CALLBACK](./jet-callback-callback-function.md)  
[JET_COLTYP](./jet-coltyp.md)  
[JET_COLUMNCREATE](./jet-columncreate-structure.md)  
[JET_COLUMNID](./jet-columnid.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_USERDEFINEDDEFAULT](./jet-userdefineddefault-structure.md)  
[JetAddColumn](./jetaddcolumn-function.md)  
[JetEscrowUpdate](./jetescrowupdate-function.md)  
[JetGetTableColumnInfo](./jetgettablecolumninfo-function.md)  
[JetOpenTempTable](./jetopentemptable-function.md)  
[JetOpenTempTable2](./jetopentemptable2-function.md)  
[JetOpenTempTable3](./jetopentemptable3-function.md)  
[JetRenameColumn](./jetrenamecolumn-function.md)
