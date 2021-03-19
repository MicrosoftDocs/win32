---
description: Retrieves a copy of the security descriptor protecting the specified open registry key in an offline registry hive.
ms.assetid: 676d5be5-d9d8-48c6-848a-917d1a0474c6
title: ORGetKeySecurity function (Offreg.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ORGetKeySecurity
api_type: 
- DllExport
api_location: 
- Offreg.dll
---

# ORGetKeySecurity function

Retrieves a copy of the security descriptor protecting the specified open registry key in an offline registry hive.

## Syntax


```C++
DWORD ORGetKeySecurity(
  _In_      ORHKEY               Handle,
  _In_      SECURITY_INFORMATION SecurityInformation,
  _Out_opt_ PSECURITY_DESCRIPTOR pSecurityDescriptor,
  _Inout_   PDWORD               lpcbSecurityDescriptor
);
```



## Parameters

<dl> <dt>

*Handle* \[in\]
</dt> <dd>

A handle to an open registry key in an offline registry hive.

</dd> <dt>

*SecurityInformation* \[in\]
</dt> <dd>

A [SECURITY\_INFORMATION](../secauthz/security-information.md) value that indicates the requested security information.

</dd> <dt>

*pSecurityDescriptor* \[out, optional\]
</dt> <dd>

A pointer to a buffer that receives a copy of the requested security descriptor. This parameter can be **NULL**.

</dd> <dt>

*lpcbSecurityDescriptor* \[in, out\]
</dt> <dd>

A pointer to a variable that specifies the size, in bytes, of the buffer pointed to by the *pSecurityDescriptor* parameter. When the function returns, the variable contains the number of bytes written to the buffer.

</dd> </dl>

## Return value

If the function succeeds, the function returns ERROR\_SUCCESS.

If the function fails, it returns a nonzero error code defined in Winerror.h. You can use the [FormatMessage](/windows/win32/api/winbase/nf-winbase-formatmessage) function with the FORMAT\_MESSAGE\_FROM\_SYSTEM flag to get a generic description of the error.

If the buffer specified by the *pSecurityDescriptor* parameter is too small, the function returns ERROR\_INSUFFICIENT\_BUFFER and the *lpcbSecurityDescriptor* parameter contains the number of bytes required for the requested security descriptor.

## Requirements



| Requirement | Value |
|----------------------------|---------------------------------------------------------------------------------------|
| Redistributable<br/> | Windows Offline Registry library version 1.0 or later<br/>                      |
| Header<br/>          | <dl> <dt>Offreg.h</dt> </dl>   |
| DLL<br/>             | <dl> <dt>Offreg.dll</dt> </dl> |



## See also

<dl> <dt>

[**ORDeleteKey**](ordeletekey.md)
</dt> <dt>

[**OROpenKey**](oropenkey.md)
</dt> <dt>

[**ORSetKeySecurity**](orsetkeysecurity.md)
</dt> <dt>

[SECURITY\_INFORMATION](../secauthz/security-information.md)
</dt> </dl>

 

 
