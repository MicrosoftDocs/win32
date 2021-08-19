---
description: "Learn more about: JetGetThreadStats Function"
title: JetGetThreadStats Function
TOCTitle: JetGetThreadStats Function
ms:assetid: 1b8df8cd-fc61-44fe-a15c-a166f7097c32
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269196(v=EXCHG.10)
ms:contentKeyID: 32765499
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetGetThreadStats
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

# JetGetThreadStats Function


_**Applies to:** Windows | Windows Server_

## JetGetThreadStats Function

The **JetGetThreadStats** function retrieves performance information from the database engine for the current thread. Multiple calls can be used to collect statistics that reflect the activity of the database engine on this thread between those calls.

**Windows Vista:**  **JetGetThreadStats** is introduced in Windows Vista.

```cpp
    JET_ERR JET_API JetGetThreadStats(
      __out         void* pvResult,
      __in          unsigned long cbMax
    );
```

### Parameters

*pvResult*

The output buffer which receives the thread statistics data. The buffer contains a [JET_THREADSTATS](./jet-threadstats-structure.md) structure after a successful call.

*cbMax*

The maximum size in bytes of the output buffer.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errBufferTooSmall</p> | <p>The operation failed because the provided output buffer was too small to contain the requested data. The <strong>JetGetThreadStats</strong> function will return this error when the output buffer is too small to contain the smallest version of the <a href="gg269227(v=exchg.10).md">JET_THREADSTATS</a> structure supported by the database engine.</p> | 



On success, the output buffer will contain a [JET_THREADSTATS](./jet-threadstats-structure.md) structure that contains database engine statistics for the current thread.

On failure, the state of the output buffer is undefined.

#### Remarks

The information provided by two consecutive calls of this API are intended to be used to compute the expense of any other database engine operations on the current thread. Generally, this is done by taking a before and after reading of the statistics and subtracting the after count from the before count to get the net count of operations performed.

For example, an application could call **JetGetThreadStats** once to get an initial reading of the statistics for the current thread. It could then call the [JetMove](./jetmove-function.md) function with the *cRow* parameter set to JET_MoveNext to move to the next index entry on an index. It could then call **JetGetThreadStats** again to get another reading of the thread's statistics. It could then subtract the cPageReferenced counter from the second reading from the first. The result would be the number of database pages referenced by the database engine to perform the [JetMove](./jetmove-function.md) operation.

The statistics for each thread are accumulated for the lifetime of that thread. The statistics are reset if the database engine's DLL is unloaded from the host process.

The [JET_THREADSTATS](./jet-threadstats-structure.md) structure will likely be expanded in the future to contain more statistics. New statistics will be added to the end of the structure and can be retrieved with an increased output buffer size. The presence of additional statistics can be inferred by a larger cbStruct value.

#### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See Also

[JET_ERR](./jet-err.md)  
[JET_THREADSTATS](./jet-threadstats-structure.md)  
[JetMove](./jetmove-function.md)
