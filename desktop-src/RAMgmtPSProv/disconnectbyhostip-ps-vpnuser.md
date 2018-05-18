---
title: DisconnectByHostIP method of the PS\_VpnUser class
description: This cmdlet disconnects a VPN connection originated by a specific user or originating from a specific client machine.
audience: developer
ms.assetid: '376927b2-b234-4ebc-8760-d7faf5e8eb6c'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DisconnectByHostIP method", "DisconnectByHostIP method, PS_VpnUser class", "PS_VpnUser class, DisconnectByHostIP method"]
topic_type:
- apiref
api_name:
- PS_VpnUser.DisconnectByHostIP
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
---

# DisconnectByHostIP method of the PS\_VpnUser class

This cmdlet disconnects a VPN connection originated by a specific user or originating from a specific client machine

## Syntax


```mof
uint32 DisconnectByHostIP(
  [in]  string  ComputerName,
  [in]  boolean PassThru,
  [in]  string  HostIPAddress[],
  [out] string  cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed. When ComputerName is specified the cmdlet looks for the specified user or host IP on that remote access server

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns an object, viz. the list of users/client IPs that were successfully disconnected. By default this cmdlet does not generate any output

</dd> <dt>

*HostIPAddress* \[in\]
</dt> <dd>

List of tunnel IP address of the VPN connection. These can be IPv4 or IPv6 addresses.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

1. List of users successfully disconnected - if username is specified. 2. List of host machines successfully disconnected - if host IP is specified.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_VpnUser**](ps-vpnuser.md)
</dt> </dl>

 

 





