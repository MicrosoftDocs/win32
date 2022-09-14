---
title: SetTimeZoneRedirection method of the Win32_TerminalServiceSetting class
description: The SetTimeZoneRedirection method sets the TimeZoneRedirection property, which allows the client computer to redirect its time zone settings to the Remote Desktop Services session.
ms.assetid: 4ae149b7-b7de-4530-a142-7253dd1e0d07
ms.tgt_platform: multiple
keywords:
- SetTimeZoneRedirection method Remote Desktop Services
- SetTimeZoneRedirection method Remote Desktop Services , Win32_TerminalServiceSetting class
- Win32_TerminalServiceSetting class Remote Desktop Services , SetTimeZoneRedirection method
topic_type:
- apiref
api_name:
- Win32_TerminalServiceSetting.SetTimeZoneRedirection
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetTimeZoneRedirection method of the Win32\_TerminalServiceSetting class

The **SetTimeZoneRedirection** method sets the **TimeZoneRedirection** property, which allows the client computer to redirect its time zone settings to the Remote Desktop Services session.

## Syntax


```mof
uint32 SetTimeZoneRedirection(
  [in] uint32 TimeZoneRedirection
);
```



## Parameters

<dl> <dt>

*TimeZoneRedirection* \[in\]
</dt> <dd>

The new value for the **TimeZoneRedirection** property.

<dt>

<span id="0"></span>

<span id="0"></span>**0**


</dt> <dd>

Disables the **TimeZoneRedirection** property. No time zone redirection occurs.

</dd> <dt>

<span id="1"></span>

<span id="1"></span>**1**


</dt> <dd>

Enables the **TimeZoneRedirection** property. The client's time zone is redirected to the session's time zone.

</dd> </dl> </dd> </dl>

## Return value

Returns 0 on success; otherwise returns a WMI error code. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values.

## Remarks

By default, the time zone for the Remote Desktop Services session is the same as the time zone for the Remote Desktop Session Host (RD Session Host) server. Client computers cannot redirect time zone information.

If time zone redirection is disabled, new sessions inherit the server time zone. When a session reconnects, the session retains the time zone it had prior to disconnecting.

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

 

