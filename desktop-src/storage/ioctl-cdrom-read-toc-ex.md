---
title: IOCTL\_CDROM\_READ\_TOC\_EX control code
description: Queries the target device for the table of contents (TOC), the program memory area (PMA), and the absolute time in pregroove (ATIP).
ms.assetid: '279df233-9164-4c80-b31f-1d4cdc1073fa'
keywords: ["IOCTL_CDROM_READ_TOC_EX control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_CDROM_READ_TOC_EX
api_location:
- ntddcdrm.h
api_type:
- HeaderDef
---

# IOCTL\_CDROM\_READ\_TOC\_EX control code

Queries the target device for the table of contents (TOC), the program memory area (PMA), and the absolute time in pregroove (ATIP). If the media is not a CD-ROM and does not support a TOC, this IOCTL returns information similar to that of a CD-ROM TOC. This is required for compatibility with some legacy initiator environments.

## Input Buffer

**Irp-&gt;AssociatedIrp.SystemBuffer** points to a buffer of type [**CDROM\_READ\_TOC\_EX**](cdrom-read-toc-ex.md) whose contents indicate what information should be retrieved from the target device.

**Parameters.Read.Length** in the I/O stack location indicates the size, in bytes, of the information to be retrieved from the target device.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** in the I/O stack location indicates the size, in bytes, of the input buffer, which must be &gt;= **sizeof**(CDROM\_READ\_TOC\_EX).

## Output Buffer

The driver returns the query data in the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Output Buffer Length

**Parameters.DeviceIoControl.OutputBufferLength** in the I/O stack location indicates the size, in bytes, of the output buffer, which must be &gt;= MINIMUM\_CDROM\_READ\_TOC\_EX\_SIZE.

## Status block

The **Information** field is set to the number of bytes returned. The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_BUFFER\_TOO\_SMALL or STATUS\_INSUFFICIENT\_RESOURCES.

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available in Windows XP and later operating systems.<br/>                                            |
| Header<br/>  | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**CDROM\_READ\_TOC\_EX**](cdrom-read-toc-ex.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_CDROM_READ_TOC_EX%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






