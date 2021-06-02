---
description: "Learn more about: JetMakeKey Function"
title: JetMakeKey Function
TOCTitle: JetMakeKey Function
ms:assetid: 8c1cff2f-2f24-4990-a9d8-fb4f822e50b1
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269329(v=EXCHG.10)
ms:contentKeyID: 32765619
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetMakeKey
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

# JetMakeKey Function


_**Applies to:** Windows | Windows Server_

## JetMakeKey Function

The **JetMakeKey** function constructs search keys that may then be used to find a set of entries in an index by some simple search criteria on their key column values. A search key is also one of the intrinsic properties of a cursor and is used by the [JetSeek](./jetseek-function.md) and [JetSetIndexRange](./jetsetindexrange-function.md) operations to locate index entries matching these search criteria on the current index of that cursor. A complete search key is built up in a series of **JetMakeKey** calls where each call is used to load the column value for the next key column of the current index of a cursor. It is also possible to load a previously constructed search key that has been retrieved from the cursor using [JetRetrieveKey](./jetretrievekey-function.md).

```cpp
    JET_ERR JET_API JetMakeKey(
      __in          JET_SESID sesid,
      __in          JET_TABLEID tableid,
      __in_opt      const void* pvData,
      __in          unsigned long cbData,
      __in          JET_GRBIT grbit
    );
```

### Parameters

*sesid*

The session to use for this call.

*tableid*

The cursor to use for this call.

*pvData*

The input buffer containing the column data for the current key column of the current index of the cursor for which the search key is being constructed.

The data type of the column data in the input buffer must exactly match the data type and other properties of the column definition of the current key column. No type coercion is performed on the column data whatsoever.

If JET_bitNormalizedKey is specified in the *grbit* parameter, the input buffer must contain a previously constructed search key. Such keys are obtained using a call to [JetRetrieveKey](./jetretrievekey-function.md).

*cbData*

The size in bytes of the column data provided in the input buffer.

If JET_bitNormalizedKey is specified in the *grbit* parameter, this is the size of the search key provided in the input buffer.

If the size of the column data is zero then the contents of the input buffer are ignored. If JET_bitKeyDataZeroLength is specified in the *grbit* parameter and the current key column of the current index of the cursor is a variable length column, the input column data is presumed to be a zero length value. Otherwise, the input column data is presumed to be a NULL value.

