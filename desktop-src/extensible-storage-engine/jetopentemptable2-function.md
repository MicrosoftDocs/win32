---
description: "Learn more about: JetOpenTempTable2 Function"
title: JetOpenTempTable2 Function
TOCTitle: JetOpenTempTable2 Function
ms:assetid: 788ec4f9-b0c3-409b-850c-7567dec47024
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269302(v=EXCHG.10)
ms:contentKeyID: 32765594
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetOpenTempTable2
topic_type: 
- apiref
- kbArticle
api_type: 
- DLLExport
- COM
api_location: 
- ESENT.DLL
ROBOTS: INDEX,FOLLOW

---

# JetOpenTempTable2 Function


_**Applies to:** Windows | Windows Server_

## JetOpenTempTable2 Function

The **JetOpenTempTable2** function creates a temporary table with a single index that can be used to store and retrieve records just like an ordinary table created using [JetCreateTableColumnIndex](./jetcreatetablecolumnindex-function.md). This function also has a Locale ID that can be used to compare Unicode key column data in the temporary table. However, temporary tables are much faster than ordinary tables due to their volatile nature. They can also be used to very quickly sort and perform duplicate removal on record sets when accessed in a purely sequential manner.

```cpp
    JET_ERR JET_API JetOpenTempTable2(
      __in          JET_SESID sesid,
      __in          const JET_COLUMNDEF* prgcolumndef,
      __in          unsigned long ccolumn,
      __in          unsigned long lcid,
      __in          JET_GRBIT grbit,
      __out         JET_TABLEID* ptableid,
      __out         JET_COLUMNID* prgcolumnid
    );
```

### Parameters

*sesid*

The session to use.

*prgcolumndef*

The column definitions of the columns to be created in the temporary table.

Important limitations exist for the column definition options that are used with a temporary table. See the Remarks section for more information.

In addition to the usual column definition options, zero or more of the following options can also be specified that are relevant only in the context of a temporary table.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitColumnTTDescending</p> | <p>The sort order of the key column for the temporary table should be descending rather than ascending. If this option is specified without JET_bitColumnTTKey then this option is ignored.</p> | 
| <p>JET_bitColumnTTKey</p> | <p>The column will be a key column for the temporary table.</p><p>The order of the column definitions with this option specified in the input array will determine the precedence of each key column for the temporary table. The first column definition in the array with this option set will be the most significant key column and so on. If more key columns are requested than can be supported by the database engine then this option is ignored for the unsupportable key columns.</p> | 



*ccolumn*

See *prgcolumndef*.

*lcid*

The locale ID to use to compare any Unicode key column data in the temporary table.

Any locale may be used as long as the appropriate language pack has been installed on the machine. The one exception is that the Language Neutral locale (LCID of zero) is illegal.

On Windows Server 2003 and later, if the Language Neutral locale is specified for this parameter then the default locale ID (U.S. English) will be used instead. This is to allow a value of zero to signify the default rather than an illegal value.

When this parameter is not present and when the *pidxunicode* parameter is not present, then the default LCID will be used to compare any Unicode key column data in the temporary table. The default LCID is the U.S. English locale.

*grbit*

