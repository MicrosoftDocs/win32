---
title: Export method of the Win32_TSVm class
description: Retrieves the virtual machine session monitoring information.
ms.assetid: 7996651c-aa7c-4fde-84a6-928b27c8c5b8
ms.tgt_platform: multiple
keywords:
- Export method Remote Desktop Services
- Export method Remote Desktop Services , Win32_TSVm class
- Win32_TSVm class Remote Desktop Services , Export method
topic_type:
- apiref
api_name:
- Win32_TSVm.Export
api_location:
- TSVmHostWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Export method of the Win32\_TSVm class

Retrieves the virtual machine session monitoring information.

## Syntax


```mof
uint32 Export(
  [in]  string ExportFolderPath,
  [out] string ExportJobObjectPath
);
```



## Parameters

<dl> <dt>

*ExportFolderPath* \[in\]
</dt> <dd>

Path to where the virtual machine will be exported.

</dd> <dt>

*ExportJobObjectPath* \[out\]
</dt> <dd>

On a success returns the HyperV ConcreteJob object path.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                             |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                   |
| MOF<br/>                      | <dl> <dt>TSVmHost.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>TSVmHostWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TSVm**](win32-tsvm.md)
</dt> </dl>

 

 





