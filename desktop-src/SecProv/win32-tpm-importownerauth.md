---
description: Imports the owner authorization information for a TPM that is already owned into the operating system registry.
ms.assetid: 9611D363-6F10-48B9-B417-97133E975257
title: Win32_Tpm::ImportOwnerAuth method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Tpm.ImportOwnerAuth
api_type: 
- COM
api_location: 
- Win32_tpm.dll
---

# Win32\_Tpm::ImportOwnerAuth method

Imports the owner authorization information for a TPM that is already owned into the operating system registry. This operation will first validate if the supplied owner authorization information is correct. If correct, the method imports this information to the registry.

This method is only accessible by local administrators.

## Syntax


```C++
uint32 ImportOwnerAuth(
  [in] STRING OwnerAuth
);
```



## Parameters

<dl> <dt>

*OwnerAuth* \[in\]
</dt> <dd>

The valid owner authorization information for the TPM.

</dd> </dl>

## Return value

All TPM errors as well as errors specific to [TPM Base Services](../tbs/tbs-return-codes.md) can be returned.

Common return codes are listed below.



| Return code/value                                                                                                                                 | Description                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl> | The method was successful.<br/> |



 

## Remarks

This method is particularly useful in the scenarios where the TPM is in a "ready with reduced functionality state " and requires the importing of the owner authorization to be fully ready or in a dual-boot scenarios where one of the operating systems has owned the TPM and the owner authorization information for TPM is not available in the other operating system.

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

 

 
