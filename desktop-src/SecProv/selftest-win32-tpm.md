---
description: Performs a self-test of the TPM and returns the result.
ms.assetid: 0f8fdb68-80b1-4fc4-beb9-e87f51b85031
title: SelfTest method of the Win32_Tpm class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Tpm.SelfTest
api_type: 
- COM
api_location: 
- Win32_tpm.dll
---

# SelfTest method of the Win32\_Tpm class

The **SelfTest** method of the [**Win32\_Tpm**](win32-tpm.md) class performs a self-test of the TPM and returns the result.

A TPM self-test runs automatically when the computer starts.

## Syntax


```mof
uint32 SelfTest(
  [out] uint8 SelfTestResult[]
);
```



## Parameters

<dl> <dt>

*SelfTestResult* \[out\]
</dt> <dd>

Type: **uint8\[\]**

An array of bytes that contains the self-test result. The format of this parameter is manufacturer-specific.

</dd> </dl>

## Return value

Type: **uint32**

All TPM errors as well as errors specific to TPM Base Services can be returned.

The following table lists some of the common return codes.



| Return code/value                                                                                                                                 | Description                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl> | The method ran successfully.<br/> |



 

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

 

 
