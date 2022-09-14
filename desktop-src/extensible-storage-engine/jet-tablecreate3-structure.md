---
description: "Learn more about: JET_TABLECREATE3 Structure"
title: JET_TABLECREATE3 Structure
TOCTitle: JET_TABLECREATE3 Structure
ms:assetid: 61909569-e704-494b-a56d-b64d1a2ee157
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269264(v=EXCHG.10)
ms:contentKeyID: 32765566
ms.date: 04/11/2016
ms.topic: reference
dev_langs:
- c++
api_name: 
topic_type: 
- apiref
- kbArticle
api_type: 
- COM
api_location: 
ROBOTS: INDEX,FOLLOW

---

# JET_TABLECREATE3 Structure


_**Applies to:** Windows | Windows Server_

The **JET_TABLECREATE3** structure contains the information that is needed to create a table populated with columns and indexes in an Extensible Storage Engine (ESE) database, and that designates a callback function. The **JET_TABLECREATE3** structure is used by the [JetCreateTableColumnIndex3](./jetcreatetablecolumnindex3-function.md) function.

The **JET_TABLECREATE3** structure was introduced in the Windows 7 operating system.

``` cpp
typedef struct tagJET_TABLECREATE3 {
  unsigned long cbStruct;
  tchar* szTableName;
  tchar* szTemplateTableName;
  unsigned long ulPages;
  unsigned long ulDensity;
  JET_COLUMNCREATE* rgcolumncreate;
  unsigned long cColumns;
    JET_INDEXCREATE2* rgindexcreate;
  unsigned long cIndexes;
  tchar* szCallback;
  JET_CBTYP cbtyp;
  JET_GRBIT grbit;
  JET_TABLEID tableid;
  un  JET_GRBIT grbit;
  JET_SPACEHINTS* pSeqSpacehints;
  JET_SPACEHINTS* pLVSpacehints;
  unsigned long cbSeparateLV;
  JET_TABLEID tableid;
  unsigned long cCreated;
} JET_TABLECREATE3;>
```

### Members

**cbStruct**

The size of this structure in bytes (for future expansion). It must be set to sizeof( JET_TABLECREATE3 ) in bytes.

**szTableName**

The name of the table to create.

The name must meet the following conditions:

  - It must have a value that is less than JET_cbNameMost, not including the terminating null.

  - It must consist of the following set of characters: 0 through 9, A through Z, a through z, and all other punctuation except for exclamation point (\!), comma (,), opening bracket (\[), and closing bracket (\]); that is, ASCII characters 0x20, 0x22 through 0x2d, 0x2f through 0x5a, 0x5c, and 0x5d through 0x7f.

  - It must not begin with a space.

  - It must consist of at least one non-space character.

**szTemplateTableName**

The name of an existing table from which to inherit the base data definition language (DDL). Use of a template table allows for the easy creation of many tables with identical columns and indexes.

**ulPages**

The initial number of database pages to allocate for the table. Specifying a number larger than one can reduce fragmentation if many rows are inserted into this table.

**ulDensity**

The table density, in percentage points. The number must be either 0 or in the range of 20 through 100. Passing 0 means that the default value should be used. The default value is 80.

**rgcolumncreate**

An array of [JET_COLUMNCREATE](./jet-columncreate-structure.md) structures, each of which corresponds to a column to be created in the new table.

**cColumns**

The number of [JET_COLUMNCREATE](./jet-columncreate-structure.md) elements in the *rgcolumncreate* parameter.

**rgindexcreate**

An array of [JET_INDEXCREATE2](./jet-indexcreate2-structure.md) structures, each of which corresponds to an index to be created in the new table.

**cIndexes**

The number of [JET_INDEXCREATE2](./jet-indexcreate2-structure.md) elements in the *rgindexcreate* parameter.

**szCallback**

The function that gets called during certain events. **cbtyp** determines when the callback function will be called.

The format of **szCallback** must be "module\!function" — for example, "alpha\!beta" refers to the beta function in the module named "alpha".

The prototype of the function must match the [JET_CALLBACK](./jet-callback-callback-function.md) callback function.

