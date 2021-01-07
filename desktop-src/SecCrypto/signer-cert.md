---
description: Specifies a certificate used to sign a document. The certificate can be stored in a Software Publisher Certificate (SPC) file or in a certificate store.
ms.assetid: 9a99ce98-237d-4223-ab3d-0576041038e3
title: SIGNER_CERT structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SIGNER_CERT
api_type: 
- NA
api_location: 
---

# SIGNER\_CERT structure

The **SIGNER\_CERT** structure specifies a [*certificate*](../secgloss/c-gly.md) used to sign a document. The certificate can be stored in a [*Software Publisher Certificate*](../secgloss/s-gly.md) (SPC) file or in a [*certificate store*](../secgloss/c-gly.md).

> [!Note]  
> This structure is not defined in any header file. To use this structure, you must define it yourself as shown in this topic.

 

## Syntax


```C++
typedef struct _SIGNER_CERT {
  DWORD cbSize;
  DWORD dwCertChoice;
  union {
    LPCWSTR                pwszSpcFile;
    SIGNER_CERT_STORE_INFO *pCertStoreInfo;
    SIGNER_SPC_CHAIN_INFO  *pSpcChainInfo;
  };
  HWND  hwnd;
} SIGNER_CERT, *PSIGNER_CERT;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

The size, in bytes, of the structure.

</dd> <dt>

**dwCertChoice**
</dt> <dd>

Specifies how the certificate is stored. This member can be one or more of the following values.



| Value                                                                                                                                                                                                                                          | Meaning                                                                                                                                                                                                                                                                           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="SIGNER_CERT_SPC_FILE"></span><span id="signer_cert_spc_file"></span><dl> <dt>**SIGNER\_CERT\_SPC\_FILE**</dt> <dt>1</dt> </dl>    | The certificate is stored in an SPC file. The **pwszSpcFile** member contains the path and file name of the SPC file.<br/>                                                                                                                                                  |
| <span id="SIGNER_CERT_STORE"></span><span id="signer_cert_store"></span><dl> <dt>**SIGNER\_CERT\_STORE**</dt> <dt>2</dt> </dl>              | The certificate is stored in a certificate store. The **pCertStoreInfo** member contains a pointer to a [**SIGNER\_CERT\_STORE\_INFO**](signer-cert-store-info.md) structure that specifies the certificate store in which the certificate is stored.<br/>                 |
| <span id="SIGNER_CERT_SPC_CHAIN"></span><span id="signer_cert_spc_chain"></span><dl> <dt>**SIGNER\_CERT\_SPC\_CHAIN**</dt> <dt>3</dt> </dl> | The certificate is stored in an SPC file and is associated with a certificate chain. The **pSpcChainInfo** member contains a pointer to a [**SIGNER\_SPC\_CHAIN\_INFO**](signer-spc-chain-info.md) structure that contains the chain information for the certificate.<br/> |



 

</dd> <dt>

**pwszSpcFile**
</dt> <dd>

A pointer to a null-terminated Unicode string that contains the path and file name of the SPC file in which the certificate is stored. This member is only used if the **dwCertChoice** member contains **SIGNER\_CERT\_SPC\_FILE**.

</dd> <dt>

**pCertStoreInfo**
</dt> <dd>

A pointer to a [**SIGNER\_CERT\_STORE\_INFO**](signer-cert-store-info.md) structure that specifies the certificate store in which the certificate is stored. This member is only used if the **dwCertChoice** member contains **SIGNER\_CERT\_STORE**.

</dd> <dt>

**pSpcChainInfo**
</dt> <dd>

A pointer to a [**SIGNER\_SPC\_CHAIN\_INFO**](signer-spc-chain-info.md) structure that contains the chain information for the certificate. This member is only used if the **dwCertChoice** member contains **SIGNER\_CERT\_SPC\_CHAIN**.

</dd> <dt>

**hwnd**
</dt> <dd>

The handle of the window to use as the owner of any dialog boxes that are displayed. This member is not currently used and is ignored.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**SignerSign**](signersign.md)
</dt> <dt>

[**SignerSignEx**](signersignex.md)
</dt> </dl>

 

 
