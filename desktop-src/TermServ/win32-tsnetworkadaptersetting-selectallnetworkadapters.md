---
title: SelectAllNetworkAdapters method of the Win32_TSNetworkAdapterSetting class
description: The SelectAllNetworkAdapters method selects all network adapters.
ms.assetid: e0bd60c3-55c3-4be9-be2d-3b97db3047d9
ms.tgt_platform: multiple
keywords:
- SelectAllNetworkAdapters method Remote Desktop Services
- SelectAllNetworkAdapters method Remote Desktop Services , Win32_TSNetworkAdapterSetting class
- Win32_TSNetworkAdapterSetting class Remote Desktop Services , SelectAllNetworkAdapters method
topic_type:
- apiref
api_name:
- Win32_TSNetworkAdapterSetting.SelectAllNetworkAdapters
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SelectAllNetworkAdapters method of the Win32\_TSNetworkAdapterSetting class

The **SelectAllNetworkAdapters** method selects all network adapters.

## Syntax


```mof
uint32 SelectAllNetworkAdapters();
```



## Parameters

This method has no parameters.

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

[**Win32\_TSNetworkAdapterSetting**](win32-tsnetworkadaptersetting.md)
</dt> </dl>

 

