---
title: UpgradeSystemVersion method of the Msvm\_VirtualSystemManagementService class
description: Upgrades a virtual machine.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 377814c0-1a57-45a3-9696-17ddb421f0f7
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- UpgradeSystemVersion method
- UpgradeSystemVersion method, Msvm_VirtualSystemManagementService class
- Msvm_VirtualSystemManagementService class, UpgradeSystemVersion method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.UpgradeSystemVersion
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# UpgradeSystemVersion method of the Msvm\_VirtualSystemManagementService class

Upgrades a virtual machine.

## Syntax


```mof
uint32 UpgradeSystemVersion(
  [in]  CIM_ComputerSystem REF ComputerSystem,
  [in]  string                 UpgradeSettingData,
  [out] CIM_ConcreteJob    REF Job
);
```



## Parameters

<dl> <dt>

*ComputerSystem* \[in\]
</dt> <dd>

A reference to the [**CIM\_ComputerSystem**](cim-computersystem.md) that represents the virtual machine.

</dd> <dt>

*UpgradeSettingData* \[in\]
</dt> <dd>

An embedded instance of [**CIM\_SettingData**](cim-settingdata.md) that represents the upgrade settings to apply to the virtual machine.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to an optional job for the operation if the operation is run asynchronously.

</dd> </dl>

## Return value

The possible return values are:

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Failed** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Invalid Parameter** (4)
</dt> <dt>

**Invalid State** (5)
</dt> <dt>

**Incompatible Parameters** (6)
</dt> <dt>

**DMTF Reserved** (7 4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097 32767)
</dt> <dt>

**Vendor Specific** (32768 65535)
</dt> </dl>

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

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> </dl>

 

 





