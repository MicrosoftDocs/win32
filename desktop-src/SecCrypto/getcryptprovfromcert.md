---
description: Gets a handle to a cryptographic service provider (CSP) and a key specification for a certificate context.
ms.assetid: ff72231f-e10f-49d2-b0e0-0008923803cc
title: GetCryptProvFromCert function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetCryptProvFromCert
api_type: 
- DllExport
api_location: 
- Mssign32.dll
---

# GetCryptProvFromCert function

> [!IMPORTANT]
> This API is deprecated. Microsoft may remove this API in future releases.

 

The **GetCryptProvFromCert** function gets a handle to a [*cryptographic service provider*](../secgloss/c-gly.md) (CSP) and a key specification for a [*certificate*](../secgloss/c-gly.md) context. Use this function to get access to the [*private key*](../secgloss/p-gly.md) of the certificate issuer.

> [!Note]  
> This function has no associated header file or import library. To call this function, you must create a user-defined header file and use the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to Mssign32.dll.

 

## Syntax


```C++
BOOL WINAPI GetCryptProvFromCert(
  _In_      HWND           hwnd,
  _In_      PCCERT_CONTEXT pCert,
  _Out_     HCRYPTPROV     *phCryptProv,
  _Out_     DWORD          *pdwKeySpec,
  _In_      BOOL           *pfDidCryptAcquire,
  _Out_opt_ LPWSTR         *ppwszTmpContainer,
  _Out_opt_ LPWSTR         *ppwszProviderName,
  _Out_     DWORD          *pdwProviderType
);
```



## Parameters

<dl> <dt>

*hwnd* \[in\]
</dt> <dd>

The handle of the window to use as the owner of any dialog boxes that are displayed. This member is not currently used and is ignored. It is safe to pass **NULL** for this parameter.

</dd> <dt>

*pCert* \[in\]
</dt> <dd>

A pointer to a [**CERT\_CONTEXT**](/windows/desktop/api/Wincrypt/ns-wincrypt-cert_context) structure for the certificate.

</dd> <dt>

*phCryptProv* \[out\]
</dt> <dd>

A pointer to an [**HCRYPTPROV**](hcryptprov.md) structure that is a handle to the CSP.

</dd> <dt>

*pdwKeySpec* \[out\]
</dt> <dd>

The specification of the private key to retrieve. Possible values include **AT\_KEYEXCHANGE** or **AT\_SIGNATURE**.

</dd> <dt>

*pfDidCryptAcquire* \[in\]
</dt> <dd>

A value that specifies whether the function acquired the provider handle based on the certificate.

</dd> <dt>

*ppwszTmpContainer* \[out, optional\]
</dt> <dd>

The address of a pointer to a null-terminated string for the temporary key container name. The **GetCryptProvFromCert** function provides and initializes the temporary container. When calling **GetCryptProvFromCert**, the address should point to a **NULL** value.

</dd> <dt>

*ppwszProviderName* \[out, optional\]
</dt> <dd>

The address of a pointer to a null-terminated string for the provider name. The **GetCryptProvFromCert** function returns the provider name. When calling **GetCryptProvFromCert**, the address should point to a **NULL** value.

</dd> <dt>

*pdwProviderType* \[out\]
</dt> <dd>

Specifies the CSP type. This can be zero or one of the [Cryptographic Provider Types](cryptographic-provider-types.md). If this member is zero, the key container is one of the CNG key storage providers.

</dd> </dl>

## Return value

Upon success, this function returns **TRUE**. The **GetCryptProvFromCert** function returns **FALSE** if it fails.

## Remarks

The [MakeCert](makecert.md) tool calls **GetCryptProvFromCert** when you invoke it by using the **-is** command line option.

If the *pfDidCryptAcquire* parameter is set to **TRUE**, the function sets *phCryptProv*, *pdwKeySpec*, and *pdwProviderType* parameters to the provider values.

When you have finished using the CSP, free it by calling the [**FreeCryptProvFromCert**](freecryptprovfromcert.md) function.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| DLL<br/>                      | <dl> <dt>Mssign32.dll</dt> </dl> |



 

 
