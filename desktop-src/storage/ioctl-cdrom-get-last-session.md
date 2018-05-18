---
title: IOCTL\_CDROM\_GET\_LAST\_SESSION control code
description: Queries the device for the first complete session number, the last complete session number, and the last complete session starting address.
ms.assetid: 'a05da124-f486-4658-87d8-6c1b423694b3'
keywords: ["IOCTL_CDROM_GET_LAST_SESSION control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_CDROM_GET_LAST_SESSION
api_location:
- ntddcdrm.h
api_type:
- HeaderDef
---

# IOCTL\_CDROM\_GET\_LAST\_SESSION control code

Queries the device for the first complete session number, the last complete session number, and the last complete session starting address. This request is the same as an [**IOCTL\_CDROM\_READ\_TOC\_EX**](ioctl-cdrom-read-toc-ex.md) request with a format of CDROM\_READ\_TOC\_EX\_FORMAT\_SESSION. For more information on the CDROM\_READ\_TOC\_EX\_FORMAT\_SESSION format, see the description of the **Format** member of the [**CDROM\_READ\_TOC\_EX**](cdrom-read-toc-ex.md) structure.

On output, if the value in the **FirstCompleteSession** member of [**CDROM\_TOC\_SESSION\_DATA**](cdrom-toc-session-data.md) is the same as the value in the **LastCompleteSession** member, the disc is not multisession.

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

The driver returns the query data in a [**CDROM\_TOC\_SESSION\_DATA**](cdrom-toc-session-data.md) structure at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Output Buffer Length

Length of a [**CDROM\_TOC\_SESSION\_DATA**](cdrom-toc-session-data.md) structure.

## Status block

The **Information** field is set to the number of bytes returned. The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_BUFFER\_TOO\_SMALL or STATUS\_INSUFFICIENT\_RESOURCES.

## Remarks

TBD

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_CDROM_GET_LAST_SESSION%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





