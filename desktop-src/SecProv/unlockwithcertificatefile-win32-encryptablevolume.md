---
Description: 'Uses the provided certificate file to obtain the derived key and unlock the encrypted volume.'
ms.assetid: '41811d38-5c89-4372-9dbc-3de45b05011f'
title: 'UnlockWithCertificateFile method of the Win32\_EncryptableVolume class'
---

# UnlockWithCertificateFile method of the Win32\_EncryptableVolume class

The **UnlockWithCertificateFile** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class uses the provided [*certificate*](security.c_gly#-security-certificate-gly) file to obtain the derived key and unlock the encrypted volume.

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

A string that specifies the location and name of the .cer file used to retrieve the certificate thumbprint. An [*encryption*](security.e_gly#-security-encryption-gly) certificate must be exported in .cer format ([*Distinguished Encoding Rules*](security.d_gly#-security-distinguished-encoding-rules-gly) (DER)-encoded binary [*X.509*](security.x_gly#-security-x-509-gly) or Base-64 encoded X.509). The encryption certificate may be generated from Microsoft PKI, third-party PKI, or self-signed.

</dd> <dt>

*PIN* \[in\]
</dt> <dd>

Type: **string**

A user-specified personal identification string. This string must consist of a sequence of 4 to 20 digits. This string is used to silently authenticate the [*key storage provider*](security.k_gly#-security-key-storage-provider-gly) (KSP) when used with a [*smart card*](security.s_gly#-security-smart-card-gly).

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
| <dl> <dt>**FVE\_E\_PRIVATEKEY\_AUTH\_FAILED**</dt> <dt>2150695060 (0x80310094)</dt> </dl> | The [*private key*](security.p_gly#-security-private-key-gly), associated with the specified certificate, could not be authorized. The private key authorization was either not provided or the provided authorization was invalid.<br/> |



 

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

 

 




