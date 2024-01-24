---
description: Writes the external key associated with the specified volume key protector to a system, hidden, read-only file in the specified folder.
ms.assetid: 8d928f85-b392-4119-aebb-f16021eb5c6a
title: SaveExternalKeyToFile method of the Win32_EncryptableVolume class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_EncryptableVolume.SaveExternalKeyToFile
api_type: 
- COM
api_location: 
- Root\CIMV2\Security\MicrosoftVolumeEncryption
---

# SaveExternalKeyToFile method of the Win32\_EncryptableVolume class

The **SaveExternalKeyToFile** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class writes the external key associated with the specified volume key protector to a system, hidden, read-only file in the specified folder.

This method is only applicable for key protectors of the type "External Key" or "TPM And Startup Key".

## Syntax


```mof
uint32 SaveExternalKeyToFile(
  [in] string VolumeKeyProtectorID,
  [in] string Path
);
```



## Parameters

<dl> <dt>

*VolumeKeyProtectorID* \[in\]
</dt> <dd>

Type: **string**

A unique string identifier used to manage an encrypted volume key protector.

</dd> <dt>

*Path* \[in\]
</dt> <dd>

Type: **string**

A string that contains the volume or folder location where the external key associated with the specified key protector is to be saved. This path does not include the name of the file, which is internal and may change from version to version. Use **GetExternalKeyFileName** to get the file name.

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following codes or another error code if it fails.



| Return code/value                                                                                                                                                                   | Description                                                                                                                                       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl>                                   | The method was successful.<br/>                                                                                                             |
| <dl> <dt>**FVE\_E\_LOCKED\_VOLUME**</dt> <dt>2150694912 (0x80310000)</dt> </dl>  | The volume is locked.<br/>                                                                                                                  |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>2147942487 (0x80070057)</dt> </dl>           | The *VolumeKeyProtectorID* parameter does not refer to a key protector of the type "External Key" or "TPM And Startup Key".<br/>            |
| <dl> <dt>**ERROR\_PATH\_NOT\_FOUND**</dt> <dt>2147942403 (0x80070003)</dt> </dl> | The *Path* parameter does not refer to a valid location.<br/> Ensure that the file name is not included in the *Path* parameter.<br/> |
| <dl> <dt>**FVE\_E\_NOT\_ACTIVATED**</dt> <dt>2150694920 (0x80310008)</dt> </dl>  | BitLocker is not enabled on the volume. Add a key protector to enable BitLocker. <br/>                                                      |



 

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

 

 
