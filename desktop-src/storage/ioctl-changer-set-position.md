---
title: IOCTL\_CHANGER\_SET\_POSITION control code
description: Sets the changer's robotic transport mechanism to the specified element address, typically to optimize moving or exchanging media by positioning the transport beforehand.
ms.assetid: 'cd4f5872-d2cb-42ee-b78c-6b7d48d41e34'
keywords: ["IOCTL_CHANGER_SET_POSITION control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_CHANGER_SET_POSITION
api_location:
- Ntddchgr.h
api_type:
- HeaderDef
---

# IOCTL\_CHANGER\_SET\_POSITION control code

Sets the changer's robotic transport mechanism to the specified element address, typically to optimize moving or exchanging media by positioning the transport beforehand.

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains a [**CHANGER\_SET\_POSITION**](changer-set-position.md) structure that specifies the transport to move and the destination. If the **Flip** member is **TRUE** and the device supports two-sided media, the media currently carried by the transport should be flipped.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** in the I/O stack location indicates the size, in bytes, of the parameter buffer, which must be &gt;= **sizeof**(CHANGER\_SET\_POSITION).

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

The **Information** field is set to **sizeof**(CHANGER\_SET\_POSITION). The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_INFO\_LENGTH\_MISMATCH, STATUS\_INSUFFICIENT\_RESOURCES, STATUS\_INVALID\_DEVICE\_REQUEST, or STATUS\_INVALID\_PARAMETER.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddchgr.h (include Ntddchgr.h)</dt> </dl> |



## See also

<dl> <dt>

[**CHANGER\_SET\_POSITION**](changer-set-position.md)
</dt> <dt>

[**ChangerSetPosition**](changersetposition.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_CHANGER_SET_POSITION%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






