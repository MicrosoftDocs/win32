---
title: NewByAcceptCertificates method of the MSFT\_HgsGuardian class
description: Creates a guardian.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'acaf21c3-6cde-4bdb-a8ae-7a7cdda71d48'
ms.prod: 'windows-server-dev'
ms.technology:
- 'host-guardian-service'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["NewByAcceptCertificates method", "NewByAcceptCertificates method, MSFT_HgsGuardian class", "MSFT_HgsGuardian class, NewByAcceptCertificates method"]
topic_type:
- apiref
api_name:
- MSFT_HgsGuardian.NewByAcceptCertificates
api_location:
- HgsClientWmi.dll
api_type:
- COM
---

# NewByAcceptCertificates method of the MSFT\_HgsGuardian class

Creates a guardian.

## Syntax


```mof
uint32 NewByAcceptCertificates(
  [in]  string           Name,
  [in]  string           EncryptionCertificate,
  [in]  string           SigningCertificate,
  [in]  string           SigningCertificatePassword,
  [in]  string           EncryptionCertificatePassword,
  [in]  boolean          AllowExpired,
  [in]  boolean          AllowUntrustedRoot,
  [out] MSFT_HgsGuardian cmdletOutput
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

A name to associate with this guardian when it is persisted to the guardian store.

</dd> <dt>

*EncryptionCertificate* \[in\]
</dt> <dd>

Password protected encryption certificate PFX file for the guardian that contains the public and private keys.

</dd> <dt>

*SigningCertificate* \[in\]
</dt> <dd>

Password protected Signing certificate PFX file for the guardian that contains the public and private keys.

</dd> <dt>

*SigningCertificatePassword* \[in\]
</dt> <dd>

Password to decrypt the Signing certificate PFX file.

</dd> <dt>

*EncryptionCertificatePassword* \[in\]
</dt> <dd>

Password to decrypt the Encryption certificate PFX file.

</dd> <dt>

*AllowExpired* \[in\]
</dt> <dd>

When specified, allows new guardian creation with certificates that are expired.

</dd> <dt>

*AllowUntrustedRoot* \[in\]
</dt> <dd>

When specified, allows new guardian to be created using self-signed certificates.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On success, returns a [**MSFT\_HgsGuardian**](msft-hgsguardian.md) instance containing the new Guardian object.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                              |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Hgs<br/>                                                    |
| MOF<br/>                      | <dl> <dt>HgsClientWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>HgsClientWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_HgsGuardian**](msft-hgsguardian.md)
</dt> </dl>

 

 





