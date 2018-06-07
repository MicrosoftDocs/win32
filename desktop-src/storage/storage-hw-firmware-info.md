---
title: STORAGE\_HW\_FIRMWARE\_INFO structure
description: This structure contains information about the device firmware.
ms.assetid: 5A85A7EC-2333-4161-A1E7-55D3420E730C
keywords:
- STORAGE_HW_FIRMWARE_INFO structure Storage Devices
- PSTORAGE_HW_FIRMWARE_INFO structure pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_HW_FIRMWARE_INFO
api_location:
- ntddstor.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# STORAGE\_HW\_FIRMWARE\_INFO structure

This structure contains information about the device firmware.

## Syntax


```C++
typedef struct _STORAGE_HW_FIRMWARE_INFO {
  ULONG                         Version;
  ULONG                         Size;
  UCHAR                         SupportUpgrade  :1;
  UCHAR                         Reserved0  :7;
  UCHAR                         SlotCount;
  UCHAR                         ActiveSlot;
  UCHAR                         PendingActivateSlot;
  BOOLEAN                       FirmwareShared;
  UCHAR                         Reserved[3];
  ULONG                         ImagePayloadAlignment;
  ULONG                         ImagePayloadMaxSize;
  STORAGE_HW_FIRMWARE_SLOT_INFO Slot[ANYSIZE_ARRAY];
} STORAGE_HW_FIRMWARE_INFO, *PSTORAGE_HW_FIRMWARE_INFO;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The version of this structure. This should be set to sizeof(STORAGE\_HW\_FIRMWARE\_INFO)

</dd> <dt>

**Size**
</dt> <dd>

The size of this structure as a buffer including slot.

</dd> <dt>

**SupportUpgrade**
</dt> <dd>

Indicates that this firmware supports an upgrade.

</dd> <dt>

**Reserved0**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**SlotCount**
</dt> <dd>

The number of firmware slots on the device. This is the dimension of the Slot array.

> [!Note]  
> Some devices can store more than 1 firmware image, if they have more than 1 firmware slot.

 

</dd> <dt>

**ActiveSlot**
</dt> <dd>

The firmware slot containing the currently active/running firmware image.

</dd> <dt>

**PendingActivateSlot**
</dt> <dd>

The firmware slot that is pending activation.

</dd> <dt>

**FirmwareShared**
</dt> <dd>

Indicates that the firmware applies to both the device and controller/adapter, e.g. NVMe SSD.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**ImagePayloadAlignment**
</dt> <dd>

The alignment of the image payload, in number of bytes. The maximum is PAGE\_SIZE. The transfer size is a mutliple of this size. Some protocols require at least sector size. When this value is set to 0, this means that this value is invalid.

</dd> <dt>

**ImagePayloadMaxSize**
</dt> <dd>

The image payload maximum size, this is used for a single command.

</dd> <dt>

**Slot**
</dt> <dd>

Contains the slot information for each slot on the device.

</dd> </dl>

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Client<br/> | Windows 10<br/>                                                                 |
| Server<br/> | Windows Server 2016<br/>                                                        |
| Header<br/> | <dl> <dt>Ntddstor.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_HW_FIRMWARE_INFO%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





