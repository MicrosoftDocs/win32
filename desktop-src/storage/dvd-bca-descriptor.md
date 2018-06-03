---
title: DVD\_BCA\_DESCRIPTOR structure
description: The DVD\_BCA\_DESCRIPTOR structure is used in conjunction with the IOCTL\_DVD\_READ\_STRUCTURE request to retrieve a DVD burst cutting area (BCA) descriptor.
ms.assetid: a573beb8-7019-4605-ab37-5871f67c585d
keywords:
- DVD_BCA_DESCRIPTOR structure Storage Devices
- PDVD_BCA_DESCRIPTOR structure pointer Storage Devices
topic_type:
- apiref
api_name:
- DVD_BCA_DESCRIPTOR
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

# DVD\_BCA\_DESCRIPTOR structure

The DVD\_BCA\_DESCRIPTOR structure is used in conjunction with the [**IOCTL\_DVD\_READ\_STRUCTURE**](ioctl-dvd-read-structure.md) request to retrieve a DVD burst cutting area (BCA) descriptor.

## Syntax


```C++
typedef struct _DVD_BCA_DESCRIPTOR {
  UCHAR BCAInformation[];
} DVD_BCA_DESCRIPTOR, *PDVD_BCA_DESCRIPTOR;
```



## Members

<dl> <dt>

**BCAInformation**
</dt> <dd>

Contains an array that holds vendor-defined information retrieved from the burst cutting area.

</dd> </dl>

## Remarks

The contents of the BCA region are specified by the media manufacturer.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdvd.h (include Ntddcdvd.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_DVD\_READ\_STRUCTURE**](ioctl-dvd-read-structure.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DVD_BCA_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






