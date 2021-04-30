---
description: "Learn more about: JET_OPENTEMPORARYTABLE Structure"
title: JET_OPENTEMPORARYTABLE Structure
TOCTitle: JET_OPENTEMPORARYTABLE Structure
ms:assetid: 23f4fb0f-ca60-498b-9b8e-14de6188eb87
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269206(v=EXCHG.10)
ms:contentKeyID: 32765509
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

# JET_OPENTEMPORARYTABLE Structure


_**Applies to:** Windows | Windows Server_

## JET_OPENTEMPORARYTABLE Structure

The **JET_OPENTEMPORARYTABLE** structure contains an easily extensible collection of parameters for the **JET_OPENTEMPORARYTABLE** function. This structure is the temporary table equivalent of the [JET_TABLECREATE](./jet-tablecreate-structure.md) structure.

**Windows Vista:** The **JET_OPENTEMPORARYTABLE** structure is introduced in Windows Vista.

```cpp
    typedef struct tagJET_OPENTEMPORARYTABLE {
      unsigned long cbStruct;
      const JET_COLUMNDEF* prgcolumndef;
      unsigned long ccolumn;
      JET_UNICODEINDEX* pidxunicode;
      JET_GRBIT grbit;
      JET_COLUMNID* prgcolumnid;
      unsigned long cbKeyMost;
      unsigned long cbVarSegMac;
      JET_TABLEID tableid;
    } JET_OPENTEMPORARYTABLE;
```

### Members

**cbStruct**

The size of this structure in bytes (for future expansion). It must be set to sizeof( JET_TABLECREATE ) in bytes.

**prgcolumndef**

Column definitions for the columns created in the temporary table.

**Important** limitations exist for the column definition options that are used with a temporary table. See the Remarks section for more information.

In addition to the usual column definition options, zero or more of the following options can also be specified that are relevant only in the context of a temporary table.

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
<td><p>JET_bitColumnTTDescending</p></td>
<td><p>The sort order of the key column for the temporary table should be descending rather than ascending. If this option is specified without JET_bitColumnTTKey then this option is ignored.</p></td>
</tr>
<tr class="even">
<td><p>JET_bitColumnTTKey</p></td>
<td><p>The column will be a key column for the temporary table.</p>
<p>The order of the column definitions with this option specified in the input array will determine the precedence of each key column for the temporary table. The first column definition in the array that has this option set will be the most significant key column and so on. If more key columns are requested than can be supported by the database engine then this option is ignored for the unsupportable key columns.</p></td>
</tr>
</tbody>
</table>


**ccolumn**

See *prgcolumndef*.

**pidxunicode**

The locale ID and normalization flags to use to compare any Unicode key column data in the temporary table.

When this parameter is not present and when the *lcid* parameter is not present, then the default LCID will be used to compare any Unicode key columns in the temporary table. The default LCID is the U.S. English locale.

When this parameter is not present, then the default normalization flags will be used to compare any Unicode key column data in the temp table. The default normalization flags are: NORM_IGNORECASE, NORM_IGNOREKANATYPE, and NORM_IGNOREWIDTH.

**grbit**

