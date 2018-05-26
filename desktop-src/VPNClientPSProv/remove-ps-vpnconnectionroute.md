---
title: Remove method of the PS\_VpnConnectionRoute class
description: Removes a route from the routes to be plumbed for a VPN profile.
audience: developer
ms.assetid: A8CC8B28-D35E-4234-B1D0-D49D6EDDA1BF
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_VpnConnectionRoute class
- PS_VpnConnectionRoute class, Remove method
topic_type:
- apiref
api_name:
- PS_VpnConnectionRoute.Remove
api_location:
- VPNClientPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Remove method of the PS\_VpnConnectionRoute class

Removes a route from the routes to be plumbed for a VPN profile.

## Syntax


```mof
uint32 Remove(
  [in]  string        ConnectionName,
  [in]  string        DestinationPrefix,
  [in]  boolean       AllUserConnection,
  [in]  boolean       PassThru,
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

*AllUserConnection* \[in\]
</dt> <dd>

**True** if the VPN connection profile is for all users; **false** if it is for a single user.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the [**MSFT\_NetRoute**](https://msdn.microsoft.com/library/hh872448) object; otherwise, **false**.

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

 

 





