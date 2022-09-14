---
title: TimeLimit method of the Win32_TSSessionSetting class
description: Sets the maximum time allocated to the specified session-limit type.
ms.assetid: 55194197-ffb6-49ae-827a-478ced867ab0
ms.tgt_platform: multiple
keywords:
- TimeLimit method Remote Desktop Services
- TimeLimit method Remote Desktop Services , Win32_TSSessionSetting class
- Win32_TSSessionSetting class Remote Desktop Services , TimeLimit method
topic_type:
- apiref
api_name:
- Win32_TSSessionSetting.TimeLimit
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TimeLimit method of the Win32\_TSSessionSetting class

Sets the maximum time allocated to the specified session-limit type.

## Syntax


```mof
uint32 TimeLimit(
  [in] string SessionLimitType,
  [in] uint32 ValueLimit
);
```



## Parameters

<dl> <dt>

*SessionLimitType* \[in\]
</dt> <dd>

Specifies the type of session-limit property that the method is setting.

<dt>

<span id="ActiveSessionLimit"></span><span id="activesessionlimit"></span><span id="ACTIVESESSIONLIMIT"></span>

<span id="ActiveSessionLimit"></span><span id="activesessionlimit"></span><span id="ACTIVESESSIONLIMIT"></span>**ActiveSessionLimit**


</dt> <dd>

The method is setting the **ActiveSessionLimit** property.

</dd> <dt>

<span id="DisconnectedSessionLimit"></span><span id="disconnectedsessionlimit"></span><span id="DISCONNECTEDSESSIONLIMIT"></span>

<span id="DisconnectedSessionLimit"></span><span id="disconnectedsessionlimit"></span><span id="DISCONNECTEDSESSIONLIMIT"></span>**DisconnectedSessionLimit**


</dt> <dd>

The method is setting the **DisconnectedSessionLimit** property.

</dd> <dt>

<span id="IdleSessionLimit"></span><span id="idlesessionlimit"></span><span id="IDLESESSIONLIMIT"></span>

<span id="IdleSessionLimit"></span><span id="idlesessionlimit"></span><span id="IDLESESSIONLIMIT"></span>**IdleSessionLimit**


</dt> <dd>

The method is setting the **IdleSessionLimit** property.

</dd> </dl> </dd> <dt>

*ValueLimit* \[in\]
</dt> <dd>

The new maximum time, in milliseconds, for the property specified by the *SessionLimitType* parameter. The value zero indicates that there is no session limit.

</dd> </dl>

## Return value

Returns Success on success, otherwise returns a WMI error code. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values. The method returns an error if the setting is under group policy control.

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

[**Win32\_TSSessionSetting**](win32-tssessionsetting.md)
</dt> </dl>

 

