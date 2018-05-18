---
title: ISCSI\_PortalInfo structure
description: The ISCSI\_PortalInfo structure contains information about an iSCSI portal.
ms.assetid: '0ecfed3e-477a-4014-8491-1a8997ac5b90'
keywords: ["ISCSI_PortalInfo structure Storage Devices", "PISCSI_PortalInfo structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- ISCSI_PortalInfo
api_location:
- iscsimgt.h
api_type:
- HeaderDef
---

# ISCSI\_PortalInfo structure

The ISCSI\_PortalInfo structure contains information about an iSCSI portal.

## Syntax


```C++
typedef struct _ISCSI_PortalInfo {
  ULONG            Index;
  UCHAR            PortalType;
  UCHAR            Protocol;
  UCHAR            Reserved1;
  UCHAR            Reserved2;
  ISCSI_IP_Address IPAddr;
  ULONG            Port;
  USHORT           PortalTag;
} ISCSI_PortalInfo, *PISCSI_PortalInfo;
```



## Members

<dl> <dt>

**Index**
</dt> <dd>

The unique port number associated with this portal.

</dd> <dt>

**PortalType**
</dt> <dd>

The type of portal. This member can have the following symbolic constant values, which are defined in *Iscsimgt.h*.



| Portal Type                 | Meaning                                                                                                                                             |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| InitiatorPortals<br/> | The portal that the initiator uses to access the network. In an initiator, a portal is identified by its IP address. <br/>                    |
| TargetPortals<br/>    | The portal that the target uses to access the network. In a target, a portal is identified by its IP address and its listening TCP port.<br/> |



 

</dd> <dt>

**Protocol**
</dt> <dd>

The portal's transport protocol. Currently, this member must hold the value that is associated with the symbolic constant, TCP. TCP is defined in *Iscsimgt.h*.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved for Microsoft use only.

</dd> <dt>

**Reserved2**
</dt> <dd>

Reserved for Microsoft use only.

</dd> <dt>

**IPAddr**
</dt> <dd>

A [**ISCSI\_IP\_Address**](iscsi-ip-address.md) structure that indicates the portal's network IP address.

</dd> <dt>

**Port**
</dt> <dd>

The socket number for the portal.

</dd> <dt>

**PortalTag**
</dt> <dd>

The portal group tag to which the portal belongs.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsimgt.h (include Iscsimgt.h)</dt> </dl> |



## See also

<dl> <dt>

[**ISCSI\_IP\_Address**](iscsi-ip-address.md)
</dt> <dt>

[ISCSI\_PortalInfo WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff561559)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ISCSI_PortalInfo%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






