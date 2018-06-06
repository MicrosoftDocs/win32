---
Description: Uses the provided certificate file to obtain the derived key and unlock the encrypted volume.
ms.assetid: 41811d38-5c89-4372-9dbc-3de45b05011f
title: UnlockWithCertificateFile method of the Win32\_EncryptableVolume class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# UnlockWithCertificateFile method of the Win32\_EncryptableVolume class

The **UnlockWithCertificateFile** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class uses the provided [*certificate*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb) file to obtain the derived key and unlock the encrypted volume.

> [!Note]  
> If the disc supports hardware encryption this function sets the band status to "unlocked""

 

## Syntax


```mof
uint32 UnlockWithCertificateFile(
  [in] string FileName,
  [in] string PIN
);
```



## Parameters

<dl> <dt>

*FileName* \[in\]
</dt> <dd>

Type: **string**

A string that specifies the location and name of the .cer file used to retrieve the certificate thumbprint. An [*encryption*](https://msdn.microsoft.com/f1caccd2-3453-448e-b194-bf899eff8091) certificate must be exported in .cer format ([*Distinguished Encoding Rules*](https://msdn.microsoft.com/d007cbb9-b547-4dc7-bc22-b526f650f7c2) (DER)-encoded binary [*X.509*](https://msdn.microsoft.com/28dba6ef-939f-4789-9789-ee6e0fef0177) or Base-64 encoded X.509). The encryption certificate may be generated from Microsoft PKI, third-party PKI, or self-signed.

</dd> <dt>

*PIN* \[in\]
</dt> <dd>

Type: **string**

A user-specified personal identification string. This string must consist of a sequence of 4 to 20 digits. This string is used to silently authenticate the [*key storage provider*](https://msdn.microsoft.com/f17042c3-ba1a-408f-af55-5f171b0dee33) (KSP) when used with a [*smart card*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50).

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following codes or another error code if it fails.



| Return code/value                                                                                                                                                                            | Description                                                                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl>                                            | The method was successful.<br/>                                                                                                                                                                                                                                    |
| <dl> <dt>**ERROR\_FILE\_NOT\_FOUND**</dt> <dt>0000000002 (0x2)</dt> </dl>                 | The system cannot file the specified file.<br/>                                                                                                                                                                                                                    |
| <dl> <dt>**FVE\_E\_NOT\_ACTIVATED**</dt> <dt>2150694920 (0x80310008)</dt> </dl>           | BitLocker is not enabled on the volume. Add a key protector to enable BitLocker. <br/>                                                                                                                                                                             |
| <dl> <dt>**FVE\_E\_FAILED\_AUTHENTICATION**</dt> <dt>2150694951 (0x80310027)</dt> </dl>   | The volume cannot be unlocked with the provided information. <br/>                                                                                                                                                                                                 |
| <dl> <dt>**FVE\_E\_PROTECTOR\_NOT\_FOUND**</dt> <dt>2150694963 (0x80310033)</dt> </dl>    | The provided key protector does not exist on the volume. You must enter another key protector.<br/>                                                                                                                                                                |
| <dl> <dt>**FVE\_E\_PRIVATEKEY\_AUTH\_FAILED**</dt> <dt>2150695060 (0x80310094)</dt> </dl> | The [*private key*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a), associated with the specified certificate, could not be authorized. The private key authorization was either not provided or the provided authorization was invalid.<br/> |



 

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

 

 




