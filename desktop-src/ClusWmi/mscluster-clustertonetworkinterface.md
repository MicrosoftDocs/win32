---
title: MSCluster\_ClusterToNetworkInterface class
description: A dynamic association WMI class that represents the network interfaces the cluster has installed on the nodes it manages.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fd4cf967-3734-43c6-b199-4f78a069d2f7
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSCluster_ClusterToNetworkInterface class
- MSCluster_ClusterToNetworkInterface class, described
topic_type:
- apiref
api_name:
- MSCluster_ClusterToNetworkInterface
- MSCluster_ClusterToNetworkInterface.GroupComponent
- MSCluster_ClusterToNetworkInterface.PartComponent
api_location:
- ClusWMI.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSCluster\_ClusterToNetworkInterface class

A dynamic association [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents the network interfaces the cluster has installed on the nodes it manages.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{CB737284-A6D8-4d46-92F0-20992869A84E}"), AMENDMENT]
class MSCluster_ClusterToNetworkInterface : CIM_Component
{
  MSCluster_Cluster          REF GroupComponent;
  MSCluster_NetworkInterface REF PartComponent;
};
```

## Members

The **MSCluster\_ClusterToNetworkInterface** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_ClusterToNetworkInterface** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **[**MSCluster\_Cluster**](mscluster-cluster.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The cluster.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **[**MSCluster\_NetworkInterface**](mscluster-networkinterface.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent")
</dt> </dl>

The network interfaces.

</dd> </dl>

## Remarks

The **MSCluster\_ClusterToNetworkInterface** class is derived from the [**CIM\_Component**](https://msdn.microsoft.com/library/aa387218) class.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Component**](cim-component.md)
</dt> <dt>

[Failover Cluster Provider Reference](server-cluster-provider-reference.md)
</dt> <dt>

[**MSCluster\_Cluster**](mscluster-cluster.md)
</dt> <dt>

[**MSCluster\_NetworkInterface**](mscluster-networkinterface.md)
</dt> </dl>

 

 





