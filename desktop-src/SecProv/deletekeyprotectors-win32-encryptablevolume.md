---
description: Deletes all key protectors for the volume.
ms.assetid: 46f61899-87ff-4e86-8409-635117cff4de
title: DeleteKeyProtectors method of the Win32_EncryptableVolume class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_EncryptableVolume.DeleteKeyProtectors
api_type: 
- COM
api_location: 
- Root\CIMV2\Security\MicrosoftVolumeEncryption
---

# DeleteKeyProtectors method of the Win32\_EncryptableVolume class

The **DeleteKeyProtectors** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class deletes all key protectors for the volume.

If an unencrypted volume has key protectors, when **DeleteKeyProtectors** is run successfully the volume reverts to a standard NTFS file system.

If the volume is not yet fully decrypted, use [**DisableKeyProtectors**](disablekeyprotectors-win32-encryptablevolume.md) before running **DeleteKeyProtectors** to ensure that encrypted portions of the volume remain accessible.

## Syntax


```mof
uint32 DeleteKeyProtectors();
```



## Parameters

This method has no parameters.

## Return value

Type: **uint32**

This method returns one of the following codes or another error code if it fails.



| Return code/value                                                                                                                                                                          | Description                                                                                                                                                                                                                                                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl>                                          | The method was successful.<br/>                                                                                                                                                                                                                                                                                     |
| <dl> <dt>**FVE\_E\_LOCKED\_VOLUME**</dt> <dt>2150694912 (0x80310000)</dt> </dl>         | The volume is locked.<br/>                                                                                                                                                                                                                                                                                          |
| <dl> <dt>**FVE\_E\_KEY\_REQUIRED**</dt> <dt>2150694941 (0x8031001D)</dt> </dl>          | The last key protector for a partially or fully encrypted volume cannot be removed if key protectors are enabled. Use [**DisableKeyProtectors**](disablekeyprotectors-win32-encryptablevolume.md) before removing this last key protector to ensure that encrypted portions of the volume remain accessible. <br/> |
| <dl> <dt>**FVE\_E\_VOLUME\_BOUND\_ALREADY**</dt> <dt>2150694943 (0x8031001F)</dt> </dl> | Key protectors cannot be deleted because one of them is being used to automatically unlock the volume. <br/> Use [**DisableAutoUnlock**](disableautounlock-win32-encryptablevolume.md) to disable automatic unlocking before running this method.<br/>                                                       |



 

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

 

 
