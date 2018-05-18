---
title: CIM\_HostedResourcePool class
description: Represents an association between a system and a resource pool that is a component of the system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '42252526-3820-490e-bb5a-d656905beb02'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_HostedResourcePool class", "CIM_HostedResourcePool class, described"]
topic_type:
- apiref
api_name:
- CIM_HostedResourcePool
- CIM_HostedResourcePool.GroupComponent
- CIM_HostedResourcePool.PartComponent
api_location:
- VMMS.exe
api_type:
- DllExport
---

# CIM\_HostedResourcePool class

Represents an association between a system and a resource pool that is a component of the system.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Composition, Abstract, Version("2.22.0"), UMLPackagePath("CIM::Core::Resource")]
class CIM_HostedResourcePool : CIM_SystemComponent
{
  CIM_System       REF GroupComponent;
  CIM_ResourcePool REF PartComponent;
};
```

## Members

The **CIM\_HostedResourcePool** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_HostedResourcePool** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_System**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Aggregate**](https://msdn.microsoft.com/library/aa393650), [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The parent system in the association.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ResourcePool**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent")
</dt> </dl>

The resource pool that is a component of the system.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_SystemComponent**](cim-systemcomponent.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





