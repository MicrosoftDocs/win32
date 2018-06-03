---
title: STORAGE\_DEVICE\_POWER\_CAP\_UNITS enumeration
description: The units of the maximum power threshold.
ms.assetid: 199900F4-90A7-4F2E-B85E-25BF3593D50B
keywords:
- STORAGE_DEVICE_POWER_CAP_UNITS enumeration Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_DEVICE_POWER_CAP_UNITS
api_location:
- ntddstor.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# STORAGE\_DEVICE\_POWER\_CAP\_UNITS enumeration

The units of the maximum power threshold.

## Syntax


```C++
typedef enum _STORAGE_DEVICE_POWER_CAP_UNITS { 
  StorageDevicePowerCapUnitsPercent,
  StorageDevicePowerCapUnitsMilliwatts
} STORAGE_DEVICE_POWER_CAP_UNITS;
```



## Constants

<dl> <dt>

<span id="StorageDevicePowerCapUnitsPercent"></span><span id="storagedevicepowercapunitspercent"></span><span id="STORAGEDEVICEPOWERCAPUNITSPERCENT"></span>**StorageDevicePowerCapUnitsPercent**
</dt> <dd>

Units in percent.

</dd> <dt>

<span id="StorageDevicePowerCapUnitsMilliwatts"></span><span id="storagedevicepowercapunitsmilliwatts"></span><span id="STORAGEDEVICEPOWERCAPUNITSMILLIWATTS"></span>**StorageDevicePowerCapUnitsMilliwatts**
</dt> <dd>

Units in milliwatts.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Client<br/> | Windows 10<br/>                                                                                      |
| Server<br/> | Windows Server 2016<br/>                                                                             |
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_DEVICE_POWER_CAP_UNITS%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





