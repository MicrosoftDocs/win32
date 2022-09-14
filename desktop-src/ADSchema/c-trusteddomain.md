---
title: Trusted-Domain class
description: An object that represents a domain trusted by (or trusting) the local domain.
ms.assetid: dd455d89-2ad0-4bc7-a84e-449b4c334bd2
ms.tgt_platform: multiple
keywords:
- Trusted-Domain class AD Schema
- trustedDomain class AD Schema
topic_type:
- apiref
api_name:
- Trusted-Domain
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# Trusted-Domain class

An object that represents a domain trusted by (or trusting) the local domain.



| Entry | Value |
|-------------------|--------------------------------------|
| CN                | Trusted-Domain                       |
| Ldap-Display-Name | trustedDomain                        |
| Update Privilege  | This value is set by the system.     |
| Update Frequency  | When a new trust is created.         |
| Schema-Id-Guid    | bf967ab8-0de6-11d0-a285-00aa003049e2 |



## Implementations

-   [**Windows 2000 Server**](#windows-2000-server)
-   [**Windows Server 2003**](#windows-server-2003)
-   [**Windows Server 2003 R2**](#windows-server-2003-r2)
-   [**Windows Server 2008**](#windows-server-2008)
-   [**Windows Server 2008 R2**](#windows-server-2008-r2)
-   [**Windows Server 2012**](#windows-server-2012)

## Windows 2000 Server

-   [Attributes](#windows-2000-server-attributes)



| Entry | Value |
|-----------------------------|----------------------------------------------------------------------------------------------|
| System-Only                 | False                                                                                        |
| Object-Category             | 1                                                                                            |
| Default-Object-Category     | \-                                                                                           |
| Governs-Id                  | 1.2.840.113556.1.5.34                                                                        |
| Default-Hiding-Value        | 1                                                                                            |
| Rdn-Att-Id                  | [**Common-Name**](a-cn.md)<br/>                                                       |
| Subclass of                 | [**Leaf**](c-leaf.md)<br/>                                                            |
| Possible Superiors          | [**Container**](c-container.md)                                                             |
| Auxiliary Classes           | \-                                                                                           |
| NT-Security-Descriptor      | O:BAG:BAD:S:                                                                                 |
| Default Security Descriptor | D:(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;DA)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;SY)(A;;RPLCLORC;;;AU) |
| System-Flags                | 0x00000010                                                                                   |



## Windows 2000 Server Attributes

This class contains the following attributes for Windows 2000 Server:



| Attribute                                                                   | Mandatory | Derived from                    |
|-----------------------------------------------------------------------------|-----------|---------------------------------|
| [**Additional-Trusted-Service-Names**](a-additionaltrustedservicenames.md) | False     | **Trusted-Domain**              |
| [**Admin-Description**](a-admindescription.md)                             | False     | [**Top**](c-top.md)<br/> |
| [**Admin-Display-Name**](a-admindisplayname.md)                            | False     | [**Top**](c-top.md)<br/> |
| [**Allowed-Attributes**](a-allowedattributes.md)                           | False     | [**Top**](c-top.md)<br/> |
| [**Allowed-Attributes-Effective**](a-allowedattributeseffective.md)        | False     | [**Top**](c-top.md)<br/> |
| [**Allowed-Child-Classes**](a-allowedchildclasses.md)                      | False     | [**Top**](c-top.md)<br/> |
| [**Allowed-Child-Classes-Effective**](a-allowedchildclasseseffective.md)   | False     | [**Top**](c-top.md)<br/> |
| [**Bridgehead-Server-List-BL**](a-bridgeheadserverlistbl.md)               | False     | [**Top**](c-top.md)<br/> |
| [**Canonical-Name**](a-canonicalname.md)                                   | False     | [**Top**](c-top.md)<br/> |
| [**Common-Name**](a-cn.md)                                                 | False     | [**Top**](c-top.md)<br/> |
| [**Create-Time-Stamp**](a-createtimestamp.md)                              | False     | [**Top**](c-top.md)<br/> |
| [**Description**](a-description.md)                                        | False     | [**Top**](c-top.md)<br/> |
| [**Display-Name**](a-displayname.md)                                       | False     | [**Top**](c-top.md)<br/> |
| [**Display-Name-Printable**](a-displaynameprintable.md)                    | False     | [**Top**](c-top.md)<br/> |
| [**Domain-Cross-Ref**](a-domaincrossref.md)                                | False     | **Trusted-Domain**              |
| [**Domain-Identifier**](a-domainidentifier.md)                             | False     | **Trusted-Domain**              |
| [**DSA-Signature**](a-dsasignature.md)                                     | False     | [**Top**](c-top.md)<br/> |
| [**DS-Core-Propagation-Data**](a-dscorepropagationdata.md)                 | False     | [**Top**](c-top.md)<br/> |
| [**Extension-Name**](a-extensionname.md)                                   | False     | [**Top**](c-top.md)<br/> |
| [**Flags**](a-flags.md)                                                    | False     | [**Top**](c-top.md)<br/> |
| [**Flat-Name**](a-flatname.md)                                             | False     | **Trusted-Domain**              |
| [**From-Entry**](a-fromentry.md)                                           | False     | [**Top**](c-top.md)<br/> |
| [**Frs-Computer-Reference-BL**](a-frscomputerreferencebl.md)               | False     | [**Top**](c-top.md)<br/> |
| [**FRS-Member-Reference-BL**](a-frsmemberreferencebl.md)                   | False     | [**Top**](c-top.md)<br/> |
| [**FSMO-Role-Owner**](a-fsmoroleowner.md)                                  | False     | [**Top**](c-top.md)<br/> |
| [**Initial-Auth-Incoming**](a-initialauthincoming.md)                      | False     | **Trusted-Domain**              |
| [**Initial-Auth-Outgoing**](a-initialauthoutgoing.md)                      | False     | **Trusted-Domain**              |
| [**Instance-Type**](a-instancetype.md)                                     | True      | [**Top**](c-top.md)<br/> |
| [**Is-Critical-System-Object**](a-iscriticalsystemobject.md)               | False     | [**Top**](c-top.md)<br/> |
| [**Is-Deleted**](a-isdeleted.md)                                           | False     | [**Top**](c-top.md)<br/> |
| [**Is-Member-Of-DL**](a-memberof.md)                                       | False     | [**Top**](c-top.md)<br/> |
| [**Is-Privilege-Holder**](a-isprivilegeholder.md)                          | False     | [**Top**](c-top.md)<br/> |
| [**Last-Known-Parent**](a-lastknownparent.md)                              | False     | [**Top**](c-top.md)<br/> |
| [**Managed-Objects**](a-managedobjects.md)                                 | False     | [**Top**](c-top.md)<br/> |
| [**Mastered-By**](a-masteredby.md)                                         | False     | [**Top**](c-top.md)<br/> |
| [**Modify-Time-Stamp**](a-modifytimestamp.md)                              | False     | [**Top**](c-top.md)<br/> |
| [**MS-DS-Consistency-Child-Count**](a-ms-ds-consistencychildcount.md)      | False     | [**Top**](c-top.md)<br/> |
| [**MS-DS-Consistency-Guid**](a-ms-ds-consistencyguid.md)                   | False     | [**Top**](c-top.md)<br/> |
| [**netboot-SCP-BL**](a-netbootscpbl.md)                                    | False     | [**Top**](c-top.md)<br/> |
| [**Non-Security-Member-BL**](a-nonsecuritymemberbl.md)                     | False     | [**Top**](c-top.md)<br/> |
| [**NT-Security-Descriptor**](a-ntsecuritydescriptor.md)                    | True      | [**Top**](c-top.md)<br/> |
| [**Obj-Dist-Name**](a-distinguishedname.md)                                | False     | [**Top**](c-top.md)<br/> |
| [**Object-Category**](a-objectcategory.md)                                 | True      | [**Top**](c-top.md)<br/> |
| [**Object-Class**](a-objectclass.md)                                       | True      | [**Top**](c-top.md)<br/> |
| [**Object-Guid**](a-objectguid.md)                                         | False     | [**Top**](c-top.md)<br/> |
| [**Object-Version**](a-objectversion.md)                                   | False     | [**Top**](c-top.md)<br/> |
| [**Other-Well-Known-Objects**](a-otherwellknownobjects.md)                 | False     | [**Top**](c-top.md)<br/> |
| [**Partial-Attribute-Deletion-List**](a-partialattributedeletionlist.md)   | False     | [**Top**](c-top.md)<br/> |
| [**Partial-Attribute-Set**](a-partialattributeset.md)                      | False     | [**Top**](c-top.md)<br/> |
| [**Possible-Inferiors**](a-possibleinferiors.md)                           | False     | [**Top**](c-top.md)<br/> |
| [**Proxied-Object-Name**](a-proxiedobjectname.md)                          | False     | [**Top**](c-top.md)<br/> |
| [**Proxy-Addresses**](a-proxyaddresses.md)                                 | False     | [**Top**](c-top.md)<br/> |
| [**Query-Policy-BL**](a-querypolicybl.md)                                  | False     | [**Top**](c-top.md)<br/> |
| [**RDN**](a-name.md)                                                       | False     | [**Top**](c-top.md)<br/> |
| [**Repl-Property-Meta-Data**](a-replpropertymetadata.md)                   | False     | [**Top**](c-top.md)<br/> |
| [**Repl-UpToDate-Vector**](a-repluptodatevector.md)                        | False     | [**Top**](c-top.md)<br/> |
| [**Reports**](a-directreports.md)                                          | False     | [**Top**](c-top.md)<br/> |
| [**Reps-From**](a-repsfrom.md)                                             | False     | [**Top**](c-top.md)<br/> |
| [**Reps-To**](a-repsto.md)                                                 | False     | [**Top**](c-top.md)<br/> |
| [**Revision**](a-revision.md)                                              | False     | [**Top**](c-top.md)<br/> |
| [**SD-Rights-Effective**](a-sdrightseffective.md)                          | False     | [**Top**](c-top.md)<br/> |
| [**Security-Identifier**](a-securityidentifier.md)                         | False     | **Trusted-Domain**              |
| [**Server-Reference-BL**](a-serverreferencebl.md)                          | False     | [**Top**](c-top.md)<br/> |
| [**Show-In-Advanced-View-Only**](a-showinadvancedviewonly.md)              | False     | [**Top**](c-top.md)<br/> |
| [**Site-Object-BL**](a-siteobjectbl.md)                                    | False     | [**Top**](c-top.md)<br/> |
| [**Sub-Refs**](a-subrefs.md)                                               | False     | [**Top**](c-top.md)<br/> |
| [**SubSchemaSubEntry**](a-subschemasubentry.md)                            | False     | [**Top**](c-top.md)<br/> |
| [**System-Flags**](a-systemflags.md)                                       | False     | [**Top**](c-top.md)<br/> |
| [**Trust-Attributes**](a-trustattributes.md)                               | False     | **Trusted-Domain**              |
| [**Trust-Auth-Incoming**](a-trustauthincoming.md)                          | False     | **Trusted-Domain**              |
| [**Trust-Auth-Outgoing**](a-trustauthoutgoing.md)                          | False     | **Trusted-Domain**              |
| [**Trust-Direction**](a-trustdirection.md)                                 | False     | **Trusted-Domain**              |
| [**Trust-Partner**](a-trustpartner.md)                                     | False     | **Trusted-Domain**              |
| [**Trust-Posix-Offset**](a-trustposixoffset.md)                            | False     | **Trusted-Domain**              |
| [**Trust-Type**](a-trusttype.md)                                           | False     | **Trusted-Domain**              |
| [**USN-Changed**](a-usnchanged.md)                                         | False     | [**Top**](c-top.md)<br/> |
| [**USN-Created**](a-usncreated.md)                                         | False     | [**Top**](c-top.md)<br/> |
| [**USN-DSA-Last-Obj-Removed**](a-usndsalastobjremoved.md)                  | False     | [**Top**](c-top.md)<br/> |
| [**USN-Intersite**](a-usnintersite.md)                                     | False     | [**Top**](c-top.md)<br/> |
| [**USN-Last-Obj-Rem**](a-usnlastobjrem.md)                                 | False     | [**Top**](c-top.md)<br/> |
| [**USN-Source**](a-usnsource.md)                                           | False     | [**Top**](c-top.md)<br/> |
| [**Wbem-Path**](a-wbempath.md)                                             | False     | [**Top**](c-top.md)<br/> |
| [**Well-Known-Objects**](a-wellknownobjects.md)                            | False     | [**Top**](c-top.md)<br/> |
| [**When-Changed**](a-whenchanged.md)                                       | False     | [**Top**](c-top.md)<br/> |
| [**When-Created**](a-whencreated.md)                                       | False     | [**Top**](c-top.md)<br/> |
| [**WWW-Home-Page**](a-wwwhomepage.md)                                      | False     | [**Top**](c-top.md)<br/> |
| [**WWW-Page-Other**](a-url.md)                                             | False     | [**Top**](c-top.md)<br/> |



## Windows Server 2003

-   [Attributes](#windows-server-2003-attributes)



| Entry | Value |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| System-Only                 | False                                                                                                                                                                                         |
| Object-Category             | 1                                                                                                                                                                                             |
| Default-Object-Category     | \-                                                                                                                                                                                            |
| Governs-Id                  | 1.2.840.113556.1.5.34                                                                                                                                                                         |
| Default-Hiding-Value        | 1                                                                                                                                                                                             |
| Rdn-Att-Id                  | [**Common-Name**](a-cn.md)<br/>                                                                                                                                                        |
| Subclass of                 | [**Leaf**](c-leaf.md)<br/>                                                                                                                                                             |
| Possible Superiors          | [**Container**](c-container.md)                                                                                                                                                              |
| Auxiliary Classes           | \-                                                                                                                                                                                            |
| NT-Security-Descriptor      | O:BAG:BAD:S:                                                                                                                                                                                  |
| Default Security Descriptor | D:(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;DA)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;SY)(A;;RPLCLORC;;;AU)(OA;;WP;736e4812-af31-11d2-b7df-00805f48caeb;bf967ab8-0de6-11d0-a285-00aa003049e2;CO)(A;;SD;;;CO) |
| System-Flags                | 0x00000010                                                                                                                                                                                    |



## Windows Server 2003 Attributes

This class contains the following attributes for Windows Server 2003:



| Attribute                                                                   | Mandatory | Derived from                    |
|-----------------------------------------------------------------------------|-----------|---------------------------------|
| [**Additional-Trusted-Service-Names**](a-additionaltrustedservicenames.md) | False     | **Trusted-Domain**              |
| [**Admin-Description**](a-admindescription.md)                             | False     | [**Top**](c-top.md)<br/> |
| [**Admin-Display-Name**](a-admindisplayname.md)                            | False     | [**Top**](c-top.md)<br/> |
| [**Allowed-Attributes**](a-allowedattributes.md)                           | False     | [**Top**](c-top.md)<br/> |
| [**Allowed-Attributes-Effective**](a-allowedattributeseffective.md)        | False     | [**Top**](c-top.md)<br/> |
| [**Allowed-Child-Classes**](a-allowedchildclasses.md)                      | False     | [**Top**](c-top.md)<br/> |
| [**Allowed-Child-Classes-Effective**](a-allowedchildclasseseffective.md)   | False     | [**Top**](c-top.md)<br/> |
| [**Bridgehead-Server-List-BL**](a-bridgeheadserverlistbl.md)               | False     | [**Top**](c-top.md)<br/> |
| [**Canonical-Name**](a-canonicalname.md)                                   | False     | [**Top**](c-top.md)<br/> |
| [**Common-Name**](a-cn.md)                                                 | False     | [**Top**](c-top.md)<br/> |
| [**Create-Time-Stamp**](a-createtimestamp.md)                              | False     | [**Top**](c-top.md)<br/> |
| [**Description**](a-description.md)                                        | False     | [**Top**](c-top.md)<br/> |
| [**Display-Name**](a-displayname.md)                                       | False     | [**Top**](c-top.md)<br/> |
| [**Display-Name-Printable**](a-displaynameprintable.md)                    | False     | [**Top**](c-top.md)<br/> |
| [**Domain-Cross-Ref**](a-domaincrossref.md)                                | False     | **Trusted-Domain**              |
| [**Domain-Identifier**](a-domainidentifier.md)                             | False     | **Trusted-Domain**              |
| [**DSA-Signature**](a-dsasignature.md)                                     | False     | [**Top**](c-top.md)<br/> |
| [**DS-Core-Propagation-Data**](a-dscorepropagationdata.md)                 | False     | [**Top**](c-top.md)<br/> |
| [**Extension-Name**](a-extensionname.md)                                   | False     | [**Top**](c-top.md)<br/> |
| [**Flags**](a-flags.md)                                                    | False     | [**Top**](c-top.md)<br/> |
| [**Flat-Name**](a-flatname.md)                                             | False     | **Trusted-Domain**              |
| [**From-Entry**](a-fromentry.md)                                           | False     | [**Top**](c-top.md)<br/> |
| [**Frs-Computer-Reference-BL**](a-frscomputerreferencebl.md)               | False     | [**Top**](c-top.md)<br/> |
| [**FRS-Member-Reference-BL**](a-frsmemberreferencebl.md)                   | False     | [**Top**](c-top.md)<br/> |
| [**FSMO-Role-Owner**](a-fsmoroleowner.md)                                  | False     | [**Top**](c-top.md)<br/> |
| [**Initial-Auth-Incoming**](a-initialauthincoming.md)                      | False     | **Trusted-Domain**              |
| [**Initial-Auth-Outgoing**](a-initialauthoutgoing.md)                      | False     | **Trusted-Domain**              |
| [**Instance-Type**](a-instancetype.md)                                     | True      | [**Top**](c-top.md)<br/> |
| [**Is-Critical-System-Object**](a-iscriticalsystemobject.md)               | False     | [**Top**](c-top.md)<br/> |
| [**Is-Deleted**](a-isdeleted.md)                                           | False     | [**Top**](c-top.md)<br/> |
| [**Is-Member-Of-DL**](a-memberof.md)                                       | False     | [**Top**](c-top.md)<br/> |
| [**Is-Privilege-Holder**](a-isprivilegeholder.md)                          | False     | [**Top**](c-top.md)<br/> |
| [**Last-Known-Parent**](a-lastknownparent.md)                              | False     | [**Top**](c-top.md)<br/> |
| [**Managed-Objects**](a-managedobjects.md)                                 | False     | [**Top**](c-top.md)<br/> |
| [**Mastered-By**](a-masteredby.md)                                         | False     | [**Top**](c-top.md)<br/> |
| [**Modify-Time-Stamp**](a-modifytimestamp.md)                              | False     | [**Top**](c-top.md)<br/> |
| [**ms-COM-PartitionSetLink**](a-mscom-partitionsetlink.md)                 | False     | [**Top**](c-top.md)<br/> |
| [**ms-COM-UserLink**](a-mscom-userlink.md)                                 | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Approx-Immed-Subordinates**](a-msds-approx-immed-subordinates.md) | False     | [**Top**](c-top.md)<br/> |
| [**MS-DS-Consistency-Child-Count**](a-ms-ds-consistencychildcount.md)      | False     | [**Top**](c-top.md)<br/> |
| [**MS-DS-Consistency-Guid**](a-ms-ds-consistencyguid.md)                   | False     | [**Top**](c-top.md)<br/> |
| [**MS-DS-Creator-SID**](a-ms-ds-creatorsid.md)                             | False     | **Trusted-Domain**              |
| [**ms-DS-Mastered-By**](a-msds-masteredby.md)                              | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Members-For-Az-Role-BL**](a-msds-membersforazrolebl.md)           | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-NC-Repl-Cursors**](a-msds-ncreplcursors.md)                       | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-NC-Repl-Inbound-Neighbors**](a-msds-ncreplinboundneighbors.md)    | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-NC-Repl-Outbound-Neighbors**](a-msds-ncreploutboundneighbors.md)  | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Non-Members-BL**](a-msds-nonmembersbl.md)                         | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Object-Reference-BL**](a-msds-objectreferencebl.md)               | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Operations-For-Az-Role-BL**](a-msds-operationsforazrolebl.md)     | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Operations-For-Az-Task-BL**](a-msds-operationsforaztaskbl.md)     | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Repl-Attribute-Meta-Data**](a-msds-replattributemetadata.md)      | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Repl-Value-Meta-Data**](a-msds-replvaluemetadata.md)              | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Tasks-For-Az-Role-BL**](a-msds-tasksforazrolebl.md)               | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Tasks-For-Az-Task-BL**](a-msds-tasksforaztaskbl.md)               | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Trust-Forest-Trust-Info**](a-msds-trustforesttrustinfo.md)        | False     | **Trusted-Domain**              |
| [**ms-Exch-Owner-BL**](a-ownerbl.md)                                       | False     | [**Top**](c-top.md)<br/> |
| [**netboot-SCP-BL**](a-netbootscpbl.md)                                    | False     | [**Top**](c-top.md)<br/> |
| [**Non-Security-Member-BL**](a-nonsecuritymemberbl.md)                     | False     | [**Top**](c-top.md)<br/> |
| [**NT-Security-Descriptor**](a-ntsecuritydescriptor.md)                    | True      | [**Top**](c-top.md)<br/> |
| [**Obj-Dist-Name**](a-distinguishedname.md)                                | False     | [**Top**](c-top.md)<br/> |
| [**Object-Category**](a-objectcategory.md)                                 | True      | [**Top**](c-top.md)<br/> |
| [**Object-Class**](a-objectclass.md)                                       | True      | [**Top**](c-top.md)<br/> |
| [**Object-Guid**](a-objectguid.md)                                         | False     | [**Top**](c-top.md)<br/> |
| [**Object-Version**](a-objectversion.md)                                   | False     | [**Top**](c-top.md)<br/> |
| [**Other-Well-Known-Objects**](a-otherwellknownobjects.md)                 | False     | [**Top**](c-top.md)<br/> |
| [**Partial-Attribute-Deletion-List**](a-partialattributedeletionlist.md)   | False     | [**Top**](c-top.md)<br/> |
| [**Partial-Attribute-Set**](a-partialattributeset.md)                      | False     | [**Top**](c-top.md)<br/> |
| [**Possible-Inferiors**](a-possibleinferiors.md)                           | False     | [**Top**](c-top.md)<br/> |
| [**Proxied-Object-Name**](a-proxiedobjectname.md)                          | False     | [**Top**](c-top.md)<br/> |
| [**Proxy-Addresses**](a-proxyaddresses.md)                                 | False     | [**Top**](c-top.md)<br/> |
| [**Query-Policy-BL**](a-querypolicybl.md)                                  | False     | [**Top**](c-top.md)<br/> |
| [**RDN**](a-name.md)                                                       | False     | [**Top**](c-top.md)<br/> |
| [**Repl-Property-Meta-Data**](a-replpropertymetadata.md)                   | False     | [**Top**](c-top.md)<br/> |
| [**Repl-UpToDate-Vector**](a-repluptodatevector.md)                        | False     | [**Top**](c-top.md)<br/> |
| [**Reports**](a-directreports.md)                                          | False     | [**Top**](c-top.md)<br/> |
| [**Reps-From**](a-repsfrom.md)                                             | False     | [**Top**](c-top.md)<br/> |
| [**Reps-To**](a-repsto.md)                                                 | False     | [**Top**](c-top.md)<br/> |
| [**Revision**](a-revision.md)                                              | False     | [**Top**](c-top.md)<br/> |
| [**SD-Rights-Effective**](a-sdrightseffective.md)                          | False     | [**Top**](c-top.md)<br/> |
| [**Security-Identifier**](a-securityidentifier.md)                         | False     | **Trusted-Domain**              |
| [**Server-Reference-BL**](a-serverreferencebl.md)                          | False     | [**Top**](c-top.md)<br/> |
| [**Show-In-Advanced-View-Only**](a-showinadvancedviewonly.md)              | False     | [**Top**](c-top.md)<br/> |
| [**Site-Object-BL**](a-siteobjectbl.md)                                    | False     | [**Top**](c-top.md)<br/> |
| [**Structural-Object-Class**](a-structuralobjectclass.md)                  | False     | [**Top**](c-top.md)<br/> |
| [**Sub-Refs**](a-subrefs.md)                                               | False     | [**Top**](c-top.md)<br/> |
| [**SubSchemaSubEntry**](a-subschemasubentry.md)                            | False     | [**Top**](c-top.md)<br/> |
| [**System-Flags**](a-systemflags.md)                                       | False     | [**Top**](c-top.md)<br/> |
| [**Trust-Attributes**](a-trustattributes.md)                               | False     | **Trusted-Domain**              |
| [**Trust-Auth-Incoming**](a-trustauthincoming.md)                          | False     | **Trusted-Domain**              |
| [**Trust-Auth-Outgoing**](a-trustauthoutgoing.md)                          | False     | **Trusted-Domain**              |
| [**Trust-Direction**](a-trustdirection.md)                                 | False     | **Trusted-Domain**              |
| [**Trust-Partner**](a-trustpartner.md)                                     | False     | **Trusted-Domain**              |
| [**Trust-Posix-Offset**](a-trustposixoffset.md)                            | False     | **Trusted-Domain**              |
| [**Trust-Type**](a-trusttype.md)                                           | False     | **Trusted-Domain**              |
| [**USN-Changed**](a-usnchanged.md)                                         | False     | [**Top**](c-top.md)<br/> |
| [**USN-Created**](a-usncreated.md)                                         | False     | [**Top**](c-top.md)<br/> |
| [**USN-DSA-Last-Obj-Removed**](a-usndsalastobjremoved.md)                  | False     | [**Top**](c-top.md)<br/> |
| [**USN-Intersite**](a-usnintersite.md)                                     | False     | [**Top**](c-top.md)<br/> |
| [**USN-Last-Obj-Rem**](a-usnlastobjrem.md)                                 | False     | [**Top**](c-top.md)<br/> |
| [**USN-Source**](a-usnsource.md)                                           | False     | [**Top**](c-top.md)<br/> |
| [**Wbem-Path**](a-wbempath.md)                                             | False     | [**Top**](c-top.md)<br/> |
| [**Well-Known-Objects**](a-wellknownobjects.md)                            | False     | [**Top**](c-top.md)<br/> |
| [**When-Changed**](a-whenchanged.md)                                       | False     | [**Top**](c-top.md)<br/> |
| [**When-Created**](a-whencreated.md)                                       | False     | [**Top**](c-top.md)<br/> |
| [**WWW-Home-Page**](a-wwwhomepage.md)                                      | False     | [**Top**](c-top.md)<br/> |
| [**WWW-Page-Other**](a-url.md)                                             | False     | [**Top**](c-top.md)<br/> |



