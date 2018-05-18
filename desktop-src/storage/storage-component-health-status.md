---
title: STORAGE\_COMPONENT\_HEALTH\_STATUS enumeration
description: Indicates the health status of a storage device.
ms.assetid: '6768C1D7-A964-44A7-A340-98060130FF24'
keywords: ["STORAGE_COMPONENT_HEALTH_STATUS enumeration Storage Devices", "PSTORAGE_COMPONENT_HEALTH_STATUS enumeration pointer Storage Devices"]
topic_type:
- apiref
api_name:
- STORAGE_COMPONENT_HEALTH_STATUS
api_location:
- Ntddstor.h
api_type:
- HeaderDef
---

# STORAGE\_COMPONENT\_HEALTH\_STATUS enumeration

Indicates the health status of a storage device.

## Syntax


```C++
typedef enum _STORAGE_COMPONENT_HEALTH_STATUS { 
  HealthStatusUnknown    = 0, // 0x0
  HealthStatusNormal,
  HealthStatusThrottled,
  HealthStatusWarning,
  HealthStatusDisabled,
  HealthStatusFailed
} STORAGE_COMPONENT_HEALTH_STATUS, *PSTORAGE_COMPONENT_HEALTH_STATUS;
```



## Constants

<dl> <dt>

<span id="HealthStatusUnknown"></span><span id="healthstatusunknown"></span><span id="HEALTHSTATUSUNKNOWN"></span>**HealthStatusUnknown**
</dt> <dd>

The storage device health status is unknown.

</dd> <dt>

<span id="HealthStatusNormal"></span><span id="healthstatusnormal"></span><span id="HEALTHSTATUSNORMAL"></span>**HealthStatusNormal**
</dt> <dd>

The storage device is operating normally.

</dd> <dt>

<span id="HealthStatusThrottled"></span><span id="healthstatusthrottled"></span><span id="HEALTHSTATUSTHROTTLED"></span>**HealthStatusThrottled**
</dt> <dd>

The storage device has been throttled.

</dd> <dt>

<span id="HealthStatusWarning"></span><span id="healthstatuswarning"></span><span id="HEALTHSTATUSWARNING"></span>**HealthStatusWarning**
</dt> <dd>

The storage device has issued a warning.

</dd> <dt>

<span id="HealthStatusDisabled"></span><span id="healthstatusdisabled"></span><span id="HEALTHSTATUSDISABLED"></span>**HealthStatusDisabled**
</dt> <dd>

The storage device has been disabled.

</dd> <dt>

<span id="HealthStatusFailed"></span><span id="healthstatusfailed"></span><span id="HEALTHSTATUSFAILED"></span>**HealthStatusFailed**
</dt> <dd>

The storage device has failed.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_COMPONENT_HEALTH_STATUS%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





