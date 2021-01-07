---
description: Indicates the encryption algorithm and key size used on the volume.
ms.assetid: 89df3dfc-4789-4d3c-b267-d8e26758e754
title: GetEncryptionMethod method of the Win32_EncryptableVolume class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_EncryptableVolume.GetEncryptionMethod
api_type: 
- COM
api_location: 
- Root\CIMV2\Security\MicrosoftVolumeEncryption
---

# GetEncryptionMethod method of the Win32\_EncryptableVolume class

The **GetEncryptionMethod** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class indicates the encryption algorithm and key size used on the volume.

## Syntax


```mof
uint32 GetEncryptionMethod(
  [out] uint32 EncryptionMethod,
  [out] string SelfEncryptionDriveEncryptionMethod
);
```



## Parameters

<dl> <dt>

*EncryptionMethod* \[out\]
</dt> <dd>

Type: **uint32**

An unsigned integer that specifies the encryption algorithm and key size used on the volume.



| Value                                                                                                                                                                                                                                          | Meaning                                                                                                                                                                                                                                                           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="None"></span><span id="none"></span><span id="NONE"></span><dl> <dt>**None**</dt> <dt>0</dt> </dl>                                | The volume is not encrypted.<br/>                                                                                                                                                                                                                           |
| <span id="AES_128_WITH_DIFFUSER"></span><span id="aes_128_with_diffuser"></span><dl> <dt>**AES\_128\_WITH\_DIFFUSER**</dt> <dt>1</dt> </dl> | The volume has been fully or partially encrypted with the Advanced Encryption Standard (AES) algorithm enhanced with a diffuser layer, using an AES key size of 128 bits. This method is no longer available on devices running Windows 8.1 or higher.<br/> |
| <span id="AES_256_WITH_DIFFUSER"></span><span id="aes_256_with_diffuser"></span><dl> <dt>**AES\_256\_WITH\_DIFFUSER**</dt> <dt>2</dt> </dl> | The volume has been fully or partially encrypted with the Advanced Encryption Standard (AES) algorithm enhanced with a diffuser layer, using an AES key size of 256 bits. This method is no longer available on devices running Windows 8.1 or higher.<br/> |
| <span id="AES_128"></span><span id="aes_128"></span><dl> <dt>**AES\_128**</dt> <dt>3</dt> </dl>                                             | The volume has been fully or partially encrypted with the Advanced Encryption Standard (AES) algorithm, using an AES key size of 128 bits.<br/>                                                                                                             |
| <span id="AES_256"></span><span id="aes_256"></span><dl> <dt>**AES\_256**</dt> <dt>4</dt> </dl>                                             | The volume has been fully or partially encrypted with the Advanced Encryption Standard (AES) algorithm, using an AES key size of 256 bits.<br/>                                                                                                             |
| <span id="HARDWARE_ENCRYPTION"></span><span id="hardware_encryption"></span><dl> <dt>**HARDWARE\_ENCRYPTION**</dt> <dt>5</dt> </dl>         | The volume has been fully or partially encrypted by using the hardware capabilities of the drive.<br/>                                                                                                                                                      |
| <span id="XTS_AES_128"></span><span id="xts_aes_128"></span><dl> <dt>**XTS\_AES\_128**</dt> <dt>6</dt> </dl>                                | The volume has been fully or partially encrypted with XTS using the Advanced Encryption Standard (AES), and an AES key size of 128 bits. This method is only available on devices running Windows 10, version 1511 or higher.<br/>                          |
| <span id="XTS_AES_256"></span><span id="xts_aes_256"></span><dl> <dt>**XTS\_AES\_256**</dt> <dt>7</dt> </dl>                                | The volume has been fully or partially encrypted with XTS using the Advanced Encryption Standard (AES), and an AES key size of 256 bits. This method is only available on devices running Windows 10, version 1511 or higher.<br/>                          |
| <dl> <dt>(uint32)–1</dt> </dl>                                                                                                                                                          | UNKNOWN<br/> The volume has been fully or partially encrypted with an unknown algorithm and key size.<br/>                                                                                                                                            |



 

</dd> <dt>

*SelfEncryptionDriveEncryptionMethod* \[out\]
</dt> <dd>

Type: **string**

The encryption algorithm is configured on the self-encrypting drive. A null string means that either BitLocker is using software encryption or no encryption method is reported.

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following codes or another error code if it fails.



| Return code/value                                                                                                                                 | Description                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl> | The method was successful.<br/> |



 

## Remarks

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Windows SDK. They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](../wmisdk/managed-object-format--mof-.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista Enterprise, Windows Vista Ultimate \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\CIMV2\\Security\\MicrosoftVolumeEncryption<br/>                                             |
| MOF<br/>                      | <dl> <dt>Win32\_encryptablevolume.mof</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_EncryptableVolume**](win32-encryptablevolume.md)
</dt> </dl>

 

 
