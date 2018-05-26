---
title: CIM\_VirtualSystemSettingDataComponent class
description: Represents a portion of a relationship between a CIM\_VirtualSystemSettingData instance and a set of CIM\_ResourceAllocationSettingData instances.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 04f8da99-08cf-4d2e-beb2-df161fac4e03
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_VirtualSystemSettingDataComponent class
- CIM_VirtualSystemSettingDataComponent class, described
topic_type:
- apiref
api_name:
- CIM_VirtualSystemSettingDataComponent
- CIM_VirtualSystemSettingDataComponent.GroupComponent
- CIM_VirtualSystemSettingDataComponent.PartComponent
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_VirtualSystemSettingDataComponent class

Represents a portion of a relationship between a [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md) instance and a set of [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md) instances.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Abstract, Version("2.22.0"), UMLPackagePath("CIM::System::SystemElements")]
class CIM_VirtualSystemSettingDataComponent : CIM_Component
{
  CIM_VirtualSystemSettingData      REF GroupComponent;
  CIM_ResourceAllocationSettingData REF PartComponent;
};
```

## Members

The **CIM\_VirtualSystemSettingDataComponent** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_VirtualSystemSettingDataComponent** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_VirtualSystemSettingData**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Aggregate**](https://msdn.microsoft.com/library/aa393650), [**Override**](https://msdn.microsoft.com/library/aa393650) ("GroupComponent")
</dt> </dl>

A reference to the top-level [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md) object of the virtual system configuration.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ResourceAllocationSettingData**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("PartComponent")
</dt> </dl>

A reference the [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md) object that represents a part of the virtual system configuration.

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

[**CIM\_Component**](cim-component.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





