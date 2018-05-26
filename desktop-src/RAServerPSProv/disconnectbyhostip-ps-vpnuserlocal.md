---
title: DisconnectByHostIP method of the PS\_VpnUserLocal class
description: Disconnects the specified user.
audience: developer
ms.assetid: 0bd95bf0-32d2-478f-bcc6-f270dd518505
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DisconnectByHostIP method
- DisconnectByHostIP method, PS_VpnUserLocal class
- PS_VpnUserLocal class, DisconnectByHostIP method
topic_type:
- apiref
api_name:
- PS_VpnUserLocal.DisconnectByHostIP
api_location:
- RAServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DisconnectByHostIP method of the PS\_VpnUserLocal class

Disconnects the specified user.

## Syntax


```mof
uint32 DisconnectByHostIP(
  [in]  string HostIPAddress[],
  [out] uint32 StatusCodes[]
);
```



## Parameters

<dl> <dt>

*HostIPAddress* \[in\]
</dt> <dd>

Array of host IP Addresses to disconnect

</dd> <dt>

*StatusCodes* \[out\]
</dt> <dd>

Error codes returned by the internal RPC APIs

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_VpnUserLocal**](ps-vpnuserlocal.md)
</dt> </dl>

 

 





