---
title: MSFT\_HgsGuardian class
description: The principal to whom key rights can be assigned.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5e7f8377-b83f-465a-a179-53403666a539
ms.prod: windows-server-dev
ms.technology:
- host-guardian-service
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_HgsGuardian class
- MSFT_HgsGuardian class, described
topic_type:
- apiref
api_name:
- MSFT_HgsGuardian
- MSFT_HgsGuardian.Name
- MSFT_HgsGuardian.SigningCertificate
- MSFT_HgsGuardian.EncryptionCertificate
- MSFT_HgsGuardian.EncryptionCertificateSignature
- MSFT_HgsGuardian.EncryptionCertificateSignatureAlgorithm
- MSFT_HgsGuardian.HasPrivateSigningKey
api_location:
- HgsClientWmi.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_HgsGuardian class

The principal to whom key rights can be assigned.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("HgsClientWmi"), ClassVersion("1.0"), AMENDMENT]
class MSFT_HgsGuardian
{
  string  Name;
  uint8   SigningCertificate[];
  uint8   EncryptionCertificate[];
  string  EncryptionCertificateSignature;
  string  EncryptionCertificateSignatureAlgorithm;
  boolean HasPrivateSigningKey;
};
```

## Members

The **MSFT\_HgsGuardian** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_HgsGuardian** class has these methods.



| Method                                                                              | Description                                                                                          |
|:------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------|
| [**Export**](export-msft-hgsguardian.md)                                           | Exports a guardian to an XML file.<br/>                                                        |
| [**Import**](import-msft-hgsguardian.md)                                           | Imports a guardian from an XML file.<br/>                                                      |
| [**NewByAcceptCertificates**](msft-hgsguardian-newbyacceptcertificates.md)         | Creates a guardian.<br/>                                                                       |
| [**NewByCertificateThumbprints**](msft-hgsguardian-newbycertificatethumbprints.md) | Creates a new Guardian by using the certificates identified by the specified thumbprints.<br/> |
| [**NewByGenerateCertificates**](msft-hgsguardian-newbygeneratecertificates.md)     | Creates a guardian and a self-signed certificate.<br/>                                         |
| [**Remove**](remove-msft-hgsguardian.md)                                           | Removes a guardian that was persisted on this machine.<br/>                                    |



 

### Properties

The **MSFT\_HgsGuardian** class has these properties.

<dl> <dt>

**EncryptionCertificate**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a list of the encryption certificates.

</dd> <dt>

**EncryptionCertificateSignature**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the encryption certificate signature.

</dd> <dt>

**EncryptionCertificateSignatureAlgorithm**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the encryption certificate signature algorithm.

</dd> <dt>

**HasPrivateSigningKey**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Returns **true** if this guardian can be used as an owner for a key protector; otherwise, **false**.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Gets the friendly name.

</dd> <dt>

**SigningCertificate**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a list of the signing certificates.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                              |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Hgs<br/>                                                    |
| MOF<br/>                      | <dl> <dt>HgsClientWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>HgsClientWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[Host Guardian Service WMI Provider](hoster-guardian-service-wmi-provider-portal.md)
</dt> <dt>

[**MSFT\_HgsKeyProtector**](msft-hgskeyprotector.md)
</dt> <dt>

[**MSFT\_HgsKeyProtector::Grant**](grant-msft-hgskeyprotector.md)
</dt> <dt>

[**MSFT\_HgsKeyProtector::NewByGuardians**](msft-hgskeyprotector-newbyguardians.md)
</dt> <dt>

[**MSFT\_HgsKeyProtector::Revoke**](revoke-msft-hgskeyprotector.md)
</dt> </dl>

 

 





