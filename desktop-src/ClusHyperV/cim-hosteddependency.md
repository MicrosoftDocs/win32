---
title: CIM\_HostedDependency class
description: Represents an association where a managed element is hosted by another.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1f704dbf-dd86-4781-8681-23242312e3b2
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_HostedDependency class
- CIM_HostedDependency class, described
topic_type:
- apiref
api_name:
- CIM_HostedDependency
- CIM_HostedDependency.Antecedent
- CIM_HostedDependency.Dependent
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_HostedDependency class

Represents an association where a managed element is hosted by another.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association, Abstract, Version("2.8.0"), UMLPackagePath("CIM::Core::CoreElements"), AMENDMENT]
class CIM_HostedDependency : CIM_Dependency
{
  CIM_ManagedElement REF Antecedent;
  CIM_ManagedElement REF Dependent;
};
```

## Members

The **CIM\_HostedDependency** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_HostedDependency** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ManagedElement**](cim-managedelement.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent"), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The host managed element.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ManagedElement**](cim-managedelement.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The hosted managed element.

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

 

 