*grbit*

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
<td><p>JET_bitFullColumnEndLimit</p></td>
<td><p>The search key should be constructed in such a way that any key columns that come after the current key column are considered to be wildcards. This means that the constructed search key can be used to match index entries that have the following:</p>
<ul>
<li><p>The exact column values provided for this key column and all previous key columns.</p></li>
<li><p>Any column values needed for subsequent key columns.</p></li>
</ul>
<p>This option should be used when building wildcard search keys to use for finding index entries closest to the end of an index. The end of the index is the index entry that is found when moving to the last record in that index. The end of the index is not the same as the high end of the index, which can change depending on the sort order of the key columns in the index.</p>
<p>This option is only available on Windows XP and later releases.</p></td>
</tr>
<tr class="even">
<td><p>JETbitFullColumnStartLimit</p></td>
<td><p>The search key should be constructed such that any key columns that come after the current key column should be considered to be wildcards. This means that the constructed search key can be used to match index entries that have the following:</p>
<ul>
<li><p>The exact column values provided for this key column and all previous key columns.</p></li>
<li><p>Any column values needed for subsequent key columns.</p></li>
</ul>
<p>This option should be used when building wildcard search keys to use for finding index entries closest to the start of an index. The start of the index is the index entry that is found when moving to the first record in that index. The start of the index is not the same as the low end of the index, which can change depending on the sort order of the key columns in the index.</p>
<p>This option is only available on Windows XP and later releases.</p></td>
</tr>
<tr class="odd">
<td><p>JET_bitKeyDataZeroLength</p></td>
<td><p>If the size of the input buffer is zero and the current key column is a variable length column, this option indicates that the input buffer contains a zero length value. Otherwise, an input buffer size of zero would indicate a NULL value.</p></td>
</tr>
<tr class="even">
<td><p>JET_bitNewKey</p></td>
<td><p>A new search key should be constructed. Any previously existing search key is discarded.</p></td>
</tr>
<tr class="odd">
<td><p>JET_bitNormalizedKey</p></td>
<td><p>When this option is specified, all other options are ignored, any previously existing search key is discarded, and the contents of the input buffer are loaded as the new search key.</p></td>
</tr>
<tr class="even">
<td><p>JET_bitPartialColumnEndLimit</p></td>
<td><p>The search key should be constructed such that the current key column is considered to be a prefix wildcard and that any key columns that come after the current key column should be considered to be wildcards. This means that the constructed search key can be used to match index entries that have the following:</p>
<ul>
<li><p>The exact column values provided for this key column and all previous key columns.</p></li>
<li><p>Any column values needed for subsequent key columns.</p></li>
</ul>
<p>This option should be used when building wildcard search keys to use for finding index entries closest to the end of an index. The end of the index is the index entry that is found when moving to the last record in that index. The end of the index is not the same as the high end of the index, which can change depending on the sort order of the key columns in the index.</p>
<p>This option cannot be used when the current key column is not a text column or a variable binary column. The operation will fail with JET_errInvalidgrbit if this is attempted.</p>
<p>This option is only available on Windows XP and later releases.</p></td>
</tr>
<tr class="odd">
<td><p>JET_bitPartialColumnStartLimit</p></td>
<td><p>This option indicates that the search key should be constructed such that the current key column is considered to be a prefix wildcard and that any key columns that come after the current key column should be considered to be wildcards. This means that the constructed search key can be used to match index entries that have the following:</p>
<ul>
<li><p>The exact column values provided for this key column and all previous key columns.</p></li>
<li><p>Any column values needed for subsequent key columns.</p></li>
</ul>
<p>This option should be used when building wildcard search keys to use for finding index entries closest to the start of an index. The start of the index is the index entry that is found when moving to the first record in that index. The start of the index is not the same as the low end of the index, which can change depending on the sort order of the key columns in the index.</p>
<p>This option cannot be used when the current key column is not a text column or a variable binary column. The operation will fail with JET_errInvalidgrbit if this is attempted.</p>
<p>This option is only available on Windows XP and later releases.</p></td>
</tr>
<tr class="even">
<td><p>JET_bitStrLimit</p></td>
<td><p>This option indicates that the search key should be constructed such that any key columns that come after the current key column should be considered to be wildcards. This means that the constructed search key can be used to match index entries that have the following:</p>
<ul>
<li><p>The exact column values provided for this key column and all previous key columns.</p></li>
<li><p>Any column values needed for subsequent key columns.</p></li>
</ul>
<p>This option should be used when building wildcard search keys to use for finding index entries closest to the end of an index. The end of the index is the index entry that is found when moving to the last record in that index. The end of the index is not the same as the high end of the index, which can change depending on the sort order of the key columns in the index.</p>
<p>When this option is specified in combination with JET_bitSubStrLimit and the current key column is a text column, this option will be ignored. This behavior is intended to allow the type of the current key column to be inferred when building the search key.</p>
<p>If you want to build a similar search key for the start of an index, a similar call to <strong>JetMakeKey</strong> should be made for the last key column that is not a wildcard, but with no wildcard options specified. The search key is then in an appropriate state to use for such a search. This is analogous to using JET_bitFullColumnStartLimit, except that the search key is not cleanly finished as it is after the use of a wildcard option.</p>
<p>This option has been deprecated for Windows XP and later releases in order to address this awkward semantic. JET_bitFullColumnStartLimit and JET_bitFullColumnEndLimit should be used instead wherever possible.</p></td>
</tr>
<tr class="odd">
<td><p>JET_bitSubStrLimit</p></td>
<td><p>This option indicates that the search key should be constructed such that the current key column is considered to be a prefix wildcard and that any key columns that come after the current key column should be considered to be wildcards. This means that the constructed search key can be used to match index entries that have the following:</p>
<ul>
<li><p>The exact column values provided for all previous key columns.</p></li>
<li><p>The specified column data as a prefix of their column value for the current key column.</p></li>
<li><p>Any column values for subsequent key columns.</p></li>
</ul>
<p>This option should be used when building wildcard search keys to use for finding index entries closest to the end of an index. The end of the index is the index entry that is found when moving to the last record in that index. The end of the index is not the same as the high end of the index, which can change depending on the sort order of the key columns in the index.</p>
<p>When this option is specified in combination with JET_bitStrLimit and the current key column is a text column, this option will take precedence. This option is ignored when the current key column is not a text column. This behavior is intended to allow the type of the current key column to be inferred when building the search key.</p>
<p>If you want to build a similar search key for the start of an index, a similar call to <strong>JetMakeKey</strong> should be made for the key column that is to be the prefix wildcard, but with that no wildcard options specified. The search key is then in an appropriate state to use for such a search. This is analogous to using JET_bitPartialColumnStartLimit, except that the search key is not cleanly finished as it is after the use of a wildcard option.</p>
<p>This option has been deprecated for Windows XP and later releases in order to address this awkward semantic. JET_bitPartialColumnStartLimit and JET_bitPartialColumnEndLimit should be used instead, when possible.</p></td>
</tr>
</tbody>
</table>


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
<td><p>JET_errClientRequestToStopJetService</p></td>
<td><p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errIndexTuplesKeyTooSmall</p></td>
<td><p>The provided column data was too small to build a valid key for the current index because that index is a tuple index and the minimum tuple size was larger than the provided column data. See <a href="gg294099(v=exchg.10).md">JetCreateIndex</a> for more information on tuple indexes. This error will only be returned by Windows XP and later releases.</p></td>
</tr>
<tr class="even">
<td><p>JET_errInstanceUnavailable</p></td>
<td><p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data. This error will only be returned by Windows XP and later releases.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errInvalidBufferSize</p></td>
<td><p>The column data provided did not match the size required by the column definition. This can happen if the column's data type is intrinsically a certain size. This can also happen if the column's data type is not intrinsically a certain size but the column's definition declares it to be of fixed length. One exception to this is that this error will not occur when too little data is provided for a fixed length text column because any missing data will be automatically padded with spaces. A second exception to this is that this error will not occur when too little data is provided for a fixed length binary column because any missing data will be automatically padded with zeroes.</p></td>
</tr>
<tr class="even">
<td><p>JET_errInvalidgrbit</p></td>
<td><p>One of the options requested was invalid, used in an illegal manner, or not implemented. This can happen for <strong>JetMakeKey</strong> when:</p>
<ul>
<li><p>JET_bitPartialColumnStartLimit or JET_bitPartialColumnEndLimit are specified and the corresponding key column is not a text column and is not a variable length binary column. This case only occurs on Windows XP and later releases.</p></li>
<li><p>An attempt is made to use more than one of the following options together: JET_bitPartialColumnStartLimit, JET_bitPartialColumnEndLimit, JET_bitFullColumnStartLimit, and JET_bitFullColumnEndLimit. This case only occurs on Windows XP and later releases.</p></li>
<li><p>An attempt is made to use JET_bitStrLimit or JET_bitSubStrLimit when one of the following options is used: JET_bitPartialColumnStartLimit, JET_bitPartialColumnEndLimit, JET_bitFullColumnStartLimit and JET_bitFullColumnEndLimit. This case only occurs on Windows XP and later releases.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>JET_errInvalidParameter</p></td>
<td><p>One of the parameters provided contained an unexpected value or contained a value that did not make sense when combined with the value of another parameter.</p>
<p>This can happen for <strong>JetMakeKey</strong> when JET_bitNormalizedKey was specified and the value provided in the input buffer was too large to be a valid search key.</p></td>
</tr>
<tr class="even">
<td><p>JET_errKeyIsMade</p></td>
<td><p>The column data provided to <strong>JetMakeKey</strong> was rejected because column data has already been provided for all the key columns in the current index. This can happen in three ways. The first way is if column data is provided for each key column in the current index. The second way is if column data has been provided for at least one key column and a wildcard option was chosen for the last call. The third way is if a previously constructed search key was provided using JET_bitNormalizedKey, which covers all key columns.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errKeyNotMade</p></td>
<td><p>There is no current search key for the cursor. This will happen for <strong>JetMakeKey</strong> if JET_bitNewKey is not specified and a search key has not been constructed for this cursor using a prior call to <strong>JetMakeKey</strong>. The search key will be deleted by a prior call to any navigational API on the cursor other than <a href="gg294117(v=exchg.10).md">JetMove</a>.</p></td>
</tr>
<tr class="even">
<td><p>JET_errNoCurrentIndex</p></td>
<td><p>There is no current index for the cursor. This will happen for <strong>JetMakeKey</strong> if the cursor is on the clustered index of a table, a primary index has not been defined, and JET_bitNormalizedKey was not specified. It is not possible to construct a search key if the cursor is on an index that does not have any key columns unless a previously constructed search key is provided.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errNotInitialized</p></td>
<td><p>It is not possible to complete the operation because the instance associated with the session has not been initialized yet.</p></td>
</tr>
<tr class="even">
<td><p>JET_errRestoreInProgress</p></td>
<td><p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errSessionSharingViolation</p></td>
<td><p>The same session cannot be used for more than one thread at the same time. This error will only be returned by Windows XP and later releases.</p></td>
</tr>
<tr class="even">
<td><p>JET_errTermInProgress</p></td>
<td><p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p></td>
</tr>
</tbody>
</table>


