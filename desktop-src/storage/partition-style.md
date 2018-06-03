---
title: '\_PARTITION\_STYLE enumeration'
description: The PARTITION\_STYLE enumeration type indicates the type of partition table for a disk.
ms.assetid: 314bd92d-95de-453d-a9da-b0bef3dcb8e9
keywords:
- _PARTITION_STYLE enumeration Storage Devices
- PARTITION_STYLE enumeration Storage Devices
topic_type:
- apiref
api_name:
- PARTITION_STYLE
api_location:
- ntdddisk.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# \_PARTITION\_STYLE enumeration

The PARTITION\_STYLE enumeration type indicates the type of partition table for a disk.

## Syntax


```C++
typedef enum _PARTITION_STYLE { 
  PARTITION_STYLE_MBR  = 0,
  PARTITION_STYLE_GPT  = 1,
  PARTITION_STYLE_RAW  = 2
} PARTITION_STYLE;
```



## Constants

<dl> <dt>

<span id="PARTITION_STYLE_MBR"></span><span id="partition_style_mbr"></span>**PARTITION\_STYLE\_MBR**
</dt> <dd>

Specifies the traditional, AT-style Master Boot Record, type of partition table.

</dd> <dt>

<span id="PARTITION_STYLE_GPT"></span><span id="partition_style_gpt"></span>**PARTITION\_STYLE\_GPT**
</dt> <dd>

Specifies the GUID Partition Table type of partition table.

</dd> <dt>

<span id="PARTITION_STYLE_RAW"></span><span id="partition_style_raw"></span>**PARTITION\_STYLE\_RAW**
</dt> <dd></dd> </dl>

## Remarks

This enumeration is only defined for Windows XP and later.

The GUID Partition Table format conforms to the Extensible Firmware Interface (EFI) standard developed by Intel. For further information, see Intel's *Extensible Firmware Interface* specification.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**CREATE\_DISK**](create-disk.md)
</dt> <dt>

[**DISK\_PARTITION\_INFO**](disk-partition-info.md)
</dt> <dt>

[**PARTITION\_INFORMATION\_EX**](partition-information-ex.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20_PARTITION_STYLE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






