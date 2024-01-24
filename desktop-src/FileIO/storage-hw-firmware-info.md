---
description: STORAGE_HW_FIRMWARE_INFO structure - This structure contains information about the device firmware.
ms.assetid: 7BDACD50-0FD1-4F00-BAE5-884D8C1485BC
title: STORAGE_HW_FIRMWARE_INFO structure (Winioctl.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- STORAGE_HW_FIRMWARE_INFO
api_type: 
- HeaderDef
api_location: 
- winioctl.h.h
---

# STORAGE\_HW\_FIRMWARE\_INFO structure

This structure contains information about the device firmware.

## Syntax


```C++
typedef struct _STORAGE_HW_FIRMWARE_INFO {
  DWORD                         Version;
  DWORD                         Size;
  BYTE                          SupportUpgrade  :1;
  BYTE                          Reserved0  :7;
  BYTE                          SlotCount;
  BYTE                          ActiveSlot;
  BYTE                          PendingActivateSlot;
  BOOLEAN                       FirmwareShared;
  BYTE                          Reserved[3];
  DWORD                         ImagePayloadAlignment;
  DWORD                         ImagePayloadMaxSize;
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

Contains the slot information for each slot on the device, of type [**STORAGE\_HW\_FIRMWARE\_SLOT\_INFO**](storage-hw-firmware-slot-info.md).

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                                        |
| Header<br/>                   | <dl> <dt>Winioctl.h.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_FIRMWARE\_ACTIVATE**](/windows/desktop/api/WinIoctl/ni-winioctl-ioctl_storage_firmware_activate)
</dt> <dt>

[**STORAGE\_HW\_FIRMWARE\_ACTIVATE**](/windows/desktop/api/winioctl/ns-winioctl-storage_hw_firmware_activate)
</dt> <dt>

[**IOCTL\_STORAGE\_FIRMWARE\_DOWNLOAD**](/windows/desktop/api/WinIoctl/ni-winioctl-ioctl_storage_firmware_download)
</dt> <dt>

[**STORAGE\_HW\_FIRMWARE\_DOWNLOAD**](/windows/desktop/api/winioctl/ns-winioctl-storage_hw_firmware_download)
</dt> <dt>

[**IOCTL\_STORAGE\_FIRMWARE\_GET\_INFO**](/windows/desktop/api/WinIoctl/ni-winioctl-ioctl_storage_firmware_get_info)
</dt> <dt>

[**STORAGE\_HW\_FIRMWARE\_INFO\_QUERY**](storage-hw-firmware-info-query.md)
</dt> <dt>

[**STORAGE\_HW\_FIRMWARE\_SLOT\_INFO**](storage-hw-firmware-slot-info.md)
</dt> </dl>

 

 




