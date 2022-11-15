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
- SIGNER_DIGEST_SIGN_INFO
api_type: 
- NA
api_location: 
---

# SIGNER\_DIGEST\_SIGN\_INFO structure

The **SIGNER\_DIGEST\_SIGN\_INFO** structure contains information about digest signing. It contains a pointer to a digest signing function implemented within the provided dll, specified by the dwDigestSignChoice. 

> [!Note]  
> This structure is not defined in any header file. To use this structure, you must define it yourself as shown in this topic.

 

## Syntax


```C++
typedef struct _SIGNER_DIGEST_SIGN_INFO
{
    DWORD cbSize;                                                
    DWORD dwDigestSignChoice;                                    
    union
    {
		PFN_AUTHENTICODE_DIGEST_SIGN pfnAuthenticodeDigestSign;                                   
        	PFN_AUTHENTICODE_DIGEST_SIGN_WITHFILEHANDLE pfnAuthenticodeDigestSignWithFileHandle;      
        PFN_AUTHENTICODE_DIGEST_SIGN_EX pfnAuthenticodeDigestSignEx;                              
        PFN_AUTHENTICODE_DIGEST_SIGN_EX_WITHFILEHANDLE pfnAuthenticodeDigestSignExWithFileHandle; 
    };
    PCRYPT_DATA_BLOB pMetadataBlob;                              
    DWORD dwReserved;                                            
    DWORD dwReserved2;
    DWORD dwReserved3;
}SIGNER_DIGEST_SIGN_INFO, *PSIGNER_DIGEST_SIGN_INFO;

```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

The size, in bytes, of the structure.

</dd> <dt>


**dwDigestSignChoice**
</dt> <dd>

Specifies which digest sign implementation to use.



| Value                                                                                                                                                                                                                                                                                   | Meaning                                                                                                                                                                                   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="DIGEST_SIGN"></span><span id="digest_sign"></span><dl> <dt>**DIGEST\_SIGN**</dt> <dt>1 (0x1)</dt> </dl>                                                                    | Use the DIGEST_SIGN implementation.<br/>                                                                                                                                |
| <span id="DIGEST_SIGN_WITHFILEHANDLE"></span><span id="digest_sign_withfilehandle"></span><dl> <dt>**DIGEST\_SIGN\_WITHFILEHANDLE**</dt> <dt>2 (0x2)</dt> </dl> | Use the DIGEST_SIGN_WITHFILEHANDLE implementation. <br/>                                                                                                |
| <span id="DIGEST_SIGN_EX"></span><span id="digest_sign_ex"></span><dl> <dt>**DIGEST\_SIGN\_EX**</dt> <dt>3 (0x3)</dt> </dl>                           | Use the DIGEST_SIGN_EX implementation.<br/> |
| <span id="DIGEST_SIGN_EX_WITHFILEHANDLE"></span><span id="digest_sign_ex_withfilehandle"></span><dl> <dt>**DIGEST\_SIGN\_EX\_WITHFILEHANDLE**</dt> <dt>4 (0x4)</dt> </dl>                           |Use the DIGEST_SIGN_EX_WITHFILEHANDLE implementation.<br/> |




 

</dd> <dt>

**pfnAuthenticodeDigestSign**
</dt> <dd>

Pointer to the PFN_AUTHENTICODE_DIGEST_SIGN callback function. Required if dwDigestSignChoice==DIGEST_SIGN.

</dd> <dt>

**pfnAuthenticodeDigestSignWithFileHandle**
</dt> <dd>

Pointer to the PFN_AUTHENTICODE_DIGEST_SIGN_WITHFILEHANDLE callback function. Required if dwDigestSignChoice==DIGEST_SIGN_WITHFILEHANDLE.

</dd> <dt>

**pfnAuthenticodeDigestSignEx**
</dt> <dd>

Pointer to the PFN_AUTHENTICODE_DIGEST_SIGN_EX callback function. Required if dwDigestSignChoice==DIGEST_SIGN_EX.

</dd> <dt>

**pfnAuthenticodeDigestSignExWithFileHandle**
</dt> <dd>

Pointer to the PFN_AUTHENTICODE_DIGEST_SIGN_EX_WITHFILEHANDLE callback function. Required if dwDigestSignChoice==DIGEST_SIGN_EX_WITHFILEHANDLE.

</dd> <dt>

**pMetadataBlob**
</dt> <dd>

Optional pointer to CRYPT_DATA_BLOB specifying metadata.
  
</dd> <dt>

**dwReserved**
</dt> <dd>

Reserved. This value must be zero (0).  
  
</dd> <dt>

**dwReserved2**
</dt> <dd>

Reserved. This value must be zero (0).  
  
</dd> <dt>

**dwReserved3**
</dt> <dd>

Reserved. This value must be zero (0).  
  
</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows 11 \[desktop apps only\]<br/>          |
| DLL                           | Mssign32.dll


<!-- 
## See also

<dl> <dt>

[**SIGNER\_CERT**](signer-cert.md)
</dt> </dl>

  -->

 
