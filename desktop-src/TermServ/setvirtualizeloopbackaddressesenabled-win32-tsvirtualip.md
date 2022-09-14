---
title: SetVirtualizeLoopbackAddressesEnabled method of the Win32_TSVirtualIP class
description: Sets the VirtualizeLoopbackAddressesEnabled property value.
ms.assetid: 84A4FF36-82B3-462A-9D2E-C15DD99524E4
ms.tgt_platform: multiple
keywords:
- SetVirtualizeLoopbackAddressesEnabled method Remote Desktop Services
- SetVirtualizeLoopbackAddressesEnabled method Remote Desktop Services , Win32_TSVirtualIP class
- Win32_TSVirtualIP class Remote Desktop Services , SetVirtualizeLoopbackAddressesEnabled method
topic_type:
- apiref
api_name:
- Win32_TSVirtualIP.SetVirtualizeLoopbackAddressesEnabled
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetVirtualizeLoopbackAddressesEnabled method of the Win32\_TSVirtualIP class

Sets the **VirtualizeLoopbackAddressesEnabled** property value.

## Syntax


```mof
uint32 SetVirtualizeLoopbackAddressesEnabled(
  [in] uint32 VirtualizeLoopbackAddressesEnabled
);
```



## Parameters

<dl> <dt>

*VirtualizeLoopbackAddressesEnabled* \[in\]
</dt> <dd>

Specifies whether to enable loopback address virtualization. This can be one of the following values.

<dt>

0
</dt> <dd>

Do not enable loopback address virtualization.

</dd> <dt>

1
</dt> <dd>

Enable loopback address virtualization.

</dd> </dl> </dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values. The method returns an error if the setting is under group policy control.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TSVirtualIP**](win32-tsvirtualip.md)
</dt> </dl>

 

 





