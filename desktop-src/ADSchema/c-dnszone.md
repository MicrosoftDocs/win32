---
title: Dns-Zone class
description: The container for DNS Nodes. Holds zone metadata.
ms.assetid: ea8e6799-df9c-4c17-a5a2-ea3e5016e3ec
ms.tgt_platform: multiple
keywords:
- Dns-Zone class AD Schema
- dnsZone class AD Schema
topic_type:
- apiref
api_name:
- Dns-Zone
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# Dns-Zone class

The container for DNS Nodes. Holds zone metadata.



| Entry | Value |
|-------------------|--------------------------------------|
| CN                | Dns-Zone                             |
| Ldap-Display-Name | dnsZone                              |
| Update Privilege  | \-                                   |
| Update Frequency  | \-                                   |
| Schema-Id-Guid    | e0fa1e8b-9b45-11d0-afdd-00c04fd930c9 |



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
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| System-Only                 | False                                                                                                                                        |
| Object-Category             | 1                                                                                                                                            |
| Default-Object-Category     | \-                                                                                                                                           |
| Governs-Id                  | 1.2.840.113556.1.5.85                                                                                                                        |
| Default-Hiding-Value        | 1                                                                                                                                            |
| Rdn-Att-Id                  | [**Domain-Component**](a-dc.md)<br/>                                                                                                  |
| Subclass of                 | [**Top**](c-top.md)<br/>                                                                                                              |
| Possible Superiors          | [**Container**](c-container.md)                                                                                                             |
| Auxiliary Classes           | \-                                                                                                                                           |
| NT-Security-Descriptor      | O:BAG:BAD:S:                                                                                                                                 |
| Default Security Descriptor | D:(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;DA)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;ED)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;SY)(A;;CC;;;AU)(A;;RPLCLORC;;;WD) |
| System-Flags                | 0x00000010                                                                                                                                   |



## Windows 2000 Server Attributes

This class contains the following attributes for Windows 2000 Server:



