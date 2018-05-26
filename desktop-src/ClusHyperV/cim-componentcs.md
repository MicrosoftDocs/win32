---
title: CIM\_ComponentCS class
description: Represents an association where a computer system contains and aggregates another computer system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 95d93fc5-6e90-4d37-9c3f-79c828d810a4
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
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
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_ComponentCS class

Represents an association where a computer system contains and aggregates another computer system. For example, if a CISC processor and its operating system are used for user interface and file support, and a RISC processor and its OS are used for complex mathematical operations, this could be modeled by implementing the **CIM\_ComponentCS** class.

In some cases, this association can be modeled as a cluster instead of using the **CIM\_ComponentCS** class. If the computer systems need to be treated as unique and distinct components, then you should use **CIM\_ComponentCS**, otherwise, you may model the association as a cluster.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Composition, Abstract, Version("2.13.0"), UMLPackagePath("CIM::System::SystemElements"), AMENDMENT]
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

Qualifiers: [**Aggregate**](https://msdn.microsoft.com/library/aa393650), [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent"), [**MAX**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The computer system that contains and aggregates other systems.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ComputerSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent")
</dt> </dl>

The contained computer system.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_SystemComponent**](cim-systemcomponent.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





