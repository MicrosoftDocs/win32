---
title: IOCTL\_MPIO\_PASS\_THROUGH\_PATH\_DIRECT\_EX control code
description: The IOCTL\_MPIO\_PASS\_THROUGH\_PATH\_DIRECT\_EX control code request is the extended version of the IOCTL\_MPIO\_PASS\_THROUGH\_PATH\_DIRECT request. This request provides support for bidirectional data transfers and allows a command data block (CDB) 16 bytes.
ms.assetid: '2B5AF281-C080-4ED9-9C58-5757CDE0117A'
keywords: ["IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT_EX control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT_EX
api_location:
- Ntddscsi.h
api_type:
- HeaderDef
---

# IOCTL\_MPIO\_PASS\_THROUGH\_PATH\_DIRECT\_EX control code

The **IOCTL\_MPIO\_PASS\_THROUGH\_PATH\_DIRECT\_EX** control code request is the extended version of the [**IOCTL\_MPIO\_PASS\_THROUGH\_PATH\_DIRECT**](ioctl-mpio-pass-through-path-direct.md) request. This request provides support for bidirectional data transfers and allows a command data block (CDB) &gt; 16 bytes.

This I/O control code allows an application or kernel driver to send a SCSI command to a designated real LUN. The following restrictions apply to the use of this I/O control code:

-   If a class driver for the pseudo LUN exists, the application must send the request to that class driver. Thus, an application can send this request directly to an MPIO only if there is no class driver for the device.

-   All pass-through requests must be synchronous.

-   Applications do not require administrative privileges to send a pass-through request to a device, but they must have read/write access to the device.

-   The request comprises a SCSI pass-through request (in an embedded [**SCSI\_PASS\_THROUGH\_DIRECT**](scsi-pass-through-direct.md) structure) as well as certain directives.

-   The SCSI pass-through structure should meet the requirements for such, as described in [**SCSI\_PASS\_THROUGH\_DIRECT**](scsi-pass-through-direct.md).

-   If the request is to be sent through the DSM that claimed the real LUN, that must be indicated. In such a case, the DSM itself must indicate the same real LUN. Otherwise, the request will fail.

-   The request must specify the real LUN that is comprised by the pseudo LUN in terms of the former's SCSI address or its MPIO **PathId**, but not both.

## Input Buffer

**Parameters.DeviceIoControl.InputBufferLength** indicates the size, in bytes, of the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Input Buffer Length

The buffer must be at least **sizeof**(MPIO\_PASS\_THROUGH\_PATH\_DIRECT\_EX) or, if sent by a 32-bit application in a 64-bit operating system, **sizeof**(MPIO\_PASS\_THROUGH\_PATH\_DIRECT32\_EX).

## Output Buffer

The port driver returns any request-sense data and any data that is transferred from the device to the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Output Buffer Length

The **SenseInfoLength** and **DataOutTransferLength** in the embedded [**SCSI\_PASS\_THROUGH\_DIRECT\_EX**](scsi-pass-through-direct-ex.md) structure are updated to indicate the amount of data that is transferred.

## Status block

The **Information** field is set to the number of bytes returned in the output buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**. The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_BUFFER\_TOO\_SMALL or STATUS\_INVALID\_PARAMETER if the input **Length** value in the embedded [**SCSI\_PASS\_THROUGH\_DIRECT\_EX**](scsi-pass-through-direct-ex.md) is improperly set.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddscsi.h (include Ntddscsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**MPIO\_PASS\_THROUGH\_PATH\_DIRECT\_EX**](mpio-pass-through-path-direct-ex.md)
</dt> <dt>

[**SCSI\_PASS\_THROUGH\_DIRECT\_EX**](scsi-pass-through-direct-ex.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT_EX%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






