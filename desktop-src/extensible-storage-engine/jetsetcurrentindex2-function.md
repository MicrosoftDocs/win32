---
description: "Learn more about: JetSetCurrentIndex2 Function"
title: JetSetCurrentIndex2 Function
TOCTitle: JetSetCurrentIndex2 Function
ms:assetid: da94465e-bd35-45c2-9ccc-1d2e8c34aa9a
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294110(v=EXCHG.10)
ms:contentKeyID: 32765725
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetSetCurrentIndex2W
- JetSetCurrentIndex2A
- JetSetCurrentIndex2
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

# JetSetCurrentIndex2 Function


_**Applies to:** Windows | Windows Server_

## JetSetCurrentIndex2 Function

The **JetSetCurrentIndex2** function sets the current index of a cursor that defines which records in a table are visible to that cursor and the order in which they appear by selecting the set of index entries to use to expose those records.

```cpp
    JET_ERR JET_API JetSetCurrentIndex2(
      __in          JET_SESID sesid,
      __in          JET_TABLEID tableid,
      __in_opt      JET_PCSTR szIndexName,
      __in          JET_GRBIT grbit
    );
```

### Parameters

*sesid*

The session to use for this call.

*tableid*

The cursor to use for this call.

*szIndexName*

The name of the index to be selected for the cursor.

If this parameter is NULL or an empty string then the clustered index will be selected. If a primary index is defined for the table then that index will be selected because it is the same as the clustered index. If no primary index is defined for the table then the sequential index will be selected. The sequential index has no index definition. See [JetCreateIndex](./jetcreateindex-function.md) for more information.

If *pindexid* is not NULL then the index name will be ignored and the index will be selected by its index ID.

*grbit*

