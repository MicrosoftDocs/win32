---
title: MSCluster\_NodeToActiveResource class
description: A dynamic association WMI class that represents the resources active on a node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 79e1aedd-158d-478e-9abb-73c807b9dfb2
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSCluster_NodeToActiveResource class
- MSCluster_NodeToActiveResource class, described
topic_type:
- apiref
api_name:
- MSCluster_NodeToActiveResource
- MSCluster_NodeToActiveResource.GroupComponent
- MSCluster_NodeToActiveResource.PartComponent
api_location:
- ClusWMI.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSCluster\_NodeToActiveResource class

A dynamic association [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents the [resources](https://msdn.microsoft.com/library/aa372152) active on a [node](https://msdn.microsoft.com/library/aa371745).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{4D440386-1CC3-4dca-AFB2-DB74A60A3891}"), AMENDMENT]
class MSCluster_NodeToActiveResource : CIM_Component
{
  MSCluster_Node     REF GroupComponent;
  MSCluster_Resource REF PartComponent;
};
```

## Members

The **MSCluster\_NodeToActiveResource** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_NodeToActiveResource** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **MSCluster\_Node**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The node.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **MSCluster\_Resource**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent")
</dt> </dl>

The resource that is active on the node.

</dd> </dl>

## Remarks

The **MSCluster\_NodeToActiveResource** class is derived from the [**CIM\_Component**](https://msdn.microsoft.com/library/aa387218) class.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



 

 





