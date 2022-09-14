---
description: Removes migration network subnets from the virtual system migration service.
ms.assetid: 6ae8de07-552b-4525-8806-bfb9da73bd42
title: RemoveNetworkSettings method of the Msvm_VirtualSystemMigrationService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_VirtualSystemMigrationService.RemoveNetworkSettings
api_type: 
- COM
api_location: 
- vmms.exe
---

# RemoveNetworkSettings method of the Msvm\_VirtualSystemMigrationService class

Removes migration network subnets from the virtual system migration service.

## Syntax


```mof
uint32 RemoveNetworkSettings(
  [in]  Msvm_VirtualSystemMigrationNetworkSettingData REF NetworkSettings[],
  [out] CIM_ConcreteJob                               REF Job
);
```



## Parameters

<dl> <dt>

*NetworkSettings* \[in\]
</dt> <dd>

An array of embedded instances of the [**Msvm\_VirtualSystemMigrationNetworkSettingData**](msvm-virtualsystemmigrationnetworksettingdata.md) class that represent the network subnets to be removed.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

If the operation is performed asynchronously, this method will return 4096, and this parameter will contain a reference to an object derived from [**CIM\_ConcreteJob**](/previous-versions//cc136808(v=vs.85)).

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

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**AddNetworkSettings**](addnetworksettings-msvm-virtualsystemmigrationservice.md)
</dt> <dt>

[**ModifyNetworkSettings**](modifynetworksettings-msvm-virtualsystemmigrationservice.md)
</dt> <dt>

[**Msvm\_VirtualSystemMigrationService**](msvm-virtualsystemmigrationservice.md)
</dt> </dl>

 

