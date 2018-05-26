---
Description: This MSIscsiInitiator\_PersistentLoginClass structure defines a persistent logon that the operating system initiates automatically when the computer boots up.
ms.assetid: 90009105-7efc-47bd-9bdb-f11a1a405e1c
title: MSIscsiInitiator\_PersistentLoginClass class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSIscsiInitiator\_PersistentLoginClass class

This **MSIscsiInitiator\_PersistentLoginClass** structure defines a persistent logon that the operating system initiates automatically when the computer boots up.

## Syntax

``` syntax
class MSIscsiInitiator_PersistentLoginClass
{
  string                              TargetName;
  boolean                             IsInformationalSession;
  string                              InitiatorInstance;
  uint32                              InitiatorPortNumber;
  MSIscsiInitiator_Portal             TargetPortal;
  ISCSI_SECURITY_FLAGS                SecurityFlags;
  MSiSCSIInitiator_TargetMappings     Mappings;
  MSIscsiInitiator_TargetLoginOptions LoginOptions;
};
```

## Members

The **MSIscsiInitiator\_PersistentLoginClass** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSIscsiInitiator\_PersistentLoginClass** class has these properties.

<dl> <dt>

**InitiatorInstance**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string representing the name of the initiator used to login to the target.

</dd> <dt>

**InitiatorPortNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The port number of the Host-Bus Adapter (HBA) through which the session login is established.

</dd> <dt>

**IsInformationalSession**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A Boolean value that indicates whether the persistent logon is configured to establish a purely informational session. If this member is TRUE, the persistent logon is configured to establish a purely informational session.

A management application can still access targets not enumerated by the system via the SendScsiInquiry, SendScsiReportLuns, and SendScsiReadCapcity functions.

</dd> <dt>

**LoginOptions**
</dt> <dd> <dl> <dt>

Data type: **MSIscsiInitiator\_TargetLoginOptions**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of [**MSIscsiInitiator\_TargetLoginOptions**](msiscsiinitiator-targetloginoptions.md) structures containing information about target login options.

</dd> <dt>

**Mappings**
</dt> <dd> <dl> <dt>

Data type: **MSiSCSIInitiator\_TargetMappings**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of [**MSIscsiInitiator\_TargetMappings**](msiscsiinitiator-targetmappings.md) structures containing information about LUN mapping.

</dd> <dt>

**SecurityFlags**
</dt> <dd> <dl> <dt>

Data type: **ISCSI\_SECURITY\_FLAGS**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A bitmap that defines the security characteristics of a login connection.



| Value                                                                                                                                                                                                                                                          | Meaning                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="ISCSI_SECURITY_FLAG_TUNNEL_MODE_PREFERRED"></span><span id="iscsi_security_flag_tunnel_mode_preferred"></span><dl> <dt>**ISCSI\_SECURITY\_FLAG\_TUNNEL\_MODE\_PREFERRED**</dt> </dl>          | The Host Bus Adapter (HBA) initiator should establish the TCP/IP connection to the target portal using IPsec tunnel mode.<br/>                                             |
| <span id="ISCSI_SECURITY_FLAG_TRANSPORT_MODE_PREFERRED"></span><span id="iscsi_security_flag_transport_mode_preferred"></span><dl> <dt>**ISCSI\_SECURITY\_FLAG\_TRANSPORT\_MODE\_PREFERRED**</dt> </dl> | The HBA initiator should establish the TCP/IP connection to the target portal using IPsec transport mode.<br/>                                                             |
| <span id="ISCSI_SECURITY_FLAG_PFS_ENABLED"></span><span id="iscsi_security_flag_pfs_enabled"></span><dl> <dt>**ISCSI\_SECURITY\_FLAG\_PFS\_ENABLED**</dt> </dl>                                         | The HBA initiator should establish the TCP/IP connection to the target portal with Perfect Forward Secrecy (PFS) mode enabled if IPsec is required.<br/>                   |
| <span id="ISCSI_SECURITY_FLAG_AGGRESSIVE_MODE_ENABLED"></span><span id="iscsi_security_flag_aggressive_mode_enabled"></span><dl> <dt>**ISCSI\_SECURITY\_FLAG\_AGGRESSIVE\_MODE\_ENABLED**</dt> </dl>    | The HBA initiator should establish the TCP/IP connection to the target portal with aggressive mode enabled.<br/>                                                           |
| <span id="ISCSI_SECURITY_FLAG_MAIN_MODE_ENABLED"></span><span id="iscsi_security_flag_main_mode_enabled"></span><dl> <dt>**ISCSI\_SECURITY\_FLAG\_MAIN\_MODE\_ENABLED**</dt> </dl>                      | The HBA initiator should establish the TCP/IP connection to the target portal with main mode enabled.<br/>                                                                 |
| <span id="ISCSI_SECURITY_FLAG_IKE_IPSEC_ENABLED"></span><span id="iscsi_security_flag_ike_ipsec_enabled"></span><dl> <dt>**ISCSI\_SECURITY\_FLAG\_IKE\_IPSEC\_ENABLED**</dt> </dl>                      | The HBA initiator should establish the TCP/IP connection to the target portal using IKE/IPsec protocol. If not set then IPsec is not required to login to the target.<br/> |
| <span id="ISCSI_SECURITY_FLAG_VALID"></span><span id="iscsi_security_flag_valid"></span><dl> <dt>**ISCSI\_SECURITY\_FLAG\_VALID**</dt> </dl>                                                            | The other mask values are valid; otherwise, security flags are not specified.<br/>                                                                                         |



 

</dd> <dt>

**TargetName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

A wide character string that indicates the name of the target with which the iSCSI initiator service establishes a persistent logon when it restarts.

</dd> <dt>

**TargetPortal**
</dt> <dd> <dl> <dt>

Data type: **MSIscsiInitiator\_Portal**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of [**MSIscsiInitiator\_Portal**](msiscsiinitiator-portal.md) structures containing information about iSCSI initiator portals.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Namespace<br/>                | Root\\WMI<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>Iscsidsc.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSIscsiInitiator\_Portal**](msiscsiinitiator-portal.md)
</dt> <dt>

[**MSIscsiInitiator\_TargetMappings**](msiscsiinitiator-targetmappings.md)
</dt> <dt>

[**MSIscsiInitiator\_TargetLoginOptions**](msiscsiinitiator-targetloginoptions.md)
</dt> </dl>

 

 




