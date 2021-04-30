---
description: Disables auto provisioning of the TPM if it is currently enabled.
ms.assetid: 30CC2581-9C16-4A11-92F1-625992F2AF20
title: Win32_Tpm::DisableAutoProvisioning method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Tpm.DisableAutoProvisioning
api_type: 
- COM
api_location: 
- Win32_tpm.dll
---

# Win32\_Tpm::DisableAutoProvisioning method

Disables auto provisioning of the TPM if it is currently enabled. The operation has no effect if auto provisioning is already disabled. By default, auto provisioning is enabled for Windows 8 and Windows Server 2012.

This method is only accessible by local administrators.

## Syntax


```C++
uint32 DisableAutoProvisioning(
  [in, optional] BOOL OnlyForNextBoot
);
```



## Parameters

<dl> <dt>

*OnlyForNextBoot* \[in, optional\]
</dt> <dd>

If set to **TRUE**, auto provisioning is disabled for only the next boot. If set to **FALSE** or not specified, auto provisioning is permanently disabled.

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

 

 
