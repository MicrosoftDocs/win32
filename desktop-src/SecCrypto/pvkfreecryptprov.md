---
description: Releases the handle to a cryptographic service provider (CSP) and optionally deletes the temporary container created by the PvkGetCryptProv function.
ms.assetid: e7dcb5c5-dd80-4810-bf1f-4b7b921fa22c
title: PvkFreeCryptProv function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PvkFreeCryptProv
api_type: 
- DllExport
api_location: 
- Mssign32.dll
---

# PvkFreeCryptProv function

> [!IMPORTANT]
> This API is deprecated. Microsoft may remove this API in future releases.

 

The **PvkFreeCryptProv** function releases the handle to a [*cryptographic service provider*](../secgloss/c-gly.md) (CSP) and optionally deletes the temporary container created by the [**PvkGetCryptProv**](pvkgetcryptprov.md) function.

> [!Note]  
> This function has no associated header file or import library. To call this function, you must create a user-defined header file and use the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to Mssign32.dll.

 

## Syntax


```C++
void WINAPI PvkFreeCryptProv(
  _In_     HCRYPTPROV hProv,
  _In_     LPCWSTR    pwszCapiProvider,
  _In_     DWORD      dwProviderType,
  _In_opt_ LPWSTR     pwszTmpContainer
);
```



## Parameters

<dl> <dt>

*hProv* \[in\]
</dt> <dd>

A handle to the CSP.

</dd> <dt>

*pwszCapiProvider* \[in\]
</dt> <dd>

A pointer to a null-terminated string for the CSP name.

</dd> <dt>

*dwProviderType* \[in\]
</dt> <dd>

A **DWORD** value that represents the cryptographic provider type. For more information, see [Cryptographic Provider Types](cryptographic-provider-types.md).

</dd> <dt>

*pwszTmpContainer* \[in, optional\]
</dt> <dd>

A pointer to a null-terminated string for the temporary key container name.

</dd> </dl>

## Return value

This function does not return a value.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| DLL<br/>                      | <dl> <dt>Mssign32.dll</dt> </dl> |



 

 
