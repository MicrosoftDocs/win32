---
description: "Learn more about: JetSetIndexRange Function"
title: JetSetIndexRange Function
TOCTitle: JetSetIndexRange Function
ms:assetid: dac99576-707d-4713-9825-ddad1980723e
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294112(v=EXCHG.10)
ms:contentKeyID: 32765726
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetSetIndexRange
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

# JetSetIndexRange Function


_**Applies to:** Windows | Windows Server_

## JetSetIndexRange Function

The **JetSetIndexRange** function temporarily limits the set of index entries that the cursor can walk using [JetMove](./jetmove-function.md) to those starting from the current index entry and ending at the index entry that matches the search criteria specified by the search key in that cursor and the specified bound criteria. A search key must have been previously constructed using [JetMakeKey](./jetmakekey-function.md).

```cpp
    JET_ERR JET_API JetSetIndexRange(
      __in          JET_SESID sesid,
    __in          JET_TABLEID tableidSrc,
      __in          JET_GRBIT grbit
    );
```

### Parameters

*sesid*

The session to use for this call.

*tableidSrc*

The cursor to use for this call.

*grbit*

A group of bits that contain the options to be used for this call, which include zero or more of the following:


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitRangeInclusive</p> | <p>This presence or absence of this option indicates the boundary criteria of the index range. When present, this option indicates that the limit of the index range is inclusive. When absent, this option indicates that the limit of the index range is exclusive. When the limit of the index range is inclusive then any index entries exactly matching the search criteria are included in the range.</p> | 
| <p>JET_bitRangeInstantDuration</p> | <p>This option requests that the index range be removed as soon as it has been established. All other aspects of the operation remain unchanged. This is useful for testing for the existence of index entries that match the search criteria.</p> | 
| <p>JET_bitRangeRemove</p> | <p>This option requests that an existing index range on the cursor be canceled. Once the index range is canceled, it will be possible to move beyond the end of the index range using <a href="gg294117(v=exchg.10).md">JetMove</a>. If an index range is not already in effect, then <strong>JetSetIndexRange</strong> will fail with JET_errInvalidOperation.</p><p>When this option is specified, all other options are ignored.</p> | 
| <p>JET_bitRangeUpperLimit</p> | <p>If this option is used, then the search key in the cursor represents the search criteria for the index entry closest to the end of the index that will match the index range. The index range will be established between the current position of the cursor and this index entry so that all matches can be found by walking forward on the index using <a href="gg294117(v=exchg.10).md">JetMove</a> with JET_MoveNext or a positive offset.</p><p>It is not meaningful to use this option with a search key that was constructed using <a href="gg269329(v=exchg.10).md">JetMakeKey</a> using a wildcard option intended to find index entries closest to the start of the index.</p><p>If this option is omitted, then the search key in the cursor represents the search criteria for the index entry closest to the start of the index that will match the index range. The index range will be established between the current position of the cursor and this index entry so that all matches can be found by walking backward on the index using <a href="gg294117(v=exchg.10).md">JetMove</a> with JET_MovePrevious or a negative offset.</p><p>It is not meaningful to omit this option with a search key that was constructed using <a href="gg269329(v=exchg.10).md">JetMakeKey</a> using a wildcard option intended to find index entries closest to the end of the index.</p> | 



### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p><p>For <strong>JetSetIndexRange</strong>, this means that either an existing index range was canceled or that there is at least one index entry inside of the index range.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data.</p><p>This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errInvalidOperation</p> | <p>This error will be returned by <strong>JetSetIndexRange</strong> when JET_bitRangeRemove was specified and no index range was in effect.</p> | 
| <p>JET_errKeyNotMade</p> | <p>There is no current search key for the cursor. <strong>JetSetIndexRange</strong> requires that the cursor have a valid search key because it will use that for the search criteria used to find index entries.</p> | 
| <p>JET_errNoCurrentIndex</p> | <p>There is no current index for the cursor. This will happen for <strong>JetSetIndexRange</strong> if the cursor is on the clustered index of a table, a primary index has not been defined. Setting an index range over such an index is not supported.</p> | 
| <p>JET_errNoCurrentRecord</p> | <p>This error will be returned by <strong>JetSetIndexRange</strong> to indicate that there are no index entries inside the index range.</p> | 
| <p>JET_errNotInitialized</p> | <p>It is not possible to complete the operation because the instance associated with the session has not been initialized yet.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p> | 
| <p>JET_errSessionSharingViolation</p> | <p>The same session cannot be used for more than one thread at the same time.</p><p>This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errTermInProgress</p> | <p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p> | 



On success, if JET_bitRangeRemove is specified, then the index range that is currently in effect is canceled. If JET_bitRangeRemove is not specified and JET_bitRangeInstantDuration is specified, then no index range is in effect. If neither JET_bitRangeRemove nor JET_bitRangeInstantDuration is specified, then a new index range is in effect. This index range will temporarily limit the set of index entries that the cursor can walk using [JetMove](./jetmove-function.md) to those starting from the current index entry and ending at the index entry that matches the search criteria. The position of the cursor will remain unchanged. If a search key has been constructed for the cursor, then that search key will be deleted. No change to the database state will occur.

On failure, if JET_errNoCurrentRecord is not returned, then no index range is in effect. If JET_errNoCurrentRecord is returned, then a new index range is in effect. This index range will temporarily limit the set of index entries that the cursor can walk using [JetMove](./jetmove-function.md) to those starting from the current index entry and ending at the index entry that matches the search criteria. The position of the cursor will remain unchanged. If JET_errNoCurrentRecord was returned and a search key has been constructed for the cursor, then that search key will be deleted. No change to the database state will occur.

#### Remarks

An index range is volatile and will automatically be canceled if any navigation other than [JetMove](./jetmove-function.md) is performed on the cursor.

Index ranges only work in one direction. If an upper limit is established then only forward motion using [JetMove](./jetmove-function.md) with JET_MoveNext or a positive offset will be prevented once the end of the index range has been reached. It is still possible to leave the index range in this case using [JetMove](./jetmove-function.md) with JET_MovePrevious or a negative offset. An analogous situation occurs for a lower limit.

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
[JetMove](./jetmove-function.md)  
[JetSetIndexRange]()  
[JetStopService](./jetstopservice-function.md)
