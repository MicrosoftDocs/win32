---
title: DisconnectByUserName method of the PS\_VpnUserLocal class
description: Disconnects the specified user.
audience: developer
ms.assetid: 'e47a7bcb-b514-47af-8eed-a2b43eb5f687'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DisconnectByUserName method", "DisconnectByUserName method, PS_VpnUserLocal class", "PS_VpnUserLocal class, DisconnectByUserName method"]
topic_type:
- apiref
api_name:
- PS_VpnUserLocal.DisconnectByUserName
api_location:
- RAServerPSProvider.dll
api_type:
- COM
---

# DisconnectByUserName method of the PS\_VpnUserLocal class

Disconnects the specified user.

## Syntax


```mof
uint32 DisconnectByUserName(
  [in]  string UserName[],
  [out] uint32 StatusCodes[]
);
```



## Parameters

<dl> <dt>

*UserName* \[in\]
</dt> <dd>

Array of user names to disconnect

</dd> <dt>

*StatusCodes* \[out\]
</dt> <dd>

Error codes returned by the internal RPC APIs

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_VpnUserLocal**](ps-vpnuserlocal.md)
</dt> </dl>

 

 





