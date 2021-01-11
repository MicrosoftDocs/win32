---
description: Gets a handle to a cryptographic service provider (CSP) based on either a private key file or a key container name.
ms.assetid: 82cdaa6f-e747-4c9d-8d2d-5fa206891eed
title: PvkGetCryptProv function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PvkGetCryptProv
api_type: 
- DllExport
api_location: 
- Mssign32.dll
---

# PvkGetCryptProv function

> [!IMPORTANT]
> This API is deprecated. Microsoft may remove this API in future releases.

 

The **PvkGetCryptProv** function gets a handle to a [*cryptographic service provider*](../secgloss/c-gly.md) (CSP) based on either a [*private key*](../secgloss/p-gly.md) file or a key container name.

> [!Note]  
> This function has no associated header file or import library. To call this function, you must create a user-defined header file and use the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to Mssign32.dll.

 

## Syntax


```C++
HRESULT WINAPI PvkGetCryptProv(
  _In_      HWND       hwnd,
  _In_      LPCWSTR    pwszCaption,
  _In_      LPCWSTR    pwszCapiProvider,
  _In_      DWORD      dwProviderType,
  _In_      LPCWSTR    pwszPvkFile,
  _In_      LPCWSTR    pwszKeyContainerName,
  _Out_     DWORD      *pdwKeySpec,
  _Out_opt_ LPWSTR     *ppwszTmpContainer,
  _Out_     HCRYPTPROV *phCryptProv
);
```



## Parameters

<dl> <dt>

*hwnd* \[in\]
</dt> <dd>

If a password is required to decrypt the private key file, this parameter is a handle to the parent of the password dialog box; otherwise, it is **NULL**.

</dd> <dt>

*pwszCaption* \[in\]
</dt> <dd>

A pointer to a null-terminated string for the dialog box caption.

</dd> <dt>

*pwszCapiProvider* \[in\]
</dt> <dd>

A pointer to a null-terminated string for the CSP name.

</dd> <dt>

*dwProviderType* \[in\]
</dt> <dd>

A **DWORD** value that represents the cryptographic provider type. For more information, see [Cryptographic Provider Types](cryptographic-provider-types.md).

</dd> <dt>

*pwszPvkFile* \[in\]
</dt> <dd>

A pointer to a null-terminated string that contains the name of a private key file.

</dd> <dt>

*pwszKeyContainerName* \[in\]
</dt> <dd>

A pointer to a null-terminated string for the private key container name.

</dd> <dt>

*pdwKeySpec* \[out\]
</dt> <dd>

A pointer to a **DWORD** value for the type of key of the container returned with *phCryptProv* and *ppwszTmpContainer*.

</dd> <dt>

*ppwszTmpContainer* \[out, optional\]
</dt> <dd>

The address of a pointer to a null-terminated string for the temporary key container name. The **PvkGetCryptProv** function provides and initializes the temporary container. When calling **PvkGetCryptProv**, the address should point to a **NULL** value.

</dd> <dt>

*phCryptProv* \[out\]
</dt> <dd>

A pointer to a handle for the CSP.

</dd> </dl>

## Return value

If the method succeeds, it returns **S\_OK**.

If the method fails, it returns an **HRESULT** value that indicates the error. For a list of common error codes, see [Common HRESULT Values](common-hresult-values.md).

## Remarks

The **PvkGetCryptProv** function first tries to get the provider handle from the key container name specified by the *pwszKeyContainerName* parameter. If you pass **NULL** for the *pwszKeyContainerName* parameter, **PvkGetCryptProv** tries to get the provider from the private key file specified in the *pwszPvkFile* parameter.

When you have finished using the CSP, free the provider handle and temporary key container by calling the [**PvkFreeCryptProv**](pvkfreecryptprov.md) function.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| DLL<br/>                      | <dl> <dt>Mssign32.dll</dt> </dl> |



 

 
