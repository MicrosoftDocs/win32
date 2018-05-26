---
title: ISCSI\_DiscoveredTargetPortalGroup2 structure
description: The ISCSI\_DiscoveredTargetPortalGroup2 structure contains information about a discovered target portal group.
ms.assetid: d852f062-3090-4a7a-bdb8-9dde93257a90
keywords:
- ISCSI_DiscoveredTargetPortalGroup2 structure Storage Devices
- PISCSI_DiscoveredTargetPortalGroup2 structure pointer Storage Devices
topic_type:
- apiref
api_name:
- ISCSI_DiscoveredTargetPortalGroup2
api_location:
- iscsifnd.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ISCSI\_DiscoveredTargetPortalGroup2 structure

The ISCSI\_DiscoveredTargetPortalGroup2 structure contains information about a discovered target portal group.

## Syntax


```C++
typedef struct _ISCSI_DiscoveredTargetPortalGroup2 {
  ULONG                         PortalCount;
  USHORT                        Tag;
  ISCSI_DiscoveredTargetPortal2 Portals[1];
} ISCSI_DiscoveredTargetPortalGroup2, *PISCSI_DiscoveredTargetPortalGroup2;
```



## Members

<dl> <dt>

**PortalCount**
</dt> <dd>

The number of portals in the group.

</dd> <dt>

**Tag**
</dt> <dd>

A tag number that identifies the portal group.

</dd> <dt>

**Portals**
</dt> <dd>

An array of [**ISCSI\_DiscoveredTargetPortal**](iscsi-discoveredtargetportal.md) structures, which describe target portals.

</dd> </dl>

## Remarks

The WMI tool suite automatically generates a declaration of the ISCSI\_DiscoveredTargetPortalGroup2 structure when it compiles the [ISCSI\_DiscoveredTargetPortalGroup2 WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff561520) in *Discover.mof*.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsifnd.h (include Iscsifnd.h)</dt> </dl> |



## See also

<dl> <dt>

[**ISCSI\_DiscoveredTargetPortal**](iscsi-discoveredtargetportal.md)
</dt> <dt>

[**ISCSI\_DiscoveredTargetPortalGroup**](iscsi-discoveredtargetportalgroup.md)
</dt> <dt>

[ISCSI\_DiscoveredTargetPortalGroup WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff561523)
</dt> <dt>

[ISCSI\_DiscoveredTargetPortalGroup2 WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff561520)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ISCSI_DiscoveredTargetPortalGroup2%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






