---
description: Resets the time-out period or other mechanism that TPM manufacturers implement to protect against dictionary attacks on TPM authorization values.
ms.assetid: c2fba6a2-2d03-4ffd-9841-4a9eac0a20ac
title: ResetAuthLockOut method of the Win32_Tpm class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Tpm.ResetAuthLockOut
api_type: 
- COM
api_location: 
- Win32_tpm.dll
---

# ResetAuthLockOut method of the Win32\_Tpm class

The **ResetAuthLockOut** method of the [**Win32\_Tpm**](win32-tpm.md) class resets the time-out period or other mechanism that TPM manufacturers implement to protect against dictionary attacks on TPM authorization values. In a dictionary attack, an attacker tries to guess a correct TPM authorization value by exhaustively attempting all possible values.

Use this method if the TPM is locked out due to too many incorrect attempts at entering the owner authorization or other authorization values. When the TPM is locked out, some or all commands issued to the TPM will return an error, TPM\_E\_DEFEND\_LOCK\_RUNNING (0x80280803).

> [!Note]  
> This method can only be used exactly once when the TPM is locked out. If the owner authorization provided to this method is incorrect, the TPM will lock out for the entire time-out period and additional attempts at resetting the lock will fail.

 

## Syntax


```mof
uint32 ResetAuthLockOut(
  [in, optional] string OwnerAuth
);
```



## Parameters

<dl> <dt>

*OwnerAuth* \[in, optional\]
</dt> <dd>

Type: **string**

A string that identifies the TPM owner.

This string must be a base64-encoded null-terminated string that contains exactly 20 bytes of binary data. Use the [**ConvertToOwnerAuth**](converttoownerauth-win32-tpm.md) method to translate a passphrase to this expected format. The *OwnerAuth* parameter is read from the registry if none is provided.

</dd> </dl>

## Return value

Type: **uint32**

All TPM errors as well as errors specific to TPM Base Services can be returned. The following table lists some of the common return values.



| Return code/value                                                                                                                                                            | Description                                                                                                                                                                                                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl>                            | The method was successful.<br/>                                                                                                                                                                                                                                     |
| <dl> <dt>**TPM\_E\_AUTHFAIL**</dt> <dt>2150105089 (0x80280001)</dt> </dl> | The provided owner authorization value is incorrect. Additional attempts at resetting the lock will fail with this same error. Please wait until the time-out period or other manufacturer-specific mechanism has expired before retrying locked TPM commands.<br/> |



 

## Remarks

This method calls the TPM\_ResetLockValue command on the TPM. The exact behavior of this method varies among TPM manufacturers. Documentation from the computer or TPM manufacturer may provide additional information on the implementation of the anti-dictionary attack mechanism.

In general, manufacturers can detect dictionary attacks by keeping track of failed authentications. If the number or frequency of failures become high enough, the TPM will lock out further commands for a certain time. Generally, the initial time-out period will be short, to allow a legitimate user a chance to correct the situation. If failures continue, the duration of each subsequent time-out period may increase rapidly.

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Windows SDK. They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](../wmisdk/managed-object-format--mof-.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\CIMV2\\Security\\MicrosoftTpm<br/>                                            |
| MOF<br/>                      | <dl> <dt>Win32\_tpm.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Win32\_tpm.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_Tpm**](win32-tpm.md)
</dt> </dl>

 

 
