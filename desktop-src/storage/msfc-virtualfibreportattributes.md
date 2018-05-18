---
title: MSFC\_VirtualFibrePortAttributes structure
description: The MSFC\_VirtualFibrePortAttributes structure contains attribute information for a virtual port.
ms.assetid: 'FD8D6063-E6DD-4EA6-9675-774C58C08B40'
keywords: ["MSFC_VirtualFibrePortAttributes structure Storage Devices", "PMSFC_VirtualFibrePortAttributes structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- MSFC_VirtualFibrePortAttributes
api_location:
- npivwmi.h
api_type:
- HeaderDef
---

# MSFC\_VirtualFibrePortAttributes structure

The MSFC\_VirtualFibrePortAttributes structure contains attribute information for a virtual port.

## Syntax


```C++
typedef struct _MSFC_VirtualFibrePortAttributes {
  ULONG  Status;
  ULONG  FCId;
  USHORT VirtualName[64];
  UCHAR  Tag[16];
  UCHAR  WWPN[8];
  UCHAR  WWNN[8];
  UCHAR  FabricWWN[8];
} MSFC_VirtualFibrePortAttributes, *PMSFC_VirtualFibrePortAttributes;
```



## Members

<dl> <dt>

**Status**
</dt> <dd>

The virtual port status.

</dd> <dt>

**FCId**
</dt> <dd>

The fabric ID of the virtual port.

</dd> <dt>

**VirtualName**
</dt> <dd>

The symbolic name of the virtual port.

</dd> <dt>

**Tag**
</dt> <dd>

A value for identifying the virtual port. This member provides a 128-bit width to accommodate a unique identifier.

</dd> <dt>

**WWPN**
</dt> <dd>

The world wide port name of the physical port.

</dd> <dt>

**WWNN**
</dt> <dd>

The world wide node name of the physical port.

</dd> <dt>

**FabricWWN**
</dt> <dd>

The world wide port name of the fabric.

</dd> </dl>

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Npivwmi.h (include Npivwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[MSFC\_VirtualFibrePortAttributes WMI Class](https://msdn.microsoft.com/library/windows/hardware/hh127629)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSFC_VirtualFibrePortAttributes%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






