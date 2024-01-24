---
description: "Learn more about: JetSetCurrentIndex4 Function"
title: JetSetCurrentIndex4 Function
TOCTitle: JetSetCurrentIndex4 Function
ms:assetid: 6076d02c-5701-4021-ba0a-da36bff166d1
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269262(v=EXCHG.10)
ms:contentKeyID: 32765564
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetSetCurrentIndex4W
- JetSetCurrentIndex4A
- JetSetCurrentIndex4
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

# JetSetCurrentIndex4 Function


_**Applies to:** Windows | Windows Server_

## JetSetCurrentIndex4 Function

The **JetSetCurrentIndex4** function is used to set the current index of a cursor. The current index of a cursor defines which records in a table are visible to that cursor and the order in which they appear by selecting the set of index entries to use to expose those records.

```cpp
    JET_ERR JET_API JetSetCurrentIndex4(
      __in          JET_SESID sesid,
      __in          JET_TABLEID tableid,
      __in_opt      JET_PCSTR szIndexName,
      __in_opt      JET_INDEXID* pindexid,
      __in          JET_GRBIT grbit,
      __in          unsigned long itagSequence
    );
```

### Parameters

*sesid*

The session to use for this call.

*tableid*

The cursor to use for this call.

*szIndexName*

The name of the index to be selected for the cursor. If this parameter is NULL or an empty string then the clustered index will be selected. If a primary index is defined for the table then that index will be selected because it is the same as the clustered index. If no primary index is defined for the table then the sequential index will be selected. The sequential index has no index definition. See [JetCreateIndex](./jetcreateindex-function.md) for more information.

If *pindexid* is not NULL then the index name will be ignored and the index will be selected by its index ID.

*pindexid*

The ID of the index to be selected for the cursor.

The index ID is a volatile, opaque handle that can be used to quickly select an index. This ID can be retrieved using JetGetIndexInfo or JetGetTableIndexInfo using the JET_IdxInfoIndexId option.

If *pindexid* is NULL then the index will be selected by its index name and the index ID will be ignored.

When this parameter is not present, its value is presumed to be NULL.

*grbit*

A group of bits that contain the options to be used for this call, which include zero or more of the following.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitMoveFirst</p> | <p>This option indicates that the cursor should be positioned on the first entry of the specified index. If the clustered index is being selected (primary index or sequential index) and the current index is a secondary index then JET_bitMoveFirst is assumed. If the current index is being selected then this option is ignored and no change to the cursor position is made.</p> | 
| <p>JET_bitNoMove</p> | <p>This option indicates that the cursor should be positioned on the index entry of the new index that corresponds to the record associated with the index entry at the current position of the cursor on the old index.</p><p>If the definition for the new index contains at least one multi-valued key column then the destination index entry is ambiguous. In this case, the specified <em>itagSequence</em> is used to select which multi-value of the most significant multi-valued key column is used to position the cursor. It is only necessary to pass a single <em>itagSequence</em> even in the case of multiple multi-valued key columns because the engine only expands all values for the most significant multi-valued key column. See <a href="gg294099(v=exchg.10).md">JetCreateIndex</a> for more details.</p><p>If JET_bitMoveFirst is specified then this option is ignored.</p><p>If the current index is being selected then this option is ignored and no change to the cursor position is made. When this parameter is not present, its value is presumed to be JET_bitMoveFirst.</p> | 



*itagSequence*

Sequence number of the multi-valued column value which will be used to position the cursor on the new index.

This parameter is only used in conjunction with JET_bitNoMove. See the description of this option for more details.

When this parameter is not present or is set to zero, its value is presumed to be 1.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errBadItagSequence</p> | <p>A secondary index is being selected with the JET_bitNoMove option and there is no value for the first multi-valued key column in the definition for the new index that corresponds to the specified sequence number.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data.</p><p>This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errInvalidIndexId</p> | <p>The contents of the index ID were not valid or have expired and need to be refreshed. This can happen for <strong>JetSetCurrentIndex4</strong> when:</p><ul><li><p>pindexid-&gt;cbStruct is not of the expected size (Windows Server 2003 and later releases).</p></li><li><p>The engine has been shut down since the index ID was fetched.</p></li><li><p>All cursors referencing the table containing the index corresponding to the index ID have been closed and the engine has evicted that index's definition from the schema cache.</p></li><li><p>The index ID is being used with a cursor opened on the wrong table.</p></li><li><p>The index has been dropped or is not yet visible to the session.</p></li></ul> | 
| <p>JET_errInvalidName</p> | <p>One of the specified object names was invalid. All object names must conform to the same set of rules. These rules are as follows:</p><ul><li><p>Object names must be composed of ASCII characters.</p></li><li><p>Object names must be at least one character in length.</p></li><li><p>Object names may not exceed JET_cbNameMost (64) characters in length.</p></li><li><p>Object names may not begin with a space.</p></li><li><p>Object names may not contain ASCII control characters (0x00 through 0x1F).</p></li><li><p>Object names may not contain an exclamation point (!), period (.), left bracket ([), or right bracket (]) character.</p></li><li><p>Once validated, only the portion of the string up to the first space (if any) will be used for the object name. This effectively means that object names may not contain a space either.</p></li></ul> | 
| <p>JET_errInvalidParameter</p> | <p>One of the parameters provided contained an unexpected value or contained a value that did not make sense when combined with the value of another parameter. This can happen for <strong>JetSetCurrentIndex4</strong> when <em>pindexid</em> is not NULL and pindexid-&gt;cbStruct is not of the expected size (Windows XP and earlier releases).</p> | 
| <p>JET_errNoCurrentRecord</p> | <p>A secondary index is being selected with the JET_bitNoMove option and there is no index entry in the new index that corresponds to the record associated with the index entry at the current position of the cursor on the old index.</p> | 
| <p>JET_errNotInitialized</p> | <p>It is not possible to complete the operation because the instance associated with the session has not been initialized yet.</p> | 
| <p>JET_errOutOfCursors</p> | <p>The engine has exhausted its pool of resources used to open cursors. The maximum number of cursors that can be opened at any one time is controlled using <a href="gg269201(v=exchg.10).md">JET_paramMaxCursors</a>. See <a href="gg294044(v=exchg.10).md">JetSetSystemParameter</a> for more information. This can happen for <strong>JetSetCurrentIndex4</strong> when a secondary index has been selected and the engine cannot open an internal cursor to use that index.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p> | 
| <p>JET_errSessionSharingViolation</p> | <p>The same session cannot be used for more than one thread at the same time.</p><p>This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errTermInProgress</p> | <p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p> | 



On success, the current index of the cursor is set to the requested index. Index entries may now be sought using [JetSeek](./jetseek-function.md) according to the index definition of the requested index. Index entries may also be enumerated using [JetMove](./jetmove-function.md) in the order specified by that index definition. The current position of the cursor is either set to the first index entry on the index (JET_bitMoveFirst) or to a specific index entry that is related to the current position of the cursor on the old index (JET_bitNoMove). No change to the database state will occur.

On failure, the current index and current position of the cursor are in an undefined state. No change to the database state will occur.

#### Remarks

If the index ID hint is stale then the API simply fails. There is no fallback to the text name of the index in this case as one might expect. This fallback must be done manually by the caller of the API.

#### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JetSetCurrentIndex4W</strong> (Unicode) and <strong>JetSetCurrentIndex4A</strong> (ANSI).</p> | 



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
[JetSeek](./jetseek-function.md)  
[JetSetSystemParameter](./jetsetsystemparameter-function.md)