On success, if JET_bitNormalizedKey and JET_bitNewKey were not specified, the search key will have been built up by the search criteria for one more key column in the current index. If JET_bitNormalizedKey was not specified and JET_bitNewKey was specified, any previously existing search key was discarded and a new one will have been built up by the search criteria for the first key column in the current index. If JET_bitNormalizedKey was specified, any previously existing search key was discarded and a new one loaded from the input buffer. In any case, no change to the database state will occur.

On failure, if JET_bitNormalizedKey or JET_bitNewKey was specified, the state of the search key is undefined. If neither JET_bitNormalizedKey nor JET_bitNewKey were specified, no change to the state of the search key will occur. In any case, no change to the database state will occur.

#### Remarks

Keys should be treated as opaque chunks of data. No attempt should be made to exploit the internal structure of this data. However, the following is known about all ESENT keys:

  - Keys may be compared against each other using [memcmp](/previous-versions/visualstudio/visual-studio-6.0/aa246467(v=vs.60)) to establish their relative ordering in the originating index over the table of the source index entries.

  - It is meaningless to compare keys of index entries from different indexes against each other.

  - A key is always less than or equal to JET_cbKeyMost (255) bytes in length prior to Windows Vista. On Windows Vista and later releases, keys can be larger. The maximum size of a key is equal to the current value of JET_paramKeyMost.

