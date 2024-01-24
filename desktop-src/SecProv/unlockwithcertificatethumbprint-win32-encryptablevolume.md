---
description: Uses the provided certificate thumbprint to obtain the derived key and unlock the encrypted volume.
ms.assetid: 41c25d17-db1b-427e-907b-a547483927e0
title: UnlockWithCertificateThumbprint method of the Win32_EncryptableVolume class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_EncryptableVolume.UnlockWithCertificateThumbprint
api_type: 
- COM
api_location: 
- Root\CIMV2\Security\MicrosoftVolumeEncryption
---

# UnlockWithCertificateThumbprint method of the Win32\_EncryptableVolume class

The **UnlockWithCertificateThumbprint** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class uses the provided [*certificate*](../secgloss/c-gly.md) thumbprint to obtain the derived key and unlock the encrypted volume.

> [!Note]  
> If the disc supports hardware encryption this function sets the band status to "unlocked""

 

## Syntax


```mof
uint32 UnlockWithCertificateThumbprint(
  [in] string CertThumbprint,
  [in] string PIN
);
```



## Parameters

<dl> <dt>

*CertThumbprint* \[in\]
</dt> <dd>

Type: **string**

A thumbprint value of 0 is accepted and results in a search of the local store for the appropriate certificate. If a single BitLocker certificate is found, the search is successful. If none or more than one certificate is found, the method fails.

</dd> <dt>

*PIN* \[in\]
</dt> <dd>

Type: **string**

A user-specified personal identification string. This string must consist of a sequence of 4 to 20 digits. This string is used to silently authenticate the [*key storage provider*](../secgloss/k-gly.md) (KSP) when used with a [*smart card*](../secgloss/s-gly.md).

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following codes or another error code if it fails.



| Return code/value                                                                                                                                                                            | Description                                                                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl>                                            | The method was successful.<br/>                                                                                                                                                                                                                                    |
| <dl> <dt>**FVE\_E\_NOT\_ACTIVATED**</dt> <dt>2150694920 (0x80310008)</dt> </dl>           | BitLocker is not enabled on the volume. Add a key protector to enable BitLocker. <br/>                                                                                                                                                                             |
| <dl> <dt>**FVE\_E\_FAILED\_AUTHENTICATION**</dt> <dt>2150694951 (0x80310027)</dt> </dl>   | The volume cannot be unlocked by using the provided information. <br/>                                                                                                                                                                                             |
| <dl> <dt>**FVE\_E\_PROTECTOR\_NOT\_FOUND**</dt> <dt>2150694963 (0x80310033)</dt> </dl>    | The provided key protector does not exist on the volume. You must enter another key protector.<br/>                                                                                                                                                                |
| <dl> <dt>**FVE\_E\_PRIVATEKEY\_AUTH\_FAILED**</dt> <dt>2150695060 (0x80310094)</dt> </dl> | The [*private key*](../secgloss/p-gly.md) associated with the specified certificate could not be authorized. The private key authorization was either not provided or the provided authorization was not valid.<br/> |



 

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

 

 
