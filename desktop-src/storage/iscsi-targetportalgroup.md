---
title: ISCSI\_TargetPortalGroup structure
description: The ISCSI\_TargetPortalGroup structure provides a definition of a target portal group.
ms.assetid: 28f48224-90b8-45f5-b69d-6bb6a34f64e0
keywords:
- ISCSI_TargetPortalGroup structure Storage Devices
- PISCSI_TargetPortalGroup structure pointer Storage Devices
topic_type:
- apiref
api_name:
- ISCSI_TargetPortalGroup
api_location:
- iscsidef.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# ISCSI\_TargetPortalGroup structure

The ISCSI\_TargetPortalGroup structure provides a definition of a target portal group.

## Syntax


```C++
typedef struct _ISCSI_TargetPortalGroup {
  ULONG              PortalCount;
  ISCSI_TargetPortal Portals[1];
} ISCSI_TargetPortalGroup, *PISCSI_TargetPortalGroup;
```



## Members

<dl> <dt>

**PortalCount**
</dt> <dd>

The number of portals in the portal group.

</dd> <dt>

**Portals**
</dt> <dd>

A variable-length array of [**ISCSI\_TargetPortal**](iscsi-targetportal.md) structures, which describe portals in the target portal group. The number of elements in the array is specified by the PortalCount field.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsidef.h (include Iscsidef.h)</dt> </dl> |



## See also

<dl> <dt>

[**ISCSI\_TargetPortal**](iscsi-targetportal.md)
</dt> <dt>

[ISCSI\_TargetPortalGroup WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff561576)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ISCSI_TargetPortalGroup%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






