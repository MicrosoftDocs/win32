---
description: Uses a provided external key to access the contents of a data volume.
ms.assetid: e383767e-8557-469c-bc44-f67591c46f23
title: UnlockWithExternalKey method of the Win32_EncryptableVolume class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_EncryptableVolume.UnlockWithExternalKey
api_type: 
- COM
api_location: 
- Root\CIMV2\Security\MicrosoftVolumeEncryption
---

# UnlockWithExternalKey method of the Win32\_EncryptableVolume class

The **UnlockWithExternalKey** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class uses a provided external key to access the contents of a data volume.

The volume's encryption key must have been secured with one or more key protectors of the type "External Key" using the [**ProtectKeyWithExternalKey**](protectkeywithexternalkey-win32-encryptablevolume.md) method to be able to unlock the volume with this method.

> [!Note]  
> If the disc supports hardware encryption this function sets the band status to "unlocked""

 

## Syntax


```mof
uint32 UnlockWithExternalKey(
  [in] uint8 ExternalKey[]
);
```



## Parameters

<dl> <dt>

*ExternalKey* \[in\]
</dt> <dd>

Type: **uint8\[\]**

An array of bytes that specifies the 256-bit external key used to unlock the volume. This key can be obtained by calling the [**GetExternalKeyFromFile**](getexternalkeyfromfile-win32-encryptablevolume.md) method.

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following codes or another error code if it fails.

If the volume is already unlocked, this method returns 0.



| Return code/value                                                                                                                                                                  | Description                                                                                                                                 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl>                                  | The method was successful.<br/>                                                                                                       |
| <dl> <dt>**ERROR\_NOT\_FOUND**</dt> <dt>No value given (0x)</dt> </dl>          | The volume does not have a key protector of the type "External Key".<br/>                                                             |
| <dl> <dt>**ERROR\_INVALID\_PASSWORD**</dt> <dt>No value given (0x)</dt> </dl>   | One or more key protectors of the type "External Key" exist, but the specified *ExternalKey* parameter cannot unlock the volume.<br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>2147942487 (0x80070057)</dt> </dl>          | The *ExternalKey* parameter is not an array of size 4.<br/>                                                                           |
| <dl> <dt>**FVE\_E\_NOT\_ACTIVATED**</dt> <dt>2150694920 (0x80310008)</dt> </dl> | BitLocker is not enabled on the volume. Add a key protector to enable BitLocker. <br/>                                                |



 

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

 

 
