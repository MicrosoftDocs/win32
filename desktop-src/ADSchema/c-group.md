---
title: Group class
description: Stores a list of user names. Used to apply security principals on resources.
ms.assetid: e8ce5c43-d0fb-4c67-a6ef-7094fb7e7669
ms.tgt_platform: multiple
keywords:
- Group class AD Schema
- group class AD Schema
topic_type:
- apiref
api_name:
- Group
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# Group class

Stores a list of user names. Used to apply security principals on resources.



| Entry | Value |
|-------------------|------------------------------------------------|
| CN                | Group                                          |
| Ldap-Display-Name | group                                          |
| Update Privilege  | This value is set by the domain administrator. |
| Update Frequency  | \-                                             |
| Schema-Id-Guid    | bf967a9c-0de6-11d0-a285-00aa003049e2           |



## Implementations

-   [**Windows 2000 Server**](#windows-2000-server)
-   [**Windows Server 2003**](#windows-server-2003)
-   [**ADAM**](#adam-attributes)
-   [**Windows Server 2003 R2**](#windows-server-2003-r2)
-   [**Windows Server 2008**](#windows-server-2008)
-   [**Windows Server 2008 R2**](#windows-server-2008-r2)
-   [**Windows Server 2012**](#windows-server-2012)

## Windows 2000 Server

-   [Attributes](#windows-2000-server-attributes)
-   [Extended Rights](#windows-2000-server-extended-rights)
-   [Validated Writes](#windows-2000-server-validated-writes)
-   [Property Sets](#windows-2000-server-property-sets)



| Entry | Value |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| System-Only                 | False                                                                                                                                                                                               |
| Object-Category             | 1                                                                                                                                                                                                   |
| Default-Object-Category     | \-                                                                                                                                                                                                  |
| Governs-Id                  | 1.2.840.113556.1.5.8                                                                                                                                                                                |
| Default-Hiding-Value        | 0                                                                                                                                                                                                   |
| Rdn-Att-Id                  | [**Common-Name**](a-cn.md)<br/>                                                                                                                                                              |
| Subclass of                 | [**Top**](c-top.md)<br/>                                                                                                                                                                     |
| Possible Superiors          | [**Domain-DNS**](c-domaindns.md)[**Organizational-Unit**](c-organizationalunit.md)[**Builtin-Domain**](c-builtindomain.md)[**Container**](c-container.md)                                       |
| Auxiliary Classes           | [**Security-Principal**](c-securityprincipal.md) (System)[**Mail-Recipient**](c-mailrecipient.md) (System)                                                                                        |
| NT-Security-Descriptor      | O:BAG:BAD:S:                                                                                                                                                                                        |
| Default Security Descriptor | D:(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;DA)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;SY)(A;;RPLCLORC;;;AU)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;AO)(A;;RPLCLORC;;;PS)(OA;;CR;ab721a55-1e2f-11d0-9819-00aa0040529b;;AU) |
| System-Flags                | 0x00000010                                                                                                                                                                                          |



## Windows 2000 Server Attributes

This class contains the following attributes for Windows 2000 Server:



| Attribute                                                                    | Mandatory | Derived from                                                                                 |
|------------------------------------------------------------------------------|-----------|----------------------------------------------------------------------------------------------|
| [**Account-Name-History**](a-accountnamehistory.md)                         | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                 |
| [**Admin-Count**](a-admincount.md)                                          | False     | **Group**                                                                                    |
| [**Admin-Description**](a-admindescription.md)                              | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Admin-Display-Name**](a-admindisplayname.md)                             | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Allowed-Attributes**](a-allowedattributes.md)                            | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Allowed-Attributes-Effective**](a-allowedattributeseffective.md)         | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Allowed-Child-Classes**](a-allowedchildclasses.md)                       | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Allowed-Child-Classes-Effective**](a-allowedchildclasseseffective.md)    | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Alt-Security-Identities**](a-altsecurityidentities.md)                   | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                 |
| [**Bridgehead-Server-List-BL**](a-bridgeheadserverlistbl.md)                | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Canonical-Name**](a-canonicalname.md)                                    | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Comment**](a-info.md)                                                    | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                         |
| [**Common-Name**](a-cn.md)                                                  | True      | [**Top**](c-top.md)<br/> [**Mail-Recipient**](c-mailrecipient.md)<br/>         |
| [**Control-Access-Rights**](a-controlaccessrights.md)                       | False     | **Group**                                                                                    |
| [**Create-Time-Stamp**](a-createtimestamp.md)                               | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Description**](a-description.md)                                         | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Desktop-Profile**](a-desktopprofile.md)                                  | False     | **Group**                                                                                    |
| [**Display-Name**](a-displayname.md)                                        | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Display-Name-Printable**](a-displaynameprintable.md)                     | False     | [**Top**](c-top.md)<br/>                                                              |
| [**DSA-Signature**](a-dsasignature.md)                                      | False     | [**Top**](c-top.md)<br/>                                                              |
| [**DS-Core-Propagation-Data**](a-dscorepropagationdata.md)                  | False     | [**Top**](c-top.md)<br/>                                                              |
| [**E-mail-Addresses**](a-mail.md)                                           | False     | **Group**                                                                                    |
| [**Extension-Name**](a-extensionname.md)                                    | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Flags**](a-flags.md)                                                     | False     | [**Top**](c-top.md)<br/>                                                              |
| [**From-Entry**](a-fromentry.md)                                            | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Frs-Computer-Reference-BL**](a-frscomputerreferencebl.md)                | False     | [**Top**](c-top.md)<br/>                                                              |
| [**FRS-Member-Reference-BL**](a-frsmemberreferencebl.md)                    | False     | [**Top**](c-top.md)<br/>                                                              |
| [**FSMO-Role-Owner**](a-fsmoroleowner.md)                                   | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Garbage-Coll-Period**](a-garbagecollperiod.md)                           | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                         |
| [**Group-Attributes**](a-groupattributes.md)                                | False     | **Group**                                                                                    |
| [**Group-Membership-SAM**](a-groupmembershipsam.md)                         | False     | **Group**                                                                                    |
| [**Group-Type**](a-grouptype.md)                                            | True      | **Group**                                                                                    |
| [**Instance-Type**](a-instancetype.md)                                      | True      | [**Top**](c-top.md)<br/>                                                              |
| [**Is-Critical-System-Object**](a-iscriticalsystemobject.md)                | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Is-Deleted**](a-isdeleted.md)                                            | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Is-Member-Of-DL**](a-memberof.md)                                        | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Is-Privilege-Holder**](a-isprivilegeholder.md)                           | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Last-Known-Parent**](a-lastknownparent.md)                               | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Legacy-Exchange-DN**](a-legacyexchangedn.md)                             | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                         |
| [**Managed-By**](a-managedby.md)                                            | False     | **Group**                                                                                    |
| [**Managed-Objects**](a-managedobjects.md)                                  | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Mastered-By**](a-masteredby.md)                                          | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Member**](a-member.md)                                                   | False     | **Group**                                                                                    |
| [**Modify-Time-Stamp**](a-modifytimestamp.md)                               | False     | [**Top**](c-top.md)<br/>                                                              |
| [**MS-DS-Consistency-Child-Count**](a-ms-ds-consistencychildcount.md)       | False     | [**Top**](c-top.md)<br/>                                                              |
| [**MS-DS-Consistency-Guid**](a-ms-ds-consistencyguid.md)                    | False     | [**Top**](c-top.md)<br/>                                                              |
| [**netboot-SCP-BL**](a-netbootscpbl.md)                                     | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Non-Security-Member**](a-nonsecuritymember.md)                           | False     | **Group**                                                                                    |
| [**Non-Security-Member-BL**](a-nonsecuritymemberbl.md)                      | False     | [**Top**](c-top.md)<br/>                                                              |
| [**NT-Group-Members**](a-ntgroupmembers.md)                                 | False     | **Group**                                                                                    |
| [**NT-Security-Descriptor**](a-ntsecuritydescriptor.md)                     | True      | [**Top**](c-top.md)<br/> [**Security-Principal**](c-securityprincipal.md)<br/> |
| [**Obj-Dist-Name**](a-distinguishedname.md)                                 | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Object-Category**](a-objectcategory.md)                                  | True      | [**Top**](c-top.md)<br/>                                                              |
| [**Object-Class**](a-objectclass.md)                                        | True      | [**Top**](c-top.md)<br/>                                                              |
| [**Object-Guid**](a-objectguid.md)                                          | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Object-Sid**](a-objectsid.md)                                            | True      | [**Security-Principal**](c-securityprincipal.md)<br/>                                 |
| [**Object-Version**](a-objectversion.md)                                    | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Operator-Count**](a-operatorcount.md)                                    | False     | **Group**                                                                                    |
| [**Other-Well-Known-Objects**](a-otherwellknownobjects.md)                  | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Partial-Attribute-Deletion-List**](a-partialattributedeletionlist.md)    | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Partial-Attribute-Set**](a-partialattributeset.md)                       | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Possible-Inferiors**](a-possibleinferiors.md)                            | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Primary-Group-Token**](a-primarygrouptoken.md)                           | False     | **Group**                                                                                    |
| [**Proxied-Object-Name**](a-proxiedobjectname.md)                           | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Proxy-Addresses**](a-proxyaddresses.md)                                  | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Query-Policy-BL**](a-querypolicybl.md)                                   | False     | [**Top**](c-top.md)<br/>                                                              |
| [**RDN**](a-name.md)                                                        | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Repl-Property-Meta-Data**](a-replpropertymetadata.md)                    | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Repl-UpToDate-Vector**](a-repluptodatevector.md)                         | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Reports**](a-directreports.md)                                           | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Reps-From**](a-repsfrom.md)                                              | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Reps-To**](a-repsto.md)                                                  | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Revision**](a-revision.md)                                               | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Rid**](a-rid.md)                                                         | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                 |
| [**SAM-Account-Name**](a-samaccountname.md)                                 | True      | [**Security-Principal**](c-securityprincipal.md)<br/>                                 |
| [**SAM-Account-Type**](a-samaccounttype.md)                                 | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                 |
| [**SD-Rights-Effective**](a-sdrightseffective.md)                           | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Security-Identifier**](a-securityidentifier.md)                          | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                 |
| [**Server-Reference-BL**](a-serverreferencebl.md)                           | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Show-In-Address-Book**](a-showinaddressbook.md)                          | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                         |
| [**Show-In-Advanced-View-Only**](a-showinadvancedviewonly.md)               | False     | [**Top**](c-top.md)<br/>                                                              |
| [**SID-History**](a-sidhistory.md)                                          | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                 |
| [**Site-Object-BL**](a-siteobjectbl.md)                                     | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Sub-Refs**](a-subrefs.md)                                                | False     | [**Top**](c-top.md)<br/>                                                              |
| [**SubSchemaSubEntry**](a-subschemasubentry.md)                             | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Supplemental-Credentials**](a-supplementalcredentials.md)                | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                 |
| [**System-Flags**](a-systemflags.md)                                        | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Telephone-Number**](a-telephonenumber.md)                                | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                         |
| [**Text-Encoded-OR-Address**](a-textencodedoraddress.md)                    | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                         |
| [**Token-Groups**](a-tokengroups.md)                                        | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                 |
| [**Token-Groups-Global-And-Universal**](a-tokengroupsglobalanduniversal.md) | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                 |
| [**Token-Groups-No-GC-Acceptable**](a-tokengroupsnogcacceptable.md)         | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                 |
| [**User-Cert**](a-usercert.md)                                              | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                         |
| [**User-SMIME-Certificate**](a-usersmimecertificate.md)                     | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                         |
| [**USN-Changed**](a-usnchanged.md)                                          | False     | [**Top**](c-top.md)<br/>                                                              |
| [**USN-Created**](a-usncreated.md)                                          | False     | [**Top**](c-top.md)<br/>                                                              |
| [**USN-DSA-Last-Obj-Removed**](a-usndsalastobjremoved.md)                   | False     | [**Top**](c-top.md)<br/>                                                              |
| [**USN-Intersite**](a-usnintersite.md)                                      | False     | [**Top**](c-top.md)<br/>                                                              |
| [**USN-Last-Obj-Rem**](a-usnlastobjrem.md)                                  | False     | [**Top**](c-top.md)<br/>                                                              |
| [**USN-Source**](a-usnsource.md)                                            | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Wbem-Path**](a-wbempath.md)                                              | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Well-Known-Objects**](a-wellknownobjects.md)                             | False     | [**Top**](c-top.md)<br/>                                                              |
| [**When-Changed**](a-whenchanged.md)                                        | False     | [**Top**](c-top.md)<br/>                                                              |
| [**When-Created**](a-whencreated.md)                                        | False     | [**Top**](c-top.md)<br/>                                                              |
| [**WWW-Home-Page**](a-wwwhomepage.md)                                       | False     | [**Top**](c-top.md)<br/>                                                              |
| [**WWW-Page-Other**](a-url.md)                                              | False     | [**Top**](c-top.md)<br/>                                                              |
| [**X509-Cert**](a-usercertificate.md)                                       | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                         |



