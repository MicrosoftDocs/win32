---
description: "Learn more about: JET_COLUMNCREATE Structure"
title: JET_COLUMNCREATE Structure
TOCTitle: JET_COLUMNCREATE Structure
ms:assetid: 553263a9-7d2c-4bd7-ad77-1dfb6d21ef2c
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269252(v=EXCHG.10)
ms:contentKeyID: 32765554
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

# JET_COLUMNCREATE Structure


_**Applies to:** Windows | Windows Server_

## JET_COLUMNCREATE Structure

The **JET_COLUMNCREATE** structure describes a column to create in a database.

```cpp
    typedef struct tag_JET_COLUMNCREATE {
      unsigned long cbStruct;
      tchar* szColumnName;
      JET_COLTYP coltyp;
      unsigned long cbMax;
      JET_GRBIT grbit;
      void* pvDefault;
      unsigned long cbDefault;
      unsigned long cp;
      JET_COLUMNID columnid;
      JET_ERR err;
    } JET_COLUMNCREATE;
```

### Members

**cbStruct**

The size of the structure, in bytes. This field must be initialized to **sizeof( JET_COLUMNCREATE )**.

**szColumnName**

The name of the column to create. The name must meet the following criteria:

  - It must be fewer than JET_cbNameMost characters in length, not including the terminating NULL.

<!-- end list -->

  - It must contain characters only from the following sets: 0 through 9, A through Z, a through z, and all other punctuation except for exclamation point (\!), comma (,), opening bracket (\[), and closing bracket (\]), that is, ASCII characters 0x20, 0x22 through 0x2d, 0x2f through 0x5a, 0x5c, 0x5d through 0x7f.

<!-- end list -->

  - It cannot begin with a space.

<!-- end list -->

  - It must contain at least one non-space character.

**coltyp**

The type of the column (for example, text, binary, or numerical). For more information, see [JET_COLTYP](./jet-coltyp.md).

**cbMax**

The maximum length, in bytes, of a variable-length column. The length of the column for fixed-length columns.

**grbit**

A group of bits that contain the options for this structure, and which include zero or more of the following values.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitColumnFixed</p> | <p>The column is fixed. It will always use the same amount of space in a row, regardless of how much data is being stored in the column. JET_bitColumnFixed cannot be used with JET_bitColumnTagged. This bit cannot be used with long values such as <strong>JET_coltypLongText</strong> and <strong>JET_coltypLongBinary</strong>.</p> | 
| <p>JET_bitColumnTagged</p> | <p>The column is tagged. Tagged columns do not take up any space in the database if they do not contain data. This bit cannot be used with JET_bitColumnFixed.</p> | 
| <p>JET_bitColumnNotNULL</p> | <p>The column must never be set to a NULL value.</p> | 
| <p>JET_bitColumnAutoincrement</p> | <p>The column is automatically incremented. The number is an increasing number, and is guaranteed to be unique within a table. The number, however, might not be continuous. For example, if five rows are inserted into a table, the autoincrement column could contain the values { 1, 2, 6, 7, 8 }.</p><p><strong>Windows 2000:  </strong>This bit can be used only on columns of type <strong>JET_coltypLong</strong>.</p><p><strong>Windows Server 2003 and later:  </strong>This bit can only be used on columns of type <strong>JET_coltypLong</strong> or <strong>JET_coltypCurrency</strong>.</p> | 
| <p>JET_bitColumnUpdatable</p> | <p>This bit is valid only on calls to <a href="gg269215(v=exchg.10).md">JetGetColumnInfo</a>.</p> | 
| <p>JET_bitColumnTTKey</p> | <p>This bit is valid only on calls to <a href="gg269211(v=exchg.10).md">JetOpenTempTable</a>.</p> | 
| <p>JET_bitColumnTTDescending</p> | <p>This bit is valid only on calls to <a href="gg269211(v=exchg.10).md">JetOpenTempTable</a>.</p> | 
| <p>JET_bitColumnMultiValued</p> | <p>The column can be multi-valued. A multi-valued column can have zero, one, or more values associated with it. The various values in a multi-valued column are identified by the <strong>itagSequence</strong> member of various structures, for example, <a href="gg294049(v=exchg.10).md">JET_RETINFO</a>, <a href="gg294090(v=exchg.10).md">JET_SETINFO</a>, <a href="gg269233(v=exchg.10).md">JET_SETCOLUMN</a>, <a href="gg269334(v=exchg.10).md">JET_RETRIEVECOLUMN</a>, <a href="gg294052(v=exchg.10).md">JET_ENUMCOLUMNVALUE</a>. Multi-valued columns must be tagged columns; that is, they cannot be fixed-length or variable-length columns.</p> | 
| <p>JET_bitColumnEscrowUpdate</p> | <p>The column is an escrow update column. An escrow update column can be updated concurrently by different sessions with <a href="gg294125(v=exchg.10).md">JetEscrowUpdate</a> and maintain transactional consistency.</p><ul><li><p>An escrow update column can be created only when the table is empty.</p></li><li><p>An escrow update column must be of type <strong>JET_coltypLong.</strong></p></li><li><p>An escrow update column must have a default value (that is <strong>cbDefault</strong> must be positive).</p></li><li><p>JET_bitColumnEscrowUpdate cannot be used in conjunction with the following constants:</p><ul><li><p>JET_bitColumnTagged</p></li><li><p>JET_bitColumnVersion</p></li><li><p>JET_bitColumnAutoincrement</p></li></ul></li></ul> | 
| <p>JET_bitColumnUnversioned</p> | <p>The column is created without a version. Other transactions attempting to add a column with the same name will fail. This bit is only useful with <a href="gg294122(v=exchg.10).md">JetAddColumn</a>. It cannot be used within a transaction.</p> | 
| <p>JET_bitColumnMaybeNull</p> | <p>Reserved for future use.</p> | 
| <p>JET_bitColumnFinalize</p> | <p>Use JET_bitColumnDeleteOnZero instead of JET_bitColumnFinalize. JET_bitColumnFinalize specifies that a column can be finalized. When a column that can be finalized has an escrow update column that reaches zero, the row will be deleted. Future versions can invoke a callback function instead. For more information, see <a href="gg294098(v=exchg.10).md">JET_CALLBACK</a>. A column that can be finalized must be an escrow update column. JET_bitColumnFinalize cannot be used with JET_bitColumnUserDefinedDefault.</p> | 
| <p>JET_bitColumnUserDefinedDefault</p> | <p>The default value for a column is provided by the callback function, <a href="gg294098(v=exchg.10).md">JET_CALLBACK</a>. A column that has a user-defined default must be a tagged column. <strong>pvDefault</strong> must point to a <a href="gg269200(v=exchg.10).md">JET_USERDEFINEDDEFAULT</a> structure, and <strong>cbDefault</strong> must be set to sizeof(<a href="gg269200(v=exchg.10).md">JET_USERDEFINEDDEFAULT</a>).</p><p>JET_bitColumnUserDefinedDefault cannot be used in conjunction with the following constants:</p><ul><li><p>JET_bitColumnFixed</p></li><li><p>JET_bitColumnNotNULL</p></li><li><p>JET_bitColumnVersion</p></li><li><p>JET_bitColumnAutoincrement</p></li><li><p>JET_bitColumnUpdatable</p></li><li><p>JET_bitColumnEscrowUpdate</p></li><li><p>JET_bitColumnFinalize</p></li><li><p>JET_bitColumnDeleteOnZero</p></li><li><p>JET_bitColumnMaybeNull</p></li></ul> | 
| <p>JET_bitColumnDeleteOnZero</p> | <p>The column is an escrow update column, and when it reaches zero, the record will be deleted. A common use for a column that can be finalized is to use it as a reference count field, and when the field reaches zero the record gets deleted. JET_bitColumnDeleteOnZero is related to JET_bitColumnFinalize. A delete-on-zero column must be an escrow update column. JET_bitColumnDeleteOnZero cannot be used with JET_bitColumnFinalize. JET_bitColumnDeleteOnZero cannot be used with user defined default columns.</p> | 



