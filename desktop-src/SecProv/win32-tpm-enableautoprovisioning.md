---
Description: Enables auto provisioning of the TPM if it is currently disabled.
ms.assetid: 70F56A4C-F936-4CB6-83F6-F3B691F43B98
title: Win32\_TpmEnableAutoProvisioning method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Win32\_Tpm::EnableAutoProvisioning method

Enables auto provisioning of the TPM if it is currently disabled. The operation has no effect if auto provisioning is already enabled. By default, auto provisioning is enabled for Windows 8 and Windows Server 2012.

This method is only accessible by local administrators.

## Syntax


```C++
uint32 EnableAutoProvisioning();
```



## Parameters

This method has no parameters.

## Return value

All TPM errors as well as errors specific to [TPM Base Services](tbs.tbs_return_codes) can be returned.

Common return codes are listed below.



| Return code/value                                                                                                                                 | Description                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl> | The method was successful.<br/> |



 

## Remarks

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Windows SDK. They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](wmi.managed_object_format__mof_).

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

 

 




