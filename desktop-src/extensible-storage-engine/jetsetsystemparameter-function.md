---
description: "Learn more about: JetSetSystemParameter Function"
title: JetSetSystemParameter Function
TOCTitle: JetSetSystemParameter Function
ms:assetid: a244b5c9-6f6e-49d1-a6f7-9248feb9b92d
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294044(v=EXCHG.10)
ms:contentKeyID: 32765643
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetSetSystemParameterA
- JetSetSystemParameterW
- JetSetSystemParameter
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

# JetSetSystemParameter Function


_**Applies to:** Windows | Windows Server_

## JetSetSystemParameter Function

The **JetSetSystemParameter** function is used to set the numerous configuration settings of the database engine.

```cpp
    JET_ERR JET_API JetSetSystemParameter(
      __in_out_opt  JET_INSTANCE* pinstance,
      __in          JET_SESID sesid,
      __in          unsigned long paramid,
      __in          JET_API_PTR lParam,
      __in_opt      JET_PCSTR szParam
    );
```

### Parameters

*pinstance*

Specifies the instance to use for this call.

**Windows 2000:**  For Windows 2000, this parameter is ignored and should always be **NULL**.

**Windows XP:**  For Windows XP and later releases, this parameter is somewhat overloaded. If the engine is operating in legacy mode (Windows 2000 compatibility mode) where only one instance is supported, then this parameter may be **NULL** or may contain the actual instance returned by [JetInit](./jetinit-function.md). In either case, all system parameter settings are read from that one instance. If the engine is operating in multi-instance mode, then this parameter may be **NULL** or a pointer to an instance created using [JetInit](./jetinit-function.md) or [JetCreateIndex](./jetcreateindex-function.md). When this parameter is **NULL** then the global system parameter setting (or default) is read. When this parameter is an instance then the system parameter setting for that instance is read.

Even though this is technically an out parameter, this API never modifies the contents of the provided buffer.

*sesid*

Specifies the session to use for this call.

When specified, the specified instance is ignored and the instance associated with the session will be used.

*paramid*

The ID of the system parameter that will be set. See [System Parameters](./extensible-storage-engine-system-parameters.md) for a complete list of system parameters and their properties.

*lParam*

Provides the value to be set for the selected system parameter if that system parameter is of an integer type.

*szParam*

