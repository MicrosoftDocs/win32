---
description: "Learn more about: JET_TABLECREATE2 Structure"
title: JET_TABLECREATE2 Structure
TOCTitle: JET_TABLECREATE2 Structure
ms:assetid: 2029e684-0d10-44e7-8033-d9cdbdffd7a4
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269203(v=EXCHG.10)
ms:contentKeyID: 32765506
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

# JET_TABLECREATE2 Structure


_**Applies to:** Windows | Windows Server_

## JET_TABLECREATE2 Structure

The **JET_TABLECREATE2** structure contains the information that is needed to create a table populated with columns and indexes in an ESE database, and that designates a callback function. The **JET_TABLECREATE2** structure is used by [JetCreateTableColumnIndex2](./jetcreatetablecolumnindex2-function.md).

**Windows XP:** The **JET_TABLECREATE2** structure is introduced in Windows XP.

```cpp
    typedef struct tagJET_TABLECREATE2 {
      unsigned long cbStruct;
      tchar* szTableName;
      tchar* szTemplateTableName;
      unsigned long ulPages;
      unsigned long ulDensity;
      JET_COLUMNCREATE* rgcolumncreate;
      unsigned long cColumns;
      JET_INDEXCREATE* rgindexcreate;
      unsigned long cIndexes;
      tchar* szCallback;
      JET_CBTYP cbtyp;
      JET_GRBIT grbit;
      JET_TABLEID tableid;
      unsigned long cCreated;
    } JET_TABLECREATE2;
```

### Members

**cbStruct**

The size of this structure in bytes (for future expansion). It must be set to sizeof( JET_TABLECREATE2 ) in bytes.

**szTableName**

The name of table to create.

The name must use meet the following conditions:

  - Have a value less than JET_cbNameMost, not including the terminating NULL.

<!-- end list -->

  - Consist of the following set of characters: 0 through 9, A through Z, a through z, and all other punctuation except for exclamation point (\!), comma (,), opening bracket (\[), and closing bracket (\]), that is, ASCII characters 0x20, 0x22 through 0x2d, 0x2f through 0x5a, 0x5c, and 0x5d through 0x7f.

<!-- end list -->

  - Not begin with a space.

<!-- end list -->

  - Consist of at least one non-space character.

**szTemplateTableName**

The name of an already-existing table from which to inherit base DDL (Data Definition Language). Using a template table allows easy creation of many tables with identical columns and indexes.

**ulPages**

The initial number of database pages to allocate for the table. Specifying a number larger than one can reduce fragmentation if many rows are inserted into this table.

**ulDensity**

The table density, in percentage points. The number must be either 0 or in the range of 20 through 100. Passing 0 means that the default value should be used. The default is 80.

**rgcolumncreate**

An array of [JET_COLUMNCREATE](./jet-columncreate-structure.md) structures, each of which corresponds to a column to be created in the new table.

**cColumns**

the number of [JET_COLUMNCREATE](./jet-columncreate-structure.md) elements in **rgcolumncreate**.

**rgindexcreate**

An array of [JET_INDEXCREATE](./jet-indexcreate-structure.md) structures, each of which corresponds to an index to be created in the new table.

**cIndexes**

The number of [JET_INDEXCREATE](./jet-indexcreate-structure.md) elements in **rgindexcreate**.

**szCallback**

The function that gets called during certain events. **cbtyp** determines when the callback function will be called.

The format of **szCallback** must be "module\!function"—for example, "alpha\!beta" refers to the beta function in the module named "alpha". The prototype of the function must match [JET_CALLBACK](./jet-callback-callback-function.md). For more information, see [JET_CALLBACK](./jet-callback-callback-function.md).

**cbtyp**

Describes the type of callback function designated by **szCallback**. For more information, see [JET_CBTYP](./jet-cbtyp.md). This bitfield is composed of one or more of the following bits.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_cbtypFinalize</p> | <p>The callback function will be called when a column that can be finalized has gone to zero.</p> | 
| <p>JET_cbtypBeforeInsert</p> | <p>The callback function will be called prior to record insertion.</p> | 
| <p>JET_cbtypAfterInsert</p> | <p>The callback function will be called once the database engine has finished inserting a record.</p> | 
| <p>JET_cbtypBeforeReplace</p> | <p>The callback function will be called prior to modification of a record.</p> | 
| <p>JET_cbtypAfterReplace</p> | <p>The callback function will be called after finishing modification of a record.</p> | 
| <p>JET_cbtypBeforeDelete</p> | <p>The callback function will be called prior to deletion of a record.</p> | 
| <p>JET_cbtypAfterDelete</p> | <p>The callback function will be called after a record has been deleted.</p> | 
| <p>JET_cbtypUserDefinedDefaultValue</p> | <p>The callback function will be called to calculate a user-defined default.</p> | 
| <p>JET_cbtypOnlineDefragCompleted</p> | <p>The callback function will be called after a call to <a href="gg294095(v=exchg.10).md">JetDefragment2</a> has completed.</p> | 
| <p>JET_cbtypFreeCursorLS</p> | <p>The callback function will be called when the local storage that is associated with a cursor must be freed.</p> | 
| <p>JET_cbtypFreeTableLS</p> | <p>The callback function will be called when the local storage that is associated with a table must be freed.</p> | 



**grbit**

A group of bits that contain the options for this call, which include zero or more of the following values.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitTableCreateFixedDDL</p> | <p>Setting JET_bitTableCreateFixedDDL prevents DDL operations on the table (such as adding or removing columns).</p> | 
| <p>JET_bitTableCreateTemplateTable</p> | <p>Setting JET_bitTableCreateTemplateTable causes the table to be a template table. New tables can then specify the name of this table as their template table. Setting JET_bitTableCreateTemplateTable implies JET_bitTableCreateFixedDDL.</p> | 
| <p>JET_bitTableCreateNoFixedVarColumnsInDerivedTables</p> | <p>Must be used in conjunction with JET_bitTableCreateTemplateTable. Deprecated. Do not use.</p> | 



**tableid**

An output field that holds the [JET_TABLEID](./jet-tableid.md) of the new table if the API call succeeds. If the API call fails, the value is undefined.

**cCreated**

An output field that contains the count of objects that are created if the API call succeeds. If the API call fails, the value is undefined.

The count of objects that is created is equal to the sum of columns, tables, and indexes that are successfully created.

### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows  Vista or Windows XP.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008 or Windows Server 2003.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JET_TABLECREATE2_W</strong> (Unicode) and <strong>JET_TABLECREATE2_A</strong> (ANSI).</p> | 



### See Also

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
