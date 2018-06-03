---
title: Get method of the PS\_RemoteAccessLoadBalancer class
description: This cmdlet displays the load balancing configuration.
audience: developer
ms.assetid: c1c49050-38ae-49a7-80f2-d99d4596afd3
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_RemoteAccessLoadBalancer class
- PS_RemoteAccessLoadBalancer class, Get method
topic_type:
- apiref
api_name:
- PS_RemoteAccessLoadBalancer.Get
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_RemoteAccessLoadBalancer class

This cmdlet displays the load balancing configuration.

## Syntax


```mof
uint32 Get(
  [in]  string                   ComputerName,
  [in]  string                   EntrypointName,
  [in]  boolean                  Brief,
  [out] RemoteAccessLoadBalancer cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed.

</dd> <dt>

*EntrypointName* \[in\]
</dt> <dd>

Entrypoint refers to the identity of a site in a multi-site deployment whose load balancing configuration needs to be retrieved. If entrypoint is not specified then the entrypoint to which the server on which the cmdlet is executed belongs is used. The server could also be represented using the ComputerName parameter. If both entrypoint and computername are specified and the ComputerName doesn't belong to the site represented by the entrypoint then the entrypoint takes precedence and its load balancing configuration is retrieved.

</dd> <dt>

*Brief* \[in\]
</dt> <dd>

This is a switch parameter which suppresses the retrieval of node status.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

1. List of nodes in the cluster. 2. Status of each node. 3. VPN IP address range for each node (if applicable). 4. IPv6 prefix assigned to VPN clients (if applicable). 5. List of internal and Internet virtual IPs of the cluster. 6. Status of 3rd party load balancer

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

 

 





