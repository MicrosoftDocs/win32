---
title: ISCSI\_DiscoveredTargetPortalGroup structure
description: The ISCSI\_DiscoveredTargetPortalGroup structure contains information about a discovered target portal group.
ms.assetid: 5c90dbc2-f42a-4c04-8c77-0ef3a712416c
keywords:
- ISCSI_DiscoveredTargetPortalGroup structure Storage Devices
- PISCSI_DiscoveredTargetPortalGroup structure pointer Storage Devices
topic_type:
- apiref
api_name:
- ISCSI_DiscoveredTargetPortalGroup
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

# ISCSI\_DiscoveredTargetPortalGroup structure

The ISCSI\_DiscoveredTargetPortalGroup structure contains information about a discovered target portal group.

## Syntax


```C++
typedef struct _ISCSI_DiscoveredTargetPortalGroup {
  ULONG                        PortalCount;
  ISCSI_DiscoveredTargetPortal Portals[1];
} ISCSI_DiscoveredTargetPortalGroup, *PISCSI_DiscoveredTargetPortalGroup;
```



## Members

<dl> <dt>

**PortalCount**
</dt> <dd>

The number of portals in the group.

</dd> <dt>

**Portals**
</dt> <dd>

An array of [**ISCSI\_DiscoveredTargetPortal**](iscsi-discoveredtargetportal.md) structures, which describe target portals.

</dd> </dl>

## Remarks

The WMI tool suite automatically generates a declaration of the ISCSI\_DiscoveredTargetPortalGroup structure when it compiles the [ISCSI\_DiscoveredTargetPortalGroup WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff561523) in *Discover.mof*.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsifnd.h (include Iscsifnd.h)</dt> </dl> |



## See also

<dl> <dt>

[**ISCSI\_DiscoveredTargetPortal**](iscsi-discoveredtargetportal.md)
</dt> <dt>

[**ISCSI\_DiscoveredTargetPortalGroup2**](iscsi-discoveredtargetportalgroup2.md)
</dt> <dt>

[ISCSI\_DiscoveredTargetPortalGroup WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff561523)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ISCSI_DiscoveredTargetPortalGroup%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






