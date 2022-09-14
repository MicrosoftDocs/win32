---
description: "Learn more about: JetOSSnapshotTruncateLog Function"
title: JetOSSnapshotTruncateLog Function
TOCTitle: JetOSSnapshotTruncateLog Function
ms:assetid: 3df8f5b2-8083-49b7-a325-fd13187f785c
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269231(v=EXCHG.10)
ms:contentKeyID: 32765533
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetOSSnapshotTruncateLog
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

# JetOSSnapshotTruncateLog Function


_**Applies to:** Windows | Windows Server_

## JetOSSnapshotTruncateLog Function

The **JetOSSnapshotTruncateLog** function enables log truncation for all instances that are part of the snapshot session.

**Windows Vista:**  **JetOSSnapshotTruncateLog** is introduced in Windows Vista.

```cpp
    JET_ERR JET_API JetOSSnapshotTruncateLog(
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
| <p>JET_bitAllDatabasesSnapshot</p> | <p>All the databases are attached so the storage engine can compute and do the log truncation.</p> | 
| <p>0 (zero)</p> | <p>No truncation will occur.</p> | 



### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errInvalidGrbit</p> | <p>The <em>grbit</em> parameter is invalid.</p> | 
| <p>JET_errOSSnapshotInvalidSequence</p> | <p>The snapshot session is not in the state in which a truncation can occur. Possible causes are:</p><ul><li><p>the call is done after the snapshot session timed-out</p></li><li><p>the session was specified as a copy snapshot</p></li></ul> | 



On success, the log files for one or all the instances part of the snapshot session will be truncated, if possible.

#### Remarks

This function should be called only if the snapshot was created with the JET_bitContinueAfterThaw option. Otherwise, the snapshot session would have ended after the [JetOSSnapshotThaw](./jetossnapshotthaw-function.md) call.

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