## Windows Server 2003 R2

-   [Attributes](#windows-server-2003-r2-attributes)



| Entry | Value |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| System-Only                 | False                                                                                                                                                                                         |
| Object-Category             | 1                                                                                                                                                                                             |
| Default-Object-Category     | \-                                                                                                                                                                                            |
| Governs-Id                  | 1.2.840.113556.1.5.34                                                                                                                                                                         |
| Default-Hiding-Value        | 1                                                                                                                                                                                             |
| Rdn-Att-Id                  | [**Common-Name**](a-cn.md)<br/>                                                                                                                                                        |
| Subclass of                 | [**Leaf**](c-leaf.md)<br/>                                                                                                                                                             |
| Possible Superiors          | [**Container**](c-container.md)                                                                                                                                                              |
| Auxiliary Classes           | \-                                                                                                                                                                                            |
| NT-Security-Descriptor      | O:BAG:BAD:S:                                                                                                                                                                                  |
| Default Security Descriptor | D:(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;DA)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;SY)(A;;RPLCLORC;;;AU)(OA;;WP;736e4812-af31-11d2-b7df-00805f48caeb;bf967ab8-0de6-11d0-a285-00aa003049e2;CO)(A;;SD;;;CO) |
| System-Flags                | 0x00000010                                                                                                                                                                                    |



