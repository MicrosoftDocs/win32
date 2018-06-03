---
Description: This MSIscsiInitiator\_IKEPresharedKeyAuthenticationInfo structure describes the characteristics of shared keys utilized by the Initiator and the Target.
ms.assetid: 9a67f242-853b-425b-a006-e5d273d6cb71
title: MSIscsiInitiator\_IKEPresharedKeyAuthenticationInfo class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSIscsiInitiator\_IKEPresharedKeyAuthenticationInfo class

This **MSIscsiInitiator\_IKEPresharedKeyAuthenticationInfo** structure describes the characteristics of shared keys utilized by the Initiator and the Target.

## Syntax

``` syntax
class MSIscsiInitiator_IKEPresharedKeyAuthenticationInfo
{
  uint32               AuthMethod;
  ISCSI_SECURITY_FLAGS SecurityFlags;
  uint32               IdType;
  uint8                Id[];
  uint8                Key[];
};
```

## Members

The **MSIscsiInitiator\_IKEPresharedKeyAuthenticationInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSIscsiInitiator\_IKEPresharedKeyAuthenticationInfo** class has these properties.

<dl> <dt>

**AuthMethod**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The specified Preshared Key Authentication Method.

</dd> <dt>

**Id**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of authentication IDs.

</dd> <dt>

**IdType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The ID type to associate with the Preshared Key. The Initiator places this identifier (ID) in the Internet Key Exchange (IKE) identification payload to identify itself to the Target. The following table describes the possible identification payload types.



| Value                                                                                                                                                       | Meaning                                                                                                                                                       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="ID_IPV4_ADDR"></span><span id="id_ipv4_addr"></span><dl> <dt>**ID\_IPV4\_ADDR**</dt> </dl> | The Initiator identifies itself to the Target during the key exchange with a single 4-byte IPv4 address.<br/>                                           |
| <span id="ID_FQDN"></span><span id="id_fqdn"></span><dl> <dt>**ID\_FQDN**</dt> </dl>                 | The Initiator identifies itself to the Target during the key exchange with a fully qualified domain name string (for example, "website.com"). <br/>     |
| <span id="ID_USER_FQDN"></span><span id="id_user_fqdn"></span><dl> <dt>**ID\_USER\_FQDN**</dt> </dl> | The Initiator identifies itself to the Target during the key exchange with a fully qualified user name string (for example, "sample@example.com").<br/> |
| <span id="ID_IPV6_ADDR"></span><span id="id_ipv6_addr"></span><dl> <dt>**ID\_IPV6\_ADDR**</dt> </dl> | The Initiator identifies itself to the Target during the key exchange with a single 16-byte IPv6 address.<br/>                                          |



 

</dd> <dt>

**Key**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of keys.

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
| <span id="ISCSI_SECURITY_FLAG_TUNNEL_MODE_PREFERRED"></span><span id="iscsi_security_flag_tunnel_mode_preferred"></span><dl> <dt>**ISCSI\_SECURITY\_FLAG\_TUNNEL\_MODE\_PREFERRED**</dt> </dl>          | The Host Bus Adapter (HBA) initiator should establish the TCP/IP connection to the target portal using IPsec tunnel mode. <br/>                                            |
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



 

 




