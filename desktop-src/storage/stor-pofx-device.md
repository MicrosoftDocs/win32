---
title: STOR\_POFX\_DEVICE structure
description: The STOR\_POFX\_DEVICE structure describes the power attributes of a storage device to the power management framework (PoFx).
ms.assetid: 5453CF25-D753-4FED-85E3-D990FAB46626
keywords:
- STOR_POFX_DEVICE structure Storage Devices
- PSTOR_POFX_DEVICE structure pointer Storage Devices
topic_type:
- apiref
api_name:
- STOR_POFX_DEVICE
api_location:
- storport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# STOR\_POFX\_DEVICE structure

The **STOR\_POFX\_DEVICE** structure describes the power attributes of a storage device to the power management framework (PoFx).

## Syntax


```C++
typedef struct _PO_FX_DEVICE {
  ULONG               Version;
  USHORT              Size;
  ULONG               ComponentCount;
  ULONG               Flags;
  STOR_POFX_COMPONENT Components[ANYSIZE_ARRAY];
} STOR_POFX_DEVICE, *PSTOR_POFX_DEVICE;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The version number of this structure. Set this member to **STOR\_POFX\_DEVICE\_VERSION\_V1**.

</dd> <dt>

**Size**
</dt> <dd>

The size of this structure. Set this value to **STOR\_POFX\_DEVICE\_SIZE**.

</dd> <dt>

**ComponentCount**
</dt> <dd>

The number of elements in the **Components** array. Set this member to 1. Currently, only a single component is supported for either a storage adapter or logical unit.

</dd> <dt>

**Flags**
</dt> <dd>

The device power state capabilities flags. The miniport sets one or more of the PoFx device flags to enable or disable power state capabilities.

**Flags** is a bitwise OR combination of the following.



| Value                                                                                                                                                                                                                                                                  | Meaning                                                                                                                                                                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="STOR_POFX_DEVICE_FLAG_DISABLE_INTERRUPTS_ON_D3"></span><span id="stor_pofx_device_flag_disable_interrupts_on_d3"></span><dl> <dt>**STOR\_POFX\_DEVICE\_FLAG\_DISABLE\_INTERRUPTS\_ON\_D3**</dt> </dl> | Specifies that, when set, Storport will disable interrupts when putting the Adapter to D3 and will reactivate interrupts when resuming to D0.<br/>                                                                                   |
| <span id="STOR_POFX_DEVICE_FLAG_ENABLE_D3_COLD"></span><span id="stor_pofx_device_flag_enable_d3_cold"></span><dl> <dt>**STOR\_POFX\_DEVICE\_FLAG\_ENABLE\_D3\_COLD**</dt> </dl>                                | Enables Storport to set the D3 Cold state for the adapter if it supports it. This flag applies to adapters only.<br/>                                                                                                                |
| <span id="STOR_POFX_DEVICE_FLAG_NO_D0"></span><span id="stor_pofx_device_flag_no_d0"></span><dl> <dt>**STOR\_POFX\_DEVICE\_FLAG\_NO\_D0**</dt> </dl>                                                            | Requests that a power up IRP not be sent to the device object for the adapter or unit.<br/>                                                                                                                                          |
| <span id="STOR_POFX_DEVICE_FLAG_NO_D3"></span><span id="stor_pofx_device_flag_no_d3"></span><dl> <dt>**STOR\_POFX\_DEVICE\_FLAG\_NO\_D3**</dt> </dl>                                                            | Requests that a power down IRP not be sent to the device object for the adapter or unit.<br/>                                                                                                                                        |
| <span id="STOR_POFX_DEVICE_FLAG_NO_DUMP_ACTIVE"></span><span id="stor_pofx_device_flag_no_dump_active"></span><dl> <dt>**STOR\_POFX\_DEVICE\_FLAG\_NO\_DUMP\_ACTIVE**</dt> </dl>                                | The miniport is not able to bring the storage device active in dump mode if the device has entered the idle state or the power off when idle state. This flag indicates whether a device is available for dump when it is idle.<br/> |



 

</dd> <dt>

**Components**
</dt> <dd>

This member is the first element in an array of one or more [**STOR\_POFX\_COMPONENT**](https://msdn.microsoft.com/library/windows/hardware/hh439575) elements. If the array contains more than one element, the additional elements immediately follow the **STOR\_POFX\_DEVICE** structure. The array contains one element for each component in the device. Currently, storage devices have only one component so additional component structures are unnecessary.

</dd> </dl>

## Remarks

To register a storage adapter for Storport PoFx support, the miniport driver calls [**StorPortEnablePassiveInitialization**](storportenablepassiveinitialization.md) in its [**HwStorInitialize**](hwstorinitialize.md) routine and implements a [**HwStorPassiveInitializeRoutine**](hwstorpassiveinitializeroutine.md). The miniport calls [**StorPortInitializePoFxPower**](storportinitializepofxpower.md) within it's **HwStorPassiveInitializeRoutine** to provide information about the adapter component.

To register a storage unit for Storport PoFx support, the miniport driver implements the [**HwStorUnitControl**](hwstorunitcontrol.md) callback routine and provides handling of the **ScsiUnitPoFxPowerInfo** unit control code. When the handling the **ScsiUnitPoFxPowerInfo** control code, the miniport calls [**StorPortInitializePoFxPower**](storportinitializepofxpower.md) if idle power management for the unit component is enabled.

The component for the storage device identified by its **Components** array index. Storage devices have only one component so the index of 0 is used. Routines such as [**StorPortPoFxActivateComponent**](storportpofxactivatecomponent.md) and [**StorPortPoFxIdleComponent**](storportpofxidlecomponent.md) use the array index of a component to identify the component.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Version<br/> | Supported starting with Windows 8.<br/>                                         |
| Header<br/>  | <dl> <dt>Storport.h</dt> </dl> |



## See also

<dl> <dt>

[**STOR\_POFX\_COMPONENT**](https://msdn.microsoft.com/library/windows/hardware/hh439575)
</dt> <dt>

[**StorPortInitializePoFxPower**](storportinitializepofxpower.md)
</dt> <dt>

[**StorPortPoFxActivateComponent**](storportpofxactivatecomponent.md)
</dt> <dt>

[**StorPortPoFxIdleComponent**](storportpofxidlecomponent.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STOR_POFX_DEVICE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