## Windows Server 2003 R2 Attributes

This class contains the following attributes for Windows Server 2003 R2:



| Attribute                                                                   | Mandatory | Derived from                    |
|-----------------------------------------------------------------------------|-----------|---------------------------------|
| [**Additional-Trusted-Service-Names**](a-additionaltrustedservicenames.md) | False     | **Trusted-Domain**              |
| [**Admin-Description**](a-admindescription.md)                             | False     | [**Top**](c-top.md)<br/> |
| [**Admin-Display-Name**](a-admindisplayname.md)                            | False     | [**Top**](c-top.md)<br/> |
| [**Allowed-Attributes**](a-allowedattributes.md)                           | False     | [**Top**](c-top.md)<br/> |
| [**Allowed-Attributes-Effective**](a-allowedattributeseffective.md)        | False     | [**Top**](c-top.md)<br/> |
| [**Allowed-Child-Classes**](a-allowedchildclasses.md)                      | False     | [**Top**](c-top.md)<br/> |
| [**Allowed-Child-Classes-Effective**](a-allowedchildclasseseffective.md)   | False     | [**Top**](c-top.md)<br/> |
| [**Bridgehead-Server-List-BL**](a-bridgeheadserverlistbl.md)               | False     | [**Top**](c-top.md)<br/> |
| [**Canonical-Name**](a-canonicalname.md)                                   | False     | [**Top**](c-top.md)<br/> |
| [**Common-Name**](a-cn.md)                                                 | False     | [**Top**](c-top.md)<br/> |
| [**Create-Time-Stamp**](a-createtimestamp.md)                              | False     | [**Top**](c-top.md)<br/> |
| [**Description**](a-description.md)                                        | False     | [**Top**](c-top.md)<br/> |
| [**Display-Name**](a-displayname.md)                                       | False     | [**Top**](c-top.md)<br/> |
| [**Display-Name-Printable**](a-displaynameprintable.md)                    | False     | [**Top**](c-top.md)<br/> |
| [**Domain-Cross-Ref**](a-domaincrossref.md)                                | False     | **Trusted-Domain**              |
| [**Domain-Identifier**](a-domainidentifier.md)                             | False     | **Trusted-Domain**              |
| [**DSA-Signature**](a-dsasignature.md)                                     | False     | [**Top**](c-top.md)<br/> |
| [**DS-Core-Propagation-Data**](a-dscorepropagationdata.md)                 | False     | [**Top**](c-top.md)<br/> |
| [**Extension-Name**](a-extensionname.md)                                   | False     | [**Top**](c-top.md)<br/> |
| [**Flags**](a-flags.md)                                                    | False     | [**Top**](c-top.md)<br/> |
| [**Flat-Name**](a-flatname.md)                                             | False     | **Trusted-Domain**              |
| [**From-Entry**](a-fromentry.md)                                           | False     | [**Top**](c-top.md)<br/> |
| [**Frs-Computer-Reference-BL**](a-frscomputerreferencebl.md)               | False     | [**Top**](c-top.md)<br/> |
| [**FRS-Member-Reference-BL**](a-frsmemberreferencebl.md)                   | False     | [**Top**](c-top.md)<br/> |
| [**FSMO-Role-Owner**](a-fsmoroleowner.md)                                  | False     | [**Top**](c-top.md)<br/> |
| [**Initial-Auth-Incoming**](a-initialauthincoming.md)                      | False     | **Trusted-Domain**              |
| [**Initial-Auth-Outgoing**](a-initialauthoutgoing.md)                      | False     | **Trusted-Domain**              |
| [**Instance-Type**](a-instancetype.md)                                     | True      | [**Top**](c-top.md)<br/> |
| [**Is-Critical-System-Object**](a-iscriticalsystemobject.md)               | False     | [**Top**](c-top.md)<br/> |
| [**Is-Deleted**](a-isdeleted.md)                                           | False     | [**Top**](c-top.md)<br/> |
| [**Is-Member-Of-DL**](a-memberof.md)                                       | False     | [**Top**](c-top.md)<br/> |
| [**Is-Privilege-Holder**](a-isprivilegeholder.md)                          | False     | [**Top**](c-top.md)<br/> |
| [**Last-Known-Parent**](a-lastknownparent.md)                              | False     | [**Top**](c-top.md)<br/> |
| [**Managed-Objects**](a-managedobjects.md)                                 | False     | [**Top**](c-top.md)<br/> |
| [**Mastered-By**](a-masteredby.md)                                         | False     | [**Top**](c-top.md)<br/> |
| [**Modify-Time-Stamp**](a-modifytimestamp.md)                              | False     | [**Top**](c-top.md)<br/> |
| [**ms-COM-PartitionSetLink**](a-mscom-partitionsetlink.md)                 | False     | [**Top**](c-top.md)<br/> |
| [**ms-COM-UserLink**](a-mscom-userlink.md)                                 | False     | [**Top**](c-top.md)<br/> |
| [**ms-DFSR-ComputerReferenceBL**](a-msdfsr-computerreferencebl.md)         | False     | [**Top**](c-top.md)<br/> |
| [**ms-DFSR-MemberReferenceBL**](a-msdfsr-memberreferencebl.md)             | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Approx-Immed-Subordinates**](a-msds-approx-immed-subordinates.md) | False     | [**Top**](c-top.md)<br/> |
| [**MS-DS-Consistency-Child-Count**](a-ms-ds-consistencychildcount.md)      | False     | [**Top**](c-top.md)<br/> |
| [**MS-DS-Consistency-Guid**](a-ms-ds-consistencyguid.md)                   | False     | [**Top**](c-top.md)<br/> |
| [**MS-DS-Creator-SID**](a-ms-ds-creatorsid.md)                             | False     | **Trusted-Domain**              |
| [**ms-DS-Mastered-By**](a-msds-masteredby.md)                              | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Members-For-Az-Role-BL**](a-msds-membersforazrolebl.md)           | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-NC-Repl-Cursors**](a-msds-ncreplcursors.md)                       | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-NC-Repl-Inbound-Neighbors**](a-msds-ncreplinboundneighbors.md)    | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-NC-Repl-Outbound-Neighbors**](a-msds-ncreploutboundneighbors.md)  | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Non-Members-BL**](a-msds-nonmembersbl.md)                         | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Object-Reference-BL**](a-msds-objectreferencebl.md)               | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Operations-For-Az-Role-BL**](a-msds-operationsforazrolebl.md)     | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Operations-For-Az-Task-BL**](a-msds-operationsforaztaskbl.md)     | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Repl-Attribute-Meta-Data**](a-msds-replattributemetadata.md)      | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Repl-Value-Meta-Data**](a-msds-replvaluemetadata.md)              | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Tasks-For-Az-Role-BL**](a-msds-tasksforazrolebl.md)               | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Tasks-For-Az-Task-BL**](a-msds-tasksforaztaskbl.md)               | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Trust-Forest-Trust-Info**](a-msds-trustforesttrustinfo.md)        | False     | **Trusted-Domain**              |
| [**ms-Exch-Owner-BL**](a-ownerbl.md)                                       | False     | [**Top**](c-top.md)<br/> |
| [**msSFU-30-Posix-Member-Of**](a-mssfu30posixmemberof.md)                  | False     | [**Top**](c-top.md)<br/> |
| [**netboot-SCP-BL**](a-netbootscpbl.md)                                    | False     | [**Top**](c-top.md)<br/> |
| [**Non-Security-Member-BL**](a-nonsecuritymemberbl.md)                     | False     | [**Top**](c-top.md)<br/> |
| [**NT-Security-Descriptor**](a-ntsecuritydescriptor.md)                    | True      | [**Top**](c-top.md)<br/> |
| [**Obj-Dist-Name**](a-distinguishedname.md)                                | False     | [**Top**](c-top.md)<br/> |
| [**Object-Category**](a-objectcategory.md)                                 | True      | [**Top**](c-top.md)<br/> |
| [**Object-Class**](a-objectclass.md)                                       | True      | [**Top**](c-top.md)<br/> |
| [**Object-Guid**](a-objectguid.md)                                         | False     | [**Top**](c-top.md)<br/> |
| [**Object-Version**](a-objectversion.md)                                   | False     | [**Top**](c-top.md)<br/> |
| [**Other-Well-Known-Objects**](a-otherwellknownobjects.md)                 | False     | [**Top**](c-top.md)<br/> |
| [**Partial-Attribute-Deletion-List**](a-partialattributedeletionlist.md)   | False     | [**Top**](c-top.md)<br/> |
| [**Partial-Attribute-Set**](a-partialattributeset.md)                      | False     | [**Top**](c-top.md)<br/> |
| [**Possible-Inferiors**](a-possibleinferiors.md)                           | False     | [**Top**](c-top.md)<br/> |
| [**Proxied-Object-Name**](a-proxiedobjectname.md)                          | False     | [**Top**](c-top.md)<br/> |
| [**Proxy-Addresses**](a-proxyaddresses.md)                                 | False     | [**Top**](c-top.md)<br/> |
| [**Query-Policy-BL**](a-querypolicybl.md)                                  | False     | [**Top**](c-top.md)<br/> |
| [**RDN**](a-name.md)                                                       | False     | [**Top**](c-top.md)<br/> |
| [**Repl-Property-Meta-Data**](a-replpropertymetadata.md)                   | False     | [**Top**](c-top.md)<br/> |
| [**Repl-UpToDate-Vector**](a-repluptodatevector.md)                        | False     | [**Top**](c-top.md)<br/> |
| [**Reports**](a-directreports.md)                                          | False     | [**Top**](c-top.md)<br/> |
| [**Reps-From**](a-repsfrom.md)                                             | False     | [**Top**](c-top.md)<br/> |
| [**Reps-To**](a-repsto.md)                                                 | False     | [**Top**](c-top.md)<br/> |
| [**Revision**](a-revision.md)                                              | False     | [**Top**](c-top.md)<br/> |
| [**SD-Rights-Effective**](a-sdrightseffective.md)                          | False     | [**Top**](c-top.md)<br/> |
| [**Security-Identifier**](a-securityidentifier.md)                         | False     | **Trusted-Domain**              |
| [**Server-Reference-BL**](a-serverreferencebl.md)                          | False     | [**Top**](c-top.md)<br/> |
| [**Show-In-Advanced-View-Only**](a-showinadvancedviewonly.md)              | False     | [**Top**](c-top.md)<br/> |
| [**Site-Object-BL**](a-siteobjectbl.md)                                    | False     | [**Top**](c-top.md)<br/> |
| [**Structural-Object-Class**](a-structuralobjectclass.md)                  | False     | [**Top**](c-top.md)<br/> |
| [**Sub-Refs**](a-subrefs.md)                                               | False     | [**Top**](c-top.md)<br/> |
| [**SubSchemaSubEntry**](a-subschemasubentry.md)                            | False     | [**Top**](c-top.md)<br/> |
| [**System-Flags**](a-systemflags.md)                                       | False     | [**Top**](c-top.md)<br/> |
| [**Trust-Attributes**](a-trustattributes.md)                               | False     | **Trusted-Domain**              |
| [**Trust-Auth-Incoming**](a-trustauthincoming.md)                          | False     | **Trusted-Domain**              |
| [**Trust-Auth-Outgoing**](a-trustauthoutgoing.md)                          | False     | **Trusted-Domain**              |
| [**Trust-Direction**](a-trustdirection.md)                                 | False     | **Trusted-Domain**              |
| [**Trust-Partner**](a-trustpartner.md)                                     | False     | **Trusted-Domain**              |
| [**Trust-Posix-Offset**](a-trustposixoffset.md)                            | False     | **Trusted-Domain**              |
| [**Trust-Type**](a-trusttype.md)                                           | False     | **Trusted-Domain**              |
| [**USN-Changed**](a-usnchanged.md)                                         | False     | [**Top**](c-top.md)<br/> |
| [**USN-Created**](a-usncreated.md)                                         | False     | [**Top**](c-top.md)<br/> |
| [**USN-DSA-Last-Obj-Removed**](a-usndsalastobjremoved.md)                  | False     | [**Top**](c-top.md)<br/> |
| [**USN-Intersite**](a-usnintersite.md)                                     | False     | [**Top**](c-top.md)<br/> |
| [**USN-Last-Obj-Rem**](a-usnlastobjrem.md)                                 | False     | [**Top**](c-top.md)<br/> |
| [**USN-Source**](a-usnsource.md)                                           | False     | [**Top**](c-top.md)<br/> |
| [**Wbem-Path**](a-wbempath.md)                                             | False     | [**Top**](c-top.md)<br/> |
| [**Well-Known-Objects**](a-wellknownobjects.md)                            | False     | [**Top**](c-top.md)<br/> |
| [**When-Changed**](a-whenchanged.md)                                       | False     | [**Top**](c-top.md)<br/> |
| [**When-Created**](a-whencreated.md)                                       | False     | [**Top**](c-top.md)<br/> |
| [**WWW-Home-Page**](a-wwwhomepage.md)                                      | False     | [**Top**](c-top.md)<br/> |
| [**WWW-Page-Other**](a-url.md)                                             | False     | [**Top**](c-top.md)<br/> |



