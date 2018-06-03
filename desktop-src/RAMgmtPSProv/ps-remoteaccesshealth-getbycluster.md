---
title: GetByCluster method of the PS\_RemoteAccessHealth class
description: This cmdlet is used to obtain the current health of a Remote Access deployment.
audience: developer
ms.assetid: dda2f546-60f1-40fa-979a-e2752abe1819
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetByCluster method
- GetByCluster method, PS_RemoteAccessHealth class
- PS_RemoteAccessHealth class, GetByCluster method
topic_type:
- apiref
api_name:
- PS_RemoteAccessHealth.GetByCluster
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetByCluster method of the PS\_RemoteAccessHealth class

This cmdlet is used to obtain the current health of a Remote Access deployment.

1. Health of a specific Remote Access server

2. Health of a load balancing cluster

3. Health of a site, in case of a multisite deployment - this again corresponds to the health of a single server or health of a cluster at that site

## Syntax


```mof
uint32 GetByCluster(
  [in]  string                    ComputerName,
  [in]  boolean                   Refresh,
  [in]  boolean                   Cluster,
  [out] RemoteAccessHealthMonitor cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Indicates the IPv4/IPv6 address or hostname of the computer on which the cmdlet needs to be executed and health retrieved. When ComputerName is specified the health of that Remote Access server is returned

</dd> <dt>

*Refresh* \[in\]
</dt> <dd>

Specifying this parameter indicates that the health details for the specified ComputerName/Cluster or EntryPoint should be re-computed.

</dd> <dt>

*Cluster* \[in\]
</dt> <dd>

Specifying this parameter indicates that the health for the entire cluster needs to be retrieved. If both cluster and ComputerName are specified then the health of the cluster to which the ComputerName belongs is returned. If cluster is specified in a multi-site scenario then the health of the cluster in the site to which the server on which the cmdlet is executed belongs is returned. The server could also be represented by using the ComputerName parameter

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Objects consisting of the following properties for cluster, server and components of server

1. Component name

2. Remote Access server address

3. HealthState

4. TimeStamp

5. OperationStatus

6. Id

7. ErrorDesc

8. ErrorCause

9. ErrorResoln

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

[**PS\_RemoteAccessHealth**](ps-remoteaccesshealth.md)
</dt> </dl>

 

 





