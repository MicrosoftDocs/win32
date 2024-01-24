---
description: This structure contains information about a slot on a device.
ms.assetid: 37475351-DE0F-4B80-B26B-1482FBCC16CD
title: STORAGE_HW_FIRMWARE_SLOT_INFO structure (Winioctl.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- STORAGE_HW_FIRMWARE_SLOT_INFO
api_type: 
- HeaderDef
api_location: 
- winioctl.h.h
---

# STORAGE\_HW\_FIRMWARE\_SLOT\_INFO structure

This structure contains information about a slot on a device.

## Syntax


```C++
typedef struct _STORAGE_HW_FIRMWARE_SLOT_INFO {
  DWORD Version;
  DWORD Size;
  BYTE  SlotNumber;
  BYTE  ReadOnly  :1;
  BYTE  Reserved0  :7;
  BYTE  Reserved1[6];
  BYTE  Revision[STORAGE_HW_FIRMWARE_REVISION_LENGTH];
} STORAGE_HW_FIRMWARE_SLOT_INFO, *PSTORAGE_HW_FIRMWARE_SLOT_INFO;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The version of this structure. This should be set to sizeof(STORAGE\_HW\_FIRMWARE\_SLOT\_INFO)

</dd> <dt>

**Size**
</dt> <dd>

The size of this structure.

</dd> <dt>

**SlotNumber**
</dt> <dd>

The slot number of this slot.

</dd> <dt>

**ReadOnly**
</dt> <dd>

Indicates whether this slot is read-only or not.

</dd> <dt>

**Reserved0**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**Revision**
</dt> <dd>

The revision of the firmware on this slot.

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

[**STORAGE\_HW\_FIRMWARE\_INFO**](storage-hw-firmware-info.md)
</dt> <dt>

[**STORAGE\_HW\_FIRMWARE\_INFO\_QUERY**](storage-hw-firmware-info-query.md)
</dt> </dl>

 

 




