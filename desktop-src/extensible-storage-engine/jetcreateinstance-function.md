---
description: "Learn more about: JetCreateInstance Function"
title: JetCreateInstance Function
TOCTitle: JetCreateInstance Function
ms:assetid: 9d6c8c9f-3d3b-4308-87d3-84b1ef270262
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269354(v=EXCHG.10)
ms:contentKeyID: 32765641
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetCreateInstanceW
- JetCreateInstance
- JetCreateInstanceA
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

# JetCreateInstance Function


_**Applies to:** Windows | Windows Server_

## JetCreateInstance Function

The **JetCreateInstance** function allocates a new instance of the database engine for use in a single process.

**Windows XP:  JetCreateInstance** is introduced in Windows XP.

```cpp
    JET_ERR JET_API JetCreateInstance(
      __out         JET_INSTANCE* pinstance,
      __in_opt      const tchar* szInstanceName
    );
```

### Parameters

*pinstance*

The output buffer that receives the newly-created instance.

*szInstanceName*

A unique string identifier for the instance to be created. This string must be unique within a given process hosting the database engine.

**Note** A NULL value is treated as a valid string identifier for an instance. Only one instance may have a NULL string identifier.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errInstanceNameInUse</p> | <p>The specified instance name is already in use for this process.</p> | 
| <p>JET_errInvalidParameter</p> | <p>One of the parameters provided contained an unexpected value or contained a value that did not make sense when combined with the value of another parameter. This can happen for <strong>JetCreateInstance</strong> when <em>pinstance</em> is <strong>NULL</strong>.</p> | 
| <p>JET_errRunningInOneInstanceMode</p> | <p>The operation failed because it cannot be used when the database engine is operating in single instance mode (Windows 2000 compatibility mode).</p> | 
| <p>JET_errTooManyInstances</p> | <p>A new instance could not be created because the maximum number of instances has been reached. The maximum number of supported instances is configured using <a href="gg294044(v=exchg.10).md">JetSetSystemParameter</a> using <em>JET_paramMaxInstances</em>.</p> | 



On success, a new instance will be allocated and the identifier for it will be returned. At this point, all system parameters for the instance will have the values of the global default system parameters. Once an instance will be allocated, it needs to be terminated and/or freed later on.

On failure, an error representing the cause of failure will be returned and no instance will be allocated.

#### Remarks

An instance must be initialized with a call to [JetInit](./jetinit-function.md) before it can be used by anything other than [JetSetSystemParameter](./jetsetsystemparameter-function.md).

An instance is destroyed by a call to the [JetTerm](./jetterm-function.md) function, even if that instance was never initialized using [JetInit](./jetinit-function.md). The maximum number of instances that may be created at any one time is controlled by [JET_paramMaxInstances](./resource-parameters.md), which can be configured by a call to [JetSetSystemParameter](./jetsetsystemparameter-function.md). An instance is the unit of recoverability for the database engine. It controls the life cycle of all the files used to protect the integrity of the data in a set of database files. These files include the checkpoint file and the transaction log files.

If the function succeeds, the database engine will automatically be changed to multi-instance mode as a side effect of this call. If the application desires to allow only one instance in the process then [JetInit](./jetinit-function.md) should be used to start the database engine in Windows 2000 compatibility mode.

If present, the *szDisplayName* will be used to identify the instance in places like Event Log or towards other callers like backup applications (through functions like [JetGetInstanceInfo](./jetgetinstanceinfo-function.md) or [JetOSSnapshotFreeze](./jetossnapshotfreeze-function.md)). If the display name is not provided, the unique *szInstanceName* will be used instead if present, otherwise an empty string will be returned. If the engine did not have the running mode set, after this call, it will be set to multi-instance mode.

The typical start-up sequence for a process potentially running multiple Jet instances would be:

  - A call to [JetCreateInstance2](./jetcreateinstance2-function.md) which will allocate and name the instance.

  - Multiple calls to [JetSetSystemParameter](./jetsetsystemparameter-function.md) for that instance in order to set different system parameters. Note that some system parameters need to be unique per instance (like [JET_paramSystemPath](./transaction-log-parameters.md) or [JET_paramLogFilePath](./transaction-log-parameters.md)) so most likely one will need to set each of those.

  - Start the instance using [JetInit](./jetinit-function.md) or [JetInit2](./jetinit2-function.md). In order to terminate and/or free an instance, [JetTerm](./jetterm-function.md), [JetTerm2](./jetterm2-function.md) needs to be used.

If this is the first instance to be started, there are a number of additional steps which will be executed during this call in order to make basic system initialization and configuration. A number of those steps might result in specific errors starting with JET_errOutOfMemory but others as well (see errors above).

#### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista or Windows XP.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008 or Windows Server 2003.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JetCreateInstanceW</strong> (Unicode) and <strong>JetCreateInstanceA</strong> (ANSI).</p> | 



#### See Also

[Extensible Storage Engine Files](./extensible-storage-engine-files.md)  
[JET_ERR](./jet-err.md)  
[JET_INSTANCE](./jet-instance.md)  
[JetCreateInstance2](./jetcreateinstance2-function.md)  
[JetEnableMultiInstance](./jetenablemultiinstance-function.md)  
[JetGetInstanceInfo](./jetgetinstanceinfo-function.md)  
[JetInit](./jetinit-function.md)  
[JetInit2](./jetinit2-function.md)  
[JetOSSnapshotFreeze](./jetossnapshotfreeze-function.md)  
[JetSetSystemParameter](./jetsetsystemparameter-function.md)  
[JetTerm](./jetterm-function.md)  
[JetTerm2](./jetterm2-function.md)
