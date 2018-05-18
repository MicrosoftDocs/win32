---
title: AACS\_VOLUME\_ID structure
description: The AACS\_VOLUME\_ID structure contains an Advanced Access Content System (AACS) volume ID and the corresponding message authentication code (MAC).
ms.assetid: '3ad7a253-cc55-4613-8086-b8d08d9bd54f'
keywords: ["AACS_VOLUME_ID structure Storage Devices", "PAACS_VOLUME_ID structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- AACS_VOLUME_ID
api_location:
- ntddcdvd.h
api_type:
- HeaderDef
---

# AACS\_VOLUME\_ID structure

The AACS\_VOLUME\_ID structure contains an Advanced Access Content System (AACS) volume ID and the corresponding message authentication code (MAC).

## Syntax


```C++
typedef struct _AACS_VOLUME_ID {
  UCHAR VolumeID[16];
  UCHAR MAC[16];
} AACS_VOLUME_ID, *PAACS_VOLUME_ID;
```



## Members

<dl> <dt>

**VolumeID**
</dt> <dd>

The volume identifier.

</dd> <dt>

**MAC**
</dt> <dd>

The message authentication code (MAC) that the client uses to verify that the volume identifier is for the current AACS authentication sequence.

</dd> </dl>

## Remarks

Clients retrieve an AACS volume ID with an [**IOCTL\_AACS\_READ\_VOLUME\_ID**](ioctl-aacs-read-volume-id.md) request.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdvd.h (include Ntddcdvd.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_AACS\_READ\_VOLUME\_ID**](ioctl-aacs-read-volume-id.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AACS_VOLUME_ID%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






