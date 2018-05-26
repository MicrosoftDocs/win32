---
title: SetPowerState method of the CIM\_ComputerSystem class
description: Sets the power state of the computer. The use of this method has been deprecated. Instead, use the SetPowerState method in the associated PowerManagementService class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 745e375a-3307-4776-9ec0-ca95b0ee70d1
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetPowerState method iSCSI Software Target API
- SetPowerState method iSCSI Software Target API , CIM_ComputerSystem class
- CIM_ComputerSystem class iSCSI Software Target API , SetPowerState method
topic_type:
- apiref
api_name:
- CIM_ComputerSystem.SetPowerState
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetPowerState method of the CIM\_ComputerSystem class

Sets the power state of the computer. The use of this method has been deprecated. Instead, use the SetPowerState method in the associated PowerManagementService class.

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

The Desired state for the ComputerSystem.

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

Time indicates when the power state should be set, either as a regular date-time value or as an interval value (where the interval begins when the method invocation is received.

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ComputerSystem**](cim-computersystem.md)
</dt> </dl>

 

 





