---
description: Allows a data volume to be automatically unlocked when the volume is mounted.
ms.assetid: ec77b17f-545b-40a7-91b2-ff0b32b8370d
title: EnableAutoUnlock method of the Win32_EncryptableVolume class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_EncryptableVolume.EnableAutoUnlock
api_type: 
- COM
api_location: 
- Root\CIMV2\Security\MicrosoftVolumeEncryption
---

# EnableAutoUnlock method of the Win32\_EncryptableVolume class

The **EnableAutoUnlock** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class allows a data volume to be automatically unlocked when the volume is mounted.

Automatic unlocking saves an external key to the operating system that can automatically unlock the volume onto the currently running operating system volume.

To use this method, the operating system volume must already be protected by BitLocker Drive Encryption or must have encryption in progress. In addition, there must already exist an external key for the data volume. Use [**ProtectKeyWithExternalKey**](protectkeywithexternalkey-win32-encryptablevolume.md) to create the external key that can automatically unlock the volume.

## Syntax


```mof
uint32 EnableAutoUnlock(
  [in] string VolumeKeyProtectorID
);
```



## Parameters

<dl> <dt>

*VolumeKeyProtectorID* \[in\]
</dt> <dd>

Type: **string**

A string that identifies the key protector of the type "External Key" used to automatically unlock the volume.

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following codes or another error code if it fails.



| Return code/value                                                                                                                                                                           | Description                                                                                                                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl>                                           | The method was successful.<br/>                                                                                                                                        |
| <dl> <dt>**FVE\_E\_LOCKED\_VOLUME**</dt> <dt>2150694912 (0x80310000)</dt> </dl>          | The volume is locked.<br/>                                                                                                                                             |
| <dl> <dt>**FVE\_E\_NOT\_ACTIVATED**</dt> <dt>2150694920 (0x80310008)</dt> </dl>          | BitLocker is not enabled on the volume. Add a key protector to enable BitLocker. <br/>                                                                                 |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>2147942487 (0x80070057)</dt> </dl>                   | The *VolumeKeyProtectorID* parameter does not refer to a valid key protector of the type "External Key".<br/>                                                          |
| <dl> <dt>**FVE\_E\_NOT\_DATA\_VOLUME**</dt> <dt>2150694937 (0x80310019)</dt> </dl>       | The method cannot be run for the currently running operating system volume.<br/>                                                                                       |
| <dl> <dt>**FVE\_E\_OS\_NOT\_PROTECTED**</dt> <dt>2150694944 (0x80310020)</dt> </dl>      | The method cannot be run if the currently running operating system volume is not protected by BitLocker Drive Encryption or does not have encryption in progress.<br/> |
| <dl> <dt>**FVE\_E\_VOLUME\_BOUND\_ALREADY** </dt> <dt>2150694943 (0x8031001F)</dt> </dl> | Automatic unlocking on the volume has previously been enabled.<br/>                                                                                                    |



 

## Remarks

Given a valid volume key protector of the type "External Key", the related 256-bit external key is extracted from the protector and stored into the registry of the currently running operating system, along with the volume key protector ID.

If the external key associated with the volume key protector ID is deleted, the functionality to automatically unlock the volume is disabled or suspended.

> [!Note]  
> Removable media is not currently supported.

 

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

 

 
