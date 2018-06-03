---
title: Remove method of the PS\_BgpRouter class
description: Removes a BGP router from the associated tenants.
audience: developer
ms.assetid: 668b0432-aa3c-4308-af53-5d588c79ca8e
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_BgpRouter class
- PS_BgpRouter class, Remove method
topic_type:
- apiref
api_name:
- PS_BgpRouter.Remove
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Remove method of the PS\_BgpRouter class

Removes a BGP router from the associated tenants.

## Syntax


```mof
uint32 Remove(
  [in] string  RoutingDomain[],
  [in] boolean Force
);
```



## Parameters

<dl> <dt>

*RoutingDomain* \[in\]
</dt> <dd>

The unique identifiers of the tenants that manage the BGP router.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Indicates no confirmation prompt before removing the BGP router for specified tenant.

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

[**PS\_BgpRouter**](ps-bgprouter.md)
</dt> </dl>

 

 





