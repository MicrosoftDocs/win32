---
description: "Learn more about: JetAddColumn Function"
title: JetAddColumn Function
TOCTitle: JetAddColumn Function
ms:assetid: e146f784-2cbd-42c0-bf64-b37dc6f9ee43
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294122(v=EXCHG.10)
ms:contentKeyID: 32765736
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetAddColumnW
- JetAddColumnA
- JetAddColumn
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

# JetAddColumn Function


_**Applies to:** Windows | Windows Server_

## JetAddColumn Function

The **JetAddColumn** function adds a new column to an existing table in an ESE database.

```cpp
    JET_ERR JET_API JetAddColumn(
      __in          JET_SESID sesid,
      __in          JET_TABLEID tableid,
      __in          JET_PCSTR szColumnName,
      __in          const JET_COLUMNDEF* pcolumndef,
      __in_opt      const void* pvDefault,
      __in          unsigned long cbDefault,
      __out_opt     JET_COLUMNID* pcolumnid
    );
```

### Parameters

*sesid*

The database session context to use for the API call.

*tableid*

The table to which to add the column.

*szColumnName*

The name of the column to add. The name must meet the following criteria:

  - It must be fewer than JET_cbNameMost characters in length, not including the terminating **NULL**.

  - It must contain characters only from the following sets: 0 through 9, A through Z, a through z, and all other punctuation except for exclamation point (\!), comma (,), opening bracket (\[), and closing bracket (\]) — that is, ASCII characters 0x20, 0x22 through 0x2d, 0x2f through 0x5a, 0x5c, and 0x5d through 0x7f.

  - It cannot begin with a space.

  - It must contain at least one non-space character.

*pcolumndef*

A pointer to a [JET_COLUMNDEF](./jet-columndef-structure.md) structure, which defines the data that can be stored in a column.

*pvDefault*

A pointer to a buffer that contains the default value for the column. The length of the buffer is **cbDefault**. If there is no default, set **pvDefault** to **NULL** and **cbDefault** to zero. Default values cannot be larger than JET_cbColumnMost bytes for fixed columns or JET_cbLVDefaultValueMost bytes for long values. If a default value is larger than that, it will be silently truncated.

If *grbit* has JET_bitColumnUserDefinedDefault set, **pvDefault** will be interpreted as a pointer to a [JET_USERDEFINEDDEFAULT](./jet-userdefineddefault-structure.md) structure.

*cbDefault*

The size, in bytes, of the buffer that is specified in **pvDefault**.

*pcolumnid*

