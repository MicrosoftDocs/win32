---
title: Remove method of the PS\_BgpRoutingPolicy class
description: Removes one or more BGP routing policies from the policy store.
audience: developer
ms.assetid: 3e9fd5f3-2a71-4b43-a34f-486795462cc2
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_BgpRoutingPolicy class
- PS_BgpRoutingPolicy class, Remove method
topic_type:
- apiref
api_name:
- PS_BgpRoutingPolicy.Remove
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Remove method of the PS\_BgpRoutingPolicy class

Removes one or more BGP routing policies from the policy store.

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

An array that contains the BGP routing policies to remove.

</dd> <dt>

*RoutingDomain* \[in\]
</dt> <dd>

The user-defined alphanumeric ID of the routing domain.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Indicates whether to confirm this procedure with a confirmation prompt.

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

[**PS\_BgpRoutingPolicy**](ps-bgproutingpolicy.md)
</dt> </dl>

 

 