A group of bits that contain the options to be used for this call, which include zero or more of the following.

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
<td><p>JET_bitMoveFirst</p></td>
<td><p>This option indicates that the cursor should be positioned on the first entry of the specified index. If the clustered index is being selected (primary index or sequential index) and the current index is a secondary index then JET_bitMoveFirst is assumed. If the current index is being selected then this option is ignored and no change to the cursor position is made.</p></td>
</tr>
<tr class="even">
<td><p>JET_bitNoMove</p></td>
<td><p>This option indicates that the cursor should be positioned on the index entry of the new index that corresponds to the record associated with the index entry at the current position of the cursor on the old index.</p>
<p>If the definition for the new index contains at least one multi-valued key column then the destination index entry is ambiguous. In this case, the specified <em>itagSequence</em> is used to select which multi-value of the most significant multi-valued key column is used to position the cursor. It is only necessary to pass a single <em>itagSequence</em> even in the case of multiple multi-valued key columns because the engine only expands all values for the most significant multi-valued key column. See <a href="gg294099(v=exchg.10).md">JetCreateIndex</a> for more details.</p>
<p>If JET_bitMoveFirst is specified then this option is ignored.</p>
<p>If the current index is being selected then this option is ignored and no change to the cursor position is made. When this parameter is not present, its value is presumed to be JET_bitMoveFirst.</p></td>
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
<td><p>JET_errBadItagSequence</p></td>
<td><p>A secondary index is being selected with the JET_bitNoMove option and there is no value for the first multi-valued key column in the new definition for the index that corresponds to the specified sequence number.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errClientRequestToStopJetService</p></td>
<td><p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p></td>
</tr>
<tr class="even">
<td><p>JET_errInstanceUnavailable</p></td>
<td><p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data.</p>
<p>This error will only be returned by Windows XP and later releases.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errInvalidIndexId</p></td>
<td><p>The contents of the index ID were not valid or have expired and need to be refreshed. This can happen for <strong>JetSetCurrentIndex2</strong> when:</p>
<ul>
<li><p>pindexid-&gt;cbStruct is not of the expected size (Windows Server 2003 and later releases).</p></li>
<li><p>The engine has been shut down since the index ID was fetched.</p></li>
<li><p>All cursors referencing the table containing the index corresponding to the index ID have been closed and the engine has evicted the definition for the index from the schema cache.</p></li>
<li><p>The index ID is being used with a cursor opened on the wrong table.</p></li>
<li><p>The index has been dropped or is not yet visible to the session.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>JET_errInvalidName</p></td>
<td><p>One of the specified object names was invalid. All object names must conform to the same set of rules. These rules are as follows:</p>
<ul>
<li><p>Object names must be composed of ASCII characters.</p></li>
<li><p>Object names must be at least one character in length.</p></li>
<li><p>Object names may not exceed JET_cbNameMost (64) characters in length.</p></li>
<li><p>Object names may not begin with a space.</p></li>
<li><p>Object names may not contain ASCII control characters (0x00 through 0x1F).</p></li>
<li><p>Object names may not contain an exclamation point (!), period (.), left bracket ([), or right bracket (]) character.</p></li>
<li><p>Once validated, only the portion of the string up to the first space (if any) will be used for the object name. This effectively means that object names may not contain a space either.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>JET_errInvalidParameter</p></td>
<td><p>One of the parameters provided contained an unexpected value or contained a value that did not make sense when combined with the value of another parameter. This can happen for <strong>JetSetCurrentIndex2</strong> when <em>pindexid</em> is not NULL and pindexid-&gt;cbStruct is not of the expected size (Windows XP and earlier releases).</p></td>
</tr>
<tr class="even">
<td><p>JET_errNoCurrentRecord</p></td>
<td><p>A secondary index is being selected with the JET_bitNoMove option and there is no index entry in the new index that corresponds to the record associated with the index entry at the current position of the cursor on the old index.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errNotInitialized</p></td>
<td><p>It is not possible to complete the operation because the instance associated with the session has not been initialized yet.</p></td>
</tr>
<tr class="even">
<td><p>JET_errOutOfCursors</p></td>
<td><p>The engine has exhausted its pool of resources used to open cursors. The maximum number of cursors that can be opened at any one time is controlled using <a href="gg269201(v=exchg.10).md">JET_paramMaxCursors</a>. See <a href="gg294044(v=exchg.10).md">JetSetSystemParameter</a> for more information. This can happen for <strong>JetSetCurrentIndex2</strong> when a secondary index has been selected and the engine cannot open an internal cursor to use that index.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errRestoreInProgress</p></td>
<td><p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p></td>
</tr>
<tr class="even">
<td><p>JET_errSessionSharingViolation</p></td>
<td><p>The same session cannot be used for more than one thread at the same time.</p>
<p>This error will only be returned by Windows XP and later releases.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errTermInProgress</p></td>
<td><p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p></td>
</tr>
</tbody>
</table>


On success, the current index of the cursor is set to the requested index. Index entries may now be sought using [JetSeek](./jetseek-function.md) according to the index definition of the requested index. Index entries may also be enumerated using [JetMove](./jetmove-function.md) in the order specified by that index definition. The current position of the cursor is either set to the first index entry on the index (JET_bitMoveFirst) or to a specific index entry that is related to the current position of the cursor on the old index (JET_bitNoMove). No change to the database state will occur.

On failure, the current index and current position of the cursor are in an undefined state. No change to the database state will occur.

#### Remarks

If the index ID hint is stale then the API simply fails. There is no fallback to the text name of the index in this case as one might expect. This fallback must be done manually by the caller of the API.

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
<tr class="even">
<td><p><strong>Unicode</strong></p></td>
<td><p>Implemented as <strong>JetSetCurrentIndex2W</strong> (Unicode) and <strong>JetSetCurrentIndex2A</strong> (ANSI).</p></td>
</tr>
</tbody>
</table>


#### See Also

[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JET_INDEXID](./jet-indexid-structure.md)  
[JetCreateIndex](./jetcreateindex-function.md)  
[JetGetCurrentIndex](./jetgetcurrentindex-function.md)  
[JetGetIndexInfo](./jetgetindexinfo-function.md)  
[JetGetTableIndexInfo](./jetgettableindexinfo-function.md)  
[JetMove](./jetmove-function.md)  
[JetSetSystemParameter](./jetsetsystemparameter-function.md)  
[JetSeek](./jetseek-function.md)  
[JetStopService](./jetstopservice-function.md)
