---
title: ISCSI\_DIGEST\_TYPES enumeration
description: The ISCSI\_DIGEST\_TYPES enumeration indicates the digest type.
ms.assetid: 0515dd76-ef1f-4f0f-a7d7-1b3b07e0523d
keywords:
- ISCSI_DIGEST_TYPES enumeration Storage Devices
- PISCSI_DIGEST_TYPES enumeration pointer Storage Devices
topic_type:
- apiref
api_name:
- ISCSI_DIGEST_TYPES
api_location:
- iscsidef.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ISCSI\_DIGEST\_TYPES enumeration

The ISCSI\_DIGEST\_TYPES enumeration indicates the digest type.

## Syntax


```C++
typedef enum  { 
  ISCSI_DIGEST_TYPE_NONE    = 0,
  ISCSI_DIGEST_TYPE_CRC32C  = 1
} ISCSI_DIGEST_TYPES, *PISCSI_DIGEST_TYPES;
```



## Constants

<dl> <dt>

<span id="ISCSI_DIGEST_TYPE_NONE"></span><span id="iscsi_digest_type_none"></span>**ISCSI\_DIGEST\_TYPE\_NONE**
</dt> <dd>

There is no usable digest that guarantees data integrity.

</dd> <dt>

<span id="ISCSI_DIGEST_TYPE_CRC32C"></span><span id="iscsi_digest_type_crc32c"></span>**ISCSI\_DIGEST\_TYPE\_CRC32C**
</dt> <dd>

The digest that guarantees data integrity uses a 32-bit cyclic redundancy check.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsidef.h (include Iscsidef.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ISCSI_DIGEST_TYPES%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





