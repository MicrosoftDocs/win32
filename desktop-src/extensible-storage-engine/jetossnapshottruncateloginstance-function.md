---
description: "Learn more about: JetOSSnapshotTruncateLogInstance Function"
title: JetOSSnapshotTruncateLogInstance Function
TOCTitle: JetOSSnapshotTruncateLogInstance Function
ms:assetid: ddc51957-5b89-4abf-9193-c34ef626a63e
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294115(v=EXCHG.10)
ms:contentKeyID: 32765729
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetOSSnapshotTruncateLogInstance
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

# JetOSSnapshotTruncateLogInstance Function


_**Applies to:** Windows | Windows Server_

## JetOSSnapshotTruncateLogInstance Function

The **JetOSSnapshotTruncateLogInstance** function truncates the log for a specified instance during a snapshot session.

**Windows Vista:**  **JetOSSnapshotTruncateLogInstance** is introduced in Windows Vista.

```cpp
    JET_ERR JET_API JetOSSnapshotTruncateLogInstance(
      __in          const JET_OSSNAPID snapId,
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

The options for this call. This parameter can have a combination of the following values.

*grbit* can be one of the following values:


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitAllDatabasesSnapshot</p> | <p>All the databases are attached so the storage engine can compute and do the log truncation.</p> | 
| <p>0 (zero)</p> | <p>No truncation will occur.</p> | 



### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errInvalidGrbit</p> | <p>The <em>grbit</em> parameter is invalid.</p> | 
| <p>JET_errOSSnapshotInvalidSequence</p> | <p>The snapshot session is not in the state in which a truncation can occur. Possible causes are:</p><ul><li><p>The call completes after the snapshot session timed out.</p></li><li><p>The session was specified as a copy snapshot.</p></li></ul> | 



If this function succeeds, the log files for one or all of the instances that are part of the snapshot session will be truncated, if possible.

#### Remarks

This function should be called only if the snapshot was created with the JET_bitContinueAfterThaw option. Otherwise, the snapshot session ends after the call to [JetOSSnapshotThaw](./jetossnapshotthaw-function.md).

#### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See Also

[Error Handling Parameters](./error-handling-parameters.md)  
[Extensible Storage Engine Errors](./extensible-storage-engine-errors.md)  
[JET_ERR](./jet-err.md)  
[JetOSSnapshotEnd](./jetossnapshotend-function.md)  
[JetOSSnapshotFreeze](./jetossnapshotfreeze-function.md)  
[JetOSSnapshotPrepare](./jetossnapshotprepare-function.md)  
[JetOSSnapshotThaw](./jetossnapshotthaw-function.md)
