---
title: CIM\_SnapshotOfVirtualSystem class
description: Associates a virtual system a snapshot of the virtual system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '8575bc7e-0c33-4add-b3eb-d8bfdb7ee6ee'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_SnapshotOfVirtualSystem class", "CIM_SnapshotOfVirtualSystem class, described"]
topic_type:
- apiref
api_name:
- CIM_SnapshotOfVirtualSystem
- CIM_SnapshotOfVirtualSystem.Antecedent
- CIM_SnapshotOfVirtualSystem.Dependent
api_location:
- VMMS.exe
api_type:
- DllExport
---

# CIM\_SnapshotOfVirtualSystem class

Associates a virtual system a snapshot of the virtual system.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association, Abstract, Version("2.22.0"), AMENDMENT]
class CIM_SnapshotOfVirtualSystem : CIM_Dependency
{
  CIM_ComputerSystem           REF Antecedent;
  CIM_VirtualSystemSettingData REF Dependent;
};
```

## Members

The **CIM\_SnapshotOfVirtualSystem** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_SnapshotOfVirtualSystem** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ComputerSystem**](cim-computersystem.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent"), [**Min**](https://msdn.microsoft.com/library/aa393650) (0), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

A reference to the computer system that represents the virtual system.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

A reference to the settings data object that represents the snapshot of the virtual system.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





