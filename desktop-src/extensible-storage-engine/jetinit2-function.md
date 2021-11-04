---
description: "Learn more about: JetInit2 Function"
title: JetInit2 Function
TOCTitle: JetInit2 Function
ms:assetid: b5541429-6ce6-457b-88cf-673d267f6209
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294065(v=EXCHG.10)
ms:contentKeyID: 32765680
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetInit2
topic_type: 
- kbArticle
- apiref
api_type: 
- COM
- DLLExport
api_location: 
- ESENT.DLL
ROBOTS: INDEX,FOLLOW

---

# JetInit2 Function


_**Applies to:** Windows | Windows Server_

## JetInit2 Function

The **JetInit2** function puts the database engine into a state where it can support application use of database files. The engine must already be properly configured for initialization using [JetSetSystemParameter](./jetsetsystemparameter-function.md). Database crash recovery is performed automatically as a part of the initialization process.

**Windows XP:**  **JetInit2** is introduced in Windows XP.

This function is obsolete. Use [JetInit3](./jetinit3-function.md) instead.

```cpp
JET_ERR JET_API JetInit2(
  __in_out_opt  JET_INSTANCE* pinstance,
  __in          JET_GRBIT grbit
);
```

### Parameters

*pinstance*

The instance to use for this call.

For Windows 2000, this parameter is ignored and should always be NULL.

For Windows XP and later releases, the use of this parameter depends on the operating mode of the engine. If the engine is operating in legacy mode (Windows 2000 compatibility mode) where only one instance is supported, this parameter may either be NULL or it may be set to a valid output buffer containing NULL or JET_instanceNil which returns the global instance handle created as a side effect of the initialization. This instance handle can then be passed to any other API that takes an instance. If the engine is operating in multi-instance mode, this parameter must be set to a valid input buffer that contains the instance handle returned by the [JetCreateInstance](./jetcreateinstance-function.md) that is being initialized.

*grbit*

A group of bits specifying zero or more of the following options.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitReplayReplicatedLogFiles</p> | <p>Reserved for future use.</p> | 
| <p>JET_bitCreateSFSVolumeIfNotExist</p> | <p>Reserved for future use.</p> | 
| <p>JET_bitReplayIgnoreMissingDB</p> | <p>This option allows the user to run recovery on a set of log files, without all of the databases being present, that were attached at one point of the log set.</p> | 
| <p>JET_bitRecoveryWithoutUndo</p> | <p>Perform recovery, but halt at the Undo phase. This allows additional transaction logs to copied in and applied.</p> | 
| <p>JET_bitTruncateLogsAfterRecovery</p> | <p>On successful soft recovery, truncate log files.</p> | 
| <p>JET_bitReplayMissingMapEntryDB</p> | <p>Missing database map entry default to same location.</p> | 
| <p>JET_bitReplayIgnoreLostLogs</p> | <p>Ignore logs lost from the end of the log stream.</p><p><strong>Windows 7:JET_bitReplayIgnoreLostLogs</strong> is introduced in Windows 7.</p> | 



### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


#### Remarks

An instance must be initialized with a call to **JetInit2** before it can be used by anything other than [JetSetSystemParameter](./jetsetsystemparameter-function.md).

An instance is destroyed by a call to the [JetTerm](./jetterm-function.md) function, even if that instance was never initialized using [JetInit](./jetinit-function.md). An instance is the unit of recoverability for the database engine. It controls the life cycle of all the files used to protect the integrity of the data in a set of database files. These files include the checkpoint file and the transaction log files.

If recovery is running on a set of logs, for which not all databases is present (which will return the error JET_errAttachedDatabaseMismatch under normal circumstances), and the client wishes recovery to continue despite missing databases, the JET_ bitReplayIgnoreMissingDB is used to continue recovery for the available databases.

See the Remarks section in [JetInit](./jetinit-function.md) for more information.

#### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista or Windows XP.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008 or Windows Server 2003.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See Also

[Extensible Storage Engine Files](./extensible-storage-engine-files.md)  
[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_INSTANCE](./jet-instance.md)  
[JetCreateInstance](./jetcreateinstance-function.md)  
[JetInit](./jetinit-function.md)  
[JetInit3](./jetinit3-function.md)  
[JetSetSystemParameter](./jetsetsystemparameter-function.md)  
[Resource Parameters](./resource-parameters.md)
