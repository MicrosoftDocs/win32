---
description: Gets the modulus of the public portion of the TPM Storage Root Key.
ms.assetid: 266AE378-8BF2-4F6E-A055-E15D95E218DC
title: Win32_Tpm::GetSrkPublicKeyModulus method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Tpm.GetSrkPublicKeyModulus
api_type: 
- COM
api_location: 
- Win32_tpm.dll
---

# Win32\_Tpm::GetSrkPublicKeyModulus method

Gets the modulus of the public portion of the TPM Storage Root Key.

This method is only accessible by local administrators.

## Syntax


```C++
uint32 GetSrkPublicKeyModulus(
  [out] uint8 SrkPublicKeyModulus
);
```



## Parameters

<dl> <dt>

*SrkPublicKeyModulus* \[out\]
</dt> <dd>

Returns a 256-byte array containing the modulus of the public portion of the TPM Storage Root Key

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

 

 
