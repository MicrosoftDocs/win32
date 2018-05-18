---
title: IOCTL\_AACS\_GENERATE\_BINDING\_NONCE control code
description: Reads the Advanced Access Content System (AACS) binding nonce starting at the specified byte offset on the disc, as part of the protocol for writing to a protected data area.
ms.assetid: 'bb0fec4e-e6be-46e1-b6be-253dd0579ca6'
keywords: ["IOCTL_AACS_GENERATE_BINDING_NONCE control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_AACS_GENERATE_BINDING_NONCE
api_location:
- Ntddcdvd.h
api_type:
- HeaderDef
---

# IOCTL\_AACS\_GENERATE\_BINDING\_NONCE control code

Reads the Advanced Access Content System (AACS) binding nonce starting at the specified byte offset on the disc, as part of the protocol for writing to a protected data area.

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains a structure of type [**AACS\_READ\_BINDING\_NONCE**](aacs-read-binding-nonce.md) that specifies the [**DVD\_SESSION\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff553743), the starting logical block address and the number of sectors for which the logical unit should generate a binding nonce.

## Input Buffer Length

Length of an [**AACS\_READ\_BINDING\_NONCE**](aacs-read-binding-nonce.md).

## Output Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains the value of type [**AACS\_BINDING\_NONCE**](aacs-binding-nonce.md) that specifies the binding nonce.

## Output Buffer Length

Length of an [**AACS\_BINDING\_NONCE**](aacs-binding-nonce.md).

## Status block

The **Information** field is set to the number of bytes transferred. The **Status** field is set to STATUS\_SUCCESS or possibly STATUS\_INSUFFICIENT\_RESOURCES.

## Remarks

The IOCTL\_AACS\_GENERATE\_BINDING\_NONCE request corresponds to the part of the AACS authentication protocol that is responsible for writing to a protected data area. For a complete description of this protocol, see the *Advanced Access Content System, Introduction and Common Cryptographic Elements* specification that is published by Advanced Access Content System Licensing Administrator (AACS LA).

The IOCTL\_AACS\_GENERATE\_BINDING\_NONCE request requires a single available AGID during its processing, and the AGID is ***not*** automatically released after the request completes. The AGID remains valid until it is explicitly invalidated or until the drive generates a power-on reset, hard reset, or media ejection event. However, the AGID cannot be reused with other requests.

It is recommended that you wait for the completion of all other requests that use secure sessions with AGIDs before making an IOCTL\_AACS\_GENERATE\_BINDING\_NONCE request.

Clients that do not use file system support must set the **Handle** member of [**AACS\_READ\_BINDING\_NONCE**](aacs-read-binding-nonce.md) to INVALID\_HANDLE\_VALUE and specify explicit values for the **StartLBA** and **NumberOfSectors** members.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdvd.h (include Ntddcdvd.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_AACS_GENERATE_BINDING_NONCE%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





