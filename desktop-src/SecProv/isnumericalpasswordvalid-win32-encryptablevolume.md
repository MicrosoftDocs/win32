---
description: Indicates whether the numerical password meets the special format requirements for this authentication value.
ms.assetid: 3995405f-db4d-4f72-98dc-133a09f9cf65
title: IsNumericalPasswordValid method of the Win32_EncryptableVolume class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_EncryptableVolume.IsNumericalPasswordValid
api_type: 
- COM
api_location: 
- Root\CIMV2\Security\MicrosoftVolumeEncryption
---

# IsNumericalPasswordValid method of the Win32\_EncryptableVolume class

The **IsNumericalPasswordValid** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class indicates whether the numerical password meets the special format requirements for this authentication value.

## Syntax


```mof
uint32 IsNumericalPasswordValid(
  [in]  string  NumericalPassword,
  [out] boolean IsNumericalPasswordValid
);
```



## Parameters

<dl> <dt>

*NumericalPassword* \[in\]
</dt> <dd>

Type: **string**

A string that specifies the numerical password.

The numerical password must contain 48 digits. These digits can be divided into 8 groups of 6 digits, with the last digit in each group indicating a checksum value for the group. Each group of 6 digits must be divisible by 11 and must be less than 720896. Assuming a group of six digits is labeled as x1, x2, x3, x4, x5, and x6, the checksum x6 digit is calculated as –x1+x2–x3+x4–x5 mod 11.

The groups of digits can optionally be separated by a space or hyphen. Therefore, "xxxxxx-xxxxxx-xxxxxx-xxxxxx-xxxxxx-xxxxxx-xxxxxx-xxxxxx" or "xxxxxx xxxxxx xxxxxx xxxxxx xxxxxx xxxxxx xxxxxx xxxxxx" may also contain valid numerical passwords.

</dd> <dt>

*IsNumericalPasswordValid* \[out\]
</dt> <dd>

Type: **boolean**

A Boolean value that is true if the numerical password meets the special format requirements for this authentication value, otherwise the value is false.

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following codes or another error code if it fails.



| Return code/value                                                                                                                                 | Description                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl> | The method was successful.<br/> |



 

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

 

 
