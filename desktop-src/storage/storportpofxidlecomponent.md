---
title: StorPortPoFxIdleComponent routine
description: The StorPortPoFxIdleComponent routine decrements the activation reference count of a specified component of a storage device.
ms.assetid: 'DF329B68-3995-4B38-8208-4C779B0626A6'
keywords: ["StorPortPoFxIdleComponent routine Storage Devices"]
topic_type:
- apiref
api_name:
- StorPortPoFxIdleComponent
api_location:
- storport.h
api_type:
- HeaderDef
---

# StorPortPoFxIdleComponent routine

The **StorPortPoFxIdleComponent** routine decrements the activation reference count of a specified component of a storage device.

## Syntax


```C++
ULONG StorPortPoFxIdleComponent(
  _In_     PVOID               HwDeviceExtension,
  _In_opt_ PSTOR_ADDRESS       Address,
  _In_opt_ PSCSI_REQUEST_BLOCK Srb,
  _In_     ULONG               Component,
  _In_     ULONG               Flags
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension for the host bus adapter (HBA).

</dd> <dt>

*Address* \[in, optional\]
</dt> <dd>

The address of a storage device unit. This parameter is **NULL** when idling a storage adapter component.

</dd> <dt>

*Srb* \[in, optional\]
</dt> <dd>

The SRB triggering the component deactivation. This parameter is **NULL** if the miniport is idling a device component internally.

</dd> <dt>

*Component* \[in\]
</dt> <dd>

The index that identifies the component. This parameter is an index into the **Components** array in the [**STOR\_POFX\_DEVICE**](stor-pofx-device.md) structure that the miniport driver registered for the device with a call to [**StorPortInitializePoFxPower**](storportinitializepofxpower.md). If the **Components** array contains N elements, component indexes range from 0 to N–1.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Not used. Set to 0.

</dd> </dl>

## Return value

The **StorPortPoFxIdleComponent** routine returns one of these status codes:



| Return code                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>                  | The storage device activation reference was successfully decremented and the component is idle.<br/>                                                                                                                                                                                                                                                                                                                                                                                 |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl>       | Either *HwDeviceExtension* or *Device* is NULL.<br/> -or-<br/> *Address* points to an invalid unit address structure.<br/> -or-<br/> The storage device specified by *Address* is not found.<br/> -or-<br/> The storage device is not registered with the power management framework (PoFx).<br/> -or-<br/> The SRB pointed to by *Srb* is not sent from Storport.<br/> -or-<br/> The *Flags* parameter is nonzero.<br/> |
| <dl> <dt>**STOR\_STATUS\_INVALID\_DEVICE\_REQUEST**</dt> </dl> | The adapter or unit does not support PoFx.<br/> -or-<br/> **StorPortPoFxIdleComponent** was called with an inactive *Component* and an *Srb* for which a previous call to [**StorPortPoFxActivateComponent**](storportpofxactivatecomponent.md) was not performed.<br/>                                                                                                                                                                                                 |
| <dl> <dt>**STOR\_STATUS\_INVALID\_IRQL**</dt> </dl>            | The current IRQL &gt; DISPATCH\_LEVEL.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| <dl> <dt>**STOR\_STATUS\_BUSY**</dt> </dl>                     | The active reference for the device component was decremented but the component is still active.<br/>                                                                                                                                                                                                                                                                                                                                                                                |



 

## Remarks

Currently, both adapter devices and unit devices have maximum component count of 1. The index in *Component* must always be set to 0.

Each call to **StorPortPoFxIdleComponent** must be matched with a previous call to [**StorPortPoFxActivateComponent**](storportpofxactivatecomponent.md).

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Available in starting with Windows 8.<br/>                                                                                        |
| Header<br/>          | <dl> <dt>Storport.h</dt> </dl>                                                   |
| IRQL<br/>            | Any<br/>                                                                                                                          |



## See also

<dl> <dt>

[**STOR\_POFX\_DEVICE**](stor-pofx-device.md)
</dt> <dt>

[**StorPortInitializePoFxPower**](storportinitializepofxpower.md)
</dt> <dt>

[**StorPortPoFxActivateComponent**](storportpofxactivatecomponent.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortPoFxIdleComponent%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






