---
title: PRO\_PARAMETER\_LIST structure
description: The PRO\_PARAMETER\_LIST structure is sent in a Persistent Reserve Out command to a device server.
ms.assetid: '96c128e1-c38a-412f-adeb-cde820e1af4e'
keywords: ["PRO_PARAMETER_LIST structure Storage Devices", "PPRO_PARAMETER_LIST structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- PRO_PARAMETER_LIST
api_location:
- storport.h
api_type:
- HeaderDef
---

# PRO\_PARAMETER\_LIST structure

The PRO\_PARAMETER\_LIST structure is sent in a Persistent Reserve Out command to a device server.

## Syntax


```C++
typedef struct {
  UCHAR ReservationKey[8];
  UCHAR ServiceActionReservationKey[8];
  UCHAR ScopeSpecificAddress[4];
  UCHAR ActivatePersistThroughPowerLoss  :1;
  UCHAR Reserved1  :7;
  UCHAR Reserved2;
  UCHAR Obsolete[2];
} PRO_PARAMETER_LIST, *PPRO_PARAMETER_LIST;
```



## Members

<dl> <dt>

**ReservationKey**
</dt> <dd>

The ReservationKey field contains an 8-byte value that is provided by the application client to the device server. This value identifies the initiator that is the source of the Persistent Reserve Out command.

</dd> <dt>

**ServiceActionReservationKey**
</dt> <dd>

The ServiceActionReservationKey field contains information that is needed for the following four service actions:

-   REGISTER

-   REGISTER AND IGNORE EXISTING KEY

-   PREEMPT

-   PREEMPT AND ABORT

</dd> <dt>

**ScopeSpecificAddress**
</dt> <dd>

The ScopeSpecificAddress field contains the element address that has zeros placed in the most significant bits to fit the field. This is true if the scope of a reservation is set to ELEMENT\_SCOPE. Otherwise, this field is set to all zeros.

</dd> <dt>

**ActivatePersistThroughPowerLoss**
</dt> <dd>

The ActivatePersistThroughPowerLoss (APTPL) bit is valid only for the following service actions:

-   REGISTER

-   REGISTER AND IGNORE EXISTING KEY

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved. Must be zero.

</dd> <dt>

**Reserved2**
</dt> <dd>

Reserved. Must be zero.

</dd> <dt>

**Obsolete**
</dt> <dd>

Reserved. Must be zero.

</dd> </dl>

## Remarks

The [**IOCTL\_STORAGE\_PERSISTENT\_RESERVE\_OUT**](ioctl-storage-persistent-reserve-out.md) request is used to control information about persistent reservations and reservation keys that are active within a device server.

## Requirements



|                   |                                                                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Storport.h (include Ntddstor.h, Minitape.h, or Scsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_PERSISTENT\_RESERVE\_OUT**](ioctl-storage-persistent-reserve-out.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PRO_PARAMETER_LIST%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






