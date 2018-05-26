---
title: MSiSCSI\_PersistentLogins structure
description: The MSiSCSI\_PersistentLogins structure contains the list of persistent target logon sessions.
ms.assetid: c735d9c9-8e87-4a80-af1d-c97d457f78fa
keywords:
- MSiSCSI_PersistentLogins structure Storage Devices
- PMSiSCSI_PersistentLogins structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MSiSCSI_PersistentLogins
api_location:
- iscsiop.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSiSCSI\_PersistentLogins structure

The MSiSCSI\_PersistentLogins structure contains the list of persistent target logon sessions.

## Syntax


```C++
typedef struct _MSiSCSI_PersistentLogins {
  ULONG                  PersistentLoginCount;
  ULONG                  Reserved;
  ISCSI_Persistent_Login PersistentLogins[1];
} MSiSCSI_PersistentLogins, *PMSiSCSI_PersistentLogins;
```



## Members

<dl> <dt>

**PersistentLoginCount**
</dt> <dd>

The number of persistent target logon sessions that the initiator manages.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved for Microsoft use only.

</dd> <dt>

**PersistentLogins**
</dt> <dd>

A variable length array of [**ISCSI\_Persistent\_Login**](iscsi-persistent-login.md) structures, each of which contains information that is associated with a particular persistent logon session that the initiator maintains.

</dd> </dl>

## Remarks

Miniport drivers that manage iSCSI initiators automatically establish persistent logon sessions as soon as they are loaded into the storage driver stack. This guarantees that targets for which the initiator maintains persistent logon sessions will be available to the system as early in the startup process as possible. You must implement this class.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsiop.h (include Iscsiop.h)</dt> </dl> |



## See also

<dl> <dt>

[**ISCSI\_Persistent\_Login**](iscsi-persistent-login.md)
</dt> <dt>

[ISCSI\_Persistent\_Login WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff561556)
</dt> <dt>

[MSiSCSI\_PersistentLogins WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff563096)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSiSCSI_PersistentLogins%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






