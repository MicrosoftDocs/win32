---
title: MSCluster\_ResourceGroupToResource class
description: A dynamic association WMI class that represents the resources in a group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a4637341-4a89-428e-8f78-7d87da73d537'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSCluster_ResourceGroupToResource class", "MSCluster_ResourceGroupToResource class, described"]
topic_type:
- apiref
api_name:
- MSCluster_ResourceGroupToResource
- MSCluster_ResourceGroupToResource.GroupComponent
- MSCluster_ResourceGroupToResource.PartComponent
api_location:
- ClusWMI.dll
api_type:
- DllExport
---

# MSCluster\_ResourceGroupToResource class

A dynamic association [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents the resources in a group.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{38DD5882-2610-4ba1-B24E-1CD955B7A6BF}"), AMENDMENT]
class MSCluster_ResourceGroupToResource : CIM_Component
{
  MSCluster_ResourceGroup REF GroupComponent;
  MSCluster_Resource      REF PartComponent;
};
```

## Members

The **MSCluster\_ResourceGroupToResource** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_ResourceGroupToResource** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **[**MSCluster\_ResourceGroup**](mscluster-resourcegroup.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The group.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **[**MSCluster\_Resource**](mscluster-resource.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent")
</dt> </dl>

The resources within the group.

</dd> </dl>

## Remarks

The **MSCluster\_ResourceGroupToResource** class is derived from the [**CIM\_Component**](https://msdn.microsoft.com/library/aa387218) class.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Component**](cim-component.md)
</dt> <dt>

[Failover Cluster Provider Reference](server-cluster-provider-reference.md)
</dt> <dt>

[**MSCluster\_ResourceGroup**](mscluster-resourcegroup.md)
</dt> <dt>

[**MSCluster\_Resource**](mscluster-resource.md)
</dt> </dl>

 

 





