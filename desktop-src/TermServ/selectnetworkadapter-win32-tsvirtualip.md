---
title: SelectNetworkAdapter method of the Win32_TSVirtualIP class
description: Sets the MAC address of the network adapter to use for IP virtualization.
ms.assetid: ad67445c-6a8b-4980-997a-56aceb70965f
ms.tgt_platform: multiple
keywords:
- SelectNetworkAdapter method Remote Desktop Services
- SelectNetworkAdapter method Remote Desktop Services , Win32_TSVirtualIP class
- Win32_TSVirtualIP class Remote Desktop Services , SelectNetworkAdapter method
topic_type:
- apiref
api_name:
- Win32_TSVirtualIP.SelectNetworkAdapter
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SelectNetworkAdapter method of the Win32\_TSVirtualIP class

Sets the MAC address of the network adapter to use for IP virtualization.

## Syntax


```mof
uint32 SelectNetworkAdapter(
  [in] string NetworkAdapterMacAddress
);
```



## Parameters

<dl> <dt>

*NetworkAdapterMacAddress* \[in\]
</dt> <dd>

Type: **string**

Specifies the MAC address of the network adapter.

</dd> </dl>

## Return value

Type: **uint32**

Returns 0 on success, otherwise returns a WMI error code. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values.

If the MAC address is invalid or does not exist, or if the IP virtualization mode is per-session, an error is returned.

The method returns an error if the setting is under group policy control.

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

[**Win32\_TSVirtualIP**](win32-tsvirtualip.md)
</dt> </dl>

 

 





