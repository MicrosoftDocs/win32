---
title: PRI\_RESERVATION\_LIST structure
description: The PRI\_RESERVATION\_LIST structure is returned in response to a Persistent Reserve In command with ServiceAction RESERVATION\_ACTION\_READ\_RESERVATIONS.
ms.assetid: '5756e907-008a-49c3-b1cd-947cb0ce1bd4'
keywords: ["PRI_RESERVATION_LIST structure Storage Devices", "PPRI_RESERVATION_LIST structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- PRI_RESERVATION_LIST
api_location:
- storport.h
api_type:
- HeaderDef
---

# PRI\_RESERVATION\_LIST structure

The PRI\_RESERVATION\_LIST structure is returned in response to a Persistent Reserve In command with ServiceAction = RESERVATION\_ACTION\_READ\_RESERVATIONS.

## Syntax


```C++
typedef struct {
  UCHAR                      Generation[4];
  UCHAR                      AdditionalLength[4];
  PRI_RESERVATION_DESCRIPTOR Reservations[];
} PRI_RESERVATION_LIST, *PPRI_RESERVATION_LIST;
```



## Members

<dl> <dt>

**Generation**
</dt> <dd>

The Generation field contains a 32-bit counter that is maintained by the device server, which is incremented every time a Persistent Reserve Out command requests a REGISTER, REGISTER AND IGNORE

EXISTING KEY, CLEAR, PREEMPT, or PREEMPT AND ABORT service action.

</dd> <dt>

**AdditionalLength**
</dt> <dd>

The AdditionalLength field contains a count of the number of bytes in the reservation descriptors.

</dd> <dt>

**Reservations**
</dt> <dd>

An array of reservation descriptors.

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
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PRI_RESERVATION_LIST%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






