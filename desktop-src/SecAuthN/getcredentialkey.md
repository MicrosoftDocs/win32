---
Description: Gets the credential key of the user logon credential.
ms.assetid: 4C65CBC2-E086-4C87-85C5-73BFF376FD3A
title: GetCredentialKey function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GetCredentialKey function

Gets the credential key of the user logon credential.

## Syntax


```C++
SEC_ENTRY GetCredentialKey(
  _In_     PVOID           ProviderHandle,
  _In_opt_ PLUID           LogonId,
  _In_opt_ PVOID           AuthBuffer,
  _In_     ULONG           AuthBufferSize,
  _In_     ULONG           Reserved,
  _Out_    PUNICODE_STRING CredentialKey
);
```



## Parameters

<dl> <dt>

*ProviderHandle* \[in\]
</dt> <dd>

Identity provider handle.

</dd> <dt>

*LogonId* \[in, optional\]
</dt> <dd>

If *AuthBuffer* is **NULL**, the *LogonId* parameter contains the logon ID of the logon session whose logon authority is the identity provider pointed to by the *ProviderHandle* parameter. The function uses the *LogonId* parameter to locate the user logon credential.

</dd> <dt>

*AuthBuffer* \[in, optional\]
</dt> <dd>

If *LogonId* is **NULL**, *AuthBuffer* provides the credential needed to authenticate the user to the online service and to compute the credential key. The credential key should be the same as one that would be returned given a logon ID of the logon session of the same user. This parameter is passed to the function when LSA disconnects a user. The *AuthBuffer* parameter is a [**SEC\_WINNT\_AUTH\_IDENTITY\_EX2**](/windows/win32/Sspi/ns-sspi-_sec_winnt_auth_identity_ex2?branch=master) buffer. The buffer will not be encrypted because LSA will decrypt the buffer before passing it to the provider. If *LogonId* is not **NULL**, *AuthBuffer* must be **NULL**.

</dd> <dt>

*AuthBufferSize* \[in\]
</dt> <dd>

The size, in bytes, of the *AuthBuffer* buffer.

</dd> <dt>

*Reserved* \[in\]
</dt> <dd>

This parameter is reserved and must be set to zero.

</dd> <dt>

*CredentialKey* \[out\]
</dt> <dd>

A string buffer that represents the credential key. The string buffer must be allocated by the function by using the [**AllocateLsaHeap**](/windows/win32/Ntsecpkg/nc-ntsecpkg-lsa_allocate_lsa_heap?branch=master) function.

</dd> </dl>

## Return value

If the function succeeds, the function returns SEC\_E\_OK.

If the function fails, the function may return one of the following error codes.



| Return value                                                                                              | Description                                                                                                                                                                                                                            |
|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>STATUS\_INVALID\_PARAMETER</dt> </dl>     | A parameter is not valid. *LogonId* and *AuthBuffer* are both **NULL** or both non-**NULL**, or *AuthBuffer* contains a [**SEC\_WINNT\_AUTH\_IDENTITY\_EX2**](/windows/win32/Sspi/ns-sspi-_sec_winnt_auth_identity_ex2?branch=master) structure that is not valid.<br/> |
| <dl> <dt>STATUS\_BAD\_VALIDATION\_CLASS</dt> </dl> | The credential type in *AuthBuffer* is not recognized.<br/>                                                                                                                                                                      |
| <dl> <dt>Others</dt> </dl>                         | Other provider-specific errors.<br/>                                                                                                                                                                                             |



 

## Remarks

Either the *LogonId* or the *AuthBuffer* parameter must be non-**NULL**, but both cannot be **NULL** or both cannot be provided on the same call to this function.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>           |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/> |



 

 




