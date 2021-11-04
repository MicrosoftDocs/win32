---
description: Contains the serial number of a USB device. It is used by the IOCTL\_STORAGE\_GET\_MEDIA\_SERIAL\_NUMBER control code.
ms.assetid: a7df4528-a3b7-4ffa-b595-7ac918371582
title: MEDIA_SERIAL_NUMBER_DATA structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MEDIA_SERIAL_NUMBER_DATA
api_type: 
- NA
api_location: 
---

# MEDIA\_SERIAL\_NUMBER\_DATA structure

Contains the serial number of a USB device. It is used by the [**IOCTL\_STORAGE\_GET\_MEDIA\_SERIAL\_NUMBER**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_storage_get_media_serial_number) control code.

## Syntax


```C++
typedef struct _MEDIA_SERIAL_NUMBER_DATA {
  ULONG SerialNumberLength;
  ULONG Result;
  ULONG Reserved[2];
  UCHAR SerialNumberData[];
} MEDIA_SERIAL_NUMBER_DATA, *PMEDIA_SERIAL_NUMBER_DATA;
```



## Members

<dl> <dt>

**SerialNumberLength**
</dt> <dd>

The size of the **SerialNumberData** string, in bytes.

</dd> <dt>

**Result**
</dt> <dd>

The status of the request.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> <dt>

**SerialNumberData**
</dt> <dd>

The serial number of the device.

</dd> </dl>

## Remarks

No header file is available for the **MEDIA\_SERIAL\_NUMBER\_DATA** structure. Include the structure definition at the top of this page in your source code.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows XP<br/>          |
| Minimum supported server<br/> | Windows Server 2003<br/> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_GET\_MEDIA\_SERIAL\_NUMBER**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_storage_get_media_serial_number)
</dt> </dl>

 

 




