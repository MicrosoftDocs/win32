---
title: SetPowerState method of the Msvm\_VssComponent class
description: This method is deprecated. Instead, use the SetPowerState property of the CIM\_PowerManagementService class.
ms.assetid: d1dbc97b-7dbe-4055-bb7e-350c1757a3f2
keywords:
- SetPowerState method Hyper-V
- SetPowerState method Hyper-V , Msvm_VssComponent class
- Msvm_VssComponent class Hyper-V , SetPowerState method
topic_type:
- apiref
api_name:
- Msvm_VssComponent.SetPowerState
api_location:
- Root\virtualization
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SetPowerState method of the Msvm\_VssComponent class

This method is deprecated. Instead, use the **SetPowerState** property of the **CIM\_PowerManagementService** class.

**Deprecated description:** Sets the power state of the logical device.

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

The power state to set.

The possible values are.

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


</dt> <dd></dd> </dl> </dd> <dt>

*Time* \[in\]
</dt> <dd>

Indicates when to set the power state, either as a regular **datetime** value or as an interval value (where the interval begins when the method invocation is received).

</dd> </dl>

## Return value

<dl> <dt>


</dt> <dd>

0

The operation completed successfully.

</dd> <dt>


</dt> <dd>

1

The operation was not completed because it is not supported.

</dd> <dt>


</dt> <dd>

2 = *value*

The operation was not completed because an error occurred.

</dd> </dl>

## Requirements



|                      |                                                                                                      |
|----------------------|------------------------------------------------------------------------------------------------------|
| Namespace<br/> | Root\\virtualization<br/>                                                                      |
| MOF<br/>       | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_LogicalDevice**](cim-logicaldevice.md)
</dt> <dt>

[**Msvm\_VssComponent**](msvm-vsscomponent.md)
</dt> </dl>

 

 





