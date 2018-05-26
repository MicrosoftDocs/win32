---
title: SetPowerState method of the CIM\_ComputerSystem class
description: Deprecated description Sets the power state of the computer.This method is deprecated. Instead, use the RequestPowerStateChange method in the CIM\_PowerManagementService class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3db8ec72-cbb7-491b-8c20-c3bef89ba8bb
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetPowerState method
- SetPowerState method, CIM_ComputerSystem class
- CIM_ComputerSystem class, SetPowerState method
topic_type:
- apiref
api_name:
- CIM_ComputerSystem.SetPowerState
api_location:
- VMMS.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetPowerState method of the CIM\_ComputerSystem class

**Deprecated description:** Sets the power state of the computer.

This method is deprecated. Instead, use the **RequestPowerStateChange** method in the **CIM\_PowerManagementService** class.

## Syntax


```mof
uint32 SetPowerState(
  [in] uint32   PowerState,
  [in] datetime Time
);
```



## Parameters

<dl> <dt>

*PowerState* \[in\]
</dt> <dd>

The new state of the computer system.

<dt>

<span id="Full_Power"></span><span id="full_power"></span><span id="FULL_POWER"></span>

**Full Power** (1)


</dt> <dd></dd> <dt>

<span id="Power_Save_-_Low_Power_Mode"></span><span id="power_save_-_low_power_mode"></span><span id="POWER_SAVE_-_LOW_POWER_MODE"></span>

**Power Save - Low Power Mode** (2)


</dt> <dd></dd> <dt>

<span id="Power_Save_-_Standby"></span><span id="power_save_-_standby"></span><span id="POWER_SAVE_-_STANDBY"></span>

**Power Save - Standby** (3)


</dt> <dd></dd> <dt>

<span id="Power_Save_-_Other"></span><span id="power_save_-_other"></span><span id="POWER_SAVE_-_OTHER"></span>

**Power Save - Other** (4)


</dt> <dd></dd> <dt>

<span id="Power_Cycle"></span><span id="power_cycle"></span><span id="POWER_CYCLE"></span>

**Power Cycle** (5)


</dt> <dd></dd> <dt>

<span id="Power_Off"></span><span id="power_off"></span><span id="POWER_OFF"></span>

**Power Off** (6)


</dt> <dd></dd> <dt>

<span id="Hibernate"></span><span id="hibernate"></span><span id="HIBERNATE"></span>

**Hibernate** (7)


</dt> <dd></dd> <dt>

<span id="Soft_Off"></span><span id="soft_off"></span><span id="SOFT_OFF"></span>

**Soft Off** (8)


</dt> <dd></dd> </dl> </dd> <dt>

*Time* \[in\]
</dt> <dd>

A regular date-time value or an interval value that indicates when to set the power state. If this is property contains an interval value, the interval must begin when the method invocation is received.

</dd> </dl>

## Return value

Returns "0" on success, otherwise returns a WMI error code.

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

[**CIM\_ComputerSystem**](cim-computersystem.md)
</dt> </dl>

 

 