## Windows Server 2008

-   [Attributes](#windows-server-2008-attributes)



| Entry | Value |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| System-Only                 | False                                                                                                                                                                                         |
| Object-Category             | 1                                                                                                                                                                                             |
| Default-Object-Category     | \-                                                                                                                                                                                            |
| Governs-Id                  | 1.2.840.113556.1.5.34                                                                                                                                                                         |
| Default-Hiding-Value        | 1                                                                                                                                                                                             |
| Rdn-Att-Id                  | [**Common-Name**](a-cn.md)<br/>                                                                                                                                                        |
| Subclass of                 | [**Leaf**](c-leaf.md)<br/>                                                                                                                                                             |
| Possible Superiors          | [**Container**](c-container.md)                                                                                                                                                              |
| Auxiliary Classes           | \-                                                                                                                                                                                            |
| NT-Security-Descriptor      | O:BAG:BAD:S:                                                                                                                                                                                  |
| Default Security Descriptor | D:(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;DA)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;SY)(A;;RPLCLORC;;;AU)(OA;;WP;736e4812-af31-11d2-b7df-00805f48caeb;bf967ab8-0de6-11d0-a285-00aa003049e2;CO)(A;;SD;;;CO) |
| System-Flags                | 0x00000010                                                                                                                                                                                    |



## Windows Server 2008 Attributes

This class contains the following attributes for Windows Server 2008:



