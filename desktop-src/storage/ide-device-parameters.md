---
title: IDE\_DEVICE\_PARAMETERS structure
description: The IDE\_DEVICE\_PARAMETERS structure contains configuration information that the port driver provides to the miniport driver to configure a device.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: e2b908ce-df40-4d64-b8fd-77da18b4f6bd
keywords:
- IDE_DEVICE_PARAMETERS structure Storage Devices
- PIDE_DEVICE_PARAMETERS structure pointer Storage Devices
topic_type:
- apiref
api_name:
- IDE_DEVICE_PARAMETERS
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

# IDE\_DEVICE\_PARAMETERS structure

The IDE\_DEVICE\_PARAMETERS structure contains configuration information that the port driver provides to the miniport driver to configure a device.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _IDE_DEVICE_PARAMETERS {
  USHORT                  Version;
  IDE_DEVICE_TYPE         IdeDeviceType;
  UCHAR                   TargetId;
  UCHAR                   MaximumLun;
  UCHAR                   NumberOfOverlappedRequests;
  UCHAR                   MaxBlockXfer;
  USHORT                  DeviceCharacteristics;
  ATA_ADDRESS_TRANSLATION AddressTranslation;
  union {
    LARGE_INTEGER MaxLba;
    struct {
      USHORT NumCylinders;
      USHORT NumHeads;
      USHORT NumSectorsPerTrack;
      USHORT Reserved;
    } Chs;
  };
  ULONG                   BytesPerLogicalSector;
  ULONG                   BytesPerPhysicalSector;
  ULONG                   BytesOffsetForSectorAlignment;
  ULONG                   TransferModeSupported;
  ULONG                   TransferModeSelected;
} IDE_DEVICE_PARAMETERS, *PIDE_DEVICE_PARAMETERS;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

Indicates the size of the *Device* parameters structure. The miniport driver should verify that sizeof(IDE\_DEVICE\_PARAMETERS) is less than or equal to the **Version** field.

</dd> <dt>

**IdeDeviceType**
</dt> <dd>

Indicates the type of the device. The allowed device types are *DeviceIsAta* for ATA devices, *DeviceIsAtapi* for ATAPI devices, and *DeviceNotExist* if no device was found at that address. The other fields in this structure are not valid if the **IdeDeviceType** is set to *DeviceNotExist*.

</dd> <dt>

**TargetId**
</dt> <dd>

Specifies the target ID of the device.

</dd> <dt>

**MaximumLun**
</dt> <dd>

The miniport driver must update this field to indicate the maximum logical unit number supported by this device. By default, the member is set to 0 indicating the existence of just one LUN.

</dd> <dt>

**NumberOfOverlappedRequests**
</dt> <dd>

The miniport driver must update this field to specify the number of overlapped requests it can handle for this device. By default, the member is set to 1.

</dd> <dt>

**MaxBlockXfer**
</dt> <dd>

Specifies the number of sectors in a block of data to be transferred. This value applies to the data blocks used in ATA block transfer commands such as Read Multiple (0xC4), Write Multiple (0xC5). For more information about the ReadMultiple and WriteMultiple commands, see the *ATA Specification*.

</dd> <dt>

**DeviceCharacteristics**
</dt> <dd>

Specifies the device characteristics. The table below lists the characteristics that could be set in this member. The high byte of this member is opaque and shall not be changed by the ATA miniport.



| Device Characteristic                 | Description                                                                                        |
|---------------------------------------|----------------------------------------------------------------------------------------------------|
| DFLAGS\_REMOVABLE\_MEDIA<br/>   | Indicates that the drive has removable media<br/>                                            |
| DFLAGS\_ REMOVABLE\_DEVICE<br/> | Indicates that the device can be safely unplugged<br/>                                       |
| DFLAGS\_FUA\_SUPPORT<br/>       | Indicates that the device supports FUA (Force Unit Access)<br/>                              |
| DFLAGS\_INT\_DRQ<br/>           | Indicates that the device interrupts as DRQ is set after receiving ATAPI Packet command<br/> |
| DFLAGS\_MSN\_SUPPORT<br/>       | Indicates that the device supports Media Status Notification.<br/>                           |



 

</dd> <dt>

**AddressTranslation**
</dt> <dd>

Contains an enumeration value of type [**ATA\_ADDRESS\_TRANSLATION**](ata-address-translation.md) that specifies the sort of address translation used during data transfers.

</dd> <dt>

**MaxLba**
</dt> <dd>

Specifies the maximum user-addressable logical block address (LBA). This member is defined when **AddressTranslation** is equal to either **LbaMode** or **Lba48BitMode**.

</dd> <dt>

**Chs**
</dt> <dd>

Specifies the drive geometry with the values for the number of cylinders, heads per cylinder, and the sectors per track. This member is defined when **AddressTranslation** is equal to **ChsMode**.

<dl></dl> </dd> <dt>

**BytesPerLogicalSector**
</dt> <dd>

This member specifies the number of bytes per logical sector (LBA) for the given device.

</dd> <dt>

**BytesPerPhysicalSector**
</dt> <dd>

This member specifies the number of bytes per physical sector (that is, the smallest amount of data that the device can physically write internally) for the given device.

</dd> <dt>

**BytesOffsetForSectorAlignment**
</dt> <dd>

This member specifies the location of sector 0 within the first physical sector as defined in the ATA specification represented in bytes.

</dd> <dt>

**TransferModeSupported**
</dt> <dd>

Contains a bitmap that indicates the supported transfer modes.

</dd> <dt>

**TransferModeSelected**
</dt> <dd>

Indicates the selected transfer modes on the device. The miniport driver must set this member.

</dd> </dl>

## Remarks

The port driver passes a IDE\_DEVICE\_PARAMETERS structure to the miniport driver when it calls [**IdeHwInitialize**](idehwinitialize.md).

## Requirements



|                   |                                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Irb.h (include Irb.h)</dt> </dl> |



## See also

<dl> <dt>

[**IDE\_DEVICE\_TYPE**](ide-device-type.md)
</dt> <dt>

[**ATA\_ADDRESS\_TRANSLATION**](ata-address-translation.md)
</dt> <dt>

[**IdeHwInitialize**](idehwinitialize.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IDE_DEVICE_PARAMETERS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






