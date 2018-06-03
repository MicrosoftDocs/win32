---
title: Remove method of the PS\_BgpPeer class
description: Removes a BGP peer from a BGP router.
audience: developer
ms.assetid: 5afa7b9f-493f-44c7-92b4-f00e92dbd2cd
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_BgpPeer class
- PS_BgpPeer class, Remove method
topic_type:
- apiref
api_name:
- PS_BgpPeer.Remove
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Remove method of the PS\_BgpPeer class

Removes a BGP peer from a BGP router.

## Syntax


```mof
uint32 Remove(
  [in] string  Name[],
  [in] string  RoutingDomain,
  [in] boolean Force
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The BGP peer names that identify the peers to delete.

</dd> <dt>

*RoutingDomain* \[in\]
</dt> <dd>

The user-defined unique alphanumeric ID of the BGP routing domain.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Indicates whether to use a confirmation prompt to remove the peer. **True** to use a confirmation prompt; otherwise **false**.

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

[**PS\_BgpPeer**](ps-bgppeer.md)
</dt> </dl>

 

 