A group of bits that contain the options to be used for this call, which include zero or more of the following.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitTTErrorOnDuplicateInsertion</p> | <p>This option requests that any attempt to insert a record with the same index key as a previously inserted record will immediately fail with JET_errKeyDuplicate. If this option is not requested then a duplicate may be detected immediately and fail or may be silently removed later depending on the strategy chosen by the database engine to implement the temporary table based on the requested functionality.</p><p>If this functionality it not required then it is best to not request it. If this functionality is not requested then the temporary table manager may be able to choose a strategy for managing the temporary table that will result in improved performance.</p> | 
| <p>JET_bitTTForceMaterialization</p> | <p>This option forces the temporary table manager to abandon any attempt to choose a clever strategy for managing the temporary table that will result in enhanced performance.</p> | 
| <p>JET_bitTTForwardOnly</p> | <p>This option requests that the temporary table only be created if the temporary table manager can use the implementation optimized for intermediate query results. If any characteristic of the temporary table would prevent the use of this optimization then the operation will fail with JET_errCannotMaterializeForwardOnlySort.</p><p>A side effect of this option is to allow the temporary table to contain records with duplicate index keys. See JET_bitTTUnique for more information.</p><p>This option is only available on Windows Server 2003 and later releases.</p> | 
| <p>JET_bitTTIndexed</p> | <p>This option requests that the temporary table be flexible enough to permit the use of <a href="gg294103(v=exchg.10).md">JetSeek</a> to look up records by index key.</p><p>If this functionality it not required then it is best to not request it. If this functionality is not requested then the temporary table manager may be able to choose a strategy for managing the temporary table that will result in improved performance.</p> | 
| <p>JET_bitTTScrollable</p> | <p>This option requests that the temporary table be flexible enough to allow records to be scanned in arbitrary order and direction using <a href="gg294117(v=exchg.10).md">JetMove</a>.</p><p>If this functionality it not required then it is best to not request it. If this functionality is not requested then the temporary table manager may be able to choose a strategy for managing the temporary table that will result in improved performance.</p> | 
| <p>JET_bitTTSortNullsHigh</p> | <p>This option requests that NULL key column values sort closer to the end of the index than non-NULL key column values.</p> | 
| <p>JET_bitTTUnique</p> | <p>This option requests that records with duplicate index keys be removed from the final set of records in the temporary table.</p><p>Prior to Windows Server 2003, the database engine always assumed this option to be in effect due to the fact that all clustered indexes must also be a primary key and thus must be unique. As of Windows Server 2003, it is now possible to create a temporary table that does NOT remove duplicates when the JET_bitTTForwardOnly option is also specified.</p><p>It is not possible to know which duplicate will win and which duplicates will be discarded in general. However, when the JET_bitTTErrorOnDuplicateInsertion option is requested then the first record with a given index key to be inserted into the temporary table will always win.</p> | 
| <p>JET_bitTTUpdatable</p> | <p>This option requests that the temporary table be flexible enough to allow records that have previously been inserted to be subsequently changed. If this functionality it not required then it is best to not request it.</p><p>If this functionality is not requested then the temporary table manager may be able to choose a strategy for managing the temporary table that will result in improved performance.</p> | 
| <p>JET_bitTTIntrinsicLVsOnly</p> | <p>Requests to permit only intrinsic long values.</p><p><strong>Windows 7</strong>: <strong>JET_bitTTIntrinsicLVsOnly</strong> is introduced in Windows 7.</p> | 



*ptableid*

The output buffer that will receive the new cursor opened on the newly created temporary table.

*prgcolumnid*

The output buffer that will receive the array of column IDs generated during the creation of the temporary table.

