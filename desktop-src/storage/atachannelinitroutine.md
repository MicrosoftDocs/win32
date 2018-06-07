---
title: AtaChannelInitRoutine routine
description: The AtaChannelInitRoutine miniport driver routine initializes the miniport driver's channel interface.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: c59f93cc-d182-4764-a207-0799e55c6cf6
keywords:
- AtaChannelInitRoutine routine Storage Devices
- IDE_CHANNEL_INIT
topic_type:
- apiref
api_name:
- AtaChannelInitRoutine
api_location:
- irb.h
api_type:
- UserDefined
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AtaChannelInitRoutine routine

The ***AtaChannelInitRoutine*** miniport driver routine initializes the miniport driver's channel interface.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
IDE_CHANNEL_INIT AtaChannelInitRoutine;

BOOLEAN AtaChannelInitRoutine(
  _In_    PVOID                  ChannelExtension,
  _Inout_ PIDE_CHANNEL_INTERFACE ChannelInterface,
  _Inout_ PVOID                  Context
)
{ ... }
```



## Parameters

<dl> <dt>

*ChannelExtension* \[in\]
</dt> <dd>

A pointer to the miniport driver channel extension.

</dd> <dt>

*ChannelInterface* \[in, out\]
</dt> <dd>

A pointer to a structure of type [**IDE\_CHANNEL\_INTERFACE**](ide-channel-interface.md).

</dd> <dt>

*Context* \[in, out\]
</dt> <dd>

A pointer to the controller extension.

</dd> </dl>

## Return value

***AtaChannelInitRoutine*** returns **TRUE** if the initialization succeeded. It returns **FALSE** if the initialization failed.

## Remarks

A vendor-supplied miniport driver that supports the channel interface must implement an ***AtaChannelInitRoutine*** routine to initialize the controller's channels. In particular, the ***AtaChannelInitRoutine*** routine must complete the initialization of the [**IDE\_CHANNEL\_INTERFACE**](ide-channel-interface.md) structure. The following sequence describes how the miniport driver and the port driver interact to initialize a channel:

1.  While in its [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine, the miniport driver calls the port driver's [**AtaPortInitializeEx**](ataportinitializeex.md) library routine to launch the initialization of the controller and the miniport driver.

2.  If the miniport driver supports the channel interface, the ***DriverEntry*** routine must initialize the **AtaChannelInitRoutine** member of [**IDE\_CONTROLLER\_INTERFACE**](ide-controller-interface.md) to point to the miniport driver's ***AtaChannelInitRoutine*** routine.

3.  The port driver calls the ***AtaAdapterControl*** routine by using control action IdeStart. ***AtaChannelInitRoutine*** is called one time for every NumberOfChannels specified in the ControllerConfiguration structure that is returned by the ***AtaAdapterControl*** routine when ***AtaAdapterControl*** handles an **IdeStart** action.

## Requirements



|                            |                                                                                                  |
|----------------------------|--------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>               |
| Header<br/>          | <dl> <dt>Irb.h (include Irb.h)</dt> </dl> |



## See also

<dl> <dt>

[**AtaPortInitializeEx**](ataportinitializeex.md)
</dt> <dt>

[**IDE\_CHANNEL\_INTERFACE**](ide-channel-interface.md)
</dt> <dt>

[**IDE\_CONTROLLER\_INTERFACE**](ide-controller-interface.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AtaChannelInitRoutine%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






