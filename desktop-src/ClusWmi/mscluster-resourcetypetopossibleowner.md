---
title: MSCluster\_ResourceTypeToPossibleOwner class
description: Lists nodes which are capable of hosting the particular resource type.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '740EFD12-8B2A-473A-9939-5EBEBFA96276'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSCluster_ResourceTypeToPossibleOwner class", "MSCluster_ResourceTypeToPossibleOwner class, described"]
topic_type:
- apiref
api_name:
- MSCluster_ResourceTypeToPossibleOwner
- MSCluster_ResourceTypeToPossibleOwner.GroupComponent
- MSCluster_ResourceTypeToPossibleOwner.PartComponent
api_location:
- ClusWMI.dll
api_type:
- DllExport
---

# MSCluster\_ResourceTypeToPossibleOwner class

Lists nodes which are capable of hosting the particular resource type.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{FFF86E19-2E61-4CBE-B49E-63B5B6164093}"), AMENDMENT]
class MSCluster_ResourceTypeToPossibleOwner : CIM_Component
{
  MSCluster_ResourceType REF GroupComponent;
  MSCluster_Node         REF PartComponent;
};
```

## Members

The **MSCluster\_ResourceTypeToPossibleOwner** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_ResourceTypeToPossibleOwner** class has these properties.

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

Data type: **[**MSCluster\_Node**](mscluster-node.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The possible owner node.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWMI.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Component**](cim-component.md)
</dt> <dt>

[Failover Cluster Provider Reference](server-cluster-provider-reference.md)
</dt> <dt>

[**MSCluster\_Node**](mscluster-node.md)
</dt> <dt>

[**MSCluster\_ResourceType**](mscluster-resourcetype.md)
</dt> </dl>

 

 





