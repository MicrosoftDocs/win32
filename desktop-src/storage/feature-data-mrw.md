---
title: FEATURE\_DATA\_MRW structure
description: The FEATURE\_DATA\_MRW structure contains information about the MRW feature.
ms.assetid: af0c8c50-c5a0-4395-a608-fced6ac3cfe5
keywords:
- FEATURE_DATA_MRW structure Storage Devices
- PFEATURE_DATA_MRW structure pointer Storage Devices
topic_type:
- apiref
api_name:
- FEATURE_DATA_MRW
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

# FEATURE\_DATA\_MRW structure

The FEATURE\_DATA\_MRW structure contains information about the MRW feature.

## Syntax


```C++
typedef struct _FEATURE_DATA_MRW {
  FEATURE_HEADER Header;
  UCHAR          Write  :1;
  UCHAR          DvdPlusRead  :1;
  UCHAR          DvdPlusWrite  :1;
  UCHAR          Reserved01  :5;
  UCHAR          Reserved2[3];
} FEATURE_DATA_MRW, *PFEATURE_DATA_MRW;
```



## Members

<dl> <dt>

**Header**
</dt> <dd>

Contains a [**FEATURE\_HEADER**](feature-header.md) structure with header information for this feature descriptor.

</dd> <dt>

**Write**
</dt> <dd>

Indicates, if set to 1, that the device can format discs using the MRW format and write to discs that have been formatted in this manner. See the *SCSI Multimedia - 4 (MMC-4)* specification for more information.

</dd> <dt>

**DvdPlusRead**
</dt> <dd></dd> <dt>

**DvdPlusWrite**
</dt> <dd></dd> <dt>

**Reserved01**
</dt> <dd></dd> <dt>

**Reserved2**
</dt> <dd>

Reserved.

</dd> </dl>

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20FEATURE_DATA_MRW%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






