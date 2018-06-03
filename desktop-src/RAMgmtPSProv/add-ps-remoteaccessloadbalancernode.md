---
title: Add method of the PS\_RemoteAccessLoadBalancerNode class
description: This cmdlet adds a single remote access server to the load balancing cluster.
audience: developer
ms.assetid: 26bb3f41-9ccd-4f94-8413-a39ce37f0a19
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, PS_RemoteAccessLoadBalancerNode class
- PS_RemoteAccessLoadBalancerNode class, Add method
topic_type:
- apiref
api_name:
- PS_RemoteAccessLoadBalancerNode.Add
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Add method of the PS\_RemoteAccessLoadBalancerNode class

This cmdlet adds a single remote access server to the load balancing cluster.

## Syntax


```mof
uint32 Add(
  [in]  string                       RemoteAccessServer,
  [in]  string                       InternalInterface,
  [in]  string                       InternetInterface,
  [in]  string                       VpnIPAddressRange[],
  [in]  string                       ComputerName,
  [in]  boolean                      Force,
  [in]  boolean                      PassThru,
  [out] RemoteAccessLoadBalancerNode cmdletOutput
);
```



## Parameters

<dl> <dt>

*RemoteAccessServer* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the remote access server that needs to be added to the load balancing cluster.

</dd> <dt>

*InternalInterface* \[in\]
</dt> <dd>

Name of the corpnet facing interface of the specified server. If name is not specified then cmdlet tries to detect the internal interface automatically. For a single-NIC configuration the same name is specified for both the internal and Internet interfaces.

</dd> <dt>

*InternetInterface* \[in\]
</dt> <dd>

Name of the Internet facing interface of the specified server. If name is not specified then cmdlet tries to detect the Internet interface automatically. For a single-NIC configuration the same name is specified for both the internal and Internet interfaces.

</dd> <dt>

*VpnIPAddressRange* \[in\]
</dt> <dd>

If VPN is enabled then this parameter must be specified. It indicates the IP address range from which IP addresses are allocated to VPN clients connecting to this server. The specified range should not overlap with the range configured on other servers in the cluster. Note that in a load balancing configuration VPN supports only static pool address assignment. DHCP address assignment is not supported.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the Remote Access server machine specific tasks should be executed. If ComputerName is specified it represents the cluster to which the server is added.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Switch parameter used to suppress user confirmation prompts for the following conditions. When suppressed the cmdlet assumes user confirmation for the below mentioned changes. 1. If self-signed NLS cert is found on all other nodes in the cluster then a self-signed cert is created for this node 2. If self-signed SSL (IPTTPS) cert is found on all other nodes in the cluster then a self-signed cert is created for this node.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns the remote access load balancer node object. By default this cmdlet does not generate any output.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

1. Address of the node added. 2. Load Balancing status 3. IP address ranges configured for VPN.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_RemoteAccessLoadBalancerNode**](ps-remoteaccessloadbalancernode.md)
</dt> </dl>

 

 





