---
title: BgpRouteAggregateConfig class
description: Contains BGP route-aggregation configuration information.
audience: developer
ms.assetid: 2f97e477-c3d9-4cc8-921f-1d6c96fc95ef
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- BgpRouteAggregateConfig class
- BgpRouteAggregateConfig class, described
topic_type:
- apiref
api_name:
- BgpRouteAggregateConfig
- BgpRouteAggregateConfig.Prefix
- BgpRouteAggregateConfig.RoutingDomain
- BgpRouteAggregateConfig.SummaryOnly
- BgpRouteAggregateConfig.PreserveASPath
- BgpRouteAggregateConfig.AttributePolicy
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# BgpRouteAggregateConfig class

Contains BGP route-aggregation configuration information.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class BgpRouteAggregateConfig
{
  string Prefix;
  string RoutingDomain;
  uint32 SummaryOnly;
  uint32 PreserveASPath;
  string AttributePolicy[];
};
```

## Members

The **BgpRouteAggregateConfig** class has these types of members:

-   [Properties](#properties)

### Properties

The **BgpRouteAggregateConfig** class has these properties.

<dl> <dt>

**AttributePolicy**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The policies configured for the aggregator.

</dd> <dt>

**Prefix**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The admin configured prefix of the aggregator.

</dd> <dt>

**PreserveASPath**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the autonomous system path of participant routes will be advertised.

</dd> <dt>

**RoutingDomain**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The friendly name of the Routing Domain.

</dd> <dt>

**SummaryOnly**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the most specific routes will be advertised.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>Ramgmtpsprovider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





