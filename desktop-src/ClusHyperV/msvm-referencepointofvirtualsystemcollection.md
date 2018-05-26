---
title: Msvm\_ReferencePointOfVirtualSystemCollection class
description: Associates a Msvm\_ReferencePointCollection instance with Msvm\_VirtualSystemCollection objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ae997e6a-5fdf-45cd-ad63-35d540fff05e
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Msvm_ReferencePointOfVirtualSystemCollection class
- Msvm_ReferencePointOfVirtualSystemCollection class, described
topic_type:
- apiref
api_name:
- Msvm_ReferencePointOfVirtualSystemCollection
- Msvm_ReferencePointOfVirtualSystemCollection.Antecedent
- Msvm_ReferencePointOfVirtualSystemCollection.Dependent
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Msvm\_ReferencePointOfVirtualSystemCollection class

Associates a [**Msvm\_ReferencePointCollection**](msvm-referencepointcollection.md) instance with [**Msvm\_VirtualSystemCollection**](msvm-virtualsystemcollection.md) objects.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_ReferencePointOfVirtualSystemCollection : CIM_Dependency
{
  CIM_CollectionOfMSEs REF Antecedent;
  CIM_Collection       REF Dependent;
};
```

## Members

The **Msvm\_ReferencePointOfVirtualSystemCollection** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ReferencePointOfVirtualSystemCollection** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_CollectionOfMSEs**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

The independent object in this association.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Collection**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The dependent object in this association.

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

[**CIM\_Dependency**](cim-dependency.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





