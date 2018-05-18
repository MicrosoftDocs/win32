---
title: AACS\_SERIAL\_NUMBER structure
description: The AACS\_SERIAL\_NUMBER structure contains an Advanced Access Content System (AACS) serial number and corresponding message authentication code (MAC).
ms.assetid: '1436c8a5-9160-41d8-acc1-0af6acadfdba'
keywords: ["AACS_SERIAL_NUMBER structure Storage Devices", "PAACS_SERIAL_NUMBER structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- AACS_SERIAL_NUMBER
api_location:
- ntddcdvd.h
api_type:
- HeaderDef
---

# AACS\_SERIAL\_NUMBER structure

The AACS\_SERIAL\_NUMBER structure contains an Advanced Access Content System (AACS) serial number and corresponding message authentication code (MAC).

## Syntax


```C++
typedef struct _AACS_SERIAL_NUMBER {
  UCHAR PrerecordedSerialNumber[16];
  UCHAR MAC[16];
} AACS_SERIAL_NUMBER, *PAACS_SERIAL_NUMBER;
```



## Members

<dl> <dt>

**PrerecordedSerialNumber**
</dt> <dd>

The serial number.

</dd> <dt>

**MAC**
</dt> <dd>

The message authentication code (MAC) that the client uses to verify that the serial number is for the current AACS authentication sequence.

</dd> </dl>

## Remarks

Clients retrieve the AACS serial number with an [**IOCTL\_AACS\_READ\_SERIAL\_NUMBER**](ioctl-aacs-read-serial-number.md) request.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdvd.h (include Ntddcdvd.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_AACS\_READ\_SERIAL\_NUMBER**](ioctl-aacs-read-serial-number.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AACS_SERIAL_NUMBER%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






