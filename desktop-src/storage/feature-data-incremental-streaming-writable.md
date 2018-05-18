---
title: FEATURE\_DATA\_INCREMENTAL\_STREAMING\_WRITABLE structure
description: The FEATURE\_DATA\_INCREMENTAL\_STREAMING\_WRITABLE structure contains information about the Incremental Streaming Writable feature.
ms.assetid: '5e3918a4-8cc6-45b9-acb1-3a2b2088d4b9'
keywords: ["FEATURE_DATA_INCREMENTAL_STREAMING_WRITABLE structure Storage Devices", "PFEATURE_DATA_INCREMENTAL_STREAMING_WRITABLE structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- FEATURE_DATA_INCREMENTAL_STREAMING_WRITABLE
api_location:
- ntddmmc.h
api_type:
- HeaderDef
---

# FEATURE\_DATA\_INCREMENTAL\_STREAMING\_WRITABLE structure

The FEATURE\_DATA\_INCREMENTAL\_STREAMING\_WRITABLE structure contains information about the Incremental Streaming Writable feature.

## Syntax


```C++
typedef struct _FEATURE_DATA_INCREMENTAL_STREAMING_WRITABLE {
  FEATURE_HEADER Header;
  UCHAR          DataTypeSupported[2];
  UCHAR          BufferUnderrunFree  :1;
  UCHAR          AddressModeReservation  :1;
  UCHAR          TrackRessourceInformation  :1;
  UCHAR          Reserved01  :5;
  UCHAR          NumberOfLinkSizes;
  UCHAR          LinkSize[];
} FEATURE_DATA_INCREMENTAL_STREAMING_WRITABLE, *PFEATURE_DATA_INCREMENTAL_STREAMING_WRITABLE;
```



## Members

<dl> <dt>

**Header**
</dt> <dd>

Contains a [**FEATURE\_HEADER**](feature-header.md) structure with header information for this feature descriptor.

</dd> <dt>

**DataTypeSupported**
</dt> <dd>

Indicates the supported data type. See the *SCSI Multimedia - 4 (MMC-4)* specification for an explanation of the values that this member can take. **DataTypeSupported**\[0\] must hold the most significant byte of the number of the data type. **DataTypeSupported**\[1\] must hold the least significant byte of the number.

</dd> <dt>

**BufferUnderrunFree**
</dt> <dd>

Indicates, when set to one, that the logical unit is capable of zero-loss linking.

</dd> <dt>

**AddressModeReservation**
</dt> <dd></dd> <dt>

**TrackRessourceInformation**
</dt> <dd></dd> <dt>

**Reserved01**
</dt> <dd></dd> <dt>

**NumberOfLinkSizes**
</dt> <dd>

Specifies the number of link sizes available for the current media. See the *MMC-3* specification for an explanation of the values that this member can take.

</dd> <dt>

**LinkSize**
</dt> <dd>

Contains an array that indicates the number of logical blocks per link.

</dd> </dl>

## Remarks

This structure holds data for the feature named "Incremental Streaming Writable" by the *MMC-3* specification. Devices that support this feature can write data to a contiguous region, and can append data to a limited number of locations on the media. On CD media, this is known as "packet recording" and on a DVD media it is known as "incremental recording".

## Requirements



|                   |                                                                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddmmc.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**FEATURE\_HEADER**](feature-header.md)
</dt> <dt>

[**FEATURE\_NUMBER**](feature-number.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20FEATURE_DATA_INCREMENTAL_STREAMING_WRITABLE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






