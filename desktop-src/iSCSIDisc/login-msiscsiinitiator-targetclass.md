---
Description: The Login method initiates a login to the target.
ms.assetid: e86bb4d8-fcf1-480a-b267-33ff4d55f03a
title: Login method of the MSIscsiInitiator\_TargetClass class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Login method of the MSIscsiInitiator\_TargetClass class

The **Login** method initiates a login to the target.

## Syntax


```mof
uint32 Login(
  [in]  boolean                             IsInformationalSession,
  [in]  uint32                              InitiatorPortNumber,
  [in]  MSIscsiInitiator_Portal             TargetPortal,
  [in]  ISCSI_SECURITY_FLAGS                SecurityFlags,
  [in]  MSIscsiInitiator_TargetMappings     Mappings[],
  [in]  MSIscsiInitiator_TargetLoginOptions LoginOptions,
  [in]  uint8                               Key[],
  [in]  boolean                             IsPersistent,
  [out] string                              UniqueSessionId,
  [out] string                              UniqueConnectionId
);
```



## Parameters

<dl> <dt>

*IsInformationalSession* \[in\]
</dt> <dd>

Indicates if the session is informational.

</dd> <dt>

*InitiatorPortNumber* \[in\]
</dt> <dd>

The initiator port number for the connection.

</dd> <dt>

*TargetPortal* \[in\]
</dt> <dd>

An [**MSIscsiInitiator\_Portal**](msiscsiinitiator-portal.md) structure containing the target portal information used to establish the connection.

</dd> <dt>

*SecurityFlags* \[in\]
</dt> <dd>

A bitmap that defines the security characteristics of a login connection.



| Value                                                                                                                                                                                                                                                          | Meaning                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="ISCSI_SECURITY_FLAG_TUNNEL_MODE_PREFERRED"></span><span id="iscsi_security_flag_tunnel_mode_preferred"></span><dl> <dt>**ISCSI\_SECURITY\_FLAG\_TUNNEL\_MODE\_PREFERRED**</dt> </dl>          | The Host Bus Adapter (HBA) initiator should establish the TCP/IP connection to the target portal using IPsec tunnel mode. <br/>                                            |
| <span id="ISCSI_SECURITY_FLAG_TRANSPORT_MODE_PREFERRED"></span><span id="iscsi_security_flag_transport_mode_preferred"></span><dl> <dt>**ISCSI\_SECURITY\_FLAG\_TRANSPORT\_MODE\_PREFERRED**</dt> </dl> | The HBA initiator should establish the TCP/IP connection to the target portal using IPsec transport mode.<br/>                                                             |
| <span id="ISCSI_SECURITY_FLAG_PFS_ENABLED"></span><span id="iscsi_security_flag_pfs_enabled"></span><dl> <dt>**ISCSI\_SECURITY\_FLAG\_PFS\_ENABLED**</dt> </dl>                                         | The HBA initiator should establish the TCP/IP connection to the target portal with Perfect Forward Secrecy (PFS) mode enabled if IPsec is required.<br/>                   |
| <span id="ISCSI_SECURITY_FLAG_AGGRESSIVE_MODE_ENABLED"></span><span id="iscsi_security_flag_aggressive_mode_enabled"></span><dl> <dt>**ISCSI\_SECURITY\_FLAG\_AGGRESSIVE\_MODE\_ENABLED**</dt> </dl>    | The HBA initiator should establish the TCP/IP connection to the target portal with aggressive mode enabled.<br/>                                                           |
| <span id="ISCSI_SECURITY_FLAG_MAIN_MODE_ENABLED"></span><span id="iscsi_security_flag_main_mode_enabled"></span><dl> <dt>**ISCSI\_SECURITY\_FLAG\_MAIN\_MODE\_ENABLED**</dt> </dl>                      | The HBA initiator should establish the TCP/IP connection to the target portal with main mode enabled.<br/>                                                                 |
| <span id="ISCSI_SECURITY_FLAG_IKE_IPSEC_ENABLED"></span><span id="iscsi_security_flag_ike_ipsec_enabled"></span><dl> <dt>**ISCSI\_SECURITY\_FLAG\_IKE\_IPSEC\_ENABLED**</dt> </dl>                      | The HBA initiator should establish the TCP/IP connection to the target portal using IKE/IPsec protocol. If not set then IPsec is not required to login to the target.<br/> |
| <span id="ISCSI_SECURITY_FLAG_VALID"></span><span id="iscsi_security_flag_valid"></span><dl> <dt>**ISCSI\_SECURITY\_FLAG\_VALID**</dt> </dl>                                                            | The other mask values are valid; otherwise, security flags are not specified.<br/>                                                                                         |



 

</dd> <dt>

*Mappings* \[in\]
</dt> <dd>

An array of [**MSIscsiInitiator\_TargetMappings**](msiscsiinitiator-targetmappings.md) structure which contain information about LUN mapping.

</dd> <dt>

*LoginOptions* \[in\]
</dt> <dd>

An array of [**MSIscsiInitiator\_TargetLoginOptions**](msiscsiinitiator-targetloginoptions.md) structures which contain information about target login options.

</dd> <dt>

*Key* \[in\]
</dt> <dd>

Indicates the login key.

</dd> <dt>

*IsPersistent* \[in\]
</dt> <dd>

Indicates if the login operation persists.

</dd> <dt>

*UniqueSessionId* \[out\]
</dt> <dd>

Indicates the unique ID generated for the session.

</dd> <dt>

*UniqueConnectionId* \[out\]
</dt> <dd>

Indicates the unique connection ID generated for this login operation.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Namespace<br/>                | Root\\WMI<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>Iscsidsc.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSIscsiInitiator\_Portal**](msiscsiinitiator-portal.md)
</dt> <dt>

[**MSIscsiInitiator\_TargetMappings**](msiscsiinitiator-targetmappings.md)
</dt> <dt>

[**MSIscsiInitiator\_TargetLoginOptions**](msiscsiinitiator-targetloginoptions.md)
</dt> <dt>

[**MSIscsiInitiator\_TargetClass**](msiscsiinitiator-targetclass.md)
</dt> </dl>

 

 




