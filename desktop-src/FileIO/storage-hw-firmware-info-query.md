---
description: STORAGE_HW_FIRMWARE_INFO_QUERY structure - This structure contains information about the device firmware.
ms.assetid: 1A2D30F3-F2DE-40CB-BFFC-8BAD19793AE1
title: STORAGE_HW_FIRMWARE_INFO_QUERY structure (Winioctl.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- STORAGE_HW_FIRMWARE_INFO_QUERY
api_type: 
- HeaderDef
api_location: 
- winioctl.h.h
---

# STORAGE\_HW\_FIRMWARE\_INFO\_QUERY structure

This structure contains information about the device firmware.

## Syntax


```C++
typedef struct _STORAGE_HW_FIRMWARE_INFO_QUERY {
  DWORD Version;
  DWORD Size;
  DWORD Flags;
  DWORD Reserved;
} STORAGE_HW_FIRMWARE_INFO_QUERY, *PSTORAGE_HW_FIRMWARE_INFO_QUERY;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The version of this structure. This should be set to sizeof(STORAGE\_HW\_FIRMWARE\_INFO\_QUERY)

</dd> <dt>

**Size**
</dt> <dd>

The size of this structure as a buffer.

</dd> <dt>

**Flags**
</dt> <dd>

The flags associated with the query. The following are flags that can be set in this member.



| Flag                                             | Description                                                                        |
|--------------------------------------------------|------------------------------------------------------------------------------------|
| STORAGE\_HW\_FIRMWARE\_REQUEST\_FLAG\_CONTROLLER | Indicates that the target of the request other than the device hand/object itself. |



 

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved for future use.

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

[**STORAGE\_HW\_FIRMWARE\_SLOT\_INFO**](storage-hw-firmware-slot-info.md)
</dt> </dl>

 

 




