---
Description: 'Contains the serial number of a USB device. It is used by the IOCTL\_STORAGE\_GET\_MEDIA\_SERIAL\_NUMBER control code.'
ms.assetid: 'a7df4528-a3b7-4ffa-b595-7ac918371582'
title: 'MEDIA\_SERIAL\_NUMBER\_DATA structure'
---

# MEDIA\_SERIAL\_NUMBER\_DATA structure

Contains the serial number of a USB device. It is used by the [**IOCTL\_STORAGE\_GET\_MEDIA\_SERIAL\_NUMBER**](ioctl-storage-get-media-serial-number.md) control code.

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



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows XP<br/>          |
| Minimum supported server<br/> | Windows Server 2003<br/> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_GET\_MEDIA\_SERIAL\_NUMBER**](ioctl-storage-get-media-serial-number.md)
</dt> </dl>

 

 