A pointer to a [JET_COLUMNID](./jet-columnid.md) structure, which, on success, will receive the identifier of the newly created column. On failure, the value is undefined.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation was successful.</p> | 
| <p>JET_errFixedDDL</p> | <p>An attempt was made to modify the data definition of a fixed DDL table. An example of a table with fixed DDL is a Template Table.</p> | 
| <p>JET_errInvalidParameter</p> | <p>An invalid parameter was passed into the API. Some examples of invalid parameters are:</p><ul><li><p>Passing in the wrong size of the <a href="gg294130(v=exchg.10).md">JET_COLUMNDEF</a> structure in its <em>cbStruct</em> member.</p></li><li><p>Passing in JET_bitColumnUserDefinedDefault, but not setting <strong>cbDefault</strong> to sizeof(<a href="gg269200(v=exchg.10).md">JET_USERDEFINEDDEFAULT</a>).</p></li></ul> | 
| <p>JET_errInTransaction</p> | <p>An attempt was made to add a column with the JET_bitColumnUnversioned bit set, but the session is currently in a transaction.</p> | 
| <p>JET_errColumnDuplicate</p> | <p>A column already exists. An attempt was made to add a column without version information, and that column already exists.</p> | 
| <p>JET_errTableNotEmpty</p> | <p>The table contains data. An Escrow Update column can only be added to an empty table.</p> | 
| <p>JET_errRecordTooBig</p> | <p>The record is too big. The sum of the <strong>cbMax</strong> parameter for the fixed columns must not exceed a certain value.</p> | 
| <p>JET_errTooManyColumns</p> | <p>An attempt was made to add too many columns to the table. A table can have no more than JET_ccolFixedMost fixed columns, no more than JET_ccolVarMost variable-length columns, and no more than JET_ccolTaggedMost tagged columns.</p> | 
| <p>JET_errColumnRedundant</p> | <p>An attempt was made to add a redundant column. There should be no more than one autoincrement column, and no more than one version column per table.</p> | 
| <p>JET_errCallbackNotResolved</p> | <p>The callback function could not be resolved. The DLL might not have been found, or the function in the DLL might not have been found. The event log will provide more details if sufficient logging is enabled.</p> | 
| <p>JET_wrnColumnMaxTruncated</p> | <p>A warning indicating that the maximum length (<strong>cbMax</strong>) of a fixed or variable column was greater than JET_cbColumnMost. This limit does not apply to Long Values (that is <a href="gg269213(v=exchg.10).md">JET_coltypLongBinary</a> and <a href="gg269213(v=exchg.10).md">JET_coltypLongText</a>).</p> | 
| <p>JET_errInvalidName</p> | <p>An invalid name was passed as <strong>szColumnName</strong>. For more information about the restrictions, see the criteria for <strong>szColumnName</strong>.</p> | 
| <p>JET_errInvalidColumnType</p> | <p>The <strong>coltyp</strong> field was not set to a valid column type.</p> | 
| <p>JET_errInvalidCodePage</p> | <p>The <strong>cp</strong> parameter of the <a href="gg294130(v=exchg.10).md">JET_COLUMNDEF</a> structure was not set to a valid code page. The only valid values for text columns are English (1252) and Unicode (1200). A value of 0 means the default will be used (English, 1252).</p> | 
| <p>JET_errTaggedNotNULL</p> | <p>JET_bitColumnNotNULL cannot be used with tagged, Long Value, or SLV columns.</p> | 
| <p>JET_errInvalidgrbit</p> | <p>An invalid combination of <em>grbits</em> was specified. Some of the reasons for this error are:</p><ul><li><p>JET_bitColumnFixed was used on a tagged, Long Value, or SLV column.</p></li><li><p>JET_bitColumnEscrowUpdate was used on a column that was not of type <a href="gg269213(v=exchg.10).md">JET_coltypLong</a>.</p></li><li><p>JET_bitColumnEscrowUpdate was used on a Version column (JET_bitColumnVersion).</p></li><li><p>JET_bitColumnEscrowUpdate was used on an AutoIncrememnt column (JET_bitColumnAutoincrement).</p></li><li><p>JET_bitColumnEscrowUpdate was used on a column that did not have a default value (<strong>cbDefault</strong> was equal to zero).</p></li><li><p>JET_bitColumnFinalize was used on a column that was not an Escrow Update column (JET_bitColumnEscrowUpdate was not set).</p></li><li><p>JET_bitColumnDeleteOnZero was used on a column that was not an Escrow Update column (JET_bitColumnEscrowUpdate was not set).</p></li><li><p>JET_bitColumnAutoincrement was used on a column that was not <a href="gg269213(v=exchg.10).md">JET_coltypLong</a>.</p><p><strong>Windows 2000:  </strong>This reason for the error code is used only in Windows 2000.</p><p>JET_bitColumnAutoincrement was used on a column that was neither <a href="gg269213(v=exchg.10).md">JET_coltypLong</a> nor <a href="gg269213(v=exchg.10).md">JET_coltypCurrency</a>.</p><p><strong>Windows XP:  </strong>This reason for the error code is used in Windows XP and later operating systems.</p></li><li><p>JET_bitColumnVersion was used on a column that was not <a href="gg269213(v=exchg.10).md">JET_coltypLong</a>.</p></li><li><p>JET_bitColumnVersion was used on an autoincrement column.</p></li><li><p>JET_bitColumnUserDefinedDefault was used in conjunction with JET_bitColumnFixed.</p></li><li><p>JET_bitColumnUserDefinedDefault was used in conjunction with JET_bitColumnNotNULL.</p></li><li><p>JET_bitColumnUserDefinedDefault was used in conjunction with JET_bitColumnVersion.</p></li><li><p>JET_bitColumnUserDefinedDefault was used in conjunction with JET_bitColumnAutoincrement.</p></li><li><p>JET_bitColumnUserDefinedDefault was used in conjunction with JET_bitColumnUpdatable.</p></li><li><p>JET_bitColumnUserDefinedDefault was used in conjunction with JET_bitColumnEscrowUpdate.</p></li><li><p>JET_bitColumnUserDefinedDefault was used in conjunction with JET_bitColumnFinalize.</p></li><li><p>JET_bitColumnUserDefinedDefault was used in conjunction with JET_bitColumnDeleteOnZero.</p></li><li><p>JET_bitColumnUserDefinedDefault was used in conjunction with JET_bitColumnMaybeNull.</p></li><li><p>JET_bitColumnUserDefinedDefault was used on a non-tagged column (that is fixed or variable).</p></li></ul> | 
| <p>JET_errMultiValuedColumnMustBeTagged</p> | <p>A multi-valued column (JET_bitColumnMultiValued) can only be used on a tagged or Long Value (<a href="gg269213(v=exchg.10).md">JET_coltypLongBinary</a> or <a href="gg269213(v=exchg.10).md">JET_coltypLongText</a>) column.</p> | 
| <p>JET_errCannotBeTagged</p> | <p>An attempt was made to use a tagged column when the column might not be tagged. Some of the constraints for disallowing tagged columns are:</p><ul><li><p>An Escrow Update column (JET_bitColumnEscrowUpdate) cannot be used on a tagged or Long Value (<a href="gg269213(v=exchg.10).md">JET_coltypLongBinary</a> or <a href="gg269213(v=exchg.10).md">JET_coltypLongText</a>) column.</p></li><li><p>An autoincrement column might not be tagged.</p></li><li><p>A Version column might not be tagged.</p></li></ul> | 
| <p>JET_errExclusiveTableLockRequired</p> | <p>An exclusive lock on the table was required for this operation.</p> | 
| <p>JET_wrnColumnMaxTruncated</p> | <p>A warning indicating that the maximum length (<em>cbMax</em>) of a fixed or variable column was greater than JET_cbColumnMost. This limit does not apply to Long Values (that is <a href="gg269213(v=exchg.10).md">JET_coltypLongBinary</a> and <a href="gg269213(v=exchg.10).md">JET_coltypLongText</a>).</p> | 



#### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JetAddColumnW</strong> (Unicode) and <strong>JetAddColumnA</strong> (ANSI).</p> | 



#### See Also

[JET_COLTYP](./jet-coltyp.md)  
[JET_COLUMNCREATE](./jet-columncreate-structure.md)  
[JET_COLUMNDEF](./jet-columndef-structure.md)  
[JET_COLUMNID](./jet-columnid.md)  
[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JetCreateTableColumnIndex](./jetcreatetablecolumnindex-function.md)  
[JetCreateTableColumnIndex2](./jetcreatetablecolumnindex2-function.md)
