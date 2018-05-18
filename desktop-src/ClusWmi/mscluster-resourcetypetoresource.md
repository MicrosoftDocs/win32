---
title: MSCluster\_ResourceTypeToResource class
description: A dynamic association WMI class that represents resources of a particular type.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '124eb30f-82d8-41fd-aa1e-8d3988178896'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSCluster_ResourceTypeToResource class", "MSCluster_ResourceTypeToResource class, described"]
topic_type:
- apiref
api_name:
- MSCluster_ResourceTypeToResource
- MSCluster_ResourceTypeToResource.GroupComponent
- MSCluster_ResourceTypeToResource.PartComponent
api_location:
- ClusWMI.dll
api_type:
- DllExport
---

# MSCluster\_ResourceTypeToResource class

A dynamic association [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents resources of a particular type.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{94F4F3DB-C193-42f1-B6AE-1C74817CD894}"), AMENDMENT]
class MSCluster_ResourceTypeToResource : CIM_Component
{
  MSCluster_ResourceType REF GroupComponent;
  MSCluster_Resource     REF PartComponent;
};
```

## Members

The **MSCluster\_ResourceTypeToResource** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_ResourceTypeToResource** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **[**MSCluster\_ResourceType**](mscluster-resourcetype.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent")
</dt> </dl>

The resource type.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **[**MSCluster\_Resource**](mscluster-resource.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The resource.

</dd> </dl>

## Remarks

The **MSCluster\_ResourceTypeToResource** class is derived from the [**CIM\_Component**](https://msdn.microsoft.com/library/aa387218) class.

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

[**MSCluster\_ResourceType**](mscluster-resourcetype.md)
</dt> <dt>

[**MSCluster\_Resource**](mscluster-resource.md)
</dt> </dl>

 

 





