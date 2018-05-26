---
title: SetPowerState method of the MSISCSITARGET\_SCSIProtocolController class
description: Sets the power state of the device.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fea6e618-dc3f-47ec-8593-96cf79658984
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetPowerState method iSCSI Software Target API
- SetPowerState method iSCSI Software Target API , MSISCSITARGET_SCSIProtocolController class
- MSISCSITARGET_SCSIProtocolController class iSCSI Software Target API , SetPowerState method
topic_type:
- apiref
api_name:
- MSISCSITARGET_SCSIProtocolController.SetPowerState
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetPowerState method of the MSISCSITARGET\_SCSIProtocolController class

Sets the power state of the device. Deprecated. Instead, use the **SetPowerState** method in the associated power management service instance.

This method is inherited from the [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) class.

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

Specifies the power state to set.

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

Specifies when the power state should be set, either as a regular date-time value or as an interval value where the interval begins when the method invocation is received.

</dd> </dl>

## Return value

Returns zero on success; otherwise returns an error code.

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_SCSIProtocolController**](msiscsitarget-scsiprotocolcontroller.md)
</dt> </dl>

 

 





