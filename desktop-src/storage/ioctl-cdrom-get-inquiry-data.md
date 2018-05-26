---
title: IOCTL\_CDROM\_GET\_INQUIRY\_DATA control code
description: Returns the SCSI inquiry data for the CD-ROM device. This IOCTL can be used when a device has been exclusively locked with IOCTL\_CDROM\_EXCLUSIVE\_ACCESS.
ms.assetid: b327bdd4-f145-4211-a77c-80dffad16547
keywords:
- IOCTL_CDROM_GET_INQUIRY_DATA control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_CDROM_GET_INQUIRY_DATA
api_location:
- Ntddcdrm.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOCTL\_CDROM\_GET\_INQUIRY\_DATA control code

Returns the SCSI inquiry data for the CD-ROM device. This IOCTL can be used when a device has been exclusively locked with [**IOCTL\_CDROM\_EXCLUSIVE\_ACCESS**](ioctl-cdrom-exclusive-access.md).

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains the returned inquiry data. For a description of the layout of the inquiry data in the output buffer, see [**INQUIRYDATA**](inquirydata.md).

## Output Buffer Length

**Parameters.DeviceIoControl.OutputBufferLength** indicates the number of bytes that can be written to **Irp-&gt;AssociatedIrp.SystemBuffer**, which must be &gt;= **sizeof**([**INQUIRYDATA**](inquirydata.md)).

## Status block

The **Information** field contains the number of bytes returned in the output buffer. The **Status** field indicates the results of the operation.

## Remarks

TBD

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_CDROM\_EXCLUSIVE\_ACCESS**](ioctl-cdrom-exclusive-access.md)
</dt> <dt>

[**INQUIRYDATA**](inquirydata.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_CDROM_GET_INQUIRY_DATA%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






