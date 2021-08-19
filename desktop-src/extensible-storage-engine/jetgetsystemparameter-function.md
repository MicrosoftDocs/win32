---
description: "Learn more about: JetGetSystemParameter Function"
title: JetGetSystemParameter Function
TOCTitle: JetGetSystemParameter Function
ms:assetid: 6e6ddb49-702c-4c45-ac9f-35ae817696dd
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269291(v=EXCHG.10)
ms:contentKeyID: 32765583
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetGetSystemParameter
- JetGetSystemParameterA
- JetGetSystemParameterW
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

# JetGetSystemParameter Function


_**Applies to:** Windows | Windows Server_

## JetGetSystemParameter Function

The **JetGetSystemParameter** function reads the numerous configuration settings of the database engine.

```cpp
    JET_ERR JET_API JetGetSystemParameter(
      __in          JET_INSTANCE instance,
      __in          JET_SESID sesid,
      __in          unsigned long paramid,
      __in_out_opt  JET_API_PTR* plParam,
      __out_opt     JET_PSTR szParam,
      __in          unsigned long cbMax
    );
```

### Parameters

*instance*

The instance to use for this call.

For Windows 2000, this parameter is ignored and should always be **NULL**.

For Windows XP and later releases, this parameter is somewhat overloaded. If the engine is operating in legacy mode (Windows 2000 compatibility mode) where only one instance is supported, this parameter may be **NULL** or may contain the actual instance returned by [JetInit](./jetinit-function.md). In either case, all system parameter settings are read from that one instance. If the engine is operating in multi-instance mode, this parameter may be **NULL** or a pointer to an instance created using [JetInit](./jetinit-function.md) or [JetCreateInstance](./jetcreateinstance-function.md). When this parameter is **NULL** then the global system parameter setting (or default) is read. When this parameter is an instance then the system parameter setting for that instance is read.

*sesid*

The session to use for this call.

When specified, the specified instance is ignored and the instance associated with the session will be used.

*paramid*

The ID of the system parameter that will be read.

See [System Parameters](./extensible-storage-engine-system-parameters.md) for a complete list of system parameters and their properties.

*plParam*

The output buffer that receives the value of the selected system parameter if that system parameter is of an integer type.

*szParam*

The output buffer that receives the value of the selected system parameter if that system parameter is of a string type.

*cbMax*

The maximum size in bytes of the string output buffer.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p> | 
| <p>JET_errInitInProgress</p> | <p>It is not possible to complete the operation because the instance associated with the session is being initialized.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data. This error will only be returned by Windows XP and later releases.</p> | 
| <p>JET_errInvalidParameter</p> | <p>One of the parameters provided contained an unexpected value or contained a value that did not make sense when combined with the value of another parameter.</p><p>This can happen for <strong>JetGetSystemParameter</strong> when:</p><ul><li><p>The specified system parameter ID is invalid or unsupported.</p></li><li><p>The specified system parameter requires the integer output buffer to be provided and that output buffer pointer was <strong>NULL</strong>.</p></li><li><p>The specified system parameter requires a string output buffer to be provided and that output buffer pointer was <strong>NULL</strong>.</p><p><strong>Windows Vista:  </strong>This can only happen on Windows Vista and later releases.</p></li><li><p>The specified system parameter requires a string output buffer to be provided and the size of that output buffer is too small to accept a null terminated string.</p><p><strong>Windows Vista:  </strong>This can only happen on Windows Vista and later releases.</p></li><li><p>The specified system parameter cannot be read because it is write-only.</p></li><li><p>The specified system parameter is global only and an attempt was made to read an instance specific value for that system parameter. This can only happen on Windows XP and later releases.</p></li><li><p>The specified system parameter is per-instance only and an attempt was made to read the global value for that system parameter. This can only happen on Windows XP and later releases.</p></li></ul> | 
| <p>JET_errNotInitialized</p> | <p>It is not possible to complete the operation because the instance associated with the session has not been initialized yet.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p> | 
| <p>JET_errTermInProgress</p> | <p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p> | 
| <p>JET_errInvalidSesid</p> | <p>The session handle is invalid or refers to a closed session. This error is not returned under all circumstances. Handles are validated on a best effort basis only.</p> | 
| <p>JET_errInvalidInstance</p> | <p>The instance handle is invalid or refers to an instance that has been shutdown. This error is not returned under all circumstances. Handles are validated on a best effort basis only.</p><p><strong>Windows Vista:  </strong>This error will only be returned by Windows Vista and later releases.</p> | 
| <p>JET_wrnBufferTruncated</p> | <p>The operation completed successfully, but the output buffer was too small to receive the entire system parameter setting.</p><p>The output buffer has been filled with as much of the system parameter setting as would fit. If the output buffer is at least one character in length then the string in that output buffer will be null terminated.</p><p><strong>Note  </strong>This error is not returned by all releases. Please see the Remarks section for more information.</p> | 
| <p>JET_errBufferTooSmall</p> | <p>The operation failed because the output buffer was too small to receive the entire system parameter setting.</p><p><strong>Note  </strong>This error is not returned in some cases to preserve application compatibility. Please see the Remarks section for more information.</p><p><strong>Windows Vista:  </strong>This error will only be returned by Windows Vista and later releases.</p> | 



On success, the output buffer appropriate for the requested system parameter will be set to the value of that system parameter.

On failure, the state of the output buffers will be undefined.

#### Remarks

There is an important problem in this API that is present in all releases. If a system parameter with a string value is requested and the output buffer is too small to receive the entire system parameter setting, JET_wrnBufferTruncated will NOT be returned. JET_errSuccess is returned instead. If the length of the returned string is equal to the size of the output buffer less the **NULL** terminator, the caller should react as if JET_wrnBufferTruncated were returned. If a zero-sized string output buffer is specified, the caller should react as if JET_errInvalidParameter were returned.

#### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JetGetSystemParameterW</strong> (Unicode) and <strong>JetGetSystemParameterA</strong> (ANSI).</p> | 



#### See Also

[JET_API_PTR](./jet-api-ptr.md)  
[JET_ERR](./jet-err.md)  
[JET_INSTANCE](./jet-instance.md)  
[JET_SESID](./jet-sesid.md)  
[JetCreateInstance](./jetcreateinstance-function.md)  
[JetInit](./jetinit-function.md)  
[JetSetSystemParameter](./jetsetsystemparameter-function.md)  
[JetStopService](./jetstopservice-function.md)  
[System Parameters](./extensible-storage-engine-system-parameters.md)
