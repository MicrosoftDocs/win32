---
title: IOCTL\_STORAGE\_BREAK\_RESERVATION control code
description: Breaks a disk reservation.
ms.assetid: '4f6d14b1-45fd-4f45-a10a-1483c10cec12'
keywords: ["IOCTL_STORAGE_BREAK_RESERVATION control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_STORAGE_BREAK_RESERVATION
api_location:
- Ntddstor.h
api_type:
- HeaderDef
---

# IOCTL\_STORAGE\_BREAK\_RESERVATION control code

Breaks a disk reservation. In a multi-initiator ("clustered") system, a single computer can reserve a disk resource, so that no other computer can access the disk. If the computer does not or cannot free the resource in a timely fashion, a means is needed to remove the reservation of the disk by force.

One means of forcing the system to free a reserved disk resource is to reset the bus. In fact, for storage devices whose bus adapters are managed by the SCSI port driver, the IOCTL\_STORAGE\_BREAK\_RESERVATION request is equivalent to [**IOCTL\_STORAGE\_RESET\_BUS**](ioctl-storage-reset-bus.md), which simply does a reset of the bus, freeing all of its reserved resources.

For storage devices whose bus adapters are managed by the STOR port driver, this I/O control code offers a better technique of breaking a disk reservation. That technique is called a "hierarchical reset." Upon receiving an IOCTL\_STORAGE\_BREAK\_RESERVATION request, the STOR port driver first attempts to remove the reserve on the logical unit by resetting the logical unit itself. If that fails, the STOR port driver attempts to reset the target device that is the parent of the logical unit. Only when resetting the target device fails will the port driver reset the bus.

Resetting the bus clears all device reservations and transfer speed settings, which must then be renegotiated. Because this is a time-consuming operation, IOCTL\_STORAGE\_BREAK\_RESERVATION is always to be preferred to a simple bus reset.

The caller requires only read access to issue a bus reset.

The **SrbStatus** flag of pending SRBs is set to SRB\_STATUS\_BUS\_RESET.

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains a [**STORAGE\_BREAK\_RESERVATION\_REQUEST**](storage-break-reservation-request.md) structure that identifies the bus to reset.

## Input Buffer Length

The length of a [**STORAGE\_BREAK\_RESERVATION\_REQUEST**](storage-break-reservation-request.md) structure.

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

The **Information** field is set to zero. The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_INSUFFICIENT\_RESOURCES, STATUS\_NOT\_IMPLEMENTED, or STATUS\_INVALID\_DEVICE\_REQUEST.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_RESET\_BUS**](ioctl-storage-reset-bus.md)
</dt> <dt>

[**STORAGE\_BREAK\_RESERVATION\_REQUEST**](storage-break-reservation-request.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_STORAGE_BREAK_RESERVATION%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