| Attribute                                                                      | Mandatory | Derived from                    |
|--------------------------------------------------------------------------------|-----------|---------------------------------|
| [**Additional-Trusted-Service-Names**](a-additionaltrustedservicenames.md)    | False     | **Trusted-Domain**              |
| [**Admin-Description**](a-admindescription.md)                                | False     | [**Top**](c-top.md)<br/> |
| [**Admin-Display-Name**](a-admindisplayname.md)                               | False     | [**Top**](c-top.md)<br/> |
| [**Allowed-Attributes**](a-allowedattributes.md)                              | False     | [**Top**](c-top.md)<br/> |
| [**Allowed-Attributes-Effective**](a-allowedattributeseffective.md)           | False     | [**Top**](c-top.md)<br/> |
| [**Allowed-Child-Classes**](a-allowedchildclasses.md)                         | False     | [**Top**](c-top.md)<br/> |
| [**Allowed-Child-Classes-Effective**](a-allowedchildclasseseffective.md)      | False     | [**Top**](c-top.md)<br/> |
| [**Bridgehead-Server-List-BL**](a-bridgeheadserverlistbl.md)                  | False     | [**Top**](c-top.md)<br/> |
| [**Canonical-Name**](a-canonicalname.md)                                      | False     | [**Top**](c-top.md)<br/> |
| [**Common-Name**](a-cn.md)                                                    | False     | [**Top**](c-top.md)<br/> |
| [**Create-Time-Stamp**](a-createtimestamp.md)                                 | False     | [**Top**](c-top.md)<br/> |
| [**Description**](a-description.md)                                           | False     | [**Top**](c-top.md)<br/> |
| [**Display-Name**](a-displayname.md)                                          | False     | [**Top**](c-top.md)<br/> |
| [**Display-Name-Printable**](a-displaynameprintable.md)                       | False     | [**Top**](c-top.md)<br/> |
| [**Domain-Cross-Ref**](a-domaincrossref.md)                                   | False     | **Trusted-Domain**              |
| [**Domain-Identifier**](a-domainidentifier.md)                                | False     | **Trusted-Domain**              |
| [**DSA-Signature**](a-dsasignature.md)                                        | False     | [**Top**](c-top.md)<br/> |
| [**DS-Core-Propagation-Data**](a-dscorepropagationdata.md)                    | False     | [**Top**](c-top.md)<br/> |
| [**Extension-Name**](a-extensionname.md)                                      | False     | [**Top**](c-top.md)<br/> |
| [**Flags**](a-flags.md)                                                       | False     | [**Top**](c-top.md)<br/> |
| [**Flat-Name**](a-flatname.md)                                                | False     | **Trusted-Domain**              |
| [**From-Entry**](a-fromentry.md)                                              | False     | [**Top**](c-top.md)<br/> |
| [**Frs-Computer-Reference-BL**](a-frscomputerreferencebl.md)                  | False     | [**Top**](c-top.md)<br/> |
| [**FRS-Member-Reference-BL**](a-frsmemberreferencebl.md)                      | False     | [**Top**](c-top.md)<br/> |
| [**FSMO-Role-Owner**](a-fsmoroleowner.md)                                     | False     | [**Top**](c-top.md)<br/> |
| [**Initial-Auth-Incoming**](a-initialauthincoming.md)                         | False     | **Trusted-Domain**              |
| [**Initial-Auth-Outgoing**](a-initialauthoutgoing.md)                         | False     | **Trusted-Domain**              |
| [**Instance-Type**](a-instancetype.md)                                        | True      | [**Top**](c-top.md)<br/> |
| [**Is-Critical-System-Object**](a-iscriticalsystemobject.md)                  | False     | [**Top**](c-top.md)<br/> |
| [**Is-Deleted**](a-isdeleted.md)                                              | False     | [**Top**](c-top.md)<br/> |
| [**Is-Member-Of-DL**](a-memberof.md)                                          | False     | [**Top**](c-top.md)<br/> |
| [**Is-Privilege-Holder**](a-isprivilegeholder.md)                             | False     | [**Top**](c-top.md)<br/> |
| [**Last-Known-Parent**](a-lastknownparent.md)                                 | False     | [**Top**](c-top.md)<br/> |
| [**Managed-Objects**](a-managedobjects.md)                                    | False     | [**Top**](c-top.md)<br/> |
| [**Mastered-By**](a-masteredby.md)                                            | False     | [**Top**](c-top.md)<br/> |
| [**Modify-Time-Stamp**](a-modifytimestamp.md)                                 | False     | [**Top**](c-top.md)<br/> |
| [**ms-COM-PartitionSetLink**](a-mscom-partitionsetlink.md)                    | False     | [**Top**](c-top.md)<br/> |
| [**ms-COM-UserLink**](a-mscom-userlink.md)                                    | False     | [**Top**](c-top.md)<br/> |
| [**ms-DFSR-ComputerReferenceBL**](a-msdfsr-computerreferencebl.md)            | False     | [**Top**](c-top.md)<br/> |
| [**ms-DFSR-MemberReferenceBL**](a-msdfsr-memberreferencebl.md)                | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Approx-Immed-Subordinates**](a-msds-approx-immed-subordinates.md)    | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-AuthenticatedTo-Accountlist**](a-msds-authenticatedtoaccountlist.md) | False     | [**Top**](c-top.md)<br/> |
| [**MS-DS-Consistency-Child-Count**](a-ms-ds-consistencychildcount.md)         | False     | [**Top**](c-top.md)<br/> |
| [**MS-DS-Consistency-Guid**](a-ms-ds-consistencyguid.md)                      | False     | [**Top**](c-top.md)<br/> |
| [**MS-DS-Creator-SID**](a-ms-ds-creatorsid.md)                                | False     | **Trusted-Domain**              |
| [**ms-DS-Is-Domain-For**](a-msds-isdomainfor.md)                              | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Is-Full-Replica-For**](a-msds-isfullreplicafor.md)                   | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Is-Partial-Replica-For**](a-msds-ispartialreplicafor.md)             | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-KrbTgt-Link-BL**](a-msds-krbtgtlinkbl.md)                            | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Mastered-By**](a-msds-masteredby.md)                                 | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Members-For-Az-Role-BL**](a-msds-membersforazrolebl.md)              | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-NC-Repl-Cursors**](a-msds-ncreplcursors.md)                          | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-NC-Repl-Inbound-Neighbors**](a-msds-ncreplinboundneighbors.md)       | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-NC-Repl-Outbound-Neighbors**](a-msds-ncreploutboundneighbors.md)     | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-NC-RO-Replica-Locations-BL**](a-msds-nc-ro-replica-locations-bl.md)  | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-NC-Type**](a-msds-nctype.md)                                         | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Non-Members-BL**](a-msds-nonmembersbl.md)                            | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Object-Reference-BL**](a-msds-objectreferencebl.md)                  | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Operations-For-Az-Role-BL**](a-msds-operationsforazrolebl.md)        | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Operations-For-Az-Task-BL**](a-msds-operationsforaztaskbl.md)        | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Principal-Name**](a-msds-principalname.md)                           | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-PSO-Applied**](a-msds-psoapplied.md)                                 | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Repl-Attribute-Meta-Data**](a-msds-replattributemetadata.md)         | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Repl-Value-Meta-Data**](a-msds-replvaluemetadata.md)                 | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Revealed-DSAs**](a-msds-revealeddsas.md)                             | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Revealed-List-BL**](a-msds-revealedlistbl.md)                        | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Supported-Encryption-Types**](a-msds-supportedencryptiontypes.md)    | False     | **Trusted-Domain**              |
| [**ms-DS-Tasks-For-Az-Role-BL**](a-msds-tasksforazrolebl.md)                  | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Tasks-For-Az-Task-BL**](a-msds-tasksforaztaskbl.md)                  | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Trust-Forest-Trust-Info**](a-msds-trustforesttrustinfo.md)           | False     | **Trusted-Domain**              |
| [**ms-Exch-Owner-BL**](a-ownerbl.md)                                          | False     | [**Top**](c-top.md)<br/> |
| [**msSFU-30-Posix-Member-Of**](a-mssfu30posixmemberof.md)                     | False     | [**Top**](c-top.md)<br/> |
| [**netboot-SCP-BL**](a-netbootscpbl.md)                                       | False     | [**Top**](c-top.md)<br/> |
| [**Non-Security-Member-BL**](a-nonsecuritymemberbl.md)                        | False     | [**Top**](c-top.md)<br/> |
| [**NT-Security-Descriptor**](a-ntsecuritydescriptor.md)                       | True      | [**Top**](c-top.md)<br/> |
| [**Obj-Dist-Name**](a-distinguishedname.md)                                   | False     | [**Top**](c-top.md)<br/> |
| [**Object-Category**](a-objectcategory.md)                                    | True      | [**Top**](c-top.md)<br/> |
| [**Object-Class**](a-objectclass.md)                                          | True      | [**Top**](c-top.md)<br/> |
| [**Object-Guid**](a-objectguid.md)                                            | False     | [**Top**](c-top.md)<br/> |
| [**Object-Version**](a-objectversion.md)                                      | False     | [**Top**](c-top.md)<br/> |
| [**Other-Well-Known-Objects**](a-otherwellknownobjects.md)                    | False     | [**Top**](c-top.md)<br/> |
| [**Partial-Attribute-Deletion-List**](a-partialattributedeletionlist.md)      | False     | [**Top**](c-top.md)<br/> |
| [**Partial-Attribute-Set**](a-partialattributeset.md)                         | False     | [**Top**](c-top.md)<br/> |
| [**Possible-Inferiors**](a-possibleinferiors.md)                              | False     | [**Top**](c-top.md)<br/> |
| [**Proxied-Object-Name**](a-proxiedobjectname.md)                             | False     | [**Top**](c-top.md)<br/> |
| [**Proxy-Addresses**](a-proxyaddresses.md)                                    | False     | [**Top**](c-top.md)<br/> |
| [**Query-Policy-BL**](a-querypolicybl.md)                                     | False     | [**Top**](c-top.md)<br/> |
| [**RDN**](a-name.md)                                                          | False     | [**Top**](c-top.md)<br/> |
| [**Repl-Property-Meta-Data**](a-replpropertymetadata.md)                      | False     | [**Top**](c-top.md)<br/> |
| [**Repl-UpToDate-Vector**](a-repluptodatevector.md)                           | False     | [**Top**](c-top.md)<br/> |
| [**Reports**](a-directreports.md)                                             | False     | [**Top**](c-top.md)<br/> |
| [**Reps-From**](a-repsfrom.md)                                                | False     | [**Top**](c-top.md)<br/> |
| [**Reps-To**](a-repsto.md)                                                    | False     | [**Top**](c-top.md)<br/> |
| [**Revision**](a-revision.md)                                                 | False     | [**Top**](c-top.md)<br/> |
| [**SD-Rights-Effective**](a-sdrightseffective.md)                             | False     | [**Top**](c-top.md)<br/> |
| [**Security-Identifier**](a-securityidentifier.md)                            | False     | **Trusted-Domain**              |
| [**Server-Reference-BL**](a-serverreferencebl.md)                             | False     | [**Top**](c-top.md)<br/> |
| [**Show-In-Advanced-View-Only**](a-showinadvancedviewonly.md)                 | False     | [**Top**](c-top.md)<br/> |
| [**Site-Object-BL**](a-siteobjectbl.md)                                       | False     | [**Top**](c-top.md)<br/> |
| [**Structural-Object-Class**](a-structuralobjectclass.md)                     | False     | [**Top**](c-top.md)<br/> |
| [**Sub-Refs**](a-subrefs.md)                                                  | False     | [**Top**](c-top.md)<br/> |
| [**SubSchemaSubEntry**](a-subschemasubentry.md)                               | False     | [**Top**](c-top.md)<br/> |
| [**System-Flags**](a-systemflags.md)                                          | False     | [**Top**](c-top.md)<br/> |
| [**Trust-Attributes**](a-trustattributes.md)                                  | False     | **Trusted-Domain**              |
| [**Trust-Auth-Incoming**](a-trustauthincoming.md)                             | False     | **Trusted-Domain**              |
| [**Trust-Auth-Outgoing**](a-trustauthoutgoing.md)                             | False     | **Trusted-Domain**              |
| [**Trust-Direction**](a-trustdirection.md)                                    | False     | **Trusted-Domain**              |
| [**Trust-Partner**](a-trustpartner.md)                                        | False     | **Trusted-Domain**              |
| [**Trust-Posix-Offset**](a-trustposixoffset.md)                               | False     | **Trusted-Domain**              |
| [**Trust-Type**](a-trusttype.md)                                              | False     | **Trusted-Domain**              |
| [**USN-Changed**](a-usnchanged.md)                                            | False     | [**Top**](c-top.md)<br/> |
| [**USN-Created**](a-usncreated.md)                                            | False     | [**Top**](c-top.md)<br/> |
| [**USN-DSA-Last-Obj-Removed**](a-usndsalastobjremoved.md)                     | False     | [**Top**](c-top.md)<br/> |
| [**USN-Intersite**](a-usnintersite.md)                                        | False     | [**Top**](c-top.md)<br/> |
| [**USN-Last-Obj-Rem**](a-usnlastobjrem.md)                                    | False     | [**Top**](c-top.md)<br/> |
| [**USN-Source**](a-usnsource.md)                                              | False     | [**Top**](c-top.md)<br/> |
| [**Wbem-Path**](a-wbempath.md)                                                | False     | [**Top**](c-top.md)<br/> |
| [**Well-Known-Objects**](a-wellknownobjects.md)                               | False     | [**Top**](c-top.md)<br/> |
| [**When-Changed**](a-whenchanged.md)                                          | False     | [**Top**](c-top.md)<br/> |
| [**When-Created**](a-whencreated.md)                                          | False     | [**Top**](c-top.md)<br/> |
| [**WWW-Home-Page**](a-wwwhomepage.md)                                         | False     | [**Top**](c-top.md)<br/> |
| [**WWW-Page-Other**](a-url.md)                                                | False     | [**Top**](c-top.md)<br/> |



