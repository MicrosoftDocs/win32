---
title: IdeHwInitialize routine
description: The IdeHwInitialize miniport driver routine configures the indicated device.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: 5665ff0a-3cbf-4ac5-adf7-5b383bac5117
keywords:
- IdeHwInitialize routine Storage Devices
- IDE_HW_INITIALIZE
topic_type:
- apiref
api_name:
- IdeHwInitialize
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

# IdeHwInitialize routine

The ***IdeHwInitialize*** miniport driver routine configures the indicated device.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
IDE_HW_INITIALIZE IdeHwInitialize;

BOOLEAN IdeHwInitialize(
  _In_    PVOID                  ChannelExtension,
  _Inout_ PIDE_DEVICE_PARAMETERS DeviceParameters,
  _In_    PIDENTIFY_DEVICE_DATA  IdentifyData
)
{ ... }
```



## Parameters

<dl> <dt>

*ChannelExtension* \[in\]
</dt> <dd>

A pointer to the miniport driver per channel device extension.

</dd> <dt>

*DeviceParameters* \[in, out\]
</dt> <dd>

A pointer to a structure of type [**IDE\_DEVICE\_PARAMETERS**](ide-device-parameters.md) that identifies the device to configure and the device parameters with which to configure the device.

</dd> <dt>

*IdentifyData* \[in\]
</dt> <dd>

A pointer to a structure of type [**IDENTIFY\_DEVICE\_DATA**](identify-device-data.md) that contains the identify data that is returned by the device.

</dd> </dl>

## Return value

***IdeHwInitialize*** returns **TRUE** if the operation succeeds. It returns **FALSE** if the operation fails.

## Remarks

After the miniport driver enumerates the devices on a channel, it calls the ***IdeHwInitialize*** routine one time for each device it enumerates. The ***IdeHwInitialize*** routine must configure each device based on the information that is specified in the [**IDE\_DEVICE\_PARAMETERS**](ide-device-parameters.md) structure, pointed to by the *DeviceParameters* parameter. In exceptional cases, the miniport driver can configure the device by using a set of parameters that differ from those contained in **IDE\_DEVICE\_PARAMETERS**. In such cases, the miniport driver must update the information in **IDE\_DEVICE\_PARAMETERS** to contain the parameter value that it actually used to configure the device. After the ***IdeHwInitialize*** routine returns, the port driver updates its cached information with the parameter values that are provided by the miniport driver.

## Requirements



|                            |                                                                                                  |
|----------------------------|--------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>               |
| Header<br/>          | <dl> <dt>Irb.h (include Irb.h)</dt> </dl> |



## See also

<dl> <dt>

[**IDE\_DEVICE\_PARAMETERS**](ide-device-parameters.md)
</dt> <dt>

[**IDENTIFY\_DEVICE\_DATA**](identify-device-data.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IdeHwInitialize%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






