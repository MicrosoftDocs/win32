---
Description: This MSIscsiInitiator\_SendTargetPortalClass structure describes the characteristics of a discovered target portal.
ms.assetid: 4a4e97ce-18e3-4b38-ad6c-74381f144901
title: MSIscsiInitiator\_SendTargetPortalClass class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSIscsiInitiator\_SendTargetPortalClass class

This **MSIscsiInitiator\_SendTargetPortalClass** structure describes the characteristics of a discovered target portal.

## Syntax

``` syntax
class MSIscsiInitiator_SendTargetPortalClass
{
  string                              PortalIdentifierString;
  string                              InitiatorName;
  uint32                              InitiatorPortNumber;
  string                              PortalSymbolicName;
  string                              PortalAddress;
  uint16                              PortalPort;
  MSIscsiInitiator_TargetLoginOptions LoginOptions;
  ISCSI_SECURITY_FLAGS                SecurityFlags;
};
```

## Members

The **MSIscsiInitiator\_SendTargetPortalClass** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSIscsiInitiator\_SendTargetPortalClass** class has these methods.



| Method                                                            | Description                                                                                 |
|:------------------------------------------------------------------|:--------------------------------------------------------------------------------------------|
| [**Refresh**](refresh-msiscsiinitiator-sendtargetportalclass.md) | Refreshes the list of discovered targets from this SendTargets Portal operation.<br/> |



 

### Properties

The **MSIscsiInitiator\_SendTargetPortalClass** class has these properties.

<dl> <dt>

**InitiatorName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the Initiator, which the iSCSI initiator service utilizes to transmit SendTargets requests to the specified Target Portal. If **NULL**, the iSCSI initiator service will use any Initiator that can reach the specified Target Portal.

</dd> <dt>

**InitiatorPortNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The port number on the Initiator to use for the SendTargets request. A value of **ISCSI\_ALL\_INITIATOR\_PORTS** indicates that the Initiator must select the appropriate port based upon current routing information.

</dd> <dt>

**LoginOptions**
</dt> <dd> <dl> <dt>

Data type: **MSIscsiInitiator\_TargetLoginOptions**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An [**MSIscsiInitiator\_TargetLoginOptions**](msiscsiinitiator-targetloginoptions.md) structure that contains the login options specified for use with the Target Portal.

</dd> <dt>

**PortalAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Portal address.

</dd> <dt>

**PortalIdentifierString**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Portal Identifier string.

</dd> <dt>

**PortalPort**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The port utilized by the Portal.

</dd> <dt>

**PortalSymbolicName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The symbolic name associated with the Portal.

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



 

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Namespace<br/>                | Root\\WMI<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>Iscsidsc.mof</dt> </dl> |



 

 




