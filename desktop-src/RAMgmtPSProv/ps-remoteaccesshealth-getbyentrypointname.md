---
title: GetByEntrypointName method of the PS\_RemoteAccessHealth class
description: This cmdlet is used to obtain the current health of a Remote Access deployment.
audience: developer
ms.assetid: d1a41e28-717b-45d0-891d-09a17823fa26
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetByEntrypointName method
- GetByEntrypointName method, PS_RemoteAccessHealth class
- PS_RemoteAccessHealth class, GetByEntrypointName method
topic_type:
- apiref
api_name:
- PS_RemoteAccessHealth.GetByEntrypointName
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetByEntrypointName method of the PS\_RemoteAccessHealth class

This cmdlet is used to obtain the current health of a Remote Access deployment.

1. Health of a specific Remote Access server

2. Health of a load balancing cluster

3. Health of a site, in case of a multisite deployment - this again corresponds to the health of a single server or health of a cluster at that site

## Syntax


```mof
uint32 GetByEntrypointName(
  [in]  string                    ComputerName,
  [in]  boolean                   Refresh,
  [in]  string                    EntrypointName,
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

*EntrypointName* \[in\]
</dt> <dd>

Entrypoint refers to the identity of a site in a multisite deployment whose health needs to be retrieved.

If both entrypoint and ComputerName are specified and the ComputerName does not belong to the site represented by the entrypoint then the entrypoint takes precedence and its health is retrieved

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

 

 





