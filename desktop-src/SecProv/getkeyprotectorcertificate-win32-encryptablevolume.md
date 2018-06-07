---
Description: Retrieves the public key and certificate thumbprint for a public key protector.
ms.assetid: 86fd0562-feb9-4b85-b27b-30270f864d8e
title: GetKeyProtectorCertificate method of the Win32\_EncryptableVolume class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetKeyProtectorCertificate method of the Win32\_EncryptableVolume class

The **GetKeyProtectorCertificate** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class retrieves the [*public key*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a) and [*certificate*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb) thumbprint for a public key protector.

## Syntax


```mof
uint32 GetKeyProtectorCertificate(
  [in]  string VolumeKeyProtectorID,
  [out] uint8  PublicKey[],
  [out] string CertThumbprint,
  [out] uint32 CertType
);
```



## Parameters

<dl> <dt>

*VolumeKeyProtectorID* \[in\]
</dt> <dd>

Type: **string**

A unique string identifier used to manage an encrypted volume key protector.

</dd> <dt>

*PublicKey* \[out\]
</dt> <dd>

Type: **uint8\[\]**

An array of bytes that specifies the public key.

</dd> <dt>

*CertThumbprint* \[out\]
</dt> <dd>

Type: **string**

A string that specifies the certificate thumbprint.

</dd> <dt>

*CertType* \[out\]
</dt> <dd>

Type: **uint32**

An unsigned integer that specifies the type of the key protector. This integer is used to differentiate between data recovery agent (DRA) and user certificates.



| Value                                                                        | Meaning                                  |
|------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt>1</dt> </dl> | The certificate is a DRA.<br/>     |
| <dl> <dt>2</dt> </dl> | The certificate is not a DRA.<br/> |



 

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following codes or another error code if it fails.



| Return code/value                                                                                                                                                                                       | Description                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl>                                                       | The method was successful.<br/>                                                                           |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>2147942487 (0x80070057)</dt> </dl>                               | The specified key protector is not a key protector. You must enter another key protector.<br/>            |
| <dl> <dt>**FVE\_E\_LOCKED\_VOLUME**</dt> <dt>2150694912 (0x80310000)</dt> </dl>                      | This drive is locked by BitLocker Drive Encryption. You must unlock this volume from Control Panel. <br/> |
| <dl> <dt>**FVE\_E\_NOT\_ACTIVATED**</dt> <dt>2150694920 (0x80310008)</dt> </dl>                      | BitLocker is not enabled on the volume. Add a key protector to enable BitLocker. <br/>                    |
| <dl> <dt>**FVE\_E\_POLICY\_USER\_CERTIFICATE\_REQUIRED**</dt> <dt>2150695027 (0x80310073)</dt> </dl> | Group Policy requires the use of a user certificate, such as a smart card.<br/>                           |



 

## Remarks

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Windows SDK. They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](https://msdn.microsoft.com/26494142-2078-4d46-a794-e43973255c2d).

## Requirements



|                                     |                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 Enterprise, Windows 7 Ultimate \[desktop apps only\]<br/>                               |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                 |
| Namespace<br/>                | Root\\CIMV2\\Security\\MicrosoftVolumeEncryption<br/>                                             |
| MOF<br/>                      | <dl> <dt>Win32\_encryptablevolume.mof</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_EncryptableVolume**](win32-encryptablevolume.md)
</dt> </dl>

 

 




