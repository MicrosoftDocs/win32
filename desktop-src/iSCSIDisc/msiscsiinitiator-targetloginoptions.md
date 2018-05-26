---
Description: This MSIscsiInitiator\_TargetLoginOptions structure contains the target login options.
ms.assetid: 665b003e-2240-4bbc-8f41-29af4374a252
title: MSIscsiInitiator\_TargetLoginOptions class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSIscsiInitiator\_TargetLoginOptions class

This **MSIscsiInitiator\_TargetLoginOptions** structure contains the target login options.

## Syntax

``` syntax
class MSIscsiInitiator_TargetLoginOptions
{
  uint32                             Version;
  ISCSI_LOGIN_OPTIONS_INFO_SPECIFIED InformationSpecified;
  ISCSI_LOGIN_FLAGS                  LoginFlags;
  ISCSI_AUTH_TYPES                   AuthType;
  uint32                             HeaderDigest;
  uint32                             DataDigest;
  uint32                             MaximumConnections;
  uint32                             DefaultTime2Wait;
  uint32                             DefaultTime2Retain;
  uint8                              Username[];
  uint8                              Password[];
};
```

## Members

The **MSIscsiInitiator\_TargetLoginOptions** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSIscsiInitiator\_TargetLoginOptions** class has these properties.

<dl> <dt>

**AuthType**
</dt> <dd> <dl> <dt>

Data type: **ISCSI\_AUTH\_TYPES**
</dt> <dt>

Access type: Read/write
</dt> </dl>

An [**ISCSI\_AUTH\_TYPES**](/windows/previous-versions/Iscsidsc/ne-iscsidsc-iscsi_auth_types?branch=master) enumeration that indicates the authentication method used to establish a connection.

</dd> <dt>

**DataDigest**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A [**ISCSI\_DIGEST\_TYPES**](/windows/previous-versions/Iscsidsc/ne-iscsidsc-iscsi_digest_types?branch=master) value that indicates the method that the Initiator uses to verify the integrity of the data digest in a logon PDU.

</dd> <dt>

**DefaultTime2Retain**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum time, in seconds, to reassign a connection after the initial wait that is indicated in **DefaultTime2Wait** has elapsed. The Initiator and Target negotiate to determine this value.

</dd> <dt>

**DefaultTime2Wait**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The minimum time to wait, in seconds, before the Initiator attempts to reconnect or reassign a connection (or task) that has been dropped after an unexpected connection termination or reset. The Initiator and Target negotiate to determine this value.

</dd> <dt>

**HeaderDigest**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A [**ISCSI\_DIGEST\_TYPES**](/windows/previous-versions/Iscsidsc/ne-iscsidsc-iscsi_digest_types?branch=master) value that indicates the method that the Initiator uses to verify the integrity of the header digest in a logon PDU.

</dd> <dt>

**InformationSpecified**
</dt> <dd> <dl> <dt>

Data type: **ISCSI\_LOGIN\_OPTIONS\_INFO\_SPECIFIED**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A bitmap that indicates which members of this structure contain valid *dataLoginFlags*.



| Value                                                                                                                                                                                                                                            | Meaning                                                                                                                                                                          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="ISCSI_LOGIN_OPTIONS_HEADER_DIGEST"></span><span id="iscsi_login_options_header_digest"></span><dl> <dt>**ISCSI\_LOGIN\_OPTIONS\_HEADER\_DIGEST**</dt> </dl>                     | The **HeaderDigest** member specifies the type of digest that is used to guarantee the integrity of header data. <br/>                                                     |
| <span id="ISCSI_LOGIN_OPTIONS_DATA_DIGEST"></span><span id="iscsi_login_options_data_digest"></span><dl> <dt>**ISCSI\_LOGIN\_OPTIONS\_DATA\_DIGEST**</dt> </dl>                           | The **DataDigest** member specifies the type of digest that is used to guarantee the integrity of header data.<br/>                                                        |
| <span id="ISCSI_LOGIN_OPTIONS_MAXIMUM_CONNECTIONS"></span><span id="iscsi_login_options_maximum_connections"></span><dl> <dt>**ISCSI\_LOGIN\_OPTIONS\_MAXIMUM\_CONNECTIONS**</dt> </dl>   | The **MaximumConnections** member specifies the maximum number of connections that are allowed in the iSCSI session. <br/>                                                 |
| <span id="ISCSI_LOGIN_OPTIONS_DEFAULT_TIME_2_WAIT"></span><span id="iscsi_login_options_default_time_2_wait"></span><dl> <dt>**ISCSI\_LOGIN\_OPTIONS\_DEFAULT\_TIME\_2\_WAIT**</dt> </dl> | The **DefaultTime2Wait** member specifies the minimum time to wait, in seconds, before the initiator attempts to reconnect or reassign a connection that was dropped.<br/> |
| <span id="ISCSI_LOGIN_OPTIONS_AUTH_TYPE"></span><span id="iscsi_login_options_auth_type"></span><dl> <dt>**ISCSI\_LOGIN\_OPTIONS\_AUTH\_TYPE**</dt> </dl>                                 | The **AuthType** member specifies the type of authentication that establishes the logon session. <br/>                                                                     |
| <span id="ISCSI_LOGIN_OPTIONS_USERNAME"></span><span id="iscsi_login_options_username"></span><dl> <dt>**ISCSI\_LOGIN\_OPTIONS\_USERNAME**</dt> </dl>                                     | The user name to be used during logon. <br/>                                                                                                                               |
| <span id="ISCSI_LOGIN_OPTIONS_PASSWORD"></span><span id="iscsi_login_options_password"></span><dl> <dt>**ISCSI\_LOGIN\_OPTIONS\_PASSWORD**</dt> </dl>                                     | The password to be used during logon. <br/>                                                                                                                                |



 

