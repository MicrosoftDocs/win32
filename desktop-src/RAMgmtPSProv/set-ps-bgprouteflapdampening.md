---
title: Set method of the PS\_BgpRouteFlapDampening class
description: Set-BgpRouteFlapDampening cmdlet configures the BGP Route Dampening engine.
audience: developer
ms.assetid: 9f410b7c-fa2d-4016-9299-feb578f6c471
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_BgpRouteFlapDampening class
- PS_BgpRouteFlapDampening class, Set method
topic_type:
- apiref
api_name:
- PS_BgpRouteFlapDampening.Set
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Set method of the PS\_BgpRouteFlapDampening class

Set-BgpRouteFlapDampening cmdlet configures the BGP Route Dampening engine.

## Syntax


```mof
uint32 Set(
  [in]  string                      RoutingDomain,
  [in]  uint32                      ReuseThreshold,
  [in]  uint32                      SuppressThreshold,
  [in]  uint32                      HalfLife,
  [in]  uint32                      HalfLifeUnreachable,
  [in]  uint32                      MaxSuppressTime,
  [in]  boolean                     PassThru,
  [in]  boolean                     Force,
  [out] BgpRouteFlapDampeningConfig cmdletOutput
);
```



## Parameters

<dl> <dt>

*RoutingDomain* \[in\]
</dt> <dd>

User-defined unique alphanumeric identifier for the routing domain or tenant.

</dd> <dt>

*ReuseThreshold* \[in\]
</dt> <dd>

The value below which the suppressed route will become usable again in BGP routing. This value is expressed in number of route withdrawals.

</dd> <dt>

*SuppressThreshold* \[in\]
</dt> <dd>

The value above which a route will become unusable. This value is expressed in the number of route withdrawals.

</dd> <dt>

*HalfLife* \[in\]
</dt> <dd>

Time duration, in minutes, after which the instability value of the Reachable route decreases to half if no flaps occur.

</dd> <dt>

*HalfLifeUnreachable* \[in\]
</dt> <dd>

Time duration, in minutes, after which the instability value of the Unreachable route decreases to half if no flaps occur.

</dd> <dt>

*MaxSuppressTime* \[in\]
</dt> <dd>

The maximum time for which the route is to be suppressed, no matter how unstable it has been before the period of stability.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to indicate that the method returns an output object. The default is **false**.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

**true** for no end-user confirmation prompt when calling this method. The default is **false**.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

If *PassThru* is **true**, returns an embedded instance of the current object.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>Ramgmtpsprovider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_BgpRouteFlapDampening**](ps-bgprouteflapdampening.md)
</dt> </dl>

 

 





