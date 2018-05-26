---
title: IOCTL\_AACS\_GET\_CHALLENGE\_KEY control code
description: Queries the logical unit for the devices challenge key. The challenge key consists of a point on an elliptic curve and its associated signature.
ms.assetid: 97c43a15-e120-44bd-8a5e-40b80aba646d
keywords:
- IOCTL_AACS_GET_CHALLENGE_KEY control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_AACS_GET_CHALLENGE_KEY
api_location:
- Ntddcdvd.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOCTL\_AACS\_GET\_CHALLENGE\_KEY control code

Queries the logical unit for the device's challenge key. The challenge key consists of a point on an elliptic curve and its associated signature.

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains a value of type [**DVD\_SESSION\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff553743) that specifies an Authentication Grant Identifier (AGID). The AGID identifies the secure session.

## Input Buffer Length

Length of a [**DVD\_SESSION\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff553743).

## Output Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains the drive challenge key with a format of [**AACS\_CHALLENGE\_KEY**](aacs-challenge-key.md).

## Output Buffer Length

Length of an [**AACS\_CHALLENGE\_KEY**](aacs-challenge-key.md).

## Status block

The **Information** field is set to the number of bytes transferred. The **Status** field is set to STATUS\_SUCCESS or possibly STATUS\_INSUFFICIENT\_RESOURCES.

## Remarks

The IOCTL\_AACS\_GET\_CHALLENGE\_KEY request corresponds to the step in the Advanced Access Content System (AACS) authentication algorithm (AACS-Auth) in which the drive provides the host with a point on the curve. For a complete description of AACS-Auth, see the *Advanced Access Content System, Introduction and Common Cryptographic Elements* specification that is published by Advanced Access Content System Licensing Administrator (AACS LA).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdvd.h (include Ntddcdvd.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_AACS_GET_CHALLENGE_KEY%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





