---
title: AACS\_BINDING\_NONCE structure
description: The AACS\_BINDING\_NONCE structure contains the binding nonce.
ms.assetid: '8bbefe34-9653-4868-894f-a77c1fc9939f'
keywords: ["AACS_BINDING_NONCE structure Storage Devices", "PAACS_BINDING_NONCE structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- AACS_BINDING_NONCE
api_location:
- ntddcdvd.h
api_type:
- HeaderDef
---

# AACS\_BINDING\_NONCE structure

The AACS\_BINDING\_NONCE structure contains the binding nonce.

## Syntax


```C++
typedef struct _AACS_BINDING_NONCE {
  UCHAR BindingNonce[16];
  UCHAR MAC[16];
} AACS_BINDING_NONCE, *PAACS_BINDING_NONCE;
```



## Members

<dl> <dt>

**BindingNonce**
</dt> <dd>

The binding nonce for the requested logical block address(es) (LBAs).

</dd> <dt>

**MAC**
</dt> <dd>

A message authentication code (MAC) that clients can use to verify that the binding nonce is for the current Advanced Access Content System (AACS) Authentication sequence.

</dd> </dl>

## Remarks

Clients retrieve the binding nonce with an [**IOCTL\_AACS\_READ\_BINDING\_NONCE**](ioctl-aacs-read-binding-nonce.md) request or an [**IOCTL\_AACS\_GENERATE\_BINDING\_NONCE**](ioctl-aacs-generate-binding-nonce.md) request.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdvd.h (include Ntddcdvd.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_AACS\_GENERATE\_BINDING\_NONCE**](ioctl-aacs-generate-binding-nonce.md)
</dt> <dt>

[**IOCTL\_AACS\_READ\_BINDING\_NONCE**](ioctl-aacs-read-binding-nonce.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AACS_BINDING_NONCE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






