---
description: Specifies the certificate store used to sign a document.
ms.assetid: aabad010-6fa3-4677-bd73-b8c52d68dbc8
title: SIGNER_CERT_STORE_INFO structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SIGNER_CERT_STORE_INFO
api_type: 
- NA
api_location: 
---

# SIGNER\_CERT\_STORE\_INFO structure

The **SIGNER\_CERT\_STORE\_INFO** structure specifies the certificate store used to sign a document.

> [!Note]  
> This structure is not defined in any header file. To use this structure, you must define it yourself as shown in this topic.

 

## Syntax


```C++
typedef struct _SIGNER_CERT_STORE_INFO {
  DWORD          cbSize;
  PCCERT_CONTEXT pSigningCert;
  DWORD          dwCertPolicy;
  HCERTSTORE     hCertStore;
} SIGNER_CERT_STORE_INFO, *PSIGNER_CERT_STORE_INFO;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

The size, in bytes, of the structure.

</dd> <dt>

**pSigningCert**
</dt> <dd>

A pointer to a [**CERT\_CONTEXT**](/windows/desktop/api/Wincrypt/ns-wincrypt-cert_context) structure for the signing certificate.

</dd> <dt>

**dwCertPolicy**
</dt> <dd>

Specifies how certificates are added to the signature. To find the certificate chain, the MY, CA, ROOT, and SPC stores, in addition to the store specified by the **hCertStore** member, are checked. This member can be one or more of the following values.



| Value                                                                                                                                                                                                                                                                                   | Meaning                                                                                                                                                                                   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="SIGNER_CERT_POLICY_CHAIN"></span><span id="signer_cert_policy_chain"></span><dl> <dt>**SIGNER\_CERT\_POLICY\_CHAIN**</dt> <dt>2 (0x2)</dt> </dl>                           | Add only certificates in the certificate chain.<br/>                                                                                                                                |
| <span id="SIGNER_CERT_POLICY_CHAIN_NO_ROOT"></span><span id="signer_cert_policy_chain_no_root"></span><dl> <dt>**SIGNER\_CERT\_POLICY\_CHAIN\_NO\_ROOT**</dt> <dt>8 (0x8)</dt> </dl> | Add only certificates in the certificate chain, excluding the root certificate.<br/>                                                                                                |
| <span id="SIGNER_CERT_POLICY_STORE"></span><span id="signer_cert_policy_store"></span><dl> <dt>**SIGNER\_CERT\_POLICY\_STORE**</dt> <dt>1 (0x1)</dt> </dl>                           | Add all certificates in the store specified by the **hCertStore** member. This flag can be a bitwise-**OR** combination with any of the other possible values for this member.<br/> |



 

</dd> <dt>

**hCertStore**
</dt> <dd>

Optional. A handle to an additional certificate store.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**SIGNER\_CERT**](signer-cert.md)
</dt> </dl>

 

 




