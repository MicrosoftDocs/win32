---
title: PingLicenseServer method of the Win32_TerminalServiceSetting class
description: PingLicenseServer is no longer available.
ms.assetid: d2a9f273-1ff9-4391-889b-a3b9c9f95c3b
ms.tgt_platform: multiple
keywords:
- PingLicenseServer method Remote Desktop Services
- PingLicenseServer method Remote Desktop Services , Win32_TerminalServiceSetting class
- Win32_TerminalServiceSetting class Remote Desktop Services , PingLicenseServer method
topic_type:
- apiref
api_name:
- Win32_TerminalServiceSetting.PingLicenseServer
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# PingLicenseServer method of the Win32\_TerminalServiceSetting class

\[**PingLicenseServer** is no longer available for use as of Windows Server 2008 R2.\]

**Windows Server 2008:** Pings the license server to determine if it is a valid license server.

## Syntax


```mof
uint32 PingLicenseServer(
  [in] string ServerName
);
```



## Parameters

<dl> <dt>

*ServerName* \[in\]
</dt> <dd>

Name of the license server.

</dd> </dl>

## Return value

<dl> <dt>

**S\_OK**
</dt> <dd>

The server is a valid license server.

</dd> <dt>

**S\_FALSE**
</dt> <dd>

The license server is not valid.

</dd> </dl>

## Remarks

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| End of client support<br/>    | None supported<br/>                                                               |
| End of server support<br/>    | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TerminalServiceSetting**](win32-terminalservicesetting.md)
</dt> </dl>

 

