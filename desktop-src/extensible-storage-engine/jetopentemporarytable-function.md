---
description: "Learn more about: JetOpenTemporaryTable Function"
title: JetOpenTemporaryTable Function
TOCTitle: JetOpenTemporaryTable Function
ms:assetid: feacd0b8-2298-4ec6-aa59-0fede08474bc
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294144(v=EXCHG.10)
ms:contentKeyID: 32765758
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetOpenTemporaryTable
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

# JetOpenTemporaryTable Function


_**Applies to:** Windows | Windows Server_

## JetOpenTemporaryTable Function

The **JetOpenTemporaryTable** function creates a volatile table with a single index that can be used to store and retrieve records, just like an ordinary table that is created via [JetCreateTableColumnIndex](./jetcreatetablecolumnindex-function.md).

**Windows Vista:**  **JetOpenTemporaryTable** is introduced in Windows Vista.

Temporary tables are faster than ordinary tables due to their volatile nature. They can quickly sort and perform duplicate removal on record sets when they are accessed in a purely sequential manner.

```cpp
    JET_ERR JET_API JetOpenTemporaryTable(
      __in          JET_SESID sesid,
      __in          JET_OPENTEMPORARYTABLE* popentemporarytable
    );
```

### Parameters

*sesid*

The session that will be used for this call.

*popentemporarytable*

