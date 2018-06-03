---
title: IDE\_CHANNEL\_CONFIGURATION structure
description: The IDE\_CHANNEL\_CONFIGURATION structure contains configuration information for the indicated channel.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: 1ca9a198-ac6b-4837-9503-68eb7ca36527
keywords:
- IDE_CHANNEL_CONFIGURATION structure Storage Devices
- PIDE_CHANNEL_CONFIGURATION structure pointer Storage Devices
topic_type:
- apiref
api_name:
- IDE_CHANNEL_CONFIGURATION
api_location:
- irb.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# IDE\_CHANNEL\_CONFIGURATION structure

The IDE\_CHANNEL\_CONFIGURATION structure contains configuration information for the indicated channel.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _IDE_CHANNEL_CONFIGURATION {
  USHORT                              Version;
  UCHAR                               ChannelNumber;
  SUPPORTED_ADVANCES                  SupportedAdvances;
  IDE_OPERATION_MODE                  ChannelMode;
  PIDE_MINIPORT_RESOURCES             ChannelResources;
  UCHAR                               NumberOfOverlappedRequests;
  UCHAR                               MaxTargetId;
  BOOLEAN                             SyncWithIsr;
  BOOLEAN                             SupportsWmi;
  PIDE_ADVANCED_CHANNEL_CONFIGURATION AdvancedChannelConfiguration;
} IDE_CHANNEL_CONFIGURATION, *PIDE_CHANNEL_CONFIGURATION;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The port driver sets this member to sizeof(IDE\_CHANNEL\_CONFIGURATION). The miniport driver should verify that the version is greater than or equal to the one it is using.

</dd> <dt>

**ChannelNumber**
</dt> <dd>

The port driver sets this field to the number assigned for this channel. For non-native mode controllers, the primary channel will always be assigned 0 and the secondary channel will always be assigned 1.

</dd> <dt>

**SupportedAdvances**
</dt> <dd> <dl> <dt>


</dt> <dt>


</dt> </dl> </dd> <dt>

**ChannelMode**
</dt> <dd>

The port driver sets this field to inform the ATA miniport which mode it is running at. There are three possible modes:



| Mode                           | Description                                                                                                                                                                                     |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IdeModeNormal <br/>      | This is the standard full capabilities mode where the ATA miniport may operate normally.<br/>                                                                                             |
| IdeModeDump,<br/>        | This is the limited no memory mode that an ATA miniport operates in during hibernate or crashdump. Call Back Routines and Registry Access Routines cannot be used when in this mode.<br/> |
| IdeModeRemovableBay<br/> | Similar to the IdeModeNormal, this indicates the ATA miniport must take extra steps to enable enumeration of devices that may have just been hotplugged onto a Parallel ATA bus.<br/>     |



 

</dd> <dt>

**ChannelResources**
</dt> <dd>

The port driver uses this pointer to pass miniport hardware resources to be used to access the HBA on a PCI bus.

</dd> <dt>

**NumberOfOverlappedRequests**
</dt> <dd>

The miniport driver should set this field to the number of requests the channel can handle at a time. By default, the port driver sets this to 1.

</dd> <dt>

**MaxTargetId**
</dt> <dd>

The miniport should set this member to the maximum target ID supported on this channel. Typically, this is 1 less than the maximum number of devices supported on the channel. By default, the port driver sets this is set to 1 to indicate that 2 devices are supported on a channel.

</dd> <dt>

**SyncWithIsr**
</dt> <dd>

Indicates support for unsynchronized I/O processing in the miniport driver. The miniport driver must set this member to **TRUE**.

</dd> <dt>

**SupportsWmi**
</dt> <dd>

Indicates support for WMI. The miniport driver must set this member to **TRUE**.

</dd> <dt>

**AdvancedChannelConfiguration**
</dt> <dd></dd> </dl>

## Remarks

## Requirements



|                   |                                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Irb.h (include Irb.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IDE_CHANNEL_CONFIGURATION%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





