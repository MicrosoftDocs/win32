---
title: STORAGE\_DEVICE\_POWER\_CAP structure
description: This structure is used as an input and output buffer for the IOCTL\_STORAGE\_DEVICE\_POWER\_CAP.
ms.assetid: '88DEC1F2-F0E7-4E95-9A46-D9E8EF72B1BB'
keywords: ["STORAGE_DEVICE_POWER_CAP structure Storage Devices", "PSTORAGE_DEVICE_POWER_CAP structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- STORAGE_DEVICE_POWER_CAP
api_location:
- ntddstor.h
api_type:
- HeaderDef
---

# STORAGE\_DEVICE\_POWER\_CAP structure

This structure is used as an input and output buffer for the [**IOCTL\_STORAGE\_DEVICE\_POWER\_CAP**](ioctl-storage-device-power-cap.md).

## Syntax


```C++
typedef struct _STORAGE_DEVICE_POWER_CAP {
  ULONG                          Version;
  ULONG                          Size;
  STORAGE_DEVICE_POWER_CAP_UNITS Units;
  ULONG                          MaxPower;
} STORAGE_DEVICE_POWER_CAP, *PSTORAGE_DEVICE_POWER_CAP;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The version of this structure. This should be set to STORAGE\_DEVICE\_POWER\_CAP\_VERSION\_V1.

</dd> <dt>

**Size**
</dt> <dd>

The size of this structure.

</dd> <dt>

**Units**
</dt> <dd>

The units of the MaxPower value.

</dd> <dt>

**MaxPower**
</dt> <dd>

Contains the value of the actual maximum power consumption level of the device. This may be equal to, less than, or greater than the desired threshold, depending on what the device supports.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Client<br/> | Windows 10<br/>                                                                                      |
| Server<br/> | Windows Server 2016<br/>                                                                             |
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_DEVICE_POWER_CAP%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





