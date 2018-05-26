---
title: IDE\_CHANNEL\_INTERFACE structure
description: The IDE\_CHANNEL\_INTERFACE structure contains interface information for the indicated channel.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: 0a742dc2-fa1a-4b93-a136-52f4571bde22
keywords:
- IDE_CHANNEL_INTERFACE structure Storage Devices
- PIDE_CHANNEL_INTERFACE structure pointer Storage Devices
topic_type:
- apiref
api_name:
- IDE_CHANNEL_INTERFACE
api_location:
- irb.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IDE\_CHANNEL\_INTERFACE structure

The IDE\_CHANNEL\_INTERFACE structure contains interface information for the indicated channel.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _IDE_CHANNEL_INTERFACE {
  USHORT            Version;
  UCHAR             ChannelNumber;
  UCHAR             Reserved;
  ULONG             ReservedUlong;
  IDE_HW_INITIALIZE IdeHwInitialize;
  IDE_HW_BUILDIO    IdeHwBuildIo;
  IDE_HW_STARTIO    IdeHwStartIo;
  IDE_HW_INTERRUPT  IdeHwInterrupt;
  IDE_HW_RESET      IdeHwReset;
  IDE_HW_CONTROL    IdeHwControl;
} IDE_CHANNEL_INTERFACE, *PIDE_CHANNEL_INTERFACE;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The port driver sets this member to sizeof(IDE\_CHANNEL\_INTERFACE). The miniport driver should verify that the version is greater than or equal to the one it is using.

</dd> <dt>

**ChannelNumber**
</dt> <dd>

The port driver sets this field to the number assigned for this channel. For non-native mode controllers, the primary channel will always be assigned 0 and the secondary channel will always be assigned 1.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved for future use. The miniport driver must not use this field.

</dd> <dt>

**ReservedUlong**
</dt> <dd> <dl> <dt>


</dt> <dt>


</dt> </dl> </dd> <dt>

**IdeHwInitialize**
</dt> <dd></dd> <dt>

**IdeHwBuildIo**
</dt> <dd></dd> <dt>

**IdeHwStartIo**
</dt> <dd></dd> <dt>

**IdeHwInterrupt**
</dt> <dd></dd> <dt>

**IdeHwReset**
</dt> <dd></dd> <dt>

**IdeHwControl**
</dt> <dd></dd> </dl>

## Remarks

## Requirements



|                   |                                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Irb.h (include Irb.h)</dt> </dl> |



## See also

<dl> <dt>

[**IdeHwInitialize**](idehwinitialize.md)
</dt> <dt>

[**IdeHwBuildIo**](idehwbuildio.md)
</dt> <dt>

[**IdeHwStartIo**](idehwstartio.md)
</dt> <dt>

[**IdeHwInterrupt**](idehwinterrupt.md)
</dt> <dt>

[**IdeHwReset**](idehwreset.md)
</dt> <dt>

[**IdeHwControl**](idehwcontrol.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IDE_CHANNEL_INTERFACE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






