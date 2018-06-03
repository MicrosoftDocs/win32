---
title: New method of the PS\_VpnTrafficSelector class
description: Creates a new traffic selector.
audience: developer
ms.assetid: 1AE0E6CF-BB35-4B10-A059-4155815D27DE
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- New method
- New method, PS_VpnTrafficSelector interface
- PS_VpnTrafficSelector interface, New method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# New method of the PS\_VpnTrafficSelector class

Creates a new traffic selector.

## Syntax


```mof
uint32 New(
  [in]  string             IPAddressRange[],
  [in]  uint32             PortRange[],
  [in]  uint32             ProtocolId,
  [in]  uint16             TsPayloadId,
  [in]  uint32             Type,
  [out] VpnTrafficSelector cmdletOutput
);
```



## Parameters

<dl> <dt>

*IPAddressRange* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*PortRange* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*ProtocolId* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*TsPayloadId* \[in\]
</dt> <dd>

Identifier tag for the [**VPNTrafficSelector**](vpntrafficselector.md).

</dd> <dt>

*Type* \[in\]
</dt> <dd>

Specifies whether the filter is IPv4 or IPv6 filter. {IPv4 \| IPv6}.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the resulting [**VpnTrafficSelector**](vpntrafficselector.md) instance.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_VpnTrafficSelector**](ps-vpntrafficselector.md)
</dt> </dl>

 

 





