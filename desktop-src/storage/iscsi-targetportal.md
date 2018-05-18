---
title: ISCSI\_TargetPortal structure
description: The ISCSI\_TargetPortal structure provides a definition of a target portal.
ms.assetid: '1adb1dbf-3ec4-4e32-bfe8-cfcf992f67ca'
keywords: ["ISCSI_TargetPortal structure Storage Devices", "PISCSI_TargetPortal structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- ISCSI_TargetPortal
api_location:
- iscsidef.h
api_type:
- HeaderDef
---

# ISCSI\_TargetPortal structure

The ISCSI\_TargetPortal structure provides a definition of a target portal.

## Syntax


```C++
typedef struct _ISCSI_TargetPortal {
  ISCSI_IP_Address Address;
  ULONG            Reserved;
  USHORT           Socket;
} ISCSI_TargetPortal, *PISCSI_TargetPortal;
```



## Members

<dl> <dt>

**Address**
</dt> <dd>

A [**ISCSI\_IP\_Address**](iscsi-ip-address.md) structure that indicates the IP address of the portal. The ISCSI\_IP\_Address structure provides a way to define an IP address that is independent of the version of the IP protocol that the initiator and the target use.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved for Microsoft use only.

</dd> <dt>

**Socket**
</dt> <dd>

Socket number associated with the target.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsidef.h (include Iscsidef.h)</dt> </dl> |



## See also

<dl> <dt>

[**ISCSI\_IP\_Address**](iscsi-ip-address.md)
</dt> <dt>

[ISCSI\_TargetPortal WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff561577)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ISCSI_TargetPortal%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






