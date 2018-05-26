---
title: AACS\_CHALLENGE\_KEY structure
description: The AACS\_CHALLENGE\_KEY structure contains the challenge key that the device sends to the host.
ms.assetid: b1eb7978-cbfc-4ffd-b345-a320e9152f03
keywords:
- AACS_CHALLENGE_KEY structure Storage Devices
- PAACS_CHALLENGE_KEY structure pointer Storage Devices
topic_type:
- apiref
api_name:
- AACS_CHALLENGE_KEY
api_location:
- ntddcdvd.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AACS\_CHALLENGE\_KEY structure

The AACS\_CHALLENGE\_KEY structure contains the challenge key that the device sends to the host.

## Syntax


```C++
typedef struct _AACS_CHALLENGE_KEY {
  UCHAR EllipticCurvePoint[40];
  UCHAR Signature[40];
} AACS_CHALLENGE_KEY, *PAACS_CHALLENGE_KEY;
```



## Members

<dl> <dt>

**EllipticCurvePoint**
</dt> <dd>

The elliptical curve (ECC) point data.

</dd> <dt>

**Signature**
</dt> <dd>

The signature that the client uses to verify that the ECC point is valid for the current Advanced Access Content System (AACS) authentication sequence.

</dd> </dl>

## Remarks

Clients retrieve the Advanced Access Content System (AACS) challenge key with an [**IOCTL\_AACS\_GET\_CHALLENGE\_KEY**](ioctl-aacs-get-challenge-key.md) request. Clients send an AACS challenge key to the logical unit in an [**AACS\_SEND\_CHALLENGE\_KEY**](aacs-send-challenge-key.md) structure with an [**IOCTL\_AACS\_SEND\_CHALLENGE\_KEY**](ioctl-aacs-send-challenge-key.md).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdvd.h (include Ntddcdvd.h)</dt> </dl> |



## See also

<dl> <dt>

[**AACS\_SEND\_CHALLENGE\_KEY**](aacs-send-challenge-key.md)
</dt> <dt>

[**IOCTL\_AACS\_GET\_CHALLENGE\_KEY**](ioctl-aacs-get-challenge-key.md)
</dt> <dt>

[**IOCTL\_AACS\_SEND\_CHALLENGE\_KEY**](ioctl-aacs-send-challenge-key.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AACS_CHALLENGE_KEY%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






