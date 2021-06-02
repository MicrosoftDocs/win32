---
title: ChangeMode method of the Win32_TerminalServiceSetting class
description: The ChangeMode method sets the licensing type of the current Remote Desktop Session Host (RD Session Host) server.
ms.assetid: 293483ee-51ce-4cd4-ba13-6c7c02bbdbbf
ms.tgt_platform: multiple
keywords:
- ChangeMode method Remote Desktop Services
- ChangeMode method Remote Desktop Services , Win32_TerminalServiceSetting class
- Win32_TerminalServiceSetting class Remote Desktop Services , ChangeMode method
topic_type:
- apiref
api_name:
- Win32_TerminalServiceSetting.ChangeMode
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ChangeMode method of the Win32\_TerminalServiceSetting class

The **ChangeMode** method sets the licensing type of the current Remote Desktop Session Host (RD Session Host) server.

## Syntax


```mof
uint32 ChangeMode(
  [in] uint32 LicensingType
);
```



## Parameters

<dl> <dt>

*LicensingType* \[in\]
</dt> <dd>

The licensing type to set based on the RD Session Host server mode.

<dt>

<span id="0"></span>

<span id="0"></span>**0**


</dt> <dd>

Personal RD Session Host server.

</dd> <dt>

<span id="1"></span>

<span id="1"></span>**1**


</dt> <dd>

Remote desktop for administration.

</dd> <dt>

<span id="2"></span>

<span id="2"></span>**2**


</dt> <dd>

Per device/per seat. Valid for application servers.

</dd> <dt>

<span id="4"></span>

<span id="4"></span>**4**


</dt> <dd>

Per User. Valid for application servers.

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

[**Win32\_TerminalServiceSetting**](win32-terminalservicesetting.md)
</dt> </dl>

 

