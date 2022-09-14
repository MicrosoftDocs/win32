---
description: Disables or suspends all key protectors associated with this volume.
ms.assetid: 19eed858-a116-4ec8-937a-2eea7aadbdc6
title: DisableKeyProtectors method of the Win32_EncryptableVolume class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_EncryptableVolume.DisableKeyProtectors
api_type: 
- COM
api_location: 
- Root\CIMV2\Security\MicrosoftVolumeEncryption
---

# DisableKeyProtectors method of the Win32\_EncryptableVolume class

The **DisableKeyProtectors** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class disables or suspends all key protectors associated with this volume.

## Syntax


```mof
uint32 DisableKeyProtectors(
  [in, optional] uint32 DisableCount
);
```



## Parameters

<dl> <dt>

*DisableCount* \[in, optional\]
</dt> <dd>

Type: **uint32**

Integer that specifies the number of reboots for which the key protectors will be disabled. This parameter is only available on OS volumes.

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following codes or another error code if it fails.



| Return code/value                                                                                                                                                                  | Description                           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl>                                  | The method was successful.<br/> |
| <dl> <dt>**FVE\_E\_LOCKED\_VOLUME**</dt> <dt>2150694912 (0x80310000)</dt> </dl> | The volume is locked.<br/>      |



 

## Security Considerations

This method exposes the volume's encryption key in the clear on the hard disk, turning off any volume protection. We recommend against having any password or encryption key in plaintext.

## Remarks

New key protectors can be added even when key protectors are disabled or suspended. These key protectors will remain disabled unless [**EnableKeyProtectors**](enablekeyprotectors-win32-encryptablevolume.md) is called.

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Windows SDK. They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](../wmisdk/managed-object-format--mof-.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                                 |
| Namespace<br/>                | Root\\CIMV2\\Security\\MicrosoftVolumeEncryption<br/>                                             |
| MOF<br/>                      | <dl> <dt>Win32\_encryptablevolume.mof</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_EncryptableVolume**](win32-encryptablevolume.md)
</dt> <dt>

[**EnableKeyProtectors**](enablekeyprotectors-win32-encryptablevolume.md)
</dt> </dl>

 

 