The column IDs in this array will exactly correspond to the input array of column definitions. As a result, the size of this buffer must correspond to the size of the input array.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errCannotMaterializeForwardOnlySort</p> | <p><strong>JetOpenTempTable2</strong> failed because JET_bitTTForwardOnly was specified and the temporary table as specified could not be created using the forward-only optimization. This error will only be returned by Windows Server 2003 and later releases.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data. This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errInvalidCodePage</p> | <p>The cp field of the <a href="gg294130(v=exchg.10).md">JET_COLUMNDEF</a> was not set to a valid code page. The only valid values for text columns are English (1252) and Unicode (1200). A value of 0 means the default will be used (English, 1252).</p> | 
| <p>JET_errInvalidColumnType</p> | <p>The <em>coltyp</em> field of the <a href="gg294130(v=exchg.10).md">JET_COLUMNDEF</a> was not set to a valid column type.</p> | 
| <p>JET_errIndexInvalidDef</p> | <p>The index could not be created because an invalid index definition was specified.</p><p><strong>JetOpenTempTable2</strong> will return this error when:</p><ul><li><p>The Language Neutral locale is specified.</p></li><li><p>An invalid set of normalization flags is specified.</p></li></ul><p>This error will only be returned by Windows 2000.</p> | 
| <p>JET_errInvalidLanguageId</p> | <p>The index could not be created because an attempt was made to use an invalid locale ID. The locale ID may either be completely invalid or the associated language pack may not be installed.</p> | 
| <p>JET_errInvalidLCMapStringFlags</p> | <p>The index could not be created because an attempt was made to use an invalid set of normalization flags. This error will only be returned by Windows XP and later releases. On Windows 2000, invalid normalization flags will result in JET_errIndexInvalidDef instead.</p> | 
| <p>JET_errNotInitialized</p> | <p>It is not possible to complete the operation because the instance associated with the session has not been initialized yet.</p> | 
| <p>JET_errOutOfCursors</p> | <p>The operation failed because the engine cannot allocate the resources required to open a new cursor. Cursor resources are configured using <a href="gg294044(v=exchg.10).md">JetSetSystemParameter</a> with <a href="gg269201(v=exchg.10).md">JET_paramMaxCursors</a>.</p> | 
| <p>JET_errOutOfMemory</p> | <p>The operation failed because not enough memory could be allocated to complete it.</p><p><strong>JetOpenTempTable2</strong> can return JET_errOutOfMemory if the address space of the host process becomes too fragmented. The temporary table manager will always allocate a 1MB chunk of address space for every temporary table created regardless of the amount of data to be stored.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p> | 
| <p>JET_errSessionSharingViolation</p> | <p>The same session cannot be used for more than one thread at the same time.</p><p>This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errTermInProgress</p> | <p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p> | 
| <p>JET_errTooManyColumns</p> | <p>An attempt was made to add too many columns to the table. A table can have no more than JET_ccolFixedMost fixed columns, no more than JET_ccolVarMost variable-length columns, and no more than JET_ccolTaggedMost tagged columns.</p> | 
| <p>JET_errTooManyOpenIndexes</p> | <p>The operation failed because the engine cannot allocate the resources required to cache the indexes of the table. The number of indexes whose schema can be cached is configured using <a href="gg294044(v=exchg.10).md">JetSetSystemParameter</a> with <a href="gg269201(v=exchg.10).md">JET_paramMaxOpenTables</a>.</p> | 
| <p>JET_errTooManyOpenTables</p> | <p>The operation failed because the engine cannot allocate the resources required to cache the schema of the table. The number of tables whose schema can be cached is configured using <a href="gg294044(v=exchg.10).md">JetSetSystemParameter</a> with <a href="gg269201(v=exchg.10).md">JET_paramMaxOpenTables</a>.</p> | 
| <p>JET_errTooManySorts</p> | <p>The operation failed because the engine cannot allocate the resources required to create a temporary table. Temporary table resources are configured using <a href="gg294044(v=exchg.10).md">JetSetSystemParameter</a> with <a href="gg294140(v=exchg.10).md">JET_paramMaxTemporaryTables</a>.</p> | 



On success, a cursor opened on the newly created temporary table will be returned. The state of the temporary database will be prepared to contain the new temporary table. The state of any ordinary databases in use by the database engine will remain unchanged.

On failure, the temporary table will not be created and a cursor will not be returned. The state of the temporary database may be changed. The state of any ordinary databases in use by the database engine will remain unchanged.

#### Remarks

See [JetOpenTempTable](./jetopentemptable-function.md).

#### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See Also

[JET_COLUMNDEF](./jet-columndef-structure.md)  
[JET_COLUMNID](./jet-columnid.md)  
[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JET_UNICODEINDEX](./jet-unicodeindex-structure.md)  
[JetCloseTable](./jetclosetable-function.md)  
[JetCreateTableColumnIndex](./jetcreatetablecolumnindex-function.md)  
[JetDupCursor](./jetdupcursor-function.md)  
[JetMove](./jetmove-function.md)  
[JetRollback](./jetrollback-function.md)  
[JetSeek](./jetseek-function.md)  
[JetSetSystemParameter](./jetsetsystemparameter-function.md)  
[System Parameters](./extensible-storage-engine-system-parameters.md)
