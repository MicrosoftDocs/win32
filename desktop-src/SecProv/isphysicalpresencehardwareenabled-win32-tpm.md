---
description: The IsPhysicalPresenceHardwareEnabled method of the Win32\_Tpm class indicates whether physical presence on the platform can be set with a hardware signal.
ms.assetid: 65dabfa9-bfbe-4b9b-8e80-02269895c7ad
title: IsPhysicalPresenceHardwareEnabled method of the Win32_Tpm class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Tpm.IsPhysicalPresenceHardwareEnabled
api_type: 
- COM
api_location: 
- Win32_tpm.dll
---

# IsPhysicalPresenceHardwareEnabled method of the Win32\_Tpm class

The **IsPhysicalPresenceHardwareEnabled** method of the [**Win32\_Tpm**](win32-tpm.md) class indicates whether physical presence on the platform can be set with a hardware signal. This value is configured by the platform manufacturer based on the design of the platform. Documentation from the platform manufacturer may provide additional information.

## Syntax


```mof
uint32 IsPhysicalPresenceHardwareEnabled(
  [out] boolean IsPhysicalPresenceHardwareEnabled
);
```



## Parameters

<dl> <dt>

*IsPhysicalPresenceHardwareEnabled* \[out\]
</dt> <dd>

Type: **boolean**

If **true**, physical presence on the platform can be set with a hardware signal.

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

 

 
