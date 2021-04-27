---
description: ProtectKeyWithCertificateThumbprint method of the Win32_EncryptableVolume class - Validates the Enhanced Key Usage (EKU) object identifier (OID) of the provided certificate.
ms.assetid: 7096cead-c44a-404c-b1e1-3e0ab27070f8
title: ProtectKeyWithCertificateThumbprint method of the Win32_EncryptableVolume class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_EncryptableVolume.ProtectKeyWithCertificateThumbprint
api_type: 
- COM
api_location: 
- Root\CIMV2\Security\MicrosoftVolumeEncryption
---

# ProtectKeyWithCertificateThumbprint method of the Win32\_EncryptableVolume class

The **ProtectKeyWithCertificateThumbprint** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class validates the Enhanced Key Usage (EKU) [*object identifier*](../secgloss/o-gly.md) (OID) of the provided certificate.

## Syntax


```mof
uint32 ProtectKeyWithCertificateThumbprint(
  [in, optional] string FriendlyName,
  [in]           string CertThumbprint,
  [out]          string VolumeKeyProtectorID
);
```



## Parameters

<dl> <dt>

*FriendlyName* \[in, optional\]
</dt> <dd>

Type: **string**

A string that specifies a user-assigned string identifier for this key protector. If this parameter is not specified, the *FriendlyName* parameter is created by using the Subject Name in the certificate.

</dd> <dt>

*CertThumbprint* \[in\]
</dt> <dd>

Type: **string**

A string that specifies the certificate thumbprint.

</dd> <dt>

*VolumeKeyProtectorID* \[out\]
</dt> <dd>

Type: **string**

A string that uniquely identifies the created key protector that can be used to manage this key protector.

If the drive supports hardware encryption and BitLocker has not taken band ownership, the ID string is set to "BitLocker" and the key protector is written to per band metadata.

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following codes or another error code if it fails.



| Return code/value                                                                                                                                                                                           | Description                                                                                                                                                                                                                                                                                    |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl>                                                           | The method was successful.<br/>                                                                                                                                                                                                                                                          |
| <dl> <dt>**ERROR\_INVALID\_DATA**</dt> <dt>13 (0xD)</dt> </dl>                                           | The data is not valid.<br/>                                                                                                                                                                                                                                                              |
| <dl> <dt>**FVE\_E\_NON\_BITLOCKER\_OID**</dt> <dt>2150695022 (0x8031006E)</dt> </dl>                     | The EKU attribute of the specified certificate does not permit it to be used for BitLocker Drive Encryption. BitLocker does not require that a certificate have an EKU attribute, but if one is configured, it must be set to an OID that matches the OID configured for BitLocker.<br/> |
| <dl> <dt>**FVE\_E\_POLICY\_USER\_CERTIFICATE\_NOT\_ALLOWED**</dt> <dt>2150695026 (0x80310072)</dt> </dl> | Group Policy does not permit user certificates, such as smart cards, to be used with BitLocker.<br/>                                                                                                                                                                                     |
| <dl> <dt>**FVE\_E\_POLICY\_USER\_CERT\_MUST\_BE\_HW**</dt> <dt>2150695028 (0x80310074)</dt> </dl>        | Group Policy requires that you supply a smart card to use BitLocker.<br/>                                                                                                                                                                                                                |
| <dl> <dt>**FVE\_E\_POLICY\_PROHIBITS\_SELFSIGNED**</dt> <dt>2150695046 (0x80310086)</dt> </dl>           | Group Policy does not permit the use of self-signed certificates.<br/>                                                                                                                                                                                                                   |



 

## Remarks

If the OID does not match the one associated with the service controller in the registry, this method fails. This prevents the user from setting data recovery agent (DRA) protectors manually on the volume. DRAs are only to be set by the service.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 Enterprise, Windows 7 Ultimate \[desktop apps only\]<br/>                               |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                 |
| Namespace<br/>                | Root\\CIMV2\\Security\\MicrosoftVolumeEncryption<br/>                                             |
| MOF<br/>                      | <dl> <dt>Win32\_encryptablevolume.mof</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_EncryptableVolume**](win32-encryptablevolume.md)
</dt> </dl>

 

 
