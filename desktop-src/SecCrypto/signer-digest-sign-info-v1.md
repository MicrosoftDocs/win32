---
description: Specifies the SIGNER_DIGEST_SIGN_INFO_V1 structure that contains information about digest signing.
ms.assetid: 69c7e44f-be55-49cf-8e2f-a061a0c5907f
title: SIGNER_DIGEST_SIGN_INFO_V1 structure
ms.topic: reference
ms.date: 11/15/2022
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SIGNER_DIGEST_SIGN_INFO_V1
api_type: 
- NA
api_location: 
---

# SIGNER\_DIGEST\_SIGN\_INFO\_V1 structure

The **SIGNER\_DIGEST\_SIGN\_INFO\_V1** structure contains information about digest signing. It contains a pointer to a digest signing function implemented within the provided dll.

> [!Note]  
> This structure is not defined in any header file. To use this structure, you must define it yourself as shown in this topic.

 

## Syntax


```C++
typedef struct SIGNER_DIGEST_SIGN_INFO_V1
    {
        DWORD cbSize;                                                //Required: should be set to sizeof(SIGNER_DIGEST_SIGN_INFO_V1)
        PFN_AUTHENTICODE_DIGEST_SIGN pfnAuthenticodeDigestSign;      //Required: pointer to AuthenticodeDigestSign function
        PCRYPT_DATA_BLOB pMetadataBlob;                              //Optional: metadata blob (opaque to SignerSignEx3)
    } SIGNER_DIGEST_SIGN_INFO_V1, *PSIGNER_DIGEST_SIGN_INFO_V1;


```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

The size, in bytes, of the structure.

</dd> <dt>

**pMetadataBlob**
</dt> <dd>

Optional pointer to [**CRYPT_DATA_BLOB**](/windows/win32/api/wincrypt/ns-wincrypt-crypt_integer_blob) specifying metadata.
  
</dd>  </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]      |
| DLL                           | Mssign32.dll



<!-- ## See also

<dl> <dt>

[**SIGNER\_CERT**](signer-cert.md)
</dt> </dl> -->

 

 
