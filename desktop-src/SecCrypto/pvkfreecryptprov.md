---
Description: Releases the handle to a cryptographic service provider (CSP) and optionally deletes the temporary container created by the PvkGetCryptProv function.
ms.assetid: e7dcb5c5-dd80-4810-bf1f-4b7b921fa22c
title: PvkFreeCryptProv function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PvkFreeCryptProv function

> \[!Important\]  
> This API is deprecated. Microsoft may remove this API in future releases.

 

The **PvkFreeCryptProv** function releases the handle to a [*cryptographic service provider*](security.c_gly#-security-cryptographic-service-provider-gly) (CSP) and optionally deletes the temporary container created by the [**PvkGetCryptProv**](pvkgetcryptprov.md) function.

> [!Note]  
> This function has no associated header file or import library. To call this function, you must create a user-defined header file and use the [**LoadLibrary**](https://msdn.microsoft.com/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/a0d7fc09-f888-4f46-a571-d3719a627597) functions to dynamically link to Mssign32.dll.

 

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



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| DLL<br/>                      | <dl> <dt>Mssign32.dll</dt> </dl> |



 

 




