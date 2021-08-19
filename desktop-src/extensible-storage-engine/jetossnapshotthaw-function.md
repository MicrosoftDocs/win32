---
description: "Learn more about: JetOSSnapshotThaw Function"
title: JetOSSnapshotThaw Function
TOCTitle: JetOSSnapshotThaw Function
ms:assetid: 3b001113-6299-4082-ab15-461f2e33e996
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269229(v=EXCHG.10)
ms:contentKeyID: 32765531
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetOSSnapshotThaw
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

# JetOSSnapshotThaw Function


_**Applies to:** Windows | Windows Server_

## JetOSSnapshotThaw Function

The **JetOSSnapshotThaw** function notifies the engine that it can resume normal IO operations after a freeze period and a successful snapshot.

**Windows XP:**  **JetOSSnapshotThaw** is introduced in Windows XP.

```cpp
    JET_ERR JET_API JetOSSnapshotThaw(
      __in          const JET_OSSNAPID snapId,
      __in          const JET_GRBIT grbit
    );
```

### Parameters

*snapId*

The identifier of the snapshot session.

*grbit*

This parameter is reserved for future use and the only valid value supported is 0.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errInvalidParameter</p> | <p>The snapshot session is invalid or the <em>grbit</em> parameter is invalid.</p> | 
| <p>JET_errOSSnapshotTimeOut</p> | <p>The snapshot session had an internal timeout before this call occurred. Consequently, IO operations returned to normal before this call was made.</p> | 
| <p>JET_errOSSnapshotInvalidSnapId</p> | <p>The identifier for snapshot session is not valid.</p> | 



If this function succeeds, a snapshot session ends and the normal engine behavior resumes. A new snapshot session can be started later.

If this function fails, the current snapshot session ends but the freeze of IOs during the snapshot period was not respected internally.

#### Remarks

Event log entries will be generated for the different steps of the snapshot.

#### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista or Windows XP.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008 or Windows Server 2003.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See Also

[JET_ERR](./jet-err.md)  
[JET_OSSNAPID](./jet-ossnapid.md)  
[JetOSSnapshotAbort](./jetossnapshotabort-function.md)  
[JetOSSnapshotFreeze](./jetossnapshotfreeze-function.md)  
[JetOSSnapshotPrepare](./jetossnapshotprepare-function.md)
