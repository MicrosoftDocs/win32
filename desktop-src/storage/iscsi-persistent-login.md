---
title: ISCSI\_Persistent\_Login structure
description: The ISCSI\_Persistent\_Login structure defines a persistent logon that the operating system initiates automatically when the computer boots up.
ms.assetid: c43ee3dd-552a-41ab-9b4f-01611e44f453
keywords:
- ISCSI_Persistent_Login structure Storage Devices
- PISCSI_Persistent_Login structure pointer Storage Devices
topic_type:
- apiref
api_name:
- ISCSI_Persistent_Login
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

# ISCSI\_Persistent\_Login structure

The ISCSI\_Persistent\_Login structure defines a persistent logon that the operating system initiates automatically when the computer boots up.

## Syntax


```C++
typedef struct _ISCSI_Persistent_Login {
  WCHAR               TargetName[223 + 1];
  ULONGLONG           SecurityFlags;
  ULONG               InitiatorPortNumber;
  ULONG               UsernameSize;
  BOOLEAN             IsInformationalSession;
  USHORT              UniqueIdForISID;
  ISCSI_TargetPortal  TargetPortal;
  ISCSI_LoginOptions  LoginOptions;
  ISCSI_TargetMapping TargetMapping;
  UCHAR               Username[1];
} ISCSI_Persistent_Login, *PISCSI_Persistent_Login;
```



## Members

<dl> <dt>

**TargetName**
</dt> <dd>

A wide character string that indicates the name of the target with which the iSCSI initiator service establishes a persistent logon when it restarts.

</dd> <dt>

**SecurityFlags**
</dt> <dd>

A bitwise OR of security flags that indicate the security requirements of the target that is specified in the persistent logon. For a list of possible values for this member, see [SECURITY\_FLAG\_QUALIFIERS](https://msdn.microsoft.com/library/windows/hardware/ff565399).

</dd> <dt>

**InitiatorPortNumber**
</dt> <dd>

The port number on the initiator side to perform the logon operation through.

</dd> <dt>

**UsernameSize**
</dt> <dd>

The size, in bytes, of the string in **Username**.

</dd> <dt>

**IsInformationalSession**
</dt> <dd>

A Boolean value that indicates whether the persistent logon is configured to establish a purely informational session. If this member is **TRUE**, the persistent logon is configured to establish a purely informational session.

</dd> <dt>

**UniqueIdForISID**
</dt> <dd>

Portal to use for initial connection

</dd> <dt>

**TargetPortal**
</dt> <dd>

An [**ISCSI\_TargetPortal**](iscsi-targetportal.md) structure that specifies which target portal to use for the initial logon connection.

</dd> <dt>

**LoginOptions**
</dt> <dd>

An [**ISCSI\_LoginOptions**](iscsi-loginoptions.md) structure that specifies the characteristics of the persistent logon session.

</dd> <dt>

**TargetMapping**
</dt> <dd>

An [**ISCSI\_TargetMapping**](iscsi-targetmapping.md) structure that defines the target mappings.

</dd> <dt>

**Username**
</dt> <dd>

A variable-length array of characters that specifies the challenge handshake authentication protocol user name (CHAP\_N) to use when the initiator is authenticating the target. The number of elements in the array is specified by the **UsernameSize** field.

</dd> </dl>

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsiop.h (include Iscsiop.h)</dt> </dl> |



## See also

<dl> <dt>

[ISCSI\_Persistent\_Login WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff561556)
</dt> <dt>

[**ISCSI\_LoginOptions**](iscsi-loginoptions.md)
</dt> <dt>

[**ISCSI\_TargetMapping**](iscsi-targetmapping.md)
</dt> <dt>

[**ISCSI\_TargetPortal**](iscsi-targetportal.md)
</dt> <dt>

[SECURITY\_FLAG\_QUALIFIERS](https://msdn.microsoft.com/library/windows/hardware/ff565399)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ISCSI_Persistent_Login%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






