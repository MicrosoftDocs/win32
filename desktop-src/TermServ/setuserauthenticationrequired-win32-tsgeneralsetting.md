---
title: SetUserAuthenticationRequired method of the Win32_TSGeneralSetting class
description: Enables or disables the requirement that users must be authenticated at connection time by setting the value of the UserAuthenticationRequired property.
ms.assetid: a0581326-fecc-4d23-87bf-3696c93366e8
ms.tgt_platform: multiple
keywords:
- SetUserAuthenticationRequired method Remote Desktop Services
- SetUserAuthenticationRequired method Remote Desktop Services , Win32_TSGeneralSetting class
- Win32_TSGeneralSetting class Remote Desktop Services , SetUserAuthenticationRequired method
topic_type:
- apiref
api_name:
- Win32_TSGeneralSetting.SetUserAuthenticationRequired
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetUserAuthenticationRequired method of the Win32\_TSGeneralSetting class

Enables or disables the requirement that users must be authenticated at connection time by setting the value of the **UserAuthenticationRequired** property in the [**Win32\_TSGeneralSetting**](win32-tsgeneralsetting.md) class. If **True**, which means enabled, **UserAuthenticationRequired** requires user authentication at connection time to increase server protection against network attacks. Only Remote Desktop Protocol (RDP) clients that support RDP version 6.0 or higher are able to connect. To avoid disruptions for remote users, it is recommended that you deploy RDP clients supporting the appropriate protocol version before you enable the property.

## Syntax


```mof
uint32 SetUserAuthenticationRequired(
  [in] uint32 UserAuthenticationRequired
);
```



## Parameters

<dl> <dt>

*UserAuthenticationRequired* \[in\]
</dt> <dd>

Indicates whether user authentication is required.

<dt>

0 (0x0)
</dt> <dd>

Disable requirement that user must be authenticated

</dd> <dt>

1 (0x1)
</dt> <dd>

Enables requirement that user must be authenticated.

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

[**Win32\_TSGeneralSetting**](win32-tsgeneralsetting.md)
</dt> </dl>

 

