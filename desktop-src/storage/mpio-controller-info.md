---
title: MPIO\_CONTROLLER\_INFO structure
description: The MPIO\_CONTROLLER\_INFO structure represents a storage controller.
ms.assetid: 30600e86-dd35-4498-91a8-14a722b2e868
keywords:
- MPIO_CONTROLLER_INFO structure Storage Devices
- PMPIO_CONTROLLER_INFO structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MPIO_CONTROLLER_INFO
api_location:
- mpiowmi.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MPIO\_CONTROLLER\_INFO structure

The MPIO\_CONTROLLER\_INFO structure represents a storage controller.

## Syntax


```C++
typedef struct _MPIO_CONTROLLER_INFO {
  ULONG IdentifierType;
  ULONG IdentifierLength;
  UCHAR Identifier[32];
  ULONG ControllerState;
  ULONG Pad;
  WCHAR AssociatedDsm[63 + 1];
} MPIO_CONTROLLER_INFO, *PMPIO_CONTROLLER_INFO;
```



## Members

<dl> <dt>

**IdentifierType**
</dt> <dd>

An unsigned 32-bitfield that represents the identifier type for the controller.

</dd> <dt>

**IdentifierLength**
</dt> <dd>

An unsigned 32-bitfield that represents the length of the controller's identifier.

</dd> <dt>

**Identifier**
</dt> <dd>

A 32-byte array that contains the actual identifier (serial number) of the controller.

</dd> <dt>

**ControllerState**
</dt> <dd>

An unsigned 32-bitfield that represents the controller state.

</dd> <dt>

**Pad**
</dt> <dd>

Should be zero.

</dd> <dt>

**AssociatedDsm**
</dt> <dd>

A string field of maximum length 63 characters. This string field returns the friendly name of the DSM that controls the devices that are exposed by this controller.

</dd> </dl>

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mpiowmi.h (include Mpiowmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MPIO_CONTROLLER_INFO%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





