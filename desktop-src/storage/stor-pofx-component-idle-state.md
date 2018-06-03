---
title: STOR\_POFX\_COMPONENT\_IDLE\_STATE structure
description: The STOR\_POFX\_COMPONENT\_IDLE\_STATE structure specifies the attributes of an functional power state (F-state) of a component in a storage device.
ms.assetid: 2600405F-AE07-4284-84AD-D19EEE2058BF
keywords:
- STOR_POFX_COMPONENT_IDLE_STATE structure Storage Devices
- PSTOR_POFX_COMPONENT_IDLE_STATE structure pointer Storage Devices
topic_type:
- apiref
api_name:
- STOR_POFX_COMPONENT_IDLE_STATE
api_location:
- Storport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# STOR\_POFX\_COMPONENT\_IDLE\_STATE structure

The **STOR\_POFX\_COMPONENT\_IDLE\_STATE** structure specifies the attributes of an functional power state (F-state) of a component in a storage device.

## Syntax


```C++
typedef struct _STOR_POFX_COMPONENT_IDLE_STATE {
  USHORT    Version;
  USHORT    Size;
  ULONGLONG TransitionLatency;
  ULONGLONG ResidencyRequirement;
  ULONG     NominalPower;
} STOR_POFX_COMPONENT_IDLE_STATE, *PSTOR_POFX_COMPONENT_IDLE_STATE;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The version of this structure. Set this member to **STOR\_POFX\_COMPONENT\_IDLE\_STATE\_VERSION\_V1**.

</dd> <dt>

**Size**
</dt> <dd>

The size of this structure. Set this value to **STOR\_POFX\_COMPONENT\_IDLE\_STATE\_SIZE**.

</dd> <dt>

**TransitionLatency**
</dt> <dd>

The transition latency. This latency is the amount of time, in 100-nanosecond units, that the component requires to return from this F-state to the F0 state. For a **STOR\_POFX\_COMPONENT\_IDLE\_STATE** structure that specifies the attributes of the F0 state, set this member to zero. Set this member to STOR\_PO\_FX\_UNKNOWN\_TIME to indicate that the power management framework (PoFx) should ignore (treat as negligible) the component's transition latency from this F-state when PoFx evaluates which power state to switch to when the component is idle.

</dd> <dt>

**ResidencyRequirement**
</dt> <dd>

The residency requirement. The residency requirement is the minimum amount of time, in 100-nanosecond units, that the component must spend in this F-state to make a transition to this F-state worthwhile. PoFx uses this member value as a hint to avoid switching a component to an F-state unless the component is likely to remain in this state for at least the amount of time specified by **ResidencyRequirement**. For a STOR\_PO\_FX\_COMPONENT\_IDLE\_STATE structure that describes the attributes of the F0 state, set this member to zero. Set this member to STOR\_PO\_FX\_UNKNOWN\_TIME to indicate that PoFx should ignore (treat as negligible) the component's residency requirement for this F-state when PoFx evaluates which power state to switch to when the component is idle.

</dd> <dt>

**NominalPower**
</dt> <dd>

The power, in microwatts, that the component consumes in this F-state. Set this member to STOR\_PO\_FX\_UNKNOWN\_POWER to indicate that PoFx should ignore (treat as negligible) the component's internal power consumption in this F-state when PoFx evaluates which power state to switch to when the component is idle.

</dd> </dl>

## Remarks

The [**STOR\_POFX\_COMPONENT**](stor-pofx-component.md) structure contains an array of **STOR\_POFX\_COMPONENT\_IDLE\_STATE** structures. Each array element specifies the attributes of an F-state. Element 0 describes F0, element 1 describes F1, and so on.

When the miniport driver registers a device with the Storport power management framework, the driver supplies an array of [**STOR\_POFX\_COMPONENT**](stor-pofx-component.md) structures. Each array element describes the power attributes of a component in the device.

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available in starting with Windows 8.<br/>                                                           |
| Header<br/>  | <dl> <dt>Storport.h (include Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[**STOR\_POFX\_COMPONENT**](stor-pofx-component.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STOR_POFX_COMPONENT_IDLE_STATE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






