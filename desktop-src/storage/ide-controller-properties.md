---
title: IDE\_CONTROLLER\_PROPERTIES structure
description: The IDE\_CONTROLLER\_PROPERTIES structure contains configuration information for an IDE controller.
ms.assetid: '3d95a758-71ee-4f09-aef9-a87284a497e7'
keywords: ["IDE_CONTROLLER_PROPERTIES structure Storage Devices", "PIDE_CONTROLLER_PROPERTIES structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- IDE_CONTROLLER_PROPERTIES
api_location:
- ide.h
api_type:
- HeaderDef
---

# IDE\_CONTROLLER\_PROPERTIES structure

The IDE\_CONTROLLER\_PROPERTIES structure contains configuration information for an IDE controller.

## Syntax


```C++
typedef struct _IDE_CONTROLLER_PROPERTIES {
  ULONG                            Size;
  ULONG                            ExtensionSize;
  ULONG                            SupportedTransferMode[MAX_IDE_CHANNEL];
  PCIIDE_CHANNEL_ENABLED           PciIdeChannelEnabled;
  PCIIDE_SYNC_ACCESS_REQUIRED      PciIdeSyncAccessRequired;
  PCIIDE_TRANSFER_MODE_SELECT_FUNC PciIdeTransferModeSelect;
  BOOLEAN                          IgnoreActiveBitForAtaDevice;
  BOOLEAN                          AlwaysClearBusMasterInterrupt;
  BOOLEAN                          UsePioOnOddTransfers;
  UCHAR                            UsePioAfter8kTransfers  :1;
  UCHAR                            DmaRetryAfterCrcError  :1;
  UCHAR                            Reserved  :6;
  PCIIDE_USEDMA_FUNC               PciIdeUseDma;
  ULONG                            AlignmentRequirement;
  ULONG                            DefaultPIO;
  PCIIDE_UDMA_MODES_SUPPORTED      PciIdeUdmaModesSupported;
} IDE_CONTROLLER_PROPERTIES, *PIDE_CONTROLLER_PROPERTIES;
```



## Members

<dl> <dt>

**Size**
</dt> <dd>

Specifies the size of this structure in bytes, as returned by **sizeof**(). In effect, this member indicates the version of this structure used by the port driver.

</dd> <dt>

**ExtensionSize**
</dt> <dd>

Specifies the amount of memory in bytes needed by the PCI IDE controller minidriver for its private data.

</dd> <dt>

**SupportedTransferMode**
</dt> <dd>

Furnishes an array of bitmaps indicating the data transfer modes supported by the PCI IDE controller. See [**PCIIDE\_TRANSFER\_MODE\_SELECT**](pciide-transfer-mode-select.md) for a detailed definition of these bitmaps.

</dd> <dt>

**PciIdeChannelEnabled**
</dt> <dd>

Pointer to a minidriver routine used to query whether an IDE channel is enabled. For further information see [**HwIdeXChannelEnabled**](hwidexchannelenabled.md).

</dd> <dt>

**PciIdeSyncAccessRequired**
</dt> <dd>

Pointer to a minidriver routine used to query whether the controller's two IDE channels can be used simultaneously or must be used one at a time. For further information see [**HwIdeXSyncAccessRequired**](hwidexsyncaccessrequired.md).

</dd> <dt>

**PciIdeTransferModeSelect**
</dt> <dd>

Pointer to a minidriver routine used to select the proper transfer modes for the given devices. For further information see [**HwIdeXTransferModeSelect**](hwidextransfermodeselect.md).

</dd> <dt>

**IgnoreActiveBitForAtaDevice**
</dt> <dd>

If **TRUE** indicates that the controller's bus-master active bit should be ignored. Some IDE controllers do not properly clear the bus-master active bit upon the completion of a bus-master interrupt. Setting this member to **TRUE** indicates that the driver should clear the active bit manually. For an IDE controller that clears its active bit properly, this member should be **FALSE**.

</dd> <dt>

**AlwaysClearBusMasterInterrupt**
</dt> <dd>

If **TRUE**, indicates that the PCI IDE controller minidriver must clear the bus-master interrupt whenever the interrupt bit in the bus master status register is set. This should always be set to **TRUE**.

</dd> <dt>

**UsePioOnOddTransfers**
</dt> <dd>

Use PIO mode for an odd number of DWORD sized transfers.

</dd> <dt>

**UsePioAfter8kTransfers**
</dt> <dd>

Use PIO mode when an 8K scaled transfer is needed. This is when the transfer byte size is 8K \* N + M where N &gt; 0 && 0 &lt; M &lt; 512.

</dd> <dt>

**DmaRetryAfterCrcError**
</dt> <dd>

One DMA retry is issued if a CRC error occurs.

</dd> <dt>

**Reserved**
</dt> <dd></dd> <dt>

**PciIdeUseDma**
</dt> <dd>

Pointer to a minidriver routine that determines whether DMA should be used or not. This routine should be called before every I/O operation. For further information see [**HwIdeXUseDma**](hwidexusedma.md).

</dd> <dt>

**AlignmentRequirement**
</dt> <dd>

Specifies an alignment requirement value to be stored in the device object. See [Initializing a Device Object](https://msdn.microsoft.com/library/windows/hardware/ff547807) for further information about defining a device object's alignment requirement.

</dd> <dt>

**DefaultPIO**
</dt> <dd>

Indicates, when set to one by the controller minidriver, that devices connected to the minidriver's controller are restricted by default to PIO. However, users can request by means of the device manager that DMA be performed on individual devices.

</dd> <dt>

**PciIdeUdmaModesSupported**
</dt> <dd>

Pointer to a minidriver routine that is optionally implemented by the controller minidriver. This routine checks a device's identify data and determines the current ultra DMA transfer mode for that device. This allows the IDE port driver, *atapi.sys*, to query the controller minidriver for newly supported transfer modes without having to interpret a device's identify data. For further information see [**HwIdeXUdmaModesSupported**](hwidexudmamodessupported.md).

</dd> </dl>

## Remarks

This structure is returned by the IDE controller minidriver's [**HwIdeXGetControllerProperties**](hwidexgetcontrollerproperties.md) minidriver routine. Some of the information in this structure is obtained directly from the device extension; all information not obtained from the device extension is obtained from PCI configuration space by means of a call to the controller library routine, [**PciIdeXGetBusData**](pciidexgetbusdata.md).

## Requirements



|                   |                                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ide.h (include Ide.h)</dt> </dl> |



## See also

<dl> <dt>

[**HwIdeXGetControllerProperties**](hwidexgetcontrollerproperties.md)
</dt> <dt>

[**PCIIDE\_TRANSFER\_MODE\_SELECT**](pciide-transfer-mode-select.md)
</dt> <dt>

[**HwIdeXTransferModeSelect**](hwidextransfermodeselect.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IDE_CONTROLLER_PROPERTIES%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






