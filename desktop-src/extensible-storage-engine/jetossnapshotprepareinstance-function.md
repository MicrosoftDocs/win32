---
description: "Learn more about: JetOSSnapshotPrepareInstance Function"
title: JetOSSnapshotPrepareInstance Function
TOCTitle: JetOSSnapshotPrepareInstance Function
ms:assetid: b4f06342-633f-47c6-be32-64ec058920fe
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294064(v=EXCHG.10)
ms:contentKeyID: 32765679
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetOSSnapshotPrepareInstance
topic_type: 
- kbArticle
- apiref
api_type: 
- DLLExport
- COM
api_location: 
- ESENT.DLL
ROBOTS: INDEX,FOLLOW

---

# JetOSSnapshotPrepareInstance Function


_**Applies to:** Windows | Windows Server_

## JetOSSnapshotPrepareInstance Function

The **JetOSSnapshotPrepareInstance** function selects a specific instance to be part of the snapshot session.

**Windows Vista:** **JetOSSnapshotPrepareInstance** was introduced in Windows Vista.

```cpp
JET_ERR JET_API JetOSSnapshotPrepareInstance(
  __in          JET_OSSNAPID snapId,
  __in          JET_INSTANCE instance,
  __in          const JET_GRBIT grbit
);
```

### Parameters

*snapId*

The identifier of the snapshot session.

*instance*

The instance that will be used for this call.

*grbit*

The options for this call. This parameter is reserved for future use. The only valid value is 0 (zero).

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errInvalidParameter</p> | <p>The snapshot id pointer is <strong>NULL</strong> or the <em>grbit</em> parameter is invalid.</p> | 
| <p>JET_errOSSnapshotInvalidSequence</p> | <p>A snapshot session is already in progress.</p> | 
| <p>JET_errOSSnapshotInvalidSnapId</p> | <p>The identifier for the snapshot session is not valid.</p> | 



If this function succeeds, the specified instance will be part of the snapshot session.

If this function fails, no change in the engine state occurs.

#### Remarks

The normal API sequence call is: [JetOSSnapshotPrepare](./jetossnapshotprepare-function.md), optionally followed by one or more calls to **JetOSSnapshotPrepareInstance**, then followed by [JetOSSnapshotFreeze](./jetossnapshotfreeze-function.md). Once the freeze is started, it can be terminated using [JetOSSnapshotThaw](./jetossnapshotthaw-function.md). At any time after the prepare, the snapshot session can be abruptly terminated with [JetOSSnapshotAbort](./jetossnapshotabort-function.md). Event log entries will be generated for the different steps of the snapshot.

If **JetOSSnapshotPrepareInstance** is not called between the start of the session ([JetOSSnapshotPrepare](./jetossnapshotprepare-function.md)) and the freeze moment ([JetOSSnapshotFreeze](./jetossnapshotfreeze-function.md)), all the running instances in the engine will freeze and become part of the snapshot session. This occurs for two reasons:

  - It simplifies the code for users who want all instances.

  - It allows backward compatibility for the callers of the snapshot APIs.

#### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See Also

[Error Handling Parameters](./error-handling-parameters.md)  
[Extensible Storage Engine Errors](./extensible-storage-engine-errors.md)  
[JET_ERR](./jet-err.md)  
[JetOSSnapshotAbort](./jetossnapshotabort-function.md)  
[JetOSSnapshotEnd](./jetossnapshotend-function.md)  
[JetOSSnapshotFreeze](./jetossnapshotfreeze-function.md)  
[JetOSSnapshotPrepare](./jetossnapshotprepare-function.md)  
[JetOSSnapshotThaw](./jetossnapshotthaw-function.md)
