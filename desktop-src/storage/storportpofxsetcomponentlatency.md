---
title: StorPortPoFxSetComponentLatency routine
description: The StorPortPoFxSetComponentLatency routine specifies the maximum latency that can be tolerated in the transition from the idle condition to the active condition in the specified storage device component.
ms.assetid: F175ED42-3DB6-4568-96CA-EFC283B14887
keywords:
- StorPortPoFxSetComponentLatency routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortPoFxSetComponentLatency
api_location:
- storport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StorPortPoFxSetComponentLatency routine

The **StorPortPoFxSetComponentLatency** routine specifies the maximum latency that can be tolerated in the transition from the idle condition to the active condition in the specified storage device component.

## Syntax


```C++
ULONG StorPortPoFxSetComponentLatency(
  _In_     PVOID         HwDeviceExtension,
  _In_opt_ PSTOR_ADDRESS Address,
  _In_     ULONG         Component,
  _In_     ULONGLONG     Latency
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension for the host bus adapter (HBA). This is the device extension used to register the device in a prior call to [**StorPortInitializePoFxPower**](storportinitializepofxpower.md).

</dd> <dt>

*Address* \[in, optional\]
</dt> <dd>

The address of a storage device unit. This parameter is **NULL** when setting the latency of a storage adapter component.

</dd> <dt>

*Component* \[in\]
</dt> <dd>

The index that identifies the component. This parameter is an index into the **Components** array in the [**STOR\_POFX\_DEVICE**](stor-pofx-device.md) structure that the miniport driver registered for the device with a call to [**StorPortInitializePoFxPower**](storportinitializepofxpower.md). If the **Components** array contains N elements, component indexes range from 0 to N 1.

</dd> <dt>

*Latency* \[in\]
</dt> <dd>

The time, in units of 100 nanoseconds, that the storage device component can tolerate for a transition from an idle state the active state.

</dd> </dl>

## Return value

The **StorPortPoFxSetComponentLatency** routine returns one of these status codes:



| Return code                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                |
|-----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>                  | The component latency successfully set.<br/>                                                                                                                                                                                                                                                                                                         |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl>       | Either *HwDeviceExtension* or *Device* is NULL.<br/> -or-<br/> *Address* points to an invalid unit address structure.<br/> -or-<br/> The storage device specified by *Address* is not found.<br/> -or-<br/> The index in *Component* specifies a component greater than the component count for the device.<br/> |
| <dl> <dt>**STOR\_STATUS\_INVALID\_DEVICE\_REQUEST**</dt> </dl> | The storage device is not registered with the power management framework (PoFx).<br/>                                                                                                                                                                                                                                                                |
| <dl> <dt>**STOR\_STATUS\_INVALID\_IRQL**</dt> </dl>            | The current IRQL &gt; DISPATCH\_LEVEL.<br/>                                                                                                                                                                                                                                                                                                          |



 

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Available in starting with Windows 8.<br/>                                                                                        |
| Header<br/>          | <dl> <dt>Storport.h</dt> </dl>                                                   |
| IRQL<br/>            | &lt;= DISPATCH\_LEVEL<br/>                                                                                                        |



## See also

<dl> <dt>

[**PoFxSetComponentLatency**](https://msdn.microsoft.com/library/windows/hardware/hh439531)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortPoFxSetComponentLatency%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






