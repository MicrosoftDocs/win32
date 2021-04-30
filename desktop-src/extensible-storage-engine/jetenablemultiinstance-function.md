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
<td><p>JET_errIndexTuplesInvalidLimits</p></td>
<td><p>The specified tuple index parameters were not allowed. This error can be returned by <strong>JetEnableMultiInstance</strong> only when setting <a href="gg294119(v=exchg.10).md">JET_paramIndexTuplesLengthMin</a>, <a href="gg294119(v=exchg.10).md">JET_paramIndexTuplesLengthMax</a>, or <a href="gg294119(v=exchg.10).md">JET_paramIndexTuplesToIndexMax</a> to an illegal value.</p>
<p><strong>Windows XP:</strong>  This return value is introduced in Windows XP.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errInvalidPath</p></td>
<td><p>The specified file system path was invalid. This error can be returned by <strong>JetEnableMultiInstance</strong> only when setting system parameters that represent file system paths. For example, <a href="gg269235(v=exchg.10).md">JET_paramSystemPath</a> can return this error.</p></td>
</tr>
<tr class="even">
<td><p>JET_errRunningInOneInstanceMode</p></td>
<td><p>The operation failed because it is illegal when the database engine is operating in single instance mode (Windows 2000 compatibility mode).</p></td>
</tr>
<tr class="odd">
<td><p>JET_errSystemParamsAlreadySet</p></td>
<td><p><strong>JetEnableMultiInstance</strong> failed because the engine is already in multi-instance mode.</p>
<p><strong>Note  </strong>This will happen even if no system parameters are specified.</p></td>
</tr>
</tbody>
</table>


If this function succeeds, the database engine will be configured to run in multi-instance mode. The engine was also successfully configured with the optional list of global system parameters.

If this function fails, the database engine will remain in the current mode. If *pcsetsucceed* is non-zero, that number of system parameters will remain set.

#### Remarks

This function should only be used if the application must configure a given set of system parameters atomically when setting up the database engine for use in a multi-user scenario in the same process. If another method of synchronization is available, it is preferable to call [JetCreateInstance](./jetcreateinstance-function.md) and [JetSetSystemParameter](./jetsetsystemparameter-function.md) separately.

#### Requirements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Client</strong></p></td>
<td><p>Requires Windows Vista or Windows XP.</p></td>
</tr>
<tr class="even">
<td><p><strong>Server</strong></p></td>
<td><p>Requires Windows Server 2008 or Windows Server 2003.</p></td>
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
<td><p>Implemented as <strong>JetEnableMultiInstanceW</strong> (Unicode) and <strong>JetEnableMultiInstanceA</strong> (ANSI).</p></td>
</tr>
</tbody>
</table>


#### See Also

[JET_ERR](./jet-err.md)  
[JET_SETSYSPARAM](./jet-setsysparam-structure.md)  
[JetCreateInstance](./jetcreateinstance-function.md)  
[JetInit](./jetinit-function.md)  
[JetSetSystemParameter](./jetsetsystemparameter-function.md)
