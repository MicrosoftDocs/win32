---
title: CIM\_ComponentCS class
description: A ComputerSystem can aggregate another ComputerSystem.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8237ccfe-fdcb-48f2-be29-bbda6f607f81
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_ComponentCS class
- CIM_ComponentCS class, described
topic_type:
- apiref
api_name:
- CIM_ComponentCS
- CIM_ComponentCS.GroupComponent
- CIM_ComponentCS.PartComponent
api_location:
- ClusWMI.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CIM\_ComponentCS class

A ComputerSystem can aggregate another ComputerSystem. This association can be used to model MPP Systems with workstation frontends, an I2O subsystem embedded in a UnitaryComputerSystem, or a System that splits functionality between two processors, potentially running different OperatingSystems.

For example, if a CISC Processor and its associated OperatingSystem, are used for user interface and file support, and a RISC Processor and its OS are used for complex mathematical operations, this could be modeled as two ComputerSystems where one aggregates the other. In some cases, this could be modeled as a Cluster. The difference is the focus of the relationship. ComponentCS represents that unique and distinct ComputerSystems are aggregated by a higher level CS object. However, each of the component CSs are still distinguishable entities and are only viewed as such. Alternately, with a Cluster, the ComputerSystems that participate in it are inconsequential, when viewed through the 'Cluster System'.

When instantiating or subclassing the ComponentCS relationship, care should be taken that the component ComputerSystem meets the definitional requirements of a ComputerSystem - ie, a functional whole that provides compute capabilities and aggregates System Devices, an OperatingSystem, etc.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, UUID("{AB653DD2-EA29-4dcc-9F10-8C809A50A646}"), AMENDMENT]
class CIM_ComponentCS : CIM_SystemComponent
{
  CIM_ComputerSystem REF GroupComponent;
  CIM_ComputerSystem REF PartComponent;
};
```

## Members

The **CIM\_ComponentCS** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ComponentCS** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ComputerSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent"), [**Aggregate**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The ComputerSystem that contains and/or aggregates other Systems.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ComputerSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent")
</dt> </dl>

The contained (Sub)ComputerSystem.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWMI.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_SystemComponent**](cim-systemcomponent.md)
</dt> </dl>

 

 





