---
title: SetByEnableLoadBalancing method of the PS\_RemoteAccessLoadBalancer class
description: This cmdlet does the following1.
audience: developer
ms.assetid: fedcfc25-e682-4aa8-86a7-1a946b7c6e44
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByEnableLoadBalancing method
- SetByEnableLoadBalancing method, PS_RemoteAccessLoadBalancer class
- PS_RemoteAccessLoadBalancer class, SetByEnableLoadBalancing method
topic_type:
- apiref
api_name:
- PS_RemoteAccessLoadBalancer.SetByEnableLoadBalancing
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetByEnableLoadBalancing method of the PS\_RemoteAccessLoadBalancer class

This cmdlet does the following1. Configures load balancing clusters on the internal and Internet interfaces (in case of double NIC) or on a single interface (in case of single NIC) for remote access and adds the current server to the cluster. Current server refers to the server on which this cmdlet is run. 2. Enables/disables usage of third-party load balancer.

## Syntax


```mof
uint32 SetByEnableLoadBalancing(
  [in]  boolean                  UseThirdPartyLoadBalancer,
  [in]  string                   InternetDedicatedIPAddress[],
  [in]  string                   InternalDedicatedIPAddress[],
  [in]  string                   InternetVirtualIPAddress[],
  [in]  string                   InternalVirtualIPAddress[],
  [in]  string                   ComputerName,
  [in]  boolean                  PassThru,
  [out] RemoteAccessLoadBalancer cmdletOutput
);
```



## Parameters

<dl> <dt>

*UseThirdPartyLoadBalancer* \[in\]
</dt> <dd>

At the time of enabling network load balancing for Remote Access in a single NIC or double NIC configuration this switch parameter is used to indicate that an external 3rd party load balancer should be used for the distribution (load sharing) of Remote Access connection requests across all nodes in the cluster.

</dd> <dt>

*InternetDedicatedIPAddress* \[in\]
</dt> <dd>

One or more IP addresses with subnet masks which the user wants to use as the dedicated IP addresses for load balancing on the Internet interface. Format: IPv4 address with subnet in the format IP\_ADDR/SUBNET or IPv6 address.

</dd> <dt>

*InternalDedicatedIPAddress* \[in\]
</dt> <dd>

One or more IP addresses with subnet masks which the user wants to use as the dedicated IP addresses for load balancing on the internal interface. Format: IPv4 address with subnet in the format IP\_ADDR/SUBNET or IPv6 address.

</dd> <dt>

*InternetVirtualIPAddress* \[in\]
</dt> <dd>

A virtual IP is an IP address that is shared among the hosts of a Network Load Balancing cluster and used by clients to address the cluster as a whole. A Network Load Balancing cluster supports multiple virtual IP addresses. This parameter represents one or more IP addresses with subnet masks which the user wants to use as the virtual IP addresses for load balancing on the Internet interface. Format: IPv4 address with subnet in the format IP\_ADDR/SUBNET or IPv6 address. The list of IPs specified should include the IPsec tunnel endpoint IPs on the Internet interface. If they are not included then the cmdlet errors out. If the Internet virtual IPs are not specified then by default the IPsec tunnel endpoint IPs on the Internet interface are used.

</dd> <dt>

*InternalVirtualIPAddress* \[in\]
</dt> <dd>

One or more IP addresses with subnet masks which the user wants to use as the virtual IP addresses for load balancing on the internal interface. These are typically the current IP addresses on the internal interface of the server on which the cmdlet is executed Format: IPv4 address with subnet in the format IP\_ADDR/SUBNET or IPv6 address A virtual IP is an IP address that is shared among the hosts of a Network Load Balancing cluster and used by clients to address the cluster as a whole. A Network Load Balancing cluster supports multiple virtual IP addresses This parameter represents one or more IP addresses with subnet masks which the user wants to use as the virtual IP addresses for load balancing on the internal interface. Format: IPv4 address with subnet in the format IP\_ADDR/SUBNET or IPv6 address If ISATAP is deployed in the internal network then at least one of the IPs specified in the parameter should be present in the ISATAP name entry in DNS.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed. If ComputerName is specified then this remote access server is added to the load balancing cluster that is created.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns the remote access load balancer configuration object. By default this cmdlet does not generate any output.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

1. List of nodes in the cluster 2. Status of each node 3. VPN IP address range for each node (if applicable) 4. Virtual IPs of the cluster 5. Status of 3rd party load balancer

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

[**PS\_RemoteAccessLoadBalancer**](ps-remoteaccessloadbalancer.md)
</dt> </dl>

 

 





