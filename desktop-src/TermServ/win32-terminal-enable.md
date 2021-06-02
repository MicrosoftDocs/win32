---
title: Enable method of the Win32_Terminal class
description: The Enable method disables or enables the terminal.
ms.assetid: f249563b-6fa0-413c-9fc7-01dd16d5c561
ms.tgt_platform: multiple
keywords:
- Enable method Remote Desktop Services
- Enable method Remote Desktop Services , Win32_Terminal class
- Win32_Terminal class Remote Desktop Services , Enable method
topic_type:
- apiref
api_name:
- Win32_Terminal.Enable
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Enable method of the Win32\_Terminal class

The **Enable** method disables or enables the terminal.

## Syntax


```mof
uint32 Enable(
  [in] uint32 fEnableTerminal
);
```



## Parameters

<dl> <dt>

*fEnableTerminal* \[in\]
</dt> <dd>

Flag that disables or enables the terminal.

<dt>

<span id="0"></span>

<span id="0"></span>**0**


</dt> <dd>

The terminal is disabled.

</dd> <dt>

<span id="1"></span>

<span id="1"></span>**1**


</dt> <dd>

The terminal is enabled.

</dd> </dl> </dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values.

## Remarks

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_Terminal**](win32-terminal.md)
</dt> </dl>

 

