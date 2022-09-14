---
title: SetAllowTSConnections method of the Win32_TerminalServiceSetting class
description: The SetAllowTSConnections method allows or denies new remote desktop connections. This method will modify the AllowTSConnections property for the class accordingly.
ms.assetid: 6cbaea62-ced0-4788-99fb-5b36816b80a1
ms.tgt_platform: multiple
keywords:
- SetAllowTSConnections method Remote Desktop Services
- SetAllowTSConnections method Remote Desktop Services , Win32_TerminalServiceSetting class
- Win32_TerminalServiceSetting class Remote Desktop Services , SetAllowTSConnections method
topic_type:
- apiref
api_name:
- Win32_TerminalServiceSetting.SetAllowTSConnections
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetAllowTSConnections method of the Win32\_TerminalServiceSetting class

The **SetAllowTSConnections** method allows or denies new remote desktop connections. This method will modify the **AllowTSConnections** property for the class accordingly.

## Syntax


```mof
uint32 SetAllowTSConnections(
  [in] uint32 AllowTSConnections,
  [in] uint32 ModifyFirewallException
);
```



## Parameters

<dl> <dt>

*AllowTSConnections* \[in\]
</dt> <dd>

Specifies whether new remote desktop connections are allowed. This must be one of the following values.

<dt>

<span id="0"></span>

<span id="0"></span>**0**


</dt> <dd>

New connections are not allowed. If the *ModifyFirewallException* parameter is 1, then the Remote Desktop firewall exception is disabled.

</dd> <dt>

<span id="1"></span>

<span id="1"></span>**1**


</dt> <dd>

New connections are allowed. If the *ModifyFirewallException* parameter is 1, then the Remote Desktop firewall exception is enabled.

</dd> </dl> </dd> <dt>

*ModifyFirewallException* \[in\]
</dt> <dd>

Specifies if the firewall exception setting for Remote Desktop will be modified to the state specified by the *AllowTSConnections* parameter. This must be one of the following values.

<dt>

<span id="0"></span>

<span id="0"></span>**0**


</dt> <dd>

Do not modify the firewall exception setting.

</dd> <dt>

<span id="1"></span>

<span id="1"></span>**1**


</dt> <dd>

Modify the firewall exception setting.

</dd> </dl> </dd> </dl>

## Return value

Returns Success on success; otherwise, returns a WMI error code. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values. The method returns an error if the setting is under group policy control.

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

 

