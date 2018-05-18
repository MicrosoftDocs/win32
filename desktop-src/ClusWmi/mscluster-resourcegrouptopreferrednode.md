---
title: MSCluster\_ResourceGroupToPreferredNode class
description: A dynamic association WMI class that represents a list of the resource groups and their preferred nodes list.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '2b811476-bb93-43ff-a587-ed151f9e5a65'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSCluster_ResourceGroupToPreferredNode class", "MSCluster_ResourceGroupToPreferredNode class, described"]
topic_type:
- apiref
api_name:
- MSCluster_ResourceGroupToPreferredNode
- MSCluster_ResourceGroupToPreferredNode.PartComponent
- MSCluster_ResourceGroupToPreferredNode.GroupComponent
api_location:
- ClusWMI.dll
api_type:
- DllExport
---

# MSCluster\_ResourceGroupToPreferredNode class

A dynamic association [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a list of the resource [groups](https://msdn.microsoft.com/library/aa369645) and their preferred [nodes](https://msdn.microsoft.com/library/aa371745) list.

## Syntax

``` syntax
[Association, Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{3e1e37d2-ad0d-47b8-a802-b94b7e25aa21}"), AMENDMENT]
class MSCluster_ResourceGroupToPreferredNode : CIM_Component
{
  MSCluster_Node          REF PartComponent;
  MSCluster_ResourceGroup REF GroupComponent;
};
```

## Members

The **MSCluster\_ResourceGroupToPreferredNode** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_ResourceGroupToPreferredNode** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **MSCluster\_ResourceGroup**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The resource group.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **MSCluster\_Node**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent")
</dt> </dl>

The preferred node for the resource group.

</dd> </dl>

## Remarks

The **MSCluster\_ResourceGroupToPreferredNode** class is derived from the [**CIM\_Component**](https://msdn.microsoft.com/library/aa387218) class.

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

[**MSCluster\_Node**](mscluster-node.md)
</dt> <dt>

[**MSCluster\_ResourceGroup**](mscluster-resourcegroup.md)
</dt> </dl>

 

 