## Windows Server 2008 R2

-   [Attributes](#windows-server-2008-r2-attributes)



| Entry | Value |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| System-Only                 | False                                                                                                                                                                                         |
| Object-Category             | 1                                                                                                                                                                                             |
| Default-Object-Category     | \-                                                                                                                                                                                            |
| Governs-Id                  | 1.2.840.113556.1.5.34                                                                                                                                                                         |
| Default-Hiding-Value        | 1                                                                                                                                                                                             |
| Rdn-Att-Id                  | [**Common-Name**](a-cn.md)<br/>                                                                                                                                                        |
| Subclass of                 | [**Leaf**](c-leaf.md)<br/>                                                                                                                                                             |
| Possible Superiors          | [**Container**](c-container.md)                                                                                                                                                              |
| Auxiliary Classes           | \-                                                                                                                                                                                            |
| NT-Security-Descriptor      | O:BAG:BAD:S:                                                                                                                                                                                  |
| Default Security Descriptor | D:(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;DA)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;SY)(A;;RPLCLORC;;;AU)(OA;;WP;736e4812-af31-11d2-b7df-00805f48caeb;bf967ab8-0de6-11d0-a285-00aa003049e2;CO)(A;;SD;;;CO) |
| System-Flags                | 0x00000010                                                                                                                                                                                    |



## Windows Server 2008 R2 Attributes

This class contains the following attributes for Windows Server 2008 R2:



| Attribute                                                                        | Mandatory | Derived from                    |
|----------------------------------------------------------------------------------|-----------|---------------------------------|
| [**Additional-Trusted-Service-Names**](a-additionaltrustedservicenames.md)      | False     | **Trusted-Domain**              |
| [**Admin-Description**](a-admindescription.md)                                  | False     | [**Top**](c-top.md)<br/> |
| [**Admin-Display-Name**](a-admindisplayname.md)                                 | False     | [**Top**](c-top.md)<br/> |
| [**Allowed-Attributes**](a-allowedattributes.md)                                | False     | [**Top**](c-top.md)<br/> |
| [**Allowed-Attributes-Effective**](a-allowedattributeseffective.md)             | False     | [**Top**](c-top.md)<br/> |
| [**Allowed-Child-Classes**](a-allowedchildclasses.md)                           | False     | [**Top**](c-top.md)<br/> |
| [**Allowed-Child-Classes-Effective**](a-allowedchildclasseseffective.md)        | False     | [**Top**](c-top.md)<br/> |
| [**Bridgehead-Server-List-BL**](a-bridgeheadserverlistbl.md)                    | False     | [**Top**](c-top.md)<br/> |
| [**Canonical-Name**](a-canonicalname.md)                                        | False     | [**Top**](c-top.md)<br/> |
| [**Common-Name**](a-cn.md)                                                      | False     | [**Top**](c-top.md)<br/> |
| [**Create-Time-Stamp**](a-createtimestamp.md)                                   | False     | [**Top**](c-top.md)<br/> |
| [**Description**](a-description.md)                                             | False     | [**Top**](c-top.md)<br/> |
| [**Display-Name**](a-displayname.md)                                            | False     | [**Top**](c-top.md)<br/> |
| [**Display-Name-Printable**](a-displaynameprintable.md)                         | False     | [**Top**](c-top.md)<br/> |
| [**Domain-Cross-Ref**](a-domaincrossref.md)                                     | False     | **Trusted-Domain**              |
| [**Domain-Identifier**](a-domainidentifier.md)                                  | False     | **Trusted-Domain**              |
| [**DSA-Signature**](a-dsasignature.md)                                          | False     | [**Top**](c-top.md)<br/> |
| [**DS-Core-Propagation-Data**](a-dscorepropagationdata.md)                      | False     | [**Top**](c-top.md)<br/> |
| [**Extension-Name**](a-extensionname.md)                                        | False     | [**Top**](c-top.md)<br/> |
| [**Flags**](a-flags.md)                                                         | False     | [**Top**](c-top.md)<br/> |
| [**Flat-Name**](a-flatname.md)                                                  | False     | **Trusted-Domain**              |
| [**From-Entry**](a-fromentry.md)                                                | False     | [**Top**](c-top.md)<br/> |
| [**Frs-Computer-Reference-BL**](a-frscomputerreferencebl.md)                    | False     | [**Top**](c-top.md)<br/> |
| [**FRS-Member-Reference-BL**](a-frsmemberreferencebl.md)                        | False     | [**Top**](c-top.md)<br/> |
| [**FSMO-Role-Owner**](a-fsmoroleowner.md)                                       | False     | [**Top**](c-top.md)<br/> |
| [**Initial-Auth-Incoming**](a-initialauthincoming.md)                           | False     | **Trusted-Domain**              |
| [**Initial-Auth-Outgoing**](a-initialauthoutgoing.md)                           | False     | **Trusted-Domain**              |
| [**Instance-Type**](a-instancetype.md)                                          | True      | [**Top**](c-top.md)<br/> |
| [**Is-Critical-System-Object**](a-iscriticalsystemobject.md)                    | False     | [**Top**](c-top.md)<br/> |
| [**Is-Deleted**](a-isdeleted.md)                                                | False     | [**Top**](c-top.md)<br/> |
| [**Is-Member-Of-DL**](a-memberof.md)                                            | False     | [**Top**](c-top.md)<br/> |
| [**Is-Privilege-Holder**](a-isprivilegeholder.md)                               | False     | [**Top**](c-top.md)<br/> |
| [**Is-Recycled**](a-isrecycled.md)                                              | False     | [**Top**](c-top.md)<br/> |
| [**Last-Known-Parent**](a-lastknownparent.md)                                   | False     | [**Top**](c-top.md)<br/> |
| [**Managed-Objects**](a-managedobjects.md)                                      | False     | [**Top**](c-top.md)<br/> |
| [**Mastered-By**](a-masteredby.md)                                              | False     | [**Top**](c-top.md)<br/> |
| [**Modify-Time-Stamp**](a-modifytimestamp.md)                                   | False     | [**Top**](c-top.md)<br/> |
| [**ms-COM-PartitionSetLink**](a-mscom-partitionsetlink.md)                      | False     | [**Top**](c-top.md)<br/> |
| [**ms-COM-UserLink**](a-mscom-userlink.md)                                      | False     | [**Top**](c-top.md)<br/> |
| [**ms-DFSR-ComputerReferenceBL**](a-msdfsr-computerreferencebl.md)              | False     | [**Top**](c-top.md)<br/> |
| [**ms-DFSR-MemberReferenceBL**](a-msdfsr-memberreferencebl.md)                  | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Approx-Immed-Subordinates**](a-msds-approx-immed-subordinates.md)      | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-AuthenticatedTo-Accountlist**](a-msds-authenticatedtoaccountlist.md)   | False     | [**Top**](c-top.md)<br/> |
| [**MS-DS-Consistency-Child-Count**](a-ms-ds-consistencychildcount.md)           | False     | [**Top**](c-top.md)<br/> |
| [**MS-DS-Consistency-Guid**](a-ms-ds-consistencyguid.md)                        | False     | [**Top**](c-top.md)<br/> |
| [**MS-DS-Creator-SID**](a-ms-ds-creatorsid.md)                                  | False     | **Trusted-Domain**              |
| [**ms-DS-Enabled-Feature-BL**](a-msds-enabledfeaturebl.md)                      | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Host-Service-Account-BL**](a-msds-hostserviceaccountbl.md)             | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Is-Domain-For**](a-msds-isdomainfor.md)                                | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Is-Full-Replica-For**](a-msds-isfullreplicafor.md)                     | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Is-Partial-Replica-For**](a-msds-ispartialreplicafor.md)               | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-KrbTgt-Link-BL**](a-msds-krbtgtlinkbl.md)                              | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Last-Known-RDN**](a-msds-lastknownrdn.md)                              | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-local-Effective-Deletion-Time**](a-msds-localeffectivedeletiontime.md) | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-local-Effective-Recycle-Time**](a-msds-localeffectiverecycletime.md)   | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Mastered-By**](a-msds-masteredby.md)                                   | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Members-For-Az-Role-BL**](a-msds-membersforazrolebl.md)                | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-NC-Repl-Cursors**](a-msds-ncreplcursors.md)                            | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-NC-Repl-Inbound-Neighbors**](a-msds-ncreplinboundneighbors.md)         | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-NC-Repl-Outbound-Neighbors**](a-msds-ncreploutboundneighbors.md)       | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-NC-RO-Replica-Locations-BL**](a-msds-nc-ro-replica-locations-bl.md)    | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-NC-Type**](a-msds-nctype.md)                                           | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Non-Members-BL**](a-msds-nonmembersbl.md)                              | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Object-Reference-BL**](a-msds-objectreferencebl.md)                    | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-OIDToGroup-Link-BL**](a-msds-oidtogrouplinkbl.md)                      | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Operations-For-Az-Role-BL**](a-msds-operationsforazrolebl.md)          | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Operations-For-Az-Task-BL**](a-msds-operationsforaztaskbl.md)          | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Principal-Name**](a-msds-principalname.md)                             | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-PSO-Applied**](a-msds-psoapplied.md)                                   | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Repl-Attribute-Meta-Data**](a-msds-replattributemetadata.md)           | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Repl-Value-Meta-Data**](a-msds-replvaluemetadata.md)                   | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Revealed-DSAs**](a-msds-revealeddsas.md)                               | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Revealed-List-BL**](a-msds-revealedlistbl.md)                          | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Supported-Encryption-Types**](a-msds-supportedencryptiontypes.md)      | False     | **Trusted-Domain**              |
| [**ms-DS-Tasks-For-Az-Role-BL**](a-msds-tasksforazrolebl.md)                    | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Tasks-For-Az-Task-BL**](a-msds-tasksforaztaskbl.md)                    | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Trust-Forest-Trust-Info**](a-msds-trustforesttrustinfo.md)             | False     | **Trusted-Domain**              |
| [**ms-Exch-Owner-BL**](a-ownerbl.md)                                            | False     | [**Top**](c-top.md)<br/> |
| [**msSFU-30-Posix-Member-Of**](a-mssfu30posixmemberof.md)                       | False     | [**Top**](c-top.md)<br/> |
| [**netboot-SCP-BL**](a-netbootscpbl.md)                                         | False     | [**Top**](c-top.md)<br/> |
| [**Non-Security-Member-BL**](a-nonsecuritymemberbl.md)                          | False     | [**Top**](c-top.md)<br/> |
| [**NT-Security-Descriptor**](a-ntsecuritydescriptor.md)                         | True      | [**Top**](c-top.md)<br/> |
| [**Obj-Dist-Name**](a-distinguishedname.md)                                     | False     | [**Top**](c-top.md)<br/> |
| [**Object-Category**](a-objectcategory.md)                                      | True      | [**Top**](c-top.md)<br/> |
| [**Object-Class**](a-objectclass.md)                                            | True      | [**Top**](c-top.md)<br/> |
| [**Object-Guid**](a-objectguid.md)                                              | False     | [**Top**](c-top.md)<br/> |
| [**Object-Version**](a-objectversion.md)                                        | False     | [**Top**](c-top.md)<br/> |
| [**Other-Well-Known-Objects**](a-otherwellknownobjects.md)                      | False     | [**Top**](c-top.md)<br/> |
| [**Partial-Attribute-Deletion-List**](a-partialattributedeletionlist.md)        | False     | [**Top**](c-top.md)<br/> |
| [**Partial-Attribute-Set**](a-partialattributeset.md)                           | False     | [**Top**](c-top.md)<br/> |
| [**Possible-Inferiors**](a-possibleinferiors.md)                                | False     | [**Top**](c-top.md)<br/> |
| [**Proxied-Object-Name**](a-proxiedobjectname.md)                               | False     | [**Top**](c-top.md)<br/> |
| [**Proxy-Addresses**](a-proxyaddresses.md)                                      | False     | [**Top**](c-top.md)<br/> |
| [**Query-Policy-BL**](a-querypolicybl.md)                                       | False     | [**Top**](c-top.md)<br/> |
| [**RDN**](a-name.md)                                                            | False     | [**Top**](c-top.md)<br/> |
| [**Repl-Property-Meta-Data**](a-replpropertymetadata.md)                        | False     | [**Top**](c-top.md)<br/> |
| [**Repl-UpToDate-Vector**](a-repluptodatevector.md)                             | False     | [**Top**](c-top.md)<br/> |
| [**Reports**](a-directreports.md)                                               | False     | [**Top**](c-top.md)<br/> |
| [**Reps-From**](a-repsfrom.md)                                                  | False     | [**Top**](c-top.md)<br/> |
| [**Reps-To**](a-repsto.md)                                                      | False     | [**Top**](c-top.md)<br/> |
| [**Revision**](a-revision.md)                                                   | False     | [**Top**](c-top.md)<br/> |
| [**SD-Rights-Effective**](a-sdrightseffective.md)                               | False     | [**Top**](c-top.md)<br/> |
| [**Security-Identifier**](a-securityidentifier.md)                              | False     | **Trusted-Domain**              |
| [**Server-Reference-BL**](a-serverreferencebl.md)                               | False     | [**Top**](c-top.md)<br/> |
| [**Show-In-Advanced-View-Only**](a-showinadvancedviewonly.md)                   | False     | [**Top**](c-top.md)<br/> |
| [**Site-Object-BL**](a-siteobjectbl.md)                                         | False     | [**Top**](c-top.md)<br/> |
| [**Structural-Object-Class**](a-structuralobjectclass.md)                       | False     | [**Top**](c-top.md)<br/> |
| [**Sub-Refs**](a-subrefs.md)                                                    | False     | [**Top**](c-top.md)<br/> |
| [**SubSchemaSubEntry**](a-subschemasubentry.md)                                 | False     | [**Top**](c-top.md)<br/> |
| [**System-Flags**](a-systemflags.md)                                            | False     | [**Top**](c-top.md)<br/> |
| [**Trust-Attributes**](a-trustattributes.md)                                    | False     | **Trusted-Domain**              |
| [**Trust-Auth-Incoming**](a-trustauthincoming.md)                               | False     | **Trusted-Domain**              |
| [**Trust-Auth-Outgoing**](a-trustauthoutgoing.md)                               | False     | **Trusted-Domain**              |
| [**Trust-Direction**](a-trustdirection.md)                                      | False     | **Trusted-Domain**              |
| [**Trust-Partner**](a-trustpartner.md)                                          | False     | **Trusted-Domain**              |
| [**Trust-Posix-Offset**](a-trustposixoffset.md)                                 | False     | **Trusted-Domain**              |
| [**Trust-Type**](a-trusttype.md)                                                | False     | **Trusted-Domain**              |
| [**USN-Changed**](a-usnchanged.md)                                              | False     | [**Top**](c-top.md)<br/> |
| [**USN-Created**](a-usncreated.md)                                              | False     | [**Top**](c-top.md)<br/> |
| [**USN-DSA-Last-Obj-Removed**](a-usndsalastobjremoved.md)                       | False     | [**Top**](c-top.md)<br/> |
| [**USN-Intersite**](a-usnintersite.md)                                          | False     | [**Top**](c-top.md)<br/> |
| [**USN-Last-Obj-Rem**](a-usnlastobjrem.md)                                      | False     | [**Top**](c-top.md)<br/> |
| [**USN-Source**](a-usnsource.md)                                                | False     | [**Top**](c-top.md)<br/> |
| [**Wbem-Path**](a-wbempath.md)                                                  | False     | [**Top**](c-top.md)<br/> |
| [**Well-Known-Objects**](a-wellknownobjects.md)                                 | False     | [**Top**](c-top.md)<br/> |
| [**When-Changed**](a-whenchanged.md)                                            | False     | [**Top**](c-top.md)<br/> |
| [**When-Created**](a-whencreated.md)                                            | False     | [**Top**](c-top.md)<br/> |
| [**WWW-Home-Page**](a-wwwhomepage.md)                                           | False     | [**Top**](c-top.md)<br/> |
| [**WWW-Page-Other**](a-url.md)                                                  | False     | [**Top**](c-top.md)<br/> |