## Windows 2000 Server Extended Rights

This class contains the following extended rights for Windows 2000 Server:



| Common Name                  |
|------------------------------|
| [**Send-To**](r-send-to.md) |



## Windows 2000 Server Validated Writes

This class contains the following validated writes for Windows 2000 Server:



| Common Name                                  |
|----------------------------------------------|
| [**Self-Membership**](r-self-membership.md) |



## Windows 2000 Server Property Sets

This class contains the following property sets for Windows 2000 Server:



| Common Name                                      |
|--------------------------------------------------|
| [**Email-Information**](r-email-information.md) |



## Windows Server 2003

-   [Attributes](#windows-server-2003-attributes)
-   [Extended Rights](#windows-server-2003-extended-rights)
-   [Validated Writes](#windows-server-2003-validated-writes)
-   [Property Sets](#windows-server-2003-property-sets)



| Entry | Value |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| System-Only                 | False                                                                                                                                                                                                                                                                                                            |
| Object-Category             | 1                                                                                                                                                                                                                                                                                                                |
| Default-Object-Category     | \-                                                                                                                                                                                                                                                                                                               |
| Governs-Id                  | 1.2.840.113556.1.5.8                                                                                                                                                                                                                                                                                             |
| Default-Hiding-Value        | 0                                                                                                                                                                                                                                                                                                                |
| Rdn-Att-Id                  | [**Common-Name**](a-cn.md)<br/>                                                                                                                                                                                                                                                                           |
| Subclass of                 | [**Top**](c-top.md)<br/>                                                                                                                                                                                                                                                                                  |
| Possible Superiors          | [**Domain-DNS**](c-domaindns.md)[**Organizational-Unit**](c-organizationalunit.md)[**Builtin-Domain**](c-builtindomain.md)[**Container**](c-container.md)[**ms-DS-Az-Admin-Manager**](c-msds-azadminmanager.md)[**ms-DS-Az-Application**](c-msds-azapplication.md)[**ms-DS-Az-Scope**](c-msds-azscope.md) |
| Auxiliary Classes           | [**Security-Principal**](c-securityprincipal.md) (System)[**Mail-Recipient**](c-mailrecipient.md) (System)                                                                                                                                                                                                     |
| NT-Security-Descriptor      | O:BAG:BAD:S:                                                                                                                                                                                                                                                                                                     |
| Default Security Descriptor | D:(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;DA)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;SY)(A;;RPLCLORC;;;AU)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;AO)(A;;RPLCLORC;;;PS)(OA;;CR;ab721a55-1e2f-11d0-9819-00aa0040529b;;AU)(OA;;RP;46a9b11d-60ae-405a-b7e8-ff8a58d456d2;;S-1-5-32-560)                                                   |
| System-Flags                | 0x00000010                                                                                                                                                                                                                                                                                                       |



## Windows Server 2003 Attributes

This class contains the following attributes for Windows Server 2003:



| Attribute                                                                    | Mandatory | Derived from                                                                                 |
|------------------------------------------------------------------------------|-----------|----------------------------------------------------------------------------------------------|
| [**Account-Name-History**](a-accountnamehistory.md)                         | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                 |
| [**Admin-Count**](a-admincount.md)                                          | False     | **Group**                                                                                    |
| [**Admin-Description**](a-admindescription.md)                              | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Admin-Display-Name**](a-admindisplayname.md)                             | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Allowed-Attributes**](a-allowedattributes.md)                            | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Allowed-Attributes-Effective**](a-allowedattributeseffective.md)         | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Allowed-Child-Classes**](a-allowedchildclasses.md)                       | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Allowed-Child-Classes-Effective**](a-allowedchildclasseseffective.md)    | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Alt-Security-Identities**](a-altsecurityidentities.md)                   | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                 |
| [**Bridgehead-Server-List-BL**](a-bridgeheadserverlistbl.md)                | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Canonical-Name**](a-canonicalname.md)                                    | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Comment**](a-info.md)                                                    | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                         |
| [**Common-Name**](a-cn.md)                                                  | True      | [**Top**](c-top.md)<br/> [**Mail-Recipient**](c-mailrecipient.md)<br/>         |
| [**Control-Access-Rights**](a-controlaccessrights.md)                       | False     | **Group**                                                                                    |
| [**Create-Time-Stamp**](a-createtimestamp.md)                               | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Description**](a-description.md)                                         | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Desktop-Profile**](a-desktopprofile.md)                                  | False     | **Group**                                                                                    |
| [**Display-Name**](a-displayname.md)                                        | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Display-Name-Printable**](a-displaynameprintable.md)                     | False     | [**Top**](c-top.md)<br/>                                                              |
| [**DSA-Signature**](a-dsasignature.md)                                      | False     | [**Top**](c-top.md)<br/>                                                              |
| [**DS-Core-Propagation-Data**](a-dscorepropagationdata.md)                  | False     | [**Top**](c-top.md)<br/>                                                              |
| [**E-mail-Addresses**](a-mail.md)                                           | False     | **Group**                                                                                    |
| [**Extension-Name**](a-extensionname.md)                                    | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Flags**](a-flags.md)                                                     | False     | [**Top**](c-top.md)<br/>                                                              |
| [**From-Entry**](a-fromentry.md)                                            | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Frs-Computer-Reference-BL**](a-frscomputerreferencebl.md)                | False     | [**Top**](c-top.md)<br/>                                                              |
| [**FRS-Member-Reference-BL**](a-frsmemberreferencebl.md)                    | False     | [**Top**](c-top.md)<br/>                                                              |
| [**FSMO-Role-Owner**](a-fsmoroleowner.md)                                   | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Garbage-Coll-Period**](a-garbagecollperiod.md)                           | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                         |
| [**Group-Attributes**](a-groupattributes.md)                                | False     | **Group**                                                                                    |
| [**Group-Membership-SAM**](a-groupmembershipsam.md)                         | False     | **Group**                                                                                    |
| [**Group-Type**](a-grouptype.md)                                            | True      | **Group**                                                                                    |
| [**Instance-Type**](a-instancetype.md)                                      | True      | [**Top**](c-top.md)<br/>                                                              |
| [**Is-Critical-System-Object**](a-iscriticalsystemobject.md)                | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Is-Deleted**](a-isdeleted.md)                                            | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Is-Member-Of-DL**](a-memberof.md)                                        | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Is-Privilege-Holder**](a-isprivilegeholder.md)                           | False     | [**Top**](c-top.md)<br/>                                                              |
| [**labeledURI**](a-labeleduri.md)                                           | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                         |
| [**Last-Known-Parent**](a-lastknownparent.md)                               | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Legacy-Exchange-DN**](a-legacyexchangedn.md)                             | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                         |
| [**Managed-By**](a-managedby.md)                                            | False     | **Group**                                                                                    |
| [**Managed-Objects**](a-managedobjects.md)                                  | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Mastered-By**](a-masteredby.md)                                          | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Member**](a-member.md)                                                   | False     | **Group**                                                                                    |
| [**Modify-Time-Stamp**](a-modifytimestamp.md)                               | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-COM-PartitionSetLink**](a-mscom-partitionsetlink.md)                  | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-COM-UserLink**](a-mscom-userlink.md)                                  | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-DS-Approx-Immed-Subordinates**](a-msds-approx-immed-subordinates.md)  | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-DS-Az-LDAP-Query**](a-msds-azldapquery.md)                            | False     | **Group**                                                                                    |
| [**MS-DS-Consistency-Child-Count**](a-ms-ds-consistencychildcount.md)       | False     | [**Top**](c-top.md)<br/>                                                              |
| [**MS-DS-Consistency-Guid**](a-ms-ds-consistencyguid.md)                    | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-DS-KeyVersionNumber**](a-msds-keyversionnumber.md)                    | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                 |
| [**ms-DS-Mastered-By**](a-msds-masteredby.md)                               | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-DS-Members-For-Az-Role-BL**](a-msds-membersforazrolebl.md)            | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-DS-NC-Repl-Cursors**](a-msds-ncreplcursors.md)                        | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-DS-NC-Repl-Inbound-Neighbors**](a-msds-ncreplinboundneighbors.md)     | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-DS-NC-Repl-Outbound-Neighbors**](a-msds-ncreploutboundneighbors.md)   | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-DS-Non-Members**](a-msds-nonmembers.md)                               | False     | **Group**                                                                                    |
| [**ms-DS-Non-Members-BL**](a-msds-nonmembersbl.md)                          | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-DS-Object-Reference-BL**](a-msds-objectreferencebl.md)                | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-DS-Operations-For-Az-Role-BL**](a-msds-operationsforazrolebl.md)      | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-DS-Operations-For-Az-Task-BL**](a-msds-operationsforaztaskbl.md)      | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-DS-Repl-Attribute-Meta-Data**](a-msds-replattributemetadata.md)       | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-DS-Repl-Value-Meta-Data**](a-msds-replvaluemetadata.md)               | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-DS-Tasks-For-Az-Role-BL**](a-msds-tasksforazrolebl.md)                | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-DS-Tasks-For-Az-Task-BL**](a-msds-tasksforaztaskbl.md)                | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-Exch-Assistant-Name**](a-msexchassistantname.md)                      | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                         |
| [**ms-Exch-LabeledURI**](a-msexchlabeleduri.md)                             | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                         |
| [**ms-Exch-Owner-BL**](a-ownerbl.md)                                        | False     | [**Top**](c-top.md)<br/>                                                              |
| [**netboot-SCP-BL**](a-netbootscpbl.md)                                     | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Non-Security-Member**](a-nonsecuritymember.md)                           | False     | **Group**                                                                                    |
| [**Non-Security-Member-BL**](a-nonsecuritymemberbl.md)                      | False     | [**Top**](c-top.md)<br/>                                                              |
| [**NT-Group-Members**](a-ntgroupmembers.md)                                 | False     | **Group**                                                                                    |
| [**NT-Security-Descriptor**](a-ntsecuritydescriptor.md)                     | True      | [**Top**](c-top.md)<br/> [**Security-Principal**](c-securityprincipal.md)<br/> |
| [**Obj-Dist-Name**](a-distinguishedname.md)                                 | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Object-Category**](a-objectcategory.md)                                  | True      | [**Top**](c-top.md)<br/>                                                              |
| [**Object-Class**](a-objectclass.md)                                        | True      | [**Top**](c-top.md)<br/>                                                              |
| [**Object-Guid**](a-objectguid.md)                                          | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Object-Sid**](a-objectsid.md)                                            | True      | [**Security-Principal**](c-securityprincipal.md)<br/>                                 |
| [**Object-Version**](a-objectversion.md)                                    | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Operator-Count**](a-operatorcount.md)                                    | False     | **Group**                                                                                    |
| [**Other-Well-Known-Objects**](a-otherwellknownobjects.md)                  | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Partial-Attribute-Deletion-List**](a-partialattributedeletionlist.md)    | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Partial-Attribute-Set**](a-partialattributeset.md)                       | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Possible-Inferiors**](a-possibleinferiors.md)                            | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Primary-Group-Token**](a-primarygrouptoken.md)                           | False     | **Group**                                                                                    |
| [**Proxied-Object-Name**](a-proxiedobjectname.md)                           | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Proxy-Addresses**](a-proxyaddresses.md)                                  | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Query-Policy-BL**](a-querypolicybl.md)                                   | False     | [**Top**](c-top.md)<br/>                                                              |
| [**RDN**](a-name.md)                                                        | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Repl-Property-Meta-Data**](a-replpropertymetadata.md)                    | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Repl-UpToDate-Vector**](a-repluptodatevector.md)                         | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Reports**](a-directreports.md)                                           | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Reps-From**](a-repsfrom.md)                                              | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Reps-To**](a-repsto.md)                                                  | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Revision**](a-revision.md)                                               | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Rid**](a-rid.md)                                                         | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                 |
| [**SAM-Account-Name**](a-samaccountname.md)                                 | True      | [**Security-Principal**](c-securityprincipal.md)<br/>                                 |
| [**SAM-Account-Type**](a-samaccounttype.md)                                 | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                 |
| [**SD-Rights-Effective**](a-sdrightseffective.md)                           | False     | [**Top**](c-top.md)<br/>                                                              |
| [**secretary**](a-secretary.md)                                             | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                         |
| [**Security-Identifier**](a-securityidentifier.md)                          | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                 |
| [**Server-Reference-BL**](a-serverreferencebl.md)                           | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Show-In-Address-Book**](a-showinaddressbook.md)                          | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                         |
| [**Show-In-Advanced-View-Only**](a-showinadvancedviewonly.md)               | False     | [**Top**](c-top.md)<br/>                                                              |
| [**SID-History**](a-sidhistory.md)                                          | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                 |
| [**Site-Object-BL**](a-siteobjectbl.md)                                     | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Structural-Object-Class**](a-structuralobjectclass.md)                   | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Sub-Refs**](a-subrefs.md)                                                | False     | [**Top**](c-top.md)<br/>                                                              |
| [**SubSchemaSubEntry**](a-subschemasubentry.md)                             | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Supplemental-Credentials**](a-supplementalcredentials.md)                | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                 |
| [**System-Flags**](a-systemflags.md)                                        | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Telephone-Number**](a-telephonenumber.md)                                | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                         |
| [**Text-Encoded-OR-Address**](a-textencodedoraddress.md)                    | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                         |
| [**Token-Groups**](a-tokengroups.md)                                        | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                 |
| [**Token-Groups-Global-And-Universal**](a-tokengroupsglobalanduniversal.md) | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                 |
| [**Token-Groups-No-GC-Acceptable**](a-tokengroupsnogcacceptable.md)         | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                 |
| [**User-Cert**](a-usercert.md)                                              | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                         |
| [**User-SMIME-Certificate**](a-usersmimecertificate.md)                     | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                         |
| [**USN-Changed**](a-usnchanged.md)                                          | False     | [**Top**](c-top.md)<br/>                                                              |
| [**USN-Created**](a-usncreated.md)                                          | False     | [**Top**](c-top.md)<br/>                                                              |
| [**USN-DSA-Last-Obj-Removed**](a-usndsalastobjremoved.md)                   | False     | [**Top**](c-top.md)<br/>                                                              |
| [**USN-Intersite**](a-usnintersite.md)                                      | False     | [**Top**](c-top.md)<br/>                                                              |
| [**USN-Last-Obj-Rem**](a-usnlastobjrem.md)                                  | False     | [**Top**](c-top.md)<br/>                                                              |
| [**USN-Source**](a-usnsource.md)                                            | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Wbem-Path**](a-wbempath.md)                                              | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Well-Known-Objects**](a-wellknownobjects.md)                             | False     | [**Top**](c-top.md)<br/>                                                              |
| [**When-Changed**](a-whenchanged.md)                                        | False     | [**Top**](c-top.md)<br/>                                                              |
| [**When-Created**](a-whencreated.md)                                        | False     | [**Top**](c-top.md)<br/>                                                              |
| [**WWW-Home-Page**](a-wwwhomepage.md)                                       | False     | [**Top**](c-top.md)<br/>                                                              |
| [**WWW-Page-Other**](a-url.md)                                              | False     | [**Top**](c-top.md)<br/>                                                              |
| [**X509-Cert**](a-usercertificate.md)                                       | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                         |



