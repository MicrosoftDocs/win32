---
description: "Learn more about: JetSetSessionParameter Function"
title: JetSetSessionParameter Function
TOCTitle: JetSetSessionParameter Function
ms:assetid: 11aecf42-22ef-4bea-a3d7-961a7bdc85aa
ms:mtpsurl: https://msdn.microsoft.com/library/JJ835038(v=EXCHG.10)
ms:contentKeyID: 49894660
ms.date: 04/11/2016
ms.topic: reference
dev_langs:
- c++
api_name: 
- JetSetSessionParameter
topic_type: 
- apiref
- kbArticle
api_type: 
- DLLExport
api_location: 
- ESENT.DLL
ROBOTS: INDEX,FOLLOW

---

# JetSetSessionParameter Function


_**Applies to:** Windows | Windows Server_

The **JetSetSessionParameter** function configures the database engine.

``` c++
JET_ERR JET_API JetSetSessionParameter (
  __in_opt      JET_SESID sesid,
  __in          unsigned long sesparamid,
  __in_read_bytes_opt_(cbParam)  void* pvParam,
  __in          unsigned long cbParam
);
```

### Parameters

*sesid*

Specifies the session to use for this call.

When specified, the specified instance is ignored and the instance associated with the session will be used.

*sesparamid*

The ID of the session parameter to set.

*pvParam*

The data to set in this session parameter.

*cbParam*

The size of the data provided.

### Return value

This function returns the [JET_ERR](./jet-err.md) data type with one of the return codes listed in the following table. For more information about the possible Extensible Storage Engine (ESE) errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errAlreadyInitialized</p> | <p>The instance has been initialized by using a call to the <a href="gg294068(v=exchg.10).md">JetInit</a> function and this operation cannot be performed as a result. This can happen when an attempt is made to configure a system parameter after a change in the parameter value can no longer affect the state of the database engine.</p> | 
| <p>JET_errClientRequestToStopJetService</p> | <p>It is not possible to complete the operation because all activity on the instance associated with the session has ceased as a result of a call to the <a href="gg269240(v=exchg.10).md">JetStopService</a> function.</p> | 
| <p>JET_errIndexTuplesInvalidLimits</p> | <p>The specified tuple index parameters were illegal. This error is returned only when the <em>JET_paramIndexTuplesLengthMin</em>, <em>JET_paramIndexTuplesLengthMax</em>, or <em>JET_paramIndexTuplesToIndexMax</em> parameter is set to an illegal value. For information about these parameters, see <a href="gg294119(v=exchg.10).md">Index Parameters</a>.</p> | 
| <p>JET_errInitInProgress</p> | <p>It is not possible to complete the operation because the instance associated with the session is being initialized.</p> | 
| <p>JET_errInstanceUnavailable</p> | <p>It is not possible to complete the operation because the instance associated with the session has encountered a fatal error that requires that access to all data be revoked to protect the integrity of that data.</p> | 
| <p>JET_errInvalidParameter</p> | <p>One of the parameters provided contained an unexpected value or contained a value that did not make sense when combined with the value of another parameter. This can happen when the following occurs:</p><ul><li><p>The specified system parameter ID is invalid or unsupported.</p></li><li><p>An attempt was made to set a string-valued system parameter with a string the length of which was outside the legal range for the parameter.</p></li><li><p>An attempt was made to set a string-valued system parameter with a file path where the length of its absolute path representation was outside the legal range for that parameter.</p></li><li><p>An attempt was made to set an integer-valued system parameter with an integer that was outside the legal range for the parameter.</p></li><li><p>An attempt was made to set JET_paramUnicodeIndexDefault with a null <a href="gg294097(v=exchg.10).md">JET_UNICODEINDEX</a> pointer, an invalid LCID, or an unsupported set of <strong>LCMapString</strong> flags.</p></li><li><p>The specified system parameter cannot be set because it is read-only.</p></li><li><p>An attempt was made to set a system parameter after the <a href="gg294068(v=exchg.10).md">JetInit</a> function was called, the database engine is in single-instance mode, and a session was not specified.</p></li><li><p>The specified system parameter is global only and an attempt was made to set an instance-specific value for that system parameter.</p></li><li><p>The specified system parameter is per-instance only and an attempt was made to set the global value for that system parameter.</p></li></ul> | 
| <p>JET_errInvalidPath</p> | <p>The specified file system path was invalid. This error may be returned by <strong>JetSetSessionParameter</strong> only when setting system parameters that represent file system paths. For example, the <em>JET_paramSystemPath</em> parameter may return this error. For information about this parameter, see <a href="gg269235(v=exchg.10).md">Transaction Log Parameters</a>.</p> | 
| <p>JET_errNotInitialized</p> | <p>It is not possible to complete the operation because the instance associated with the session has not been initialized yet.</p> | 
| <p>JET_errRestoreInProgress</p> | <p>It is not possible to complete the operation because a restore operation is in progress on the instance associated with the session.</p> | 
| <p>JET_errTermInProgress</p> | <p>It is not possible to complete the operation because the instance associated with the session is being shut down.</p> | 
| <p>JET_errInvalidSesid</p> | <p>The session handle is invalid or refers to a closed session.</p><p>This error is not returned under all circumstances. Handles are validated on a best effort basis only.</p> | 
| <p>JET_errInvalidInstance</p> | <p>The instance handle is invalid or refers to an instance that has been shut down.</p><p>This error is not returned under all circumstances. Handles are validated on a best effort basis only.</p> | 



On success, the system parameter will be set to the provided value.

On failure, the system parameter value will remain unchanged.

#### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows 8.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2012.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See also

[JET_API_PTR](./jet-api-ptr.md)  
[JET_ERR](./jet-err.md)  
[JET_INSTANCE](./jet-instance.md)  
[JET_SESID](./jet-sesid.md)  
[JetCreateInstance](./jetcreateinstance-function.md)  
[JetGetSystemParameter](./jetgetsystemparameter-function.md)  
[JetInit](./jetinit-function.md)  
[System Parameters](./extensible-storage-engine-system-parameters.md)
