---
Description: Gets the owner authorization information for a TPM if one is available in the registry.
ms.assetid: 3E2C28C8-4154-4B1B-9C47-AEDFD5622979
title: Win32\_Tpm::GetOwnerAuth method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

All TPM errors as well as errors specific to [TPM Base Services](https://msdn.microsoft.com/windows/desktop/a3888263-aa00-4b31-b51d-c6d448c1edb7) can be returned.

Common return codes are listed below.



| Return code/value                                                                                                                                 | Description                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl> | The method was successful.<br/> |



 

## Remarks

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Windows SDK. They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](https://msdn.microsoft.com/windows/desktop/26494142-2078-4d46-a794-e43973255c2d).

## Requirements



|                                     |                                                                                           |
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

 

 




