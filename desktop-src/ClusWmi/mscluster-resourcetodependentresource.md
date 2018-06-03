---
title: MSCluster\_ResourceToDependentResource class
description: A dynamic association WMI class that represents the dependencies of a resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: dfd50a0b-0df4-41f2-8abf-9a6673e97e78
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSCluster_ResourceToDependentResource class
- MSCluster_ResourceToDependentResource class, described
topic_type:
- apiref
api_name:
- MSCluster_ResourceToDependentResource
- MSCluster_ResourceToDependentResource.Antecedent
- MSCluster_ResourceToDependentResource.Dependent
api_location:
- ClusWMI.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSCluster\_ResourceToDependentResource class

A dynamic association [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents the dependencies of a resource.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{C09C3AB9-E97C-46d8-921F-4B3EA2A7C457}"), AMENDMENT]
class MSCluster_ResourceToDependentResource : CIM_Dependency
{
  MSCluster_Resource REF Antecedent;
  MSCluster_Resource REF Dependent;
};
```

## Members

The **MSCluster\_ResourceToDependentResource** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_ResourceToDependentResource** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **[**MSCluster\_Resource**](mscluster-resource.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

The resource.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**MSCluster\_Resource**](mscluster-resource.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The resource to be depended on.

</dd> </dl>

## Remarks

The **MSCluster\_ResourceToDependentResource** class is derived from the [**CIM\_Dependency**](https://msdn.microsoft.com/library/aa387238) class.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> <dt>

[Failover Cluster Provider Reference](server-cluster-provider-reference.md)
</dt> <dt>

[**MSCluster\_Resource**](mscluster-resource.md)
</dt> </dl>

 

 





