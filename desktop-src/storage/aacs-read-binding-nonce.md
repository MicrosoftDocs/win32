---
title: AACS\_READ\_BINDING\_NONCE structure
description: The AACS\_READ\_BINDING\_NONCE structure is a wrapper for the Authentication Grant Identifier (AGID) and logical block address (LBA)/length pair that are required to read a nonce.
ms.assetid: 5d017896-bb83-4ea3-9d28-b774213f86e9
keywords:
- AACS_READ_BINDING_NONCE structure Storage Devices
- PAACS_READ_BINDING_NONCE structure pointer Storage Devices
topic_type:
- apiref
api_name:
- AACS_READ_BINDING_NONCE
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

# AACS\_READ\_BINDING\_NONCE structure

The AACS\_READ\_BINDING\_NONCE structure is a wrapper for the Authentication Grant Identifier (AGID) and logical block address (LBA)/length pair that are required to read a nonce.

## Syntax


```C++
typedef struct _AACS_READ_BINDING_NONCE {
  DVD_SESSION_ID SessionId;
  ULONG          NumberOfSectors;
  ULONGLONG      StartLba;
  union {
    HANDLE    Handle;
    ULONGLONG ForceStructureLengthToMatch64bit;
  };
} AACS_READ_BINDING_NONCE, *PAACS_READ_BINDING_NONCE;
```



## Members

<dl> <dt>

**SessionId**
</dt> <dd>

A value of type DVD\_SESSION\_ID that specifies an AGID. The client obtains this value by a successful call to IOCTL\_AACS\_START\_SESSION.

</dd> <dt>

**NumberOfSectors**
</dt> <dd>

The number of sectors in the area for which the binding nonce is retrieved. To request the nonce for a file, the caller of IOCTL\_AACS\_READ\_BINDING\_NONCE must set this member to MAXULONGLONG.

</dd> <dt>

**StartLba**
</dt> <dd>

The starting logical block address of the area for which the binding nonce is retrieved. To request the nonce for a file, the caller of [**IOCTL\_AACS\_GENERATE\_BINDING\_NONCE**](ioctl-aacs-generate-binding-nonce.md) or [**IOCTL\_AACS\_READ\_BINDING\_NONCE**](ioctl-aacs-read-binding-nonce.md) must set this member to MAXULONGLONG.

</dd> <dt>

**Handle**
</dt> <dd>

The file handle. Callers of IOCTL\_AACS\_READ\_BINDING\_NONCE that use file system support can set this member to a file handle. If the caller does not use file system support, this member must have a value of INVALID\_HANDLE\_VALUE.

</dd> <dt>

**ForceStructureLengthToMatch64bit**
</dt> <dd></dd> </dl>

## Remarks

Clients retrieve the binding nonce with an [**IOCTL\_AACS\_GENERATE\_BINDING\_NONCE**](ioctl-aacs-generate-binding-nonce.md) request or an [**IOCTL\_AACS\_READ\_BINDING\_NONCE**](ioctl-aacs-read-binding-nonce.md) request.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdvd.h (include Ntddcdvd.h)</dt> </dl> |



## See also

<dl> <dt>

[**AACS\_BINDING\_NONCE**](aacs-binding-nonce.md)
</dt> <dt>

[**IOCTL\_AACS\_GENERATE\_BINDING\_NONCE**](ioctl-aacs-generate-binding-nonce.md)
</dt> <dt>

[**IOCTL\_AACS\_READ\_BINDING\_NONCE**](ioctl-aacs-read-binding-nonce.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AACS_READ_BINDING_NONCE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






