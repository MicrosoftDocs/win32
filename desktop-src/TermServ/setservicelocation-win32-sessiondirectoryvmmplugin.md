---
title: SetServiceLocation method of the Win32_SessionDirectoryVMMPlugin class
description: Sets the service location for the plug-in.
ms.assetid: e886a40b-9ea9-4159-a2ea-776160559410
ms.tgt_platform: multiple
keywords:
- SetServiceLocation method Remote Desktop Services
- SetServiceLocation method Remote Desktop Services , Win32_SessionDirectoryVMMPlugin class
- Win32_SessionDirectoryVMMPlugin class Remote Desktop Services , SetServiceLocation method
topic_type:
- apiref
api_name:
- Win32_SessionDirectoryVMMPlugin.SetServiceLocation
api_location:
- TssdWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetServiceLocation method of the Win32\_SessionDirectoryVMMPlugin class

Sets the service location for the plug-in.

## Syntax


```mof
uint32 SetServiceLocation(
  [in] string sServiceLocation
);
```



## Parameters

<dl> <dt>

*sServiceLocation* \[in\]
</dt> <dd>

The service location that the plug-in should contact.

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

 

 





