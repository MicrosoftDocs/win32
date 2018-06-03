---
title: PDO\_TYPE enumeration
description: This enumeration describes the types of Physical Device Objects (PDOs).
ms.assetid: 9695d55c-a214-4bba-aba9-38dfa7f54ec9
keywords:
- PDO_TYPE enumeration Storage Devices
topic_type:
- apiref
api_name:
- PDO_TYPE
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

# PDO\_TYPE enumeration

This enumeration describes the types of Physical Device Objects (PDOs).

## Syntax


```C++
typedef enum _PDO_TYPE { 
  PDO_TYPE_UNDEFINED  = 0,
  PDO_TYPE_DISK       = 1,
  PDO_TYPE_CONTROL    = 2,
  PDO_TYPE_SILO       = 3,
  PDO_TYPE_THIS       = 256
} PDO_TYPE;
```



## Constants

<dl> <dt>

<span id="PDO_TYPE_UNDEFINED"></span><span id="pdo_type_undefined"></span>**PDO\_TYPE\_UNDEFINED**
</dt> <dd>

Types either enumerated or provided as filter parameter to [**IOCTL\_EHSTOR\_DEVICE\_ENUMERATE\_PDOS**](ioctl-ehstor-device-enumerate-pdos.md)

</dd> <dt>

<span id="PDO_TYPE_DISK"></span><span id="pdo_type_disk"></span>**PDO\_TYPE\_DISK**
</dt> <dd>

This value indicates the PDO is for a logical disk device.

</dd> <dt>

<span id="PDO_TYPE_CONTROL"></span><span id="pdo_type_control"></span>**PDO\_TYPE\_CONTROL**
</dt> <dd>

This value indicates the PDO is for a logical control device.

</dd> <dt>

<span id="PDO_TYPE_SILO"></span><span id="pdo_type_silo"></span>**PDO\_TYPE\_SILO**
</dt> <dd>

This value indicates the PDO is for a logical silo device.

</dd> <dt>

<span id="PDO_TYPE_THIS"></span><span id="pdo_type_this"></span>**PDO\_TYPE\_THIS**
</dt> <dd></dd> </dl>

## Remarks

## Requirements



|                   |                                                                                                                  |
|-------------------|------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>EhStorIoctl.h (include EhStorIoctl.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_EHSTOR\_DEVICE\_ENUMERATE\_PDOS**](ioctl-ehstor-device-enumerate-pdos.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PDO_TYPE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






