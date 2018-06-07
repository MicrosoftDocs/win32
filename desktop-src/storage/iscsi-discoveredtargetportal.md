---
title: ISCSI\_DiscoveredTargetPortal structure
description: The ISCSI\_DiscoveredTargetPortal structure provides information that is associated with a discovered target portal.
ms.assetid: af5d0ad6-a035-4291-9390-889fdc3429ee
keywords:
- ISCSI_DiscoveredTargetPortal structure Storage Devices
- PISCSI_DiscoveredTargetPortal structure pointer Storage Devices
topic_type:
- apiref
api_name:
- ISCSI_DiscoveredTargetPortal
api_location:
- iscsifnd.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# ISCSI\_DiscoveredTargetPortal structure

The ISCSI\_DiscoveredTargetPortal structure provides information that is associated with a discovered target portal.

## Syntax


```C++
typedef struct _ISCSI_DiscoveredTargetPortal {
  USHORT           Socket;
  ISCSI_IP_Address Address;
  WCHAR            SymbolicName[256 + 1];
} ISCSI_DiscoveredTargetPortal, *PISCSI_DiscoveredTargetPortal;
```



## Members

<dl> <dt>

**Socket**
</dt> <dd>

The socket number of the portal.

</dd> <dt>

**Address**
</dt> <dd>

The network address of the portal.

</dd> <dt>

**SymbolicName**
</dt> <dd>

A wide character string that indicates the portal's symbolic name.

</dd> </dl>

## Remarks

The WMI tool suite automatically generates a declaration of the ISCSI\_DiscoveredTargetPortal structure when it compiles the [ISCSI\_DiscoveredTargetPortal WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff561524) in *Discover.mof*.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsifnd.h (include Iscsifnd.h)</dt> </dl> |



## See also

<dl> <dt>

[**ISCSI\_DiscoveredTargetPortal2**](iscsi-discoveredtargetportal2.md)
</dt> <dt>

[ISCSI\_DiscoveredTargetPortal WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff561524)
</dt> <dt>

[**ISCSI\_TargetPortal**](iscsi-targetportal.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ISCSI_DiscoveredTargetPortal%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






