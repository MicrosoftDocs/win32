---
title: Get method of the PS\_VpnConnection class
description: Retrieves virtual private network (VPN) connection profiles.
audience: developer
ms.assetid: d6339336-4a26-4d78-85e7-dcffcc29bd81
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_VpnConnection class
- PS_VpnConnection class, Get method
topic_type:
- apiref
api_name:
- PS_VpnConnection.Get
api_location:
- VPNClientPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_VpnConnection class

Retrieves virtual private network (VPN) connection profiles.

## Syntax


```mof
static uint32 Get(
  [in]  string          Name[],
  [in]  boolean         AllUserConnection,
  [out] VpnCommonConfig cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The names of the VPN connection profiles to retrieve.

</dd> <dt>

*AllUserConnection* \[in\]
</dt> <dd>

**True** if the VPN connection profile is for all users; **false** if it is for a single user.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, contains the [**VpnConnection**](vpnconnection.md) object.

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

[**PS\_VpnConnection**](ps-vpnconnection.md)
</dt> </dl>

 

 





