---
title: ATA\_ADDRESS\_TRANSLATION enumeration
description: The ATA\_ADDRESS\_TRANSLATION enumeration type indicates the type of address translation used during data transfers.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: 72fddd86-6e9f-4e75-af6a-e7f3e1064a8b
keywords:
- ATA_ADDRESS_TRANSLATION enumeration Storage Devices
topic_type:
- apiref
api_name:
- ATA_ADDRESS_TRANSLATION
api_location:
- irb.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ATA\_ADDRESS\_TRANSLATION enumeration

The ATA\_ADDRESS\_TRANSLATION enumeration type indicates the type of address translation used during data transfers.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef enum  { 
  UnknownMode   = 0,
  ChsMode       = 1,
  LbaMode       = 2,
  Lba48BitMode  = 3
} ATA_ADDRESS_TRANSLATION;
```



## Constants

<dl> <dt>

<span id="UnknownMode"></span><span id="unknownmode"></span><span id="UNKNOWNMODE"></span>**UnknownMode**
</dt> <dd></dd> <dt>

<span id="ChsMode"></span><span id="chsmode"></span><span id="CHSMODE"></span>**ChsMode**
</dt> <dd>

Indicates that sectors are to be addressed using cylinder/head/sector (CHS) values.

</dd> <dt>

<span id="LbaMode"></span><span id="lbamode"></span><span id="LBAMODE"></span>**LbaMode**
</dt> <dd>

Indicates that sectors are to be addressed using logical block addressing (LBA) values.

</dd> <dt>

<span id="Lba48BitMode"></span><span id="lba48bitmode"></span><span id="LBA48BITMODE"></span>**Lba48BitMode**
</dt> <dd>

Indicates support for 48-bit LBAs.

</dd> </dl>

## Requirements



|                   |                                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Irb.h (include Irb.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ATA_ADDRESS_TRANSLATION%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





