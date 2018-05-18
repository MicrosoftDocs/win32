---
Description: 'Indicates whether the TPM is ready for use.'
ms.assetid: '70E9EB90-DC13-4431-97E5-D77B4E345373'
title: 'Win32\_Tpm::IsReady method'
---

# Win32\_Tpm::IsReady method

Indicates whether the TPM is ready for use.

This method is only accessible by local administrators.

## Syntax


```C++
uint32 IsReady(
  [out] BOOL IsReady
);
```



## Parameters

<dl> <dt>

*IsReady* \[out\]
</dt> <dd>

Set to **TRUE** if the TPM and system are fully provisioned for TPM use.

</dd> </dl>

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

 

 




