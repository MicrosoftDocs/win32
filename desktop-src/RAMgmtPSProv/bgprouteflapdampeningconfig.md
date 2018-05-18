---
title: BgpRouteFlapDampeningConfig class
description: Contains BGP route-flap-dampening configuration information.
audience: developer
ms.assetid: '4da0ab53-0667-4279-94a3-5cdb6c6e44a3'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["BgpRouteFlapDampeningConfig class", "BgpRouteFlapDampeningConfig class, described"]
topic_type:
- apiref
api_name:
- BgpRouteFlapDampeningConfig
- BgpRouteFlapDampeningConfig.RoutingDomain
- BgpRouteFlapDampeningConfig.ReuseThreshold
- BgpRouteFlapDampeningConfig.SuppressThreshold
- BgpRouteFlapDampeningConfig.HalfLife
- BgpRouteFlapDampeningConfig.HalfLifeUnreachable
- BgpRouteFlapDampeningConfig.MaxSuppressTime
- BgpRouteFlapDampeningConfig.Ceiling
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# BgpRouteFlapDampeningConfig class

Contains BGP route-flap-dampening configuration information.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class BgpRouteFlapDampeningConfig
{
  string RoutingDomain;
  uint32 ReuseThreshold;
  uint32 SuppressThreshold;
  uint32 HalfLife;
  uint32 HalfLifeUnreachable;
  uint32 MaxSuppressTime;
  uint32 Ceiling;
};
```

## Members

The **BgpRouteFlapDampeningConfig** class has these types of members:

-   [Properties](#properties)

### Properties

The **BgpRouteFlapDampeningConfig** class has these properties.

<dl> <dt>

**Ceiling**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The highest value that figure-of-merit can attain.

</dd> <dt>

**HalfLife**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The duration after which the instability value of the Reachable route decreases to half if no flaps occur, in minutes.

</dd> <dt>

**HalfLifeUnreachable**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The duration after which the instability value of the Unreachable route decreases to half if no flaps occur, in minutes.

</dd> <dt>

**MaxSuppressTime**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum time for which the route is to be suppressed, no matter how unstable it has been before the period of stability.

</dd> <dt>

**ReuseThreshold**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The value below which the suppressed route will become usable again in BGP routing. The value is expressed in number of route withdrawals.

</dd> <dt>

**RoutingDomain**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A User defined alphanumeric ID of the BGP routing domain. For use in multi-tenant deployment only.

</dd> <dt>

**SuppressThreshold**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The value above which a route will become unusable. The value is expressed in number of route withdrawals.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>Ramgmtpsprovider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





