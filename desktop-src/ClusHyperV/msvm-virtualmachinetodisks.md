---
title: Msvm\_VirtualMachineToDisks class
description: Setting data to be passed as an array to the Msvm\_CollectionReferencePointExportSettingData class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 917e6164-d631-43f7-b096-dc858f4ef516
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Msvm_VirtualMachineToDisks class
- Msvm_VirtualMachineToDisks class, described
topic_type:
- apiref
api_name:
- Msvm_VirtualMachineToDisks
- Msvm_VirtualMachineToDisks.VirtualMachineId
- Msvm_VirtualMachineToDisks.DisksToExport
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Msvm\_VirtualMachineToDisks class

Setting data to be passed as an array to the [**Msvm\_CollectionReferencePointExportSettingData**](msvm-collectionreferencepointexportsettingdata.md) class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_VirtualMachineToDisks
{
  string VirtualMachineId;
  string DisksToExport[];
};
```

## Members

The **Msvm\_VirtualMachineToDisks** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_VirtualMachineToDisks** class has these properties.

<dl> <dt>

**DisksToExport**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

WMI instance IDs of the disks those belong to given Virtual Machine ID for which data needs to be exported.

</dd> <dt>

**VirtualMachineId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Virtual Machine ID for which virtual disks are associated with.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



 

 





