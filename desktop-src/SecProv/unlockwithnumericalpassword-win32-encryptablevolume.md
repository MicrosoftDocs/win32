---
description: Uses a provided numerical password to access the contents of a data volume.
ms.assetid: ee968372-18a4-4748-ab18-2f1b8d297f0e
title: UnlockWithNumericalPassword method of the Win32_EncryptableVolume class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_EncryptableVolume.UnlockWithNumericalPassword
api_type: 
- COM
api_location: 
- Root\CIMV2\Security\MicrosoftVolumeEncryption
---

# UnlockWithNumericalPassword method of the Win32\_EncryptableVolume class

The **UnlockWithNumericalPassword** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class uses a provided numerical password to access the contents of a data volume.

The volume's encryption key must have been secured with one or more key protectors of the type "Numerical Password" (by using the [**ProtectKeyWithNumericalPassword**](protectkeywithnumericalpassword-win32-encryptablevolume.md) method) to be able to unlock the volume with this method.

> [!Note]  
> If the disc supports hardware encryption this function sets the band status to "unlocked""

 

## Syntax


```mof
uint32 UnlockWithNumericalPassword(
  [in] string NumericalPassword
);
```



## Parameters

<dl> <dt>

*NumericalPassword* \[in\]
</dt> <dd>

Type: **string**

A string that specifies the numerical password.

The numerical password must contain 48 digits. These digits can be divided into 8 groups of 6 digits, with the last digit in each group indicating a checksum value for the group. Each group of 6 digits must be divisible by 11 and must be less than 65536. Assuming a group of six digits is labeled as x1, x2, x3, x4, x5, and x6, the checksum x6 digit is calculated as –x1+x2–x3+x4–x5 mod 11.

The groups of digits can optionally be separated by a space or hyphen. Therefore, "xxxxxx-xxxxxx-xxxxxx-xxxxxx-xxxxxx-xxxxxx-xxxxxx-xxxxxx" or "xxxxxx xxxxxx xxxxxx xxxxxx xxxxxx xxxxxx xxxxxx xxxxxx" may also contain valid numerical passwords.

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following codes or another error code if it fails.

If the volume is already unlocked and no other errors occur, this method returns 0.



| Return code/value                                                                                                                                                                             | Description                                                                                                                                                                                                                    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl>                                             | The method was successful.<br/>                                                                                                                                                                                          |
| <dl> <dt>**FVE\_E\_NOT\_ACTIVATED**</dt> <dt>2150694920 (0x80310008)</dt> </dl>            | BitLocker is not enabled on the volume. Add a key protector to enable BitLocker. <br/>                                                                                                                                   |
| <dl> <dt>**FVE\_E\_PROTECTOR\_NOT\_FOUND**</dt> <dt>2150694963 (0x80310033)</dt> </dl>     | The volume does not have a key protector of the type "Numerical Password".<br/> The *NumericalPassword* parameter has a valid format, but you cannot use a numerical password to unlock the volume.<br/>           |
| <dl> <dt>**FVE\_E\_FAILED\_AUTHENTICATION**</dt> <dt>2150694951 (0x80310027)</dt> </dl>    | The *NumericalPassword* parameter cannot unlock the volume.<br/> One or more key protectors of the type "Numerical Password" exist, but the specified *NumericalPassword* parameter cannot unlock the volume.<br/> |
| <dl> <dt>**FVE\_E\_INVALID\_PASSWORD\_FORMAT**</dt> <dt>2150694965 (0x80310035)</dt> </dl> | The *NumericalPassword* parameter does not have a valid format.<br/>                                                                                                                                                     |



 

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

 

 
