---
title: Add method of the PS\_VpnConnectionRoute class
description: Adds a route to be plumbed for a VPN profile.
audience: developer
ms.assetid: B2A6EDD1-49D3-4E8D-81CF-55902E8EE3B4
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, PS_VpnConnectionRoute class
- PS_VpnConnectionRoute class, Add method
topic_type:
- apiref
api_name:
- PS_VpnConnectionRoute.Add
api_location:
- VPNClientPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Add method of the PS\_VpnConnectionRoute class

Adds a route to be plumbed for a VPN profile.

## Syntax


```mof
uint32 Add(
  [in]  string        ConnectionName,
  [in]  string        DestinationPrefix,
  [in]  uint32        RouteMetric,
  [in]  boolean       PassThru,
  [in]  boolean       AllUserConnection,
  [out] MSFT_NetRoute cmdletOutput
);
```



## Parameters

<dl> <dt>

*ConnectionName* \[in\]
</dt> <dd>

The name of the VPN connection profile to modify.

</dd> <dt>

*DestinationPrefix* \[in\]
</dt> <dd>

The destination prefix of the route.

</dd> <dt>

*RouteMetric* \[in\]
</dt> <dd>

The route metric.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the [**MSFT\_NetRoute**](https://msdn.microsoft.com/library/hh872448) object; otherwise **false**.

</dd> <dt>

*AllUserConnection* \[in\]
</dt> <dd>

**True** if the VPN connection profile is for all users; **false** if it is for a single user.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, contains the [**MSFT\_NetRoute**](https://msdn.microsoft.com/library/hh872448) object. The destination prefix and metric field are populated.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\Client<br/>                                          |
| MOF<br/>                      | <dl> <dt>VPNClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VPNClientPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_VpnConnectionRoute**](ps-vpnconnectionroute.md)
</dt> </dl>

 

 





