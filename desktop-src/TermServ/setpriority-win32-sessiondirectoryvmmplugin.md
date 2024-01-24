---
title: SetPriority method of the Win32_SessionDirectoryVMMPlugin class
description: Sets the priority of the plug-in.
ms.assetid: ddcf30cd-b87c-4869-80fc-ec92092e0df3
ms.tgt_platform: multiple
keywords:
- SetPriority method Remote Desktop Services
- SetPriority method Remote Desktop Services , Win32_SessionDirectoryVMMPlugin class
- Win32_SessionDirectoryVMMPlugin class Remote Desktop Services , SetPriority method
topic_type:
- apiref
api_name:
- Win32_SessionDirectoryVMMPlugin.SetPriority
api_location:
- TssdWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetPriority method of the Win32\_SessionDirectoryVMMPlugin class

Sets the priority of the plug-in.

## Syntax


```mof
uint32 SetPriority(
  [in] sint32 Priority
);
```



## Parameters

<dl> <dt>

*Priority* \[in\]
</dt> <dd>

The priority of the plug-in. The higher the value, the higher the priority of the plug-in. The priority is zero by default.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                      |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                               |
| MOF<br/>                      | <dl> <dt>TssdWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TssdWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_SessionDirectoryVMMPlugin**](win32-sessiondirectoryvmmplugin.md)
</dt> </dl>

 

 





