---
title: ModifySystemSettings method of the CIM\_VirtualSystemManagementService class
description: Updates the settings of a virtual system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '6018dc1c-b5c8-4198-9743-d38fdd009563'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["ModifySystemSettings method", "ModifySystemSettings method, CIM_VirtualSystemManagementService class", "CIM_VirtualSystemManagementService class, ModifySystemSettings method"]
topic_type:
- apiref
api_name:
- CIM_VirtualSystemManagementService.ModifySystemSettings
api_location:
- VMMS.exe
api_type:
- COM
---

# ModifySystemSettings method of the CIM\_VirtualSystemManagementService class

Updates the settings of a virtual system.

## Syntax


```mof
uint32 ModifySystemSettings(
  [in]  string              SystemSettings,
  [out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*SystemSettings* \[in\]
</dt> <dd>

An embedded instance of the [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md) class that is used to update the system.

> [!Note]  
> The [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md) must have a valid **InstanceID** property value that identifies the virtual system to update.

 

</dd> <dt>

*Job* \[out\]
</dt> <dd>

If the operation is to run asynchronously, this parameter will return a job for the operation.

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

**DMTF Reserved** (7–4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097–32767)
</dt> <dt>

**Vendor Specific** (32768–65535)
</dt> </dl>

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

[**CIM\_VirtualSystemManagementService**](cim-virtualsystemmanagementservice.md)
</dt> </dl>

 

 





