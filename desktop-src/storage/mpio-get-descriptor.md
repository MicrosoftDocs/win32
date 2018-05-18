---
title: MPIO\_GET\_DESCRIPTOR structure
description: The MPIO\_GET\_DESCRIPTOR structure is used to query for LUN instances that correspond to various paths.
ms.assetid: 'cabd2a6d-20d0-4499-8494-7ad746f2d915'
keywords: ["MPIO_GET_DESCRIPTOR structure Storage Devices", "PMPIO_GET_DESCRIPTOR structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- MPIO_GET_DESCRIPTOR
api_location:
- mpiodisk.h
api_type:
- HeaderDef
---

# MPIO\_GET\_DESCRIPTOR structure

The MPIO\_GET\_DESCRIPTOR structure is used to query for LUN instances that correspond to various paths. This structure retrieves device-path pairing information about a multi-path disk. The target of the request must be a pseudo-LUN that is addressed by using its WMI instance name.

## Syntax


```C++
typedef struct _MPIO_GET_DESCRIPTOR {
  ULONG           NumberPdos;
  WCHAR           DeviceName[63 + 1];
  PDO_INFORMATION PdoInformation[1];
} MPIO_GET_DESCRIPTOR, *PMPIO_GET_DESCRIPTOR;
```



## Members

<dl> <dt>

**NumberPdos**
</dt> <dd>

An unsigned 32-bitfield that returns the number of real instances of the pseudo-LUN through its various paths.

</dd> <dt>

**DeviceName**
</dt> <dd>

A string field of maximum-length 63 characters that returns the device name that is created by MPIO for the LUN.

</dd> <dt>

**PdoInformation**
</dt> <dd>

A field that returns an array of PDO\_INFORMATION structures, where the number of elements is given by *NumberPdos*, and each element represents an instance of the LUN that is exposed through a particular path.

</dd> </dl>

## Requirements



|                   |                                                                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mpiodisk.h (include Mpiowmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MPIO_GET_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





