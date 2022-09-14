---
description: Exports information that may help salvage encrypted data when the drive is severely damaged and no data backup files exist.
ms.assetid: 3d376a02-3392-433e-b842-24c73074610c
title: GetKeyPackage method of the Win32_EncryptableVolume class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_EncryptableVolume.GetKeyPackage
api_type: 
- COM
api_location: 
- Root\CIMV2\Security\MicrosoftVolumeEncryption
---

# GetKeyPackage method of the Win32\_EncryptableVolume class

The **GetKeyPackage** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class exports information that may help salvage encrypted data when the drive is severely damaged and no data backup files exist.

The exported information consists of the volume's encryption key secured by a key protector of the type "Numerical Password" or "External Key". To make use of this package, you must also save the corresponding numerical password or external key.

> [!IMPORTANT]
> If you choose to export a key package, make certain to keep this information in a well-protected location. Do not carry this information with your computer. If this key package is lost or stolen, you will need to decrypt the volume and reencrypt it by using a new key.

 

In the event of a drive failure, the BitLocker Repair Tool exists to help salvage available data. For more information about how this tool can use the key package, see [How to use the BitLocker Repair Tool to help recover data from an encrypted volume in Windows Vista](https://support.microsoft.com/kb/928201).

## Syntax


```mof
uint32 GetKeyPackage(
  [in]  string VolumeKeyProtectorID,
  [out] uint8  KeyPackage[]
);
```



## Parameters

<dl> <dt>

*VolumeKeyProtectorID* \[in\]
</dt> <dd>

Type: **string**

A unique string identifier used to manage an encrypted volume key protector. To export a key package, you must use a key protector of type "Numerical Password" or "External Key".

</dd> <dt>

*KeyPackage\[\]* \[out\]
</dt> <dd>

Type: **uint8**

A byte stream that contains the encryption key for a volume, secured by the specified key protector.

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following codes or another error code if it fails.



| Return code/value                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl>                                            | The method was successful.<br/>                                                                                                                                                                                                                                                                                                                                                                       |
| <dl> <dt>**FVE\_E\_LOCKED\_VOLUME**</dt> <dt>2150694912 (0x80310000)</dt> </dl>           | The volume is locked.<br/>                                                                                                                                                                                                                                                                                                                                                                            |
| <dl> <dt>**FVE\_E\_NOT\_ACTIVATED**</dt> <dt>2150694920 (0x80310008)</dt> </dl>           | BitLocker is not enabled on the volume. Add a key protector to enable BitLocker. <br/>                                                                                                                                                                                                                                                                                                                |
| <dl> <dt>**FVE\_E\_PROTECTOR\_NOT\_FOUND**</dt> <dt>2150694963 (0x80310033)</dt> </dl>    | The provided key protector does not exist on the volume.<br/>                                                                                                                                                                                                                                                                                                                                         |
| <dl> <dt>**FVE\_E\_INVALID\_PROTECTOR\_TYPE**</dt> <dt>2150694970 (0x8031003A)</dt> </dl> | The *VolumeKeyProtectorID* parameter does not refer to a key protector of the type "Numerical Password" or "External Key". Use either the [**ProtectKeyWithNumericalPassword**](protectkeywithnumericalpassword-win32-encryptablevolume.md) or [**ProtectKeyWithExternalKey**](protectkeywithexternalkey-win32-encryptablevolume.md) method to create a key protector of the appropriate type.<br/> |



 

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

 

 
