---
title: Disable method of the PS\_RemoteAccessRoutingDomain class
description: Disables site-to-site (S2S) VPN for the specified routing domain.
audience: developer
ms.assetid: 90d62a31-4eff-459a-a960-f20e439a83ab
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Disable method
- Disable method, PS_RemoteAccessRoutingDomain class
- PS_RemoteAccessRoutingDomain class, Disable method
topic_type:
- apiref
api_name:
- PS_RemoteAccessRoutingDomain.Disable
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Disable method of the PS\_RemoteAccessRoutingDomain class

Disables site-to-site (S2S) VPN for the specified routing domain.

## Syntax


```mof
uint32 Disable(
  [in]  string                     Name,
  [in]  boolean                    Force,
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

*Force* \[in\]
</dt> <dd>

Indicates whether this method uses the default confirmation prompt before performing the operation. **True** to use the default confirmation prompt, otherwise **false**. The default value for this parameter is **True**.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Indicates wether the *cmdletOutput* parameter returns an object. **True** to return an object; otherwise **false**.

</dd> <dt>

*Type* \[in\]
</dt> <dd>

The type of remote access component to disable.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

If *PassThru* is **true**, returns a [**RoutingDomainConfiguration**](remoteaccessroutingdomainconfiguration.md) object.

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

 

 





