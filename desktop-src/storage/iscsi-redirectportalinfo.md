---
title: ISCSI\_RedirectPortalInfo structure
description: This ISCSI\_RedirectPortalInfo structure contains information about a collection of iSCSI portals that can be used during portal hopping or portal redirect operations.
ms.assetid: '90d9c5e9-4bdf-4c7a-b5ac-54e1f94818bf'
keywords: ["ISCSI_RedirectPortalInfo structure Storage Devices", "PISCSI_RedirectPortalInfo structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- ISCSI_RedirectPortalInfo
api_location:
- iscsimgt.h
api_type:
- HeaderDef
---

# ISCSI\_RedirectPortalInfo structure

This ISCSI\_RedirectPortalInfo structure contains information about a collection of iSCSI portals that can be used during portal hopping or portal redirect operations. If a target portal is not available for login, the initiator can "hop" through the list of target portals that it discovered and that can be used for login operations. That is, the initiator will continue to try the list of portals that are available until it finds one that can be used for login, so it can then log in to the available target portal.

## Syntax


```C++
typedef struct _ISCSI_RedirectPortalInfo {
  ULONGLONG        UniqueConnectionId;
  ISCSI_IP_Address OriginalIPAddr;
  ULONG            OriginalPort;
  ISCSI_IP_Address RedirectedIPAddr;
  ULONG            RedirectedPort;
  UCHAR            Redirected;
  UCHAR            TemporaryRedirect;
} ISCSI_RedirectPortalInfo, *PISCSI_RedirectPortalInfo;
```



## Members

<dl> <dt>

**UniqueConnectionId**
</dt> <dd>

The connection identifier (ID) that the operating system and application software use to uniquely identify the connection. The [LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599) and [AddConnectionToSession](https://msdn.microsoft.com/library/windows/hardware/ff550121) methods both return this value in the UniqueConnectionId parameter. This value is not to be confused with the connection ID (CID).

</dd> <dt>

**OriginalIPAddr**
</dt> <dd>

This is the original IP address given during login from which redirection is to be set, and the IP address is provided via the ISCSI\_IP\_Address structure.

</dd> <dt>

**OriginalPort**
</dt> <dd>

This is the original portals socket number given during login.

</dd> <dt>

**RedirectedIPAddr**
</dt> <dd>

This is the IP address to which traffic needs to be redirected. The IP address is provided via the ISCSI\_IP\_Address structure.

</dd> <dt>

**RedirectedPort**
</dt> <dd>

This is the socket number for the redirected target portal.

</dd> <dt>

**Redirected**
</dt> <dd>

This indicates whether the login is redirected. If this value is **TRUE**, RedirectedIPAddr and RedirectedPort are valid.

</dd> <dt>

**TemporaryRedirect**
</dt> <dd>

This value is **true** if redirection is temporary.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsimgt.h (include Iscsimgt.h)</dt> </dl> |



## See also

<dl> <dt>

[AddConnectionToSession](https://msdn.microsoft.com/library/windows/hardware/ff550121)
</dt> <dt>

[LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ISCSI_RedirectPortalInfo%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






