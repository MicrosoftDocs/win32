---
title: RoutingDomainConfiguration class
description: Retrieves and updates a routing domain configuration for the Remote Access service.
audience: developer
ms.assetid: 5469f10c-34e1-43b6-924c-e399a523bef2
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RoutingDomainConfiguration class
- RoutingDomainConfiguration class, described
topic_type:
- apiref
api_name:
- RoutingDomainConfiguration
- RoutingDomainConfiguration.RoutingDomain
- RoutingDomainConfiguration.RoutingDomainID
- RoutingDomainConfiguration.RoutingDomainStatus
- RoutingDomainConfiguration.VpnStatus
- RoutingDomainConfiguration.VpnS2SStatus
- RoutingDomainConfiguration.RoutingStatus
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RoutingDomainConfiguration class

Retrieves and updates a routing domain configuration for the Remote Access service.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class RoutingDomainConfiguration
{
  string RoutingDomain;
  string RoutingDomainID;
  string RoutingDomainStatus;
  uint32 VpnStatus;
  uint32 VpnS2SStatus;
  uint32 RoutingStatus;
};
```

## Members

The **RoutingDomainConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **RoutingDomainConfiguration** class has these properties.

<dl> <dt>

**RoutingDomain**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The friendly Name of the routing domain

</dd> <dt>

**RoutingDomainID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The ID of the routing domain

</dd> <dt>

**RoutingDomainStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The status of the routing domain

</dd> <dt>

**RoutingStatus**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The routing status for the routing domain

</dd> <dt>

**VpnS2SStatus**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The site-to-site (S2S) status for the routing domain

</dd> <dt>

**VpnStatus**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The VPN status for the routing domain

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

[RAMgmtPSProvider Provider Classes](remote-access-management.md)
</dt> </dl>

 

 





