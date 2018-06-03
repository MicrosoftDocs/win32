---
title: RemovePersistentLogin\_IN structure
description: The RemovePersistentLogin\_IN structure holds the input data for the RemovePersistentLogin method, which is used to remove persistent login information.
ms.assetid: 94dc7a87-83a0-419d-914c-008d797fec87
keywords:
- RemovePersistentLogin_IN structure Storage Devices
- PRemovePersistentLogin_IN structure pointer Storage Devices
topic_type:
- apiref
api_name:
- RemovePersistentLogin_IN
api_location:
- iscsiop.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# RemovePersistentLogin\_IN structure

The RemovePersistentLogin\_IN structure holds the input data for the [RemovePersistentLogin](https://msdn.microsoft.com/library/windows/hardware/ff563995) method, which is used to remove persistent login information.

## Syntax


```C++
typedef struct _RemovePersistentLogin_IN {
  ULONG              PortNumber;
  WCHAR              TargetName[223 + 1];
  ISCSI_TargetPortal TargetPortal;
} RemovePersistentLogin_IN, *PRemovePersistentLogin_IN;
```



## Members

<dl> <dt>

**PortNumber**
</dt> <dd>

The port number from which the initiator established the logon session.

</dd> <dt>

**TargetName**
</dt> <dd>

The iSCSI target name to be removed from the initiator's list of persistent logon targets.

</dd> <dt>

**TargetPortal**
</dt> <dd>

A [**ISCSI\_TargetPortal**](iscsi-targetportal.md) structure that specifies the target portal for which the initiator should delete persistent logons. ISCSI\_TargetPortal has an **Address** member of type [**ISCSI\_IP\_Address**](iscsi-ip-address.md). If the **Type** member of ISCSI\_IP\_Address is set to ISCSI\_IP\_ADDRESS\_EMPTY, the [RemovePersistentLogin](https://msdn.microsoft.com/library/windows/hardware/ff563995) method removes the persistent logons to the target for all portals.

</dd> </dl>

## Remarks

You must implement this method.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsiop.h (include Iscsiop.h)</dt> </dl> |



## See also

<dl> <dt>

[**ISCSI\_IP\_Address**](iscsi-ip-address.md)
</dt> <dt>

[**ISCSI\_TargetPortal**](iscsi-targetportal.md)
</dt> <dt>

[RemovePersistentLogin](https://msdn.microsoft.com/library/windows/hardware/ff563995)
</dt> <dt>

[**RemovePersistentLogin\_OUT**](removepersistentlogin-out.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20RemovePersistentLogin_IN%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






