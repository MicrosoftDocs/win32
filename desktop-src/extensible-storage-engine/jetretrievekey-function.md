---
description: "Learn more about: JetRetrieveKey Function"
title: JetRetrieveKey Function
TOCTitle: JetRetrieveKey Function
ms:assetid: a96d0a7c-f1db-48bc-807d-4e6357aec726
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294051(v=EXCHG.10)
ms:contentKeyID: 32765650
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetRetrieveKey
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

# JetRetrieveKey Function


_**Applies to:** Windows | Windows Server_

## JetRetrieveKey Function

The **JetRetrieveKey** function retrieves the key for the index entry at the current position of a cursor. Such keys are constructed by calls to [JetMakeKey](./jetmakekey-function.md). The retrieved key can then be used to efficiently return that cursor to the same index entry by a call to [JetSeek](./jetseek-function.md).

```cpp
    JET_ERR JET_API JetRetrieveKey(
      __in          JET_SESID sesid,
      __in          JET_TABLEID tableid,
      __out_opt     void* pvData,
      __in          unsigned long cbMax,
      __out_opt     unsigned long* pcbActual,
      __in          JET_GRBIT grbit
    );
```

### Parameters

*sesid*

The session to use for this call.

*tableid*

The cursor to use for this call.

*pvData*

The output buffer that will receive the key.

*cbMax*

The maximum size in bytes of the output buffer.

*pcbActual*

Receives the actual size in bytes of the key.

If this parameter is NULL then the actual size of the key will not be returned.

If the output buffer is too small, then the actual size of the key will still be returned. That means that this number will be larger than the size of the output buffer.

*grbit*

A group of bits that contain the options to be used for this call, which include zero or more of the following.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitRetrieveCopy</p> | <p>When specified, the engine will return the search key for the cursor. The search key is built up using one or more prior calls to <a href="gg269329(v=exchg.10).md">JetMakeKey</a> for the purposes of seeking to that key using <a href="gg294103(v=exchg.10).md">JetSeek</a> or setting an index range using <a href="gg294112(v=exchg.10).md">JetSetIndexRange</a>.</p> | 



### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data. This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errKeyNotMade</p> | <p>There is no current search key for the cursor. This will happen for <strong>JetRetrieveKey</strong> if JET_bitRetrieveCopy is specified and a search key has not been constructed for this cursor using a prior call to <a href="gg269329(v=exchg.10).md">JetMakeKey</a>. The search key will be deleted by a prior call to any navigational API on the cursor other than <a href="gg294117(v=exchg.10).md">JetMove</a>.</p> | 
| <p>JET_errNoCurrentRecord</p> | <p>The cursor is not positioned on a record. This can happen for many different reasons. For example, this will happen if the cursor is currently positioned after the last record on the current index.</p> | 
| <p>JET_errNotInitialized</p> | <p>It is not possible to complete the operation because the instance associated with the session has not been initialized yet.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p> | 
| <p>JET_errSessionSharingViolation</p> | <p>The same session cannot be used for more than one thread at the same time. This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errTermInProgress</p> | <p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p> | 
| <p>JET_wrnBufferTruncated</p> | <p>The operation completed successfully, but the output buffer was too small to receive the entire key. The output buffer has been filled with as much of the key as would fit. The actual size of the key has also been returned, if requested.</p><p><strong>Note</strong>   This error will not be returned if JET_bitRetrieveCopy is specified. Please see the Remarks section for more information.</p> | 



On success, the key for the index entry at the current position of a cursor will be returned in the output buffer. If JET_wrnBufferTruncated is returned then the output buffer will contain as much of the key as will fit in the space provided and the actual size of the key will be accurate. No change to the database state will occur.

On failure, the state of the output buffer and the actual size of the key will be undefined. No change to the database state will occur.

#### Remarks

Keys should generally be treated as opaque chunks of data. No attempt should be made to exploit the internal structure of this data. However, the following properties can be known about all ESENT keys:

  - Keys may be compared against each other using [memcmp](https://msdn.microsoft.com/library/aa246467\(vs.60\).aspx) function to establish their relative ordering in the originating index over the table of the source index entries.

  - It is meaningless to compare keys of index entries from different indexes against each other.

  - A key is always less than or equal to JET_cbKeyMost (255) bytes in length prior to Windows Vista. On Windows Vista and later releases, keys can be larger. The maximum size of a key is equal to the current value of JET_paramKeyMost.

In addition to the above properties of ESENT keys in general, it is important to note that a search key is different from the key for an index entry. Specifically, a search key may be longer than an ordinary key. This extra length occurs when a wildcard option is used while constructing the search key. See [JetMakeKey](./jetmakekey-function.md) for more information.

There is an important bug in this API that is present in all releases. If the search key is requested using the use of JET_bitRetrieveCopy and the output buffer is too small to receive the entire key then JET_wrnBufferTruncated will NOT be returned. JET_errSuccess will be returned instead. It is important to verify that the actual size of the key as returned using *pcbActual* is less than or equal to the size of the output buffer. If the actual size is larger than the size of the output buffer, then the caller of **JetRetrieveKey** should react as if JET_wrnBufferTruncated were returned instead.

#### Requirements


| 
|
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
[JetSeek](./jetseek-function.md)  
[JetSetIndexRange](./jetsetindexrange-function.md)