## Windows Server 2012

-   [Attributes](#windows-server-2012-attributes)



| Entry | Value |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| System-Only                 | False                                                                                                                                                                                         |
| Object-Category             | 1                                                                                                                                                                                             |
| Default-Object-Category     | \-                                                                                                                                                                                            |
| Governs-Id                  | 1.2.840.113556.1.5.34                                                                                                                                                                         |
| Default-Hiding-Value        | 1                                                                                                                                                                                             |
| Rdn-Att-Id                  | [**Common-Name**](a-cn.md)<br/>                                                                                                                                                        |
| Subclass of                 | [**Leaf**](c-leaf.md)<br/>                                                                                                                                                             |
| Possible Superiors          | [**Container**](c-container.md)                                                                                                                                                              |
| Auxiliary Classes           | \-                                                                                                                                                                                            |
| NT-Security-Descriptor      | O:BAG:BAD:S:                                                                                                                                                                                  |
| Default Security Descriptor | D:(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;DA)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;SY)(A;;RPLCLORC;;;AU)(OA;;WP;736e4812-af31-11d2-b7df-00805f48caeb;bf967ab8-0de6-11d0-a285-00aa003049e2;CO)(A;;SD;;;CO) |
| System-Flags                | 0x00000010                                                                                                                                                                                    |



## Windows Server 2012 Attributes

This class contains the following attributes for Windows Server 2012:



