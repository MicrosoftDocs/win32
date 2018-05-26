---
title: STORAGE\_BUS\_TYPE enumeration
description: The STORAGE\_BUS\_TYPE enumeration provides a symbolic means of representing storage bus types.
ms.assetid: 4c56f6e6-0909-447a-95f9-e131c0ac0a0c
keywords:
- STORAGE_BUS_TYPE enumeration Storage Devices
- PSTORAGE_BUS_TYPE enumeration pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_BUS_TYPE
api_location:
- ntddstor.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# STORAGE\_BUS\_TYPE enumeration

The STORAGE\_BUS\_TYPE enumeration provides a symbolic means of representing storage bus types.

## Syntax


```C++
typedef enum _STORAGE_BUS_TYPE { 
  BusTypeUnknown            = 0x00,
  BusTypeScsi               = 0x1,
  BusTypeAtapi              = 0x2,
  BusTypeAta                = 0x3,
  BusType1394               = 0x4,
  BusTypeSsa                = 0x5,
  BusTypeFibre              = 0x6,
  BusTypeUsb                = 0x7,
  BusTypeRAID               = 0x8,
  BusTypeiScsi              = 0x9,
  BusTypeSas                = 0xA,
  BusTypeSata               = 0xB,
  BusTypeSd                 = 0xC,
  BusTypeMmc                = 0xD,
  BusTypeVirtual            = 0xE,
  BusTypeFileBackedVirtual  = 0xF,
  BusTypeSpaces             = 0x10,
  BusTypeMax                = 0x11,
  BusTypeMaxReserved        = 0x7F
} STORAGE_BUS_TYPE, *PSTORAGE_BUS_TYPE;
```



## Constants

<dl> <dt>

<span id="BusTypeUnknown"></span><span id="bustypeunknown"></span><span id="BUSTYPEUNKNOWN"></span>**BusTypeUnknown**
</dt> <dd>

Indicates an unknown bus type.

</dd> <dt>

<span id="BusTypeScsi"></span><span id="bustypescsi"></span><span id="BUSTYPESCSI"></span>**BusTypeScsi**
</dt> <dd>

Indicates a small computer system interface (SCSI) bus.

</dd> <dt>

<span id="BusTypeAtapi"></span><span id="bustypeatapi"></span><span id="BUSTYPEATAPI"></span>**BusTypeAtapi**
</dt> <dd>

Indicates an AT Attachment Packet Interface (ATAPI) bus.

</dd> <dt>

<span id="BusTypeAta"></span><span id="bustypeata"></span><span id="BUSTYPEATA"></span>**BusTypeAta**
</dt> <dd>

Indicates an advanced technology attachment (ATA) bus.

</dd> <dt>

<span id="BusType1394"></span><span id="bustype1394"></span><span id="BUSTYPE1394"></span>**BusType1394**
</dt> <dd>

Indicates an IEEE 1394 bus.

</dd> <dt>

<span id="BusTypeSsa"></span><span id="bustypessa"></span><span id="BUSTYPESSA"></span>**BusTypeSsa**
</dt> <dd>

Indicates a serial storage architecture (SSA) bus.

</dd> <dt>

<span id="BusTypeFibre"></span><span id="bustypefibre"></span><span id="BUSTYPEFIBRE"></span>**BusTypeFibre**
</dt> <dd>

Indicates a fibre channel bus type.

</dd> <dt>

<span id="BusTypeUsb"></span><span id="bustypeusb"></span><span id="BUSTYPEUSB"></span>**BusTypeUsb**
</dt> <dd>

Indicates a USB bus type.

</dd> <dt>

<span id="BusTypeRAID"></span><span id="bustyperaid"></span><span id="BUSTYPERAID"></span>**BusTypeRAID**
</dt> <dd>

Indicates a bus for a redundant array of independent disks (RAID).

</dd> <dt>

<span id="BusTypeiScsi"></span><span id="bustypeiscsi"></span><span id="BUSTYPEISCSI"></span>**BusTypeiScsi**
</dt> <dd>

Indicates an iSCSI bus.

</dd> <dt>

<span id="BusTypeSas"></span><span id="bustypesas"></span><span id="BUSTYPESAS"></span>**BusTypeSas**
</dt> <dd>

Indicates a serial-attached SCSI bus.

</dd> <dt>

<span id="BusTypeSata"></span><span id="bustypesata"></span><span id="BUSTYPESATA"></span>**BusTypeSata**
</dt> <dd>

Indicates a serial ATA bus.

</dd> <dt>

<span id="BusTypeSd"></span><span id="bustypesd"></span><span id="BUSTYPESD"></span>**BusTypeSd**
</dt> <dd>

Indicates a secure digital bus.

</dd> <dt>

<span id="BusTypeMmc"></span><span id="bustypemmc"></span><span id="BUSTYPEMMC"></span>**BusTypeMmc**
</dt> <dd>

Indicates a multimedia card bus.

</dd> <dt>

<span id="BusTypeVirtual"></span><span id="bustypevirtual"></span><span id="BUSTYPEVIRTUAL"></span>**BusTypeVirtual**
</dt> <dd>

Indicates a virtual storage bus.

</dd> <dt>

<span id="BusTypeFileBackedVirtual"></span><span id="bustypefilebackedvirtual"></span><span id="BUSTYPEFILEBACKEDVIRTUAL"></span>**BusTypeFileBackedVirtual**
</dt> <dd>

Indicates a virtual file backed storage bus.

</dd> <dt>

<span id="BusTypeSpaces"></span><span id="bustypespaces"></span><span id="BUSTYPESPACES"></span>**BusTypeSpaces**
</dt> <dd>

Indicates a storage spaces bus.

</dd> <dt>

<span id="BusTypeMax"></span><span id="bustypemax"></span><span id="BUSTYPEMAX"></span>**BusTypeMax**
</dt> <dd>

Indicates the maximum value for this value.

</dd> <dt>

<span id="BusTypeMaxReserved"></span><span id="bustypemaxreserved"></span><span id="BUSTYPEMAXRESERVED"></span>**BusTypeMaxReserved**
</dt> <dd></dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_BUS_TYPE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