**cbtyp**

Describes the type of callback function designated by **szCallback**. For more information, see [JET_CBTYP](./jet-cbtyp.md).

This bitfield is composed of one or more of the bit values listed in the following table.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_cbtypFinalize</p> | <p>The callback function will be called when a column that can be finalized has gone to zero.</p> | 
| <p>JET_cbtypBeforeInsert</p> | <p>The callback function will be called prior to record insertion.</p> | 
| <p>JET_cbtypAfterInsert</p> | <p>The callback function will be called after the database engine has finished inserting a record.</p> | 
| <p>JET_cbtypBeforeReplace</p> | <p>The callback function will be called prior to the modification of a record.</p> | 
| <p>JET_cbtypAfterReplace</p> | <p>The callback function will be called after finishing the modification of a record.</p> | 
| <p>JET_cbtypBeforeDelete</p> | <p>The callback function will be called prior to the deletion of a record.</p> | 
| <p>JET_cbtypAfterDelete</p> | <p>The callback function will be called after a record has been deleted.</p> | 
| <p>JET_cbtypUserDefinedDefaultValue</p> | <p>The callback function will be called to calculate a user-defined default.</p> | 
| <p>JET_cbtypFreeCursorLS</p> | <p>The callback function will be called when the local storage that is associated with a cursor must be freed.</p> | 
| <p>JET_cbtypFreeTableLS</p> | <p>The callback function will be called when the local storage that is associated with a table must be freed.</p> | 



**grbit**

A group of bits that contains zero or more of the call option values listed in the following table.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitTableCreateFixedDDL</p> | <p>Prevents DDL operations on the table (such as adding or removing columns).</p> | 
| <p>JET_bitTableCreateTemplateTable</p> | <p>Causes the table to be a template table. New tables can then specify the name of this table as their template table. Setting JET_bitTableCreateTemplateTable implies JET_bitTableCreateFixedDDL.</p> | 
| <p>JET_bitTableCreateNoFixedVarColumnsInDerivedTables</p> | <p>Must be used in conjunction with JET_bitTableCreateTemplateTable. Deprecated. Do not use.</p> | 



**pSeqSpacehints**

A pointer to a [JET_SPACEHINTS](./jet-spacehints-structure.md) structure for default sequential index.

**pSeqSpacehints** was introduced in Windows 7.

**pLVSpacehints**

A pointer to a [JET_SPACEHINTS](./jet-spacehints-structure.md) structure for a Separated Long Value tree.

**pLVSpacehints** was introduced in Windows 7.

**cbSeparateLV**

The size to separate an intrinsic LV from the primary record. Any long-value c structure for a Separated LV tree. For more information, see ng-value in [JET_SPACEHINTS](./jet-spacehints-structure.md). Long-value columns smaller than this value may be separated if the record becomes too large.

**cbSeparateLV** was introduced in Windows 7.

**tableid**

An output field that holds the [JET_TABLEID](./jet-tableid.md) of the new table if the API call succeeds. If the API call fails, the value is undefined. This table is opened exclusively.

**cCreated**

An output field that contains the count of objects that are created if the API call succeeds. If the API call fails, the value is undefined.

The count of objects that are created is equal to the sum of columns, tables, and indexes that are successfully created.

### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista or Windows XP.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008 or Windows Server 2003.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JET_TABLECREATE3_W</strong> (Unicode) and <strong>JET_TABLECREATE3_A</strong> (ANSI).</p> | 



### See also

[JET_CALLBACK](./jet-callback-callback-function.md)  
[JET_CBTYP](./jet-cbtyp.md)  
[JET_CONDITIONALCOLUMN](./jet-conditionalcolumn-structure.md)  
[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_INDEXCREATE](./jet-indexcreate-structure.md)  
[JET_TABLEID](./jet-tableid.md)  
[JetCreateTable](./jetcreatetable-function.md)  
[JetCreateTableColumnIndex](./jetcreatetablecolumnindex-function.md)  
[JetCreateTableColumnIndex2](./jetcreatetablecolumnindex2-function.md)  
[JetDefragment2](./jetdefragment2-function.md)