## Windows Server 2003 Extended Rights

This class contains the following extended rights for Windows Server 2003:



| Common Name                  |
|------------------------------|
| [**Send-To**](r-send-to.md) |



## Windows Server 2003 Validated Writes

This class contains the following validated writes for Windows Server 2003:



| Common Name                                  |
|----------------------------------------------|
| [**Self-Membership**](r-self-membership.md) |



## Windows Server 2003 Property Sets

This class contains the following property sets for Windows Server 2003:



| Common Name                                      |
|--------------------------------------------------|
| [**Email-Information**](r-email-information.md) |



## ADAM

-   [Attributes](#adam-attributes)
-   [Validated Writes](#adam-validated-writes)
-   [Property Sets](#adam-property-sets)



| Entry | Value |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------|
| System-Only                 | False                                                                                                                |
| Object-Category             | 1                                                                                                                    |
| Default-Object-Category     | \-                                                                                                                   |
| Governs-Id                  | 1.2.840.113556.1.5.8                                                                                                 |
| Default-Hiding-Value        | 0                                                                                                                    |
| Rdn-Att-Id                  | [**Common-Name**](a-cn.md)<br/>                                                                               |
| Subclass of                 | [**Top**](c-top.md)<br/>                                                                                      |
| Possible Superiors          | [**Domain-DNS**](c-domaindns.md)[**Organizational-Unit**](c-organizationalunit.md)[**Container**](c-container.md) |
| Auxiliary Classes           | [**Security-Principal**](c-securityprincipal.md) (System)                                                           |
| NT-Security-Descriptor      | O:BAG:BAD:S:                                                                                                         |
| Default Security Descriptor | D:S:                                                                                                                 |
| System-Flags                | 0x00000010                                                                                                           |



## ADAM Attributes

This class contains the following attributes for ADAM:



| Attribute                                                                   | Mandatory | Derived from                                                                                 |
|-----------------------------------------------------------------------------|-----------|----------------------------------------------------------------------------------------------|
| [**Admin-Description**](a-admindescription.md)                             | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Admin-Display-Name**](a-admindisplayname.md)                            | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Allowed-Attributes**](a-allowedattributes.md)                           | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Allowed-Attributes-Effective**](a-allowedattributeseffective.md)        | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Allowed-Child-Classes**](a-allowedchildclasses.md)                      | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Allowed-Child-Classes-Effective**](a-allowedchildclasseseffective.md)   | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Bridgehead-Server-List-BL**](a-bridgeheadserverlistbl.md)               | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Canonical-Name**](a-canonicalname.md)                                   | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Common-Name**](a-cn.md)                                                 | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Create-Time-Stamp**](a-createtimestamp.md)                              | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Description**](a-description.md)                                        | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Desktop-Profile**](a-desktopprofile.md)                                 | False     | **Group**                                                                                    |
| [**Display-Name**](a-displayname.md)                                       | False     | [**Top**](c-top.md)<br/>                                                              |
| [**DSA-Signature**](a-dsasignature.md)                                     | False     | [**Top**](c-top.md)<br/>                                                              |
| [**DS-Core-Propagation-Data**](a-dscorepropagationdata.md)                 | False     | [**Top**](c-top.md)<br/>                                                              |
| [**From-Entry**](a-fromentry.md)                                           | False     | [**Top**](c-top.md)<br/>                                                              |
| [**FSMO-Role-Owner**](a-fsmoroleowner.md)                                  | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Group-Type**](a-grouptype.md)                                           | True      | **Group**                                                                                    |
| [**Instance-Type**](a-instancetype.md)                                     | True      | [**Top**](c-top.md)<br/>                                                              |
| [**Is-Critical-System-Object**](a-iscriticalsystemobject.md)               | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Is-Deleted**](a-isdeleted.md)                                           | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Is-Member-Of-DL**](a-memberof.md)                                       | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Last-Known-Parent**](a-lastknownparent.md)                              | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Managed-By**](a-managedby.md)                                           | False     | **Group**                                                                                    |
| [**Managed-Objects**](a-managedobjects.md)                                 | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Mastered-By**](a-masteredby.md)                                         | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Member**](a-member.md)                                                  | False     | **Group**                                                                                    |
| [**Modify-Time-Stamp**](a-modifytimestamp.md)                              | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-DS-Approx-Immed-Subordinates**](a-msds-approx-immed-subordinates.md) | False     | [**Top**](c-top.md)<br/>                                                              |
| [**MS-DS-Consistency-Child-Count**](a-ms-ds-consistencychildcount.md)      | False     | [**Top**](c-top.md)<br/>                                                              |
| [**MS-DS-Consistency-Guid**](a-ms-ds-consistencyguid.md)                   | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-DS-Disable-For-Instances-BL**](a-msds-disableforinstancesbl.md)      | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-DS-Mastered-By**](a-msds-masteredby.md)                              | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-DS-NC-Repl-Cursors**](a-msds-ncreplcursors.md)                       | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-DS-NC-Repl-Inbound-Neighbors**](a-msds-ncreplinboundneighbors.md)    | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-DS-NC-Repl-Outbound-Neighbors**](a-msds-ncreploutboundneighbors.md)  | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-DS-Repl-Attribute-Meta-Data**](a-msds-replattributemetadata.md)      | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-DS-Repl-Value-Meta-Data**](a-msds-replvaluemetadata.md)              | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-DS-Service-Account-BL**](a-msds-serviceaccountbl.md)                 | False     | [**Top**](c-top.md)<br/>                                                              |
| [**NT-Security-Descriptor**](a-ntsecuritydescriptor.md)                    | True      | [**Top**](c-top.md)<br/> [**Security-Principal**](c-securityprincipal.md)<br/> |
| [**Obj-Dist-Name**](a-distinguishedname.md)                                | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Object-Category**](a-objectcategory.md)                                 | True      | [**Top**](c-top.md)<br/>                                                              |
| [**Object-Class**](a-objectclass.md)                                       | True      | [**Top**](c-top.md)<br/>                                                              |
| [**Object-Guid**](a-objectguid.md)                                         | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Object-Sid**](a-objectsid.md)                                           | True      | [**Security-Principal**](c-securityprincipal.md)<br/>                                 |
| [**Object-Version**](a-objectversion.md)                                   | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Other-Well-Known-Objects**](a-otherwellknownobjects.md)                 | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Partial-Attribute-Deletion-List**](a-partialattributedeletionlist.md)   | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Partial-Attribute-Set**](a-partialattributeset.md)                      | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Possible-Inferiors**](a-possibleinferiors.md)                           | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Primary-Group-Token**](a-primarygrouptoken.md)                          | False     | **Group**                                                                                    |
| [**Proxied-Object-Name**](a-proxiedobjectname.md)                          | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Proxy-Addresses**](a-proxyaddresses.md)                                 | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Query-Policy-BL**](a-querypolicybl.md)                                  | False     | [**Top**](c-top.md)<br/>                                                              |
| [**RDN**](a-name.md)                                                       | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Repl-Property-Meta-Data**](a-replpropertymetadata.md)                   | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Repl-UpToDate-Vector**](a-repluptodatevector.md)                        | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Reps-From**](a-repsfrom.md)                                             | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Reps-To**](a-repsto.md)                                                 | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Revision**](a-revision.md)                                              | False     | [**Top**](c-top.md)<br/>                                                              |
| [**SD-Rights-Effective**](a-sdrightseffective.md)                          | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Server-Reference-BL**](a-serverreferencebl.md)                          | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Show-In-Advanced-View-Only**](a-showinadvancedviewonly.md)              | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Site-Object-BL**](a-siteobjectbl.md)                                    | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Structural-Object-Class**](a-structuralobjectclass.md)                  | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Sub-Refs**](a-subrefs.md)                                               | False     | [**Top**](c-top.md)<br/>                                                              |
| [**SubSchemaSubEntry**](a-subschemasubentry.md)                            | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Supplemental-Credentials**](a-supplementalcredentials.md)               | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                 |
| [**System-Flags**](a-systemflags.md)                                       | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Token-Groups**](a-tokengroups.md)                                       | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                 |
| [**USN-Changed**](a-usnchanged.md)                                         | False     | [**Top**](c-top.md)<br/>                                                              |
| [**USN-Created**](a-usncreated.md)                                         | False     | [**Top**](c-top.md)<br/>                                                              |
| [**USN-DSA-Last-Obj-Removed**](a-usndsalastobjremoved.md)                  | False     | [**Top**](c-top.md)<br/>                                                              |
| [**USN-Intersite**](a-usnintersite.md)                                     | False     | [**Top**](c-top.md)<br/>                                                              |
| [**USN-Last-Obj-Rem**](a-usnlastobjrem.md)                                 | False     | [**Top**](c-top.md)<br/>                                                              |
| [**USN-Source**](a-usnsource.md)                                           | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Wbem-Path**](a-wbempath.md)                                             | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Well-Known-Objects**](a-wellknownobjects.md)                            | False     | [**Top**](c-top.md)<br/>                                                              |
| [**When-Changed**](a-whenchanged.md)                                       | False     | [**Top**](c-top.md)<br/>                                                              |
| [**When-Created**](a-whencreated.md)                                       | False     | [**Top**](c-top.md)<br/>                                                              |
| [**WWW-Home-Page**](a-wwwhomepage.md)                                      | False     | [**Top**](c-top.md)<br/>                                                              |
| [**WWW-Page-Other**](a-url.md)                                             | False     | [**Top**](c-top.md)<br/>                                                              |



## ADAM Validated Writes

This class contains the following validated writes for ADAM:



| Common Name                                  |
|----------------------------------------------|
| [**Self-Membership**](r-self-membership.md) |



## ADAM Property Sets

This class contains the following property sets for ADAM:



| Common Name                                      |
|--------------------------------------------------|
| [**Email-Information**](r-email-information.md) |



## Windows Server 2003 R2

