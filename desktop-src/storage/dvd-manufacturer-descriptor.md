---
title: DVD\_MANUFACTURER\_DESCRIPTOR structure
description: The DVD\_MANUFACTURER\_DESCRIPTOR structure is used in conjunction with the IOCTL\_DVD\_READ\_STRUCTURE request to retrieve a DVD manufacturer descriptor.
ms.assetid: 19a65a8f-5272-424a-85b3-88074fb9e22f
keywords:
- DVD_MANUFACTURER_DESCRIPTOR structure Storage Devices
- PDVD_MANUFACTURER_DESCRIPTOR structure pointer Storage Devices
topic_type:
- apiref
api_name:
- DVD_MANUFACTURER_DESCRIPTOR
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

# DVD\_MANUFACTURER\_DESCRIPTOR structure

The DVD\_MANUFACTURER\_DESCRIPTOR structure is used in conjunction with the [**IOCTL\_DVD\_READ\_STRUCTURE**](ioctl-dvd-read-structure.md) request to retrieve a DVD manufacturer descriptor.

## Syntax


```C++
typedef struct _DVD_MANUFACTURER_DESCRIPTOR {
  UCHAR ManufacturingInformation[2048];
} DVD_MANUFACTURER_DESCRIPTOR, *PDVD_MANUFACTURER_DESCRIPTOR;
```



## Members

<dl> <dt>

**ManufacturingInformation**
</dt> <dd>

Contains an array holding the manufacturing information taken from the DVD media lead-in area. In the case of DVD-R multisession disc, this information is taken from the last border-in area.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdvd.h (include Ntddcdvd.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_DVD\_READ\_STRUCTURE**](ioctl-dvd-read-structure.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DVD_MANUFACTURER_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






