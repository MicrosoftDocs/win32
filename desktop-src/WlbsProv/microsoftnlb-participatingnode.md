---
title: MicrosoftNLB\_ParticipatingNode class
description: The MicrosoftNLB\_ParticipatingNode association WMI class associates an instance of the MicrosoftNLB\_Cluster class with participating MicrosoftNLB\_Node class instances.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '783554ab-c251-49e9-9b64-38bb072eb7ce'
ms.prod: 'windows-server-dev'
ms.technology:
- 'network-load-balancing'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MicrosoftNLB_ParticipatingNode class", "MicrosoftNLB_ParticipatingNode class, described"]
topic_type:
- apiref
api_name:
- MicrosoftNLB_ParticipatingNode
- MicrosoftNLB_ParticipatingNode.StateOfNode
- MicrosoftNLB_ParticipatingNode.RoleOfNode
- MicrosoftNLB_ParticipatingNode.Dependent
- MicrosoftNLB_ParticipatingNode.Antecedent
api_location:
- WlbsProv.dll
api_type:
- DllExport
---

# MicrosoftNLB\_ParticipatingNode class

The **MicrosoftNLB\_ParticipatingNode** association [*WMI class*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-22-gly) associates an instance of the **MicrosoftNLB\_Cluster** class with participating [**MicrosoftNLB\_Node**](microsoftnlb-node.md) class instances.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("Microsoft|NLB_Provider|V1.0"), AMENDMENT]
class MicrosoftNLB_ParticipatingNode : CIM_ParticipatingCS
{
  uint16                   StateOfNode;
  uint16                   RoleOfNode;
  MicrosoftNLB_Cluster REF Dependent;
  MicrosoftNLB_Node    REF Antecedent;
};
```

## Members

The **MicrosoftNLB\_ParticipatingNode** class has these types of members:

-   [Properties](#properties)

### Properties

The **MicrosoftNLB\_ParticipatingNode** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **MicrosoftNLB\_Node**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

A [**MicrosoftNLB\_Node**](microsoftnlb-node.md) that represents the computer system which participates in the cluster.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **MicrosoftNLB\_Cluster**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

A **MicrosoftNLB\_Cluster** that represents the cluster.

</dd> <dt>

**RoleOfNode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Not used.

This property inherits from [**CIM\_ParticipatingCS**](cim-participatingcs.md).

</dd> <dt>

**StateOfNode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Not used.

This property inherits from [**CIM\_ParticipatingCS**](cim-participatingcs.md).

</dd> </dl>

## Remarks

Enumerating instances of the **MicrosoftNLB\_ParticipatingNode** class will have the same results as enumerating instances of [**MicrosoftNLB\_Node**](microsoftnlb-node.md). For more information see [enumerating nodes](enumerating-nodes.md).

An attempt to obtain a **MicrosoftNLB\_Cluster** instance using the **Dependent** property will fail.

The **MicrosoftNLB\_ParticipatingNode** class is derived from the **CIM\_ParticipatingCS** class.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ParticipatingCS**](cim-participatingcs.md)
</dt> <dt>

[**MicrosoftNLB\_Node**](microsoftnlb-node.md)
</dt> </dl>

 

 





