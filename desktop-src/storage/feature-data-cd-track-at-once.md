---
title: FEATURE\_DATA\_CD\_TRACK\_AT\_ONCE structure
description: The FEATURE\_DATA\_CD\_TRACK\_AT\_ONCE structure holds information about the CD Track at Once feature.
ms.assetid: e3ce42a6-0d94-46cb-9831-c29f92a677cd
keywords:
- FEATURE_DATA_CD_TRACK_AT_ONCE structure Storage Devices
- PFEATURE_DATA_CD_TRACK_AT_ONCE structure pointer Storage Devices
topic_type:
- apiref
api_name:
- FEATURE_DATA_CD_TRACK_AT_ONCE
api_location:
- ntddmmc.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# FEATURE\_DATA\_CD\_TRACK\_AT\_ONCE structure

The FEATURE\_DATA\_CD\_TRACK\_AT\_ONCE structure holds information about the CD Track at Once feature.

## Syntax


```C++
typedef struct _FEATURE_DATA_CD_TRACK_AT_ONCE {
  FEATURE_HEADER Header;
  UCHAR          RWSubchannelsRecordable  :1;
  UCHAR          CdRewritable  :1;
  UCHAR          TestWriteOk  :1;
  UCHAR          RWSubchannelPackedOk  :1;
  UCHAR          RWSubchannelRawOk  :1;
  UCHAR          Reserved1  :1;
  UCHAR          BufferUnderrunFree  :1;
  UCHAR          Reserved3  :1;
  UCHAR          Reserved2;
  UCHAR          DataTypeSupported[2];
} FEATURE_DATA_CD_TRACK_AT_ONCE, *PFEATURE_DATA_CD_TRACK_AT_ONCE;
```



## Members

<dl> <dt>

**Header**
</dt> <dd>

Contains a [**FEATURE\_HEADER**](feature-header.md) structure with header information for this feature descriptor.

</dd> <dt>

**RWSubchannelsRecordable**
</dt> <dd>

Indicates, when set to 1, that the device can record the read/write subchannels with user-supplied data.

</dd> <dt>

**CdRewritable**
</dt> <dd>

Indicates, when set to 1, that the device supports overwriting a Track-at-Once track with another track's information.

</dd> <dt>

**TestWriteOk**
</dt> <dd>

Indicates, when set to 1, that the device can perform test writes.

</dd> <dt>

**RWSubchannelPackedOk**
</dt> <dd>

Indicates, when set to 1, that the device supports writing R-W sub code in the packed mode.

</dd> <dt>

**RWSubchannelRawOk**
</dt> <dd>

Indicates, when set to 1, that the device supports writing R-W sub code in the raw mode.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved.

</dd> <dt>

**BufferUnderrunFree**
</dt> <dd>

Indicates, when set to 1, that the device is capable of zero-loss linking.

</dd> <dt>

**Reserved3**
</dt> <dd>

Reserved.

</dd> <dt>

**Reserved2**
</dt> <dd>

Reserved.

</dd> <dt>

**DataTypeSupported**
</dt> <dd>

Indicates the data types that the device supports. See the *SCSI Multimedia 3* (*MMC-3*) specification for a description of the values that this member can take. **DataTypeSupported**\[0\] holds the most significant byte of value that indicates the data types. **DataTypeSupported**\[1\] holds the least significant byte of that value.

</dd> </dl>

## Remarks

This structure holds data for the feature named "CD Track at Once" by the *MMC-3* specification. Devices that support this feature can write data to a CD track.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20FEATURE_DATA_CD_TRACK_AT_ONCE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






