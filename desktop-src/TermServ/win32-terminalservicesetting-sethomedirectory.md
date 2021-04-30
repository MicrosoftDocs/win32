---
title: SetHomeDirectory method of the Win32_TerminalServiceSetting class
description: Sets the TerminalServicesHomeDirectory property for the class.
ms.assetid: 8173cd5b-965e-41bc-97cf-70d8729b8cea
ms.tgt_platform: multiple
keywords:
- SetHomeDirectory method Remote Desktop Services
- SetHomeDirectory method Remote Desktop Services , Win32_TerminalServiceSetting class
- Win32_TerminalServiceSetting class Remote Desktop Services , SetHomeDirectory method
topic_type:
- apiref
api_name:
- Win32_TerminalServiceSetting.SetHomeDirectory
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetHomeDirectory method of the Win32\_TerminalServiceSetting class

The **SetHomeDirectory** method sets the **TerminalServicesHomeDirectory** property for the class.

## Syntax


```mof
uint32 SetHomeDirectory(
  [in] string HomeDirectory
);
```



## Parameters

<dl> <dt>

*HomeDirectory* \[in\]
</dt> <dd>

The new value for the **TerminalServicesHomeDirectory** property, which specifies the computer's root directory.

</dd> </dl>

## Return value

Returns Success on success; otherwise, returns a WMI error code. For a list of WMI error codes, see [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md).

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

[**Win32\_TerminalServiceSetting**](win32-terminalservicesetting.md)
</dt> </dl>

 

