---
title: SetByDisableLoadBalancing method of the PS\_RemoteAccessLoadBalancer class
description: This cmdlet does the following1.
audience: developer
ms.assetid: 6d5351f5-5076-41b5-992a-e3416235e701
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByDisableLoadBalancing method
- SetByDisableLoadBalancing method, PS_RemoteAccessLoadBalancer class
- PS_RemoteAccessLoadBalancer class, SetByDisableLoadBalancing method
topic_type:
- apiref
api_name:
- PS_RemoteAccessLoadBalancer.SetByDisableLoadBalancing
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetByDisableLoadBalancing method of the PS\_RemoteAccessLoadBalancer class

This cmdlet does the following1. Configures load balancing clusters on the internal and Internet interfaces (in case of double NIC) or on a single interface (in case of single NIC) for remote access and adds the current server to the cluster. Current server refers to the server on which this cmdlet is run. 2. Enables/disables usage of 3rd party load balancer.

## Syntax


```mof
uint32 SetByDisableLoadBalancing(
  [in]  boolean                  Disable,
  [in]  string                   ComputerName,
  [in]  boolean                  Force,
  [in]  boolean                  PassThru,
  [out] RemoteAccessLoadBalancer cmdletOutput
);
```



## Parameters

<dl> <dt>

*Disable* \[in\]
</dt> <dd>

When specified this switch parameter indicates that all forms of load balancing should be disabled all together.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed. If ComputerName is specified then this remote access server is added to the load balancing cluster that is created.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Switch parameter used to suppress user confirmation prompts for the following conditions. When suppressed the cmdlet assumes user confirmation for the below mentioned changes 1. Disabling load balancing disables high availability capabilities for the Remote Access deployment.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns the remote access load balancer configuration object. By default this cmdlet does not generate any output.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

1.  List of nodes in the cluster.
2.  Status of each node.
3.  VPN IP address range for each node (if applicable).
4.  Virtual IPs of the cluster.
5.  Status of third-party load balancer.

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

 

 