A pointer to a [JET_OPENTEMPORARYTABLE](./jet-opentemporarytable-structure.md) structure that contains the description of the temporary table to create on input. After a successful call, the structure contains the handle to the temporary table and column identifications.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Return code</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>JET_errSuccess</p></td>
<td><p>The operation completed successfully.</p></td>
</tr>
<tr class="even">
<td><p>JET_errOutOfMemory</p></td>
<td><p>The operation failed because not enough memory could be allocated to complete it.</p>
<p><strong>JetOpenTemporaryTable</strong> can return JET_errOutOfMemory if the address space of the host process becomes too fragmented. The temporary table manager will allocates a 1 MB chunk of address space for every temporary table created regardless of the amount of data is stored.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errInvalidParameter</p></td>
<td><p>One of the provided parameters contained an unexpected value or the combination of several parameter values resulted in an unexpected result.</p>
<p>This error is returned by <strong>JetOpenTemporaryTable</strong> under the following conditions:</p>
<ul>
<li><p>The <strong>cbStruct</strong> member of the <a href="gg269206(v=exchg.10).md">JET_OPENTEMPORARYTABLE</a> structure does not correspond to a version of this structure that is supported by that version of the database engine</p></li>
<li><p>The <strong>cbKeyMost</strong> member of the <a href="gg269206(v=exchg.10).md">JET_OPENTEMPORARYTABLE</a> structure is less than JET_cbKeyMostMin.</p></li>
<li><p>The <strong>cbKeyMost</strong> member of the <a href="gg269206(v=exchg.10).md">JET_OPENTEMPORARYTABLE</a> structure is larger than the largest supported value for the database page size for the instance (JET_paramDatabasePageSize). See the JET_paramKeyMost parameter in the list of <a href="gg269241(v=exchg.10).md">Informational Parameters</a> for more information.</p></li>
<li><p>The cbVarSegMac member of the <a href="gg269206(v=exchg.10).md">JET_OPENTEMPORARYTABLE</a> structure is larger than The <strong>cbKeyMost</strong> member.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>JET_errNotInitialized</p></td>
<td><p>The operation cannot complete because the instance that was associated with the session has not yet been initialized.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errClientRequestToStopJetService</p></td>
<td><p>The operation cannot complete because all activity on the instance that is associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p></td>
</tr>
<tr class="even">
<td><p>JET_errInstanceUnavailable</p></td>
<td><p>The operation cannot complete because the instance that is associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data.</p>
<p><strong>Windows XP:</strong>  This error will only be returned by Windows XP and later releases.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errTermInProgress</p></td>
<td><p>The operation cannot complete because the instance that is associated with the session is being shut down.</p></td>
</tr>
<tr class="even">
<td><p>JET_errRestoreInProgress</p></td>
<td><p>The operation cannot complete because a restore operation is in progress on the instance that is associated with the session.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errSessionSharingViolation</p></td>
<td><p>The same session cannot be used for more than one thread at the same time.</p>
<p><strong>Windows XP:</strong>  This error will only be returned by Windows XP and later releases.</p></td>
</tr>
<tr class="even">
<td><p>JET_errInvalidSesid</p></td>
<td><p>The session handle is invalid or refers to a closed session.</p>
<p><strong>Note</strong>  This error is not returned under all circumstances. Handles are validated on a best effort basis only.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errOutOfCursors</p></td>
<td><p>The operation failed because the engine cannot allocate the resources that are required to open a new cursor. Cursor resources are configured using <a href="gg294044(v=exchg.10).md">JetSetSystemParameter</a> with <a href="gg269201(v=exchg.10).md">JET_paramMaxCursors</a>.</p></td>
</tr>
<tr class="even">
<td><p>JET_errTooManySorts</p></td>
<td><p>The operation failed because the engine cannot allocate the resources that are required to create a temporary table. Temporary table resources are configured using <a href="gg294044(v=exchg.10).md">JetSetSystemParameter</a> with <a href="gg294140(v=exchg.10).md">JET_paramMaxTemporaryTables</a>.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errCannotMaterializeForwardOnlySort</p></td>
<td><p><strong>JetOpenTemporaryTable</strong> failed because JET_bitTTForwardOnly was specified and the temporary table that was specified could not be created using the forward-only optimization.</p>
<p><strong>Windows Server 2003:</strong>  This error will only be returned by Windows Server 2003 and later releases.</p></td>
</tr>
<tr class="even">
<td><p>JET_errTooManyColumns</p></td>
<td><p>An attempt was made to add too many columns to the table. A table can have no more than JET_ccolFixedMost fixed columns, no more than JET_ccolVarMost variable-length columns, and no more than JET_ccolTaggedMost tagged columns.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errTooManyOpenTables</p></td>
<td><p>The operation failed because the engine cannot allocate the resources that are required to cache the schema of the table. To configure the number of tables that have schemas that can be cached, use <a href="gg294044(v=exchg.10).md">JetSetSystemParameter</a> with <a href="gg269201(v=exchg.10).md">JET_paramMaxOpenTables</a>.</p></td>
</tr>
<tr class="even">
<td><p>JET_errInvalidCodePage</p></td>
<td><p>The <strong>cp</strong> member of the <a href="gg294130(v=exchg.10).md">JET_COLUMNDEF</a> structure was not set to a valid code page. The only valid values for text columns are English (1252) and Unicode (1200). A value of 0 means the default will be used (English, 1252).</p></td>
</tr>
<tr class="odd">
<td><p>JET_errInvalidColumnType</p></td>
<td><p>The <strong>coltyp</strong> member of the <a href="gg294130(v=exchg.10).md">JET_COLUMNDEF</a> was not set to a valid column type.</p></td>
</tr>
<tr class="even">
<td><p>JET_errInvalidLanguageId</p></td>
<td><p>The index could not be created because an attempt was made to use an invalid locale ID. The locale ID might be either completely invalid or the associated language pack might not be installed.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errInvalidLCMapStringFlags</p></td>
<td><p>The index could not be created because an attempt was made to use an invalid set of normalization flags.</p>
<p><strong>Windows XP:</strong>  This error will only be returned by Windows XP and later releases.</p>
<p><strong>Windows 2000:</strong>  On Windows 2000, invalid normalization flags will result in JET_errIndexInvalidDef.</p></td>
</tr>
<tr class="even">
<td><p>JET_errIndexInvalidDef</p></td>
<td><p>The index could not be created because an invalid index definition was specified. <strong>JetOpenTemporaryTable</strong> will return this error under the following conditions:</p>
<ul>
<li><p>The Language Neutral locale is specified.</p></li>
<li><p>An invalid set of normalization flags is specified.</p></li>
</ul>
<p><strong>Windows 2000:</strong>  This error will only be returned by Windows 2000.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errTooManyOpenIndexes</p></td>
<td><p>The operation failed because the engine cannot allocate the resources that are required to cache the indexes of the table. To configure the number of indexes that have schemas that can be cached, use <a href="gg294044(v=exchg.10).md">JetSetSystemParameter</a> with <a href="gg269201(v=exchg.10).md">JET_paramMaxOpenTables</a>.</p></td>
</tr>
</tbody>
</table>


