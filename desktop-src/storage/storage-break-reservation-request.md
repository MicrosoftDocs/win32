---
title: STORAGE\_BREAK\_RESERVATION\_REQUEST structure
description: The STORAGE\_BREAK\_RESERVATION\_REQUEST structure is used in conjunction with the IOCTL\_STORAGE\_BREAK\_RESERVATION request to free a disk resource that was previously reserved.
ms.assetid: 06de4432-9437-4275-8d1e-606f209e1468
keywords:
- STORAGE_BREAK_RESERVATION_REQUEST structure Storage Devices
- PSTORAGE_BREAK_RESERVATION_REQUEST structure pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_BREAK_RESERVATION_REQUEST
api_location:
- ntddstor.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# STORAGE\_BREAK\_RESERVATION\_REQUEST structure

The STORAGE\_BREAK\_RESERVATION\_REQUEST structure is used in conjunction with the [**IOCTL\_STORAGE\_BREAK\_RESERVATION**](ioctl-storage-break-reservation.md) request to free a disk resource that was previously reserved.

## Syntax


```C++
typedef struct STORAGE_BREAK_RESERVATION_REQUEST {
  ULONG Length;
  UCHAR _unused;
  UCHAR PathId;
  UCHAR TargetId;
  UCHAR Lun;
} STORAGE_BREAK_RESERVATION_REQUEST, *PSTORAGE_BREAK_RESERVATION_REQUEST;
```



## Members

<dl> <dt>

**Length**
</dt> <dd>

Contains the length of this structure in bytes.

</dd> <dt>

**\_unused**
</dt> <dd>

Reserved. Do not use.

</dd> <dt>

**PathId**
</dt> <dd>

Indicates the number of the bus to be reset.

</dd> <dt>

**TargetId**
</dt> <dd>

Contains the number of the target device.

</dd> <dt>

**Lun**
</dt> <dd>

Contains the logical unit number.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_BREAK\_RESERVATION**](ioctl-storage-break-reservation.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_BREAK_RESERVATION_REQUEST%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






