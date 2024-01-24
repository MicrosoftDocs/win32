---
description: "Learn more about: JetEnableMultiInstance Function"
title: JetEnableMultiInstance Function
TOCTitle: JetEnableMultiInstance Function
ms:assetid: d88a7b2a-c0d1-47de-9239-3631150d92da
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294107(v=EXCHG.10)
ms:contentKeyID: 32765722
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetEnableMultiInstanceW
- JetEnableMultiInstanceA
- JetEnableMultiInstance
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

# JetEnableMultiInstance Function


_**Applies to:** Windows | Windows Server_

## JetEnableMultiInstance Function

The **JetEnableMultiInstance** function configures the database engine for use with multiple instances in the same process. An optional array of global system parameters is available to the first caller allowing for the change to multi-instance mode.

**Windows XP:  JetEnableMultiInstance** is introduced in Windows XP.

```cpp
    JET_ERR JET_API JetEnableMultiInstance(
      __in_opt      JET_SETSYSPARAM* psetsysparam,
      __in_opt      unsigned long csetsysparam,
      __out_opt     unsigned long* pcsetsucceed
    );
```

### Parameters

*psetsysparam*

An array of global system parameters to set if and only if the engine enters multi-instance mode as a result of this call. If *csetsysparam* is zero then *psetsysparam* is ignored.

*csetsysparam*

The count of elements for the array of global parameters to set if and only if the engine enters multi-instance mode as a result of this call. If *csetsysparam* is zero then *psetsysparam* is ignored.

*pcsetsucceed*

A pointer to the count of global system parameters that were successfully configured as a result of this call.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).


| <p>Return code</p> | <p>Description</p> | 
|--------------------|--------------------|
| <p>JET_errSuccess</p> | <p>The operation completed successfully.</p> | 
| <p>JET_errIndexTuplesInvalidLimits</p> | <p>The specified tuple index parameters were not allowed. This error can be returned by <strong>JetEnableMultiInstance</strong> only when setting <a href="gg294119(v=exchg.10).md">JET_paramIndexTuplesLengthMin</a>, <a href="gg294119(v=exchg.10).md">JET_paramIndexTuplesLengthMax</a>, or <a href="gg294119(v=exchg.10).md">JET_paramIndexTuplesToIndexMax</a> to an illegal value.</p><p><strong>Windows XP:</strong>  This return value is introduced in Windows XP.</p> | 
| <p>JET_errInvalidPath</p> | <p>The specified file system path was invalid. This error can be returned by <strong>JetEnableMultiInstance</strong> only when setting system parameters that represent file system paths. For example, <a href="gg269235(v=exchg.10).md">JET_paramSystemPath</a> can return this error.</p> | 
| <p>JET_errRunningInOneInstanceMode</p> | <p>The operation failed because it is illegal when the database engine is operating in single instance mode (Windows 2000 compatibility mode).</p> | 
| <p>JET_errSystemParamsAlreadySet</p> | <p><strong>JetEnableMultiInstance</strong> failed because the engine is already in multi-instance mode.</p><p><strong>Note  </strong>This will happen even if no system parameters are specified.</p> | 



If this function succeeds, the database engine will be configured to run in multi-instance mode. The engine was also successfully configured with the optional list of global system parameters.

If this function fails, the database engine will remain in the current mode. If *pcsetsucceed* is non-zero, that number of system parameters will remain set.

#### Remarks

This function should only be used if the application must configure a given set of system parameters atomically when setting up the database engine for use in a multi-user scenario in the same process. If another method of synchronization is available, it is preferable to call [JetCreateInstance](./jetcreateinstance-function.md) and [JetSetSystemParameter](./jetsetsystemparameter-function.md) separately.

#### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista or Windows XP.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008 or Windows Server 2003.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JetEnableMultiInstanceW</strong> (Unicode) and <strong>JetEnableMultiInstanceA</strong> (ANSI).</p> | 



#### See Also

[JET_ERR](./jet-err.md)  
[JET_SETSYSPARAM](./jet-setsysparam-structure.md)  
[JetCreateInstance](./jetcreateinstance-function.md)  
[JetInit](./jetinit-function.md)  
[JetSetSystemParameter](./jetsetsystemparameter-function.md)
