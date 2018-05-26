---
title: Set method of the PS\_VpnConnectionTriggerDnsConfiguration class
description: Sets the DNS servers for a DNS suffix in the configuration and the DNS suffix search list.
audience: developer
ms.assetid: B49A98A6-EC6C-4DC6-B148-3692E69114E8
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_VpnConnectionTriggerDnsConfiguration class
- PS_VpnConnectionTriggerDnsConfiguration class, Set method
topic_type:
- apiref
api_name:
- PS_VpnConnectionTriggerDnsConfiguration.Set
api_location:
- VPNClientPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Set method of the PS\_VpnConnectionTriggerDnsConfiguration class

Sets the DNS servers for a DNS suffix in the configuration and the DNS suffix search list.

## Syntax


```mof
uint32 Set(
  [in]  string                               ConnectionName,
  [in]  string                               DnsSuffix,
  [in]  string                               DnsIPAddress[],
  [in]  string                               DnsSuffixSearchList[],
  [in]  boolean                              PassThru,
  [in]  boolean                              Force,
  [out] VpnConnectionTriggerDnsConfiguration cmdletOutput
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

The IPv4/IPv6 addresses of the DNS servers to use for the specified DNS suffix.

</dd> <dt>

*DnsSuffixSearchList* \[in\]
</dt> <dd>

The DNS suffix search list for the auto-triggered VPN connection.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the [**VpnConnectionTriggerDnsConfiguration**](vpnconnectiontriggerdnsconfiguration.md) object that contains the DNS configuration for VPN triggering; otherwise **false**.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

**True** to force the resetting of the DNS servers for the DNS suffix; otherwise, **false**.

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

 

 





