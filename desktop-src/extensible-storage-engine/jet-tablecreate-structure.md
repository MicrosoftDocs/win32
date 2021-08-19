---
description: "Learn more about: JET_TABLECREATE Structure"
title: JET_TABLECREATE Structure
TOCTitle: JET_TABLECREATE Structure
ms:assetid: ff06325c-d61e-4239-b2d4-868f557f5f76
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294146(v=EXCHG.10)
ms:contentKeyID: 32765760
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

# JET_TABLECREATE Structure


_**Applies to:** Windows | Windows Server_

## JET_TABLECREATE Structure

The **JET_TABLECREATE** structure contains the information that is necessary to create a table populated with columns and indexes in an ESE database. The **JET_TABLECREATE** structure is used by [JetCreateTableColumnIndex](./jetcreatetablecolumnindex-function.md)

```cpp
    typedef struct tagJET_TABLECREATE {
      unsigned long cbStruct;
      tchar* szTableName;
      tchar* szTemplateTableName;
      unsigned long ulPages;
      unsigned long ulDensity;
      JET_COLUMNCREATE* rgcolumncreate;
      unsigned long cColumns;
      JET_INDEXCREATE* rgindexcreate;
      unsigned long cIndexes;
      JET_GRBIT grbit;
      JET_TABLEID tableid;
      unsigned long cCreated;
    } JET_TABLECREATE;
```

### Members

**cbStruct**

The size of this structure in bytes (for future expansion). It must be set to sizeof( JET_TABLECREATE ) in bytes.

**szTableName**

The name of the table to create.

The name must use meet the following conditions:

  - Have a value less than JET_cbNameMost, not including the terminating NULL.

<!-- end list -->

  - Consist of the following set of characters: 0 through 9, A through Z, a through z, and all other punctuation except for exclamation point (\!), comma (,), opening bracket (\[), and closing bracket (\]), that is, ASCII characters 0x20, 0x22 through 0x2d, 0x2f through 0x5a, 0x5c, and 0x5d through 0x7f.

<!-- end list -->

  - Not begin with a space.

<!-- end list -->

  - Consist of at least one non-space character.

**szTemplateTableName**

The name of an already-existing table from which to inherit base DDL (Data Definition Language). Use of a template table allows for the easy creation of many tables with identical columns and indexes.

**ulPages**

The initial number of database pages to allocate for the table. Specifying a number larger than one can reduce fragmentation if many rows are inserted into this table.

**ulDensity**

The table density, in percentage points. The number must be either 0 or in the range of 20 through 100. Passing 0 means that the default value should be used. The default is 80.

**rgcolumncreate**

An array of [JET_COLUMNCREATE](./jet-columncreate-structure.md) structures, each of which corresponds to a column to be created in the new table.

**cColumns**

The number of [JET_COLUMNCREATE](./jet-columncreate-structure.md) elements in **rgcolumncreate**.

**rgindexcreate**

An array of [JET_INDEXCREATE](./jet-indexcreate-structure.md) structures, each of which corresponds to an index to be created in the new table.

**cIndexes**

The number of [JET_INDEXCREATE](./jet-indexcreate-structure.md) elements in **rgindexcreate**.

**grbit**

A group of bits that contain the options for this call, which include zero or more of the following values.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitTableCreateFixedDDL</p> | <p>Setting JET_bitTableCreateFixedDDL prevents DDL operations on the table (such as adding or removing columns).</p> | 
| <p>JET_bitTableCreateTemplateTable</p> | <p>Setting JET_bitTableCreateTemplateTable causes the table to be a template table. New tables can then specify the name of this table as their template table. Setting JET_bitTableCreateTemplateTable implies JET_bitTableCreateFixedDDL.</p> | 
| <p>JET_bitTableCreateNoFixedVarColumnsInDerivedTables</p> | <p>Deprecated. Do not use.</p> | 



**tableid**

An output field that holds the [JET_TABLEID](./jet-tableid.md) of the new table if the API call succeeds. If the API call fails, the value is undefined.

**cCreated**

An output field that contains the count of objects created if the API call succeeds. If the API call fails, the value is undefined.

The count of objects that are created is equal to the sum of columns, tables, and indexes that are successfully created.

### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JET_TABLECREATE_W</strong> (Unicode) and <strong>JET_TABLECREATE_A</strong> (ANSI).</p> | 



### See Also

[JET_CALLBACK](./jet-callback-callback-function.md)  
[JET_CBTYP](./jet-cbtyp.md)  
[JET_CONDITIONALCOLUMN](./jet-conditionalcolumn-structure.md)  
[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_TABLEID](./jet-tableid.md)  
[JET_INDEXCREATE](./jet-indexcreate-structure.md)  
[JetCreateTable](./jetcreatetable-function.md)  
[JetCreateTableColumnIndex](./jetcreatetablecolumnindex-function.md)  
[JetCreateTableColumnIndex2](./jetcreatetablecolumnindex2-function.md)
