---
title: STORAGE\_TEMPERATURE\_INFO structure
description: Describes device temperature data. Returned as part of STORAGE\_TEMPERATURE\_DATA\_DESCRIPTOR when querying for temperature data with an IOCTL\_STORAGE\_QUERY\_PROPERTY request.
ms.assetid: 1B7C68BF-78AE-4427-B5DC-E388CB5FAC0C
keywords:
- STORAGE_TEMPERATURE_INFO structure Storage Devices
- PSTORAGE_TEMPERATURE_INFO structure pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_TEMPERATURE_INFO
api_location:
- ntddstor.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# STORAGE\_TEMPERATURE\_INFO structure

Describes device temperature data. Returned as part of [**STORAGE\_TEMPERATURE\_DATA\_DESCRIPTOR**](storage-temperature-data-descriptor.md) when querying for temperature data with an [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) request.

## Syntax


```C++
typedef struct _STORAGE_TEMPERATURE_INFO {
  WORD    Index;
  SHORT   Temperature;
  SHORT   OverThreshold;
  SHORT   UnderThreshold;
  BOOLEAN OverThresholdChangable;
  BOOLEAN UnderThresholdChangable;
  BOOLEAN EventGenerated;
  UCHAR   Reserved0;
  ULONG   Reserved1;
} STORAGE_TEMPERATURE_INFO, *PSTORAGE_TEMPERATURE_INFO;
```



## Members

<dl> <dt>

**Index**
</dt> <dd>

Identifies the instance of temperature information. Starts from 0. Index 0 may indicate a composite value.

</dd> <dt>

**Temperature**
</dt> <dd>

A signed value that indicates the current temperature, in degrees Celsius.

</dd> <dt>

**OverThreshold**
</dt> <dd>

A signed value that specifies the maximum temperature within the desired threshold, in degrees Celsius.

</dd> <dt>

**UnderThreshold**
</dt> <dd>

A signed value that specifies the minimum temperature within the desired threshold, in degrees Celsius.

</dd> <dt>

**OverThresholdChangable**
</dt> <dd>

Indicates if *OverThreshold* can be changed by using [**IOCTL\_STORAGE\_SET\_TEMPERATURE\_THRESHOLD**](ioctl-storage-set-temperature-threshold.md).

</dd> <dt>

**UnderThresholdChangable**
</dt> <dd>

Indicates if *UnderThreshold* can be changed by using [**IOCTL\_STORAGE\_SET\_TEMPERATURE\_THRESHOLD**](ioctl-storage-set-temperature-threshold.md).

</dd> <dt>

**EventGenerated**
</dt> <dd>

Indicates if a notification will be generated when the current temperature crosses a threshold.

</dd> <dt>

**Reserved0**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved for future use.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_TEMPERATURE_INFO%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






