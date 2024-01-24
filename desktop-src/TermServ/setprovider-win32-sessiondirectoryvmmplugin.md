---
title: SetProvider method of the Win32_SessionDirectoryVMMPlugin class
description: Sets the name of the plug-in provider.
ms.assetid: fefb7c19-2bab-4ae3-b88b-20da5fd19ff3
ms.tgt_platform: multiple
keywords:
- SetProvider method Remote Desktop Services
- SetProvider method Remote Desktop Services , Win32_SessionDirectoryVMMPlugin class
- Win32_SessionDirectoryVMMPlugin class Remote Desktop Services , SetProvider method
topic_type:
- apiref
api_name:
- Win32_SessionDirectoryVMMPlugin.SetProvider
api_location:
- TssdWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetProvider method of the Win32\_SessionDirectoryVMMPlugin class

Sets the name of the plug-in provider.

## Syntax


```mof
uint32 SetProvider(
  [in] string sProvider
);
```



## Parameters

<dl> <dt>

*sProvider* \[in\]
</dt> <dd>

The name of the plug-in provider.

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

 

 





