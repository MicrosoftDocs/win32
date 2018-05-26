---
title: LoginToTarget\_IN structure
description: The LoginToTarget\_IN structure holds the input data for the LoginToTarget method, which is used to login to a target.
ms.assetid: f25b503b-0182-452d-8561-b3c82f595f81
keywords:
- LoginToTarget_IN structure Storage Devices
- PLoginToTarget_IN structure pointer Storage Devices
topic_type:
- apiref
api_name:
- LoginToTarget_IN
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

# LoginToTarget\_IN structure

The LoginToTarget\_IN structure holds the input data for the [LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599) method, which is used to login to a target.

## Syntax


```C++
typedef struct _LoginToTarget_IN {
  ULONG               PortNumber;
  ISCSI_LoginOptions  LoginOptions;
  ULONG               SessionType;
  ULONGLONG           SecurityFlags;
  ISCSI_TargetPortal  TargetPortal;
  ULONG               UsernameSize;
  ULONG               PasswordSize;
  ULONG               KeySize;
  USHORT              UniqueIdForISID;
  BOOLEAN             PersistentLogin;
  WCHAR               InitiatorNode[223 + 1];
  WCHAR               InitiatorAlias[255 + 1];
  WCHAR               TargetName[223 + 1];
  ISCSI_TargetMapping Mappings;
  UCHAR               Key[1];
} LoginToTarget_IN, *PLoginToTarget_IN;
```



## Members

<dl> <dt>

**PortNumber**
</dt> <dd>

The number of the port (initiator portal) that the HBA initiator uses to establish the logon session. This value must match the **Index** member of the [**ISCSI\_PortalInfo**](iscsi-portalinfo.md) structure.

</dd> <dt>

**LoginOptions**
</dt> <dd>

A [**ISCSI\_LoginOptions**](iscsi-loginoptions.md) structure that specifies the characteristics of the logon session.

</dd> <dt>

**SessionType**
</dt> <dd>

A [**LOGINSESSIONTYPE**](loginsessiontype.md) enumeration value that specifies the type of logon session.

</dd> <dt>

**SecurityFlags**
</dt> <dd>

A bitwise OR of security flags that indicate the security requirements that are associated with the authentication key that is used to establish the logon session. For a list of the flags that you can combine to define this member's value, see [SECURITY\_FLAG\_QUALIFIERS](https://msdn.microsoft.com/library/windows/hardware/ff565399).

</dd> <dt>

**TargetPortal**
</dt> <dd>

A [**ISCSI\_TargetPortal**](iscsi-targetportal.md) structure that indicates which target portal to use to make the connection.

</dd> <dt>

**UsernameSize**
</dt> <dd>

The size, in bytes, of the string in **Username**.

</dd> <dt>

**PasswordSize**
</dt> <dd>

The size, in bytes, of the string in **Password**.

</dd> <dt>

**KeySize**
</dt> <dd>

The size, in bytes, of the string in **Key**.

</dd> <dt>

**UniqueIdForISID**
</dt> <dd>

A number that the miniport driver that manages the HBA can use to construct a unique session identifier (ISID).

</dd> <dt>

**PersistentLogin**
</dt> <dd>

A Boolean value that indicates if the logon should be persistent. If this member is **TRUE**, the logon should be persistent. The HBA's miniport driver should store the characteristics of this logon in non-volatile memory and log on to the target automatically every time the operating system loads the miniport driver. If this member is **FALSE**, the logon is not persistent.

</dd> <dt>

**InitiatorNode**
</dt> <dd>

The iSCSI name of the initiator node to use for the connection. If this member is empty, the HBA's miniport driver can choose any initiator node name during authentication. The initiator node name is usually an iSCSI qualified name (IQN).

</dd> <dt>

**InitiatorAlias**
</dt> <dd>

The iSCSI alias of the initiator node.

</dd> <dt>

**TargetName**
</dt> <dd>

The iSCSI target name with which to establish the logon session.

</dd> <dt>

**Mappings**
</dt> <dd>

A [**ISCSI\_TargetMapping**](iscsi-targetmapping.md) structure that maps a collection of logical unit numbers (LUNs) that are locally defined to a group of 64-bit iSCSI LUNs. If the initiator service does not specify mappings, the HBA's miniport driver can use any mappings for the LUNs. The miniport driver should report unmapped LUNs to the port driver to be enumerated.

</dd> <dt>

**Key**
</dt> <dd>

A variable-length array of UCHAR values that defines the preshared key that is associated with the target IP address.

</dd> </dl>

## Remarks

You must implement this method.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsiop.h (include Iscsiop.h)</dt> </dl> |



## See also

<dl> <dt>

[**ISCSI\_LoginOptions**](iscsi-loginoptions.md)
</dt> <dt>

[**ISCSI\_PortalInfo**](iscsi-portalinfo.md)
</dt> <dt>

[**ISCSI\_TargetMapping**](iscsi-targetmapping.md)
</dt> <dt>

[**ISCSI\_TargetPortal**](iscsi-targetportal.md)
</dt> <dt>

[**LOGINSESSIONTYPE**](loginsessiontype.md)
</dt> <dt>

[LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599)
</dt> <dt>

[**LoginToTarget\_OUT**](logintotarget-out.md)
</dt> <dt>

[MSiSCSI\_Operations WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff563091)
</dt> <dt>

[SECURITY\_FLAG\_QUALIFIERS](https://msdn.microsoft.com/library/windows/hardware/ff565399)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20LoginToTarget_IN%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






