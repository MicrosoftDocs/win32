---
title: AtaPortInitializeEx routine
description: The AtaPortInitializeEx ATA port driver library routine initializes the port and miniport drivers.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: 578992cf-63eb-4b8e-b0cb-9caee5c534e1
keywords:
- AtaPortInitializeEx routine Storage Devices
topic_type:
- apiref
api_name:
- AtaPortInitializeEx
api_location:
- Pciidex.lib
- Pciidex.dll
api_type:
- LibDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AtaPortInitializeEx routine

The **AtaPortInitializeEx** ATA port driver library routine initializes the port and miniport drivers.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
ULONG AtaPortInitializeEx(
  _In_ PVOID                     DriverObject,
  _In_ PVOID                     RegistryPath,
  _In_ PIDE_CONTROLLER_INTERFACE ControllerInterface
);
```



## Parameters

<dl> <dt>

*DriverObject* \[in\]
</dt> <dd>

A pointer to the miniport driver object.

</dd> <dt>

*RegistryPath* \[in\]
</dt> <dd>

Contains a Unicode string that indicates the location in the registry where the miniport driver configuration information is stored.

</dd> <dt>

*ControllerInterface* \[in\]
</dt> <dd>

Contains the entry points for the ***AtaAdapterControl***, ***AtaChannelInitRoutine***, ***AtaControllerChannelEnabled***, and ***AtaControllerTransferModeSelect*** routines.

</dd> </dl>

## Return value

**AtaPortInitializeEx** returns STATUS\_SUCCESS if the operation succeeds. Otherwise, it returns an error code.

## Remarks

The **AtaPortInitializeEx** routine initializes key data structures that are used by the port and miniport drivers. It also starts the initialization of the controller's channels. The following sequence describes the principal actions taken by this routine:

1.  While in its [**DriverEntry**](driverentry.md) routine, the miniport driver calls the port driver's **AtaPortInitializeEx** library routine and passes it the following key parameters:
    -   *ControllerInterface*: Contains the entry points for the ***AtaAdapterControl***, ***AtaChannelInitRoutine***, ***AtaControllerChannelEnabled***, and ***AtaControllerTransferModeSelect*** routines.
2.  The **AtaPortInitializeEx** routine initializes key data structures that are used by the port and miniport drivers and performs the following actions:
    1.  Initializes the miniport driver's dispatch tables.
    2.  Allocates an extension for the driver object.
    3.  Copies ControllerInterface into the driver extension.
    4.  After ***AtaPortInitializeEx*** completes the initialization of the port driver, it returns to the miniport driver's ***DriverEntry*** routine.
3.  While starting the adapter device, the miniport driver routine ***AtaAdapterControl*** will be called by the port driver with control action **IdeStart**.

4.  When the ATA port driver is processing a channel device start request, the miniport driver routine [**AtaControllerChannelEnabled**](atacontrollerchannelenabled.md) is called for each channel on the controller to determine whether it is enabled.

5.  After the [**AtaControllerChannelEnabled**](atacontrollerchannelenabled.md) routine determines which channels are enabled, the ATA port driver calls [**AtaChannelInitRoutine**](atachannelinitroutine.md) for this channel.

## Requirements



|                            |                                                                                                           |
|----------------------------|-----------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                        |
| Header<br/>          | <dl> <dt>Irb.h (include Ata.h or Irb.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Pciidex.lib</dt> </dl>                    |



## See also

<dl> <dt>

[**AtaChannelInitRoutine**](atachannelinitroutine.md)
</dt> <dt>

[**AtaControllerChannelEnabled**](atacontrollerchannelenabled.md)
</dt> <dt>

[**DriverEntry**](driverentry.md)
</dt> <dt>

[**IDE\_CONTROLLER\_CONFIGURATION**](ide-controller-configuration.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AtaPortInitializeEx%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