-   [Attributes](#windows-server-2003-r2-attributes)
-   [Extended Rights](#windows-server-2003-r2-extended-rights)
-   [Validated Writes](#windows-server-2003-r2-validated-writes)
-   [Property Sets](#windows-server-2003-r2-property-sets)



| Entry | Value |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| System-Only                 | False                                                                                                                                                                                                                                                                                                            |
| Object-Category             | 1                                                                                                                                                                                                                                                                                                                |
| Default-Object-Category     | \-                                                                                                                                                                                                                                                                                                               |
| Governs-Id                  | 1.2.840.113556.1.5.8                                                                                                                                                                                                                                                                                             |
| Default-Hiding-Value        | 0                                                                                                                                                                                                                                                                                                                |
| Rdn-Att-Id                  | [**Common-Name**](a-cn.md)<br/>                                                                                                                                                                                                                                                                           |
| Subclass of                 | [**Top**](c-top.md)<br/>                                                                                                                                                                                                                                                                                  |
| Possible Superiors          | [**Domain-DNS**](c-domaindns.md)[**Organizational-Unit**](c-organizationalunit.md)[**Builtin-Domain**](c-builtindomain.md)[**Container**](c-container.md)[**ms-DS-Az-Admin-Manager**](c-msds-azadminmanager.md)[**ms-DS-Az-Application**](c-msds-azapplication.md)[**ms-DS-Az-Scope**](c-msds-azscope.md) |
| Auxiliary Classes           | [**posixGroup**](c-posixgroup.md)[**Security-Principal**](c-securityprincipal.md) (System)[**Mail-Recipient**](c-mailrecipient.md) (System)                                                                                                                                                                   |
| NT-Security-Descriptor      | O:BAG:BAD:S:                                                                                                                                                                                                                                                                                                     |
| Default Security Descriptor | D:(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;DA)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;SY)(A;;RPLCLORC;;;AU)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;AO)(A;;RPLCLORC;;;PS)(OA;;CR;ab721a55-1e2f-11d0-9819-00aa0040529b;;AU)(OA;;RP;46a9b11d-60ae-405a-b7e8-ff8a58d456d2;;S-1-5-32-560)                                                   |
| System-Flags                | 0x00000010                                                                                                                                                                                                                                                                                                       |



## Windows Server 2003 R2 Attributes

This class contains the following attributes for Windows Server 2003 R2:



| Attribute                                                                    | Mandatory | Derived from                                                                                                                       |
|------------------------------------------------------------------------------|-----------|------------------------------------------------------------------------------------------------------------------------------------|
| [**Account-Name-History**](a-accountnamehistory.md)                         | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**Admin-Count**](a-admincount.md)                                          | False     | **Group**                                                                                                                          |
| [**Admin-Description**](a-admindescription.md)                              | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Admin-Display-Name**](a-admindisplayname.md)                             | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Allowed-Attributes**](a-allowedattributes.md)                            | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Allowed-Attributes-Effective**](a-allowedattributeseffective.md)         | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Allowed-Child-Classes**](a-allowedchildclasses.md)                       | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Allowed-Child-Classes-Effective**](a-allowedchildclasseseffective.md)    | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Alt-Security-Identities**](a-altsecurityidentities.md)                   | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**Bridgehead-Server-List-BL**](a-bridgeheadserverlistbl.md)                | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Canonical-Name**](a-canonicalname.md)                                    | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Comment**](a-info.md)                                                    | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**Common-Name**](a-cn.md)                                                  | True      | [**Top**](c-top.md)<br/> [**posixGroup**](c-posixgroup.md)<br/> [**Mail-Recipient**](c-mailrecipient.md)<br/> |
| [**Control-Access-Rights**](a-controlaccessrights.md)                       | False     | **Group**                                                                                                                          |
| [**Create-Time-Stamp**](a-createtimestamp.md)                               | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Description**](a-description.md)                                         | False     | [**Top**](c-top.md)<br/> [**posixGroup**](c-posixgroup.md)<br/>                                                      |
| [**Desktop-Profile**](a-desktopprofile.md)                                  | False     | **Group**                                                                                                                          |
| [**Display-Name**](a-displayname.md)                                        | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Display-Name-Printable**](a-displaynameprintable.md)                     | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**DSA-Signature**](a-dsasignature.md)                                      | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**DS-Core-Propagation-Data**](a-dscorepropagationdata.md)                  | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**E-mail-Addresses**](a-mail.md)                                           | False     | **Group**                                                                                                                          |
| [**Extension-Name**](a-extensionname.md)                                    | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Flags**](a-flags.md)                                                     | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**From-Entry**](a-fromentry.md)                                            | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Frs-Computer-Reference-BL**](a-frscomputerreferencebl.md)                | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**FRS-Member-Reference-BL**](a-frsmemberreferencebl.md)                    | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**FSMO-Role-Owner**](a-fsmoroleowner.md)                                   | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Garbage-Coll-Period**](a-garbagecollperiod.md)                           | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**gidNumber**](a-gidnumber.md)                                             | False     | [**posixGroup**](c-posixgroup.md)<br/>                                                                                      |
| [**Group-Attributes**](a-groupattributes.md)                                | False     | **Group**                                                                                                                          |
| [**Group-Membership-SAM**](a-groupmembershipsam.md)                         | False     | **Group**                                                                                                                          |
| [**Group-Type**](a-grouptype.md)                                            | True      | **Group**                                                                                                                          |
| [**Instance-Type**](a-instancetype.md)                                      | True      | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Is-Critical-System-Object**](a-iscriticalsystemobject.md)                | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Is-Deleted**](a-isdeleted.md)                                            | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Is-Member-Of-DL**](a-memberof.md)                                        | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Is-Privilege-Holder**](a-isprivilegeholder.md)                           | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**labeledURI**](a-labeleduri.md)                                           | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**Last-Known-Parent**](a-lastknownparent.md)                               | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Legacy-Exchange-DN**](a-legacyexchangedn.md)                             | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**Managed-By**](a-managedby.md)                                            | False     | **Group**                                                                                                                          |
| [**Managed-Objects**](a-managedobjects.md)                                  | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Mastered-By**](a-masteredby.md)                                          | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Member**](a-member.md)                                                   | False     | **Group**                                                                                                                          |
| [**memberUid**](a-memberuid.md)                                             | False     | [**posixGroup**](c-posixgroup.md)<br/>                                                                                      |
| [**Modify-Time-Stamp**](a-modifytimestamp.md)                               | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-COM-PartitionSetLink**](a-mscom-partitionsetlink.md)                  | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-COM-UserLink**](a-mscom-userlink.md)                                  | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DFSR-ComputerReferenceBL**](a-msdfsr-computerreferencebl.md)          | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DFSR-MemberReferenceBL**](a-msdfsr-memberreferencebl.md)              | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Approx-Immed-Subordinates**](a-msds-approx-immed-subordinates.md)  | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Az-LDAP-Query**](a-msds-azldapquery.md)                            | False     | **Group**                                                                                                                          |
| [**MS-DS-Consistency-Child-Count**](a-ms-ds-consistencychildcount.md)       | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**MS-DS-Consistency-Guid**](a-ms-ds-consistencyguid.md)                    | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-KeyVersionNumber**](a-msds-keyversionnumber.md)                    | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**ms-DS-Mastered-By**](a-msds-masteredby.md)                               | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Members-For-Az-Role-BL**](a-msds-membersforazrolebl.md)            | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-NC-Repl-Cursors**](a-msds-ncreplcursors.md)                        | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-NC-Repl-Inbound-Neighbors**](a-msds-ncreplinboundneighbors.md)     | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-NC-Repl-Outbound-Neighbors**](a-msds-ncreploutboundneighbors.md)   | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Non-Members**](a-msds-nonmembers.md)                               | False     | **Group**                                                                                                                          |
| [**ms-DS-Non-Members-BL**](a-msds-nonmembersbl.md)                          | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Object-Reference-BL**](a-msds-objectreferencebl.md)                | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Operations-For-Az-Role-BL**](a-msds-operationsforazrolebl.md)      | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Operations-For-Az-Task-BL**](a-msds-operationsforaztaskbl.md)      | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Repl-Attribute-Meta-Data**](a-msds-replattributemetadata.md)       | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Repl-Value-Meta-Data**](a-msds-replvaluemetadata.md)               | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Tasks-For-Az-Role-BL**](a-msds-tasksforazrolebl.md)                | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Tasks-For-Az-Task-BL**](a-msds-tasksforaztaskbl.md)                | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-Exch-Assistant-Name**](a-msexchassistantname.md)                      | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**ms-Exch-LabeledURI**](a-msexchlabeleduri.md)                             | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**ms-Exch-Owner-BL**](a-ownerbl.md)                                        | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**msSFU-30-Name**](a-mssfu30name.md)                                       | False     | **Group**                                                                                                                          |
| [**msSFU-30-Nis-Domain**](a-mssfu30nisdomain.md)                            | False     | **Group**                                                                                                                          |
| [**msSFU-30-Posix-Member**](a-mssfu30posixmember.md)                        | False     | **Group**                                                                                                                          |
| [**msSFU-30-Posix-Member-Of**](a-mssfu30posixmemberof.md)                   | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**netboot-SCP-BL**](a-netbootscpbl.md)                                     | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Non-Security-Member**](a-nonsecuritymember.md)                           | False     | **Group**                                                                                                                          |
| [**Non-Security-Member-BL**](a-nonsecuritymemberbl.md)                      | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**NT-Group-Members**](a-ntgroupmembers.md)                                 | False     | **Group**                                                                                                                          |
| [**NT-Security-Descriptor**](a-ntsecuritydescriptor.md)                     | True      | [**Top**](c-top.md)<br/> [**Security-Principal**](c-securityprincipal.md)<br/>                                       |
| [**Obj-Dist-Name**](a-distinguishedname.md)                                 | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Object-Category**](a-objectcategory.md)                                  | True      | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Object-Class**](a-objectclass.md)                                        | True      | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Object-Guid**](a-objectguid.md)                                          | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Object-Sid**](a-objectsid.md)                                            | True      | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**Object-Version**](a-objectversion.md)                                    | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Operator-Count**](a-operatorcount.md)                                    | False     | **Group**                                                                                                                          |
| [**Other-Well-Known-Objects**](a-otherwellknownobjects.md)                  | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Partial-Attribute-Deletion-List**](a-partialattributedeletionlist.md)    | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Partial-Attribute-Set**](a-partialattributeset.md)                       | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Possible-Inferiors**](a-possibleinferiors.md)                            | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Primary-Group-Token**](a-primarygrouptoken.md)                           | False     | **Group**                                                                                                                          |
| [**Proxied-Object-Name**](a-proxiedobjectname.md)                           | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Proxy-Addresses**](a-proxyaddresses.md)                                  | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Query-Policy-BL**](a-querypolicybl.md)                                   | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**RDN**](a-name.md)                                                        | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Repl-Property-Meta-Data**](a-replpropertymetadata.md)                    | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Repl-UpToDate-Vector**](a-repluptodatevector.md)                         | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Reports**](a-directreports.md)                                           | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Reps-From**](a-repsfrom.md)                                              | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Reps-To**](a-repsto.md)                                                  | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Revision**](a-revision.md)                                               | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Rid**](a-rid.md)                                                         | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**SAM-Account-Name**](a-samaccountname.md)                                 | True      | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**SAM-Account-Type**](a-samaccounttype.md)                                 | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**SD-Rights-Effective**](a-sdrightseffective.md)                           | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**secretary**](a-secretary.md)                                             | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**Security-Identifier**](a-securityidentifier.md)                          | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**Server-Reference-BL**](a-serverreferencebl.md)                           | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Show-In-Address-Book**](a-showinaddressbook.md)                          | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**Show-In-Advanced-View-Only**](a-showinadvancedviewonly.md)               | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**SID-History**](a-sidhistory.md)                                          | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**Site-Object-BL**](a-siteobjectbl.md)                                     | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Structural-Object-Class**](a-structuralobjectclass.md)                   | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Sub-Refs**](a-subrefs.md)                                                | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**SubSchemaSubEntry**](a-subschemasubentry.md)                             | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Supplemental-Credentials**](a-supplementalcredentials.md)                | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**System-Flags**](a-systemflags.md)                                        | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Telephone-Number**](a-telephonenumber.md)                                | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**Text-Encoded-OR-Address**](a-textencodedoraddress.md)                    | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**Token-Groups**](a-tokengroups.md)                                        | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**Token-Groups-Global-And-Universal**](a-tokengroupsglobalanduniversal.md) | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**Token-Groups-No-GC-Acceptable**](a-tokengroupsnogcacceptable.md)         | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**unixUserPassword**](a-unixuserpassword.md)                               | False     | [**posixGroup**](c-posixgroup.md)<br/>                                                                                      |
| [**User-Cert**](a-usercert.md)                                              | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**User-Password**](a-userpassword.md)                                      | False     | [**posixGroup**](c-posixgroup.md)<br/>                                                                                      |
| [**User-SMIME-Certificate**](a-usersmimecertificate.md)                     | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**USN-Changed**](a-usnchanged.md)                                          | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**USN-Created**](a-usncreated.md)                                          | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**USN-DSA-Last-Obj-Removed**](a-usndsalastobjremoved.md)                   | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**USN-Intersite**](a-usnintersite.md)                                      | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**USN-Last-Obj-Rem**](a-usnlastobjrem.md)                                  | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**USN-Source**](a-usnsource.md)                                            | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Wbem-Path**](a-wbempath.md)                                              | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Well-Known-Objects**](a-wellknownobjects.md)                             | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**When-Changed**](a-whenchanged.md)                                        | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**When-Created**](a-whencreated.md)                                        | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**WWW-Home-Page**](a-wwwhomepage.md)                                       | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**WWW-Page-Other**](a-url.md)                                              | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**X509-Cert**](a-usercertificate.md)                                       | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |



## Windows Server 2003 R2 Extended Rights

This class contains the following extended rights for Windows Server 2003 R2:



| Common Name                  |
|------------------------------|
| [**Send-To**](r-send-to.md) |