On success, a cursor opened on the newly created temporary table will be returned. The state of the temporary database will be prepared to contain the new temporary table. The state of any ordinary databases in use by the database engine will remain unchanged.

On failure, the temporary table will not be created and a cursor will not be returned. The state of the temporary database can be changed. The state of any ordinary databases in use by the database engine will remain unchanged.

#### Remarks

Temporary tables do not support the full complement of column definition options that are ordinarily supported by the database engine. In fact, only JET_bitColumnFixed and JET_bitColumnTagged are supported. This means that it is not possible to create an auto-increment, version, or multi-valued column in a temporary table. Finally, escrow update columns are not supported because they can only be used by one session at a time. If any of these options are requested then they will be ignored.

Temporary tables do not support default values. If a column definition is provided that contains a default value specification then that specification will be ignored.

Temporary tables are returned to the caller as a result of many different ESE functions. For example, [JetGetIndexInfo](./jetgetindexinfo-function.md) with the JET_IdxInfo option set will return a temporary table containing a list of all the key columns in a given index. The temporary tables follow the same lifecycle rules as ordinary temporary tables as described here.

Temporary tables are also used internally by the database engine for many tasks. The most important of these tasks is the creation of an index over an existing table. A temporary table will be used to sort the index keys that are used to construct that index.

All temporary tables are stored in the temporary database. The temporary database is a special database file that is maintained during the lifetime of an ESE instance and is deleted when that instance is shut down or restarted. The location of the temporary database can be configured using [JetSetSystemParameter](./jetsetsystemparameter-function.md) with [JET_paramTempPath](./temporary-database-parameters.md). Placement of the temporary database on disk relative to your transaction log files and database files may be important if your application makes heavy use of temporary tables or creates indexes frequently.

The lifecycle of a temporary table is tied to the cursors that reference it. If all the cursors that reference a temporary table are closed, either implicitly or explicitly, then the temporary table will be deleted. If a temporary table is created inside a transaction and that transaction is subsequently rolled back then the temporary table will be deleted because any cursors that referenced it at this time will be implicitly closed. New cursors can reference a temporary table only through the use of [JetDupCursor](./jetdupcursor-function.md). In this case, the new cursors will be positioned on the first index entry of the temporary table. [JetDupCursor](./jetdupcursor-function.md) will only work during certain phases of use for the temporary table. See the remarks concerning temporary table cursor capabilities for more information. It is not possible to reference a temporary table from more than one session at a time.

**Caution**  There is an important problem in [JetDupCursor](./jetdupcursor-function.md) that affects temporary tables. If an attempt is made to duplicate a temporary table that is in forward-only mode then the resulting cursor will not be created properly and will malfunction. It is still safe to duplicate a cursor over a materialized temporary table.

The temporary table manager can implement a temporary table in three ways. The first method is to maintain an in-memory table. This strategy is the fastest but can only be used for small, simple, temporary tables. The second method is to create a disk-based sort that can be driven using a forward-only iterator. This strategy can only be used under certain circumstances and is the fastest way to sort and remove duplicates from a very large data set. The third method is to create a B+ Tree in the temporary database to hold the temporary table. This strategy is the slowest, but the most versatile, and is referred to as a materialized temporary table. These strategies can be used in combination to ultimately achieve the functionality that is requested of the temporary table.

When the temporary table is not materialized then it is used primarily in two major phases. The first phase is the insertion phase where the table is populated with its initial data set. During this phase, only data insertion is allowed. This phase ends when an attempt is made to move the cursor using [JetMove](./jetmove-function.md) or [JetSeek](./jetseek-function.md). The second phase is the data extraction phase. During this phase, the data that is stored in the temporary table can be extracted according to the capabilities that were requested when the temporary table was created.

**Temporary Table Cursor Capabilities**

