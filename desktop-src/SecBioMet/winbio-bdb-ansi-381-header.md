---
title: WINBIO_BDB_ANSI_381_HEADER structure (Winbio\_types.h)
description: Specifies information about a series of fingerprint or palm samples.
ms.assetid: 8b0caa50-9bba-45c4-b4bf-514540894793
keywords:
- WINBIO_BDB_ANSI_381_HEADER structure Windows Biometric Framework API
topic_type:
- apiref
api_name:
- WINBIO_BDB_ANSI_381_HEADER
api_location:
- Winbio_types.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WINBIO\_BDB\_ANSI\_381\_HEADER structure

The **WINBIO\_BDB\_ANSI\_381\_HEADER** structure specifies information about a series of fingerprint or palm samples.

## Syntax


```C++
typedef struct _WINBIO_BDB_ANSI_381_HEADER {
  ULONG64                  RecordLength;
  ULONG                    FormatIdentifier;
  ULONG                    VersionNumber;
  WINBIO_REGISTERED_FORMAT ProductId;
  USHORT                   CaptureDeviceId;
  USHORT                   ImageAcquisitionLevel;
  USHORT                   HorizontalScanResolution;
  USHORT                   VerticalScanResolution;
  USHORT                   HorizontalImageResolution;
  USHORT                   VerticalImageResolution;
  UCHAR                    ElementCount;
  UCHAR                    ScaleUnits;
  UCHAR                    PixelDepth;
  UCHAR                    ImageCompressionAlg;
  USHORT                   Reserved;
} WINBIO_BDB_ANSI_381_HEADER;
```



## Members

<dl> <dt>

**RecordLength**
</dt> <dd>

The size, in bytes, of this structure plus the size of all [**WINBIO\_BDB\_ANSI\_381\_RECORD**](winbio-bdb-ansi-381-record.md) structures for the fingerprint or palm samples captured from an end user. Only the low six bytes are valid.

</dd> <dt>

**FormatIdentifier**
</dt> <dd>

Specifies the format. Currently, this must be 0x46495200.

</dd> <dt>

**VersionNumber**
</dt> <dd>

Specifies the version number. Currently this must be 0x30313000 which corresponds internally to 0.1.0.0.

</dd> <dt>

**ProductId**
</dt> <dd>

A [**WINBIO\_REGISTERED\_FORMAT**](winbio-registered-format.md) structure that contains the registered data format as an owner/type pair.

</dd> <dt>

**CaptureDeviceId**
</dt> <dd>

Contains the unit ID of the device used to capture the sample.

</dd> <dt>

**ImageAcquisitionLevel**
</dt> <dd>

Specifies the resolution level at which the sample is captured.

</dd> <dt>

**HorizontalScanResolution**
</dt> <dd>

Specifies the horizontal resolution of the scan.

</dd> <dt>

**VerticalScanResolution**
</dt> <dd>

Specifies the vertical resolution of the scan.

</dd> <dt>

**HorizontalImageResolution**
</dt> <dd>

Specifies the horizontal resolution of the captured fingerprint or palm image.

</dd> <dt>

**VerticalImageResolution**
</dt> <dd>

Specifies the vertical resolution of the captured fingerprint or palm image.

</dd> <dt>

**ElementCount**
</dt> <dd>

Number of finger or palm records in this structure.

</dd> <dt>

**ScaleUnits**
</dt> <dd>

Contains the unit of measure, 1 for inches and 2 for centimeters.

</dd> <dt>

**PixelDepth**
</dt> <dd>

Specifies the number of bits in a pixel. This can be 1 to 16 bits per pixel for color.

</dd> <dt>

**ImageCompressionAlg**
</dt> <dd>

Specifies the algorithm used to compress the finger or palm image.

</dd> <dt>

**Reserved**
</dt> <dd></dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                       |
| Header<br/>                   | <dl> <dt>Winbio\_types.h (include Winbio.h)</dt> </dl> |



## See also

<dl> <dt>

[Client Application Structures](client-application-structures.md)
</dt> </dl>

 

 





