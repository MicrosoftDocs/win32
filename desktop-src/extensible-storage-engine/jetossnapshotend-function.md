---
description: "Learn more about: JetOSSnapshotEnd Function"
title: JetOSSnapshotEnd Function
TOCTitle: JetOSSnapshotEnd Function
ms:assetid: f7f4db8b-8e40-48d7-bc7b-0c80d0d0f77f
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294136(v=EXCHG.10)
ms:contentKeyID: 32765750
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetOSSnapshotEnd
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

# JetOSSnapshotEnd Function


_**Applies to:** Windows | Windows Server_

## JetOSSnapshotEnd Function

The **JetOSSnapshotEnd** function notifies the engine that the snapshot session finished.

**Windows Vista:**  **JetOSSnapshotEnd** is introduced in Windows Vista:.

```cpp
    JET_ERR JET_API JetOSSnapshotEnd(
      __in          const JET_OSSNAPID snapId,
      __in          const JET_GRBIT grbit
    );
```

### Parameters

*snapId*

The identifier of the snapshot session.

*grbit*

The options for this call. This parameter can have a combination of the following values.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>0</p> | <p>The successful end of the snapshot session.</p> | 
| <p>JET_bitAbortSnapshot</p> | <p>The snapshot session aborted.</p> | 



### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errInvalidGrbit</p> | <p>One of the options requested is invalid, used incorrectly, or not implemented.</p> | 
| <p>JET_errOSSnapshotInvalidSequence</p> | <p>A snapshot session is already in progress. This is not allowed.</p> | 
| <p>JET_errOSSnapshotInvalidSnapId</p> | <p>The identifier for the snapshot session is not valid.</p> | 
| <p>JET_errOSSnapshotTimeOut</p> | <p>The snapshot session had an internal timeout before this call occurred. As a result, the IO operations returned to normal before this call was made.</p> | 



If this function succeeds, a snapshot session will complete and the normal engine behavior will resume. A new snapshot session can be started later.

If this function fails, the JET_errOSSnapshotTimeOut return code returns and the current snapshot session ends but the freeze of IOs during the snapshot period was not respected internally. For all other errors, the snapshot session state will not be changed.

#### Remarks

This function is called only if [JetOSSnapshotThaw](./jetossnapshotthaw-function.md) was called with JET_bitContinueAfterThaw.

The snapshot session must complete for the snapshot verification and log truncation to take place. Event log entries will be generated for the different steps of the snapshot.

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
[JetOSSnapshotThaw](./jetossnapshotthaw-function.md)
