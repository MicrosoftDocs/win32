---
title: Msvm\_SharedDiskSetReplicationRelationshipOfVirtualSystemCollection class
description: Associates the Msvm\_SharedDiskSetReplicationRelationship to the corresponding Msvm\_VirtualSystemCollection objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 10434f28-5b12-4960-b5c2-9435b6d62afd
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Msvm_SharedDiskSetReplicationRelationshipOfVirtualSystemCollection class
- Msvm_SharedDiskSetReplicationRelationshipOfVirtualSystemCollection class, described
topic_type:
- apiref
api_name:
- Msvm_SharedDiskSetReplicationRelationshipOfVirtualSystemCollection
- Msvm_SharedDiskSetReplicationRelationshipOfVirtualSystemCollection.Antecedent
- Msvm_SharedDiskSetReplicationRelationshipOfVirtualSystemCollection.Dependent
api_location:
- VMMS.exe
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Msvm\_SharedDiskSetReplicationRelationshipOfVirtualSystemCollection class

Associates the [**Msvm\_SharedDiskSetReplicationRelationship**](msvm-shareddisksetreplicationrelationship.md) to the corresponding [**Msvm\_VirtualSystemCollection**](msvm-virtualsystemcollection.md) objects.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_SharedDiskSetReplicationRelationshipOfVirtualSystemCollection : CIM_Dependency
{
  Msvm_VirtualSystemCollection              REF Antecedent;
  Msvm_SharedDiskSetReplicationRelationship REF Dependent;
};
```

## Members

The **Msvm\_SharedDiskSetReplicationRelationshipOfVirtualSystemCollection** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_SharedDiskSetReplicationRelationshipOfVirtualSystemCollection** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **Msvm\_VirtualSystemCollection**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

A [**Msvm\_VirtualSystemCollection**](msvm-virtualsystemcollection.md) that contains the instance of the associated virtual system collection.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **Msvm\_SharedDiskSetReplicationRelationship**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

A [**Msvm\_SharedDiskSetReplicationRelationship**](msvm-shareddisksetreplicationrelationship.md) that contains an instance of the dependent shared disk replica relationship.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

 





