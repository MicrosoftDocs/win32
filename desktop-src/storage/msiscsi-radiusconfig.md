---
title: MSiSCSI\_RADIUSConfig structure
description: The MSiSCSI\_RADIUSConfig structure provides information that the initiator requires to use the remote authentication dial-in user service (RADIUS).
ms.assetid: 6f8be86e-2729-4aa9-982d-df323f05cf1c
keywords:
- MSiSCSI_RADIUSConfig structure Storage Devices
- PMSiSCSI_RADIUSConfig structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MSiSCSI_RADIUSConfig
api_location:
- iscsicfg.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSiSCSI\_RADIUSConfig structure

The MSiSCSI\_RADIUSConfig structure provides information that the initiator requires to use the remote authentication dial-in user service (RADIUS).

## Syntax


```C++
typedef struct _MSiSCSI_RADIUSConfig {
  BOOLEAN          UseRADIUSForCHAP;
  ULONG            SharedSecretSizeInBytes;
  ISCSI_IP_Address RADIUSServer;
  ISCSI_IP_Address BackupRADIUSServer;
  ULONG            Reserved;
  UCHAR            SharedSecret[1];
} MSiSCSI_RADIUSConfig, *PMSiSCSI_RADIUSConfig;
```



## Members

<dl> <dt>

**UseRADIUSForCHAP**
</dt> <dd>

A Boolean value that indicates whether the initiator should use RADIUS for authentication during the challenge handshake of the challenge handshake authentication protocol (CHAP). If this member is **TRUE**, the initiator should use RADIUS for authentication during the challenge handshake of CHAP. If this member is **FALSE**, the initiator is not required to use RADIUS.

</dd> <dt>

**SharedSecretSizeInBytes**
</dt> <dd>

The size, in bytes, of shared secret for use with RADIUS servers.

</dd> <dt>

**RADIUSServer**
</dt> <dd>

A [**ISCSI\_IP\_Address**](iscsi-ip-address.md) structure that specifies a fixed address for the RADIUS server. The ISCSI\_IP\_Address structure defines the IP address in a way that is independent of the version of the IP protocol in use.

</dd> <dt>

**BackupRADIUSServer**
</dt> <dd>

A ISCSI\_IP\_Address structure that specifies a fixed addresses for a backup RADIUS server.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved for Microsoft use only. Set this member to zero.

</dd> <dt>

**SharedSecret**
</dt> <dd>

A variable-length array that contains a shared secret. The initiator uses this shared secret to authenticate primary and backup RADIUS servers.

</dd> </dl>

## Remarks

Initiators use RADIUS servers to perform authentication during the challenge handshake of CHAP.

The WMI tool suite automatically generates a declaration of the MSiSCSI\_RADIUSConfig structure when it compiles the [MSiSCSI\_RADIUSConfig WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff563114) in *Config.mof*.

Initiators that support using RADIUS for CHAP authentication must implement the MSiSCSI\_RADIUSConfig class.

Initiators should use RADIUS whenever possible, because RADIUS allows the centralized management of CHAP credentials.

Initiators should register each instance of the MSiSCSI\_RADIUSConfig class using the name of the physical device object (PDO) for the HBAYou must implement this class if the adapter supports authentication via RADIUS.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsicfg.h (include Iscsicfg.h)</dt> </dl> |



## See also

<dl> <dt>

[**ISCSI\_IP\_Address**](iscsi-ip-address.md)
</dt> <dt>

[MSiSCSI\_RADIUSConfig WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff563114)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSiSCSI_RADIUSConfig%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






