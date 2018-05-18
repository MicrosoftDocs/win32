---
title: NewByCertificateThumbprints method of the MSFT\_HgsGuardian class
description: Creates a new guardian by using the certificates identified by the specified thumbprints.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '28bd59fb-2b9a-4f2b-9ed6-e0a709fd3768'
ms.prod: 'windows-server-dev'
ms.technology:
- 'host-guardian-service'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["NewByCertificateThumbprints method", "NewByCertificateThumbprints method, MSFT_HgsGuardian class", "MSFT_HgsGuardian class, NewByCertificateThumbprints method"]
---

# NewByCertificateThumbprints method of the MSFT\_HgsGuardian class

Creates a new guardian by using the certificates identified by the specified thumbprints.

## Syntax


```mof
uint32 NewByCertificateThumbprints(
  [in]  string           Name,
  [in]  string           SigningCertificateThumbprint,
  [in]  string           EncryptionCertificateThumbprint,
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

*SigningCertificateThumbprint* \[in\]
</dt> <dd>

The thumbprint of the signing certificate, for the guardian, containing the public and private keys.

</dd> <dt>

*EncryptionCertificateThumbprint* \[in\]
</dt> <dd>

The thumbprint of the encryption certificate, for the guardian, containing the public and private keys.

</dd> <dt>

*AllowExpired* \[in\]
</dt> <dd>

When specified allows new guardian creation with certificates that are expired.

</dd> <dt>

*AllowUntrustedRoot* \[in\]
</dt> <dd>

When specified allows new guardian to be created using self-signed certificates.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An [**MSFT\_HgsGuardian**](msft-hgsguardian.md) that contains the new guardian object.

</dd> </dl>

## Return value

TBD

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

 

 





