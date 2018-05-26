---
title: CIM\_ParticipatingCS class
description: A CIM\_Cluster is composed of two or more computer systems, operating together. A computer system may participate in multiple clusters.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3aeb317f-b137-472c-ad6a-c791561c3114
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_ParticipatingCS class
- CIM_ParticipatingCS class, described
topic_type:
- apiref
api_name:
- CIM_ParticipatingCS
- CIM_ParticipatingCS.Antecedent
- CIM_ParticipatingCS.Dependent
- CIM_ParticipatingCS.StateOfNode
- CIM_ParticipatingCS.RoleOfNode
api_location:
- WlbsProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_ParticipatingCS class

A [**CIM\_Cluster**](cim-cluster.md) is composed of two or more computer system's, operating together. A computer system may participate in multiple clusters.

When first establishing or bringing up a cluster, only one computer system may be defined as participating in it. Therefore, the cardinality of the association for the CIM\_ComputerSystem reference is Min(1).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, AMENDMENT]
class CIM_ParticipatingCS : CIM_Dependency
{
  CIM_ComputerSystem REF Antecedent;
  CIM_Cluster        REF Dependent;
  uint16                 StateOfNode;
  uint16                 RoleOfNode;
};
```

## Members

The **CIM\_ParticipatingCS** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ParticipatingCS** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ComputerSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The ComputerSystem which participates in the Cluster.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Cluster**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The cluster

</dd> <dt>

**RoleOfNode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

RoleOfNode indicates whether the cluster nodes are peers (value = 3), connected in a master-subordinate/primary-secondary relationship (values = 4 for primary, 5 for secondary), available in a standby configuration (6) or of some other (1) or unknown (2) relationship.

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


</dt> <dd></dd> </dl>

</dd> <dt>

**StateOfNode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

StateOfNode indicates the condition of the participating computer system in the cluster. For example, one value is "Joining" (2).

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

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

 





