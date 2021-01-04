---
title: RegisterVMMPlugin method of the Win32_SessionDirectoryVMMPlugin class
description: Registers a new VMM plug-in.
ms.assetid: 8fa6109e-6320-4ad1-b313-f100d8383f85
ms.tgt_platform: multiple
keywords:
- RegisterVMMPlugin method Remote Desktop Services
- RegisterVMMPlugin method Remote Desktop Services , Win32_SessionDirectoryVMMPlugin class
- Win32_SessionDirectoryVMMPlugin class Remote Desktop Services , RegisterVMMPlugin method
topic_type:
- apiref
api_name:
- Win32_SessionDirectoryVMMPlugin.RegisterVMMPlugin
api_location:
- TssdWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RegisterVMMPlugin method of the Win32\_SessionDirectoryVMMPlugin class

Registers a new VMM plug-in.

## Syntax


```mof
uint32 RegisterVMMPlugin(
  [in] string  sName,
  [in] string  sProvider,
  [in] string  sServiceLocation,
  [in] string  sClassID,
  [in] sint32  Priority = ,
  [in] boolean Enabled = 
);
```



## Parameters

<dl> <dt>

*sName* \[in\]
</dt> <dd>

The name of the plug-in.

</dd> <dt>

*sProvider* \[in\]
</dt> <dd>

The name of the plug-in provider.

</dd> <dt>

*sServiceLocation* \[in\]
</dt> <dd>

The service location that the plug-in should contact.

</dd> <dt>

*sClassID* \[in\]
</dt> <dd>

The class identifier of the plug-in.

</dd> <dt>

*Priority* \[in\]
</dt> <dd>

The priority of the plug-in. The higher the value, the higher the priority of the plug-in.

</dd> <dt>

*Enabled* \[in\]
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

 

 





