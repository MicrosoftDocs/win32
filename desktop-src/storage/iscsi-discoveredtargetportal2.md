---
title: ISCSI\_DiscoveredTargetPortal2 structure
description: The ISCSI\_DiscoveredTargetPortal2 structure provides information that is associated with a discovered target portal.
ms.assetid: 68128d39-2490-4c6b-8780-e5aa542a4e3d
keywords:
- ISCSI_DiscoveredTargetPortal2 structure Storage Devices
- PISCSI_DiscoveredTargetPortal2 structure pointer Storage Devices
topic_type:
- apiref
api_name:
- ISCSI_DiscoveredTargetPortal2
api_location:
- iscsifnd.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ISCSI\_DiscoveredTargetPortal2 structure

The ISCSI\_DiscoveredTargetPortal2 structure provides information that is associated with a discovered target portal.

## Syntax


```C++
typedef struct _ISCSI_DiscoveredTargetPortal2 {
  USHORT           Socket;
  ISCSI_IP_Address Address;
  ULONG            SecurityBitmap;
  ULONG            KeySize;
  UCHAR            Key[1];
} ISCSI_DiscoveredTargetPortal2, *PISCSI_DiscoveredTargetPortal2;
```



## Members

<dl> <dt>

**Socket**
</dt> <dd>

The socket number of the portal.

</dd> <dt>

**Address**
</dt> <dd>

The network address of the portal.

</dd> <dt>

**SecurityBitmap**
</dt> <dd>

A bitmap, which is defined in the *iSNS specification*, that indicates the security characteristics of logon connections that are made to this target portal. The following table describes possible security flag values.



| Security flags                                               | Meaning                                                                                                                                                                                      |
|--------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ISCSI\_SECURITY\_FLAG\_TUNNEL\_MODE\_PREFERRED<br/>    | The initiator HBA should log on targets by using IPsec tunnel mode. If this bit is not set IPsec tunnel mode is not required. <br/>                                                    |
| ISCSI\_SECURITY\_FLAG\_TRANSPORT\_MODE\_PREFERRED<br/> | The initiator HBA should log on targets by using IPsec transport mode. If this bit is not set IPsec transport mode is not required. <br/>                                              |
| ISCSI\_SECURITY\_FLAG\_PFS\_ENABLED<br/>               | The initiator HBA should log on targets with Perfect Forward Secrecy (PFS) mode enabled; otherwise, the initiator HBA should make the session connection with PFS mode disabled. <br/> |
| ISCSI\_SECURITY\_FLAG\_AGGRESSIVE\_MODE\_ENABLED<br/>  | The initiator HBA should log on targets with aggressive mode enabled. If this bit is not set the initiator HBA should make the session connection with aggressive mode disabled.<br/>  |
| ISCSI\_SECURITY\_FLAG\_MAIN\_MODE\_ENABLED<br/>        | The initiator HBA should log on targets with main mode enabled. If this bit is not set the initiator HBA should make the session connection with main mode disabled. <br/>             |
| ISCSI\_SECURITY\_FLAG\_IKE\_IPSEC\_ENABLED<br/>        | The initiator HBA should log on targets with the IKE/IPsec protocol enabled. If this bit is not set the IKE/IPsec protocol is disabled.<br/>                                           |
| ISCSI\_SECURITY\_FLAG\_VALID<br/>                      | The other mask values are valid. If this bit is not set security flags are not specified.. <br/>                                                                                       |



 

For more information about how to configure the default security characteristics that are assigned of the target portal in the registry, see the Remarks section.

</dd> <dt>

**KeySize**
</dt> <dd>

The size, in bytes, of the encryption key in the **Key** member.

</dd> <dt>

**Key**
</dt> <dd>

A variable-length array of characters that contains the encryption key that is associated with the portal address.

</dd> </dl>

## Remarks

The ISCSI\_DiscoveredTargetPortal2 structure is a superset of the information that is provided by the [**ISCSI\_DiscoveredTargetPortal**](iscsi-discoveredtargetportal.md) structure, which only defines the target portal address. In addition to the network address of the target portal, the ISCSI\_DiscoveredTargetPortal2 structure contains information about the target portal's security characteristics.

If the iSNS server does not assign a security bitmap to the target portal, the operating system associates the bitmap in the **DefaultSecurityBitmap** registry value with the portal. The **DefaultSecurityBitmap** registry value is located under the following registry key: **HKLM\\Software\\Microsoft\\Windows NT\\Current Version\\ISCSI\\Discovery Values**.

The default security bitmap is useful in cases where the target portal is configured for IPsec but does not support iSNS.

In general, management applications should use the iSCSI client PSKey command to configure the security bitmap for a target portal. But if there are a large number of portals that have the same security bitmap, the default security bitmap is a good way to automatically assign the same bitmap to all portals.

The WMI tool suite automatically generates a declaration of the ISCSI\_DiscoveredTargetPortal2 structure when it compiles the [ISCSI\_DiscoveredTargetPortal WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff561524) in *Discover.mof*.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsifnd.h (include Iscsifnd.h)</dt> </dl> |



## See also

<dl> <dt>

[**ISCSI\_DiscoveredTargetPortal**](iscsi-discoveredtargetportal.md)
</dt> <dt>

[ISCSI\_DiscoveredTargetPortal WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff561524)
</dt> <dt>

[**ISCSI\_TargetPortal**](iscsi-targetportal.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ISCSI_DiscoveredTargetPortal2%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






