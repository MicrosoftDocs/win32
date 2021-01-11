---
description: Indicates whether the volume is automatically unlocked when it is mounted.
ms.assetid: cba04d77-1e7c-4191-8eb7-b8c43694193f
title: IsAutoUnlockEnabled method of the Win32_EncryptableVolume class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_EncryptableVolume.IsAutoUnlockEnabled
api_type: 
- COM
api_location: 
- Root\CIMV2\Security\MicrosoftVolumeEncryption
---

# IsAutoUnlockEnabled method of the Win32\_EncryptableVolume class

The **IsAutoUnlockEnabled** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class indicates whether the volume is automatically unlocked when it is mounted (for example, when removable memory devices are connected to the computer).

## Syntax


```mof
uint32 IsAutoUnlockEnabled(
  [out] boolean IsAutoUnlockEnabled,
  [out] string  VolumeKeyProtectorID
);
```



## Parameters

<dl> <dt>

*IsAutoUnlockEnabled* \[out\]
</dt> <dd>

Type: **boolean**

A Boolean value that is true if the external key used to automatically unlock the volume exists and has been stored in the currently running operating system volume, otherwise it is false.

</dd> <dt>

*VolumeKeyProtectorID* \[out\]
</dt> <dd>

Type: **string**

A unique string identifier that contains the associated encrypted volume key protector ID if *IsAutoUnlockEnabled* is true.

If *IsAutoUnlockEnabled* is false, *VolumeKeyProtectorID* is an empty string.

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following codes or another error code if it fails.



| Return code/value                                                                                                                                                                     | Description                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl>                                     | The method was successful.<br/>                                                       |
| <dl> <dt>**FVE\_E\_NOT\_ACTIVATED**</dt> <dt>2150694920 (0x80310008)</dt> </dl>    | BitLocker is not enabled on the volume. Add a key protector to enable BitLocker.<br/> |
| <dl> <dt>**FVE\_E\_NOT\_DATA\_VOLUME**</dt> <dt>2150694937 (0x80310019)</dt> </dl> | The method cannot be run for the currently running operating system volume.<br/>      |



 

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

 

 
