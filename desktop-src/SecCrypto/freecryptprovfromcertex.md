---
description: 'Releases the handle either to a cryptographic service provider (CSP) or to a Cryptography API: Next Generation (CNG) key.'
ms.assetid: 76cbf8ae-c4ab-43d9-b06d-ea0b2a66368a
title: FreeCryptProvFromCertEx function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FreeCryptProvFromCertEx
api_type: 
- DllExport
api_location: 
- Mssign32.dll
---

# FreeCryptProvFromCertEx function

The **FreeCryptProvFromCertEx** function releases the handle either to a [*cryptographic service provider*](../secgloss/c-gly.md) (CSP) or to a Cryptography API: Next Generation (CNG) key.

> [!Note]  
> This function has no associated header file or import library. To call this function, you must create a user-defined header file and use the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to Mssign32.dll.

 

## Syntax


```C++
void WINAPI FreeCryptProvFromCertEx(
  _In_     BOOL                            fAcquired,
  _In_     HCRYPTPROV_OR_NCRYPT_KEY_HANDLE hProv,
           DWORD                           dwKeySpec,
  _In_opt_ LPWSTR                          pwszCapiProvider,
  _In_     DWORD                           dwProviderType,
  _In_opt_ LPWSTR                          pwszTmpContainer
);
```



## Parameters

<dl> <dt>

*fAcquired* \[in\]
</dt> <dd>

A value that specifies whether the provider handle was acquired from the [*certificate*](../secgloss/c-gly.md).

</dd> <dt>

*hProv* \[in\]
</dt> <dd>

A handle to a CAPICOM CSP or a handle to a CNG key.

</dd> <dt>

*dwKeySpec* 
</dt> <dd>

The address of a **DWORD** variable that receives additional information about the key. This can be one of the following values.



| Value                                                                                                                                                                                | Meaning                                                                                                          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| <span id="AT_KEYEXCHANGE"></span><span id="at_keyexchange"></span><dl> <dt>**AT\_KEYEXCHANGE**</dt> </dl>                     | The key pair is a key exchange pair.<br/>                                                                  |
| <span id="AT_SIGNATURE"></span><span id="at_signature"></span><dl> <dt>**AT\_SIGNATURE**</dt> </dl>                           | The key pair is a signature pair.<br/>                                                                     |
| <span id="CERT_NCRYPT_KEY_SPEC"></span><span id="cert_ncrypt_key_spec"></span><dl> <dt>**CERT\_NCRYPT\_KEY\_SPEC**</dt> </dl> | The key is a CNG key.<br/> **Windows Server 2003 and Windows XP:** This value is not supported.<br/> |



 

</dd> <dt>

*pwszCapiProvider* \[in, optional\]
</dt> <dd>

A pointer to a null-terminated string for the provider name.

</dd> <dt>

*dwProviderType* \[in\]
</dt> <dd>

Specifies the CSP type. This can be zero or one of the [Cryptographic Provider Types](cryptographic-provider-types.md). If this member is zero, the key container is one of the CNG key storage providers.

</dd> <dt>

*pwszTmpContainer* \[in, optional\]
</dt> <dd>

A pointer to a null-terminated string for the name of the temporary key container.

</dd> </dl>

## Return value

This function does not return a value.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| DLL<br/>                      | <dl> <dt>Mssign32.dll</dt> </dl> |



 

 