| Attribute                                                                 | Mandatory | Derived from                    |
|---------------------------------------------------------------------------|-----------|---------------------------------|
| [**Admin-Description**](a-admindescription.md)                           | False     | [**Top**](c-top.md)<br/> |
| [**Admin-Display-Name**](a-admindisplayname.md)                          | False     | [**Top**](c-top.md)<br/> |
| [**Allowed-Attributes**](a-allowedattributes.md)                         | False     | [**Top**](c-top.md)<br/> |
| [**Allowed-Attributes-Effective**](a-allowedattributeseffective.md)      | False     | [**Top**](c-top.md)<br/> |
| [**Allowed-Child-Classes**](a-allowedchildclasses.md)                    | False     | [**Top**](c-top.md)<br/> |
| [**Allowed-Child-Classes-Effective**](a-allowedchildclasseseffective.md) | False     | [**Top**](c-top.md)<br/> |
| [**Bridgehead-Server-List-BL**](a-bridgeheadserverlistbl.md)             | False     | [**Top**](c-top.md)<br/> |
| [**Canonical-Name**](a-canonicalname.md)                                 | False     | [**Top**](c-top.md)<br/> |
| [**Common-Name**](a-cn.md)                                               | False     | [**Top**](c-top.md)<br/> |
| [**Create-Time-Stamp**](a-createtimestamp.md)                            | False     | [**Top**](c-top.md)<br/> |
| [**Description**](a-description.md)                                      | False     | [**Top**](c-top.md)<br/> |
| [**Display-Name**](a-displayname.md)                                     | False     | [**Top**](c-top.md)<br/> |
| [**Display-Name-Printable**](a-displaynameprintable.md)                  | False     | [**Top**](c-top.md)<br/> |
| [**Dns-Allow-Dynamic**](a-dnsallowdynamic.md)                            | False     | **Dns-Zone**                    |
| [**Dns-Allow-XFR**](a-dnsallowxfr.md)                                    | False     | **Dns-Zone**                    |
| [**Dns-Notify-Secondaries**](a-dnsnotifysecondaries.md)                  | False     | **Dns-Zone**                    |
| [**DNS-Property**](a-dnsproperty.md)                                     | False     | **Dns-Zone**                    |
| [**Dns-Secure-Secondaries**](a-dnssecuresecondaries.md)                  | False     | **Dns-Zone**                    |
| [**Domain-Component**](a-dc.md)                                          | True      | **Dns-Zone**                    |
| [**DSA-Signature**](a-dsasignature.md)                                   | False     | [**Top**](c-top.md)<br/> |
| [**DS-Core-Propagation-Data**](a-dscorepropagationdata.md)               | False     | [**Top**](c-top.md)<br/> |
| [**Extension-Name**](a-extensionname.md)                                 | False     | [**Top**](c-top.md)<br/> |
| [**Flags**](a-flags.md)                                                  | False     | [**Top**](c-top.md)<br/> |
| [**From-Entry**](a-fromentry.md)                                         | False     | [**Top**](c-top.md)<br/> |
| [**Frs-Computer-Reference-BL**](a-frscomputerreferencebl.md)             | False     | [**Top**](c-top.md)<br/> |
| [**FRS-Member-Reference-BL**](a-frsmemberreferencebl.md)                 | False     | [**Top**](c-top.md)<br/> |
| [**FSMO-Role-Owner**](a-fsmoroleowner.md)                                | False     | [**Top**](c-top.md)<br/> |
| [**Instance-Type**](a-instancetype.md)                                   | True      | [**Top**](c-top.md)<br/> |
| [**Is-Critical-System-Object**](a-iscriticalsystemobject.md)             | False     | [**Top**](c-top.md)<br/> |
| [**Is-Deleted**](a-isdeleted.md)                                         | False     | [**Top**](c-top.md)<br/> |
| [**Is-Member-Of-DL**](a-memberof.md)                                     | False     | [**Top**](c-top.md)<br/> |
| [**Is-Privilege-Holder**](a-isprivilegeholder.md)                        | False     | [**Top**](c-top.md)<br/> |
| [**Last-Known-Parent**](a-lastknownparent.md)                            | False     | [**Top**](c-top.md)<br/> |
| [**Managed-By**](a-managedby.md)                                         | False     | **Dns-Zone**                    |
| [**Managed-Objects**](a-managedobjects.md)                               | False     | [**Top**](c-top.md)<br/> |
| [**Mastered-By**](a-masteredby.md)                                       | False     | [**Top**](c-top.md)<br/> |
| [**Modify-Time-Stamp**](a-modifytimestamp.md)                            | False     | [**Top**](c-top.md)<br/> |
| [**MS-DS-Consistency-Child-Count**](a-ms-ds-consistencychildcount.md)    | False     | [**Top**](c-top.md)<br/> |
| [**MS-DS-Consistency-Guid**](a-ms-ds-consistencyguid.md)                 | False     | [**Top**](c-top.md)<br/> |
| [**netboot-SCP-BL**](a-netbootscpbl.md)                                  | False     | [**Top**](c-top.md)<br/> |
| [**Non-Security-Member-BL**](a-nonsecuritymemberbl.md)                   | False     | [**Top**](c-top.md)<br/> |
| [**NT-Security-Descriptor**](a-ntsecuritydescriptor.md)                  | True      | [**Top**](c-top.md)<br/> |
| [**Obj-Dist-Name**](a-distinguishedname.md)                              | False     | [**Top**](c-top.md)<br/> |
| [**Object-Category**](a-objectcategory.md)                               | True      | [**Top**](c-top.md)<br/> |
| [**Object-Class**](a-objectclass.md)                                     | True      | [**Top**](c-top.md)<br/> |
| [**Object-Guid**](a-objectguid.md)                                       | False     | [**Top**](c-top.md)<br/> |
| [**Object-Version**](a-objectversion.md)                                 | False     | [**Top**](c-top.md)<br/> |
| [**Other-Well-Known-Objects**](a-otherwellknownobjects.md)               | False     | [**Top**](c-top.md)<br/> |
| [**Partial-Attribute-Deletion-List**](a-partialattributedeletionlist.md) | False     | [**Top**](c-top.md)<br/> |
| [**Partial-Attribute-Set**](a-partialattributeset.md)                    | False     | [**Top**](c-top.md)<br/> |
| [**Possible-Inferiors**](a-possibleinferiors.md)                         | False     | [**Top**](c-top.md)<br/> |
| [**Proxied-Object-Name**](a-proxiedobjectname.md)                        | False     | [**Top**](c-top.md)<br/> |
| [**Proxy-Addresses**](a-proxyaddresses.md)                               | False     | [**Top**](c-top.md)<br/> |
| [**Query-Policy-BL**](a-querypolicybl.md)                                | False     | [**Top**](c-top.md)<br/> |
| [**RDN**](a-name.md)                                                     | False     | [**Top**](c-top.md)<br/> |
| [**Repl-Property-Meta-Data**](a-replpropertymetadata.md)                 | False     | [**Top**](c-top.md)<br/> |
| [**Repl-UpToDate-Vector**](a-repluptodatevector.md)                      | False     | [**Top**](c-top.md)<br/> |
| [**Reports**](a-directreports.md)                                        | False     | [**Top**](c-top.md)<br/> |
| [**Reps-From**](a-repsfrom.md)                                           | False     | [**Top**](c-top.md)<br/> |
| [**Reps-To**](a-repsto.md)                                               | False     | [**Top**](c-top.md)<br/> |
| [**Revision**](a-revision.md)                                            | False     | [**Top**](c-top.md)<br/> |
| [**SD-Rights-Effective**](a-sdrightseffective.md)                        | False     | [**Top**](c-top.md)<br/> |
| [**Server-Reference-BL**](a-serverreferencebl.md)                        | False     | [**Top**](c-top.md)<br/> |
| [**Show-In-Advanced-View-Only**](a-showinadvancedviewonly.md)            | False     | [**Top**](c-top.md)<br/> |
| [**Site-Object-BL**](a-siteobjectbl.md)                                  | False     | [**Top**](c-top.md)<br/> |
| [**Sub-Refs**](a-subrefs.md)                                             | False     | [**Top**](c-top.md)<br/> |
| [**SubSchemaSubEntry**](a-subschemasubentry.md)                          | False     | [**Top**](c-top.md)<br/> |
| [**System-Flags**](a-systemflags.md)                                     | False     | [**Top**](c-top.md)<br/> |
| [**USN-Changed**](a-usnchanged.md)                                       | False     | [**Top**](c-top.md)<br/> |
| [**USN-Created**](a-usncreated.md)                                       | False     | [**Top**](c-top.md)<br/> |
| [**USN-DSA-Last-Obj-Removed**](a-usndsalastobjremoved.md)                | False     | [**Top**](c-top.md)<br/> |
| [**USN-Intersite**](a-usnintersite.md)                                   | False     | [**Top**](c-top.md)<br/> |
| [**USN-Last-Obj-Rem**](a-usnlastobjrem.md)                               | False     | [**Top**](c-top.md)<br/> |
| [**USN-Source**](a-usnsource.md)                                         | False     | [**Top**](c-top.md)<br/> |
| [**Wbem-Path**](a-wbempath.md)                                           | False     | [**Top**](c-top.md)<br/> |
| [**Well-Known-Objects**](a-wellknownobjects.md)                          | False     | [**Top**](c-top.md)<br/> |
| [**When-Changed**](a-whenchanged.md)                                     | False     | [**Top**](c-top.md)<br/> |
| [**When-Created**](a-whencreated.md)                                     | False     | [**Top**](c-top.md)<br/> |
| [**WWW-Home-Page**](a-wwwhomepage.md)                                    | False     | [**Top**](c-top.md)<br/> |
| [**WWW-Page-Other**](a-url.md)                                           | False     | [**Top**](c-top.md)<br/> |



## Windows Server 2003

-   [Attributes](#windows-server-2003-attributes)



| Entry | Value |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| System-Only                 | False                                                                                                                                                                            |
| Object-Category             | 1                                                                                                                                                                                |
| Default-Object-Category     | \-                                                                                                                                                                               |
| Governs-Id                  | 1.2.840.113556.1.5.85                                                                                                                                                            |
| Default-Hiding-Value        | 1                                                                                                                                                                                |
| Rdn-Att-Id                  | [**Domain-Component**](a-dc.md)<br/>                                                                                                                                      |
| Subclass of                 | [**Top**](c-top.md)<br/>                                                                                                                                                  |
| Possible Superiors          | [**Container**](c-container.md)                                                                                                                                                 |
| Auxiliary Classes           | \-                                                                                                                                                                               |
| NT-Security-Descriptor      | O:BAG:BAD:S:                                                                                                                                                                     |
| Default Security Descriptor | D:(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;DA)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;ED)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;SY)(A;;CC;;;AU)(A;;RPLCLORC;;;WD)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;CO) |
| System-Flags                | 0x00000010                                                                                                                                                                       |



