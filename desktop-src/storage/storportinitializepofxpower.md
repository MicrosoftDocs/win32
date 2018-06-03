---
title: StorPortInitializePoFxPower routine
description: A miniport driver calls StorPortInitializePoFxPower to register a storage device with the power management framework (PoFx).
ms.assetid: 154EAF9B-4B30-4124-B31D-6C7D09B52674
keywords:
- StorPortInitializePoFxPower routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortInitializePoFxPower
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

# StorPortInitializePoFxPower routine

A miniport driver calls **StorPortInitializePoFxPower** to register a storage device with the power management framework (PoFx).

## Syntax


```C++
ULONG StorPortInitializePoFxPower(
  _In_     PVOID             HwDeviceExtension,
  _In_opt_ PSTOR_ADDRESS     Address,
  _In_     PSTOR_POFX_DEVICE Device,
  _Inout_  PBOOLEAN          D3ColdEnabled
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

The address of a storage device unit. This parameter is **NULL** when registering for a storage adapter.

</dd> <dt>

*Device* \[in\]
</dt> <dd>

A pointer to a **STOR\_POFX\_DEVICE\_V2** structure cast to a pointer to [**STOR\_POFX\_DEVICE**](stor-pofx-device.md). This structure contains a component list with F-states for a storage device.

</dd> <dt>

*D3ColdEnabled* \[in, out\]
</dt> <dd>

A pointer to a **BOOLEAN** value which the Storport driver will set to indicate whether the D3 Cold state is enabled for the storage device.

</dd> </dl>

## Return value

The **StorPortInitializePoFxPower** routine returns one of these status codes:



| Return code                                                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl>      | Either *HwDeviceExtension* or *Device* is NULL.<br/> -or-<br/> *Address* points to an invalid unit address structure.<br/> -or-<br/> The storage device specified by *Address* is not found.<br/> -or-<br/> The [**STOR\_POFX\_DEVICE**](stor-pofx-device.md) structure pointed to by *Device* is formatted incorrectly or contains invalid data.<br/> |
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>                 | The storage device was successfully registered with PoFx.<br/>                                                                                                                                                                                                                                                                                                                              |
| <dl> <dt>**STOR\_STATUS\_INSUFFICIENT\_RESOURCES**</dt> </dl> | Sufficient resources are not available to register the storage device with PoFx.<br/>                                                                                                                                                                                                                                                                                                       |
| <dl> <dt>**STOR\_STATUS\_UNSUCCESSFUL**</dt> </dl>            | The storage device was not successfully registered with PoFx.<br/> -or-<br/> The storage device is already registered with PoFx.<br/>                                                                                                                                                                                                                                           |



 

## Remarks

Adapter devices are always registered with a **NULL** value for *address*. Unit devices are registered by specifying a valid unit address for *address*.

If the **STOR\_POFX\_DEVICE\_FLAG\_ENABLE\_D3\_COLD** flag is set in the **Flags** member of *Device*, Storport will attempt to enable D3 Cold support for the device component. The D3 Cold enabled status is returned in the **BOOLEAN** value pointed to by *D3ColdEnabled*.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Available in starting with Windows 8.<br/>                                                                                        |
| Header<br/>          | <dl> <dt>Storport.h</dt> </dl>                                                   |



## See also

<dl> <dt>

[**STOR\_POFX\_DEVICE**](stor-pofx-device.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortInitializePoFxPower%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






