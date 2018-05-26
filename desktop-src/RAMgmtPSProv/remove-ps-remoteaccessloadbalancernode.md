---
title: Remove method of the PS\_RemoteAccessLoadBalancerNode class
description: This cmdlet removes a single remote access server from the load balancing cluster.
audience: developer
ms.assetid: 65c2298b-39c3-447f-9c5a-2c76722bdd86
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_RemoteAccessLoadBalancerNode class
- PS_RemoteAccessLoadBalancerNode class, Remove method
topic_type:
- apiref
api_name:
- PS_RemoteAccessLoadBalancerNode.Remove
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Remove method of the PS\_RemoteAccessLoadBalancerNode class

This cmdlet removes a single remote access server from the load balancing cluster.

## Syntax


```mof
uint32 Remove(
  [in]  string  RemoteAccessServer,
  [in]  string  ComputerName,
  [in]  boolean PassThru,
  [in]  boolean Force,
  [out] string  cmdletOutput
);
```



## Parameters

<dl> <dt>

*RemoteAccessServer* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the remote access server that needs to be removed from the load balancing cluster

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the Remote Access server machine specific tasks should be executed

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

When PassThru is specified this cmdlet returns the address of the server that was removed from the cluster. The cmdlet doesn't return an object by default

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Switch parameter used to suppress user confirmation prompts for the following conditions. When suppressed the cmdlet assumes user confirmation for the below mentioned changes. 1. Removal of node from the load balancing cluster. The total amount of load that the network can take reduces and so does the availability of the network

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Output will be the IPv4/IPv6 address or hostname of the server that was removed from the cluster

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

 

 





