---
title: Enable method of the PS\_RemoteAccessRoutingDomain class
description: Enables site-to-site (S2S) VPN for the specified routing domain.
audience: developer
ms.assetid: 21a9f3d3-71fc-4506-be8c-c0d011fce8f4
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Enable method
- Enable method, PS_RemoteAccessRoutingDomain class
- PS_RemoteAccessRoutingDomain class, Enable method
topic_type:
- apiref
api_name:
- PS_RemoteAccessRoutingDomain.Enable
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Enable method of the PS\_RemoteAccessRoutingDomain class

Enables site-to-site (S2S) VPN for the specified routing domain.

## Syntax


```mof
uint32 Enable(
  [in]  string                     Name,
  [in]  boolean                    PassThru,
  [in]  uint32                     Type,
  [out] RoutingDomainConfiguration cmdletOutput
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the routing domain.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Indicates wether the *cmdletOutput* parameter returns an object. **True** to return an object; otherwise **false**.

</dd> <dt>

*Type* \[in\]
</dt> <dd>

The type of remote access component to enable.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The [**RoutingDomainConfiguration**](routingdomainconfiguration.md) object that receives the updated routing domain configuration.

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

 

 





