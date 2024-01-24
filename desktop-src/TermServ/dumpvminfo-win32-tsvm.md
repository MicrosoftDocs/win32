---
title: DumpVmInfo method of the Win32_TSVm class
description: This member is for internal testing purposes, and should not be used in your code.
ms.assetid: 40cb4fdc-f657-47c6-8daa-684a12be30e4
ms.tgt_platform: multiple
keywords:
- DumpVmInfo method Remote Desktop Services
- DumpVmInfo method Remote Desktop Services , Win32_TSVm class
- Win32_TSVm class Remote Desktop Services , DumpVmInfo method
topic_type:
- apiref
api_name:
- Win32_TSVm.DumpVmInfo
api_location:
- TSVmHostWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# DumpVmInfo method of the Win32\_TSVm class

This member is for internal testing purposes, and should not be used in your code.

## Syntax


```mof
uint32 DumpVmInfo();
```



## Parameters

This method has no parameters.

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

 

 





