---
title: ExplicitLogon method of the Win32_TSLogonSetting class
description: The ExplicitLogon method sets the credentials to use for authentication.
ms.assetid: cfd43396-0d66-4d5e-81c8-5c0e66422dc5
ms.tgt_platform: multiple
keywords:
- ExplicitLogon method Remote Desktop Services
- ExplicitLogon method Remote Desktop Services , Win32_TSLogonSetting class
- Win32_TSLogonSetting class Remote Desktop Services , ExplicitLogon method
topic_type:
- apiref
api_name:
- Win32_TSLogonSetting.ExplicitLogon
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ExplicitLogon method of the Win32\_TSLogonSetting class

The **ExplicitLogon** method sets the credentials to use for authentication.

## Syntax


```mof
uint32 ExplicitLogon(
  [in] string UserName,
  [in] string Domain,
  [in] string Password
);
```



## Parameters

<dl> <dt>

*UserName* \[in\]
</dt> <dd>

The user name logon credential.

</dd> <dt>

*Domain* \[in\]
</dt> <dd>

The domain logon credential.

</dd> <dt>

*Password* \[in\]
</dt> <dd>

The password logon credential.

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

[**Win32\_TSLogonSetting**](win32-tslogonsetting.md)
</dt> </dl>

 

