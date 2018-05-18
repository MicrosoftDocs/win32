---
title: STORAGE\_TEMPERATURE\_THRESHOLD structure
description: This structure is used to set the over or under temperature threshold of a storage device (via IOCTL\_STORAGE\_SET\_TEMPERATURE\_THRESHOLD).
ms.assetid: '19096AD2-5149-4AE1-94CD-9004ED8C24DC'
keywords: ["STORAGE_TEMPERATURE_THRESHOLD structure Storage Devices", "PSTORAGE_TEMPERATURE_THRESHOLD structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- STORAGE_TEMPERATURE_THRESHOLD
api_location:
- ntddstor.h
api_type:
- HeaderDef
---

# STORAGE\_TEMPERATURE\_THRESHOLD structure

This structure is used to set the over or under temperature threshold of a storage device (via [**IOCTL\_STORAGE\_SET\_TEMPERATURE\_THRESHOLD**](ioctl-storage-set-temperature-threshold.md)).

## Syntax


```C++
typedef struct _STORAGE_TEMPERATURE_THRESHOLD {
  ULONG   Version;
  ULONG   Size;
  USHORT  Flags;
  USHORT  Index;
  SHORT   Threshold;
  BOOLEAN OverThreshold;
  UCHAR   Reserved;
} STORAGE_TEMPERATURE_THRESHOLD, *PSTORAGE_TEMPERATURE_THRESHOLD;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The version of the structure.

</dd> <dt>

**Size**
</dt> <dd>

The size of this structure. This should be set to sizeof(**STORAGE\_TEMPERATURE\_THRESHOLD**).

</dd> <dt>

**Flags**
</dt> <dd>

Flags set for this request. The following are valid flags.



| Flag                                                   | Description                                                             |
|--------------------------------------------------------|-------------------------------------------------------------------------|
| **STORAGE\_PROTOCOL\_COMMAND\_FLAG\_ADAPTER\_REQUEST** | This flag indicates the request to target an adapter instead of device. |



 

</dd> <dt>

**Index**
</dt> <dd>

Identifies the instance of temperature information. Starts from 0. Index 0 may indicate a composite value.

</dd> <dt>

**Threshold**
</dt> <dd>

A signed value that indicates the temperature of the threshold, in degrees Celsius.

</dd> <dt>

**OverThreshold**
</dt> <dd>

Indicates if the *Threshold* specifies the over or under temperature threshold. If **true**, set the **OverThreshold** temperature value of the device; otherwise, set the **UnderThreshold** temperature value.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved for future use.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Client<br/> | Windows 10<br/>                                                                                      |
| Server<br/> | Windows Server 2016<br/>                                                                             |
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_TEMPERATURE_THRESHOLD%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






