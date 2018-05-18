---
title: MSCluster\_ClusterToNode class
description: A dynamic association WMI class that provides access to the nodes in a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'fb764dc7-ea9c-49d2-99a6-54b1055136a3'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSCluster_ClusterToNode class", "MSCluster_ClusterToNode class, described"]
topic_type:
- apiref
api_name:
- MSCluster_ClusterToNode
- MSCluster_ClusterToNode.StateOfNode
- MSCluster_ClusterToNode.RoleOfNode
- MSCluster_ClusterToNode.Antecedent
- MSCluster_ClusterToNode.Dependent
api_location:
- ClusWMI.dll
api_type:
- DllExport
---

# MSCluster\_ClusterToNode class

A dynamic association [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that provides access to the nodes in a cluster.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{1DA51F43-8562-4093-9C3A-D9CBB35CF6D2}"), AMENDMENT]
class MSCluster_ClusterToNode : CIM_ParticipatingCS
{
  uint16                StateOfNode;
  uint16                RoleOfNode;
  MSCluster_Cluster REF Antecedent;
  MSCluster_Node    REF Dependent;
};
```

## Members

The **MSCluster\_ClusterToNode** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_ClusterToNode** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **[**MSCluster\_Cluster**](mscluster-cluster.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The cluster.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**MSCluster\_Node**](mscluster-node.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

Node managed by the cluster.

</dd> <dt>

**RoleOfNode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

RoleOfNode indicates whether the Cluster nodes are peers (value = 2), connected in a master-slave/primary-secondary relationship (values = 3 for primary, 4 for secondary), available in a standby configuration (5) or of some other (1) or unknown (0) relationship. In a System/390 environment, the nodes are identified as "Base Plex" (value=6) or "Enhanced Plex" (value=7).

This property is inherited from [**CIM\_ParticipatingCS**](cim-participatingcs.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Peer"></span><span id="peer"></span><span id="PEER"></span>

**Peer** (2)


</dt> <dd></dd> <dt>

<span id="Primary"></span><span id="primary"></span><span id="PRIMARY"></span>

**Primary** (3)


</dt> <dd></dd> <dt>

<span id="Secondary"></span><span id="secondary"></span><span id="SECONDARY"></span>

**Secondary** (4)


</dt> <dd></dd> <dt>

<span id="Standby"></span><span id="standby"></span><span id="STANDBY"></span>

**Standby** (5)


</dt> <dd></dd> <dt>

<span id="Base_Plex"></span><span id="base_plex"></span><span id="BASE_PLEX"></span>

**Base Plex** (6)


</dt> <dd></dd> <dt>

<span id="Enhanced_Plex"></span><span id="enhanced_plex"></span><span id="ENHANCED_PLEX"></span>

**Enhanced Plex** (7)


</dt> <dd></dd> </dl>

</dd> <dt>

**StateOfNode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

StateOfNode indicates the condition of the participating ComputerSystem in the Cluster. For example, one value is "Joining" (2).

This property is inherited from [**CIM\_ParticipatingCS**](cim-participatingcs.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Joining"></span><span id="joining"></span><span id="JOINING"></span>

**Joining** (2)


</dt> <dd></dd> <dt>

<span id="Paused"></span><span id="paused"></span><span id="PAUSED"></span>

**Paused** (3)


</dt> <dd></dd> <dt>

<span id="Available"></span><span id="available"></span><span id="AVAILABLE"></span>

**Available** (4)


</dt> <dd></dd> <dt>

<span id="Unavailable"></span><span id="unavailable"></span><span id="UNAVAILABLE"></span>

**Unavailable** (5)


</dt> <dd></dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

**Degraded** (6)


</dt> <dd></dd> </dl>

</dd> </dl>

## Remarks

The **MSCluster\_ClusterToNode** class is derived from the **CIM\_ParticipatingCS** class.

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

[**CIM\_ParticipatingCS**](cim-participatingcs.md)
</dt> <dt>

[Failover Cluster Provider Reference](server-cluster-provider-reference.md)
</dt> <dt>

[**MSCluster\_Cluster**](mscluster-cluster.md)
</dt> <dt>

[**MSCluster\_Node**](mscluster-node.md)
</dt> </dl>

 

 





