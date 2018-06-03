---
title: Get method of the PS\_RemoteAccessRoutingDomain class
description: Retrieves a VPN routing domain configuration for the specified routing domain, or for all routing domains of the gateway.
audience: developer
ms.assetid: 3ecdf1dd-cb3e-4f50-8a38-3c90f11c0858
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_RemoteAccessRoutingDomain class
- PS_RemoteAccessRoutingDomain class, Get method
topic_type:
- apiref
api_name:
- PS_RemoteAccessRoutingDomain.Get
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_RemoteAccessRoutingDomain class

Retrieves a VPN routing domain configuration for the specified routing domain, or for all routing domains of the gateway.

## Syntax


```mof
uint32 Get(
  [in]  string                 Name,
  [out] VpnRoutingDomainConfig cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the routing domain that specifies the VPN routing domain configuration to retrieve. If this parameter is not specified, the VPN routing domain configurations for all routing domains is retrieved.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The[**VpnRoutingDomainConfig**](vpnroutingdomainconfig.md) object that receives the retrieved routing domain configurations.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_RemoteAccessRoutingDomain**](ps-remoteaccessroutingdomain.md)
</dt> </dl>

 

 





