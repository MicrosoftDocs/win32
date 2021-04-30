---
description: Determines whether the volume is located on a drive that supports or can support hardware encryption.
ms.assetid: C6007BC4-71CD-404A-A0E9-D9662906151F
title: GetHardwareEncryptionStatus method of the Win32_EncryptableVolume class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_EncryptableVolume.GetHardwareEncryptionStatus
api_type: 
- COM
api_location: 
- Root\CIMV2\Security\MicrosoftVolumeEncryption
---

# GetHardwareEncryptionStatus method of the Win32\_EncryptableVolume class

The **GetHardwareEncryptionStatus** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class determines whether the volume is located on a drive that supports or can support hardware encryption.

## Syntax


```mof
uint32 GetHardwareEncryptionStatus(
  [out] uint32 HardwareEncryptionStatus
);
```



## Parameters

<dl> <dt>

*HardwareEncryptionStatus* \[out\]
</dt> <dd>

Specifies whether the drive can support hardware encryption. This can be one of the following values.



| Value                                                                                                                                                                                                                                               | Meaning                                             |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <span id="Not_supported"></span><span id="not_supported"></span><span id="NOT_SUPPORTED"></span><dl> <dt>**Not supported**</dt> <dt>0</dt> </dl> | Hardware encryption is not supported.<br/>    |
| <span id="No_protection"></span><span id="no_protection"></span><span id="NO_PROTECTION"></span><dl> <dt>**No protection**</dt> <dt>1</dt> </dl> | Drive encryption is not supported.<br/>       |
| <span id="Uses_software"></span><span id="uses_software"></span><span id="USES_SOFTWARE"></span><dl> <dt>**Uses software**</dt> <dt>2</dt> </dl> | The encryption method is software-based.<br/> |
| <span id="Uses_hardware"></span><span id="uses_hardware"></span><span id="USES_HARDWARE"></span><dl> <dt>**Uses hardware**</dt> <dt>3</dt> </dl> | The drive supports hardware encryption.<br/>  |



 

</dd> </dl>

## Return value

This function returns zero (0) if the volume is compatible with BitLocker hardware encryption. Otherwise, the function returns an error.



| Return code/value                                                                                                                                 | Description                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl> | The volume is compatible with BitLocker hardware encryption.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 Enterprise, Windows 8 Pro \[desktop apps only\]<br/>                                    |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\CIMV2\\Security\\MicrosoftVolumeEncryption<br/>                                             |
| MOF<br/>                      | <dl> <dt>Win32\_encryptablevolume.mof</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_EncryptableVolume**](win32-encryptablevolume.md)
</dt> </dl>

 

 