| Attribute                                                                                      | Mandatory | Derived from                    |
|------------------------------------------------------------------------------------------------|-----------|---------------------------------|
| [**Additional-Trusted-Service-Names**](a-additionaltrustedservicenames.md)                    | False     | **Trusted-Domain**              |
| [**Admin-Description**](a-admindescription.md)                                                | False     | [**Top**](c-top.md)<br/> |
| [**Admin-Display-Name**](a-admindisplayname.md)                                               | False     | [**Top**](c-top.md)<br/> |
| [**Allowed-Attributes**](a-allowedattributes.md)                                              | False     | [**Top**](c-top.md)<br/> |
| [**Allowed-Attributes-Effective**](a-allowedattributeseffective.md)                           | False     | [**Top**](c-top.md)<br/> |
| [**Allowed-Child-Classes**](a-allowedchildclasses.md)                                         | False     | [**Top**](c-top.md)<br/> |
| [**Allowed-Child-Classes-Effective**](a-allowedchildclasseseffective.md)                      | False     | [**Top**](c-top.md)<br/> |
| [**Bridgehead-Server-List-BL**](a-bridgeheadserverlistbl.md)                                  | False     | [**Top**](c-top.md)<br/> |
| [**Canonical-Name**](a-canonicalname.md)                                                      | False     | [**Top**](c-top.md)<br/> |
| [**Common-Name**](a-cn.md)                                                                    | False     | [**Top**](c-top.md)<br/> |
| [**Create-Time-Stamp**](a-createtimestamp.md)                                                 | False     | [**Top**](c-top.md)<br/> |
| [**Description**](a-description.md)                                                           | False     | [**Top**](c-top.md)<br/> |
| [**Display-Name**](a-displayname.md)                                                          | False     | [**Top**](c-top.md)<br/> |
| [**Display-Name-Printable**](a-displaynameprintable.md)                                       | False     | [**Top**](c-top.md)<br/> |
| [**Domain-Cross-Ref**](a-domaincrossref.md)                                                   | False     | **Trusted-Domain**              |
| [**Domain-Identifier**](a-domainidentifier.md)                                                | False     | **Trusted-Domain**              |
| [**DSA-Signature**](a-dsasignature.md)                                                        | False     | [**Top**](c-top.md)<br/> |
| [**DS-Core-Propagation-Data**](a-dscorepropagationdata.md)                                    | False     | [**Top**](c-top.md)<br/> |
| [**Extension-Name**](a-extensionname.md)                                                      | False     | [**Top**](c-top.md)<br/> |
| [**Flags**](a-flags.md)                                                                       | False     | [**Top**](c-top.md)<br/> |
| [**Flat-Name**](a-flatname.md)                                                                | False     | **Trusted-Domain**              |
| [**From-Entry**](a-fromentry.md)                                                              | False     | [**Top**](c-top.md)<br/> |
| [**Frs-Computer-Reference-BL**](a-frscomputerreferencebl.md)                                  | False     | [**Top**](c-top.md)<br/> |
| [**FRS-Member-Reference-BL**](a-frsmemberreferencebl.md)                                      | False     | [**Top**](c-top.md)<br/> |
| [**FSMO-Role-Owner**](a-fsmoroleowner.md)                                                     | False     | [**Top**](c-top.md)<br/> |
| [**Initial-Auth-Incoming**](a-initialauthincoming.md)                                         | False     | **Trusted-Domain**              |
| [**Initial-Auth-Outgoing**](a-initialauthoutgoing.md)                                         | False     | **Trusted-Domain**              |
| [**Instance-Type**](a-instancetype.md)                                                        | True      | [**Top**](c-top.md)<br/> |
| [**Is-Critical-System-Object**](a-iscriticalsystemobject.md)                                  | False     | [**Top**](c-top.md)<br/> |
| [**Is-Deleted**](a-isdeleted.md)                                                              | False     | [**Top**](c-top.md)<br/> |
| [**Is-Member-Of-DL**](a-memberof.md)                                                          | False     | [**Top**](c-top.md)<br/> |
| [**Is-Privilege-Holder**](a-isprivilegeholder.md)                                             | False     | [**Top**](c-top.md)<br/> |
| [**Is-Recycled**](a-isrecycled.md)                                                            | False     | [**Top**](c-top.md)<br/> |
| [**Last-Known-Parent**](a-lastknownparent.md)                                                 | False     | [**Top**](c-top.md)<br/> |
| [**Managed-Objects**](a-managedobjects.md)                                                    | False     | [**Top**](c-top.md)<br/> |
| [**Mastered-By**](a-masteredby.md)                                                            | False     | [**Top**](c-top.md)<br/> |
| [**Modify-Time-Stamp**](a-modifytimestamp.md)                                                 | False     | [**Top**](c-top.md)<br/> |
| [**ms-COM-PartitionSetLink**](a-mscom-partitionsetlink.md)                                    | False     | [**Top**](c-top.md)<br/> |
| [**ms-COM-UserLink**](a-mscom-userlink.md)                                                    | False     | [**Top**](c-top.md)<br/> |
| [**ms-DFSR-ComputerReferenceBL**](a-msdfsr-computerreferencebl.md)                            | False     | [**Top**](c-top.md)<br/> |
| [**ms-DFSR-MemberReferenceBL**](a-msdfsr-memberreferencebl.md)                                | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Approx-Immed-Subordinates**](a-msds-approx-immed-subordinates.md)                    | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-AuthenticatedTo-Accountlist**](a-msds-authenticatedtoaccountlist.md)                 | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Claim-Shares-Possible-Values-With-BL**](a-msds-claimsharespossiblevalueswithbl.md)   | False     | [**Top**](c-top.md)<br/> |
| [**MS-DS-Consistency-Child-Count**](a-ms-ds-consistencychildcount.md)                         | False     | [**Top**](c-top.md)<br/> |
| [**MS-DS-Consistency-Guid**](a-ms-ds-consistencyguid.md)                                      | False     | [**Top**](c-top.md)<br/> |
| [**MS-DS-Creator-SID**](a-ms-ds-creatorsid.md)                                                | False     | **Trusted-Domain**              |
| [**ms-DS-Egress-Claims-Transformation-Policy**](a-msds-egressclaimstransformationpolicy.md)   | False     | **Trusted-Domain**              |
| [**ms-DS-Enabled-Feature-BL**](a-msds-enabledfeaturebl.md)                                    | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Host-Service-Account-BL**](a-msds-hostserviceaccountbl.md)                           | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Ingress-Claims-Transformation-Policy**](a-msds-ingressclaimstransformationpolicy.md) | False     | **Trusted-Domain**              |
| [**ms-DS-Is-Domain-For**](a-msds-isdomainfor.md)                                              | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Is-Full-Replica-For**](a-msds-isfullreplicafor.md)                                   | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Is-Partial-Replica-For**](a-msds-ispartialreplicafor.md)                             | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Is-Primary-Computer-For**](a-msds-isprimarycomputerfor.md)                           | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-KrbTgt-Link-BL**](a-msds-krbtgtlinkbl.md)                                            | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Last-Known-RDN**](a-msds-lastknownrdn.md)                                            | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-local-Effective-Deletion-Time**](a-msds-localeffectivedeletiontime.md)               | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-local-Effective-Recycle-Time**](a-msds-localeffectiverecycletime.md)                 | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Mastered-By**](a-msds-masteredby.md)                                                 | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Members-For-Az-Role-BL**](a-msds-membersforazrolebl.md)                              | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Members-Of-Resource-Property-List-BL**](a-msds-membersofresourcepropertylistbl.md)   | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-NC-Repl-Cursors**](a-msds-ncreplcursors.md)                                          | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-NC-Repl-Inbound-Neighbors**](a-msds-ncreplinboundneighbors.md)                       | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-NC-Repl-Outbound-Neighbors**](a-msds-ncreploutboundneighbors.md)                     | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-NC-RO-Replica-Locations-BL**](a-msds-nc-ro-replica-locations-bl.md)                  | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-NC-Type**](a-msds-nctype.md)                                                         | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Non-Members-BL**](a-msds-nonmembersbl.md)                                            | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Object-Reference-BL**](a-msds-objectreferencebl.md)                                  | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-OIDToGroup-Link-BL**](a-msds-oidtogrouplinkbl.md)                                    | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Operations-For-Az-Role-BL**](a-msds-operationsforazrolebl.md)                        | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Operations-For-Az-Task-BL**](a-msds-operationsforaztaskbl.md)                        | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Principal-Name**](a-msds-principalname.md)                                           | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-PSO-Applied**](a-msds-psoapplied.md)                                                 | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Repl-Attribute-Meta-Data**](a-msds-replattributemetadata.md)                         | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Repl-Value-Meta-Data**](a-msds-replvaluemetadata.md)                                 | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Revealed-DSAs**](a-msds-revealeddsas.md)                                             | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Revealed-List-BL**](a-msds-revealedlistbl.md)                                        | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Supported-Encryption-Types**](a-msds-supportedencryptiontypes.md)                    | False     | **Trusted-Domain**              |
| [**ms-DS-Tasks-For-Az-Role-BL**](a-msds-tasksforazrolebl.md)                                  | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Tasks-For-Az-Task-BL**](a-msds-tasksforaztaskbl.md)                                  | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-TDO-Egress-BL**](a-msds-tdoegressbl.md)                                              | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-TDO-Ingress-BL**](a-msds-tdoingressbl.md)                                            | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Trust-Forest-Trust-Info**](a-msds-trustforesttrustinfo.md)                           | False     | **Trusted-Domain**              |
| [**ms-DS-Value-Type-Reference-BL**](a-msds-valuetypereferencebl.md)                           | False     | [**Top**](c-top.md)<br/> |
| [**ms-Exch-Owner-BL**](a-ownerbl.md)                                                          | False     | [**Top**](c-top.md)<br/> |
| [**msSFU-30-Posix-Member-Of**](a-mssfu30posixmemberof.md)                                     | False     | [**Top**](c-top.md)<br/> |
| [**netboot-SCP-BL**](a-netbootscpbl.md)                                                       | False     | [**Top**](c-top.md)<br/> |
| [**Non-Security-Member-BL**](a-nonsecuritymemberbl.md)                                        | False     | [**Top**](c-top.md)<br/> |
| [**NT-Security-Descriptor**](a-ntsecuritydescriptor.md)                                       | True      | [**Top**](c-top.md)<br/> |
| [**Obj-Dist-Name**](a-distinguishedname.md)                                                   | False     | [**Top**](c-top.md)<br/> |
| [**Object-Category**](a-objectcategory.md)                                                    | True      | [**Top**](c-top.md)<br/> |
| [**Object-Class**](a-objectclass.md)                                                          | True      | [**Top**](c-top.md)<br/> |
| [**Object-Guid**](a-objectguid.md)                                                            | False     | [**Top**](c-top.md)<br/> |
| [**Object-Version**](a-objectversion.md)                                                      | False     | [**Top**](c-top.md)<br/> |
| [**Other-Well-Known-Objects**](a-otherwellknownobjects.md)                                    | False     | [**Top**](c-top.md)<br/> |
| [**Partial-Attribute-Deletion-List**](a-partialattributedeletionlist.md)                      | False     | [**Top**](c-top.md)<br/> |
| [**Partial-Attribute-Set**](a-partialattributeset.md)                                         | False     | [**Top**](c-top.md)<br/> |
| [**Possible-Inferiors**](a-possibleinferiors.md)                                              | False     | [**Top**](c-top.md)<br/> |
| [**Proxied-Object-Name**](a-proxiedobjectname.md)                                             | False     | [**Top**](c-top.md)<br/> |
| [**Proxy-Addresses**](a-proxyaddresses.md)                                                    | False     | [**Top**](c-top.md)<br/> |
| [**Query-Policy-BL**](a-querypolicybl.md)                                                     | False     | [**Top**](c-top.md)<br/> |
| [**RDN**](a-name.md)                                                                          | False     | [**Top**](c-top.md)<br/> |
| [**Repl-Property-Meta-Data**](a-replpropertymetadata.md)                                      | False     | [**Top**](c-top.md)<br/> |
| [**Repl-UpToDate-Vector**](a-repluptodatevector.md)                                           | False     | [**Top**](c-top.md)<br/> |
| [**Reports**](a-directreports.md)                                                             | False     | [**Top**](c-top.md)<br/> |
| [**Reps-From**](a-repsfrom.md)                                                                | False     | [**Top**](c-top.md)<br/> |
| [**Reps-To**](a-repsto.md)                                                                    | False     | [**Top**](c-top.md)<br/> |
| [**Revision**](a-revision.md)                                                                 | False     | [**Top**](c-top.md)<br/> |
| [**SD-Rights-Effective**](a-sdrightseffective.md)                                             | False     | [**Top**](c-top.md)<br/> |
| [**Security-Identifier**](a-securityidentifier.md)                                            | False     | **Trusted-Domain**              |
| [**Server-Reference-BL**](a-serverreferencebl.md)                                             | False     | [**Top**](c-top.md)<br/> |
| [**Show-In-Advanced-View-Only**](a-showinadvancedviewonly.md)                                 | False     | [**Top**](c-top.md)<br/> |
| [**Site-Object-BL**](a-siteobjectbl.md)                                                       | False     | [**Top**](c-top.md)<br/> |
| [**Structural-Object-Class**](a-structuralobjectclass.md)                                     | False     | [**Top**](c-top.md)<br/> |
| [**Sub-Refs**](a-subrefs.md)                                                                  | False     | [**Top**](c-top.md)<br/> |
| [**SubSchemaSubEntry**](a-subschemasubentry.md)                                               | False     | [**Top**](c-top.md)<br/> |
| [**System-Flags**](a-systemflags.md)                                                          | False     | [**Top**](c-top.md)<br/> |
| [**Trust-Attributes**](a-trustattributes.md)                                                  | False     | **Trusted-Domain**              |
| [**Trust-Auth-Incoming**](a-trustauthincoming.md)                                             | False     | **Trusted-Domain**              |
| [**Trust-Auth-Outgoing**](a-trustauthoutgoing.md)                                             | False     | **Trusted-Domain**              |
| [**Trust-Direction**](a-trustdirection.md)                                                    | False     | **Trusted-Domain**              |
| [**Trust-Partner**](a-trustpartner.md)                                                        | False     | **Trusted-Domain**              |
| [**Trust-Posix-Offset**](a-trustposixoffset.md)                                               | False     | **Trusted-Domain**              |
| [**Trust-Type**](a-trusttype.md)                                                              | False     | **Trusted-Domain**              |
| [**USN-Changed**](a-usnchanged.md)                                                            | False     | [**Top**](c-top.md)<br/> |
| [**USN-Created**](a-usncreated.md)                                                            | False     | [**Top**](c-top.md)<br/> |
| [**USN-DSA-Last-Obj-Removed**](a-usndsalastobjremoved.md)                                     | False     | [**Top**](c-top.md)<br/> |
| [**USN-Intersite**](a-usnintersite.md)                                                        | False     | [**Top**](c-top.md)<br/> |
| [**USN-Last-Obj-Rem**](a-usnlastobjrem.md)                                                    | False     | [**Top**](c-top.md)<br/> |
| [**USN-Source**](a-usnsource.md)                                                              | False     | [**Top**](c-top.md)<br/> |
| [**Wbem-Path**](a-wbempath.md)                                                                | False     | [**Top**](c-top.md)<br/> |
| [**Well-Known-Objects**](a-wellknownobjects.md)                                               | False     | [**Top**](c-top.md)<br/> |
| [**When-Changed**](a-whenchanged.md)                                                          | False     | [**Top**](c-top.md)<br/> |
| [**When-Created**](a-whencreated.md)                                                          | False     | [**Top**](c-top.md)<br/> |
| [**WWW-Home-Page**](a-wwwhomepage.md)                                                         | False     | [**Top**](c-top.md)<br/> |
| [**WWW-Page-Other**](a-url.md)                                                                | False     | [**Top**](c-top.md)<br/> |



 

 





