---
description: The PFN_AUTHENTICODE_DIGEST_SIGN user supplied callback function implements digest signing.
ms.assetid: 7ebd19fa-af19-4873-bbed-f4ca2e951468
title: PFN_AUTHENTICODE_DIGEST_SIGN callback function
ms.topic: reference
ms.date: 11/18/2022
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PFN_AUTHENTICODE_DIGEST_SIGN
api_type: 
- UserDefined
api_location: 
---

# PFN\_AUTHENTICODE\_DIGEST\_SIGN callback function

The **PFN\_AUTHENTICODE\_DIGEST\_SIGN** user supplied callback function implements digest signing. You must implement this function as part of your provided dll. This function is currently called by [**SignerSignEx3**](signersignex3.md) for digest signing.

## Syntax


```C++
PFN_AUTHENTICODE_DIGEST_SIGN pfnAuthenticodeDigestSign; 

HRESULT __stdcall pfnAuthenticodeDigestSign(
    _In_ PCCERT_CONTEXT pSigningCert,                        
    _In_opt_ PCRYPT_DATA_BLOB pMetadataBlob,                 
    _In_ ALG_ID digestAlgId,                                 
    _In_ PBYTE pbToBeSignedDigest, 
    _In_ DWORD cbToBeSignedDigest,                           
    _Out_ PCRYPT_DATA_BLOB pSignedDigest                     
);

```



## Parameters

<dl> <dt>

*pSigningCert* \[in\]
</dt> <dd>

A pointer to a [**CERT\_CONTEXT**](/windows/desktop/api/Wincrypt/ns-wincrypt-cert_context) structure that specifies the certificate used to create the digital signature.

</dd> <dt>

*pMetadataBlob* \[in, optional\]
</dt> <dd>

Pointer to a [**CRYPT_DATA_BLOB**](/windows/win32/api/wincrypt/ns-wincrypt-crypt_integer_blob) structure that contains metadata for digest signing. 

</dd> <dt>

*digestAlgId* \[in\]
</dt> <dd>

Specifies the digest algorithm to be used for digest signing.

</dd> <dt>

*pbToBeSignedDigest* \[in\]
</dt> <dd>

Pointer to a buffer which contains the digest to be signed. 

</dd> <dt>

*cbToBeSignedDigest* \[in\]
</dt> <dd>

The size, in bytes, of the pbToBeSignedDigest buffer. 
</dd> <dt>

*pSignedDigest* \[out\]
</dt> <dd>

Pointer to [**CRYPT_DATA_BLOB**](/windows/win32/api/wincrypt/ns-wincrypt-crypt_integer_blob) which receives the signed digest.

</dd> </dl>

## Return value

If the function succeeds, the function returns S_OK.
If the function fails, it returns an HRESULT value that indicates the error. For a list of common error codes, see [Common HRESULT Values](https://learn.microsoft.com/en-us/windows/win32/seccrypto/common-hresult-values).


## Remarks  

The parameter `pSignedDigest->pbData` must be allocated by calling `HeapAlloc` passing the result of `GetProcessHeap()` as the first parameter. 


## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/> |
| DLL<br/>                      | Mssign32.dll                                   |



 

 


