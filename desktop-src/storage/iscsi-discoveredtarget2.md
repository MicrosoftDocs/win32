---
title: ISCSI\_DiscoveredTarget2 structure
description: The ISCSI\_DiscoveredTarget2 structure contains information that is related to a discovered target device.
ms.assetid: 77fb2942-5836-44cb-9a5e-e45f6a022264
keywords:
- ISCSI_DiscoveredTarget2 structure Storage Devices
- PISCSI_DiscoveredTarget2 structure pointer Storage Devices
topic_type:
- apiref
api_name:
- ISCSI_DiscoveredTarget2
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

# ISCSI\_DiscoveredTarget2 structure

The ISCSI\_DiscoveredTarget2 structure contains information that is related to a discovered target device.

## Syntax


```C++
typedef struct _ISCSI_DiscoveredTarget2 {
  ULONG                              TargetPortalGroupCount;
  WCHAR                              TargetName[223 + 1];
  WCHAR                              TargetAlias[255 + 1];
  ISCSI_DiscoveredTargetPortalGroup2 TargetDiscoveredPortalGroups[1];
} ISCSI_DiscoveredTarget2, *PISCSI_DiscoveredTarget2;
```



## Members

<dl> <dt>

**TargetPortalGroupCount**
</dt> <dd>

The number of portal groups that are associated with the target.

</dd> <dt>

**TargetName**
</dt> <dd>

A name for the target that uniquely identifies the target anywhere in the world. For more information about how to specify this name, see the *iSCSI* specification that is published by the Internet Engineering Task Force (IETF) of the IP storage working group.

</dd> <dt>

**TargetAlias**
</dt> <dd>

The human-readable name or description that is assigned to the target device by its host operating system. You can use this name in user interfaces, but it is not unique, so you should not use it in authentication decisions.

</dd> <dt>

**TargetDiscoveredPortalGroups**
</dt> <dd>

A variable-length array of [**ISCSI\_DiscoveredTargetPortalGroup2**](iscsi-discoveredtargetportalgroup2.md) structures that contains information about the portal groups that the initiator can use to connect to the target.

</dd> </dl>

## Remarks

The WMI tool suite automatically generates a declaration of the ISCSI\_DiscoveredTarget2 structure when it compiles the [ISCSI\_DiscoveredTarget2 WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff561505) in *Discover.mof*.

The only difference between the ISCSI\_DiscoveredTarget2 structure and the [**ISCSI\_DiscoveredTarget**](iscsi-discoveredtarget.md) structure is that the **TargetDiscoveredPortalGroups** member of ISCSI\_DiscoveredTarget2 is a [**ISCSI\_DiscoveredTargetPortalGroup2**](iscsi-discoveredtargetportalgroup2.md) structure instead of a [**ISCSI\_DiscoveredTargetPortalGroup**](iscsi-discoveredtargetportalgroup.md) structure.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsifnd.h (include Iscsifnd.h)</dt> </dl> |



## See also

<dl> <dt>

[**ISCSI\_DiscoveredTarget**](iscsi-discoveredtarget.md)
</dt> <dt>

[ISCSI\_DiscoveredTarget WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff561527)
</dt> <dt>

[ISCSI\_DiscoveredTarget2 WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff561505)
</dt> <dt>

[**ISCSI\_DiscoveredTargetPortalGroup**](iscsi-discoveredtargetportalgroup.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ISCSI_DiscoveredTarget2%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






