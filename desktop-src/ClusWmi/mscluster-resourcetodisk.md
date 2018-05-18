---
title: MSCluster\_ResourceToDisk class
description: A dynamic WMI class that associates an instance of the MSCluster\_Resource class representing a disk resource to an instance of the MSCluster\_Disk class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'eed143d2-7704-4acb-94e2-ab072288d05e'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSCluster_ResourceToDisk class", "MSCluster_ResourceToDisk class, described"]
topic_type:
- apiref
api_name:
- MSCluster_ResourceToDisk
- MSCluster_ResourceToDisk.GroupComponent
- MSCluster_ResourceToDisk.PartComponent
api_location:
- ClusWMI.dll
api_type:
- DllExport
---

# MSCluster\_ResourceToDisk class

A dynamic [*WMI class*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-22-gly) that associates an instance of the [**MSCluster\_Resource**](mscluster-resource.md) class representing a disk resource to an instance of the [**MSCluster\_Disk**](mscluster-disk.md) class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{7B81696D-C2AC-481A-BFD0-A2FB02238926}"), AMENDMENT]
class MSCluster_ResourceToDisk : CIM_Component
{
  MSCluster_Resource REF GroupComponent;
  MSCluster_Disk     REF PartComponent;
};
```

## Members

The **MSCluster\_ResourceToDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSCluster\_ResourceToDisk** class has these properties.

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

Data type: **[**MSCluster\_Disk**](mscluster-disk.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent")
</dt> </dl>

Represents the disk associated with this physical disk resource.

</dd> </dl>

## Remarks

The **MSCluster\_ResourceToDisk** class is derived from the [**CIM\_Component**](https://msdn.microsoft.com/library/aa387218) class.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Component**](cim-component.md)
</dt> <dt>

[Failover Cluster Provider Reference](server-cluster-provider-reference.md)
</dt> <dt>

[**MSCluster\_Disk**](mscluster-disk.md)
</dt> <dt>

[**MSCluster\_Resource**](mscluster-resource.md)
</dt> </dl>

 

 