## Windows Server 2003 R2 Validated Writes

This class contains the following validated writes for Windows Server 2003 R2:



| Common Name                                  |
|----------------------------------------------|
| [**Self-Membership**](r-self-membership.md) |



## Windows Server 2003 R2 Property Sets

This class contains the following property sets for Windows Server 2003 R2:



| Common Name                                      |
|--------------------------------------------------|
| [**Email-Information**](r-email-information.md) |



## Windows Server 2008

-   [Attributes](#windows-server-2008-attributes)
-   [Extended Rights](#windows-server-2008-extended-rights)
-   [Validated Writes](#windows-server-2008-validated-writes)
-   [Property Sets](#windows-server-2008-property-sets)



| Entry | Value |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| System-Only                 | False                                                                                                                                                                                                                                                                                                            |
| Object-Category             | 1                                                                                                                                                                                                                                                                                                                |
| Default-Object-Category     | \-                                                                                                                                                                                                                                                                                                               |
| Governs-Id                  | 1.2.840.113556.1.5.8                                                                                                                                                                                                                                                                                             |
| Default-Hiding-Value        | 0                                                                                                                                                                                                                                                                                                                |
| Rdn-Att-Id                  | [**Common-Name**](a-cn.md)<br/>                                                                                                                                                                                                                                                                           |
| Subclass of                 | [**Top**](c-top.md)<br/>                                                                                                                                                                                                                                                                                  |
| Possible Superiors          | [**Domain-DNS**](c-domaindns.md)[**Organizational-Unit**](c-organizationalunit.md)[**Builtin-Domain**](c-builtindomain.md)[**Container**](c-container.md)[**ms-DS-Az-Admin-Manager**](c-msds-azadminmanager.md)[**ms-DS-Az-Application**](c-msds-azapplication.md)[**ms-DS-Az-Scope**](c-msds-azscope.md) |
| Auxiliary Classes           | [**posixGroup**](c-posixgroup.md)[**Security-Principal**](c-securityprincipal.md) (System)[**Mail-Recipient**](c-mailrecipient.md) (System)                                                                                                                                                                   |
| NT-Security-Descriptor      | O:BAG:BAD:S:                                                                                                                                                                                                                                                                                                     |
| Default Security Descriptor | D:(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;DA)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;SY)(A;;RPLCLORC;;;AU)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;AO)(A;;RPLCLORC;;;PS)(OA;;CR;ab721a55-1e2f-11d0-9819-00aa0040529b;;AU)(OA;;RP;46a9b11d-60ae-405a-b7e8-ff8a58d456d2;;S-1-5-32-560)                                                   |
| System-Flags                | 0x00000010                                                                                                                                                                                                                                                                                                       |



## Windows Server 2008 Attributes

This class contains the following attributes for Windows Server 2008:



| Attribute                                                                        | Mandatory | Derived from                                                                                                                       |
|----------------------------------------------------------------------------------|-----------|------------------------------------------------------------------------------------------------------------------------------------|
| [**Account-Name-History**](a-accountnamehistory.md)                             | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**Admin-Count**](a-admincount.md)                                              | False     | **Group**                                                                                                                          |
| [**Admin-Description**](a-admindescription.md)                                  | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Admin-Display-Name**](a-admindisplayname.md)                                 | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Allowed-Attributes**](a-allowedattributes.md)                                | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Allowed-Attributes-Effective**](a-allowedattributeseffective.md)             | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Allowed-Child-Classes**](a-allowedchildclasses.md)                           | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Allowed-Child-Classes-Effective**](a-allowedchildclasseseffective.md)        | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Alt-Security-Identities**](a-altsecurityidentities.md)                       | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**Bridgehead-Server-List-BL**](a-bridgeheadserverlistbl.md)                    | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Canonical-Name**](a-canonicalname.md)                                        | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Comment**](a-info.md)                                                        | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**Common-Name**](a-cn.md)                                                      | True      | [**Top**](c-top.md)<br/> [**posixGroup**](c-posixgroup.md)<br/> [**Mail-Recipient**](c-mailrecipient.md)<br/> |
| [**Control-Access-Rights**](a-controlaccessrights.md)                           | False     | **Group**                                                                                                                          |
| [**Create-Time-Stamp**](a-createtimestamp.md)                                   | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Description**](a-description.md)                                             | False     | [**Top**](c-top.md)<br/> [**posixGroup**](c-posixgroup.md)<br/>                                                      |
| [**Desktop-Profile**](a-desktopprofile.md)                                      | False     | **Group**                                                                                                                          |
| [**Display-Name**](a-displayname.md)                                            | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Display-Name-Printable**](a-displaynameprintable.md)                         | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**DSA-Signature**](a-dsasignature.md)                                          | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**DS-Core-Propagation-Data**](a-dscorepropagationdata.md)                      | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**E-mail-Addresses**](a-mail.md)                                               | False     | **Group**                                                                                                                          |
| [**Extension-Name**](a-extensionname.md)                                        | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Flags**](a-flags.md)                                                         | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**From-Entry**](a-fromentry.md)                                                | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Frs-Computer-Reference-BL**](a-frscomputerreferencebl.md)                    | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**FRS-Member-Reference-BL**](a-frsmemberreferencebl.md)                        | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**FSMO-Role-Owner**](a-fsmoroleowner.md)                                       | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Garbage-Coll-Period**](a-garbagecollperiod.md)                               | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**gidNumber**](a-gidnumber.md)                                                 | False     | [**posixGroup**](c-posixgroup.md)<br/>                                                                                      |
| [**Group-Attributes**](a-groupattributes.md)                                    | False     | **Group**                                                                                                                          |
| [**Group-Membership-SAM**](a-groupmembershipsam.md)                             | False     | **Group**                                                                                                                          |
| [**Group-Type**](a-grouptype.md)                                                | True      | **Group**                                                                                                                          |
| [**Instance-Type**](a-instancetype.md)                                          | True      | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Is-Critical-System-Object**](a-iscriticalsystemobject.md)                    | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Is-Deleted**](a-isdeleted.md)                                                | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Is-Member-Of-DL**](a-memberof.md)                                            | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Is-Privilege-Holder**](a-isprivilegeholder.md)                               | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**labeledURI**](a-labeleduri.md)                                               | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**Last-Known-Parent**](a-lastknownparent.md)                                   | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Legacy-Exchange-DN**](a-legacyexchangedn.md)                                 | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**Managed-By**](a-managedby.md)                                                | False     | **Group**                                                                                                                          |
| [**Managed-Objects**](a-managedobjects.md)                                      | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Mastered-By**](a-masteredby.md)                                              | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Member**](a-member.md)                                                       | False     | **Group**                                                                                                                          |
| [**memberUid**](a-memberuid.md)                                                 | False     | [**posixGroup**](c-posixgroup.md)<br/>                                                                                      |
| [**Modify-Time-Stamp**](a-modifytimestamp.md)                                   | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-COM-PartitionSetLink**](a-mscom-partitionsetlink.md)                      | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-COM-UserLink**](a-mscom-userlink.md)                                      | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DFSR-ComputerReferenceBL**](a-msdfsr-computerreferencebl.md)              | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DFSR-MemberReferenceBL**](a-msdfsr-memberreferencebl.md)                  | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Approx-Immed-Subordinates**](a-msds-approx-immed-subordinates.md)      | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-AuthenticatedTo-Accountlist**](a-msds-authenticatedtoaccountlist.md)   | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Az-Application-Data**](a-msds-azapplicationdata.md)                    | False     | **Group**                                                                                                                          |
| [**ms-DS-Az-Biz-Rule**](a-msds-azbizrule.md)                                    | False     | **Group**                                                                                                                          |
| [**ms-DS-Az-Biz-Rule-Language**](a-msds-azbizrulelanguage.md)                   | False     | **Group**                                                                                                                          |
| [**ms-DS-Az-Generic-Data**](a-msds-azgenericdata.md)                            | False     | **Group**                                                                                                                          |
| [**ms-DS-Az-Last-Imported-Biz-Rule-Path**](a-msds-azlastimportedbizrulepath.md) | False     | **Group**                                                                                                                          |
| [**ms-DS-Az-LDAP-Query**](a-msds-azldapquery.md)                                | False     | **Group**                                                                                                                          |
| [**ms-DS-Az-Object-Guid**](a-msds-azobjectguid.md)                              | False     | **Group**                                                                                                                          |
| [**MS-DS-Consistency-Child-Count**](a-ms-ds-consistencychildcount.md)           | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**MS-DS-Consistency-Guid**](a-ms-ds-consistencyguid.md)                        | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Is-Domain-For**](a-msds-isdomainfor.md)                                | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Is-Full-Replica-For**](a-msds-isfullreplicafor.md)                     | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Is-Partial-Replica-For**](a-msds-ispartialreplicafor.md)               | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-KeyVersionNumber**](a-msds-keyversionnumber.md)                        | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**ms-DS-KrbTgt-Link-BL**](a-msds-krbtgtlinkbl.md)                              | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Mastered-By**](a-msds-masteredby.md)                                   | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Members-For-Az-Role-BL**](a-msds-membersforazrolebl.md)                | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-NC-Repl-Cursors**](a-msds-ncreplcursors.md)                            | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-NC-Repl-Inbound-Neighbors**](a-msds-ncreplinboundneighbors.md)         | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-NC-Repl-Outbound-Neighbors**](a-msds-ncreploutboundneighbors.md)       | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-NC-RO-Replica-Locations-BL**](a-msds-nc-ro-replica-locations-bl.md)    | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-NC-Type**](a-msds-nctype.md)                                           | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Non-Members**](a-msds-nonmembers.md)                                   | False     | **Group**                                                                                                                          |
| [**ms-DS-Non-Members-BL**](a-msds-nonmembersbl.md)                              | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Object-Reference-BL**](a-msds-objectreferencebl.md)                    | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Operations-For-Az-Role-BL**](a-msds-operationsforazrolebl.md)          | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Operations-For-Az-Task-BL**](a-msds-operationsforaztaskbl.md)          | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Phonetic-Display-Name**](a-msds-phoneticdisplayname.md)                | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**ms-DS-Principal-Name**](a-msds-principalname.md)                             | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-PSO-Applied**](a-msds-psoapplied.md)                                   | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Repl-Attribute-Meta-Data**](a-msds-replattributemetadata.md)           | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Repl-Value-Meta-Data**](a-msds-replvaluemetadata.md)                   | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Revealed-DSAs**](a-msds-revealeddsas.md)                               | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Revealed-List-BL**](a-msds-revealedlistbl.md)                          | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Tasks-For-Az-Role-BL**](a-msds-tasksforazrolebl.md)                    | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Tasks-For-Az-Task-BL**](a-msds-tasksforaztaskbl.md)                    | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-Exch-Assistant-Name**](a-msexchassistantname.md)                          | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**ms-Exch-LabeledURI**](a-msexchlabeleduri.md)                                 | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**ms-Exch-Owner-BL**](a-ownerbl.md)                                            | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**msSFU-30-Name**](a-mssfu30name.md)                                           | False     | **Group**                                                                                                                          |
| [**msSFU-30-Nis-Domain**](a-mssfu30nisdomain.md)                                | False     | **Group**                                                                                                                          |
| [**msSFU-30-Posix-Member**](a-mssfu30posixmember.md)                            | False     | **Group**                                                                                                                          |
| [**msSFU-30-Posix-Member-Of**](a-mssfu30posixmemberof.md)                       | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**netboot-SCP-BL**](a-netbootscpbl.md)                                         | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Non-Security-Member**](a-nonsecuritymember.md)                               | False     | **Group**                                                                                                                          |
| [**Non-Security-Member-BL**](a-nonsecuritymemberbl.md)                          | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**NT-Group-Members**](a-ntgroupmembers.md)                                     | False     | **Group**                                                                                                                          |
| [**NT-Security-Descriptor**](a-ntsecuritydescriptor.md)                         | True      | [**Top**](c-top.md)<br/> [**Security-Principal**](c-securityprincipal.md)<br/>                                       |
| [**Obj-Dist-Name**](a-distinguishedname.md)                                     | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Object-Category**](a-objectcategory.md)                                      | True      | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Object-Class**](a-objectclass.md)                                            | True      | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Object-Guid**](a-objectguid.md)                                              | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Object-Sid**](a-objectsid.md)                                                | True      | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**Object-Version**](a-objectversion.md)                                        | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Operator-Count**](a-operatorcount.md)                                        | False     | **Group**                                                                                                                          |
| [**Other-Well-Known-Objects**](a-otherwellknownobjects.md)                      | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Partial-Attribute-Deletion-List**](a-partialattributedeletionlist.md)        | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Partial-Attribute-Set**](a-partialattributeset.md)                           | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Possible-Inferiors**](a-possibleinferiors.md)                                | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Primary-Group-Token**](a-primarygrouptoken.md)                               | False     | **Group**                                                                                                                          |
| [**Proxied-Object-Name**](a-proxiedobjectname.md)                               | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Proxy-Addresses**](a-proxyaddresses.md)                                      | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Query-Policy-BL**](a-querypolicybl.md)                                       | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**RDN**](a-name.md)                                                            | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Repl-Property-Meta-Data**](a-replpropertymetadata.md)                        | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Repl-UpToDate-Vector**](a-repluptodatevector.md)                             | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Reports**](a-directreports.md)                                               | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Reps-From**](a-repsfrom.md)                                                  | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Reps-To**](a-repsto.md)                                                      | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Revision**](a-revision.md)                                                   | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Rid**](a-rid.md)                                                             | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**SAM-Account-Name**](a-samaccountname.md)                                     | True      | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**SAM-Account-Type**](a-samaccounttype.md)                                     | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**SD-Rights-Effective**](a-sdrightseffective.md)                               | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**secretary**](a-secretary.md)                                                 | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**Security-Identifier**](a-securityidentifier.md)                              | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**Server-Reference-BL**](a-serverreferencebl.md)                               | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Show-In-Address-Book**](a-showinaddressbook.md)                              | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**Show-In-Advanced-View-Only**](a-showinadvancedviewonly.md)                   | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**SID-History**](a-sidhistory.md)                                              | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**Site-Object-BL**](a-siteobjectbl.md)                                         | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Structural-Object-Class**](a-structuralobjectclass.md)                       | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Sub-Refs**](a-subrefs.md)                                                    | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**SubSchemaSubEntry**](a-subschemasubentry.md)                                 | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Supplemental-Credentials**](a-supplementalcredentials.md)                    | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**System-Flags**](a-systemflags.md)                                            | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Telephone-Number**](a-telephonenumber.md)                                    | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**Text-Encoded-OR-Address**](a-textencodedoraddress.md)                        | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**Token-Groups**](a-tokengroups.md)                                            | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**Token-Groups-Global-And-Universal**](a-tokengroupsglobalanduniversal.md)     | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**Token-Groups-No-GC-Acceptable**](a-tokengroupsnogcacceptable.md)             | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**unixUserPassword**](a-unixuserpassword.md)                                   | False     | [**posixGroup**](c-posixgroup.md)<br/>                                                                                      |
| [**User-Cert**](a-usercert.md)                                                  | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**User-Password**](a-userpassword.md)                                          | False     | [**posixGroup**](c-posixgroup.md)<br/>                                                                                      |
| [**User-SMIME-Certificate**](a-usersmimecertificate.md)                         | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**USN-Changed**](a-usnchanged.md)                                              | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**USN-Created**](a-usncreated.md)                                              | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**USN-DSA-Last-Obj-Removed**](a-usndsalastobjremoved.md)                       | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**USN-Intersite**](a-usnintersite.md)                                          | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**USN-Last-Obj-Rem**](a-usnlastobjrem.md)                                      | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**USN-Source**](a-usnsource.md)                                                | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Wbem-Path**](a-wbempath.md)                                                  | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Well-Known-Objects**](a-wellknownobjects.md)                                 | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**When-Changed**](a-whenchanged.md)                                            | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**When-Created**](a-whencreated.md)                                            | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**WWW-Home-Page**](a-wwwhomepage.md)                                           | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**WWW-Page-Other**](a-url.md)                                                  | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**X509-Cert**](a-usercertificate.md)                                           | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |



