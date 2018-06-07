---
title: MSiSCSI\_BootConfiguration structure
description: The MSiSCSI\_BootConfiguration structure describes how the boot device is configured.
ms.assetid: 3a4b55b1-977d-43fb-9968-7a734e04b21b
keywords:
- MSiSCSI_BootConfiguration structure Storage Devices
- PMSiSCSI_BootConfiguration structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MSiSCSI_BootConfiguration
api_location:
- iscsicfg.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# MSiSCSI\_BootConfiguration structure

The MSiSCSI\_BootConfiguration structure describes how the boot device is configured.

## Syntax


```C++
typedef struct _MSiSCSI_BootConfiguration {
  ULONGLONG          LUN;
  ULONGLONG          SecurityFlags;
  ULONG              UsernameSize;
  ULONG              PasswordSize;
  BOOLEAN            DiscoverBootDevice;
  WCHAR              InitiatorNode[223 + 1];
  WCHAR              TargetName[223 + 1];
  ISCSI_TargetPortal TargetPortal;
  ISCSI_LoginOptions LoginOptions;
  UCHAR              Username[1];
} MSiSCSI_BootConfiguration, *PMSiSCSI_BootConfiguration;
```



## Members

<dl> <dt>

**LUN**
</dt> <dd>

The logical unit number (LUN) that identifies the logical unit on the target that functions as a boot device.

</dd> <dt>

**SecurityFlags**
</dt> <dd>

A bitwise OR of security flags that indicate the security requirements of the boot device. For a list of possible flags for this member, see [SECURITY\_FLAG\_QUALIFIERS](https://msdn.microsoft.com/library/windows/hardware/ff565399).

</dd> <dt>

**UsernameSize**
</dt> <dd>

The size, in bytes, of the string in **Username**.

</dd> <dt>

**PasswordSize**
</dt> <dd>

The size, in bytes, of the string in **Password**.

</dd> <dt>

**DiscoverBootDevice**
</dt> <dd>

A Boolean value that indicates whether the system should dynamically discover the boot device. If this member is **TRUE**, the system should dynamically discover the boot device.

</dd> <dt>

**InitiatorNode**
</dt> <dd>

The iSCSI name of the initiator node to use for connecting to the boot device. If this member is **NULL**, the HBA can choose any initiator node. The iSCSI name for the initiator uniquely identifies the initiator anywhere in the world. For more information about how to specify this name, see the *iSCSI* specification that is published by the Internet Engineering Task Force (IETF) of the IP storage working group.

</dd> <dt>

**TargetName**
</dt> <dd>

The iSCSI name for the target that contains the boot device.

</dd> <dt>

**TargetPortal**
</dt> <dd>

A [**ISCSI\_TargetPortal**](iscsi-targetportal.md) structure that specifies the portal to use for the connection.

</dd> <dt>

**LoginOptions**
</dt> <dd>

A [**ISCSI\_LoginOptions**](iscsi-loginoptions.md) structure that specifies the characteristics of the logon session to establish with the boot device.

</dd> <dt>

**Username**
</dt> <dd>

A variable length array of characters that specifies the user name to use with the challenge handshake authentication protocol (CHAP). The user name is also known as the *CHAP name* (CHAP\_N). The initiator uses the CHAP name to authenticate the target.

</dd> </dl>

## Remarks

The WMI tool suite automatically generates a declaration of the MSiSCSI\_BootConfiguration structure when it compiles the [MSiSCSI\_BootConfiguration WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562979) in *Config.mof*.It is optional that you implement this class.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsicfg.h (include Iscsicfg.h)</dt> </dl> |



## See also

<dl> <dt>

[**ISCSI\_LoginOptions**](iscsi-loginoptions.md)
</dt> <dt>

[**ISCSI\_TargetPortal**](iscsi-targetportal.md)
</dt> <dt>

[MSiSCSI\_BootConfiguration WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562979)
</dt> <dt>

[SECURITY\_FLAG\_QUALIFIERS](https://msdn.microsoft.com/library/windows/hardware/ff565399)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSiSCSI_BootConfiguration%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