Search keys can be one byte longer if a wildcard option was used. In that case, the search key will be up to JET_cbLimitKeyMost (256) bytes for releases prior to Windows Vista and JET_paramKeyMost + 1 bytes for Windows Vista and later releases.

There is a very important ramification to this maximum key size. Whenever there is an index entry that has column values that are large enough to cause a key to be generated for that index that would otherwise be larger than this maximum size, that key is silently truncated at that maximum size. This causes two effects:

  - For entries in a unique index, it will cause entries that would otherwise be unique to be declared as duplicates.

  - For entries in all indexes, key truncation will cause index entries that would otherwise not match the search criteria of a given search key to be declared as matches.

Applications must anticipate this truncation and either avoid it or compensate for its effects. In Windows Vista, a new index flag, JET_bitIndexDisallowTruncation, has been added to make it easier for applications to prevent key truncations. See the [JET_INDEXCREATE](./jet-indexcreate-structure.md) structure for more information on this indexing option.

#### Requirements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Client</strong></p></td>
<td><p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p></td>
</tr>
<tr class="even">
<td><p><strong>Server</strong></p></td>
<td><p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p></td>
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
[JET_GRBIT](./jet-grbit.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JetCreateIndex](./jetcreateindex-function.md)  
[JetRetrieveKey](./jetretrievekey-function.md)  
[JetSeek](./jetseek-function.md)  
[JetSetIndexRange](./jetsetindexrange-function.md)
