---
title: SetPowerState method of the MSCluster\_Node class
description: Defines the desired power state of a ComputerSystem and its running OperatingSystem, and when the system should be put into that state.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 48644d59-feb9-4de9-99af-82106458c26f
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetPowerState method
- SetPowerState method, MSCluster_Node class
- MSCluster_Node class, SetPowerState method
topic_type:
- apiref
api_name:
- MSCluster_Node.SetPowerState
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetPowerState method of the MSCluster\_Node class

Defines the desired power state of a ComputerSystem and its running OperatingSystem, and when the system should be put into that state. The *PowerState* parameter is specified as one of the valid integer values defined for the property, *PowerState*. The Time parameter (for all state changes but 5, "Power Cycle") indicates when the power state should be set, either as a regular date-time value or as an interval value (where the interval begins when the method invocation is received). When the *PowerState* parameter is equal to 5, "Power Cycle", the Time parameter indicates when the system should power on again. Power off is immediate. **SetPowerState** should return 0 if successful, 1 if the specified State and Time request is not supported, and some other value if any other error occurred.

## Syntax


```mof
uint32 SetPowerState(
  [in] uint16   PowerState,
  [in] datetime Time
);
```



## Parameters

<dl> <dt>

*PowerState* \[in\]
</dt> <dd>

Specifies the power operation.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Full_Power"></span><span id="full_power"></span><span id="FULL_POWER"></span>

**Full Power** (1)


</dt> <dd></dd> <dt>

<span id="Power_Save_-_Low_Power_Mode"></span><span id="power_save_-_low_power_mode"></span><span id="POWER_SAVE_-_LOW_POWER_MODE"></span>

**Power Save - Low Power Mode** (2)


</dt> <dd></dd> <dt>

<span id="Power_Save_-_Standby"></span><span id="power_save_-_standby"></span><span id="POWER_SAVE_-_STANDBY"></span>

**Power Save - Standby** (3)


</dt> <dd></dd> <dt>

<span id="Power_Save_-_Unknown"></span><span id="power_save_-_unknown"></span><span id="POWER_SAVE_-_UNKNOWN"></span>

**Power Save - Unknown** (4)


</dt> <dd></dd> <dt>

<span id="Power_Cycle"></span><span id="power_cycle"></span><span id="POWER_CYCLE"></span>

**Power Cycle** (5)


</dt> <dd></dd> <dt>

<span id="Power_Off"></span><span id="power_off"></span><span id="POWER_OFF"></span>

**Power Off** (6)


</dt> <dd></dd> <dt>

<span id="Power_Save_-_Warning"></span><span id="power_save_-_warning"></span><span id="POWER_SAVE_-_WARNING"></span>

**Power Save - Warning** (7)


</dt> <dd></dd> </dl> </dd> <dt>

*Time* \[in\]
</dt> <dd>

Indicates when the power state should be set, either as a regular date-time value or as an interval value (where the interval begins when the method invocation is received). When the *PowerState* parameter is equal to 5, "Power Cycle", the *Time* parameter indicates when the system should power on again. Power off is immediate.

</dd> </dl>

## Return value

Returns 0 if successful, 1 if the specified power state and time requests are not supported, and some other value if any other error occurred.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWMI.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_Node**](mscluster-node.md)
</dt> </dl>

 

 





