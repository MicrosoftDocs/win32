---
title: EmptySpecifiedLicenseServerList method of the Win32_TerminalServiceSetting class
description: Removes all license servers from the list of specified license servers.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: de1633ca-3f0b-4540-8b45-44303a4e72fe
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- EmptySpecifiedLicenseServerList method Remote Desktop Services
- EmptySpecifiedLicenseServerList method Remote Desktop Services , Win32_TerminalServiceSetting class
- Win32_TerminalServiceSetting class Remote Desktop Services , EmptySpecifiedLicenseServerList method
topic_type:
- apiref
api_name:
- Win32_TerminalServiceSetting.EmptySpecifiedLicenseServerList
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# EmptySpecifiedLicenseServerList method of the Win32\_TerminalServiceSetting class

Removes all license servers from the list of specified license servers.

## Syntax


```mof
uint32 EmptySpecifiedLicenseServerList();
```



## Parameters

This method has no parameters.

## Return value

Returns 0 on success, otherwise returns a WMI error code. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                       |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TerminalServiceSetting**](win32-terminalservicesetting.md)
</dt> <dt>

[**AddLSToSpecifiedLicenseServerList**](addlstospecifiedlicenseserverlist-win32-terminalservicesetting.md)
</dt> <dt>

[**GetSpecifiedLicenseServerList**](getspecifiedlicenseserverlist-win32-terminalservicesetting.md)
</dt> <dt>

[**RemoveLSFromSpecifiedLicenseServerList**](removelsfromspecifiedlicenseserverlist-win32-terminalservicesetting.md)
</dt> <dt>

[**SetSpecifiedLicenseServerList**](setspecifiedlicenseserverlist-win32-terminalservicesetting.md)
</dt> </dl>

 

 





