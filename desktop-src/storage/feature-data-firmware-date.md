---
title: FEATURE\_DATA\_FIRMWARE\_DATE structure
description: The FEATURE\_DATA\_FIRMWARE\_DATE structure holds the date information associated with the Firmware Information feature.
ms.assetid: 1f6c6a37-9510-47bc-b507-b3fd7477b432
keywords:
- FEATURE_DATA_FIRMWARE_DATE structure Storage Devices
- PFEATURE_DATA_FIRMWARE_DATE structure pointer Storage Devices
topic_type:
- apiref
api_name:
- FEATURE_DATA_FIRMWARE_DATE
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

# FEATURE\_DATA\_FIRMWARE\_DATE structure

The FEATURE\_DATA\_FIRMWARE\_DATE structure holds the date information associated with the Firmware Information feature.

## Syntax


```C++
typedef struct _FEATURE_DATA_FIRMWARE_DATE {
  FEATURE_HEADER Header;
  UCHAR          Year[4];
  UCHAR          Month[2];
  UCHAR          Day[2];
  UCHAR          Hour[2];
  UCHAR          Minute[2];
  UCHAR          Seconds[2];
  UCHAR          Reserved[2];
} FEATURE_DATA_FIRMWARE_DATE, *PFEATURE_DATA_FIRMWARE_DATE;
```



## Members

<dl> <dt>

**Header**
</dt> <dd>

Contains a [**FEATURE\_HEADER**](feature-header.md) structure with header information for this feature descriptor.

</dd> <dt>

**Year**
</dt> <dd>

Contains the two low order decimal digits represented as ASCII characters that indicate the year. For example, if the year is 2013, the **Year** member will contain characters "33" (a hexadecimal value of 0x3133).

</dd> <dt>

**Month**
</dt> <dd>

Contains two decimal digits represented as ASCII characters that indicate the month. For example, if the month is August, the **Month** member will contain characters "08" (a hexadecimal value of 0x3038).

</dd> <dt>

**Day**
</dt> <dd>

Contains two decimal digits represented as ASCII characters that indicate the day. For example, if the day is August 12, the **Day** member will contain characters "12" (a hexadecimal value of 0x3132).

</dd> <dt>

**Hour**
</dt> <dd>

Contains two decimal digits represented as ASCII characters that indicate the hour. For example, if the time 1:20:43 PM, the **Hour** member will contain the characters "13" (hexadecimal value of 0x3133).

</dd> <dt>

**Minute**
</dt> <dd>

Contains two decimal digits represented as ASCII characters that indicates the minute of the hour. For example, if the time 1:20:43 PM, the **Minute** member will contain the characters "20" (hexadecimal value of 0x3230).

</dd> <dt>

**Seconds**
</dt> <dd>

Contains two decimal digits represented as ASCII characters that indicates the minute of the hour. For example, if the time 1:20:43 PM, the **Seconds** member will contain the characters "43" (hexadecimal value of 0x3433).

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> </dl>

## Remarks

The structure holds the date information associated with the feature named "Firmware Information" by the *SCSI Multimedia - 4* (*MMC-4*) specification. Devices that support this feature can be queried for the date and Greenwich Mean Time (GMT) of the creation of the firmware revision currently loaded on the device.

## Requirements



|                   |                                                                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddmmc.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**FEATURE\_HEADER**](feature-header.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20FEATURE_DATA_FIRMWARE_DATE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