Provides the value for the selected system parameter if that system parameter is of a string type.

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
<td><p>The operation completed successfully.</p>
<p><strong>Windows Vista:</strong>  On Windows Vista and later releases, success can be returned without a change to the system parameter's value. See the JET_paramEnableAdvanced system parameter in the <a href="gg269346(v=exchg.10).md">Meta Parameters</a> topic for more information.</p></td>
</tr>
<tr class="even">
<td><p>JET_errAlreadyInitialized</p></td>
<td><p>The instance has been initialized using a call to <a href="gg294068(v=exchg.10).md">JetInit</a> and this operation cannot be performed as a result. This can happen for <strong>JetSetSystemParameter</strong> when an attempt is made to configure a system parameter after a change in its value cannot affect the state of the database engine.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errClientRequestToStopJetService</p></td>
<td><p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to <a href="gg269240(v=exchg.10).md">JetStopService</a>.</p></td>
</tr>
<tr class="even">
<td><p>JET_errIndexTuplesInvalidLimits</p></td>
<td><p>The specified tuple index parameters were illegal. This error may be returned by <strong>JetSetSystemParameter</strong> only when setting <a href="gg294119(v=exchg.10).md">JET_paramIndexTuplesLengthMin</a>, <a href="gg294119(v=exchg.10).md">JET_paramIndexTuplesLengthMax</a>, or <a href="gg294119(v=exchg.10).md">JET_paramIndexTuplesToIndexMax</a> to an illegal value.</p>
<p><strong>Windows XP and Windows Server 2003:</strong>  This can only happen on Windows XP and Windows Server 2003.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errInitInProgress</p></td>
<td><p>It is not possible to complete the operation because the instance associated with the session is being initialized.</p></td>
</tr>
<tr class="even">
<td><p>JET_errInstanceUnavailable</p></td>
<td><p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data.</p>
<p><strong>Windows XP:</strong>  This error will only be returned by Windows XP and later releases.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errInvalidParameter</p></td>
<td><p>One of the parameters provided contained an unexpected value or contained a value that did not make sense when combined with the value of another parameter. This can happen for <strong>JetSetSystemParameter</strong> when:</p>
<ul>
<li><p>The specified system parameter ID is invalid or unsupported.</p></li>
<li><p>An attempt was made to set a string-valued system parameter with a string whose length was outside the legal range for the parameter.</p></li>
<li><p>An attempt was made to set a string-valued system parameter with a file path where the length of its absolute path representation was outside the legal range for that parameter.</p>
<p><strong>Windows Vista:</strong>  This can only happen on Windows Vista and later releases.</p></li>
<li><p>An attempt was made to set an integer-valued system parameter with an integer that was outside the legal range for the parameter.</p></li>
<li><p>An attempt was made to set JET_paramUnicodeIndexDefault with a <strong>NULL</strong> <a href="gg294097(v=exchg.10).md">JET_UNICODEINDEX</a> pointer, an invalid LCID, or an unsupported set of LCMapString flags.</p>
<p><strong>Windows Vista:</strong>  This can only happen on Windows Vista and later releases.</p></li>
<li><p>The specified system parameter cannot be set because it is read-only.</p></li>
<li><p>An attempt was made to set a system parameter after <a href="gg294068(v=exchg.10).md">JetInit</a> was called, the database engine is in single-instance mode, and a session was not specified.</p>
<p><strong>Windows XP and Windows Server 2003:</strong>  This can only happen on Windows XP and Windows Server 2003.</p></li>
<li><p>The specified system parameter is global only and an attempt was made to set an instance specific value for that system parameter.</p>
<p><strong>Windows XP and Windows Server 2003:</strong>  This can only happen on Windows XP and Windows Server 2003.</p></li>
<li><p>The specified system parameter is per-instance only and an attempt was made to set the global value for that system parameter.</p>
<p><strong>Windows XP and Windows Server 2003:</strong>  This can only happen on Windows XP and Windows Server 2003.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>JET_errInvalidPath</p></td>
<td><p>The specified file system path was invalid. This error may be returned by <strong>JetSetSystemParameter</strong> only when setting system parameters that represent file system paths. For example, <a href="gg269235(v=exchg.10).md">JET_paramSystemPath</a> may return this error.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errNotInitialized</p></td>
<td><p>It is not possible to complete the operation because the instance associated with the session has not been initialized yet.</p></td>
</tr>
<tr class="even">
<td><p>JET_errRestoreInProgress</p></td>
<td><p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errTermInProgress</p></td>
<td><p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p></td>
</tr>
<tr class="even">
<td><p>JET_errInvalidSesid</p></td>
<td><p>The session handle is invalid or refers to a closed session.</p>
<p>This error is not returned under all circumstances. Handles are validated on a best effort basis only.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errInvalidInstance</p></td>
<td><p>The instance handle is invalid or refers to an instance that has been shutdown.</p>
<p>This error is not returned under all circumstances. Handles are validated on a best effort basis only.</p>
<p><strong>Windows Vista:</strong>  This error will only be returned by Windows Vista and later releases.</p></td>
</tr>
</tbody>
</table>


On success, the setting for the system parameter will be set to the provided value.

On failure, the setting for the system parameter will remain unchanged.

#### Remarks

**JetSetSystemParameter** does a poor job of validating the chosen setting for each system parameter. Care must be taken to not rely on this validation to enforce good settings. Please pay close attention to the description of each system parameter and follow those guidelines for a good system parameter setting.

There are a set of system parameters that should always be set to guarantee that the database engine works as intended. Specifically, any system parameters that affect the physical layout of the files used by the database engine should always be set. For more information, see [System Parameters](./extensible-storage-engine-system-parameters.md).

Every system parameter has a default value. These default values have evolved over time and are quite arbitrary. It is highly recommended that an application evaluate all the default values to ensure that they are appropriate. If they are not appropriate, then they should be configured by the application. This is important as many of these parameters can greatly impact the reliability, performance, and resource utilization of the database engine.

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
<td><p>Implemented as <strong>JetSetSystemParameterW</strong> (Unicode) and <strong>JetSetSystemParameterA</strong> (ANSI).</p></td>
</tr>
</tbody>
</table>


#### See Also

[JET_API_PTR](./jet-api-ptr.md)  
[JET_ERR](./jet-err.md)  
[JET_INSTANCE](./jet-instance.md)  
[JET_SESID](./jet-sesid.md)  
[JetCreateInstance](./jetcreateinstance-function.md)  
[JetGetSystemParameter](./jetgetsystemparameter-function.md)  
[JetInit](./jetinit-function.md)  
[System Parameters](./extensible-storage-engine-system-parameters.md)