## Windows Server 2003 Attributes

This class contains the following attributes for Windows Server 2003:



| Attribute                                                                   | Mandatory | Derived from                    |
|-----------------------------------------------------------------------------|-----------|---------------------------------|
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
| [**Dns-Allow-Dynamic**](a-dnsallowdynamic.md)                              | False     | **Dns-Zone**                    |
| [**Dns-Allow-XFR**](a-dnsallowxfr.md)                                      | False     | **Dns-Zone**                    |
| [**Dns-Notify-Secondaries**](a-dnsnotifysecondaries.md)                    | False     | **Dns-Zone**                    |
| [**DNS-Property**](a-dnsproperty.md)                                       | False     | **Dns-Zone**                    |
| [**Dns-Secure-Secondaries**](a-dnssecuresecondaries.md)                    | False     | **Dns-Zone**                    |
| [**Domain-Component**](a-dc.md)                                            | True      | **Dns-Zone**                    |
| [**DSA-Signature**](a-dsasignature.md)                                     | False     | [**Top**](c-top.md)<br/> |
| [**DS-Core-Propagation-Data**](a-dscorepropagationdata.md)                 | False     | [**Top**](c-top.md)<br/> |
| [**Extension-Name**](a-extensionname.md)                                   | False     | [**Top**](c-top.md)<br/> |
| [**Flags**](a-flags.md)                                                    | False     | [**Top**](c-top.md)<br/> |
| [**From-Entry**](a-fromentry.md)                                           | False     | [**Top**](c-top.md)<br/> |
| [**Frs-Computer-Reference-BL**](a-frscomputerreferencebl.md)               | False     | [**Top**](c-top.md)<br/> |
| [**FRS-Member-Reference-BL**](a-frsmemberreferencebl.md)                   | False     | [**Top**](c-top.md)<br/> |
| [**FSMO-Role-Owner**](a-fsmoroleowner.md)                                  | False     | [**Top**](c-top.md)<br/> |
| [**Instance-Type**](a-instancetype.md)                                     | True      | [**Top**](c-top.md)<br/> |
| [**Is-Critical-System-Object**](a-iscriticalsystemobject.md)               | False     | [**Top**](c-top.md)<br/> |
| [**Is-Deleted**](a-isdeleted.md)                                           | False     | [**Top**](c-top.md)<br/> |
| [**Is-Member-Of-DL**](a-memberof.md)                                       | False     | [**Top**](c-top.md)<br/> |
| [**Is-Privilege-Holder**](a-isprivilegeholder.md)                          | False     | [**Top**](c-top.md)<br/> |
| [**Last-Known-Parent**](a-lastknownparent.md)                              | False     | [**Top**](c-top.md)<br/> |
| [**Managed-By**](a-managedby.md)                                           | False     | **Dns-Zone**                    |
| [**Managed-Objects**](a-managedobjects.md)                                 | False     | [**Top**](c-top.md)<br/> |
| [**Mastered-By**](a-masteredby.md)                                         | False     | [**Top**](c-top.md)<br/> |
| [**Modify-Time-Stamp**](a-modifytimestamp.md)                              | False     | [**Top**](c-top.md)<br/> |
| [**ms-COM-PartitionSetLink**](a-mscom-partitionsetlink.md)                 | False     | [**Top**](c-top.md)<br/> |
| [**ms-COM-UserLink**](a-mscom-userlink.md)                                 | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Approx-Immed-Subordinates**](a-msds-approx-immed-subordinates.md) | False     | [**Top**](c-top.md)<br/> |
| [**MS-DS-Consistency-Child-Count**](a-ms-ds-consistencychildcount.md)      | False     | [**Top**](c-top.md)<br/> |
| [**MS-DS-Consistency-Guid**](a-ms-ds-consistencyguid.md)                   | False     | [**Top**](c-top.md)<br/> |
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
| [**Server-Reference-BL**](a-serverreferencebl.md)                          | False     | [**Top**](c-top.md)<br/> |
| [**Show-In-Advanced-View-Only**](a-showinadvancedviewonly.md)              | False     | [**Top**](c-top.md)<br/> |
| [**Site-Object-BL**](a-siteobjectbl.md)                                    | False     | [**Top**](c-top.md)<br/> |
| [**Structural-Object-Class**](a-structuralobjectclass.md)                  | False     | [**Top**](c-top.md)<br/> |
| [**Sub-Refs**](a-subrefs.md)                                               | False     | [**Top**](c-top.md)<br/> |
| [**SubSchemaSubEntry**](a-subschemasubentry.md)                            | False     | [**Top**](c-top.md)<br/> |
| [**System-Flags**](a-systemflags.md)                                       | False     | [**Top**](c-top.md)<br/> |
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
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| System-Only                 | False                                                                                                                                                                            |
| Object-Category             | 1                                                                                                                                                                                |
| Default-Object-Category     | \-                                                                                                                                                                               |
| Governs-Id                  | 1.2.840.113556.1.5.85                                                                                                                                                            |
| Default-Hiding-Value        | 1                                                                                                                                                                                |
| Rdn-Att-Id                  | [**Domain-Component**](a-dc.md)<br/>                                                                                                                                      |
| Subclass of                 | [**Top**](c-top.md)<br/>                                                                                                                                                  |
| Possible Superiors          | [**Container**](c-container.md)                                                                                                                                                 |
| Auxiliary Classes           | \-                                                                                                                                                                               |
| NT-Security-Descriptor      | O:BAG:BAD:S:                                                                                                                                                                     |
| Default Security Descriptor | D:(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;DA)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;ED)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;SY)(A;;CC;;;AU)(A;;RPLCLORC;;;WD)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;CO) |
| System-Flags                | 0x00000010                                                                                                                                                                       |



## Windows Server 2003 R2 Attributes

This class contains the following attributes for Windows Server 2003 R2:



