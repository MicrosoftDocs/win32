---
title: IDE\_CONTROLLER\_INTERFACE structure
description: The IDE\_CONTROLLER\_INTERFACE structure is used to pass controller configuration information between the port driver and the miniport driver.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: 'cb18f7d9-f9e8-436d-8d61-3641730bd8a2'
keywords: ["IDE_CONTROLLER_INTERFACE structure Storage Devices", "PIDE_CONTROLLER_INTERFACE structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- IDE_CONTROLLER_INTERFACE
api_location:
- irb.h
api_type:
- HeaderDef
---

# IDE\_CONTROLLER\_INTERFACE structure

The IDE\_CONTROLLER\_INTERFACE structure is used to pass controller configuration information between the port driver and the miniport driver.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _IDE_CONTROLLER_INTERFACE {
  USHORT                   Version;
  USHORT                   Reserved;
  ULONG                    ControllerExtensionSize;
  ULONG                    ChannelExtensionSize;
  ULONG                    AlignmentMask;
  IDE_CHANNEL_INIT         AtaChannelInitRoutine;
  IDE_CHANNEL_ENABLED      AtaControllerChannelEnabled;
  IDE_TRANSFER_MODE_SELECT AtaControllerTransferModeSelect;
  IDE_ADAPTER_CONTROL      AtaAdapterControl;
} IDE_CONTROLLER_INTERFACE, *PIDE_CONTROLLER_INTERFACE;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The port driver sets this field to indicate the version of the port driver. The port driver sets the version to sizeof(IDE\_CONTROLLER\_INTERFACE). The miniport driver should verify that the version is greater than or equal to the one it is using.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved for future use. The miniport driver shall not use this field.

</dd> <dt>

**ControllerExtensionSize**
</dt> <dd>

Specifies the size in bytes required by a miniport driver for its controller device extension.

</dd> <dt>

**ChannelExtensionSize**
</dt> <dd>

Specifies the size in bytes required by a miniport driver for its per-channel device extension.

</dd> <dt>

**AlignmentMask**
</dt> <dd>

Contains a mask indicating the alignment restrictions for buffers required by the HBA for transfer operations. Valid mask values are also restricted by characteristics of the memory managers on different versions of Windows. Under Windows 2000 and Windows XP, the valid mask values are 0 (byte-aligned), 1 (word-aligned), 3 (DWORD-aligned) and 7 (double DWORD-aligned). The miniport driver should set this mask if the HBA supports scatter/gather.

</dd> <dt>

**AtaChannelInitRoutine**
</dt> <dd>

Pointer to the miniport's **AtaChannelInitRoutine** routine. The miniport needs to set this entry point only if it supports the Channel Interface.

</dd> <dt>

**AtaControllerChannelEnabled**
</dt> <dd>

Pointer to the miniport's **AtaControllerChannelEnabled** routine. This is an optional entry point.

</dd> <dt>

**AtaControllerTransferModeSelect**
</dt> <dd>

Pointer to the miniport's **AtaControllerTransferModeSelect** routine. This is an optional entry point.

</dd> <dt>

**AtaAdapterControl**
</dt> <dd>

Pointer to the miniport's **AtaControllerAdapterControl** routine. This is a required entry point.

</dd> </dl>

## Remarks

## Requirements



|                   |                                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Irb.h (include Irb.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IDE_CONTROLLER_INTERFACE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





