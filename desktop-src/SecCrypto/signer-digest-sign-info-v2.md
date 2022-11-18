---
description: contains information about digest signing.
ms.assetid: 
title: SIGNER_SPC_CHAIN_INFO structure
ms.topic: reference
ms.date: 11/15/2022
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SIGNER_DIGEST_SIGN_INFO_V2
api_type: 
- NA
api_location: 
---

# SIGNER\_DIGEST\_SIGN\_INFO_V2 structure

The **SIGNER\_DIGEST\_SIGN\_INFO_V2** structure contains information about digest signing. It contains a pointer to a digest signing function implemented within the provided dll, specified by the dwDigestSignChoice. 

> [!Note]  
> This structure is not defined in any header file. To use this structure, you must define it yourself as shown in this topic.

 

## Syntax


```C++
   typedef struct SIGNER_DIGEST_SIGN_INFO_V2
    {
        DWORD cbSize;                                                
        PFN_AUTHENTICODE_DIGEST_SIGN pfnAuthenticodeDigestSign;      
        PFN_AUTHENTICODE_DIGEST_SIGN_EX pfnAuthenticodeDigestSignEx; 
        PCRYPT_DATA_BLOB pMetadataBlob;                              
    } SIGNER_DIGEST_SIGN_INFO_V2, *PSIGNER_DIGEST_SIGN_INFO_V2;


```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

The size, in bytes, of the structure.

</dd> <dt>

**pfnAuthenticodeDigestSign**
</dt> <dd>

Pointer to the PFN_AUTHENTICODE_DIGEST_SIGN callback function. Required if the caller of SignerSignEx3 specifies SPC_DIGEST_SIGN_FLAG in the dwFlags parameter. 

</dd> <dt>

**pfnAuthenticodeDigestSignEx**
</dt> <dd>

Pointer to the PFN_AUTHENTICODE_DIGEST_SIGN_EX callback function. Required if the caller of SignerSignEx3 specifies SPC_DIGEST_SIGN_EX_FLAG in the dwFlags parameter. 
</dd> <dt>

**pMetadataBlob**
</dt> <dd>

Optional pointer to CRYPT_DATA_BLOB specifying metadata.
  
</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 May 2020 Update \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2022 \[desktop apps only\]<br/>          |
| DLL                           | Mssign32.dll


<!-- 
## See also

<dl> <dt>

[**SIGNER\_CERT**](signer-cert.md)
</dt> </dl>

  -->

 
