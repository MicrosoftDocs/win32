---
description: "Learn more about: JetSeek Function"
title: JetSeek Function
TOCTitle: JetSeek Function
ms:assetid: d3d5bfae-dd27-47ab-96c4-6bc9a01a501b
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294103(v=EXCHG.10)
ms:contentKeyID: 32765718
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetSeek
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

# JetSeek Function


_**Applies to:** Windows | Windows Server_

## JetSeek Function

The **JetSeek** function efficiently positions a cursor to an index entry that matches the search criteria specified by the search key in that cursor and the specified inequality. A search key must have been previously constructed using [JetMakeKey](./jetmakekey-function.md).

```cpp
    JET_ERR JET_API JetSeek(
      __in          JET_SESID sesid,
      __in          JET_TABLEID tableid,
      __in          JET_GRBIT grbit
    );
```

### Parameters

*sesid*

The session to use for this call.

*tableid*

The cursor to use for this call.

*grbit*

A group of bits that contain the options to be used for this call. *Grbit* must be nonzero and must include one or more of the values listed in the following table.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitCheckUniqueness</p> | <p>A special error code, JET_wrnUniqueKey, will be returned if it can be cheaply determined that there is exactly one index entry that matches the search key.</p><p>This option is ignored unless JET_bitSeekEQ is also specified.</p><p>This option is only available on Windows Server 2003 and later releases.</p> | 
| <p>JET_bitSeekEQ</p> | <p>The cursor will be positioned at the index entry closest to the start of the index that exactly matches the search key. The start of the index is the index entry that is found when moving to the first record in that index. The start of the index is not the same as the low end of the index, which can change depending on the sort order of the key columns in the index.</p><p>It is not meaningful to use this option with a search key that was constructed using <a href="gg269329(v=exchg.10).md">JetMakeKey</a> using a wildcard option.</p> | 
| <p>JET_bitSeekGE</p> | <p>The cursor will be positioned at the index entry closest to the start of the index that is greater than or equal to an index entry that would exactly match the search criteria. The start of the index is the index entry that is found when moving to the first record in that index. The start of the index is not the same as the low end of the index, which can change depending on the sort order of the key columns in the index.</p><p>It is not meaningful to use this option with a search key that was constructed using <a href="gg269329(v=exchg.10).md">JetMakeKey</a> using a wildcard option intended to find index entries closest to the end of the index.</p> | 
| <p>JET_bitSeekGT</p> | <p>The cursor will be positioned at the index entry closest to the start of the index that is greater than an index entry that would exactly match the search criteria. The start of the index is the index entry that is found when moving to the first record in that index. The start of the index is not the same as the low end of the index, which can change depending on the sort order of the key columns in the index.</p><p>It is not meaningful to use this option with a search key that was constructed using <a href="gg269329(v=exchg.10).md">JetMakeKey</a> using a wildcard option intended to find index entries closest to the start of the index.</p> | 
| <p>JET_bitSeekLE</p> | <p>The cursor will be positioned at the index entry closest to the end of the index that is less than or equal to an index entry that would exactly match the search criteria. The end of the index is the index entry that is found when moving to the last record in that index. The end of the index is not the same as the high end of the index, which can change depending on the sort order of the key columns in the index.</p><p>It is not meaningful to use this option with a search key that was constructed using <a href="gg269329(v=exchg.10).md">JetMakeKey</a> using a wildcard option intended to find index entries closest to the start of the index.</p> | 
| <p>JET_bitSeekLT</p> | <p>The cursor will be positioned at the index entry closest to the end of the index that is less than an index entry that would exactly match the search criteria. The end of the index is the index entry that is found when moving to the last record in that index. The end of the index is not the same as the high end of the index, which can change depending on the sort order of the key columns in the index.</p><p>It is not meaningful to use this option with a search key that was constructed using <a href="gg269329(v=exchg.10).md">JetMakeKey</a> using a wildcard option intended to find index entries closest to the end of the index.</p> | 
| <p>JET_bitSetIndexRange</p> | <p>An index range will automatically be setup for all keys that exactly match the search key. The resulting index range is identical to one that would have otherwise been created by a call to <a href="gg294112(v=exchg.10).md">JetSetIndexRange</a> with the JET_bitRangeInclusive and JET_bitRangeUpperLimit options. See <a href="gg294112(v=exchg.10).md">JetSetIndexRange</a> for more information.</p><p>This is a convenient method for discovering all the index entries that match the same search criteria.</p><p>This option is ignored unless JET_bitSeekEQ is also specified.</p> | 



### Return Value

This function allows for the return of any [JET_ERRs](./jet-err.md) that are defined in this API. For more information about Jet errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p><p>For <strong>JetSeek</strong>, this means that an index entry was found that exactly matched the search criteria.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data.</p><p>This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errKeyNotMade</p> | <p>There is no current search key for the cursor. <strong>JetSeek</strong> requires that the cursor have a valid search key because it will use that for the search criteria used to find index entries.</p> | 
| <p>JET_errNotInitialized</p> | <p>It is not possible to complete the operation because the instance associated with the session has not been initialized yet.</p> | 
| <p>JET_errRecordNotFound</p> | <p>No index entry was found that matched the search criteria.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p> | 
| <p>JET_wrnSeekNotEqual</p> | <p>An index entry was found that matched the search criteria. However, that index entry was not an exact match.</p> | 
| <p>JET_errSessionSharingViolation</p> | <p>The same session cannot be used for more than one thread at the same time.</p><p>This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errTermInProgress</p> | <p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p> | 
| <p>JET_wrnUniqueKey</p> | <p>Exactly one index entry was found that exactly matched the search criteria. This error will only be returned if JET_bitSeekCheckUniqueness was specified and it was cheap to determine that the matching index entry was the only index entry that exactly matches the search criteria.</p><p>This error will only be returned by Windows Server 2003 and later releases.</p> | 



On success, the cursor will be positioned at an index entry that matches the search criteria. If a record has been prepared for update, then that update will be canceled. If an index range is in effect, that index range will be canceled. If a search key has been constructed for the cursor, then that search key will be deleted. No change to the database state will occur. When multiple index entries have the same value, the entry closest to the start of the index is always selected.

On failure, the position of the cursor will remain unchanged unless JET_errRecordNotFound was returned. In that case, the cursor will be positioned where the index entry that matched the search criteria specified by the search key in that cursor and the specified inequality would have been. The cursor can be moved relative to that position but is still not on a valid index entry. If a record has been prepared for update, then that update will be canceled. If an index range is in effect, that index range will be canceled. If a search key has been constructed for the cursor, then that search key will be deleted. No change to the database state will occur.

#### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See Also

[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JetMakeKey](./jetmakekey-function.md)  
[JetSetIndexRange](./jetsetindexrange-function.md)  
[JetStopService](./jetstopservice-function.md)
