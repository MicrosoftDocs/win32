---
title: Msvm\_CollectedSnapshots class
description: Associates an Msvm\_SnapshotCollection object with contained Msvm\_VirtualSystemSettingData objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6072c271-33e9-400e-bba9-a0830c7e3ecb
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Msvm_CollectedSnapshots class
- Msvm_CollectedSnapshots class, described
topic_type:
- apiref
api_name:
- Msvm_CollectedSnapshots
- Msvm_CollectedSnapshots.Collection
- Msvm_CollectedSnapshots.Member
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Msvm\_CollectedSnapshots class

Associates an [**Msvm\_SnapshotCollection**](msvm-snapshotcollection.md) object with contained [**Msvm\_VirtualSystemSettingData**](msvm-virtualsystemsettingdata.md) objects.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_CollectedSnapshots : CIM_CollectedMSEs
{
  Msvm_SnapshotCollection       REF Collection;
  Msvm_VirtualSystemSettingData REF Member;
};
```

## Members

The **Msvm\_CollectedSnapshots** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_CollectedSnapshots** class has these properties.

<dl> <dt>

**Collection**
</dt> <dd> <dl> <dt>

Data type: **Msvm\_SnapshotCollection**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Aggregate**](https://msdn.microsoft.com/library/aa393650), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Collection")
</dt> </dl>

A reference to the object that represents the collection.

</dd> <dt>

**Member**
</dt> <dd> <dl> <dt>

Data type: **Msvm\_VirtualSystemSettingData**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Member")
</dt> </dl>

A reference to the object that represents the members of the collection.

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

 

 





