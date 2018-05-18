---
title: STOR\_UNIT\_ATTRIBUTES structure
description: The STOR\_UNIT\_ATTRIBUTES structure contains bitfields indicating attribute support for a storage device unit.
ms.assetid: '9677C044-354B-4575-B2EC-187D1B4E8C61'
keywords: ["STOR_UNIT_ATTRIBUTES structure Storage Devices", "PSTOR_UNIT_ATTRIBUTES structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- STOR_UNIT_ATTRIBUTES
api_location:
- Storport.h
api_type:
- HeaderDef
---

# STOR\_UNIT\_ATTRIBUTES structure

The **STOR\_UNIT\_ATTRIBUTES** structure contains bitfields indicating attribute support for a storage device unit.

## Syntax


```C++
typedef struct _STOR_UNIT_ATTRIBUTES {
  ULONG DeviceAttentionSupported  :1;
  ULONG AsyncNotificationSupported  :1;
  ULONG D3ColdNotSupported  :1;
  ULONG Reserved  :29;
} STOR_UNIT_ATTRIBUTES, *PSTOR_UNIT_ATTRIBUTES;
```



## Members

<dl> <dt>

**DeviceAttentionSupported**
</dt> <dd>

Set to 1 if device attention is supported for the unit. Otherwise, set to 0.

</dd> <dt>

**AsyncNotificationSupported**
</dt> <dd>

Set to 1 if the device supports asynchronous notifications. Otherwise, set to 0.

</dd> <dt>

**D3ColdNotSupported**
</dt> <dd>

Set to 1 if the D3 Cold power state is NOT supported. Otherwise, set to 0.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved bits. Must be set to 0.

</dd> </dl>

## Remarks

The unit attributes are registered with Storport using this structure as a parameter to the [**StorPortSetUnitAttributes**](storportsetunitattributes.md) routine.

If the miniport driver supports asynchronous notifications, the **AsyncNotificationSupported** field set to 1, it will send notifications to the Storport driver using the [**StorPortAsyncNotificationDetected**](storportasyncnotificationdetected.md) routine.

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8.<br/>                                                              |
| Header<br/>  | <dl> <dt>Storport.h (include Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[**StorPortAsyncNotificationDetected**](storportasyncnotificationdetected.md)
</dt> <dt>

[**StorPortSetUnitAttributes**](storportsetunitattributes.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STOR_UNIT_ATTRIBUTES%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






