---
description: Returns the name of the file that contains the external key.
ms.assetid: c02d8dca-f30b-4ab5-a770-1ec6ac0b81c6
title: GetExternalKeyFileName method of the Win32_EncryptableVolume class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_EncryptableVolume.GetExternalKeyFileName
api_type: 
- COM
api_location: 
- Root\CIMV2\Security\MicrosoftVolumeEncryption
---

# GetExternalKeyFileName method of the Win32\_EncryptableVolume class

The **GetExternalKeyFileName** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class returns the name of the file that contains the external key, if this external key is saved to a file location by using the [**SaveExternalKeyToFile**](saveexternalkeytofile-win32-encryptablevolume.md) method.

This method is only applicable for key protectors of the type "External Key", "TPM And PIN And Startup Key", or "TPM And Startup Key".

## Syntax


```mof
uint32 GetExternalKeyFileName(
  [in]  string VolumeKeyProtectorID,
  [out] string FileName
);
```



## Parameters

<dl> <dt>

*VolumeKeyProtectorID* \[in\]
</dt> <dd>

Type: **string**

A unique string identifier used to manage an encrypted volume key protector.

</dd> <dt>

*FileName* \[out\]
</dt> <dd>

Type: **string**

A string that specifies the name with extension but without the file path, of the file that contains the external key.

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following codes or another error code if it fails.



| Return code/value                                                                                                                                                                  | Description                                                                                                                                                            |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl>                                  | The method was successful.<br/>                                                                                                                                  |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>2147942487 (0x80070057)</dt> </dl>          | The *VolumeKeyProtectorID* parameter does not refer to a key protector of the type "External Key", "TPM And PIN And Startup Key", or "TPM And Startup Key".<br/> |
| <dl> <dt>**FVE\_E\_LOCKED\_VOLUME**</dt> <dt>2150694912 (0x80310000)</dt> </dl> | The volume is locked.<br/>                                                                                                                                       |
| <dl> <dt>**FVE\_E\_NOT\_ACTIVATED**</dt> <dt>2150694920 (0x80310008)</dt> </dl> | BitLocker is not enabled on the volume. Add a key protector to enable BitLocker. <br/>                                                                           |



 

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
</dt> <dt>

[**SaveExternalKeyToFile**](saveexternalkeytofile-win32-encryptablevolume.md)
</dt> </dl>

 

 
