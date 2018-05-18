---
title: PCIIDE\_TRANSFER\_MODE\_SELECT structure
description: The PCIIDE\_TRANSFER\_MODE\_SELECT structure contains transfer mode information for all devices attached to a channel of an IDE controller.
ms.assetid: 'c8a006e4-0e26-4d21-816d-39533db90c4e'
keywords: ["PCIIDE_TRANSFER_MODE_SELECT structure Storage Devices", "PPCIIDE_TRANSFER_MODE_SELECT structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- PCIIDE_TRANSFER_MODE_SELECT
api_location:
- ide.h
api_type:
- HeaderDef
---

# PCIIDE\_TRANSFER\_MODE\_SELECT structure

The PCIIDE\_TRANSFER\_MODE\_SELECT structure contains transfer mode information for all devices attached to a channel of an IDE controller.

## Syntax


```C++
typedef struct _PCIIDE_TRANSFER_MODE_SELECT {
  ULONG         Channel;
  BOOLEAN       DevicePresent[MAX_IDE_DEVICE * MAX_IDE_LINE];
  BOOLEAN       FixedDisk[MAX_IDE_DEVICE * MAX_IDE_LINE];
  BOOLEAN       IoReadySupported[MAX_IDE_DEVICE * MAX_IDE_LINE];
  ULONG         DeviceTransferModeSupported[MAX_IDE_DEVICE * MAX_IDE_LINE];
  ULONG         BestPioCycleTime[MAX_IDE_DEVICE * MAX_IDE_LINE];
  ULONG         BestSwDmaCycleTime[MAX_IDE_DEVICE * MAX_IDE_LINE];
  ULONG         BestMwDmaCycleTime[MAX_IDE_DEVICE * MAX_IDE_LINE];
  ULONG         BestUDmaCycleTime[MAX_IDE_DEVICE * MAX_IDE_LINE];
  ULONG         DeviceTransferModeCurrent[MAX_IDE_DEVICE * MAX_IDE_LINE];
  ULONG         UserChoiceTransferMode[MAX_IDE_DEVICE * MAX_IDE_LINE];
  ULONG         EnableUDMA66;
  IDENTIFY_DATA IdentifyData[MAX_IDE_DEVICE];
  ULONG         DeviceTransferModeSelected[MAX_IDE_DEVICE * MAX_IDE_LINE];
  PULONG        TransferModeTimingTable;
  ULONG         TransferModeTableLength;
} PCIIDE_TRANSFER_MODE_SELECT, *PPCIIDE_TRANSFER_MODE_SELECT;
```



## Members

<dl> <dt>

**Channel**
</dt> <dd>

Contains the IDE channel number (0 or 1) of the devices for which a transfer mode is requested. All devices for which information is requested must be attached to the same channel.

</dd> <dt>

**DevicePresent**
</dt> <dd>

Each array entry, when **TRUE**, indicates that the corresponding device is currently present in the system. All of the member arrays of PCIIDE\_TRANSFER\_MODE\_SELECT contain entries for up to MAX\_IDE\_DEVICE devices, but for any given entry *n*, DevicePresent\[*n*\] must be consulted to determine if the *nth* device is actually present in the system. If the *nth* device is present, then DevicePresent\[*n*\] = **TRUE**.

</dd> <dt>

**FixedDisk**
</dt> <dd>

Each array entry, when **TRUE**, indicates that the corresponding device is an ATA hard disk.

</dd> <dt>

**IoReadySupported**
</dt> <dd>

Each array entry, when **TRUE**, indicates that the corresponding device supports I/O Ready.

</dd> <dt>

**DeviceTransferModeSupported**
</dt> <dd>

Furnishes a bitmap indicating the data transfer modes that each attached device supports. For more information, see the Remarks section.

</dd> <dt>

**BestPioCycleTime**
</dt> <dd>

Contains an array of integer values that indicate each device's best PIO cycle time in nanoseconds.

</dd> <dt>

**BestSwDmaCycleTime**
</dt> <dd>

Contains an array of integer values that indicate each device's best Single-word DMA cycle time in nanoseconds.

</dd> <dt>

**BestMwDmaCycleTime**
</dt> <dd>

Contains an array of integer values that indicate each device's best Multiword DMA cycle time in nanoseconds.

</dd> <dt>

**BestUDmaCycleTime**
</dt> <dd>

Contains an array of integer values that indicate each device's best Ultra DMA cycle time in nanoseconds.

</dd> <dt>

**DeviceTransferModeCurrent**
</dt> <dd>

Furnishes a bitmap indicating the data transfer modes each device is currently programmed for. For more information, see the Remarks section.

</dd> <dt>

**UserChoiceTransferMode**
</dt> <dd> <dl> <dt>


</dt> <dt>


</dt> </dl> </dd> <dt>

**EnableUDMA66**
</dt> <dd> <dl> <dt>


</dt> <dt>

The miniport will save this data in their deviceExtension
</dt> </dl> </dd> <dt>

**IdentifyData**
</dt> <dd> <dl> <dt>


</dt> <dt>

Indicate devices' data transfer modes chosen by 
</dt> <dt>


</dt> </dl> </dd> <dt>

**DeviceTransferModeSelected**
</dt> <dd>

Furnishes a bitmap indicating the data transfer modes selected by the PCI minidriver for each device. For more information, see the Remarks section.

</dd> <dt>

**TransferModeTimingTable**
</dt> <dd></dd> <dt>

**TransferModeTableLength**
</dt> <dd></dd> </dl>

## Remarks

Member arrays **DeviceTransferModeSupported**, **DeviceTransferModeCurrent**, and **DeviceTransferModeSelected** are arrays of ULONG bitmaps indicating combinations of PIO and DMA transfer modes. Each bitmap corresponds to the transfer modes of a single device. The bitmaps are defined as follows:

<dl> // PIO Modes  
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
</dl>

## Requirements



|                   |                                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ide.h (include Ide.h)</dt> </dl> |



## See also

<dl> <dt>

[**HwIdeXTransferModeSelect**](hwidextransfermodeselect.md)
</dt> <dt>

[**HwIdeXGetControllerProperties**](hwidexgetcontrollerproperties.md)
</dt> <dt>

[**IDE\_CONTROLLER\_PROPERTIES**](ide-controller-properties.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PCIIDE_TRANSFER_MODE_SELECT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






