---
title: MSCluster\_ResourceToPossibleOwner class
description: A dynamic association WMI class that represents a list of the resources and their possible owner nodes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'fae95ee7-f603-4424-a0e1-804be811c46b'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSCluster_ResourceToPossibleOwner class", "MSCluster_ResourceToPossibleOwner class, described"]
topic_type:
- apiref
api_name:
- MSCluster_ResourceToPossibleOwner
- MSCluster_ResourceToPossibleOwner.GroupComponent
- MSCluster_ResourceToPossibleOwner.PartComponent
api_location:
- ClusWMI.dll
api_type:
- DllExport
---

# MSCluster\_ResourceToPossibleOwner class

A dynamic association [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a list of the resources and their possible owner nodes.

## Syntax

``` syntax
[Association, Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{f57d5a56-c22a-45c5-a335-c790ee0b7122}"), AMENDMENT]
class MSCluster_ResourceToPossibleOwner : CIM_Component
{
  MSCluster_Resource REF GroupComponent;
  MSCluster_Node     REF PartComponent;
};
```

## Members

The **MSCluster\_ResourceToPossibleOwner** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_ResourceToPossibleOwner** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **[**MSCluster\_Resource**](mscluster-resource.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The resource.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **[**MSCluster\_Node**](mscluster-node.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent")
</dt> </dl>

The possible owner of this resource.

</dd> </dl>

## Remarks

The **MSCluster\_ResourceToPossibleOwner** class is derived from the [**CIM\_Component**](https://msdn.microsoft.com/library/aa387218) class.

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

[**MSCluster\_Resource**](mscluster-resource.md)
</dt> <dt>

[**MSCluster\_Node**](mscluster-node.md)
</dt> </dl>

 

 





