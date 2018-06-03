---
title: DVD\_REGION structure
description: The DVD\_REGION structure is used in conjunction with the IOCTL\_DVD\_GET\_REGION request to retrieve region playback control (RPC) information for a DVD device.
ms.assetid: a2e31a1a-59e4-4a83-b866-944ef1693f65
keywords:
- DVD_REGION structure Storage Devices
- PDVD_REGION structure pointer Storage Devices
topic_type:
- apiref
api_name:
- DVD_REGION
api_location:
- ntddcdvd.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# DVD\_REGION structure

The DVD\_REGION structure is used in conjunction with the [**IOCTL\_DVD\_GET\_REGION**](ioctl-dvd-get-region.md) request to retrieve region playback control (RPC) information for a DVD device.

## Syntax


```C++
typedef struct _DVD_REGION {
  UCHAR CopySystem;
  UCHAR RegionData;
  UCHAR SystemRegion;
  UCHAR ResetCount;
} DVD_REGION, *PDVD_REGION;
```



## Members

<dl> <dt>

**CopySystem**
</dt> <dd>

Indicates the copyright protection type. For more information about copyright protection types, see the *SCSI Multimedia Commands - 3* (MMC-3) specification.

</dd> <dt>

**RegionData**
</dt> <dd>

Indicates the region code of the currently mounted DVD media. This is an eight-bit bitmask, with one bit for each DVD region. A value of 0x00 means that no region is specified.

</dd> <dt>

**SystemRegion**
</dt> <dd>

Indicates the region code of the DVD player. This is an eight-bit bitmask, with one bit for each system region. A value of 0x00 means that no region is specified.

</dd> <dt>

**ResetCount**
</dt> <dd>

Indicates the remaining number of times the DVD device's region code can be changed by the user. This member can hold a value between 0 and 7.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdvd.h (include Ntddcdvd.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_DVD\_GET\_REGION**](ioctl-dvd-get-region.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DVD_REGION%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






