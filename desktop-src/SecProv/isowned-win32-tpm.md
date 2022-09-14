---
description: The IsOwned method of the Win32\_Tpm class indicates whether the device has an owner. This value is changed by the TakeOwnership method.
ms.assetid: 04a9394f-98de-43e3-8a19-7a8f409823b8
title: IsOwned method of the Win32_Tpm class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Tpm.IsOwned
api_type: 
- COM
api_location: 
- Win32_tpm.dll
---

# IsOwned method of the Win32\_Tpm class

The **IsOwned** method of the [**Win32\_Tpm**](win32-tpm.md) class indicates whether the device has an owner. This value is changed by the [**TakeOwnership**](takeownership-win32-tpm.md) method.

## Syntax


```mof
uint32 IsOwned(
  [out] boolean IsOwned
);
```



## Parameters

<dl> <dt>

*IsOwned* \[out\]
</dt> <dd>

Type: **boolean**

If **true**, the device has an owner.

</dd> </dl>

## Return value

Type: **uint32**

All TPM errors as well as errors specific to TPM Base Services can be returned.

Common return codes are listed below.



| Return code/value                                                                                                                                 | Description                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl> | The method was successful.<br/> |



 

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

 

 
