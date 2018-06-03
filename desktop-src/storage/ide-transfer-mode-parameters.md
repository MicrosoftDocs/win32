---
title: IDE\_TRANSFER\_MODE\_PARAMETERS structure
description: The IDE\_TRANSFER\_MODE\_PARAMETERS structure is used in conjunction with the miniport driver's AtaControllerTransferModeSelect routine to set the transfer mode parameters on a channel.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the Storport driver and Storport miniport driver models.
ms.assetid: 66e6efd0-6651-4c87-94ba-d9d3b9191339
keywords:
- IDE_TRANSFER_MODE_PARAMETERS structure Storage Devices
- PIDE_TRANSFER_MODE_PARAMETERS structure pointer Storage Devices
topic_type:
- apiref
api_name:
- IDE_TRANSFER_MODE_PARAMETERS
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

# IDE\_TRANSFER\_MODE\_PARAMETERS structure

The IDE\_TRANSFER\_MODE\_PARAMETERS structure is used in conjunction with the miniport driver's [**AtaControllerTransferModeSelect**](atacontrollertransfermodeselect.md) routine to set the transfer mode parameters on a channel.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _IDE_TRANSFER_MODE_PARAMETERS {
  UCHAR           ChannelNumber;
  IDE_DEVICE_TYPE DeviceType[MAX_IDE_DEVICE];
  BOOLEAN         IoReadySupported[MAX_IDE_DEVICE];
  ULONG           DeviceTransferModeSupported[MAX_IDE_DEVICE];
  ULONG           DeviceTransferModeCurrent[MAX_IDE_DEVICE];
  ULONG           DeviceTransferModeSelected[MAX_IDE_DEVICE];
} IDE_TRANSFER_MODE_PARAMETERS, *PIDE_TRANSFER_MODE_PARAMETERS;
```



## Members

<dl> <dt>

**ChannelNumber**
</dt> <dd>

Indicates the channel number whose mode parameters are to be set.

</dd> <dt>

**DeviceType**
</dt> <dd>

Contains an enumeration value of type [**IDE\_DEVICE\_TYPE**](ide-device-type.md) that indicates the type of device. The miniport driver should not select a transfer mode if the device type is **DeviceNotExist**.

</dd> <dt>

**IoReadySupported**
</dt> <dd>

Indicates when **TRUE** that bit 11 of word 49 of the indicated device's identify data is set to 1. An IDE request with a function value of IRB\_FUNCTION\_ATA\_IDENTIFY will retrieve a device's identify data. For more information about ATA identify data, see the sections on the Identify Device information packet in version 6.0 of the *ATA/ATAPI specification*.

</dd> <dt>

**DeviceTransferModeSupported**
</dt> <dd>

Contains a bitmap that indicates the supported transfer modes for each of the devices on the channel. The port driver sets this member. The miniport driver must not select a transfer mode that the port driver does not support. For more information about this member, see the **Remarks** section.

</dd> <dt>

**DeviceTransferModeCurrent**
</dt> <dd>

Contains a bitmap that indicates the current transfer mode settings for each of the device on the channel. The port driver retrieves the current transfer mode of the devices from their identify device data. For more information about this member, see the **Remarks** section.

</dd> <dt>

**DeviceTransferModeSelected**
</dt> <dd>

Contains a bitmap that indicates the selected transfer mode settings for each of the device on the channel. The miniport driver should use this member to indicate to the port driver which transfer modes it selects. For more information about this member, see the **Remarks** section.

</dd> </dl>

## Remarks

Member arrays **DeviceTransferModeSupported**, **DeviceTransferModeCurrent**, and **DeviceTransferModeSelected** are arrays of ULONG bitmaps indicating combinations of PIO and DMA transfer modes. The bitmaps are defined as follows:

// PIO Modes

\#define PIO\_MODE0 (1 &lt;&lt; 0)

\#define PIO\_MODE1 (1 &lt;&lt; 1)

\#define PIO\_MODE2 (1 &lt;&lt; 2)

\#define PIO\_MODE3 (1 &lt;&lt; 3)

\#define PIO\_MODE4 (1 &lt;&lt; 4)

// Single-word DMA Modes

\#define SWDMA\_MODE0 (1 &lt;&lt; 5)

\#define SWDMA\_MODE1 (1 &lt;&lt; 6)

\#define SWDMA\_MODE2 (1 &lt;&lt; 7)

// Multi-word DMA Modes

\#define MWDMA\_MODE0 (1 &lt;&lt; 8)

\#define MWDMA\_MODE1 (1 &lt;&lt; 9)

\#define MWDMA\_MODE2 (1 &lt;&lt; 10)

// Ultra DMA Modes

\#define UDMA\_MODE0 (1 &lt;&lt; 11)

\#define UDMA\_MODE1 (1 &lt;&lt; 12)

\#define UDMA\_MODE2 (1 &lt;&lt; 13)

\#define UDMA\_MODE3 (1 &lt;&lt; 14)

\#define UDMA\_MODE4 (1 &lt;&lt; 15)

\#define UDMA\_MODE5 (1 &lt;&lt; 16)

## Requirements



|                   |                                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Irb.h (include Irb.h)</dt> </dl> |



## See also

<dl> <dt>

[**AtaControllerTransferModeSelect**](atacontrollertransfermodeselect.md)
</dt> <dt>

[**IDE\_DEVICE\_TYPE**](ide-device-type.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IDE_TRANSFER_MODE_PARAMETERS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






