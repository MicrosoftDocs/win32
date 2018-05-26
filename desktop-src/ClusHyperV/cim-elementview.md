---
title: CIM\_ElementView class
description: Represents and association between a view, and an instance that represents the normalized view of a managed resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 937e182d-c616-41af-8342-daf0ed3be606
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_ElementView class
- CIM_ElementView class, described
topic_type:
- apiref
api_name:
- CIM_ElementView
- CIM_ElementView.Antecedent
- CIM_ElementView.Dependent
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_ElementView class

Represents and association between a view, and an instance that represents the normalized view of a managed resource.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Association, Experimental, Version("2.21.1"), UMLPackagePath("CIM::Core::CoreElements")]
class CIM_ElementView : CIM_Dependency
{
  CIM_ManagedElement REF Antecedent;
  CIM_View           REF Dependent;
};
```

## Members

The **CIM\_ElementView** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ElementView** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ManagedElement**](cim-managedelement.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

The instance that represents the normalized view of the managed resource.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_View**](cim-view.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The view that represents a de-normalized or aggregate view of the managed resource.

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

 

 





