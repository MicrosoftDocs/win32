---
description: "Learn more about: JetSetTableSequential Function"
title: JetSetTableSequential Function
TOCTitle: JetSetTableSequential Function
ms:assetid: 874ddd3c-0d69-4d48-b61a-e9e0457426ef
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269323(v=EXCHG.10)
ms:contentKeyID: 32765613
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetSetTableSequential
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

# JetSetTableSequential Function


_**Applies to:** Windows | Windows Server_

## JetSetTableSequential Function

The **JetSetTableSequential** function notifies the database engine that the application is scanning the entire current index that contains a given cursor. Consequently, the methods that are used to access the index data will be tuned to make this scenario as fast as possible.

**Windows XP:**  **JetSetTableSequential** is introduced in Windows XP.

```cpp
    JET_ERR JET_API JetSetTableSequential(
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

A group of bits that specify zero or more of the following options.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitPrereadForward</p> | <p>This option is used to index in the forward direction.</p><p><strong>Windows 7:</strong>  <strong>JET_bitPrereadForward</strong> is introduced in Windows 7.</p> | 
| <p>JET_bitPrereadBackward</p> | <p>This option is used to index in the backward direction.</p><p><strong>Windows 7:</strong>  <strong>JET_bitPrereadBackward</strong> is introduced in Windows 7.</p> | 



### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errClientRequestToStopJetService</p> | <p>The operation cannot complete because all activity on the instance that is associated with the session has been quiesced as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>The operation cannot complete because the instance that is associated with the session encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data.</p><p><strong>Windows XP:</strong>  This return value is introduced in Windows XP.</p> | 
| <p>JET_errNotInitialized</p> | <p>The operation cannot complete because the instance that is associated with the session has not yet been initialized.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>The operation cannot complete because a restore operation is in progress on the instance that is associated with the session.</p> | 
| <p>JET_errTermInProgress</p> | <p>The operation cannot complete because the instance that is associated with the session is being shut down.</p> | 



If this function succeeds, the current index of the cursor is optimized for a sequential scan of the entire index. No change to the database state will occur.

If this function fails, no change to the configuration of the cursor will occur. No change to the database state will occur.

#### Remarks

If the application needs to efficiently scan a known subset of an index, a similar optimization is also performed whenever an index range is established by using [JetSetIndexRange](./jetsetindexrange-function.md). This optimization is only available on Windows XP and later releases.

If the application needs to efficiently scan an unknown subset of an index, no action should be taken. The engine can automatically detect scanning behavior and will fetch data ahead of time. This behavior is not as aggressive, however.

This optimization will make scanning the primary index efficient and will make scanning just the index entry data in a secondary index efficient. It will not make scanning a secondary index while retrieving record data efficient. This is because the engine does not perform a read-ahead on the record data.

#### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista or Windows XP.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008 or Windows Server 2003.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See Also

[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_SESID](./jet-sesid.md)  
[JET_TABLEID](./jet-tableid.md)  
[JetSetIndexRange](./jetsetindexrange-function.md)  
[JetStopService](./jetstopservice-function.md)
