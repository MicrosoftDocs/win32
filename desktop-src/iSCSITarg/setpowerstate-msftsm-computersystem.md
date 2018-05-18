---
title: SetPowerState method of the MSFTSM\_ComputerSystem class
description: Sets the power state of the computer. This method is deprecated. Instead, use the SetPowerState method in the associated power management service class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1cf693ab-e8d9-4319-a023-7368b9afd855'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SetPowerState method iSCSI Software Target API", "SetPowerState method iSCSI Software Target API , MSFTSM_ComputerSystem class", "MSFTSM_ComputerSystem class iSCSI Software Target API , SetPowerState method"]
topic_type:
- apiref
api_name:
- MSFTSM_ComputerSystem.SetPowerState
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
---

# SetPowerState method of the MSFTSM\_ComputerSystem class

Sets the power state of the computer. This method is deprecated. Instead, use the **SetPowerState** method in the associated power management service class.

This method is inherited from the [**CIM\_ComputerSystem**](https://msdn.microsoft.com/library/aa387219) class.

## Syntax


```mof
uint32 SetPowerState(
  [in] uint32   PowerState,
  [in] datetime Time
);
```



## Parameters

<dl> <dt>

*PowerState* \[in\]
</dt> <dd>

Specifies the requested power state.

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


</dt> <dd></dd> <dt>

<span id="Hibernate"></span><span id="hibernate"></span><span id="HIBERNATE"></span>

**Hibernate** (7)


</dt> <dd></dd> <dt>

<span id="Soft_Off"></span><span id="soft_off"></span><span id="SOFT_OFF"></span>

**Soft Off** (8)


</dt> <dd></dd> </dl> </dd> <dt>

*Time* \[in\]
</dt> <dd>

Specifies when the power state is to be set.

</dd> </dl>

## Return value

Returns zero on success; otherwise returns an error code.

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFTSM\_ComputerSystem**](msftsm-computersystem.md)
</dt> </dl>

 

 





