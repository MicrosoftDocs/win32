---
title: PRI\_RESERVATION\_DESCRIPTOR structure
description: The PRI\_RESERVATION\_DESCRIPTOR structure is used to construct the PRI\_RESERVATION\_LIST structure that is returned in response to a Persistent Reserve In command with ServiceAction RESERVATION\_ACTION\_READ\_RESERVATIONS.
ms.assetid: f03506f6-404e-4635-a9ad-f2f36164ff2f
keywords:
- PRI_RESERVATION_DESCRIPTOR structure Storage Devices
- PPRI_RESERVATION_DESCRIPTOR structure pointer Storage Devices
topic_type:
- apiref
api_name:
- PRI_RESERVATION_DESCRIPTOR
api_location:
- storport.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PRI\_RESERVATION\_DESCRIPTOR structure

The PRI\_RESERVATION\_DESCRIPTOR structure is used to construct the [**PRI\_RESERVATION\_LIST**](pri-reservation-list.md) structure that is returned in response to a Persistent Reserve In command with ServiceAction = RESERVATION\_ACTION\_READ\_RESERVATIONS.

## Syntax


```C++
typedef struct {
  UCHAR ReservationKey[8];
  UCHAR ScopeSpecificAddress[4];
  UCHAR Reserved;
  UCHAR Type  :4;
  UCHAR Scope  :4;
  UCHAR Obsolete[2];
} PRI_RESERVATION_DESCRIPTOR, *PPRI_RESERVATION_DESCRIPTOR;
```



## Members

<dl> <dt>

**ReservationKey**
</dt> <dd>

The reservation key under which the persistent reservation is held.

</dd> <dt>

**ScopeSpecificAddress**
</dt> <dd>

The ScopeSpecificAddress field contains the element address, that has zeros placed in the most significant bits to fit the field.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved. Must be zero.

</dd> <dt>

**Type**
</dt> <dd>

The type of the persistent reservation as present in the Persistent Reserve Out command that created the persistent reservation.

</dd> <dt>

**Scope**
</dt> <dd>

The scope of the persistent reservation as present in the Persistent Reserve Out command that created the persistent reservation.

</dd> <dt>

**Obsolete**
</dt> <dd>

Reserved. Must be zero.

</dd> </dl>

## Remarks

The [**IOCTL\_STORAGE\_PERSISTENT\_RESERVE\_IN**](ioctl-storage-persistent-reserve-in.md) request is used to obtain information about persistent reservations and reservation keys that are active within a device server.

## Requirements



|                   |                                                                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Storport.h (include Ntddstor.h, Minitape.h, or Scsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_PERSISTENT\_RESERVE\_IN**](ioctl-storage-persistent-reserve-in.md)
</dt> <dt>

[**PRI\_RESERVATION\_LIST**](pri-reservation-list.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PRI_RESERVATION_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






