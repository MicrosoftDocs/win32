---
title: SetPrimaryLicenseServer method of the Win32_TerminalServiceSetting class
description: Sets the given license server as the first entry in the list of specified license servers.
ms.assetid: 8921e861-3b9a-49c5-a691-ded7be18ca0a
ms.tgt_platform: multiple
keywords:
- SetPrimaryLicenseServer method Remote Desktop Services
- SetPrimaryLicenseServer method Remote Desktop Services , Win32_TerminalServiceSetting class
- Win32_TerminalServiceSetting class Remote Desktop Services , SetPrimaryLicenseServer method
topic_type:
- apiref
api_name:
- Win32_TerminalServiceSetting.SetPrimaryLicenseServer
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetPrimaryLicenseServer method of the Win32\_TerminalServiceSetting class

Sets the given license server as the first entry in the list of specified license servers.

## Syntax


```mof
uint32 SetPrimaryLicenseServer(
  [in] string LicenseServerName
);
```



## Parameters

<dl> <dt>

*LicenseServerName* \[in\]
</dt> <dd>

The name of the license server.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                       |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TerminalServiceSetting**](win32-terminalservicesetting.md)
</dt> </dl>

 

 





