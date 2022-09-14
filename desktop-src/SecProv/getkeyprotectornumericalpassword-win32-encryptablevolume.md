---
description: Retrieves the numerical password for a given key protector.
ms.assetid: 5c4663fb-285d-471c-b355-82d553a7e686
title: GetKeyProtectorNumericalPassword method of the Win32_EncryptableVolume class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_EncryptableVolume.GetKeyProtectorNumericalPassword
api_type: 
- COM
api_location: 
- Root\CIMV2\Security\MicrosoftVolumeEncryption
---

# GetKeyProtectorNumericalPassword method of the Win32\_EncryptableVolume class

The **GetKeyProtectorNumericalPassword** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class retrieves the numerical password for a given key protector of the appropriate type.

The key protector identifier must refer to a key protector of type "Numerical Password".

## Syntax


```mof
uint32 GetKeyProtectorNumericalPassword(
  [in]  string VolumeKeyProtectorID,
  [out] string NumericalPassword
);
```



## Parameters

<dl> <dt>

*VolumeKeyProtectorID* \[in\]
</dt> <dd>

Type: **string**

A unique string identifier used to manage an encrypted volume key protector.

</dd> <dt>

*NumericalPassword* \[out\]
</dt> <dd>

Type: **string**

A string that represents the password that can be used to unlock the corresponding volume.

The numerical password is 48 digits. These digits are divided into 8 groups of 6 digits, with the last digit in each group indicating a checksum value for the group. Assuming that a group of six digits is labeled as x1, x2, x3, x4, x5, and x6, the checksum x6 digit is calculated as –x1+x2–x3+x4–x5 mod 11.

The groups of digits are separated by a hyphen. Therefore, "xxxxxx-xxxxxx-xxxxxx-xxxxxx-xxxxxx-xxxxxx-xxxxxx-xxxxxx" is the format of the returned password.

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following codes or another error code if it fails.



| Return code/value                                                                                                                                                                  | Description                                                                                                         |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl>                                  | The method was successful.<br/>                                                                               |
| <dl> <dt>**FVE\_E\_LOCKED\_VOLUME**</dt> <dt>2150694912 (0x80310000)</dt> </dl> | The volume is locked.<br/>                                                                                    |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>2147942487 (0x80070057)</dt> </dl>          | The *VolumeKeyProtectorID* parameter does not refer to a key protector of the type "Numerical Password".<br/> |
| <dl> <dt>**FVE\_E\_NOT\_ACTIVATED**</dt> <dt>2150694920 (0x80310008)</dt> </dl> | BitLocker is not enabled on the volume. Add a key protector to enable BitLocker. <br/>                        |



 

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

 

 
