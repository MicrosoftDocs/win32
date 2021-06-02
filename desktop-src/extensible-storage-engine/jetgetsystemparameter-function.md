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

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Return code</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>JET_errSuccess</p></td>
<td><p>The operation completed successfully.</p></td>
</tr>
<tr class="even">
<td><p>JET_errClientRequestToStopJetService</p></td>
<td><p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errInitInProgress</p></td>
<td><p>It is not possible to complete the operation because the instance associated with the session is being initialized.</p></td>
</tr>
<tr class="even">
<td><p>JET_errInstanceUnavailable</p></td>
<td><p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data. This error will only be returned by Windows XP and later releases.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errInvalidParameter</p></td>
<td><p>One of the parameters provided contained an unexpected value or contained a value that did not make sense when combined with the value of another parameter.</p>
<p>This can happen for <strong>JetGetSystemParameter</strong> when:</p>
<ul>
<li><p>The specified system parameter ID is invalid or unsupported.</p></li>
<li><p>The specified system parameter requires the integer output buffer to be provided and that output buffer pointer was <strong>NULL</strong>.</p></li>
<li><p>The specified system parameter requires a string output buffer to be provided and that output buffer pointer was <strong>NULL</strong>.</p>
<p><strong>Windows Vista:  </strong>This can only happen on Windows Vista and later releases.</p></li>
<li><p>The specified system parameter requires a string output buffer to be provided and the size of that output buffer is too small to accept a null terminated string.</p>
<p><strong>Windows Vista:  </strong>This can only happen on Windows Vista and later releases.</p></li>
<li><p>The specified system parameter cannot be read because it is write-only.</p></li>
<li><p>The specified system parameter is global only and an attempt was made to read an instance specific value for that system parameter. This can only happen on Windows XP and later releases.</p></li>
<li><p>The specified system parameter is per-instance only and an attempt was made to read the global value for that system parameter. This can only happen on Windows XP and later releases.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>JET_errNotInitialized</p></td>
<td><p>It is not possible to complete the operation because the instance associated with the session has not been initialized yet.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errRestoreInProgress</p></td>
<td><p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p></td>
</tr>
<tr class="even">
<td><p>JET_errTermInProgress</p></td>
<td><p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errInvalidSesid</p></td>
<td><p>The session handle is invalid or refers to a closed session. This error is not returned under all circumstances. Handles are validated on a best effort basis only.</p></td>
</tr>
<tr class="even">
<td><p>JET_errInvalidInstance</p></td>
<td><p>The instance handle is invalid or refers to an instance that has been shutdown. This error is not returned under all circumstances. Handles are validated on a best effort basis only.</p>
<p><strong>Windows Vista:  </strong>This error will only be returned by Windows Vista and later releases.</p></td>
</tr>
<tr class="odd">
<td><p>JET_wrnBufferTruncated</p></td>
<td><p>The operation completed successfully, but the output buffer was too small to receive the entire system parameter setting.</p>
<p>The output buffer has been filled with as much of the system parameter setting as would fit. If the output buffer is at least one character in length then the string in that output buffer will be null terminated.</p>
<p><strong>Note  </strong>This error is not returned by all releases. Please see the Remarks section for more information.</p></td>
</tr>
<tr class="even">
<td><p>JET_errBufferTooSmall</p></td>
<td><p>The operation failed because the output buffer was too small to receive the entire system parameter setting.</p>
<p><strong>Note  </strong>This error is not returned in some cases to preserve application compatibility. Please see the Remarks section for more information.</p>
<p><strong>Windows Vista:  </strong>This error will only be returned by Windows Vista and later releases.</p></td>
</tr>
</tbody>
</table>


On success, the output buffer appropriate for the requested system parameter will be set to the value of that system parameter.

On failure, the state of the output buffers will be undefined.

#### Remarks

There is an important problem in this API that is present in all releases. If a system parameter with a string value is requested and the output buffer is too small to receive the entire system parameter setting, JET_wrnBufferTruncated will NOT be returned. JET_errSuccess is returned instead. If the length of the returned string is equal to the size of the output buffer less the **NULL** terminator, the caller should react as if JET_wrnBufferTruncated were returned. If a zero-sized string output buffer is specified, the caller should react as if JET_errInvalidParameter were returned.

#### Requirements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Client</strong></p></td>
<td><p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p></td>
</tr>
<tr class="even">
<td><p><strong>Server</strong></p></td>
<td><p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Header</strong></p></td>
<td><p>Declared in Esent.h.</p></td>
</tr>
<tr class="even">
<td><p><strong>Library</strong></p></td>
<td><p>Use ESENT.lib.</p></td>
</tr>
<tr class="odd">
<td><p><strong>DLL</strong></p></td>
<td><p>Requires ESENT.dll.</p></td>
</tr>
<tr class="even">
<td><p><strong>Unicode</strong></p></td>
<td><p>Implemented as <strong>JetGetSystemParameterW</strong> (Unicode) and <strong>JetGetSystemParameterA</strong> (ANSI).</p></td>
</tr>
</tbody>
</table>


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
