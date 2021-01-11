---
description: Resumes the encryption or decryption of a volume.
ms.assetid: e37f3e32-5510-431e-9782-11908e65300d
title: ResumeConversion method of the Win32_EncryptableVolume class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_EncryptableVolume.ResumeConversion
api_type: 
- COM
api_location: 
- Root\CIMV2\Security\MicrosoftVolumeEncryption
---

# ResumeConversion method of the Win32\_EncryptableVolume class

The **ResumeConversion** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class resumes the encryption or decryption of a volume.

> [!Note]  
> If the disc supports hardware encryption, this function can resume a wiping operation only. For more information, see [**PauseConversion**](pauseconversion-win32-encryptablevolume.md).

 

## Syntax


```mof
uint32 ResumeConversion();
```



## Parameters

This method has no parameters.

## Return value

Type: **uint32**

This method returns one of the following codes or another error code if it fails.

If this method is used on a fully encrypted or fully decrypted volume, or if encryption/decryption is already in progress on the volume, 0 is returned assuming no other errors occur.



| Return code/value                                                                                                                                                                  | Description                           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl>                                  | The method was successful.<br/> |
| <dl> <dt>**FVE\_E\_LOCKED\_VOLUME**</dt> <dt>2150694912 (0x80310000)</dt> </dl> | The volume is locked.<br/>      |



 

## Remarks

If this method is used on a volume with paused encryption/decryption, successfully running this method causes [**GetConversionStatus**](getconversionstatus-win32-encryptablevolume.md) to indicate that encryption or decryption is in progress.

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

 

 
