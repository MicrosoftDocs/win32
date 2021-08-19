---
description: "Learn more about: JetTerm Function"
title: JetTerm Function
TOCTitle: JetTerm Function
ms:assetid: 7711c960-98f4-4134-b8ae-8ddf7b26b6b0
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269298(v=EXCHG.10)
ms:contentKeyID: 32765590
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetTerm
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

# JetTerm Function


_**Applies to:** Windows | Windows Server_

## JetTerm Function

The **JetTerm** function initiates the shutdown of an instance that has been initialized by [JetInit](./jetinit-function.md).

**JetTerm** can also be used to destroy an uninitialized instance that was created by [JetCreateInstance](./jetcreateinstance-function.md).

```cpp
    JET_ERR JET_API JetTerm(
      __in          JET_INSTANCE instance
    );
```

### Parameters

*instance*

Specifies the instance to use for this call.

**Windows 2000:**  This parameter is ignored and should always be **NULL**.

**Windows XP and later releases:**  This parameter is overloaded. If the engine is operating in legacy mode (Windows 2000 compatibility mode) where only one instance is supported, then this parameter might be **NULL** or might contain the actual instance that is returned by [JetInit](./jetinit-function.md). If the engine is operating in multi-instance mode, then this parameter must be a pointer to an instance that was created using [JetCreateInstance](./jetcreateinstance-function.md).

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errInvalidParameter</p> | <p>One of the parameters that was provided contained an unexpected value, or the combination of several parameters yielded an unexpected result. This error will be returned by <strong>JetTerm</strong> when the engine is in multi-instance mode and when <em>pinstance</em> refers to an invalid instance.</p><p><strong>Windows XP:</strong>  This return value is introduced in Windows XP.</p> | 
| <p>JET_errNotInitialized</p> | <p>The operation cannot complete because the instance has not yet been initialized.</p> | 
| <p>JET_errTermInProgress</p> | <p>The operation cannot complete because the instance is being shut down.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>It is not possible to complete the operation because a restore operation is in progress on the instance.</p> | 
| <p>JET_errBackupInProgress</p> | <p>The operation cannot complete because a backup operation is in progress on the instance.</p> | 
| <p>JET_errTooManyActiveUsers</p> | <p>The instance cannot be shut down because there are currently sessions with active transactions for the specified instance. This error occurs only if the JET_bitTermComplete is used.</p> | 



If this function succeeds, the specified instance will be shut down. The instance handle will also be closed and made unavailable to any API that takes an instance handle. All other objects that are associated with the instance, such as sessions, will also be closed. The state of the checkpoint file, transaction log files, and the database files attached to the instance will be modified during the shutdown process.

If this function fails as the result of a usage error, then the instance remains in an initialized state and nothing changes. Otherwise, the instance is still shut down as per the success case. The difference is that the instance will need to go through crash recovery when it is next initialized. The engine will try to flush as much data as possible to minimize the amount of recovery that is required. Conceptually, such a failure of **JetTerm** is no different than a process crash.

#### Remarks

If the host process of an instance quits for any reason before **JetTerm** is successfully called on that instance then the instance is considered to be in a crashed state. Crash recovery will occur on the next attempt to initialize that instance.

#### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See Also

[Extensible Storage Engine Files](./extensible-storage-engine-files.md)  
[JetCreateInstance](./jetcreateinstance-function.md)  
[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JetInit](./jetinit-function.md)  
[JET_INSTANCE](./jet-instance.md)  
[JetTerm2](./jetterm2-function.md)
