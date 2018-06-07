---
title: PDO\_CAPS enumeration
description: This enumeration describes the capabilities of Physical Device Objects (PDOs).
ms.assetid: 78b6f3c7-bb42-4e93-8128-28b6f8e11dda
keywords:
- PDO_CAPS enumeration Storage Devices
topic_type:
- apiref
api_name:
- PDO_CAPS
api_location:
- EhStorIoctl.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# PDO\_CAPS enumeration

This enumeration describes the capabilities of Physical Device Objects (PDOs).

## Syntax


```C++
typedef enum _PDO_CAPS { 
  PDO_CAPABILITY_UNDEFINED     = 0,
  PDO_CAPABILITY_INC512_SET    = 1,
  PDO_CAPABILITY_INC512_CLEAR  = 2
} PDO_CAPS;
```



## Constants

<dl> <dt>

<span id="PDO_CAPABILITY_UNDEFINED"></span><span id="pdo_capability_undefined"></span>**PDO\_CAPABILITY\_UNDEFINED**
</dt> <dd>

Command data block size granularity is undefined.

</dd> <dt>

<span id="PDO_CAPABILITY_INC512_SET"></span><span id="pdo_capability_inc512_set"></span>**PDO\_CAPABILITY\_INC512\_SET**
</dt> <dd>

Command data block size granularity of 512 bytes is supported.

</dd> <dt>

<span id="PDO_CAPABILITY_INC512_CLEAR"></span><span id="pdo_capability_inc512_clear"></span>**PDO\_CAPABILITY\_INC512\_CLEAR**
</dt> <dd>

Command data block size granularity of 1 byte is supported.

</dd> </dl>

## Remarks

A silo must support either PDO\_CAPABILITY\_INC512\_SET or PDO\_CAPABILITY\_INC512\_CLEAR. It may also indicate that both values are supported by returning a logical OR of these two bits.

## Requirements



|                   |                                                                                                                  |
|-------------------|------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>EhStorIoctl.h (include EhStorIoctl.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PDO_CAPS%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





