---
description: Gets the owner authorization information for a TPM if one is available in the registry.
ms.assetid: 3E2C28C8-4154-4B1B-9C47-AEDFD5622979
title: Win32_Tpm::GetOwnerAuth method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Tpm.GetOwnerAuth
api_type: 
- COM
api_location: 
- Win32_tpm.dll
---

# Win32\_Tpm::GetOwnerAuth method

Gets the owner authorization information for a TPM if one is available in the registry. If a TPM is owned or provisioned in Windows 8 with the default settings, the TPM owner authorization information is stored in the registry and is available for use by this method.

This method is only accessible by local administrators.

## Syntax


```C++
uint32 GetOwnerAuth(
  [out] STRING OwnerAuth
);
```



## Parameters

<dl> <dt>

*OwnerAuth* \[out\]
</dt> <dd>

The owner authorization information for a TPM, if one is available in the registry.

</dd> </dl>

## Return value

All TPM errors as well as errors specific to [TPM Base Services](../tbs/tbs-return-codes.md) can be returned.

Common return codes are listed below.



| Return code/value                                                                                                                                 | Description                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl> | The method was successful.<br/> |



 

## Remarks

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Windows SDK. They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](../wmisdk/managed-object-format--mof-.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | \\\\.\\root\\CIMV2\\Security\\MicrosoftTpm<br/>                                     |
| MOF<br/>                      | <dl> <dt>Win32\_tpm.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Win32\_tpm.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_Tpm**](win32-tpm.md)
</dt> </dl>

 

 