When the temporary table is materialized, the cursor has the following capabilities but might be further limited by the options that are requested:

  - [JetCloseTable](./jetclosetable-function.md)

  - [JetDelete](./jetdelete-function.md)

  - [JetDupCursor](./jetdupcursor-function.md)

  - [JetEnumerateColumns](./jetenumeratecolumns-function.md)

  - [JetEscrowUpdate](./jetescrowupdate-function.md)

  - [JetGetBookmark](./jetgetbookmark-function.md)

  - [JetGetCursorInfo](./jetgetcursorinfo-function.md)

  - [JetGetLS](./jetgetls-function.md)

  - [JetGetRecordSize](./jetgetrecordsize-function.md)

  - [JetGetTableInfo](./jetgettableinfo-function.md)

  - [JetGotoBookmark](./jetgotobookmark-function.md)

  - [JetMakeKey](./jetmakekey-function.md)

  - [JetMove](./jetmove-function.md)

  - [JetPrepareUpdate](./jetprepareupdate-function.md)

  - [JetRetrieveColumn](./jetretrievecolumn-function.md)

  - [JetRetrieveColumns](./jetretrievecolumns-function.md)

  - [JetRetrieveKey](./jetretrievekey-function.md)

  - [JetSeek](./jetseek-function.md)

  - [JetSetColumn](./jetsetcolumn-function.md)

  - [JetSetColumns](./jetsetcolumns-function.md)

  - [JetSetIndexRange](./jetsetindexrange-function.md)

  - [JetSetLS](./jetsetls-function.md)

  - [JetUpdate](./jetupdate-function.md)

When the temporary table is not materialized and is in the insert phase, the cursor has the following capabilities but might be further limited by the options that are requested:

  - [JetCloseTable](./jetclosetable-function.md)

  - [JetEscrowUpdate](./jetescrowupdate-function.md)

  - [JetMakeKey](./jetmakekey-function.md)

  - [JetMove](./jetmove-function.md)
    
    **Note**  Causes transition to the extract phase.

  - [JetPrepareUpdate](./jetprepareupdate-function.md)

  - [JetRetrieveKey](./jetretrievekey-function.md)

  - [JetSeek](./jetseek-function.md)
    
    **Note**  Causes transition to the extract phase.

  - [JetSetColumn](./jetsetcolumn-function.md)

  - [JetSetColumns](./jetsetcolumns-function.md)

  - [JetUpdate](./jetupdate-function.md)

When the temporary table is not materialized and is in the extract phase, the cursor has the following capabilities but may be further limited by the options that are requested:

  - [JetCloseTable](./jetclosetable-function.md)

  - [JetDupCursor](./jetdupcursor-function.md)
    
    **Note**  If an attempt is made to duplicate a temporary table that is in forward-only mode then the resulting cursor will not be created properly and will malfunction. It is still safe to duplicate a cursor over a materialized temporary table.

  - [JetEnumerateColumns](./jetenumeratecolumns-function.md)

  - [JetGetBookmark](./jetgetbookmark-function.md)

  - [JetGetLS](./jetgetls-function.md)

  - [JetGetRecordSize](./jetgetrecordsize-function.md)

  - [JetGetTableInfo](./jetgettableinfo-function.md)

  - [JetGotoBookmark](./jetgotobookmark-function.md)

  - [JetMakeKey](./jetmakekey-function.md)

  - [JetMove](./jetmove-function.md)

  - [JetRetrieveColumn](./jetretrievecolumn-function.md)

  - [JetRetrieveColumns](./jetretrievecolumns-function.md)

  - [JetRetrieveKey](./jetretrievekey-function.md)

  - [JetSeek](./jetseek-function.md)

  - [JetSetIndexRange](./jetsetindexrange-function.md)

  - [JetSetLS](./jetsetls-function.md)

#### Requirements

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
<tr class="even">
<td><p><strong>Library</strong></p></td>
<td><p>Use ESENT.lib.</p></td>
</tr>
<tr class="odd">
<td><p><strong>DLL</strong></p></td>
<td><p>Requires ESENT.dll.</p></td>
</tr>
</tbody>
</table>


#### See Also

[JET_ERR](./jet-err.md)  
[JET_SESID](./jet-sesid.md)  
[JET_OPENTEMPORARYTABLE](./jet-opentemporarytable-structure.md)  
[JetCloseTable](./jetclosetable-function.md)  
[JetCreateTableColumnIndex](./jetcreatetablecolumnindex-function.md)  
[JetDupCursor](./jetdupcursor-function.md)  
[JetMove](./jetmove-function.md)  
[JetRollback](./jetrollback-function.md)  
[JetSeek](./jetseek-function.md)  
[JetSetSystemParameter](./jetsetsystemparameter-function.md)  
[Informational Parameters](./informational-parameters.md)  
[Temporary Database Parameters](./temporary-database-parameters.md)