## Windows Server 2008 Extended Rights

This class contains the following extended rights for Windows Server 2008:



| Common Name                  |
|------------------------------|
| [**Send-To**](r-send-to.md) |



## Windows Server 2008 Validated Writes

This class contains the following validated writes for Windows Server 2008:



| Common Name                                  |
|----------------------------------------------|
| [**Self-Membership**](r-self-membership.md) |



## Windows Server 2008 Property Sets

This class contains the following property sets for Windows Server 2008:



| Common Name                                      |
|--------------------------------------------------|
| [**Email-Information**](r-email-information.md) |



## Windows Server 2008 R2

-   [Attributes](#windows-server-2008-r2-attributes)
-   [Extended Rights](#windows-server-2008-r2-extended-rights)
-   [Validated Writes](#windows-server-2008-r2-validated-writes)
-   [Property Sets](#windows-server-2008-r2-property-sets)



| Entry | Value |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| System-Only                 | False                                                                                                                                                                                                                                                                                                            |
| Object-Category             | 1                                                                                                                                                                                                                                                                                                                |
| Default-Object-Category     | \-                                                                                                                                                                                                                                                                                                               |
| Governs-Id                  | 1.2.840.113556.1.5.8                                                                                                                                                                                                                                                                                             |
| Default-Hiding-Value        | 0                                                                                                                                                                                                                                                                                                                |
| Rdn-Att-Id                  | [**Common-Name**](a-cn.md)<br/>                                                                                                                                                                                                                                                                           |
| Subclass of                 | [**Top**](c-top.md)<br/>                                                                                                                                                                                                                                                                                  |
| Possible Superiors          | [**Domain-DNS**](c-domaindns.md)[**Organizational-Unit**](c-organizationalunit.md)[**Builtin-Domain**](c-builtindomain.md)[**Container**](c-container.md)[**ms-DS-Az-Admin-Manager**](c-msds-azadminmanager.md)[**ms-DS-Az-Application**](c-msds-azapplication.md)[**ms-DS-Az-Scope**](c-msds-azscope.md) |
| Auxiliary Classes           | [**posixGroup**](c-posixgroup.md)[**Security-Principal**](c-securityprincipal.md) (System)[**Mail-Recipient**](c-mailrecipient.md) (System)                                                                                                                                                                   |
| NT-Security-Descriptor      | O:BAG:BAD:S:                                                                                                                                                                                                                                                                                                     |
| Default Security Descriptor | D:(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;DA)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;SY)(A;;RPLCLORC;;;AU)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;AO)(A;;RPLCLORC;;;PS)(OA;;CR;ab721a55-1e2f-11d0-9819-00aa0040529b;;AU)(OA;;RP;46a9b11d-60ae-405a-b7e8-ff8a58d456d2;;S-1-5-32-560)                                                   |
| System-Flags                | 0x00000010                                                                                                                                                                                                                                                                                                       |



## Windows Server 2008 R2 Attributes

This class contains the following attributes for Windows Server 2008 R2:



| Attribute                                                                        | Mandatory | Derived from                                                                                                                       |
|----------------------------------------------------------------------------------|-----------|------------------------------------------------------------------------------------------------------------------------------------|
| [**Account-Name-History**](a-accountnamehistory.md)                             | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**Admin-Count**](a-admincount.md)                                              | False     | **Group**                                                                                                                          |
| [**Admin-Description**](a-admindescription.md)                                  | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Admin-Display-Name**](a-admindisplayname.md)                                 | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Allowed-Attributes**](a-allowedattributes.md)                                | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Allowed-Attributes-Effective**](a-allowedattributeseffective.md)             | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Allowed-Child-Classes**](a-allowedchildclasses.md)                           | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Allowed-Child-Classes-Effective**](a-allowedchildclasseseffective.md)        | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Alt-Security-Identities**](a-altsecurityidentities.md)                       | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**Bridgehead-Server-List-BL**](a-bridgeheadserverlistbl.md)                    | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Canonical-Name**](a-canonicalname.md)                                        | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Comment**](a-info.md)                                                        | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**Common-Name**](a-cn.md)                                                      | True      | [**Top**](c-top.md)<br/> [**posixGroup**](c-posixgroup.md)<br/> [**Mail-Recipient**](c-mailrecipient.md)<br/> |
| [**Control-Access-Rights**](a-controlaccessrights.md)                           | False     | **Group**                                                                                                                          |
| [**Create-Time-Stamp**](a-createtimestamp.md)                                   | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Description**](a-description.md)                                             | False     | [**Top**](c-top.md)<br/> [**posixGroup**](c-posixgroup.md)<br/>                                                      |
| [**Desktop-Profile**](a-desktopprofile.md)                                      | False     | **Group**                                                                                                                          |
| [**Display-Name**](a-displayname.md)                                            | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Display-Name-Printable**](a-displaynameprintable.md)                         | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**DSA-Signature**](a-dsasignature.md)                                          | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**DS-Core-Propagation-Data**](a-dscorepropagationdata.md)                      | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**E-mail-Addresses**](a-mail.md)                                               | False     | **Group**                                                                                                                          |
| [**Extension-Name**](a-extensionname.md)                                        | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Flags**](a-flags.md)                                                         | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**From-Entry**](a-fromentry.md)                                                | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Frs-Computer-Reference-BL**](a-frscomputerreferencebl.md)                    | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**FRS-Member-Reference-BL**](a-frsmemberreferencebl.md)                        | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**FSMO-Role-Owner**](a-fsmoroleowner.md)                                       | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Garbage-Coll-Period**](a-garbagecollperiod.md)                               | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**gidNumber**](a-gidnumber.md)                                                 | False     | [**posixGroup**](c-posixgroup.md)<br/>                                                                                      |
| [**Group-Attributes**](a-groupattributes.md)                                    | False     | **Group**                                                                                                                          |
| [**Group-Membership-SAM**](a-groupmembershipsam.md)                             | False     | **Group**                                                                                                                          |
| [**Group-Type**](a-grouptype.md)                                                | True      | **Group**                                                                                                                          |
| [**Instance-Type**](a-instancetype.md)                                          | True      | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Is-Critical-System-Object**](a-iscriticalsystemobject.md)                    | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Is-Deleted**](a-isdeleted.md)                                                | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Is-Member-Of-DL**](a-memberof.md)                                            | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Is-Privilege-Holder**](a-isprivilegeholder.md)                               | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Is-Recycled**](a-isrecycled.md)                                              | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**labeledURI**](a-labeleduri.md)                                               | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**Last-Known-Parent**](a-lastknownparent.md)                                   | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Legacy-Exchange-DN**](a-legacyexchangedn.md)                                 | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**Managed-By**](a-managedby.md)                                                | False     | **Group**                                                                                                                          |
| [**Managed-Objects**](a-managedobjects.md)                                      | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Mastered-By**](a-masteredby.md)                                              | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Member**](a-member.md)                                                       | False     | **Group**                                                                                                                          |
| [**memberUid**](a-memberuid.md)                                                 | False     | [**posixGroup**](c-posixgroup.md)<br/>                                                                                      |
| [**Modify-Time-Stamp**](a-modifytimestamp.md)                                   | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-COM-PartitionSetLink**](a-mscom-partitionsetlink.md)                      | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-COM-UserLink**](a-mscom-userlink.md)                                      | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DFSR-ComputerReferenceBL**](a-msdfsr-computerreferencebl.md)              | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DFSR-MemberReferenceBL**](a-msdfsr-memberreferencebl.md)                  | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Approx-Immed-Subordinates**](a-msds-approx-immed-subordinates.md)      | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-AuthenticatedTo-Accountlist**](a-msds-authenticatedtoaccountlist.md)   | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Az-Application-Data**](a-msds-azapplicationdata.md)                    | False     | **Group**                                                                                                                          |
| [**ms-DS-Az-Biz-Rule**](a-msds-azbizrule.md)                                    | False     | **Group**                                                                                                                          |
| [**ms-DS-Az-Biz-Rule-Language**](a-msds-azbizrulelanguage.md)                   | False     | **Group**                                                                                                                          |
| [**ms-DS-Az-Generic-Data**](a-msds-azgenericdata.md)                            | False     | **Group**                                                                                                                          |
| [**ms-DS-Az-Last-Imported-Biz-Rule-Path**](a-msds-azlastimportedbizrulepath.md) | False     | **Group**                                                                                                                          |
| [**ms-DS-Az-LDAP-Query**](a-msds-azldapquery.md)                                | False     | **Group**                                                                                                                          |
| [**ms-DS-Az-Object-Guid**](a-msds-azobjectguid.md)                              | False     | **Group**                                                                                                                          |
| [**MS-DS-Consistency-Child-Count**](a-ms-ds-consistencychildcount.md)           | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**MS-DS-Consistency-Guid**](a-ms-ds-consistencyguid.md)                        | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Enabled-Feature-BL**](a-msds-enabledfeaturebl.md)                      | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Host-Service-Account-BL**](a-msds-hostserviceaccountbl.md)             | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Is-Domain-For**](a-msds-isdomainfor.md)                                | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Is-Full-Replica-For**](a-msds-isfullreplicafor.md)                     | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Is-Partial-Replica-For**](a-msds-ispartialreplicafor.md)               | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-KeyVersionNumber**](a-msds-keyversionnumber.md)                        | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**ms-DS-KrbTgt-Link-BL**](a-msds-krbtgtlinkbl.md)                              | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Last-Known-RDN**](a-msds-lastknownrdn.md)                              | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-local-Effective-Deletion-Time**](a-msds-localeffectivedeletiontime.md) | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-local-Effective-Recycle-Time**](a-msds-localeffectiverecycletime.md)   | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Mastered-By**](a-msds-masteredby.md)                                   | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Members-For-Az-Role-BL**](a-msds-membersforazrolebl.md)                | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-NC-Repl-Cursors**](a-msds-ncreplcursors.md)                            | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-NC-Repl-Inbound-Neighbors**](a-msds-ncreplinboundneighbors.md)         | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-NC-Repl-Outbound-Neighbors**](a-msds-ncreploutboundneighbors.md)       | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-NC-RO-Replica-Locations-BL**](a-msds-nc-ro-replica-locations-bl.md)    | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-NC-Type**](a-msds-nctype.md)                                           | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Non-Members**](a-msds-nonmembers.md)                                   | False     | **Group**                                                                                                                          |
| [**ms-DS-Non-Members-BL**](a-msds-nonmembersbl.md)                              | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Object-Reference-BL**](a-msds-objectreferencebl.md)                    | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-OIDToGroup-Link-BL**](a-msds-oidtogrouplinkbl.md)                      | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Operations-For-Az-Role-BL**](a-msds-operationsforazrolebl.md)          | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Operations-For-Az-Task-BL**](a-msds-operationsforaztaskbl.md)          | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Phonetic-Display-Name**](a-msds-phoneticdisplayname.md)                | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**ms-DS-Principal-Name**](a-msds-principalname.md)                             | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-PSO-Applied**](a-msds-psoapplied.md)                                   | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Repl-Attribute-Meta-Data**](a-msds-replattributemetadata.md)           | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Repl-Value-Meta-Data**](a-msds-replvaluemetadata.md)                   | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Revealed-DSAs**](a-msds-revealeddsas.md)                               | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Revealed-List-BL**](a-msds-revealedlistbl.md)                          | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Tasks-For-Az-Role-BL**](a-msds-tasksforazrolebl.md)                    | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Tasks-For-Az-Task-BL**](a-msds-tasksforaztaskbl.md)                    | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-Exch-Assistant-Name**](a-msexchassistantname.md)                          | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**ms-Exch-LabeledURI**](a-msexchlabeleduri.md)                                 | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**ms-Exch-Owner-BL**](a-ownerbl.md)                                            | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**msSFU-30-Name**](a-mssfu30name.md)                                           | False     | **Group**                                                                                                                          |
| [**msSFU-30-Nis-Domain**](a-mssfu30nisdomain.md)                                | False     | **Group**                                                                                                                          |
| [**msSFU-30-Posix-Member**](a-mssfu30posixmember.md)                            | False     | **Group**                                                                                                                          |
| [**msSFU-30-Posix-Member-Of**](a-mssfu30posixmemberof.md)                       | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**netboot-SCP-BL**](a-netbootscpbl.md)                                         | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Non-Security-Member**](a-nonsecuritymember.md)                               | False     | **Group**                                                                                                                          |
| [**Non-Security-Member-BL**](a-nonsecuritymemberbl.md)                          | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**NT-Group-Members**](a-ntgroupmembers.md)                                     | False     | **Group**                                                                                                                          |
| [**NT-Security-Descriptor**](a-ntsecuritydescriptor.md)                         | True      | [**Top**](c-top.md)<br/> [**Security-Principal**](c-securityprincipal.md)<br/>                                       |
| [**Obj-Dist-Name**](a-distinguishedname.md)                                     | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Object-Category**](a-objectcategory.md)                                      | True      | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Object-Class**](a-objectclass.md)                                            | True      | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Object-Guid**](a-objectguid.md)                                              | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Object-Sid**](a-objectsid.md)                                                | True      | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**Object-Version**](a-objectversion.md)                                        | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Operator-Count**](a-operatorcount.md)                                        | False     | **Group**                                                                                                                          |
| [**Other-Well-Known-Objects**](a-otherwellknownobjects.md)                      | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Partial-Attribute-Deletion-List**](a-partialattributedeletionlist.md)        | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Partial-Attribute-Set**](a-partialattributeset.md)                           | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Possible-Inferiors**](a-possibleinferiors.md)                                | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Primary-Group-Token**](a-primarygrouptoken.md)                               | False     | **Group**                                                                                                                          |
| [**Proxied-Object-Name**](a-proxiedobjectname.md)                               | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Proxy-Addresses**](a-proxyaddresses.md)                                      | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Query-Policy-BL**](a-querypolicybl.md)                                       | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**RDN**](a-name.md)                                                            | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Repl-Property-Meta-Data**](a-replpropertymetadata.md)                        | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Repl-UpToDate-Vector**](a-repluptodatevector.md)                             | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Reports**](a-directreports.md)                                               | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Reps-From**](a-repsfrom.md)                                                  | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Reps-To**](a-repsto.md)                                                      | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Revision**](a-revision.md)                                                   | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Rid**](a-rid.md)                                                             | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**SAM-Account-Name**](a-samaccountname.md)                                     | True      | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**SAM-Account-Type**](a-samaccounttype.md)                                     | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**SD-Rights-Effective**](a-sdrightseffective.md)                               | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**secretary**](a-secretary.md)                                                 | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**Security-Identifier**](a-securityidentifier.md)                              | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**Server-Reference-BL**](a-serverreferencebl.md)                               | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Show-In-Address-Book**](a-showinaddressbook.md)                              | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**Show-In-Advanced-View-Only**](a-showinadvancedviewonly.md)                   | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**SID-History**](a-sidhistory.md)                                              | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**Site-Object-BL**](a-siteobjectbl.md)                                         | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Structural-Object-Class**](a-structuralobjectclass.md)                       | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Sub-Refs**](a-subrefs.md)                                                    | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**SubSchemaSubEntry**](a-subschemasubentry.md)                                 | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Supplemental-Credentials**](a-supplementalcredentials.md)                    | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**System-Flags**](a-systemflags.md)                                            | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Telephone-Number**](a-telephonenumber.md)                                    | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**Text-Encoded-OR-Address**](a-textencodedoraddress.md)                        | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**Token-Groups**](a-tokengroups.md)                                            | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**Token-Groups-Global-And-Universal**](a-tokengroupsglobalanduniversal.md)     | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**Token-Groups-No-GC-Acceptable**](a-tokengroupsnogcacceptable.md)             | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**unixUserPassword**](a-unixuserpassword.md)                                   | False     | [**posixGroup**](c-posixgroup.md)<br/>                                                                                      |
| [**User-Cert**](a-usercert.md)                                                  | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**User-Password**](a-userpassword.md)                                          | False     | [**posixGroup**](c-posixgroup.md)<br/>                                                                                      |
| [**User-SMIME-Certificate**](a-usersmimecertificate.md)                         | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**USN-Changed**](a-usnchanged.md)                                              | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**USN-Created**](a-usncreated.md)                                              | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**USN-DSA-Last-Obj-Removed**](a-usndsalastobjremoved.md)                       | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**USN-Intersite**](a-usnintersite.md)                                          | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**USN-Last-Obj-Rem**](a-usnlastobjrem.md)                                      | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**USN-Source**](a-usnsource.md)                                                | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Wbem-Path**](a-wbempath.md)                                                  | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Well-Known-Objects**](a-wellknownobjects.md)                                 | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**When-Changed**](a-whenchanged.md)                                            | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**When-Created**](a-whencreated.md)                                            | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**WWW-Home-Page**](a-wwwhomepage.md)                                           | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**WWW-Page-Other**](a-url.md)                                                  | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**X509-Cert**](a-usercertificate.md)                                           | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |



## Windows Server 2008 R2 Extended Rights

This class contains the following extended rights for Windows Server 2008 R2:



| Common Name                  |
|------------------------------|
| [**Send-To**](r-send-to.md) |



## Windows Server 2008 R2 Validated Writes

This class contains the following validated writes for Windows Server 2008 R2:



| Common Name                                  |
|----------------------------------------------|
| [**Self-Membership**](r-self-membership.md) |



## Windows Server 2008 R2 Property Sets

This class contains the following property sets for Windows Server 2008 R2:



| Common Name                                      |
|--------------------------------------------------|
| [**Email-Information**](r-email-information.md) |



## Windows Server 2012

-   [Attributes](#windows-server-2012-attributes)
-   [Extended Rights](#windows-server-2012-extended-rights)
-   [Validated Writes](#windows-server-2012-validated-writes)
-   [Property Sets](#windows-server-2012-property-sets)



| Entry | Value |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| System-Only                 | False                                                                                                                                                                                                                                                                                                            |
| Object-Category             | 1                                                                                                                                                                                                                                                                                                                |
| Default-Object-Category     | \-                                                                                                                                                                                                                                                                                                               |
| Governs-Id                  | 1.2.840.113556.1.5.8                                                                                                                                                                                                                                                                                             |
| Default-Hiding-Value        | 0                                                                                                                                                                                                                                                                                                                |
| Rdn-Att-Id                  | [**Common-Name**](a-cn.md)<br/>                                                                                                                                                                                                                                                                           |
| Subclass of                 | [**Top**](c-top.md)<br/>                                                                                                                                                                                                                                                                                  |
| Possible Superiors          | [**Domain-DNS**](c-domaindns.md)[**Organizational-Unit**](c-organizationalunit.md)[**Builtin-Domain**](c-builtindomain.md)[**Container**](c-container.md)[**ms-DS-Az-Admin-Manager**](c-msds-azadminmanager.md)[**ms-DS-Az-Application**](c-msds-azapplication.md)[**ms-DS-Az-Scope**](c-msds-azscope.md) |
| Auxiliary Classes           | [**posixGroup**](c-posixgroup.md)[**Security-Principal**](c-securityprincipal.md) (System)[**Mail-Recipient**](c-mailrecipient.md) (System)                                                                                                                                                                   |
| NT-Security-Descriptor      | O:BAG:BAD:S:                                                                                                                                                                                                                                                                                                     |
| Default Security Descriptor | D:(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;DA)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;SY)(A;;RPLCLORC;;;AU)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;AO)(A;;RPLCLORC;;;PS)(OA;;CR;ab721a55-1e2f-11d0-9819-00aa0040529b;;AU)(OA;;RP;46a9b11d-60ae-405a-b7e8-ff8a58d456d2;;S-1-5-32-560)                                                   |
| System-Flags                | 0x00000010                                                                                                                                                                                                                                                                                                       |



## Windows Server 2012 Attributes

This class contains the following attributes for Windows Server 2012:



| Attribute                                                                                    | Mandatory | Derived from                                                                                                                       |
|----------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------------------------------------------------------------------------------|
| [**Account-Name-History**](a-accountnamehistory.md)                                         | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**Admin-Count**](a-admincount.md)                                                          | False     | **Group**                                                                                                                          |
| [**Admin-Description**](a-admindescription.md)                                              | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Admin-Display-Name**](a-admindisplayname.md)                                             | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Allowed-Attributes**](a-allowedattributes.md)                                            | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Allowed-Attributes-Effective**](a-allowedattributeseffective.md)                         | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Allowed-Child-Classes**](a-allowedchildclasses.md)                                       | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Allowed-Child-Classes-Effective**](a-allowedchildclasseseffective.md)                    | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Alt-Security-Identities**](a-altsecurityidentities.md)                                   | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**Bridgehead-Server-List-BL**](a-bridgeheadserverlistbl.md)                                | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Canonical-Name**](a-canonicalname.md)                                                    | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Comment**](a-info.md)                                                                    | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**Common-Name**](a-cn.md)                                                                  | True      | [**Top**](c-top.md)<br/> [**posixGroup**](c-posixgroup.md)<br/> [**Mail-Recipient**](c-mailrecipient.md)<br/> |
| [**Control-Access-Rights**](a-controlaccessrights.md)                                       | False     | **Group**                                                                                                                          |
| [**Create-Time-Stamp**](a-createtimestamp.md)                                               | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Description**](a-description.md)                                                         | False     | [**Top**](c-top.md)<br/> [**posixGroup**](c-posixgroup.md)<br/>                                                      |
| [**Desktop-Profile**](a-desktopprofile.md)                                                  | False     | **Group**                                                                                                                          |
| [**Display-Name**](a-displayname.md)                                                        | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Display-Name-Printable**](a-displaynameprintable.md)                                     | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**DSA-Signature**](a-dsasignature.md)                                                      | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**DS-Core-Propagation-Data**](a-dscorepropagationdata.md)                                  | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**E-mail-Addresses**](a-mail.md)                                                           | False     | **Group**                                                                                                                          |
| [**Extension-Name**](a-extensionname.md)                                                    | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Flags**](a-flags.md)                                                                     | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**From-Entry**](a-fromentry.md)                                                            | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Frs-Computer-Reference-BL**](a-frscomputerreferencebl.md)                                | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**FRS-Member-Reference-BL**](a-frsmemberreferencebl.md)                                    | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**FSMO-Role-Owner**](a-fsmoroleowner.md)                                                   | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Garbage-Coll-Period**](a-garbagecollperiod.md)                                           | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**gidNumber**](a-gidnumber.md)                                                             | False     | [**posixGroup**](c-posixgroup.md)<br/>                                                                                      |
| [**Group-Attributes**](a-groupattributes.md)                                                | False     | **Group**                                                                                                                          |
| [**Group-Membership-SAM**](a-groupmembershipsam.md)                                         | False     | **Group**                                                                                                                          |
| [**Group-Type**](a-grouptype.md)                                                            | True      | **Group**                                                                                                                          |
| [**Instance-Type**](a-instancetype.md)                                                      | True      | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Is-Critical-System-Object**](a-iscriticalsystemobject.md)                                | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Is-Deleted**](a-isdeleted.md)                                                            | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Is-Member-Of-DL**](a-memberof.md)                                                        | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Is-Privilege-Holder**](a-isprivilegeholder.md)                                           | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Is-Recycled**](a-isrecycled.md)                                                          | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**labeledURI**](a-labeleduri.md)                                                           | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**Last-Known-Parent**](a-lastknownparent.md)                                               | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Legacy-Exchange-DN**](a-legacyexchangedn.md)                                             | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**Managed-By**](a-managedby.md)                                                            | False     | **Group**                                                                                                                          |
| [**Managed-Objects**](a-managedobjects.md)                                                  | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Mastered-By**](a-masteredby.md)                                                          | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Member**](a-member.md)                                                                   | False     | **Group**                                                                                                                          |
| [**memberUid**](a-memberuid.md)                                                             | False     | [**posixGroup**](c-posixgroup.md)<br/>                                                                                      |
| [**Modify-Time-Stamp**](a-modifytimestamp.md)                                               | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-COM-PartitionSetLink**](a-mscom-partitionsetlink.md)                                  | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-COM-UserLink**](a-mscom-userlink.md)                                                  | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DFSR-ComputerReferenceBL**](a-msdfsr-computerreferencebl.md)                          | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DFSR-MemberReferenceBL**](a-msdfsr-memberreferencebl.md)                              | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Approx-Immed-Subordinates**](a-msds-approx-immed-subordinates.md)                  | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-AuthenticatedTo-Accountlist**](a-msds-authenticatedtoaccountlist.md)               | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Az-Application-Data**](a-msds-azapplicationdata.md)                                | False     | **Group**                                                                                                                          |
| [**ms-DS-Az-Biz-Rule**](a-msds-azbizrule.md)                                                | False     | **Group**                                                                                                                          |
| [**ms-DS-Az-Biz-Rule-Language**](a-msds-azbizrulelanguage.md)                               | False     | **Group**                                                                                                                          |
| [**ms-DS-Az-Generic-Data**](a-msds-azgenericdata.md)                                        | False     | **Group**                                                                                                                          |
| [**ms-DS-Az-Last-Imported-Biz-Rule-Path**](a-msds-azlastimportedbizrulepath.md)             | False     | **Group**                                                                                                                          |
| [**ms-DS-Az-LDAP-Query**](a-msds-azldapquery.md)                                            | False     | **Group**                                                                                                                          |
| [**ms-DS-Az-Object-Guid**](a-msds-azobjectguid.md)                                          | False     | **Group**                                                                                                                          |
| [**ms-DS-Claim-Shares-Possible-Values-With-BL**](a-msds-claimsharespossiblevalueswithbl.md) | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**MS-DS-Consistency-Child-Count**](a-ms-ds-consistencychildcount.md)                       | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**MS-DS-Consistency-Guid**](a-ms-ds-consistencyguid.md)                                    | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Enabled-Feature-BL**](a-msds-enabledfeaturebl.md)                                  | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-GeoCoordinates-Altitude**](a-msds-geocoordinatesaltitude.md)                       | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**ms-DS-GeoCoordinates-Latitude**](a-msds-geocoordinateslatitude.md)                       | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**ms-DS-GeoCoordinates-Longitude**](a-msds-geocoordinateslongitude.md)                     | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**ms-DS-Host-Service-Account-BL**](a-msds-hostserviceaccountbl.md)                         | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Is-Domain-For**](a-msds-isdomainfor.md)                                            | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Is-Full-Replica-For**](a-msds-isfullreplicafor.md)                                 | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Is-Partial-Replica-For**](a-msds-ispartialreplicafor.md)                           | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Is-Primary-Computer-For**](a-msds-isprimarycomputerfor.md)                         | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-KeyVersionNumber**](a-msds-keyversionnumber.md)                                    | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**ms-DS-KrbTgt-Link-BL**](a-msds-krbtgtlinkbl.md)                                          | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Last-Known-RDN**](a-msds-lastknownrdn.md)                                          | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-local-Effective-Deletion-Time**](a-msds-localeffectivedeletiontime.md)             | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-local-Effective-Recycle-Time**](a-msds-localeffectiverecycletime.md)               | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Mastered-By**](a-msds-masteredby.md)                                               | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Members-For-Az-Role-BL**](a-msds-membersforazrolebl.md)                            | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Members-Of-Resource-Property-List-BL**](a-msds-membersofresourcepropertylistbl.md) | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-NC-Repl-Cursors**](a-msds-ncreplcursors.md)                                        | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-NC-Repl-Inbound-Neighbors**](a-msds-ncreplinboundneighbors.md)                     | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-NC-Repl-Outbound-Neighbors**](a-msds-ncreploutboundneighbors.md)                   | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-NC-RO-Replica-Locations-BL**](a-msds-nc-ro-replica-locations-bl.md)                | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-NC-Type**](a-msds-nctype.md)                                                       | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Non-Members**](a-msds-nonmembers.md)                                               | False     | **Group**                                                                                                                          |
| [**ms-DS-Non-Members-BL**](a-msds-nonmembersbl.md)                                          | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Object-Reference-BL**](a-msds-objectreferencebl.md)                                | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-OIDToGroup-Link-BL**](a-msds-oidtogrouplinkbl.md)                                  | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Operations-For-Az-Role-BL**](a-msds-operationsforazrolebl.md)                      | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Operations-For-Az-Task-BL**](a-msds-operationsforaztaskbl.md)                      | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Phonetic-Display-Name**](a-msds-phoneticdisplayname.md)                            | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**ms-DS-Primary-Computer**](a-msds-primarycomputer.md)                                     | False     | **Group**                                                                                                                          |
| [**ms-DS-Principal-Name**](a-msds-principalname.md)                                         | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-PSO-Applied**](a-msds-psoapplied.md)                                               | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Repl-Attribute-Meta-Data**](a-msds-replattributemetadata.md)                       | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Repl-Value-Meta-Data**](a-msds-replvaluemetadata.md)                               | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Revealed-DSAs**](a-msds-revealeddsas.md)                                           | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Revealed-List-BL**](a-msds-revealedlistbl.md)                                      | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Tasks-For-Az-Role-BL**](a-msds-tasksforazrolebl.md)                                | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Tasks-For-Az-Task-BL**](a-msds-tasksforaztaskbl.md)                                | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-TDO-Egress-BL**](a-msds-tdoegressbl.md)                                            | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-TDO-Ingress-BL**](a-msds-tdoingressbl.md)                                          | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-DS-Value-Type-Reference-BL**](a-msds-valuetypereferencebl.md)                         | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**ms-Exch-Assistant-Name**](a-msexchassistantname.md)                                      | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**ms-Exch-LabeledURI**](a-msexchlabeleduri.md)                                             | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**ms-Exch-Owner-BL**](a-ownerbl.md)                                                        | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**msSFU-30-Name**](a-mssfu30name.md)                                                       | False     | **Group**                                                                                                                          |
| [**msSFU-30-Nis-Domain**](a-mssfu30nisdomain.md)                                            | False     | **Group**                                                                                                                          |
| [**msSFU-30-Posix-Member**](a-mssfu30posixmember.md)                                        | False     | **Group**                                                                                                                          |
| [**msSFU-30-Posix-Member-Of**](a-mssfu30posixmemberof.md)                                   | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**netboot-SCP-BL**](a-netbootscpbl.md)                                                     | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Non-Security-Member**](a-nonsecuritymember.md)                                           | False     | **Group**                                                                                                                          |
| [**Non-Security-Member-BL**](a-nonsecuritymemberbl.md)                                      | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**NT-Group-Members**](a-ntgroupmembers.md)                                                 | False     | **Group**                                                                                                                          |
| [**NT-Security-Descriptor**](a-ntsecuritydescriptor.md)                                     | True      | [**Top**](c-top.md)<br/> [**Security-Principal**](c-securityprincipal.md)<br/>                                       |
| [**Obj-Dist-Name**](a-distinguishedname.md)                                                 | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Object-Category**](a-objectcategory.md)                                                  | True      | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Object-Class**](a-objectclass.md)                                                        | True      | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Object-Guid**](a-objectguid.md)                                                          | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Object-Sid**](a-objectsid.md)                                                            | True      | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**Object-Version**](a-objectversion.md)                                                    | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Operator-Count**](a-operatorcount.md)                                                    | False     | **Group**                                                                                                                          |
| [**Other-Well-Known-Objects**](a-otherwellknownobjects.md)                                  | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Partial-Attribute-Deletion-List**](a-partialattributedeletionlist.md)                    | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Partial-Attribute-Set**](a-partialattributeset.md)                                       | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Possible-Inferiors**](a-possibleinferiors.md)                                            | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Primary-Group-Token**](a-primarygrouptoken.md)                                           | False     | **Group**                                                                                                                          |
| [**Proxied-Object-Name**](a-proxiedobjectname.md)                                           | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Proxy-Addresses**](a-proxyaddresses.md)                                                  | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Query-Policy-BL**](a-querypolicybl.md)                                                   | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**RDN**](a-name.md)                                                                        | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Repl-Property-Meta-Data**](a-replpropertymetadata.md)                                    | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Repl-UpToDate-Vector**](a-repluptodatevector.md)                                         | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Reports**](a-directreports.md)                                                           | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Reps-From**](a-repsfrom.md)                                                              | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Reps-To**](a-repsto.md)                                                                  | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Revision**](a-revision.md)                                                               | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Rid**](a-rid.md)                                                                         | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**SAM-Account-Name**](a-samaccountname.md)                                                 | True      | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**SAM-Account-Type**](a-samaccounttype.md)                                                 | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**SD-Rights-Effective**](a-sdrightseffective.md)                                           | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**secretary**](a-secretary.md)                                                             | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**Security-Identifier**](a-securityidentifier.md)                                          | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**Server-Reference-BL**](a-serverreferencebl.md)                                           | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Show-In-Address-Book**](a-showinaddressbook.md)                                          | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**Show-In-Advanced-View-Only**](a-showinadvancedviewonly.md)                               | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**SID-History**](a-sidhistory.md)                                                          | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**Site-Object-BL**](a-siteobjectbl.md)                                                     | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Structural-Object-Class**](a-structuralobjectclass.md)                                   | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Sub-Refs**](a-subrefs.md)                                                                | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**SubSchemaSubEntry**](a-subschemasubentry.md)                                             | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Supplemental-Credentials**](a-supplementalcredentials.md)                                | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**System-Flags**](a-systemflags.md)                                                        | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Telephone-Number**](a-telephonenumber.md)                                                | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**Text-Encoded-OR-Address**](a-textencodedoraddress.md)                                    | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**Token-Groups**](a-tokengroups.md)                                                        | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**Token-Groups-Global-And-Universal**](a-tokengroupsglobalanduniversal.md)                 | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**Token-Groups-No-GC-Acceptable**](a-tokengroupsnogcacceptable.md)                         | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                                                       |
| [**unixUserPassword**](a-unixuserpassword.md)                                               | False     | [**posixGroup**](c-posixgroup.md)<br/>                                                                                      |
| [**User-Cert**](a-usercert.md)                                                              | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**User-Password**](a-userpassword.md)                                                      | False     | [**posixGroup**](c-posixgroup.md)<br/>                                                                                      |
| [**User-SMIME-Certificate**](a-usersmimecertificate.md)                                     | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |
| [**USN-Changed**](a-usnchanged.md)                                                          | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**USN-Created**](a-usncreated.md)                                                          | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**USN-DSA-Last-Obj-Removed**](a-usndsalastobjremoved.md)                                   | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**USN-Intersite**](a-usnintersite.md)                                                      | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**USN-Last-Obj-Rem**](a-usnlastobjrem.md)                                                  | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**USN-Source**](a-usnsource.md)                                                            | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Wbem-Path**](a-wbempath.md)                                                              | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**Well-Known-Objects**](a-wellknownobjects.md)                                             | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**When-Changed**](a-whenchanged.md)                                                        | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**When-Created**](a-whencreated.md)                                                        | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**WWW-Home-Page**](a-wwwhomepage.md)                                                       | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**WWW-Page-Other**](a-url.md)                                                              | False     | [**Top**](c-top.md)<br/>                                                                                                    |
| [**X509-Cert**](a-usercertificate.md)                                                       | False     | [**Mail-Recipient**](c-mailrecipient.md)<br/>                                                                               |



## Windows Server 2012 Extended Rights

This class contains the following extended rights for Windows Server 2012:



| Common Name                  |
|------------------------------|
| [**Send-To**](r-send-to.md) |



## Windows Server 2012 Validated Writes

This class contains the following validated writes for Windows Server 2012:



| Common Name                                  |
|----------------------------------------------|
| [**Self-Membership**](r-self-membership.md) |



## Windows Server 2012 Property Sets

This class contains the following property sets for Windows Server 2012:



| Common Name                                      |
|--------------------------------------------------|
| [**Email-Information**](r-email-information.md) |



 

 





