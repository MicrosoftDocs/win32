---
title: MSiSCSI\_PortalInfoClass structure
description: The MSiSCSI\_PortalInfoClass structure contains information about a collection of iSCSI portals.
ms.assetid: 400ff6fc-6eb7-4b3f-afec-7d0b69039ed1
keywords:
- MSiSCSI_PortalInfoClass structure Storage Devices
- PMSiSCSI_PortalInfoClass structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MSiSCSI_PortalInfoClass
api_location:
- iscsimgt.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# MSiSCSI\_PortalInfoClass structure

The MSiSCSI\_PortalInfoClass structure contains information about a collection of iSCSI portals.

## Syntax


```C++
typedef struct _MSiSCSI_PortalInfoClass {
  ULONG            PortalInfoCount;
  ISCSI_PortalInfo PortalInformation[1];
} MSiSCSI_PortalInfoClass, *PMSiSCSI_PortalInfoClass;
```



## Members

<dl> <dt>

**PortalInfoCount**
</dt> <dd>

The number of portals that the initiator discovered and for which portal information is available.

</dd> <dt>

**PortalInformation**
</dt> <dd>

A variable length array of [**ISCSI\_PortalInfo**](iscsi-portalinfo.md) structures. The number of elements in the array is specified by the **PortalInfoCount** field.

</dd> </dl>

## Remarks

We recommend that you implement this class.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsimgt.h (include Iscsimgt.h)</dt> </dl> |



## See also

<dl> <dt>

[**ISCSI\_PortalInfo**](iscsi-portalinfo.md)
</dt> <dt>

[MSiSCSI\_PortalInfoClass WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff563100)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSiSCSI_PortalInfoClass%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






