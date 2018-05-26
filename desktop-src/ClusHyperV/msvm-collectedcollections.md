---
title: Msvm\_CollectedCollections class
description: Associates a Msvm\_VirtualSystemCollection object with contained Msvm\_ComputerSystem objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0f845687-eeab-49df-9a80-9da1681a9c32
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Msvm_CollectedCollections class
- Msvm_CollectedCollections class, described
topic_type:
- apiref
api_name:
- Msvm_CollectedCollections
- Msvm_CollectedCollections.Collection
- Msvm_CollectedCollections.Member
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Msvm\_CollectedCollections class

Associates a [**Msvm\_VirtualSystemCollection**](msvm-virtualsystemcollection.md) object with contained [**Msvm\_ComputerSystem**](msvm-computersystem.md) objects.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_CollectedCollections : CIM_CollectedMSEs
{
  Msvm_ManagementCollection REF Collection;
  CIM_CollectionOfMSEs      REF Member;
};
```

## Members

The **Msvm\_CollectedCollections** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_CollectedCollections** class has these properties.

<dl> <dt>

**Collection**
</dt> <dd> <dl> <dt>

Data type: **Msvm\_ManagementCollection**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Aggregate**](https://msdn.microsoft.com/library/aa393650), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Collection")
</dt> </dl>

The object that represents the virtual system collection.

</dd> <dt>

**Member**
</dt> <dd> <dl> <dt>

Data type: **CIM\_CollectionOfMSEs**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Member")
</dt> </dl>

The object that represents the members of the virtual system collection.

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

[**CIM\_CollectedMSEs**](cim-collectedmses.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





