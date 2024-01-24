---
description: The IsOwnershipAllowed method of the Win32\_Tpm class indicates whether the ability to install an owner for the device is permitted.
ms.assetid: dfeb5afe-4169-470b-b5e4-cf1e5781271e
title: IsOwnershipAllowed method of the Win32_Tpm class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Tpm.IsOwnershipAllowed
api_type: 
- COM
api_location: 
- Win32_tpm.dll
---

# IsOwnershipAllowed method of the Win32\_Tpm class

The **IsOwnershipAllowed** method of the [**Win32\_Tpm**](win32-tpm.md) class indicates whether the ability to install an owner for the device is permitted.

## Syntax


```mof
uint32 IsOwnershipAllowed(
  [out] boolean IsOwnershipAllowed
);
```



## Parameters

<dl> <dt>

*IsOwnershipAllowed* \[out\]
</dt> <dd>

Type: **boolean**

If **true**, the ability to install an owner for the device is permitted. If **false**, the method [**TakeOwnership**](takeownership-win32-tpm.md) will fail to install an owner for the device.

This value can be changed with the [**SetPhysicalPresenceRequest**](setphysicalpresencerequest-win32-tpm.md) method. The value is reset to **true** after the [**Clear**](clear-win32-tpm.md) method is run.

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

 

 
