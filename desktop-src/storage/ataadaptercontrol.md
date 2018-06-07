---
title: AtaAdapterControl routine
description: The AtaAdapterControl miniport driver routine is called to perform Plug and Play (PnP) and Power Management operations on the HBA.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: 50125022-7450-4582-b98d-1d597e4e96d4
keywords:
- AtaAdapterControl routine Storage Devices
- IDE_ADAPTER_CONTROL
topic_type:
- apiref
api_name:
- AtaAdapterControl
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

# AtaAdapterControl routine

The *AtaAdapterControl* miniport driver routine is called to perform Plug and Play (PnP) and Power Management operations on the HBA.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
IDE_ADAPTER_CONTROL AtaAdapterControl;

BOOLEAN AtaAdapterControl(
  _In_    PVOID              ControllerExtension,
  _In_    IDE_CONTROL_ACTION ControlAction,
  _Inout_ PVOID              Parameters
)
{ ... }
```



## Parameters

<dl> <dt>

*ControllerExtension* \[in\]
</dt> <dd>

A pointer to the controller extension.

</dd> <dt>

*ControlAction* \[in\]
</dt> <dd>

One of five actions that the miniport driver must perform as defined in the following table.



| ControlAction               | Parameters                                | Description                                                                                                                                                                                                                                                                                                                     |
|-----------------------------|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IdeStart<br/>         | IDE\_CONTROLLER\_CONFIGURATION<br/> | Indicates that the adapter is being started. The miniport driver should update the member in the [**IDE\_CONTROLLER\_CONFIGURATION**](ide-controller-configuration.md) structure. If it is required, the miniport driver could obtain its hardware resources from the **IDE\_CONTROLLER\_CONFIGURATION** structure.<br/> |
| IdeStop<br/>          | None<br/>                           | The miniport driver should stop using any resources that are allocated for this controller. Be aware that the port driver guarantees that all the channels that are exposed by the adapter are stopped before it stops the adapter.<br/>                                                                                  |
| IdePowerUp<br/>       | None<br/>                           | Indicates that the adapter is being turned on. Anything that does not persist across a power cycle must be configured during IdePowerUp. <br/>                                                                                                                                                                            |
| IdePowerDown<br/>     | None<br/>                           | Indicates that the adapter is being turned off.<br/>                                                                                                                                                                                                                                                                      |
| IdeVendorDefined<br/> | None<br/>                           | Indicates that the miniport driver should perform a vendor-defined control action..<br/>                                                                                                                                                                                                                                  |



 

</dd> <dt>

*Parameters* \[in, out\]
</dt> <dd>

Parameters associated with the given action.

</dd> </dl>

## Return value

The miniport driver must return **TRUE** to acknowledge the completion of the requested action. A return value of **FALSE** indicates that the miniport driver was unable to complete the action successfully. A return value of **FALSE** for certain actions might cause the device installation to fail.

## Remarks

The port driver guarantees that there is no outstanding I/O on the adapter before it invokes the *AtaAdapterControl* routine.

## Requirements



|                            |                                                                                                  |
|----------------------------|--------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>               |
| Header<br/>          | <dl> <dt>Irb.h (include Irb.h)</dt> </dl> |



## See also

<dl> <dt>

[**IDE\_CONTROLLER\_CONFIGURATION**](ide-controller-configuration.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AtaAdapterControl%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






