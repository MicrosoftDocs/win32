---
title: Create method of the Win32_Terminal class
description: Creates a terminal with default settings which can be customized by using the properties and methods of the Win32\_TerminalSetting classes.
ms.assetid: 64c90695-72d4-42be-a37a-89b54c04a78c
ms.tgt_platform: multiple
keywords:
- Create method Remote Desktop Services
- Create method Remote Desktop Services , Win32_Terminal class
- Win32_Terminal class Remote Desktop Services , Create method
topic_type:
- apiref
api_name:
- Win32_Terminal.Create
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Create method of the Win32\_Terminal class

The **Create** method creates a terminal with default settings which can be customized by using the properties and methods of the [**Win32\_TerminalSetting**](win32-terminalsetting.md) classes. The function returns zero on success and an error on failure.

## Syntax


```mof
uint32 Create(
  [in] string NewTerminalName,
  [in] string Transport,
  [in] string TerminalProtocol
);
```



## Parameters

<dl> <dt>

*NewTerminalName* \[in\]
</dt> <dd>

Name of the terminal.

</dd> <dt>

*Transport* \[in\]
</dt> <dd>

Transport for the terminal. This is a property of the [**Win32\_TSGeneralSetting**](win32-tsgeneralsetting.md) class.

</dd> <dt>

*TerminalProtocol* \[in\]
</dt> <dd>

Protocol for the terminal. This is a property of the [**Win32\_TSGeneralSetting**](win32-tsgeneralsetting.md) class.

</dd> </dl>

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

 

