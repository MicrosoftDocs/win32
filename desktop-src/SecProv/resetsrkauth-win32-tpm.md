---
description: Resets the Storage Root Key (SRK) authorization value to be compatible with the operating system.
ms.assetid: af008733-b43c-4017-9e79-bdd98f2e20b6
title: ResetSrkAuth method of the Win32_Tpm class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Tpm.ResetSrkAuth
api_type: 
- COM
api_location: 
- Win32_tpm.dll
---

# ResetSrkAuth method of the Win32\_Tpm class

The **ResetSrkAuth** method of the [**Win32\_Tpm**](win32-tpm.md) class resets the Storage Root Key (SRK) authorization value to be compatible with the operating system.

## Syntax


```mof
uint32 ResetSrkAuth(
  [in, optional] string OwnerAuth
);
```



## Parameters

<dl> <dt>

*OwnerAuth* \[in, optional\]
</dt> <dd>

Type: **string**

A string that identifies the TPM owner. This string must be a base64-encoded null-terminated string that contains exactly 20 bytes of binary data. Use the [**ConvertToOwnerAuth**](converttoownerauth-win32-tpm.md) method to translate a passphrase to this expected format. The *OwnerAuth* parameter is read from the registry if none is provided.

</dd> </dl>

## Return value

Type: **uint32**

All TPM errors as well as errors specific to TPM Base Services can be returned.

The following table lists some of the common return codes.



| Return code/value                                                                                                                                                                         | Description                                                                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl>                                         | The method was successful.<br/>                                                                                                                                                |
| <dl> <dt>**TPM\_E\_AUTHFAIL** </dt> <dt>2150105089 (0x80280001)</dt> </dl>             | The provided owner authorization value cannot fulfill the request.<br/>                                                                                                        |
| <dl> <dt>**TPM\_E\_DEFEND\_LOCK\_RUNNING**</dt> <dt>2150107139 (0x80280803)</dt> </dl> | The TPM is defending against dictionary attacks and is in a time-out period. For more information, see the [**ResetAuthLockOut**](resetauthlockout-win32-tpm.md) method.<br/> |



 

## Remarks

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

 

 
