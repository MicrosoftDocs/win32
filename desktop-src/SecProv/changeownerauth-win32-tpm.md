---
description: Changes the TPM owner authorization value.
ms.assetid: ed280037-2360-4889-baba-cfa9e4fd473e
title: ChangeOwnerAuth method of the Win32_Tpm class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Tpm.ChangeOwnerAuth
api_type: 
- COM
api_location: 
- Win32_tpm.dll
---

# ChangeOwnerAuth method of the Win32\_Tpm class

The **ChangeOwnerAuth** method of the [**Win32\_Tpm**](win32-tpm.md) class changes the TPM owner authorization value.

## Syntax


```mof
uint32 ChangeOwnerAuth(
  [in, optional] string OldOwnerAuth,
  [in, optional] string NewOwnerAuth
);
```



## Parameters

<dl> <dt>

*OldOwnerAuth* \[in, optional\]
</dt> <dd>

Type: **string**

A string that names the current TPM owner authorization value of the device. Use the [**ConvertToOwnerAuth**](converttoownerauth-win32-tpm.md) method to translate a password to this authorization value. The *OldOwnerAuth* parameter is not supplied or an empty string is provided, this method gets the value from the registry if present.

</dd> <dt>

*NewOwnerAuth* \[in, optional\]
</dt> <dd>

Type: **string**

A string that names the new TPM owner authorization value. Use the [**ConvertToOwnerAuth**](converttoownerauth-win32-tpm.md) method to translate a password to this authorization value. The *NewOwnerAuth* parameter cannot be empty or **NULL.**

</dd> </dl>

## Return value

Type: **uint32**

All TPM errors as well as errors specific to TPM Base Services can be returned.

The following table lists some of the common return codes.



| Return code/value                                                                                                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl>                                              | The method was successful.<br/>                                                                                                                                                                                                                                                                                                                                                            |
| <dl> <dt>**TPM\_E\_AUTHFAIL**</dt> <dt>2150105089 (0x80280001)</dt> </dl>                   | The current TPM owner authorization value is incorrect.<br/>                                                                                                                                                                                                                                                                                                                               |
| <dl> <dt>**TPM\_E\_DEFEND\_LOCK\_RUNNING**</dt> <dt>2150107139 (0x80280803)</dt> </dl>      | The TPM is defending against dictionary attacks and is in a time-out period. For more information, see the [**ResetAuthLockOut**](resetauthlockout-win32-tpm.md) method.<br/>                                                                                                                                                                                                             |
| <dl> <dt>**FVE\_E\_AD\_SCHEMA\_NOT\_INSTALLED**</dt> <dt>2150694922 (0x8031000A)</dt> </dl> | Cannot save recovery information to the network. The computer has been configured to store recovery information to Active Directory Domain Services. For instructions on how to set up Active Directory, see [BitLocker Drive Encryption Configuration Guide: Backing Up BitLocker and TPM Recovery Information to Active Directory](/previous-versions/windows/it-pro/windows-vista/cc766015(v=ws.10)).<br/> |
| <dl> <dt>**Connection Failed**</dt> <dt>2147943755 (0x8007054B)</dt> </dl>                  | Cannot save recovery information to the network. The computer has been configured to store recovery information to Active Directory Domain Services. A network connection is required to continue.<br/>                                                                                                                                                                                    |



 

## Remarks

The **ChangeOwnerAuth** method backs up the new TPM owner authorization to Active Directory Domain Services if the appropriate Group Policy settings have been configured.

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

 

 
