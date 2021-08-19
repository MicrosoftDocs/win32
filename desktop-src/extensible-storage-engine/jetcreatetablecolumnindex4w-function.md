---
description: "Learn more about: JetCreateTableColumnIndex4W Function"
title: JetCreateTableColumnIndex4W Function
TOCTitle: JetCreateTableColumnIndex4W Function
ms:assetid: 5a74b397-dfb4-4a1d-807b-284329239bc3
ms:mtpsurl: https://msdn.microsoft.com/library/JJ835042(v=EXCHG.10)
ms:contentKeyID: 49894664
ms.date: 04/11/2016
ms.topic: reference
dev_langs:
- c++
api_name: 
- JetCreateTableColumnIndex4W
topic_type: 
- apiref
- kbArticle
api_type: 
- DLLExport
api_location: 
- ESENT.DLL
ROBOTS: INDEX,FOLLOW

---

# JetCreateTableColumnIndex4W Function


_**Applies to:** Windows | Windows Server_

The **JetCreateTableColumnIndex4W** function creates a table in an Extensible Storage Engine (ESE( database with an initial set of indexes and an initial set of columns from an array of [JET_TABLECREATE3](./jet-tablecreate3-structure.md) structures. The [JET_TABLECREATE3](./jet-tablecreate3-structure.md) structure allows a callback function to be specified.

The **JetCreateTableColumnIndex4W** function was introduced in the Windows 8 operating system.

``` c++
JET_ERR JET_API JetCreateTableColumnIndex4W(
  __in          JET_SESID sesid,
  __in          JET_DBID dbid,
  __in_out      JET_TABLECREATE3* ptablecreate
);
```

### Parameters

*sesid*

The database session context to use for the API call.

*dbid*

The database identifier to use for the API call.

*ptablecreate*

A pointer to a [JET_TABLECREATE3](./jet-tablecreate3-structure.md) structure that defines the table to be created. See [JET_TABLECREATE3](./jet-tablecreate3-structure.md) for more details.

### Return value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the return codes listed in the following table. For more information about the possible Extensible Storage Enginge (ESE) errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errCallbackNotResolved</p> | <p>The callback function could not be resolved. The DLL might not have been found, or the function in the DLL might not have been found. With sufficient logging enabled, the event log will provide more details.</p> | 
| <p>JET_errCannotIndex</p> | <p>An attempt was made to index over an escrow-update or SLV column (note that SLV columns are deprecated).</p> | 
| <p>JET_errCannotNestDDL</p> | <p>Returned if the <em>ptablecreate-&gt;grbit</em> parameter specifies the JET_bitTableCreateTemplateTable value, but the <em>ptablecreate-&gt;szTemplateTableName</em> parameter is set to null.</p> | 
| <p>JET_errColumnDuplicate</p> | <p>A column already exists.</p> | 
| <p>JET_errColumnNotFound</p> | <p>An attempt was made to index over a nonexistent column. An attempt to conditionally index over a nonexistent column can also produce this error.</p> | 
| <p>JET_errColumnRedundant</p> | <p>An attempt was made to add a redundant column. No more than one autoincrement column should exist, and no more than one version column should exist per table.</p> | 
| <p>JET_errDensityInvalid</p> | <p>This error will be returned if the <strong>ulDensity</strong> member of the <a href="gg294082(v=exchg.10).md">JET_INDEXCREATE2</a> structure is set to a number less than 20 or more than 100.</p> | 
| <p>JET_errDDLNotInheritable</p> | <p>Signifies that the table named in the <strong>szTemplateTableName</strong> member of the <a href="gg269264(v=exchg.10).md">JET_TABLECREATE3</a> structure was not marked as a template table (that is, that table did not have the JET_bitTableCreateTemplateTable parameter value set).</p> | 
| <p>JET_errIndexDuplicate</p> | <p>An attempt to define two identical indexes was made.</p> | 
| <p>JET_errIndexHasPrimary</p> | <p>An attempt was made to specify more than one primary index for a table. A table must have exactly one primary index. If no primary index is specified, the database engine will transparently create one.</p> | 
| <p>JET_errIndexInvalidDef</p> | <p>An invalid index definition was specified. The following are some of the possible reasons for this error:</p><ul><li><p>A primary index is conditional (that is, the <strong>grbit</strong> member of the <a href="gg294082(v=exchg.10).md">JET_INDEXCREATE2</a> structure has the JET_bitIndexPrimary value set, and the <strong>cConditionalColumn</strong> member of the <a href="gg294082(v=exchg.10).md">JET_INDEXCREATE2</a> structure is greater than zero).</p></li><li><p>Applies to versions of the Windows Server operating system starting with Windows Server 2003. An attempt to create a tuple index with tuple limits, but without passing the <strong>ptuplelimits</strong> member in the <a href="gg294082(v=exchg.10).md">JET_INDEXCREATE2</a> structure (that is, the <strong>grbit</strong> member of the <strong>JET_INDEXCREATE2</strong> structure has JET_bitIndexTupleLimits value set, but the <strong>ptuplelimits</strong> pointer is null).</p></li><li><p>Passing in an invalid key definition in the <strong>szKey</strong> member of the <a href="gg294082(v=exchg.10).md">JET_INDEXCREATE2</a> structure. For information about valid definitions, see <a href="gg294082(v=exchg.10).md">JET_INDEXCREATE2</a>.</p></li><li><p>Setting the <strong>cbVarSegMac</strong> member in <a href="gg294082(v=exchg.10).md">JET_INDEXCREATE2</a> to be greater than the JET_cbPrimaryKeyMost value (for a primary index) or greater than the JET_cbSecondaryKeyMost value (for a secondary index).</p></li><li><p>Passing an invalid combination for a user-defined Unicode index (one that has the JET_bitIndexUnicode value bit set in the <strong>grbit</strong> member of the <a href="gg294082(v=exchg.10).md">JET_INDEXCREATE2</a> structure). Some common causes include the <strong>pidxunicode</strong> member of the <a href="gg294082(v=exchg.10).md">JET_INDEXCREATE2</a> structure is null, or the LCID specified in the <strong>pidxunicode</strong> structure is invalid.</p></li><li><p>Specifying a multivalued column for a primary index.</p></li><li><p>Trying to index too many conditional columns. The <strong>cConditionalColumn</strong> member of the <a href="gg294082(v=exchg.10).md">JET_INDEXCREATE2</a> structure must not be greater than <strong>JET_ccolKeyMost</strong>.</p></li></ul> | 
| <p>JET_errIndexTuplesInvalidLimits</p> | <p>Applies to versions of Windows starting with Windows XP. A <a href="gg269207(v=exchg.10).md">JET_TUPLELIMITS</a> structure was specified, and its limits are not supported. For more information, see the remarks section of the <a href="gg269207(v=exchg.10).md">JET_TUPLELIMITS</a> structure.</p> | 
| <p>JET_errIndexTuplesNonUniqueOnly</p> | <p>Applies to versions of Windows starting with Windows XP. A tuple index cannot be unique (that is, the <em>grbit</em> member of the <a href="gg294082(v=exchg.10).md">JET_INDEXCREATE2</a> structure must not have both JET_bitIndexPrimary and JET_bitIndexUnique values set).</p> | 
| <p>JET_errIndexTuplesOneColumnOnly</p> | <p>Applies to versions of Windows starting with Windows XP. A tuple index can only be over a single column (that is, if the <strong>grbit</strong> member of the <a href="gg294082(v=exchg.10).md">JET_INDEXCREATE2</a> structure has JET_bitIndexTuples value set, and the <strong>szKey</strong> member of the <a href="gg294082(v=exchg.10).md">JET_INDEXCREATE2</a> structure specifies more than one column).</p> | 
| <p>JET_errIndexTuplesSecondaryIndexOnly</p> | <p>Applies to versions of Windows starting with Windows XP. A tuple index cannot be a primary index (that is, the <strong>grbit</strong> member of the <a href="gg294082(v=exchg.10).md">JET_INDEXCREATE2</a> structure must not have both JET_bitIndexPrimary and JET_bitIndexTuples set).</p> | 
| <p>JET_errIndexTuplesTextColumnsOnly</p> | <p>Applies to versions of Windows starting with Windows XP. A tuple index can only be on a text or Unicode column. An attempt to index other columns (such as binary columns) will result in a JET_errIndexTuplesTextColumnsOnly response code.</p> | 
| <p>JET_errIndexTuplesVarSegMacNotAllowed</p> | <p>Applies to versions of Windows starting with Windows XP. A tuple index does not allow the <strong>cbVarSegMac</strong> member of the <a href="gg294082(v=exchg.10).md">JET_INDEXCREATE2</a> structure to be set.</p> | 
| <p>JET_errInTransaction</p> | <p>An attempt was made to create an index without version information while in a transaction.</p> | 
| <p>JET_errInvalidCodePage</p> | <p>The <strong>cp</strong> member of the <a href="gg269252(v=exchg.10).md">JET_COLUMNCREATE</a> structure was not set to a valid code page. The only valid values for text columns are English (1252) and Unicode (1200). A value of 0 means the default will be used (English, 1252).</p> | 
| <p>JET_errInvalidColumnType</p> | <p>The <strong>coltyp</strong> member of the <a href="gg269252(v=exchg.10).md">JET_COLUMNCREATE</a> structure was not set to a valid column type.</p> | 
| <p>JET_errInvalidCreateIndex</p> | <p>The following are some reasons why this error may occur:</p><ul><li><p>The <strong>rgindexcreate</strong> member of the <a href="gg269203(v=exchg.10).md">JET_TABLECREATE2</a> structure was set to null.</p></li><li><p>The <strong>rgcolumncreate</strong> member of the <a href="gg269203(v=exchg.10).md">JET_TABLECREATE2</a> structure was set to null.</p></li><li><p>The <strong>cbStruct</strong> member of a <a href="gg294082(v=exchg.10).md">JET_INDEXCREATE2</a> structure was not set to a valid value.</p></li></ul> | 
| <p>JET_errInvalidgrbit</p> | <p>An invalid combination of <strong>grbit</strong> members was specified in the <a href="gg269264(v=exchg.10).md">JET_TABLECREATE3</a> structure.</p><p>The index definition is invalid because the <strong>grbit</strong> member contains inconsistent values. The following are some possible reasons:</p><ul><li><p>A primary index had an ignore bit specified (that is, JET_bitIndexPrimary value was passed with the JET_bitIndexIgnoreNull, JET_bitIndexIgnoreAnyNull, or JET_bitIndexIgnoreFirstNull values).</p></li><li><p>An empty index does not ignore any null members (that is, the <strong>grbit</strong> member of the <a href="gg294082(v=exchg.10).md">JET_INDEXCREATE2</a> structure has the JET_bitIndexEmpty value set, but does not have JET_bitIndexIgnoreAnyNull value set).</p></li><li><p>Passing in a <a href="gg269214(v=exchg.10).md">JET_CONDITIONALCOLUMN</a> structure with an invalid <strong>grbit</strong> member.</p></li></ul> | 
| <p>JET_errInvalidLanguageId</p> | <p>An invalid Locale ID (LCID) was passed in (either through the <strong>lcid</strong> member of the <a href="gg294097(v=exchg.10).md">JET_UNICODEINDEX</a> structure that the <strong>pidxunicode</strong> member in the <a href="gg294082(v=exchg.10).md">JET_INDEXCREATE2</a> structure points to, or through the <strong>lcid</strong> field of the <a href="gg294082(v=exchg.10).md">JET_INDEXCREATE2</a> structure).</p> | 
| <p>JET_errInvalidParameter</p> | <p>An invalid parameter was given. The following are some possible reasons:</p><ul><li><p>The <strong>rgcolumncreate</strong> member of the <a href="gg269264(v=exchg.10).md">JET_TABLECREATE3</a> structure is null.</p></li><li><p>The <strong>cbStruct</strong> member of one of the <a href="gg269252(v=exchg.10).md">JET_COLUMNCREATE</a> structures given in the <strong>rgcolumncreate</strong> member of the <a href="gg269203(v=exchg.10).md">JET_TABLECREATE2</a> structure was not set to sizeof( JET_COLUMNCREATE ).</p></li><li><p>The <strong>cbKey</strong> member of a <a href="gg294082(v=exchg.10).md">JET_INDEXCREATE2</a> structure is set to zero.</p></li><li><p>The <strong>cbStruct</strong> member of a <a href="gg294082(v=exchg.10).md">JET_INDEXCREATE2</a> structure is not set to sizeof( JET_INDEXCREATE2 ).</p></li></ul> | 
| <p>JET_errRecordTooBig</p> | <p>The record is too big. The sum of the <strong>cbMax</strong> member of the <a href="gg269252(v=exchg.10).md">JET_COLUMNCREATE</a> structure for all fixed columns must not exceed a certain value.</p> | 
| <p>JET_errTableDuplicate</p> | <p>The table already exists.</p> | 
| <p>JET_errTooManyColumns</p> | <p>An attempt was made to add too many columns to the table. A table can have no more than <strong>JET_ccolFixedMost</strong> fixed columns, no more than <strong>JET_ccolVarMost</strong> variable-length columns, and no more than <strong>JET_ccolTaggedMost</strong> tagged columns.</p> | 
| <p>JET_errUnicodeTranslationFail</p> | <p>An error occurred when an attempt was made to normalize a Unicode column. This can be caused by running out of system resources.</p> | 
| <p>JET_errSpaceHintsInvalid</p> | <p>An element of the JET space hints structure was not correct or actionable.</p> | 



#### Remarks

The **JetCreateTableColumnIndex4W** function creates a table with an initial set of columns and indexes. Additional columns and indexes can be added and removed dynamically by means of the [JetAddColumn](./jetaddcolumn-function.md), [JetDeleteColumn](./jetdeletecolumn-function.md), [JetDeleteColumn2](./jetdeletecolumn2-function.md), [JetCreateIndex](./jetcreateindex-function.md), [JetCreateIndex2](./jetcreateindex2-function.md), [JetCreateIndex3](./jetcreateindex3-function.md), [JetCreateIndex4W](./jetcreateindex4w-function.md), and [JetDeleteIndex](./jetdeleteindex-function.md) functions.

As with the [JetOpenTable](./jetopentable-function.md) function, when the application is done using the returned *tableid*, the [JetCloseTable](./jetclosetable-function.md) function should close the application.

#### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows 8.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2012.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See also

[JET_CBTYP](./jet-cbtyp.md)  
[JET_DBID](./jet-dbid.md)  
[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_INDEXCREATE](./jet-indexcreate-structure.md)  
[JET_INDEXCREATE2](./jet-indexcreate2-structure.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JET_TABLECREATE2](./jet-tablecreate2-structure.md)  
[JET_TABLECREATE3](./jet-tablecreate3-structure.md)  
[JET_TUPLELIMITS](./jet-tuplelimits-structure.md)  
[JetAddColumn](./jetaddcolumn-function.md)  
[JetCreateIndex](./jetcreateindex-function.md)  
[JetCreateIndex2](./jetcreateindex2-function.md)  
[JetCreateIndex3](./jetcreateindex3-function.md)  
[JetCreateTable](./jetcreatetable-function.md)  
[JetCreateTableColumnIndex](./jetcreatetablecolumnindex-function.md)  
[JetDeleteColumn](./jetdeletecolumn-function.md)  
[JetDeleteColumn2](./jetdeletecolumn2-function.md)
