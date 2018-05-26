---
title: MSCluster\_ClusterToNetwork class
description: A dynamic association WMI class that represents the networks the cluster uses for communication.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3be2c36b-cd10-43ae-aba3-951d1229f36a
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSCluster_ClusterToNetwork class
- MSCluster_ClusterToNetwork class, described
topic_type:
- apiref
api_name:
- MSCluster_ClusterToNetwork
- MSCluster_ClusterToNetwork.GroupComponent
- MSCluster_ClusterToNetwork.PartComponent
api_location:
- ClusWMI.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSCluster\_ClusterToNetwork class

A dynamic association [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents the networks the cluster uses for communication.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{F3CAB1DD-2F7D-484b-AD54-54187C0A8351}"), AMENDMENT]
class MSCluster_ClusterToNetwork : CIM_Component
{
  MSCluster_Cluster REF GroupComponent;
  MSCluster_Network REF PartComponent;
};
```

## Members

The **MSCluster\_ClusterToNetwork** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_ClusterToNetwork** class has these properties.

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

Data type: **[**MSCluster\_Network**](mscluster-network.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent")
</dt> </dl>

The network used cluster for communication.

</dd> </dl>

## Remarks

The **MSCluster\_ClusterToNetwork** class is derived from the [**CIM\_Component**](https://msdn.microsoft.com/library/aa387218) class.

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

[**MSCluster\_Network**](mscluster-network.md)
</dt> </dl>

 

 





