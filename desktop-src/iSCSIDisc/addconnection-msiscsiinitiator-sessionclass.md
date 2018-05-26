---
Description: The AddConnection method adds a new connection to the specified session.
ms.assetid: 6f116e76-7c62-46ba-bb8f-ea23e1d8fa87
title: AddConnection method of the MSIscsiInitiator\_SessionClass class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AddConnection method of the MSIscsiInitiator\_SessionClass class

The **AddConnection** method adds a new connection to the specified session.

## Syntax


```mof
uint32 AddConnection(
  [in]  uint32                              InitiatorPortNumber,
  [in]  MSIscsiInitiator_Portal             TargetPortal,
  [in]  ISCSI_SECURITY_FLAGS                SecurityFlags,
  [in]  MSIscsiInitiator_TargetLoginOptions LoginOptions,
  [in]  uint8                               Key[],
  [out] string                              UniqueConnectionId
);
```



## Parameters

<dl> <dt>

*InitiatorPortNumber* \[in\]
</dt> <dd>

The port number associated with the Initiator.

</dd> <dt>

*TargetPortal* \[in\]
</dt> <dd>

An [**MSIscsiInitiator\_Portal**](msiscsiinitiator-portal.md) structure that contains information about the Target Portal.

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

*LoginOptions* \[in\]
</dt> <dd>

An [**MSIscsiInitiator\_TargetLoginOptions**](msiscsiinitiator-targetloginoptions.md) structure that specifies the characteristics of the login session.

</dd> <dt>

*Key* \[in\]
</dt> <dd>

The key used for authentication.

</dd> <dt>

*UniqueConnectionId* \[out\]
</dt> <dd>

The unique ID associated with the new connection.

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

[**MSIscsiInitiator\_SessionClass**](msiscsiinitiator-sessionclass.md)
</dt> </dl>

 

 




