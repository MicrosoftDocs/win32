---
title: MSCluster\_NodeToActiveGroup class
description: A dynamic association WMI class that represents the groups active on a node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d8ebfbce-a698-4039-a13c-e042a0be1195
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSCluster_NodeToActiveGroup class
- MSCluster_NodeToActiveGroup class, described
topic_type:
- apiref
api_name:
- MSCluster_NodeToActiveGroup
- MSCluster_NodeToActiveGroup.GroupComponent
- MSCluster_NodeToActiveGroup.PartComponent
api_location:
- ClusWMI.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSCluster\_NodeToActiveGroup class

A dynamic association [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents the [groups](https://msdn.microsoft.com/library/aa369645) active on a [node](https://msdn.microsoft.com/library/aa371745).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{AE76778B-B9C4-4765-9E61-7A3DC17F919C}"), AMENDMENT]
class MSCluster_NodeToActiveGroup : CIM_Component
{
  MSCluster_Node          REF GroupComponent;
  MSCluster_ResourceGroup REF PartComponent;
};
```

## Members

The **MSCluster\_NodeToActiveGroup** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_NodeToActiveGroup** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **MSCluster\_Node**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The node.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **MSCluster\_ResourceGroup**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent")
</dt> </dl>

The group that is active on the node.

</dd> </dl>

## Remarks

The **MSCluster\_NodeToActiveGroup** class is derived from the [**CIM\_Component**](https://msdn.microsoft.com/library/aa387218) class.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



 

 





