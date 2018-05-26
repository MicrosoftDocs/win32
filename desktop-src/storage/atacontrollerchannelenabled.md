---
title: AtaControllerChannelEnabled routine
description: The AtaControllerChannelEnabled miniport driver routine indicates whether the specified channel is enabled.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: 67713537-6a5b-4108-8af9-fb5d16844b03
keywords:
- AtaControllerChannelEnabled routine Storage Devices
- IDE_CHANNEL_ENABLED
topic_type:
- apiref
api_name:
- AtaControllerChannelEnabled
api_location:
- irb.h
api_type:
- UserDefined
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AtaControllerChannelEnabled routine

The ***AtaControllerChannelEnabled*** miniport driver routine indicates whether the specified channel is enabled.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
IDE_CHANNEL_ENABLED AtaControllerChannelEnabled;

ATA_CHANNEL_STATE AtaControllerChannelEnabled(
  _In_ PVOID ControllerExtension,
  _In_ ULONG ChannelNumber
)
{ ... }
```



## Parameters

<dl> <dt>

*ControllerExtension* \[in\]
</dt> <dd>

A pointer to the controller extension.

</dd> <dt>

*ChannelNumber* \[in\]
</dt> <dd>

Specifies the channel number whose state will be determined.

</dd> </dl>

## Return value

***AtaControllerChannelEnabled*** returns an enumerator value of type [**ATA\_CHANNEL\_STATE**](ata-channel-state.md), which can have any of the following values:



| Return code                                                                                         | Description                                                                 |
|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <dl> <dt>**ChannelStateEnabled**</dt> </dl>  | Indicates that the specified channel is enabled. <br/>                |
| <dl> <dt>**ChannelStateDisabled**</dt> </dl> | Indicates that the specified channel is disabled.<br/>                |
| <dl> <dt>**ChannelStateUnKnown**</dt> </dl>  | Indicates that the state of the channel could not be determined.<br/> |



 

## Remarks

The following sequence describes how the miniport driver and the port driver interact to determine which controller channels are enabled:

1.  The port driver calls the miniport driver's ***AtaAdapterControl*** routine with control action **IdeStart**.

2.  While the miniport driver processes the ***AtaAdapterControl*** routine with control action **IdeStart**, it initializes the **NumberOfChannels** member of [**IDE\_CONTROLLER\_CONFIGURATION**](ide-controller-configuration.md) to indicate the number of channels that are enabled.

3.  After the ***AtaAdapterControl*** routine returns, the port driver calls **AtaControllerChannelEnabled** one time for every NumberOfChannels specified in the ControllerConfiguration structure that are returned by ***AtaAdapterControl***.

This routine should not have steps that are critical to the operation of the controller. There are situations, such as during a crashdump operation, where this function will not be called at all. Additionally, this function is not called when a channel is restarted, only when PCIIDEx responds to a QueryDeviceRelations IRP.

**AtaControllerChannelEnabled** is an optional routine. If the miniport driver does not implement this routine, the port driver will load a default handler. If the port driver loads a default handler, all channels that are specified by NumberOfChannels in the ControllerConfiguration structure that is returned by [**AtaAdapterControl**](ataadaptercontrol.md) when handling an IdeStart action are assumed to be enabled. This routine enables PCIIDEx to load the ATA port driver for only the channels enabled. Doing this allows for sparse channel support (for example, channel 0, channel 1, channel 3, channel 4, and channel 6, but not channel 2 and channel 5).

## Requirements



|                            |                                                                                                  |
|----------------------------|--------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>               |
| Header<br/>          | <dl> <dt>Irb.h (include Irb.h)</dt> </dl> |



## See also

<dl> <dt>

[**IDE\_CONTROLLER\_CONFIGURATION**](ide-controller-configuration.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AtaControllerChannelEnabled%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