A group of bits specifying zero or more of the following options.

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
<td><p>JET_bitTTIndexed</p></td>
<td><p>This option requests that the temporary table be flexible enough to permit the use of <a href="gg294103(v=exchg.10).md">JetSeek</a> to look up records by index key.</p>
<p>If this functionality it not required then it is best to not request it. If this functionality is not requested then the temporary table manager may be able to choose a strategy for managing the temporary table that will result in improved performance.</p></td>
</tr>
<tr class="even">
<td><p>JET_bitTTUnique</p></td>
<td><p>Requests that records with duplicate index keys be removed from the final set of records in the temporary table.</p>
<p>Prior to Windows Server 2003, the database engine always assumed this option to be in effect due to the fact that all clustered indexes must also be a primary key and thus must be unique. As of Windows Server 2003, it is now possible to create a temporary table that does not remove duplicates when the JET_bitTTForwardOnly option is also specified.</p>
<p>It is not possible to know which duplicate will succeed and which duplicates will be discarded, in general. However, when the JET_bitTTErrorOnDuplicateInsertion option is requested then the first record with a given index key to be inserted into the temporary table will always succeed.</p></td>
</tr>
<tr class="odd">
<td><p>JET_bitTTUpdatable</p></td>
<td><p>Requests that the temporary table be flexible enough to allow records that have previously been inserted to be subsequently changed. If this functionality it not required then it is best to not request it.</p>
<p>If this functionality is not requested then the temporary table manager may be able to choose a strategy for managing the temporary table that will result in improved performance.</p></td>
</tr>
<tr class="even">
<td><p>JET_bitTTScrollable</p></td>
<td><p>Requests that the temporary table be flexible enough to allow records to be scanned in arbitrary order and direction using <a href="gg294117(v=exchg.10).md">JetMove</a>.</p>
<p>If this functionality is not required then it is best to not request it. If this functionality is not requested then the temporary table manager may be able to choose a strategy for managing the temporary table that will result in improved performance.</p></td>
</tr>
<tr class="odd">
<td><p>JET_bitTTSortNullsHigh</p></td>
<td><p>Requests that <strong>NULL</strong> key column values sort closer to the end of the index than non-NULL key column values.</p></td>
</tr>
<tr class="even">
<td><p>JET_bitTTForceMaterialization</p></td>
<td><p>Forces the temporary table manager to abandon the search for the best strategy to use managing the temporary table that will result in enhanced performance.</p></td>
</tr>
<tr class="odd">
<td><p>JET_bitTTErrorOnDuplicateInsertion</p></td>
<td><p>Any attempt to insert a record with the same index key as a previously inserted record will immediately fail with JET_errKeyDuplicate. If this option is not requested then a duplicate is detected immediately and fails, or is silently removed later, depending on the strategy chosen by the database engine to implement the temporary table, based on the requested functionality.</p>
<p>If this functionality it not required then it is best to not request it. If this functionality is not requested then the temporary table manager may be able to choose a strategy for managing the temporary table that will result in improved performance.</p></td>
</tr>
<tr class="even">
<td><p>JET_bitTTForwardOnly</p></td>
<td><p>The temporary table is only created if the temporary table manager can use the implementation that is optimized for intermediate query results. If any characteristic of the temporary table would prevent the use of this optimization then the operation will fail with JET_errCannotMaterializeForwardOnlySort.</p>
<p>A side effect of this option is to allow the temporary table to contain records with duplicate index keys. See JET_bitTTUnique for more information.</p>
<p><strong>Windows Server 2003:  </strong>This option is only available on Windows Server 2003 and later releases.</p></td>
</tr>
</tbody>
</table>


**prgcolumnid**

The output buffer that receives the array of column IDs generated during the creation of the temporary table.

The column IDs in this array will exactly correspond to the input array of column definitions. As a result, the size of this buffer must correspond to the size of the input array.

**cbKeyMost**

The maximum size for a key representing a given row.

The maximum key size may be set to control how keys are truncated. Key truncation is important because it can affect when rows are considered to be distinct.

If this parameter is set to 0 or JET_cbKeyMostMin (255) then the maximum key size and its semantics will remain identical to the maximum key size supported by Windows Server 2003 and previous releases. This parameter may also be set to a larger value as a function of the database page size for the instance (JET_paramDatabasePageSize). See JET_paramKeyMost for more information.

**cbVarSegMac**

The maximum amount of data that will be used from any variable length column to construct a key for a given row.

This parameter may be used to control the amount of key space consumed by any given key column. This limit is in bytes. If this parameter is zero or is the same as the *cbKeyMost* parameter then no limit is in effect.

**tableid**

The table handle for the temporary table created as a result of a successful call to [JetOpenTemporaryTable](./jetopentemporarytable-function.md).

### Requirements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Client</strong></p></td>
<td><p>Requires Windows Vista.</p></td>
</tr>
<tr class="even">
<td><p><strong>Server</strong></p></td>
<td><p>Requires Windows Server 2008.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Header</strong></p></td>
<td><p>Declared in Esent.h.</p></td>
</tr>
</tbody>
</table>


### See Also

[JET_TABLECREATE](./jet-tablecreate-structure.md)  
[JET_COLUMNDEF](./jet-columndef-structure.md)  
[JET_UNICODEINDEX](./jet-unicodeindex-structure.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_COLUMNID](./jet-columnid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JetOpenTemporaryTable](./jetopentemporarytable-function.md)  
[Extensible Storage Engine System Parameters](./extensible-storage-engine-system-parameters.md)
