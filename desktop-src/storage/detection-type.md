---
title: DETECTION\_TYPE enumeration
description: The DETECTION\_TYPE enumeration type is used in conjunction with the IOCTL\_DISK\_GET\_DRIVE\_GEOMETRY\_EX request and the DISK\_GEOMETRY\_EX structure to determine the type of formatting used by the BIOS to record the disk geometry.
ms.assetid: 3257a207-dd7e-4321-b037-95d62cea6f76
keywords:
- DETECTION_TYPE enumeration Storage Devices
topic_type:
- apiref
api_name:
- DETECTION_TYPE
api_location:
- ntdddisk.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DETECTION\_TYPE enumeration

The DETECTION\_TYPE enumeration type is used in conjunction with the [**IOCTL\_DISK\_GET\_DRIVE\_GEOMETRY\_EX**](ioctl-disk-get-drive-geometry-ex.md) request and the [**DISK\_GEOMETRY\_EX**](disk-geometry-ex.md) structure to determine the type of formatting used by the BIOS to record the disk geometry.

## Syntax


```C++
typedef enum _DETECTION_TYPE { 
  DetectNone     = 0,
  DetectInt13    = 1,
  DetectExInt13  = 2
} DETECTION_TYPE;
```



## Constants

<dl> <dt>

<span id="DetectNone"></span><span id="detectnone"></span><span id="DETECTNONE"></span>**DetectNone**
</dt> <dd>

Indicates that the disk contains neither an INT 13h partition nor an extended INT 13h partition.

</dd> <dt>

<span id="DetectInt13"></span><span id="detectint13"></span><span id="DETECTINT13"></span>**DetectInt13**
</dt> <dd>

Indicates that the disk has a standard INT 13h partition.

</dd> <dt>

<span id="DetectExInt13"></span><span id="detectexint13"></span><span id="DETECTEXINT13"></span>**DetectExInt13**
</dt> <dd>

Indicates that the disk contains an extended INT 13h partition.

</dd> </dl>

## Remarks

Possible formatting types are the standard INT 13h partition format or the extended INT 13h partition format.

## Requirements



|                   |                                                                                                                                    |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h, Ntddk.h, or Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**DISK\_DETECTION\_INFO**](disk-detection-info.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DETECTION_TYPE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






