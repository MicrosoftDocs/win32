---
description: The IsPhysicalClearDisabled method of the Win32\_Tpm class indicates whether only the device owner may be able to clear the device.
ms.assetid: b87f1c4f-8735-45c5-9256-53dbb9579f95
title: IsPhysicalClearDisabled method of the Win32_Tpm class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Tpm.IsPhysicalClearDisabled
api_type: 
- COM
api_location: 
- Win32_tpm.dll
---

# IsPhysicalClearDisabled method of the Win32\_Tpm class

The **IsPhysicalClearDisabled** method of the [**Win32\_Tpm**](win32-tpm.md) class indicates whether only the device owner may be able to clear the device.

## Syntax


```mof
uint32 IsPhysicalClearDisabled(
  [out] boolean IsPhysicalClearDisabled
);
```



## Parameters

<dl> <dt>

*IsPhysicalClearDisabled* \[out\]
</dt> <dd>

Type: **boolean**

If **true**, only the device owner is able to clear the device.

</dd> </dl>

## Return value

Type: **uint32**

All TPM errors as well as errors specific to TPM Base Services can be returned.

Common return codes are listed below.



| Return code/value                                                                                                                                 | Description                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl> | The method was successful.<br/> |



 

## Remarks

This value is reset to **false** at the beginning of each startup cycle.

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

 

 
