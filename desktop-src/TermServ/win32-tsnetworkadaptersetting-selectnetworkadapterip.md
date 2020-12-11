---
title: SelectNetworkAdapterIP method of the Win32_TSNetworkAdapterSetting class
description: Selects a network adapter based on the adapter's IP address.
ms.assetid: 7f89fb83-8abe-421b-a48b-876c093e3a3d
ms.tgt_platform: multiple
keywords:
- SelectNetworkAdapterIP method Remote Desktop Services
- SelectNetworkAdapterIP method Remote Desktop Services , Win32_TSNetworkAdapterSetting class
- Win32_TSNetworkAdapterSetting class Remote Desktop Services , SelectNetworkAdapterIP method
topic_type:
- apiref
api_name:
- Win32_TSNetworkAdapterSetting.SelectNetworkAdapterIP
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SelectNetworkAdapterIP method of the Win32\_TSNetworkAdapterSetting class

Selects a network adapter based on the adapter's IP address.

## Syntax


```mof
uint32 SelectNetworkAdapterIP(
  [in] string NetworkAdapterIP
);
```



## Parameters

<dl> <dt>

*NetworkAdapterIP* \[in\]
</dt> <dd>

The IP address of the network adapter to set.

</dd> </dl>

## Return value

Returns zero if the specified IP address is valid, and returns a WMI error code if the IP address is invalid or does not exist. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values.

## Remarks

You can retrieve the IP address of a network adapter by enumerating the properties of the [**Win32\_TSNetworkAdapterListSetting**](win32-tsnetworkadapterlistsetting.md) class.

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

 

