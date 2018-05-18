---
title: FEATURE\_DATA\_CD\_READ structure
description: The FEATURE\_DATA\_CD\_READ structure contains information about the CD Read feature.
ms.assetid: '55d63dcc-7728-4982-ad1c-e1ca40cc941e'
keywords: ["FEATURE_DATA_CD_READ structure Storage Devices", "PFEATURE_DATA_CD_READ structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- FEATURE_DATA_CD_READ
api_location:
- ntddmmc.h
api_type:
- HeaderDef
---

# FEATURE\_DATA\_CD\_READ structure

The FEATURE\_DATA\_CD\_READ structure contains information about the CD Read feature.

## Syntax


```C++
typedef struct _FEATURE_DATA_CD_READ {
  FEATURE_HEADER Header;
  UCHAR          CDText  :1;
  UCHAR          C2ErrorData  :1;
  UCHAR          Reserved01  :5;
  UCHAR          DigitalAudioPlay  :1;
  UCHAR          Reserved2[3];
} FEATURE_DATA_CD_READ, *PFEATURE_DATA_CD_READ;
```



## Members

<dl> <dt>

**Header**
</dt> <dd>

Contains a [**FEATURE\_HEADER**](feature-header.md) structure with header information for this feature descriptor.

</dd> <dt>

**CDText**
</dt> <dd>

Indicates, when set to 1, that the device supports format code 0x05 of the READ/TOC/PMA/ATIP command, as defined in the *SCSI Multimedia - 4 (MMC-4)* specification. When set to zero, CD-Text is not supported.

</dd> <dt>

**C2ErrorData**
</dt> <dd>

Indicates, when set to 1, that the device supports the C2 error pointers as described in the *MMC-3* specification. When set to zero, it indicates that the device does not support C2 error pointers.

</dd> <dt>

**Reserved01**
</dt> <dd></dd> <dt>

**DigitalAudioPlay**
</dt> <dd></dd> <dt>

**Reserved2**
</dt> <dd>

Reserved.

</dd> </dl>

## Remarks

This structure holds data for the feature named "CD Read" by the *MMC-3* specification. Devices that support this feature can read CD-specific information from the media and can read user data from all types of CD blocks.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20FEATURE_DATA_CD_READ%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






