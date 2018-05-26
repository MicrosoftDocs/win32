---
title: PDO\_INFORMATION structure
description: The PDO\_INFORMATION structure represents a device-path pairing, which is an instance of a LUN through a particular path.
ms.assetid: 26ce460f-b12d-4e5e-994a-047a1853325d
keywords:
- PDO_INFORMATION structure Storage Devices
- PPDO_INFORMATION structure pointer Storage Devices
topic_type:
- apiref
api_name:
- PDO_INFORMATION
api_location:
- mpiodisk.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PDO\_INFORMATION structure

The PDO\_INFORMATION structure represents a device-path pairing, which is an instance of a LUN through a particular path.

## Syntax


```C++
typedef struct _PDO_INFORMATION {
  PDOSCSI_ADDR ScsiAddress;
  ULONG        DeviceState;
  ULONGLONG    PathIdentifier;
  ULONG        IdentifierType;
  ULONG        IdentifierLength;
  UCHAR        Identifier[32];
  UCHAR        Pad[4];
} PDO_INFORMATION, *PPDO_INFORMATION;
```



## Members

<dl> <dt>

**ScsiAddress**
</dt> <dd>

A PDOSCSI\_ADDR structure that represents the SCSI address of the LUN's instance that corresponds to a particular path.

</dd> <dt>

**DeviceState**
</dt> <dd>

An unsigned 32-bitfield that represents whether the path, through which this instance of the LUN was exposed, is usable.

</dd> <dt>

**PathIdentifier**
</dt> <dd>

An unsigned 64-bitfield that represents the identifier that is associated with the path through which this instance of the LUN is exposed.

</dd> <dt>

**IdentifierType**
</dt> <dd>

An unsigned 32-bitfield that represents the identifier type of the LUN's controller.

</dd> <dt>

**IdentifierLength**
</dt> <dd>

An unsigned 32-bitfield that represents the length of the identifier of the LUN's controller.

</dd> <dt>

**Identifier**
</dt> <dd>

An unsigned 64-bitfield that represents the identifier that is associated with the path through which this instance of the LUN is exposed.

</dd> <dt>

**Pad**
</dt> <dd>

Should be zero.

</dd> </dl>

## Requirements



|                   |                                                                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mpiodisk.h (include Mpiowmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PDO_INFORMATION%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





