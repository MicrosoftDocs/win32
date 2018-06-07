---
title: FEATURE\_DATA\_CD\_MASTERING structure
description: The FEATURE\_DATA\_CD\_MASTERING structure holds information for the CD Mastering feature.
ms.assetid: 340e9675-9d07-4224-ac1b-86e7586c0738
keywords:
- FEATURE_DATA_CD_MASTERING structure Storage Devices
- PFEATURE_DATA_CD_MASTERING structure pointer Storage Devices
topic_type:
- apiref
api_name:
- FEATURE_DATA_CD_MASTERING
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

# FEATURE\_DATA\_CD\_MASTERING structure

The FEATURE\_DATA\_CD\_MASTERING structure holds information for the CD Mastering feature.

## Syntax


```C++
typedef struct _FEATURE_DATA_CD_MASTERING {
  FEATURE_HEADER Header;
  UCHAR          RWSubchannelsRecordable  :1;
  UCHAR          CdRewritable  :1;
  UCHAR          TestWriteOk  :1;
  UCHAR          RawRecordingOk  :1;
  UCHAR          RawMultiSessionOk  :1;
  UCHAR          SessionAtOnceOk  :1;
  UCHAR          BufferUnderrunFree  :1;
  UCHAR          Reserved1  :1;
  UCHAR          MaximumCueSheetLength[3];
} FEATURE_DATA_CD_MASTERING, *PFEATURE_DATA_CD_MASTERING;
```



## Members

<dl> <dt>

**Header**
</dt> <dd>

Contains a [**FEATURE\_HEADER**](feature-header.md) structure with header information for this feature descriptor.

</dd> <dt>

**RWSubchannelsRecordable**
</dt> <dd>

Indicates, when set to 1, that the device can record the R-W subchannels with user-supplied information.

</dd> <dt>

**CdRewritable**
</dt> <dd>

Indicates, when set to 1, that the device can do mastering and TAO recording on rewritable media.

</dd> <dt>

**TestWriteOk**
</dt> <dd>

Indicates, when set to 1, that the device can perform test writes.

</dd> <dt>

**RawRecordingOk**
</dt> <dd>

Indicates, when set to 1, that the device can record using the raw write type.

</dd> <dt>

**RawMultiSessionOk**
</dt> <dd>

Indicates, when set to 1, that the device can record multisession in raw mode.

</dd> <dt>

**SessionAtOnceOk**
</dt> <dd>

Indicates, when set to 1, that the device can record using the Session-at-Once recording mode.

</dd> <dt>

**BufferUnderrunFree**
</dt> <dd>

Indicates, when set to 1, that the device is capable of zero-loss linking.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved.

</dd> <dt>

**MaximumCueSheetLength**
</dt> <dd>

Indicates the maximum length of a Cue Sheet that can be accepted by the device for Session at Once recording. **MaximumCueSheetLength**\[0\] holds the most significant byte of the 3-byte value for the length. **MaximumCueSheetLength**\[2\] holds the least significant byte.

</dd> </dl>

## Remarks

This structure holds data for the feature named "CD Mastering" by the *SCSI Multimedia - 4 (MMC-4)* specification. Devices that support this feature can write to a CD in either "Session-at-Once" mode or Raw mode.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20FEATURE_DATA_CD_MASTERING%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






