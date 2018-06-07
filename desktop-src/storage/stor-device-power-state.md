---
title: STOR\_DEVICE\_POWER\_STATE enumeration
description: The STOR\_DEVICE\_POWER\_STATE enumerator specifies a device power state.
ms.assetid: 563ece3e-1359-4e3c-9ae7-61b94bf90ad0
keywords:
- STOR_DEVICE_POWER_STATE enumeration Storage Devices
- PSTOR_DEVICE_POWER_STATE enumeration pointer Storage Devices
topic_type:
- apiref
api_name:
- STOR_DEVICE_POWER_STATE
api_location:
- storport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# STOR\_DEVICE\_POWER\_STATE enumeration

The STOR\_DEVICE\_POWER\_STATE enumerator specifies a device power state.

## Syntax


```C++
typedef enum _STOR_DEVICE_POWER_STATE { 
  StorPowerDeviceUnspecified  = 0,
  StorPowerDeviceD0           = 1,
  StorPowerDeviceD1           = 2,
  StorPowerDeviceD2           = 3,
  StorPowerDeviceD3           = 4,
  StorPowerDeviceMaximum      = 5
} STOR_DEVICE_POWER_STATE, *PSTOR_DEVICE_POWER_STATE;
```



## Constants

<dl> <dt>

<span id="StorPowerDeviceUnspecified"></span><span id="storpowerdeviceunspecified"></span><span id="STORPOWERDEVICEUNSPECIFIED"></span>**StorPowerDeviceUnspecified**
</dt> <dd>

Device power state unspecified.

</dd> <dt>

<span id="StorPowerDeviceD0"></span><span id="storpowerdeviced0"></span><span id="STORPOWERDEVICED0"></span>**StorPowerDeviceD0**
</dt> <dd>

The D0 device power state.

</dd> <dt>

<span id="StorPowerDeviceD1"></span><span id="storpowerdeviced1"></span><span id="STORPOWERDEVICED1"></span>**StorPowerDeviceD1**
</dt> <dd>

The D1 device power state.

</dd> <dt>

<span id="StorPowerDeviceD2"></span><span id="storpowerdeviced2"></span><span id="STORPOWERDEVICED2"></span>**StorPowerDeviceD2**
</dt> <dd>

The D2 device power state.

</dd> <dt>

<span id="StorPowerDeviceD3"></span><span id="storpowerdeviced3"></span><span id="STORPOWERDEVICED3"></span>**StorPowerDeviceD3**
</dt> <dd>

The D3 device power state.

</dd> <dt>

<span id="StorPowerDeviceMaximum"></span><span id="storpowerdevicemaximum"></span><span id="STORPOWERDEVICEMAXIMUM"></span>**StorPowerDeviceMaximum**
</dt> <dd>

The upper delimiting value on device power states.

</dd> </dl>

## Requirements



|                   |                                                                                                                                  |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Storport.h (include Storport.h, Minitape.h, or Srb.h)</dt> </dl> |



## See also

<dl> <dt>

[**SCSI\_POWER\_REQUEST\_BLOCK**](scsi-power-request-block.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STOR_DEVICE_POWER_STATE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