| Attribute                                                                   | Mandatory | Derived from                    |
|-----------------------------------------------------------------------------|-----------|---------------------------------|
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
| [**Dns-Allow-Dynamic**](a-dnsallowdynamic.md)                              | False     | **Dns-Zone**                    |
| [**Dns-Allow-XFR**](a-dnsallowxfr.md)                                      | False     | **Dns-Zone**                    |
| [**Dns-Notify-Secondaries**](a-dnsnotifysecondaries.md)                    | False     | **Dns-Zone**                    |
| [**DNS-Property**](a-dnsproperty.md)                                       | False     | **Dns-Zone**                    |
| [**Dns-Secure-Secondaries**](a-dnssecuresecondaries.md)                    | False     | **Dns-Zone**                    |
| [**Domain-Component**](a-dc.md)                                            | True      | **Dns-Zone**                    |
| [**DSA-Signature**](a-dsasignature.md)                                     | False     | [**Top**](c-top.md)<br/> |
| [**DS-Core-Propagation-Data**](a-dscorepropagationdata.md)                 | False     | [**Top**](c-top.md)<br/> |
| [**Extension-Name**](a-extensionname.md)                                   | False     | [**Top**](c-top.md)<br/> |
| [**Flags**](a-flags.md)                                                    | False     | [**Top**](c-top.md)<br/> |
| [**From-Entry**](a-fromentry.md)                                           | False     | [**Top**](c-top.md)<br/> |
| [**Frs-Computer-Reference-BL**](a-frscomputerreferencebl.md)               | False     | [**Top**](c-top.md)<br/> |
| [**FRS-Member-Reference-BL**](a-frsmemberreferencebl.md)                   | False     | [**Top**](c-top.md)<br/> |
| [**FSMO-Role-Owner**](a-fsmoroleowner.md)                                  | False     | [**Top**](c-top.md)<br/> |
| [**Instance-Type**](a-instancetype.md)                                     | True      | [**Top**](c-top.md)<br/> |
| [**Is-Critical-System-Object**](a-iscriticalsystemobject.md)               | False     | [**Top**](c-top.md)<br/> |
| [**Is-Deleted**](a-isdeleted.md)                                           | False     | [**Top**](c-top.md)<br/> |
| [**Is-Member-Of-DL**](a-memberof.md)                                       | False     | [**Top**](c-top.md)<br/> |
| [**Is-Privilege-Holder**](a-isprivilegeholder.md)                          | False     | [**Top**](c-top.md)<br/> |
| [**Last-Known-Parent**](a-lastknownparent.md)                              | False     | [**Top**](c-top.md)<br/> |
| [**Managed-By**](a-managedby.md)                                           | False     | **Dns-Zone**                    |
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
| [**Server-Reference-BL**](a-serverreferencebl.md)                          | False     | [**Top**](c-top.md)<br/> |
| [**Show-In-Advanced-View-Only**](a-showinadvancedviewonly.md)              | False     | [**Top**](c-top.md)<br/> |
| [**Site-Object-BL**](a-siteobjectbl.md)                                    | False     | [**Top**](c-top.md)<br/> |
| [**Structural-Object-Class**](a-structuralobjectclass.md)                  | False     | [**Top**](c-top.md)<br/> |
| [**Sub-Refs**](a-subrefs.md)                                               | False     | [**Top**](c-top.md)<br/> |
| [**SubSchemaSubEntry**](a-subschemasubentry.md)                            | False     | [**Top**](c-top.md)<br/> |
| [**System-Flags**](a-systemflags.md)                                       | False     | [**Top**](c-top.md)<br/> |
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
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| System-Only                 | False                                                                                                                                                                            |
| Object-Category             | 1                                                                                                                                                                                |
| Default-Object-Category     | \-                                                                                                                                                                               |
| Governs-Id                  | 1.2.840.113556.1.5.85                                                                                                                                                            |
| Default-Hiding-Value        | 1                                                                                                                                                                                |
| Rdn-Att-Id                  | [**Domain-Component**](a-dc.md)<br/>                                                                                                                                      |
| Subclass of                 | [**Top**](c-top.md)<br/>                                                                                                                                                  |
| Possible Superiors          | [**Container**](c-container.md)                                                                                                                                                 |
| Auxiliary Classes           | \-                                                                                                                                                                               |
| NT-Security-Descriptor      | O:BAG:BAD:S:                                                                                                                                                                     |
| Default Security Descriptor | D:(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;DA)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;ED)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;SY)(A;;CC;;;AU)(A;;RPLCLORC;;;WD)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;CO) |
| System-Flags                | 0x00000010                                                                                                                                                                       |



## Windows Server 2008 Attributes

This class contains the following attributes for Windows Server 2008:



