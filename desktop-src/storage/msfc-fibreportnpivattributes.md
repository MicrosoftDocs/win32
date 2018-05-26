---
title: MSFC\_FibrePortNPIVAttributes structure
description: The MSFC\_FibrePortNPIVAttributes structure contains attribute information for the virtual ports on an adapter.
ms.assetid: 1641C3A0-E6D9-4E30-9E3C-3C09A14F591F
keywords:
- MSFC_FibrePortNPIVAttributes structure Storage Devices
- PMSFC_FibrePortNPIVAttributes structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MSFC_FibrePortNPIVAttributes
api_location:
- npivwmi.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSFC\_FibrePortNPIVAttributes structure

The MSFC\_FibrePortNPIVAttributes structure contains attribute information for the virtual ports on an adapter.

## Syntax


```C++
typedef struct _MSFC_FibrePortNPIVAttributes {
  UCHAR                           WWPN[8];
  UCHAR                           WWNN[8];
  ULONG                           NumberVirtualPorts;
  MSFC_VirtualFibrePortAttributes VirtualPorts[1];
} MSFC_FibrePortNPIVAttributes, *PMSFC_FibrePortNPIVAttributes;
```



## Members

<dl> <dt>

**WWPN**
</dt> <dd>

The world wide port name of the physical port.

</dd> <dt>

**WWNN**
</dt> <dd>

The world wide node name of the physical port.

</dd> <dt>

**NumberVirtualPorts**
</dt> <dd>

The number of virtual ports on the adapter.

</dd> <dt>

**VirtualPorts**
</dt> <dd>

An array of virtual ports. The array length is specified in the **NumberVirtualPorts** member.

</dd> </dl>

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Npivwmi.h (include Npivwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[MSFC\_FibrePortNPIVAttributes WMI Class](https://msdn.microsoft.com/library/windows/hardware/hh127624)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSFC_FibrePortNPIVAttributes%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






