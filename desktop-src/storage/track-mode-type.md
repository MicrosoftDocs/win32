---
title: TRACK\_MODE\_TYPE enumeration
description: The TRACK\_MODE\_TYPE enumeration type is used in conjunction with the IOCTL\_CDROM\_RAW\_READ request and the RAW\_READ\_INFO structure to read data from a CD-ROM in raw mode.
ms.assetid: ea7d7b5a-625f-41f7-b3fd-96a6bf338db9
keywords:
- TRACK_MODE_TYPE enumeration Storage Devices
- PTRACK_MODE_TYPE enumeration pointer Storage Devices
topic_type:
- apiref
api_name:
- TRACK_MODE_TYPE
api_location:
- ntddcdrm.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# TRACK\_MODE\_TYPE enumeration

The TRACK\_MODE\_TYPE enumeration type is used in conjunction with the [**IOCTL\_CDROM\_RAW\_READ**](ioctl-cdrom-raw-read.md) request and the [**RAW\_READ\_INFO**](raw-read-info.md) structure to read data from a CD-ROM in raw mode.

## Syntax


```C++
typedef enum _TRACK_MODE_TYPE { 
  YellowMode2          = 0,
  XAForm2              = 1,
  CDDA                 = 2,
  RawWithC2AndSubCode  = 3,
  RawWithC2            = 4,
  RawWithSubCode       = 5
} TRACK_MODE_TYPE, *PTRACK_MODE_TYPE;
```



## Constants

<dl> <dt>

<span id="YellowMode2"></span><span id="yellowmode2"></span><span id="YELLOWMODE2"></span>**YellowMode2**
</dt> <dd>

Indicates that CD-ROM mode should be used. This mode is used with read-only 120 mm Optical Data Discs (CD-ROM). For more information, see the ISO/IEC 10149 specification.

</dd> <dt>

<span id="XAForm2"></span><span id="xaform2"></span><span id="XAFORM2"></span>**XAForm2**
</dt> <dd>

Indicates that compact disc read-only memory extended architecture mode should be used. For more information see the specification for CD-ROM XA published by NV Philips and Sony Corporation.

</dd> <dt>

<span id="CDDA"></span><span id="cdda"></span>**CDDA**
</dt> <dd>

Indicates that digital audio information mode should be used. For more information, see the IEC 908:1987 specification.

</dd> <dt>

<span id="RawWithC2AndSubCode"></span><span id="rawwithc2andsubcode"></span><span id="RAWWITHC2ANDSUBCODE"></span>**RawWithC2AndSubCode**
</dt> <dd>

CD\_RAW\_SECTOR\_WITH\_C2\_AND\_SUBCODE\_SIZE per sector

</dd> <dt>

<span id="RawWithC2"></span><span id="rawwithc2"></span><span id="RAWWITHC2"></span>**RawWithC2**
</dt> <dd>

CD\_RAW\_SECTOR\_WITH\_C2\_SIZE per sector

</dd> <dt>

<span id="RawWithSubCode"></span><span id="rawwithsubcode"></span><span id="RAWWITHSUBCODE"></span>**RawWithSubCode**
</dt> <dd>

CD\_RAW\_SECTOR\_WITH\_SUBCODE\_SIZE per sector

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_CDROM\_RAW\_READ**](ioctl-cdrom-raw-read.md)
</dt> <dt>

[**RAW\_READ\_INFO**](raw-read-info.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20TRACK_MODE_TYPE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