| Attribute                                                                      | Mandatory | Derived from                    |
|--------------------------------------------------------------------------------|-----------|---------------------------------|
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
| [**Dns-Allow-Dynamic**](a-dnsallowdynamic.md)                                 | False     | **Dns-Zone**                    |
| [**Dns-Allow-XFR**](a-dnsallowxfr.md)                                         | False     | **Dns-Zone**                    |
| [**Dns-Notify-Secondaries**](a-dnsnotifysecondaries.md)                       | False     | **Dns-Zone**                    |
| [**DNS-Property**](a-dnsproperty.md)                                          | False     | **Dns-Zone**                    |
| [**Dns-Secure-Secondaries**](a-dnssecuresecondaries.md)                       | False     | **Dns-Zone**                    |
| [**Domain-Component**](a-dc.md)                                               | True      | **Dns-Zone**                    |
| [**DSA-Signature**](a-dsasignature.md)                                        | False     | [**Top**](c-top.md)<br/> |
| [**DS-Core-Propagation-Data**](a-dscorepropagationdata.md)                    | False     | [**Top**](c-top.md)<br/> |
| [**Extension-Name**](a-extensionname.md)                                      | False     | [**Top**](c-top.md)<br/> |
| [**Flags**](a-flags.md)                                                       | False     | [**Top**](c-top.md)<br/> |
| [**From-Entry**](a-fromentry.md)                                              | False     | [**Top**](c-top.md)<br/> |
| [**Frs-Computer-Reference-BL**](a-frscomputerreferencebl.md)                  | False     | [**Top**](c-top.md)<br/> |
| [**FRS-Member-Reference-BL**](a-frsmemberreferencebl.md)                      | False     | [**Top**](c-top.md)<br/> |
| [**FSMO-Role-Owner**](a-fsmoroleowner.md)                                     | False     | [**Top**](c-top.md)<br/> |
| [**Instance-Type**](a-instancetype.md)                                        | True      | [**Top**](c-top.md)<br/> |
| [**Is-Critical-System-Object**](a-iscriticalsystemobject.md)                  | False     | [**Top**](c-top.md)<br/> |
| [**Is-Deleted**](a-isdeleted.md)                                              | False     | [**Top**](c-top.md)<br/> |
| [**Is-Member-Of-DL**](a-memberof.md)                                          | False     | [**Top**](c-top.md)<br/> |
| [**Is-Privilege-Holder**](a-isprivilegeholder.md)                             | False     | [**Top**](c-top.md)<br/> |
| [**Last-Known-Parent**](a-lastknownparent.md)                                 | False     | [**Top**](c-top.md)<br/> |
| [**Managed-By**](a-managedby.md)                                              | False     | **Dns-Zone**                    |
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
| [**ms-DS-Tasks-For-Az-Role-BL**](a-msds-tasksforazrolebl.md)                  | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Tasks-For-Az-Task-BL**](a-msds-tasksforaztaskbl.md)                  | False     | [**Top**](c-top.md)<br/> |
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
| [**Server-Reference-BL**](a-serverreferencebl.md)                             | False     | [**Top**](c-top.md)<br/> |
| [**Show-In-Advanced-View-Only**](a-showinadvancedviewonly.md)                 | False     | [**Top**](c-top.md)<br/> |
| [**Site-Object-BL**](a-siteobjectbl.md)                                       | False     | [**Top**](c-top.md)<br/> |
| [**Structural-Object-Class**](a-structuralobjectclass.md)                     | False     | [**Top**](c-top.md)<br/> |
| [**Sub-Refs**](a-subrefs.md)                                                  | False     | [**Top**](c-top.md)<br/> |
| [**SubSchemaSubEntry**](a-subschemasubentry.md)                               | False     | [**Top**](c-top.md)<br/> |
| [**System-Flags**](a-systemflags.md)                                          | False     | [**Top**](c-top.md)<br/> |
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
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| System-Only                 | False                                                                                                                                                                            |
| Object-Category             | 1                                                                                                                                                                                |
| Default-Object-Category     | \-                                                                                                                                                                               |
| Governs-Id                  | 1.2.840.113556.1.5.85                                                                                                                                                            |
| Default-Hiding-Value        | 1                                                                                                                                                                                |
| Rdn-Att-Id                  | [**Domain-Component**](a-dc.md)<br/>                                                                                                                                      |
| Subclass of                 | [**Top**](c-top.md)<br/>                                                                                                                                                  |
| Possible Superiors          | [**Container**](c-container.md)                                                                                                                                                 |
| Auxiliary Classes           | \-                                                                                                                                                                               |
| NT-Security-Descriptor      | O:BAG:BAD:S:                                                                                                                                                                     |
| Default Security Descriptor | D:(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;DA)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;ED)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;SY)(A;;CC;;;AU)(A;;RPLCLORC;;;WD)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;CO) |
| System-Flags                | 0x00000010                                                                                                                                                                       |



## Windows Server 2008 R2 Attributes

This class contains the following attributes for Windows Server 2008 R2:



| Attribute                                                                        | Mandatory | Derived from                    |
|----------------------------------------------------------------------------------|-----------|---------------------------------|
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
| [**Dns-Allow-Dynamic**](a-dnsallowdynamic.md)                                   | False     | **Dns-Zone**                    |
| [**Dns-Allow-XFR**](a-dnsallowxfr.md)                                           | False     | **Dns-Zone**                    |
| [**Dns-Notify-Secondaries**](a-dnsnotifysecondaries.md)                         | False     | **Dns-Zone**                    |
| [**DNS-Property**](a-dnsproperty.md)                                            | False     | **Dns-Zone**                    |
| [**Dns-Secure-Secondaries**](a-dnssecuresecondaries.md)                         | False     | **Dns-Zone**                    |
| [**Domain-Component**](a-dc.md)                                                 | True      | **Dns-Zone**                    |
| [**DSA-Signature**](a-dsasignature.md)                                          | False     | [**Top**](c-top.md)<br/> |
| [**DS-Core-Propagation-Data**](a-dscorepropagationdata.md)                      | False     | [**Top**](c-top.md)<br/> |
| [**Extension-Name**](a-extensionname.md)                                        | False     | [**Top**](c-top.md)<br/> |
| [**Flags**](a-flags.md)                                                         | False     | [**Top**](c-top.md)<br/> |
| [**From-Entry**](a-fromentry.md)                                                | False     | [**Top**](c-top.md)<br/> |
| [**Frs-Computer-Reference-BL**](a-frscomputerreferencebl.md)                    | False     | [**Top**](c-top.md)<br/> |
| [**FRS-Member-Reference-BL**](a-frsmemberreferencebl.md)                        | False     | [**Top**](c-top.md)<br/> |
| [**FSMO-Role-Owner**](a-fsmoroleowner.md)                                       | False     | [**Top**](c-top.md)<br/> |
| [**Instance-Type**](a-instancetype.md)                                          | True      | [**Top**](c-top.md)<br/> |
| [**Is-Critical-System-Object**](a-iscriticalsystemobject.md)                    | False     | [**Top**](c-top.md)<br/> |
| [**Is-Deleted**](a-isdeleted.md)                                                | False     | [**Top**](c-top.md)<br/> |
| [**Is-Member-Of-DL**](a-memberof.md)                                            | False     | [**Top**](c-top.md)<br/> |
| [**Is-Privilege-Holder**](a-isprivilegeholder.md)                               | False     | [**Top**](c-top.md)<br/> |
| [**Is-Recycled**](a-isrecycled.md)                                              | False     | [**Top**](c-top.md)<br/> |
| [**Last-Known-Parent**](a-lastknownparent.md)                                   | False     | [**Top**](c-top.md)<br/> |
| [**Managed-By**](a-managedby.md)                                                | False     | **Dns-Zone**                    |
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
| [**ms-DS-Tasks-For-Az-Role-BL**](a-msds-tasksforazrolebl.md)                    | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Tasks-For-Az-Task-BL**](a-msds-tasksforaztaskbl.md)                    | False     | [**Top**](c-top.md)<br/> |
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
| [**Server-Reference-BL**](a-serverreferencebl.md)                               | False     | [**Top**](c-top.md)<br/> |
| [**Show-In-Advanced-View-Only**](a-showinadvancedviewonly.md)                   | False     | [**Top**](c-top.md)<br/> |
| [**Site-Object-BL**](a-siteobjectbl.md)                                         | False     | [**Top**](c-top.md)<br/> |
| [**Structural-Object-Class**](a-structuralobjectclass.md)                       | False     | [**Top**](c-top.md)<br/> |
| [**Sub-Refs**](a-subrefs.md)                                                    | False     | [**Top**](c-top.md)<br/> |
| [**SubSchemaSubEntry**](a-subschemasubentry.md)                                 | False     | [**Top**](c-top.md)<br/> |
| [**System-Flags**](a-systemflags.md)                                            | False     | [**Top**](c-top.md)<br/> |
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
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| System-Only                 | False                                                                                                                                                                            |
| Object-Category             | 1                                                                                                                                                                                |
| Default-Object-Category     | \-                                                                                                                                                                               |
| Governs-Id                  | 1.2.840.113556.1.5.85                                                                                                                                                            |
| Default-Hiding-Value        | 1                                                                                                                                                                                |
| Rdn-Att-Id                  | [**Domain-Component**](a-dc.md)<br/>                                                                                                                                      |
| Subclass of                 | [**Top**](c-top.md)<br/>                                                                                                                                                  |
| Possible Superiors          | [**Container**](c-container.md)                                                                                                                                                 |
| Auxiliary Classes           | \-                                                                                                                                                                               |
| NT-Security-Descriptor      | O:BAG:BAD:S:                                                                                                                                                                     |
| Default Security Descriptor | D:(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;DA)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;ED)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;SY)(A;;CC;;;AU)(A;;RPLCLORC;;;WD)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;CO) |
| System-Flags                | 0x00000010                                                                                                                                                                       |



