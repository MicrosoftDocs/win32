---
title: Msvm\_ComponentCS class
description: Represents an aggregation relationship between an instance of Msvm\_ComputerSystem, and an instance of Msvm\_ComputerSystem.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '91a7b126-14a9-4a51-a1d4-7303028abb5b'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Msvm_ComponentCS class", "Msvm_ComponentCS class, described"]
topic_type:
- apiref
api_name:
- Msvm_ComponentCS
- Msvm_ComponentCS.GroupComponent
- Msvm_ComponentCS.PartComponent
api_location:
- VMMS.exe
api_type:
- DllExport
---

# Msvm\_ComponentCS class

Represents an aggregation relationship between an instance of [**Msvm\_ComputerSystem**](msvm-computersystem.md), and an instance of **Msvm\_ComputerSystem**.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_ComponentCS : CIM_ComponentCS
{
  Msvm_ComputerSystem REF GroupComponent;
  Msvm_ComputerSystem REF PartComponent;
};
```

## Members

The **Msvm\_ComponentCS** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ComponentCS** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **Msvm\_ComputerSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent")
</dt> </dl>

The computer system that aggregates other computer systems.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **Msvm\_ComputerSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent")
</dt> </dl>

The aggregated computer system in the relationship.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_ComponentCS**](cim-componentcs.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