</dd> <dt>

**LoginFlags**
</dt> <dd> <dl> <dt>

Data type: **ISCSI\_LOGIN\_FLAGS**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Defines the login process. Possible values are defined by the [**ISCSI\_LOGIN\_OPTIONS**](/windows/previous-versions/Iscsidsc/ns-iscsidsc-iscsi_login_options?branch=master) structure.



| Value                                                                                                                                                                                                                                     | Meaning                                                                                                                                                                                                                                                                                                                                                                    |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="ISCSI_LOGIN_FLAG_REQUIRE_IPSEC"></span><span id="iscsi_login_flag_require_ipsec"></span><dl> <dt>**ISCSI\_LOGIN\_FLAG\_REQUIRE\_IPSEC**</dt> </dl>                       | The logon session must use the IPsec protocol.<br/>                                                                                                                                                                                                                                                                                                                  |
| <span id="ISCSI_LOGIN_FLAG_MULTIPATH_ENABLED"></span><span id="iscsi_login_flag_multipath_enabled"></span><dl> <dt>**ISCSI\_LOGIN\_FLAG\_MULTIPATH\_ENABLED**</dt> </dl>           | Multipathing software is installed, so the iSCSI initiator service allows multiple sessions to the same target.<br/>                                                                                                                                                                                                                                                 |
| <span id="ISCSI_LOGIN_FLAG_RESERVED1"></span><span id="iscsi_login_flag_reserved1"></span><dl> <dt>**ISCSI\_LOGIN\_FLAG\_RESERVED1**</dt> </dl>                                    | Microsoft internal use only.<br/>                                                                                                                                                                                                                                                                                                                                    |
| <span id="ISCSI_LOGIN_FLAG_ALLOW_PORTAL_HOPPING"></span><span id="iscsi_login_flag_allow_portal_hopping"></span><dl> <dt>**ISCSI\_LOGIN\_FLAG\_ALLOW\_PORTAL\_HOPPING**</dt> </dl> | If a target portal is not available for login, the initiator can “hop” through the list of target portals that it discovered and that can be used for login operations. That is, the initiator will continue to try the list of portals that are available until it finds one that can be used for login, so it can then log in to the available target portal.<br/> |
| <span id="ISCSI_LOGIN_FLAG_RADIUS_RESPONSE"></span><span id="iscsi_login_flag_radius_response"></span><dl> <dt>**ISCSI\_LOGIN\_FLAG\_RADIUS\_RESPONSE**</dt> </dl>                 | Use RADIUS to generate CHAP response.<br/>                                                                                                                                                                                                                                                                                                                           |
| <span id="ISCSI_LOGIN_FLAG_RADIUS_VERIFICATION"></span><span id="iscsi_login_flag_radius_verification"></span><dl> <dt>**ISCSI\_LOGIN\_FLAG\_RADIUS\_VERIFICATION**</dt> </dl>     | Use RADIUS to verify CHAP response.<br/>                                                                                                                                                                                                                                                                                                                             |



 

</dd> <dt>

**MaximumConnections**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A value between 1 and 65535 that specifies the maximum number of connections to target devices that can be associated with a single logon session. A value of 0 indicates that there is no limit to the number of connections.

</dd> <dt>

**Password**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The password used for login.

</dd> <dt>

**Username**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The user name used for login.

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The ISCSI\_LoginOptions version information.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Namespace<br/>                | Root\\WMI<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>Iscsidsc.mof</dt> </dl> |



 

 




