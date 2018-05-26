---
title: STORAGE\_TEMPERATURE\_DATA\_DESCRIPTOR structure
description: This structure is used in conjunction with IOCTL\_STORAGE\_QUERY\_PROPERTY to return temperature data from a storage device or adapter.
ms.assetid: A6041B10-0296-4A96-B65C-C35B8DCB2B5D
keywords:
- STORAGE_TEMPERATURE_DATA_DESCRIPTOR structure Storage Devices
- PSTORAGE_TEMPERATURE_DATA_DESCRIPTOR structure pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_TEMPERATURE_DATA_DESCRIPTOR
api_location:
- ntddstor.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# STORAGE\_TEMPERATURE\_DATA\_DESCRIPTOR structure

This structure is used in conjunction with [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) to return temperature data from a storage device or adapter.

## Syntax


```C++
typedef struct _STORAGE_TEMPERATURE_DATA_DESCRIPTOR {
  ULONG                    Version;
  ULONG                    Size;
  SHORT                    CriticalTemperature;
  SHORT                    WarningTemperature;
  USHORT                   InfoCount;
  UCHAR                    Reserved0[2];
  ULONG                    Reserved1[2];
  STORAGE_TEMPERATURE_INFO TemperatureInfo[ANYSIZE_ARRAY];
} STORAGE_TEMPERATURE_DATA_DESCRIPTOR, *PSTORAGE_TEMPERATURE_DATA_DESCRIPTOR;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

Contains the size of this structure, in bytes. The value of this member will change as members are added to the structure.

</dd> <dt>

**Size**
</dt> <dd>

Specifies the total size of the data returned, in bytes. This may include data that follows this structure.

</dd> <dt>

**CriticalTemperature**
</dt> <dd>

Indicates the minimum temperature in degrees Celsius that may prevent normal operation. Exceeding this temperature may result in possible data loss, automatic device shutdown, extreme performance throttling, or permanent damage.

</dd> <dt>

**WarningTemperature**
</dt> <dd>

Indicates the maximum temperature in degrees Celsius at which the device is capable of operating continuously without degrading operation or reliability.

</dd> <dt>

**InfoCount**
</dt> <dd>

Specifies the number of [**STORAGE\_TEMPERATURE\_INFO**](storage-temperature-info.md) structures reported in **TemperatureInfo**. More than one set of temperature data may be returned when there are multiple sensors in the drive.

</dd> <dt>

**Reserved0**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**TemperatureInfo\[ANYSIZE\_ARRAY\]**
</dt> <dd>

Device temperature data, of type [**STORAGE\_TEMPERATURE\_INFO**](storage-temperature-info.md).

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Client<br/> | Windows 10<br/>                                                                                      |
| Server<br/> | Windows Server 2016<br/>                                                                             |
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md)
</dt> <dt>

[**STORAGE\_PROPERTY\_QUERY**](storage-property-query.md)
</dt> <dt>

[**STORAGE\_PROPERTY\_ID**](storage-property-id.md)
</dt> <dt>

[**STORAGE\_TEMPERATURE\_INFO**](storage-temperature-info.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_TEMPERATURE_DATA_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






