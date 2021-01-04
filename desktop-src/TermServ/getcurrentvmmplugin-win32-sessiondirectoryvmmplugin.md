---
title: GetCurrentVMMPlugin method of the Win32_SessionDirectoryVMMPlugin class
description: Gets the highest priority plug-in that is enabled.
ms.assetid: 7712573f-2252-4a3c-820c-b679be5dfd46
ms.tgt_platform: multiple
keywords:
- GetCurrentVMMPlugin method Remote Desktop Services
- GetCurrentVMMPlugin method Remote Desktop Services , Win32_SessionDirectoryVMMPlugin class
- Win32_SessionDirectoryVMMPlugin class Remote Desktop Services , GetCurrentVMMPlugin method
topic_type:
- apiref
api_name:
- Win32_SessionDirectoryVMMPlugin.GetCurrentVMMPlugin
api_location:
- TssdWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# GetCurrentVMMPlugin method of the Win32\_SessionDirectoryVMMPlugin class

Gets the highest priority plug-in that is enabled.

## Syntax


```mof
uint32 GetCurrentVMMPlugin(
  [out] string  sName,
  [out] string  sProvider,
  [out] string  sServiceLocation,
  [out] string  sClassID,
  [out] sint32  Priority,
  [out] boolean Enabled
);
```



## Parameters

<dl> <dt>

*sName* \[out\]
</dt> <dd>

The name of the plug-in.

</dd> <dt>

*sProvider* \[out\]
</dt> <dd>

The name of the plug-in provider.

</dd> <dt>

*sServiceLocation* \[out\]
</dt> <dd>

The service location that the plug-in should contact.

</dd> <dt>

*sClassID* \[out\]
</dt> <dd>

The class identifier of the plug-in.

</dd> <dt>

*Priority* \[out\]
</dt> <dd>

The priority of the plug-in. The higher the value, the higher the priority of the plug-in.

</dd> <dt>

*Enabled* \[out\]
</dt> <dd>

Indicates whether the plug-in is enabled or disabled. **True** if the plug-in is enabled or **false** otherwise.

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

 

 





