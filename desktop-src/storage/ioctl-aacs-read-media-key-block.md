---
title: IOCTL\_AACS\_READ\_MEDIA\_KEY\_BLOCK control code
description: Queries the logical unit for the Media Key Block (MKB).
ms.assetid: '08852f41-1836-4c55-bf6f-0246caa2c8bd'
keywords: ["IOCTL_AACS_READ_MEDIA_KEY_BLOCK control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_AACS_READ_MEDIA_KEY_BLOCK
api_location:
- Ntddcdvd.h
api_type:
- HeaderDef
---

# IOCTL\_AACS\_READ\_MEDIA\_KEY\_BLOCK control code

Queries the logical unit for the Media Key Block (MKB).

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains the AACS\_LAYER\_NUMBER number of the layer. The AACS\_LAYER\_NUMBER is an unsigned long integer value in the range 0 to 255 inclusive that specifies the layer of the media to which a command applies.

`typedef ULONG AACS_LAYER_NUMBER, *PAACS_LAYER_NUMBER;`

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** in the I/O stack location indicates the size, in bytes, of the buffer, which must be &gt;= **sizeof**(AACS\_LAYER\_NUMBER).

## Output Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains an opaque, variable-length MKB. The size of the MKB is always a multiple of 32,768 (0x8000).

## Output Buffer Length

Length of a variable-length MKB.

## Status block

The **Information** field is set to the number of bytes transferred. The **Status** field is set to STATUS\_SUCCESS if the operation succeeds. If **Irp-&gt;AssociatedIrp.SystemBuffer** is **NULL** or the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** is not sufficient to contain the full MKB, the operation fails and returns a status of STATUS\_BUFFER\_TOO\_SMALL, and the required buffer size is returned in **IoStatus.Information**.

## Remarks

The storage stack uses a READ DISC STRUCTURE command (format 0x17) with Advanced Access Control System (AACS) extensions to retrieve the MKB. IOCTL\_AACS\_READ\_MEDIA\_KEY\_BLOCK request will not work if the media in the logical unit is not AACS protected.

Unlike the MKB that is used with Content-Scrambling System (CSS) encryption, AACS MKBs are self-protected with digital signatures. The MKB structure is fully documented in the *Advanced Access Content System, Introduction and Common Cryptographic Elements* specification that is published by Advanced Access Content System Licensing Administrator (AACS LA).

The IOCTL\_AACS\_READ\_MEDIA\_KEY\_BLOCK request corresponds to one of the steps of the Advanced Access Content System (AACS) authentication algorithm (AACS-Auth). For a complete description of AACS-Auth, see the *Advanced Access Content System, Introduction and Common Cryptographic Elements* specification.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdvd.h (include Ntddcdvd.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_AACS_READ_MEDIA_KEY_BLOCK%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