**pvDefault**

Points to a buffer which will be the default value for a column. The length of the buffer is **cbDefault**. If there is no default, **pvDefault** should be set to NULL and **cbDefault** should be set to zero. If *grbit* has JET_bitColumnUserDefinedDefault set, **pvDefault** will be interpreted as a pointer to a JET_USERDEFINEDDEFAULT structure. Default values cannot be larger than 255 bytes. If a default value is larger than 255 bytes, it will be silently truncated.

**cbDefault**

The size, in bytes, of the buffer specified by **pvDefault**.

**cp**

The code page for the column. The only valid values for text columns are English (1252) and Unicode (1200). A value of zero means the default will be used (English, 1252). If the column is not a text column, the code page automatically gets set to zero.

**columnid**

On success, the column identifier of the newly-created column will be passed back in this field. On failure, the value is undefined.

**err**

The **err** field will contain the status of creating this column. See [JetAddColumn](./jetaddcolumn-function.md) for a list of likely return values.

### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JET_COLUMNCREATE_W</strong> (Unicode) and <strong>JET_COLUMNCREATE_A</strong> (ANSI).</p> | 



### See Also

[JET_COLTYP](./jet-coltyp.md)  
[JET_COLUMNID](./jet-columnid.md)  
[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_RETINFO](./jet-retinfo-structure.md)  
[JET_SETINFO](./jet-setinfo-structure.md)  
[JET_SETCOLUMN](./jet-setcolumn-structure.md)  
[JET_RETRIEVECOLUMN](./jet-retrievecolumn-structure.md)  
[JET_ENUMCOLUMNVALUE](./jet-enumcolumnvalue-structure.md)  
[JetAddColumn](./jetaddcolumn-function.md)  
[JetCreateTableColumnIndex](./jetcreatetablecolumnindex-function.md)  
[JetCreateTableColumnIndex2](./jetcreatetablecolumnindex2-function.md)  
[JetEscrowUpdate](./jetescrowupdate-function.md)  
[JetRenameColumn](./jetrenamecolumn-function.md)  
[JetSetColumns](./jetsetcolumns-function.md)
