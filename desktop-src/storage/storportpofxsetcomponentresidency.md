---
title: StorPortPoFxSetComponentResidency routine
description: The StorPortPoFxSetComponentResidency routine sets the estimated time for how long a storage device component is likely to remain idle after the component enters the idle condition.
ms.assetid: 78DFB17E-5351-419A-9B9B-8CBCD7548910
keywords:
- StorPortPoFxSetComponentResidency routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortPoFxSetComponentResidency
api_location:
- storport.lib
- storport.dll
api_type:
- LibDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# StorPortPoFxSetComponentResidency routine

The **StorPortPoFxSetComponentResidency** routine sets the estimated time for how long a storage device component is likely to remain idle after the component enters the idle condition.

## Syntax


```C++
ULONG StorPortPoFxSetComponentResidency(
  _In_     PVOID         HwDeviceExtension,
  _In_opt_ PSTOR_ADDRESS Address,
  _In_     ULONG         Component,
  _In_     ULONGLONG     Residency
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

The address of a storage device unit. This parameter is **NULL** when setting the residency of a storage adapter component.

</dd> <dt>

*Component* \[in\]
</dt> <dd>

The index that identifies the component. This parameter is an index into the **Components** array in the [**STOR\_POFX\_DEVICE**](stor-pofx-device.md) structure that the miniport driver registered for the device with a call to [**StorPortInitializePoFxPower**](storportinitializepofxpower.md). If the **Components** array contains N elements, component indexes range from 0 to N 1.

</dd> <dt>

*Residency* \[in\]
</dt> <dd>

The estimated residency time, in 100-nanosecond units. This parameter is a hint to power management framework (PoFx) about how long the component is likely to remain idle after a transition from the active condition to the idle condition.

</dd> </dl>

## Return value

The **StorPortPoFxSetComponentResidency** routine returns one of these status codes:



| Return code                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                |
|-----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>                  | The component residency is successfully set.<br/>                                                                                                                                                                                                                                                                                                    |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl>       | Either *HwDeviceExtension* or *Device* is NULL.<br/> -or-<br/> *Address* points to an invalid unit address structure.<br/> -or-<br/> The storage device specified by *Address* is not found.<br/> -or-<br/> The index in *Component* specifies a component greater than the component count for the device.<br/> |
| <dl> <dt>**STOR\_STATUS\_INVALID\_DEVICE\_REQUEST**</dt> </dl> | The storage device is not registered with the PoFx.<br/>                                                                                                                                                                                                                                                                                             |
| <dl> <dt>**STOR\_STATUS\_INVALID\_IRQL**</dt> </dl>            | The current IRQL &gt; DISPATCH\_LEVEL.<br/>                                                                                                                                                                                                                                                                                                          |



 

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Available in starting with Windows 8.<br/>                                                                                        |
| Header<br/>          | <dl> <dt>Storport.h</dt> </dl>                                                   |
| Library<br/>         | <dl> <dt>Storport.lib</dt> </dl>                                                 |
| IRQL<br/>            | &lt;= DISPATCH\_LEVEL<br/>                                                                                                        |



## See also

<dl> <dt>

[**PoFxSetComponentResidency**](https://msdn.microsoft.com/library/windows/hardware/hh439536)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortPoFxSetComponentResidency%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






