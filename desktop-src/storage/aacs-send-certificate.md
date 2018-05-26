---
title: AACS\_SEND\_CERTIFICATE structure
description: The AACS\_SEND\_CERTIFICATE structure is a wrapper for both an Advanced Access Content System (AACS) certificate and an Authentication Grant Identifier (AGID).
ms.assetid: e0071ee1-7675-4029-b457-e7c26e642c31
keywords:
- AACS_SEND_CERTIFICATE structure Storage Devices
- PAACS_SEND_CERTIFICATE structure pointer Storage Devices
topic_type:
- apiref
api_name:
- AACS_SEND_CERTIFICATE
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

# AACS\_SEND\_CERTIFICATE structure

The AACS\_SEND\_CERTIFICATE structure is a wrapper for both an Advanced Access Content System (AACS) certificate and an Authentication Grant Identifier (AGID).

## Syntax


```C++
typedef struct _AACS_SEND_CERTIFICATE {
  DVD_SESSION_ID   SessionId;
  AACS_CERTIFICATE Certificate;
} AACS_SEND_CERTIFICATE, *PAACS_SEND_CERTIFICATE;
```



## Members

<dl> <dt>

**SessionId**
</dt> <dd>

A value of type DVD\_SESSION\_ID that specifies an AGID.

</dd> <dt>

**Certificate**
</dt> <dd>

A structure of type [**AACS\_CERTIFICATE**](aacs-certificate.md) that specifies the certificate to retrieve.

</dd> </dl>

## Remarks

Clients send an Advanced Access Content System (AACS) certificate with an [**IOCTL\_AACS\_SEND\_CERTIFICATE**](ioctl-aacs-send-certificate.md) request. Clients retrieve an AACS certificate with an [**IOCTL\_AACS\_GET\_CERTIFICATE**](ioctl-aacs-get-certificate.md) request.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdvd.h (include Ntddcdvd.h)</dt> </dl> |



## See also

<dl> <dt>

[**AACS\_CERTIFICATE**](aacs-certificate.md)
</dt> <dt>

[**DVD\_SESSION\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff553743)
</dt> <dt>

[**IOCTL\_AACS\_GET\_CERTIFICATE**](ioctl-aacs-get-certificate.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AACS_SEND_CERTIFICATE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






