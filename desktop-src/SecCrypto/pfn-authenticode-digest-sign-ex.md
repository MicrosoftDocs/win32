---
description: The PFN_AUTHENTICODE_DIGEST_SIGN_EX user supplied callback function implements digest signing.
ms.assetid: fa3064d5-2d6b-4a56-8d6d-b30da750bc91
title: PFN_AUTHENTICODE_DIGEST_SIGN_EX callback function
ms.topic: reference
ms.date: 11/18/2022
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PFN_AUTHENTICODE_DIGEST_SIGN_EX
api_type: 
- UserDefined
api_location: 
---

# PFN\_AUTHENTICODE\_DIGEST\_SIGN\_EX callback function

The **AuthenticodeDigestSignEx** user supplied callback function implements digest signing. You must implement this function as part of your provided dll. This function is currently called by [**SignerSignEx3**](signersignex3.md) for digest signing.

## Syntax


```C++
PFN_AUTHENTICODE_DIGEST_SIGN_EX pfnAuthenticodeDigestSignEx;

HRESULT __stdcall pfnAuthenticodeDigestSignEx(
    _In_opt_ PCRYPT_DATA_BLOB pMetadataBlob,         
    _In_ ALG_ID digestAlgId,                                 
    _In_ PBYTE pbToBeSignedDigest, 
    _In_ DWORD cbToBeSignedDigest,                           
    _Out_ PCRYPT_DATA_BLOB pSignedDigest,                    
    _Out_ PCCERT_CONTEXT* ppSignerCert,                      
    _Inout_ HCERTSTORE hCertChainStore                       
);


```



## Parameters

<dl> <dt>

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

</dd> <dt>

*ppSignerCert* \[out\]
</dt> <dd>

Pointer to [**PCCERT_CONTEXT\***](/windows/win32/api/wincrypt/ns-wincrypt-cert_context) which receives the certificate chain signing certificate.

</dd> <dt>

*hCertChainStore* \[in, out, optional\]
</dt> <dd>

Optional, receives the cert chain of the signer cert.  

</dd> </dl>

## Return value

If the function succeeds, the function returns S_OK.
If the function fails, it returns an HRESULT value that indicates the error. For a list of common error codes, see [Common HRESULT Values](https://learn.microsoft.com/en-us/windows/win32/seccrypto/common-hresult-values).


## Remarks  

The parameter pSignedDigest->pbData must be allocated by calling HeapAlloc passing the result of GetProcessHeap() as the first parameter. The parameter \*ppSignerCert will be freed by the caller by calling CertFreeCertificateContext.


## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 May 2020 Update\[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2022 \[desktop apps only\]<br/> |
| DLL<br/>                      | Mssign32.dll                                   |



 

 


