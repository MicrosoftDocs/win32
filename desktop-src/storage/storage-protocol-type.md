---
title: STORAGE\_PROTOCOL\_TYPE enumeration
description: This enumeration is used to define the different storage command protocols that are used between software and hardware.
ms.assetid: 3CC4DF0A-26F1-4825-AD89-D56B0D5F4AC6
keywords:
- STORAGE_PROTOCOL_TYPE enumeration Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_PROTOCOL_TYPE
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# STORAGE\_PROTOCOL\_TYPE enumeration

This enumeration is used to define the different storage command protocols that are used between software and hardware.

## Syntax


```C++
typedef enum _STORAGE_PROTOCOL_TYPE { 
  ProtocolTypeUnknown      = 0,   // 0x0
  ProtocolTypeScsi,
  ProtocolTypeAta,
  ProtocolTypeNvme,
  ProtocolTypeSd,
  ProtocolTypeUfs,
  ProtocolTypeProprietary  = 126, // 0x7E
  ProtocolTypeMaxReserved  = 127 // 0x7F
} STORAGE_PROTOCOL_TYPE;
```



## Constants

<dl> <dt>

<span id="ProtocolTypeUnknown"></span><span id="protocoltypeunknown"></span><span id="PROTOCOLTYPEUNKNOWN"></span>**ProtocolTypeUnknown**
</dt> <dd>

Unknown protocol type.

</dd> <dt>

<span id="ProtocolTypeScsi"></span><span id="protocoltypescsi"></span><span id="PROTOCOLTYPESCSI"></span>**ProtocolTypeScsi**
</dt> <dd>

SCSI protocol type.

</dd> <dt>

<span id="ProtocolTypeAta"></span><span id="protocoltypeata"></span><span id="PROTOCOLTYPEATA"></span>**ProtocolTypeAta**
</dt> <dd>

ATA protocol type.

</dd> <dt>

<span id="ProtocolTypeNvme"></span><span id="protocoltypenvme"></span><span id="PROTOCOLTYPENVME"></span>**ProtocolTypeNvme**
</dt> <dd>

NVMe protocol type.

</dd> <dt>

<span id="ProtocolTypeSd"></span><span id="protocoltypesd"></span><span id="PROTOCOLTYPESD"></span>**ProtocolTypeSd**
</dt> <dd>

SD protocol type.

</dd> <dt>

<span id="ProtocolTypeUfs"></span><span id="protocoltypeufs"></span><span id="PROTOCOLTYPEUFS"></span>**ProtocolTypeUfs**
</dt> <dd>

UFS protocol type.

</dd> <dt>

<span id="ProtocolTypeProprietary"></span><span id="protocoltypeproprietary"></span><span id="PROTOCOLTYPEPROPRIETARY"></span>**ProtocolTypeProprietary**
</dt> <dd>

Vendor-specific protocol type.

</dd> <dt>

<span id="ProtocolTypeMaxReserved"></span><span id="protocoltypemaxreserved"></span><span id="PROTOCOLTYPEMAXRESERVED"></span>**ProtocolTypeMaxReserved**
</dt> <dd>

Reserved.

</dd> </dl>

## Remarks

Protocol types that are 128 (0x80) and above in value are reserved for Microsoft use.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_PROTOCOL_TYPE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





