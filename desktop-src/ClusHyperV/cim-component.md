---
title: CIM\_Component class
description: Represents a generic association between a parent managed element and a child managed element where the child represents a component or part of the parent.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2236911a-76ce-4dae-98a1-6bba987dbca2
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_Component class
- CIM_Component class, described
topic_type:
- apiref
api_name:
- CIM_Component
- CIM_Component.GroupComponent
- CIM_Component.PartComponent
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_Component class

Represents a generic association between a parent managed element and a child managed element where the child represents a component or part of the parent. For example, it could be used to define the components or parts of a system.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association, Abstract, Aggregation, Version("2.7.0"), UMLPackagePath("CIM::Core::CoreElements"), AMENDMENT]
class CIM_Component
{
  CIM_ManagedElement REF GroupComponent;
  CIM_ManagedElement REF PartComponent;
};
```

## Members

The **CIM\_Component** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_Component** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ManagedElement**](cim-managedelement.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Aggregate**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The parent element in the association.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ManagedElement**](cim-managedelement.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The child element in the association.

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

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





