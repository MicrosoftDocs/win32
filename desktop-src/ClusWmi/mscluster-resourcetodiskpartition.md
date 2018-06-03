---
title: MSCluster\_ResourceToDiskPartition class
description: A dynamic WMI class that associates an instance of the MSCluster\_Resource class representing a disk resource to an instance of the MSCluster\_DiskPartition class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4638300A-AC1A-4704-AC36-FBCFFF19A228
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSCluster_ResourceToDiskPartition class
- MSCluster_ResourceToDiskPartition class, described
topic_type:
- apiref
api_name:
- MSCluster_ResourceToDiskPartition
- MSCluster_ResourceToDiskPartition.GroupComponent
- MSCluster_ResourceToDiskPartition.PartComponent
api_location:
- ClusWMI.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSCluster\_ResourceToDiskPartition class

A dynamic [*WMI class*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-22-gly) that associates an instance of the [**MSCluster\_Resource**](mscluster-resource.md) class representing a disk resource to an instance of the [**MSCluster\_DiskPartition**](mscluster-diskpartition.md) class.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{DA5E549F-565A-4503-80CA-C2C3237E6D96}"), AMENDMENT]
class MSCluster_ResourceToDiskPartition : CIM_Component
{
  MSCluster_Resource      REF GroupComponent;
  MSCluster_DiskPartition REF PartComponent;
};
```

## Members

The **MSCluster\_ResourceToDiskPartition** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_ResourceToDiskPartition** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **[**MSCluster\_Resource**](mscluster-resource.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

Represents the physical disk resource.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **[**MSCluster\_DiskPartition**](mscluster-diskpartition.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent")
</dt> </dl>

Represents the disk partition associated with this physical disk resource.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Component**](cim-component.md)
</dt> <dt>

[Failover Cluster Provider Reference](server-cluster-provider-reference.md)
</dt> <dt>

[**MSCluster\_DiskPartition**](mscluster-diskpartition.md)
</dt> <dt>

[**MSCluster\_Resource**](mscluster-resource.md)
</dt> </dl>

 

 





