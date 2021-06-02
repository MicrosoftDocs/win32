---
description: Retrieves the virtual flags on the specified open registry key in an offline registry hive.
ms.assetid: 2a04c257-e3b0-415b-97d2-616e12513a0a
title: ORGetVirtualFlags function (Offreg.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ORGetVirtualFlags
api_type: 
- DllExport
api_location: 
- Offreg.dll
---

# ORGetVirtualFlags function

Retrieves the virtual flags on the specified open registry key in an offline registry hive.

## Syntax


```C++
DWORD ORGetVirtualFlags(
  _In_  ORHKEY Handle,
  _Out_ PDWORD pdwFlags
);
```



## Parameters

<dl> <dt>

*Handle* \[in\]
</dt> <dd>

A handle to an open registry key in an offline registry hive.

</dd> <dt>

*pdwFlags* \[out\]
</dt> <dd>

A pointer to a variable to receive the virtualization flags set for the key. After the function returns, this parameter can be one or more of the following values.



| Value                                                                                                                                                                                                                                                    | Meaning                                                                                                                                                                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="REG_KEY_DONT_SILENT_FAIL"></span><span id="reg_key_dont_silent_fail"></span><dl> <dt>**REG\_KEY\_DONT\_SILENT\_FAIL**</dt> <dt>4</dt> </dl> | If this flag is set and an Open operation fails on a key that has virtualization enabled, the registry does not attempt to reopen the key. If this flag is clear, the registry attempts to reopen the key with MAXIMUM\_ALLOWED access.<br/>                                                                                            |
| <span id="REG_KEY_DONT_VIRTUALIZE"></span><span id="reg_key_dont_virtualize"></span><dl> <dt>**REG\_KEY\_DONT\_VIRTUALIZE**</dt> <dt>2</dt> </dl>     | If this flag is set and a Create Key operation fails because the caller does not have the KEY\_CREATE\_SUB\_KEY right on the parent key, the registry fails the Create operation. If this flag is clear, the registry attempts to create the key in the virtual store. The caller must have the KEY\_READ right on the parent key.<br/> |
| <span id="REG_KEY_RECURSE_FLAG"></span><span id="reg_key_recurse_flag"></span><dl> <dt>**REG\_KEY\_RECURSE\_FLAG**</dt> <dt>8</dt> </dl>              | If this flag is set, registry virtualization flags are propagated from the parent key. If this flag is clear, registry virtualization flags are not propagated.<br/>                                                                                                                                                                    |



 

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is a nonzero error code defined in Winerror.h. You can use the [FormatMessage](/windows/win32/api/winbase/nf-winbase-formatmessage) function with the FORMAT\_MESSAGE\_FROM\_SYSTEM flag to get a generic description of the error.

## Remarks

Registry virtualization is an interim application compatibility technology that enables registry write operations that have global impact to be redirected to per-user locations. This redirection is transparent to applications reading from or writing to the registry.

Registry virtualization is supported starting with Windows Vista. However, Microsoft intends to remove it from future versions of the Windows operating system as more applications are made compatible with Windows Vista. Therefore, applications should not depend on the behavior of registry virtualization in the system.

Registry virtualization is enabled only for the following:

-   32-bit interactive processes
-   Keys in **HKEY\_LOCAL\_MACHINE\\Software**
-   Keys that an administrator can write to

For more information, see [Registry Virtualization](../sysinfo/registry-virtualization.md).

## Requirements



| Requirement | Value |
|----------------------------|---------------------------------------------------------------------------------------|
| Redistributable<br/> | Windows Offline Registry library version 1.0 or later<br/>                      |
| Header<br/>          | <dl> <dt>Offreg.h</dt> </dl>   |
| DLL<br/>             | <dl> <dt>Offreg.dll</dt> </dl> |



## See also

<dl> <dt>

[**ORSetVirtualFlags**](orsetvirtualflags.md)
</dt> <dt>

[Registry Virtualization](../sysinfo/registry-virtualization.md)
</dt> </dl>

 

 
