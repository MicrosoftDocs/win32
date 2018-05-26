---
title: Add method of the PS\_VpnConnectionTriggerDnsConfiguration class
description: Adds a DNS suffix and the corresponding DNS servers to the configuration.
audience: developer
ms.assetid: 16D080E3-8069-431A-8A05-3FF487122CB6
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, PS_VpnConnectionTriggerDnsConfiguration class
- PS_VpnConnectionTriggerDnsConfiguration class, Add method
topic_type:
- apiref
api_name:
- PS_VpnConnectionTriggerDnsConfiguration.Add
api_location:
- VPNClientPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Add method of the PS\_VpnConnectionTriggerDnsConfiguration class

Adds a DNS suffix and the corresponding DNS servers to the configuration.

## Syntax


```mof
uint32 Add(
  [in]  string                               ConnectionName,
  [in]  string                               DnsSuffix[],
  [in]  string                               DnsIPAddress[],
  [in]  boolean                              PassThru,
  [in]  boolean                              Force,
  [out] VpnConnectionTriggerDnsConfiguration cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ConnectionName* \[in\]
</dt> <dd>

The name of the VPN connection profile to modify.

</dd> <dt>

*DnsSuffix* \[in\]
</dt> <dd>

The DNS suffix for auto triggering a VPN connection.

</dd> <dt>

*DnsIPAddress* \[in\]
</dt> <dd>

The IPv4/IPv6 addresses of the DNS servers to use for the DNS suffix.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the [**VpnConnectionTriggerDnsConfiguration**](vpnconnectiontriggerdnsconfiguration.md) object that contains the DNS configuration for VPN triggering; otherwise **false**.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

**True** to force the addition of the DNS servers for the DNS suffix; otherwise, **false**.

**Windows 8 and Windows Server 2012:** This parameter is not available until Windows 8.1 and Windows Server 2012 R2.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, contains the [**VpnConnectionTriggerDnsConfiguration**](vpnconnectiontriggerdnsconfiguration.md) object that holds the DNS configuration for VPN triggering.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\Client<br/>                                          |
| MOF<br/>                      | <dl> <dt>VPNClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VPNClientPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_VpnConnectionTriggerDnsConfiguration**](ps-vpnconnectiontriggerdnsconfiguration.md)
</dt> </dl>

 

 





