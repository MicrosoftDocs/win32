---
title: FEATURE\_DATA\_REAL\_TIME\_STREAMING structure
description: The FEATURE\_DATA\_REAL\_TIME\_STREAMING structure holds information about the Real Time Streaming feature.
ms.assetid: 3b1b54cc-52a5-48ce-a637-70e289c1944e
keywords:
- FEATURE_DATA_REAL_TIME_STREAMING structure Storage Devices
- PFEATURE_DATA_REAL_TIME_STREAMING structure pointer Storage Devices
topic_type:
- apiref
api_name:
- FEATURE_DATA_REAL_TIME_STREAMING
api_location:
- ntddmmc.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FEATURE\_DATA\_REAL\_TIME\_STREAMING structure

The FEATURE\_DATA\_REAL\_TIME\_STREAMING structure holds information about the Real Time Streaming feature.

## Syntax


```C++
typedef struct _FEATURE_DATA_REAL_TIME_STREAMING {
  FEATURE_HEADER Header;
  UCHAR          StreamRecording  :1;
  UCHAR          WriteSpeedInGetPerf  :1;
  UCHAR          WriteSpeedInMP2A  :1;
  UCHAR          SetCDSpeed  :1;
  UCHAR          ReadBufferCapacityBlock  :1;
  UCHAR          Reserved1  :3;
  UCHAR          Reserved2[3];
} FEATURE_DATA_REAL_TIME_STREAMING, *PFEATURE_DATA_REAL_TIME_STREAMING;
```



## Members

<dl> <dt>

**Header**
</dt> <dd>

Contains a [**FEATURE\_HEADER**](feature-header.md) structure with header information for this feature descriptor.

</dd> <dt>

**StreamRecording**
</dt> <dd>

Indicates, when set to 1, that the device supports the stream recording operation. When set to zero, this bit indicates that the device might not support the stream recording operation.

</dd> <dt>

**WriteSpeedInGetPerf**
</dt> <dd>

Indicates, when set to 1, that the device supports the write speed data of the GET PERFORMANCE command and the WRC field of the SETSTREAMING command.

</dd> <dt>

**WriteSpeedInMP2A**
</dt> <dd>

Indicates, when set to 1, that the device supports CD/DVD capabilities & mechanical status mode page.

</dd> <dt>

**SetCDSpeed**
</dt> <dd>

Indicates, when set to 1, that the device supports the SET CD SPEED command. When set to zero, it indicates that the device does not support the SET CD SPEED command.

</dd> <dt>

**ReadBufferCapacityBlock**
</dt> <dd>

Indicates, when set to 1, that the device supports the READ BUFFERCAPACITY command.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved.

</dd> <dt>

**Reserved2**
</dt> <dd>

Reserved.

</dd> </dl>

## Remarks

This structure holds data for the feature named "Real Time Streaming" by the *SCSI Multimedia - 4 (MMC-4)* specification. Devices that support this feature allow the initiator to specify the performance level of the device within certain limits allowed by the device. These devices must also indicate to the initiator whether they support stream playback operations.

When queried, devices supporting this feature must return the information indicated in [**FEATURE\_HEADER**](feature-header.md). No other feature-specific information is required.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20FEATURE_DATA_REAL_TIME_STREAMING%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






