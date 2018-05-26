---
title: MPIO\_ADAPTER\_INFORMATION structure
description: The MPIO\_ADAPTER\_INFORMATION structure contains information that pertains to MPIOs view of a path.
ms.assetid: bcf159a7-75a5-46aa-897a-2c5eb00f51d8
keywords:
- MPIO_ADAPTER_INFORMATION structure Storage Devices
- PMPIO_ADAPTER_INFORMATION structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MPIO_ADAPTER_INFORMATION
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

# MPIO\_ADAPTER\_INFORMATION structure

The MPIO\_ADAPTER\_INFORMATION structure contains information that pertains to MPIO's view of a path.

## Syntax


```C++
typedef struct _MPIO_ADAPTER_INFORMATION {
  ULONGLONG PathId;
  UCHAR     BusNumber;
  UCHAR     DeviceNumber;
  UCHAR     FunctionNumber;
  UCHAR     Pad;
  WCHAR     AdapterName[63 + 1];
} MPIO_ADAPTER_INFORMATION, *PMPIO_ADAPTER_INFORMATION;
```



## Members

<dl> <dt>

**PathId**
</dt> <dd>

An unsigned 64-bitfield that represents an identifier that is assigned to a particular path. This field will match the PathIdentifier field in the instance(s) of the PDO\_INFORMATION class that represent device(s) exposed via this path.

</dd> <dt>

**BusNumber**
</dt> <dd>

An unsigned 8-bitfield that corresponds to the bus number that is assigned by PCI to the host bus adapter through which this path is exposed.

</dd> <dt>

**DeviceNumber**
</dt> <dd>

An unsigned 8-bitfield that corresponds to the device number that is assigned by PCI to the host bus adapter through which this path is exposed.

</dd> <dt>

**FunctionNumber**
</dt> <dd>

An unsigned 8-bitfield that corresponds to the function number that is assigned by PCI to the host bus adapter through which this path is exposed.

</dd> <dt>

**Pad**
</dt> <dd>

Should be zero.

</dd> <dt>

**AdapterName**
</dt> <dd>

A string field that returns the friendly name of the host bus adapter through which this path is exposed.

</dd> </dl>

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mpiowmi.h (include Mpiowmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MPIO_ADAPTER_INFORMATION%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





