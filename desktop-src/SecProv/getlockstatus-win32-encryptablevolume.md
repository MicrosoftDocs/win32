---
description: Indicates whether the contents of the volume are accessible from Windows.
ms.assetid: 54b2a41b-11c6-40ec-97fa-74996c15554e
title: GetLockStatus method of the Win32_EncryptableVolume class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_EncryptableVolume.GetLockStatus
api_type: 
- COM
api_location: 
- Root\CIMV2\Security\MicrosoftVolumeEncryption
---

# GetLockStatus method of the Win32\_EncryptableVolume class

The **GetLockStatus** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class indicates whether the contents of the volume are accessible from Windows.

## Syntax


```mof
uint32 GetLockStatus(
  [out] uint32 LockStatus
);
```



## Parameters

<dl> <dt>

*LockStatus* \[out\]
</dt> <dd>

Type: **uint32**

Specifies whether the contents of the volume are accessible from Windows.



| Value                                                                                                                                                                                                                           | Meaning                                                                                                                                                                                                                                                                                                                                                                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Unlocked"></span><span id="unlocked"></span><span id="UNLOCKED"></span><dl> <dt>**Unlocked**</dt> <dt>0</dt> </dl> | For a standard HDD:<br/> The full contents of the volume are accessible. An unlocked volume is either fully decrypted or has the encryption key available in the clear on disk. The volume containing the current running operating system (for example, the running Windows volume) is always accessible and cannot be locked.<br/> For an EHDD:<br/> The band is perpetually unlocked.<br/> |
| <span id="Locked"></span><span id="locked"></span><span id="LOCKED"></span><dl> <dt>**Locked**</dt> <dt>1</dt> </dl>         | For a standard HDD:<br/> All or a portion of the contents of the volume are not accessible. A locked volume must be partially or fully encrypted and must not have the encryption key available in the clear on disk.<br/> For an EHDD:<br/> The band is unlocked or locked.<br/>                                                                                                             |



 

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following codes or another error code if it fails.



| Return code/value                                                                                                                                 | Description                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl> | The method was successful.<br/> |



 

## Remarks

Use the [**UnlockWithExternalKey**](unlockwithexternalkey-win32-encryptablevolume.md) and [**UnlockWithNumericalPassword**](unlockwithnumericalpassword-win32-encryptablevolume.md) to get access to the volume contents. Use the [**Lock**](lock-win32-encryptablevolume.md) method to relinquish access to volume contents.

The volume that contains the currently running operating system is always accessible and cannot be locked.

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

 

 
