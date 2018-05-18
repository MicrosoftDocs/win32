---
title: GetSystemCompatibilityInfo method of the Msvm\_VirtualSystemMigrationService class
description: Generates an opaque BLOB of data that contains compatibility information for the specified system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e307f95d-ccc4-4103-bce7-a7eba50a5765'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetSystemCompatibilityInfo method", "GetSystemCompatibilityInfo method, Msvm_VirtualSystemMigrationService class", "Msvm_VirtualSystemMigrationService class, GetSystemCompatibilityInfo method"]
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemMigrationService.GetSystemCompatibilityInfo
api_location:
- VMMS.exe
api_type:
- COM
---

# GetSystemCompatibilityInfo method of the Msvm\_VirtualSystemMigrationService class

Generates an opaque BLOB of data that contains compatibility information for the specified system.

## Syntax


```mof
uint32 GetSystemCompatibilityInfo(
  [in]  CIM_ComputerSystem REF ComputerSystem,
  [out] uint8                  CompatibilityInfo[]
);
```



## Parameters

<dl> <dt>

*ComputerSystem* \[in\]
</dt> <dd>

A reference to a [**CIM\_ComputerSystem**](cim-computersystem.md) class that represents the VM to retrieve compatibility information. If the ComputerSystem parameter refers to the hosting computer system, the data returned in the CompatibilityInfo parameter can be used to determine whether any of the VMs on the hosting computer system can be quickly migrated to another hosting computer system.

</dd> <dt>

*CompatibilityInfo* \[out\]
</dt> <dd>

An opaque blob of data that can be passed to the [**CheckSystemCompatibilityInfo**](msvm-virtualsystemmigrationservice-checksystemcompatibilityinfo.md) method on another hosting computer system to confirm compatibility.

</dd> </dl>

## Return value

This method returns one of the following values.

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Failed** (32768)
</dt> <dt>

**Access Denied** (32769)
</dt> <dt>

**Not Supported** (32770)
</dt> <dt>

**Status is unknown** (32771)
</dt> <dt>

**Timeout** (32772)
</dt> <dt>

**Invalid parameter** (32773)
</dt> <dt>

**System is in use** (32774)
</dt> <dt>

**Invalid state for this operation** (32775)
</dt> <dt>

**Incorrect data type** (32776)
</dt> <dt>

**System is not available** (32777)
</dt> <dt>

**Out of memory** (32778)
</dt> </dl>

## Remarks

The **GetSystemCompatibilityInfo** method is used in conjunction with [**CheckSystemCompatibilityInfo**](msvm-virtualsystemmigrationservice-checksystemcompatibilityinfo.md) to determine whether a quick or live migration of a VM to another hosting computer system is possible without first trying the migration. The compatibility information is dependent on the current **EnabledState** property of the system specified in the *ComputerSystem* parameter. In addition, the compatibility information for a VM may change when a snapshot is applied or the system is restarted. A VM in the Disabled state (**EnabledState** property value of 3) is compatible with more systems than one in the Suspended or Enabled states (**EnabledState** property value of 32769 or 2.)

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

[**Msvm\_VirtualSystemMigrationService**](msvm-virtualsystemmigrationservice.md)
</dt> </dl>

 

 





