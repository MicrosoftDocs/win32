---
title: ATA\_CHANNEL\_STATE enumeration
description: The ATA\_CHANNEL\_STATE enumeration type indicates the state of the channel.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: 97df2db8-6a42-46d4-bc31-babb124635ee
keywords:
- ATA_CHANNEL_STATE enumeration Storage Devices
topic_type:
- apiref
api_name:
- ATA_CHANNEL_STATE
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

# ATA\_CHANNEL\_STATE enumeration

The ATA\_CHANNEL\_STATE enumeration type indicates the state of the channel.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef enum  { 
  ChannelStateDisabled  = 0,
  ChannelStateEnabled   = 1,
  ChannelStateUnKnown   = 2
} ATA_CHANNEL_STATE;
```



## Constants

<dl> <dt>

<span id="ChannelStateDisabled"></span><span id="channelstatedisabled"></span><span id="CHANNELSTATEDISABLED"></span>**ChannelStateDisabled**
</dt> <dd>

Indicates that the channel is disabled.

</dd> <dt>

<span id="ChannelStateEnabled"></span><span id="channelstateenabled"></span><span id="CHANNELSTATEENABLED"></span>**ChannelStateEnabled**
</dt> <dd>

Indicates that the channel is enabled.

</dd> <dt>

<span id="ChannelStateUnKnown"></span><span id="channelstateunknown"></span><span id="CHANNELSTATEUNKNOWN"></span>**ChannelStateUnKnown**
</dt> <dd>

Indicates that the state of the channel is unknown.

</dd> </dl>

## Remarks

The ATA\_CHANNEL\_STATE enumeration type is used in conjunction with the [**AtaControllerChannelEnabled**](atacontrollerchannelenabled.md) routine to determine whether the channel is enabled.

## Requirements



|                   |                                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Irb.h (include Irb.h)</dt> </dl> |



## See also

<dl> <dt>

[**AtaControllerChannelEnabled**](atacontrollerchannelenabled.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ATA_CHANNEL_STATE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