## Windows Server 2012 Attributes

This class contains the following attributes for Windows Server 2012:



| Attribute                                                                                    | Mandatory | Derived from                    |
|----------------------------------------------------------------------------------------------|-----------|---------------------------------|
| [**Admin-Description**](a-admindescription.md)                                              | False     | [**Top**](c-top.md)<br/> |
| [**Admin-Display-Name**](a-admindisplayname.md)                                             | False     | [**Top**](c-top.md)<br/> |
| [**Allowed-Attributes**](a-allowedattributes.md)                                            | False     | [**Top**](c-top.md)<br/> |
| [**Allowed-Attributes-Effective**](a-allowedattributeseffective.md)                         | False     | [**Top**](c-top.md)<br/> |
| [**Allowed-Child-Classes**](a-allowedchildclasses.md)                                       | False     | [**Top**](c-top.md)<br/> |
| [**Allowed-Child-Classes-Effective**](a-allowedchildclasseseffective.md)                    | False     | [**Top**](c-top.md)<br/> |
| [**Bridgehead-Server-List-BL**](a-bridgeheadserverlistbl.md)                                | False     | [**Top**](c-top.md)<br/> |
| [**Canonical-Name**](a-canonicalname.md)                                                    | False     | [**Top**](c-top.md)<br/> |
| [**Common-Name**](a-cn.md)                                                                  | False     | [**Top**](c-top.md)<br/> |
| [**Create-Time-Stamp**](a-createtimestamp.md)                                               | False     | [**Top**](c-top.md)<br/> |
| [**Description**](a-description.md)                                                         | False     | [**Top**](c-top.md)<br/> |
| [**Display-Name**](a-displayname.md)                                                        | False     | [**Top**](c-top.md)<br/> |
| [**Display-Name-Printable**](a-displaynameprintable.md)                                     | False     | [**Top**](c-top.md)<br/> |
| [**Dns-Allow-Dynamic**](a-dnsallowdynamic.md)                                               | False     | **Dns-Zone**                    |
| [**Dns-Allow-XFR**](a-dnsallowxfr.md)                                                       | False     | **Dns-Zone**                    |
| [**Dns-Notify-Secondaries**](a-dnsnotifysecondaries.md)                                     | False     | **Dns-Zone**                    |
| [**DNS-Property**](a-dnsproperty.md)                                                        | False     | **Dns-Zone**                    |
| [**Dns-Secure-Secondaries**](a-dnssecuresecondaries.md)                                     | False     | **Dns-Zone**                    |
| [**Domain-Component**](a-dc.md)                                                             | True      | **Dns-Zone**                    |
| [**DSA-Signature**](a-dsasignature.md)                                                      | False     | [**Top**](c-top.md)<br/> |
| [**DS-Core-Propagation-Data**](a-dscorepropagationdata.md)                                  | False     | [**Top**](c-top.md)<br/> |
| [**Extension-Name**](a-extensionname.md)                                                    | False     | [**Top**](c-top.md)<br/> |
| [**Flags**](a-flags.md)                                                                     | False     | [**Top**](c-top.md)<br/> |
| [**From-Entry**](a-fromentry.md)                                                            | False     | [**Top**](c-top.md)<br/> |
| [**Frs-Computer-Reference-BL**](a-frscomputerreferencebl.md)                                | False     | [**Top**](c-top.md)<br/> |
| [**FRS-Member-Reference-BL**](a-frsmemberreferencebl.md)                                    | False     | [**Top**](c-top.md)<br/> |
| [**FSMO-Role-Owner**](a-fsmoroleowner.md)                                                   | False     | [**Top**](c-top.md)<br/> |
| [**Instance-Type**](a-instancetype.md)                                                      | True      | [**Top**](c-top.md)<br/> |
| [**Is-Critical-System-Object**](a-iscriticalsystemobject.md)                                | False     | [**Top**](c-top.md)<br/> |
| [**Is-Deleted**](a-isdeleted.md)                                                            | False     | [**Top**](c-top.md)<br/> |
| [**Is-Member-Of-DL**](a-memberof.md)                                                        | False     | [**Top**](c-top.md)<br/> |
| [**Is-Privilege-Holder**](a-isprivilegeholder.md)                                           | False     | [**Top**](c-top.md)<br/> |
| [**Is-Recycled**](a-isrecycled.md)                                                          | False     | [**Top**](c-top.md)<br/> |
| [**Last-Known-Parent**](a-lastknownparent.md)                                               | False     | [**Top**](c-top.md)<br/> |
| [**Managed-By**](a-managedby.md)                                                            | False     | **Dns-Zone**                    |
| [**Managed-Objects**](a-managedobjects.md)                                                  | False     | [**Top**](c-top.md)<br/> |
| [**Mastered-By**](a-masteredby.md)                                                          | False     | [**Top**](c-top.md)<br/> |
| [**Modify-Time-Stamp**](a-modifytimestamp.md)                                               | False     | [**Top**](c-top.md)<br/> |
| [**ms-COM-PartitionSetLink**](a-mscom-partitionsetlink.md)                                  | False     | [**Top**](c-top.md)<br/> |
| [**ms-COM-UserLink**](a-mscom-userlink.md)                                                  | False     | [**Top**](c-top.md)<br/> |
| [**ms-DFSR-ComputerReferenceBL**](a-msdfsr-computerreferencebl.md)                          | False     | [**Top**](c-top.md)<br/> |
| [**ms-DFSR-MemberReferenceBL**](a-msdfsr-memberreferencebl.md)                              | False     | [**Top**](c-top.md)<br/> |
| [**ms-DNS-DNSKEY-Records**](a-msdns-dnskeyrecords.md)                                       | False     | **Dns-Zone**                    |
| [**ms-DNS-DNSKEY-Record-Set-TTL**](a-msdns-dnskeyrecordsetttl.md)                           | False     | **Dns-Zone**                    |
| [**ms-DNS-DS-Record-Algorithms**](a-msdns-dsrecordalgorithms.md)                            | False     | **Dns-Zone**                    |
| [**ms-DNS-DS-Record-Set-TTL**](a-msdns-dsrecordsetttl.md)                                   | False     | **Dns-Zone**                    |
| [**ms-DNS-Is-Signed**](a-msdns-issigned.md)                                                 | False     | **Dns-Zone**                    |
| [**ms-DNS-Maintain-Trust-Anchor**](a-msdns-maintaintrustanchor.md)                          | False     | **Dns-Zone**                    |
| [**ms-DNS-NSEC3-Current-Salt**](a-msdns-nsec3currentsalt.md)                                | False     | **Dns-Zone**                    |
| [**ms-DNS-NSEC3-Hash-Algorithm**](a-msdns-nsec3hashalgorithm.md)                            | False     | **Dns-Zone**                    |
| [**ms-DNS-NSEC3-Iterations**](a-msdns-nsec3iterations.md)                                   | False     | **Dns-Zone**                    |
| [**ms-DNS-NSEC3-OptOut**](a-msdns-nsec3optout.md)                                           | False     | **Dns-Zone**                    |
| [**ms-DNS-NSEC3-Random-Salt-Length**](a-msdns-nsec3randomsaltlength.md)                     | False     | **Dns-Zone**                    |
| [**ms-DNS-NSEC3-User-Salt**](a-msdns-nsec3usersalt.md)                                      | False     | **Dns-Zone**                    |
| [**ms-DNS-Parent-Has-Secure-Delegation**](a-msdns-parenthassecuredelegation.md)             | False     | **Dns-Zone**                    |
| [**ms-DNS-Propagation-Time**](a-msdns-propagationtime.md)                                   | False     | **Dns-Zone**                    |
| [**ms-DNS-RFC5011-Key-Rollovers**](a-msdns-rfc5011keyrollovers.md)                          | False     | **Dns-Zone**                    |
| [**ms-DNS-Secure-Delegation-Polling-Period**](a-msdns-securedelegationpollingperiod.md)     | False     | **Dns-Zone**                    |
| [**ms-DNS-Signature-Inception-Offset**](a-msdns-signatureinceptionoffset.md)                | False     | **Dns-Zone**                    |
| [**ms-DNS-Signing-Key-Descriptors**](a-msdns-signingkeydescriptors.md)                      | False     | **Dns-Zone**                    |
| [**ms-DNS-Signing-Keys**](a-msdns-signingkeys.md)                                           | False     | **Dns-Zone**                    |
| [**ms-DNS-Sign-With-NSEC3**](a-msdns-signwithnsec3.md)                                      | False     | **Dns-Zone**                    |
| [**ms-DS-Approx-Immed-Subordinates**](a-msds-approx-immed-subordinates.md)                  | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-AuthenticatedTo-Accountlist**](a-msds-authenticatedtoaccountlist.md)               | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Claim-Shares-Possible-Values-With-BL**](a-msds-claimsharespossiblevalueswithbl.md) | False     | [**Top**](c-top.md)<br/> |
| [**MS-DS-Consistency-Child-Count**](a-ms-ds-consistencychildcount.md)                       | False     | [**Top**](c-top.md)<br/> |
| [**MS-DS-Consistency-Guid**](a-ms-ds-consistencyguid.md)                                    | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Enabled-Feature-BL**](a-msds-enabledfeaturebl.md)                                  | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Host-Service-Account-BL**](a-msds-hostserviceaccountbl.md)                         | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Is-Domain-For**](a-msds-isdomainfor.md)                                            | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Is-Full-Replica-For**](a-msds-isfullreplicafor.md)                                 | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Is-Partial-Replica-For**](a-msds-ispartialreplicafor.md)                           | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Is-Primary-Computer-For**](a-msds-isprimarycomputerfor.md)                         | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-KrbTgt-Link-BL**](a-msds-krbtgtlinkbl.md)                                          | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Last-Known-RDN**](a-msds-lastknownrdn.md)                                          | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-local-Effective-Deletion-Time**](a-msds-localeffectivedeletiontime.md)             | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-local-Effective-Recycle-Time**](a-msds-localeffectiverecycletime.md)               | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Mastered-By**](a-msds-masteredby.md)                                               | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Members-For-Az-Role-BL**](a-msds-membersforazrolebl.md)                            | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Members-Of-Resource-Property-List-BL**](a-msds-membersofresourcepropertylistbl.md) | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-NC-Repl-Cursors**](a-msds-ncreplcursors.md)                                        | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-NC-Repl-Inbound-Neighbors**](a-msds-ncreplinboundneighbors.md)                     | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-NC-Repl-Outbound-Neighbors**](a-msds-ncreploutboundneighbors.md)                   | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-NC-RO-Replica-Locations-BL**](a-msds-nc-ro-replica-locations-bl.md)                | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-NC-Type**](a-msds-nctype.md)                                                       | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Non-Members-BL**](a-msds-nonmembersbl.md)                                          | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Object-Reference-BL**](a-msds-objectreferencebl.md)                                | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-OIDToGroup-Link-BL**](a-msds-oidtogrouplinkbl.md)                                  | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Operations-For-Az-Role-BL**](a-msds-operationsforazrolebl.md)                      | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Operations-For-Az-Task-BL**](a-msds-operationsforaztaskbl.md)                      | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Principal-Name**](a-msds-principalname.md)                                         | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-PSO-Applied**](a-msds-psoapplied.md)                                               | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Repl-Attribute-Meta-Data**](a-msds-replattributemetadata.md)                       | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Repl-Value-Meta-Data**](a-msds-replvaluemetadata.md)                               | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Revealed-DSAs**](a-msds-revealeddsas.md)                                           | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Revealed-List-BL**](a-msds-revealedlistbl.md)                                      | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Tasks-For-Az-Role-BL**](a-msds-tasksforazrolebl.md)                                | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Tasks-For-Az-Task-BL**](a-msds-tasksforaztaskbl.md)                                | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-TDO-Egress-BL**](a-msds-tdoegressbl.md)                                            | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-TDO-Ingress-BL**](a-msds-tdoingressbl.md)                                          | False     | [**Top**](c-top.md)<br/> |
| [**ms-DS-Value-Type-Reference-BL**](a-msds-valuetypereferencebl.md)                         | False     | [**Top**](c-top.md)<br/> |
| [**ms-Exch-Owner-BL**](a-ownerbl.md)                                                        | False     | [**Top**](c-top.md)<br/> |
| [**msSFU-30-Posix-Member-Of**](a-mssfu30posixmemberof.md)                                   | False     | [**Top**](c-top.md)<br/> |
| [**netboot-SCP-BL**](a-netbootscpbl.md)                                                     | False     | [**Top**](c-top.md)<br/> |
| [**Non-Security-Member-BL**](a-nonsecuritymemberbl.md)                                      | False     | [**Top**](c-top.md)<br/> |
| [**NT-Security-Descriptor**](a-ntsecuritydescriptor.md)                                     | True      | [**Top**](c-top.md)<br/> |
| [**Obj-Dist-Name**](a-distinguishedname.md)                                                 | False     | [**Top**](c-top.md)<br/> |
| [**Object-Category**](a-objectcategory.md)                                                  | True      | [**Top**](c-top.md)<br/> |
| [**Object-Class**](a-objectclass.md)                                                        | True      | [**Top**](c-top.md)<br/> |
| [**Object-Guid**](a-objectguid.md)                                                          | False     | [**Top**](c-top.md)<br/> |
| [**Object-Version**](a-objectversion.md)                                                    | False     | [**Top**](c-top.md)<br/> |
| [**Other-Well-Known-Objects**](a-otherwellknownobjects.md)                                  | False     | [**Top**](c-top.md)<br/> |
| [**Partial-Attribute-Deletion-List**](a-partialattributedeletionlist.md)                    | False     | [**Top**](c-top.md)<br/> |
| [**Partial-Attribute-Set**](a-partialattributeset.md)                                       | False     | [**Top**](c-top.md)<br/> |
| [**Possible-Inferiors**](a-possibleinferiors.md)                                            | False     | [**Top**](c-top.md)<br/> |
| [**Proxied-Object-Name**](a-proxiedobjectname.md)                                           | False     | [**Top**](c-top.md)<br/> |
| [**Proxy-Addresses**](a-proxyaddresses.md)                                                  | False     | [**Top**](c-top.md)<br/> |
| [**Query-Policy-BL**](a-querypolicybl.md)                                                   | False     | [**Top**](c-top.md)<br/> |
| [**RDN**](a-name.md)                                                                        | False     | [**Top**](c-top.md)<br/> |
| [**Repl-Property-Meta-Data**](a-replpropertymetadata.md)                                    | False     | [**Top**](c-top.md)<br/> |
| [**Repl-UpToDate-Vector**](a-repluptodatevector.md)                                         | False     | [**Top**](c-top.md)<br/> |
| [**Reports**](a-directreports.md)                                                           | False     | [**Top**](c-top.md)<br/> |
| [**Reps-From**](a-repsfrom.md)                                                              | False     | [**Top**](c-top.md)<br/> |
| [**Reps-To**](a-repsto.md)                                                                  | False     | [**Top**](c-top.md)<br/> |
| [**Revision**](a-revision.md)                                                               | False     | [**Top**](c-top.md)<br/> |
| [**SD-Rights-Effective**](a-sdrightseffective.md)                                           | False     | [**Top**](c-top.md)<br/> |
| [**Server-Reference-BL**](a-serverreferencebl.md)                                           | False     | [**Top**](c-top.md)<br/> |
| [**Show-In-Advanced-View-Only**](a-showinadvancedviewonly.md)                               | False     | [**Top**](c-top.md)<br/> |
| [**Site-Object-BL**](a-siteobjectbl.md)                                                     | False     | [**Top**](c-top.md)<br/> |
| [**Structural-Object-Class**](a-structuralobjectclass.md)                                   | False     | [**Top**](c-top.md)<br/> |
| [**Sub-Refs**](a-subrefs.md)                                                                | False     | [**Top**](c-top.md)<br/> |
| [**SubSchemaSubEntry**](a-subschemasubentry.md)                                             | False     | [**Top**](c-top.md)<br/> |
| [**System-Flags**](a-systemflags.md)                                                        | False     | [**Top**](c-top.md)<br/> |
| [**USN-Changed**](a-usnchanged.md)                                                          | False     | [**Top**](c-top.md)<br/> |
| [**USN-Created**](a-usncreated.md)                                                          | False     | [**Top**](c-top.md)<br/> |
| [**USN-DSA-Last-Obj-Removed**](a-usndsalastobjremoved.md)                                   | False     | [**Top**](c-top.md)<br/> |
| [**USN-Intersite**](a-usnintersite.md)                                                      | False     | [**Top**](c-top.md)<br/> |
| [**USN-Last-Obj-Rem**](a-usnlastobjrem.md)                                                  | False     | [**Top**](c-top.md)<br/> |
| [**USN-Source**](a-usnsource.md)                                                            | False     | [**Top**](c-top.md)<br/> |
| [**Wbem-Path**](a-wbempath.md)                                                              | False     | [**Top**](c-top.md)<br/> |
| [**Well-Known-Objects**](a-wellknownobjects.md)                                             | False     | [**Top**](c-top.md)<br/> |
| [**When-Changed**](a-whenchanged.md)                                                        | False     | [**Top**](c-top.md)<br/> |
| [**When-Created**](a-whencreated.md)                                                        | False     | [**Top**](c-top.md)<br/> |
| [**WWW-Home-Page**](a-wwwhomepage.md)                                                       | False     | [**Top**](c-top.md)<br/> |
| [**WWW-Page-Other**](a-url.md)                                                              | False     | [**Top**](c-top.md)<br/> |



 

 





