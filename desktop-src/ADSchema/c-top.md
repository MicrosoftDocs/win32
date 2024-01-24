---
title: Top class
description: The top level class from which all classes are derived.
ms.assetid: 025aff6c-1804-4141-accf-d50cfd50e90e
ms.tgt_platform: multiple
keywords:
- Top class AD Schema
- top class AD Schema
topic_type:
- apiref
api_name:
- Top
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# Top class

The top level class from which all classes are derived.



| Entry | Value |
|-------------------|--------------------------------------|
| CN                | Top                                  |
| Ldap-Display-Name | top                                  |
| Update Privilege  | Schema administrator                 |
| Update Frequency  | \-                                   |
| Schema-Id-Guid    | bf967ab7-0de6-11d0-a285-00aa003049e2 |



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



| Entry | Value |
|-----------------------------|----------------------------------------------------------------------------------------------|
| System-Only                 | True                                                                                         |
| Object-Category             | 2                                                                                            |
| Default-Object-Category     | \-                                                                                           |
| Governs-Id                  | 2.5.6.0                                                                                      |
| Default-Hiding-Value        | 1                                                                                            |
| Rdn-Att-Id                  | [**Common-Name**](a-cn.md)<br/>                                                       |
| Subclass of                 | **Top**<br/>                                                                           |
| Possible Superiors          | [**Lost-And-Found**](c-lostandfound.md)                                                     |
| Auxiliary Classes           | \-                                                                                           |
| NT-Security-Descriptor      | O:BAG:BAD:S:                                                                                 |
| Default Security Descriptor | D:(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;DA)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;SY)(A;;RPLCLORC;;;AU) |
| System-Flags                | 0x00000010                                                                                   |



## Windows 2000 Server Attributes

This class contains the following attributes for Windows 2000 Server:



| Attribute                                                                 | Mandatory | Derived from |
|---------------------------------------------------------------------------|-----------|--------------|
| [**Admin-Description**](a-admindescription.md)                           | False     | **Top**      |
| [**Admin-Display-Name**](a-admindisplayname.md)                          | False     | **Top**      |
| [**Allowed-Attributes**](a-allowedattributes.md)                         | False     | **Top**      |
| [**Allowed-Attributes-Effective**](a-allowedattributeseffective.md)      | False     | **Top**      |
| [**Allowed-Child-Classes**](a-allowedchildclasses.md)                    | False     | **Top**      |
| [**Allowed-Child-Classes-Effective**](a-allowedchildclasseseffective.md) | False     | **Top**      |
| [**Bridgehead-Server-List-BL**](a-bridgeheadserverlistbl.md)             | False     | **Top**      |
| [**Canonical-Name**](a-canonicalname.md)                                 | False     | **Top**      |
| [**Common-Name**](a-cn.md)                                               | False     | **Top**      |
| [**Create-Time-Stamp**](a-createtimestamp.md)                            | False     | **Top**      |
| [**Description**](a-description.md)                                      | False     | **Top**      |
| [**Display-Name**](a-displayname.md)                                     | False     | **Top**      |
| [**Display-Name-Printable**](a-displaynameprintable.md)                  | False     | **Top**      |
| [**DSA-Signature**](a-dsasignature.md)                                   | False     | **Top**      |
| [**DS-Core-Propagation-Data**](a-dscorepropagationdata.md)               | False     | **Top**      |
| [**Extension-Name**](a-extensionname.md)                                 | False     | **Top**      |
| [**Flags**](a-flags.md)                                                  | False     | **Top**      |
| [**From-Entry**](a-fromentry.md)                                         | False     | **Top**      |
| [**Frs-Computer-Reference-BL**](a-frscomputerreferencebl.md)             | False     | **Top**      |
| [**FRS-Member-Reference-BL**](a-frsmemberreferencebl.md)                 | False     | **Top**      |
| [**FSMO-Role-Owner**](a-fsmoroleowner.md)                                | False     | **Top**      |
| [**Instance-Type**](a-instancetype.md)                                   | True      | **Top**      |
| [**Is-Critical-System-Object**](a-iscriticalsystemobject.md)             | False     | **Top**      |
| [**Is-Deleted**](a-isdeleted.md)                                         | False     | **Top**      |
| [**Is-Member-Of-DL**](a-memberof.md)                                     | False     | **Top**      |
| [**Is-Privilege-Holder**](a-isprivilegeholder.md)                        | False     | **Top**      |
| [**Last-Known-Parent**](a-lastknownparent.md)                            | False     | **Top**      |
| [**Managed-Objects**](a-managedobjects.md)                               | False     | **Top**      |
| [**Mastered-By**](a-masteredby.md)                                       | False     | **Top**      |
| [**Modify-Time-Stamp**](a-modifytimestamp.md)                            | False     | **Top**      |
| [**MS-DS-Consistency-Child-Count**](a-ms-ds-consistencychildcount.md)    | False     | **Top**      |
| [**MS-DS-Consistency-Guid**](a-ms-ds-consistencyguid.md)                 | False     | **Top**      |
| [**netboot-SCP-BL**](a-netbootscpbl.md)                                  | False     | **Top**      |
| [**Non-Security-Member-BL**](a-nonsecuritymemberbl.md)                   | False     | **Top**      |
| [**NT-Security-Descriptor**](a-ntsecuritydescriptor.md)                  | True      | **Top**      |
| [**Obj-Dist-Name**](a-distinguishedname.md)                              | False     | **Top**      |
| [**Object-Category**](a-objectcategory.md)                               | True      | **Top**      |
| [**Object-Class**](a-objectclass.md)                                     | True      | **Top**      |
| [**Object-Guid**](a-objectguid.md)                                       | False     | **Top**      |
| [**Object-Version**](a-objectversion.md)                                 | False     | **Top**      |
| [**Other-Well-Known-Objects**](a-otherwellknownobjects.md)               | False     | **Top**      |
| [**Partial-Attribute-Deletion-List**](a-partialattributedeletionlist.md) | False     | **Top**      |
| [**Partial-Attribute-Set**](a-partialattributeset.md)                    | False     | **Top**      |
| [**Possible-Inferiors**](a-possibleinferiors.md)                         | False     | **Top**      |
| [**Proxied-Object-Name**](a-proxiedobjectname.md)                        | False     | **Top**      |
| [**Proxy-Addresses**](a-proxyaddresses.md)                               | False     | **Top**      |
| [**Query-Policy-BL**](a-querypolicybl.md)                                | False     | **Top**      |
| [**RDN**](a-name.md)                                                     | False     | **Top**      |
| [**Repl-Property-Meta-Data**](a-replpropertymetadata.md)                 | False     | **Top**      |
| [**Repl-UpToDate-Vector**](a-repluptodatevector.md)                      | False     | **Top**      |
| [**Reports**](a-directreports.md)                                        | False     | **Top**      |
| [**Reps-From**](a-repsfrom.md)                                           | False     | **Top**      |
| [**Reps-To**](a-repsto.md)                                               | False     | **Top**      |
| [**Revision**](a-revision.md)                                            | False     | **Top**      |
| [**SD-Rights-Effective**](a-sdrightseffective.md)                        | False     | **Top**      |
| [**Server-Reference-BL**](a-serverreferencebl.md)                        | False     | **Top**      |
| [**Show-In-Advanced-View-Only**](a-showinadvancedviewonly.md)            | False     | **Top**      |
| [**Site-Object-BL**](a-siteobjectbl.md)                                  | False     | **Top**      |
| [**Sub-Refs**](a-subrefs.md)                                             | False     | **Top**      |
| [**SubSchemaSubEntry**](a-subschemasubentry.md)                          | False     | **Top**      |
| [**System-Flags**](a-systemflags.md)                                     | False     | **Top**      |
| [**USN-Changed**](a-usnchanged.md)                                       | False     | **Top**      |
| [**USN-Created**](a-usncreated.md)                                       | False     | **Top**      |
| [**USN-DSA-Last-Obj-Removed**](a-usndsalastobjremoved.md)                | False     | **Top**      |
| [**USN-Intersite**](a-usnintersite.md)                                   | False     | **Top**      |
| [**USN-Last-Obj-Rem**](a-usnlastobjrem.md)                               | False     | **Top**      |
| [**USN-Source**](a-usnsource.md)                                         | False     | **Top**      |
| [**Wbem-Path**](a-wbempath.md)                                           | False     | **Top**      |
| [**Well-Known-Objects**](a-wellknownobjects.md)                          | False     | **Top**      |
| [**When-Changed**](a-whenchanged.md)                                     | False     | **Top**      |
| [**When-Created**](a-whencreated.md)                                     | False     | **Top**      |
| [**WWW-Home-Page**](a-wwwhomepage.md)                                    | False     | **Top**      |
| [**WWW-Page-Other**](a-url.md)                                           | False     | **Top**      |



## Windows Server 2003

-   [Attributes](#windows-server-2003-attributes)



| Entry | Value |
|-----------------------------|----------------------------------------------------------------------------------------------|
| System-Only                 | True                                                                                         |
| Object-Category             | 2                                                                                            |
| Default-Object-Category     | \-                                                                                           |
| Governs-Id                  | 2.5.6.0                                                                                      |
| Default-Hiding-Value        | 1                                                                                            |
| Rdn-Att-Id                  | [**Common-Name**](a-cn.md)<br/>                                                       |
| Subclass of                 | **Top**<br/>                                                                           |
| Possible Superiors          | [**Lost-And-Found**](c-lostandfound.md)                                                     |
| Auxiliary Classes           | \-                                                                                           |
| NT-Security-Descriptor      | O:BAG:BAD:S:                                                                                 |
| Default Security Descriptor | D:(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;DA)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;SY)(A;;RPLCLORC;;;AU) |
| System-Flags                | 0x00000010                                                                                   |



## Windows Server 2003 Attributes

This class contains the following attributes for Windows Server 2003:



| Attribute                                                                   | Mandatory | Derived from |
|-----------------------------------------------------------------------------|-----------|--------------|
| [**Admin-Description**](a-admindescription.md)                             | False     | **Top**      |
| [**Admin-Display-Name**](a-admindisplayname.md)                            | False     | **Top**      |
| [**Allowed-Attributes**](a-allowedattributes.md)                           | False     | **Top**      |
| [**Allowed-Attributes-Effective**](a-allowedattributeseffective.md)        | False     | **Top**      |
| [**Allowed-Child-Classes**](a-allowedchildclasses.md)                      | False     | **Top**      |
| [**Allowed-Child-Classes-Effective**](a-allowedchildclasseseffective.md)   | False     | **Top**      |
| [**Bridgehead-Server-List-BL**](a-bridgeheadserverlistbl.md)               | False     | **Top**      |
| [**Canonical-Name**](a-canonicalname.md)                                   | False     | **Top**      |
| [**Common-Name**](a-cn.md)                                                 | False     | **Top**      |
| [**Create-Time-Stamp**](a-createtimestamp.md)                              | False     | **Top**      |
| [**Description**](a-description.md)                                        | False     | **Top**      |
| [**Display-Name**](a-displayname.md)                                       | False     | **Top**      |
| [**Display-Name-Printable**](a-displaynameprintable.md)                    | False     | **Top**      |
| [**DSA-Signature**](a-dsasignature.md)                                     | False     | **Top**      |
| [**DS-Core-Propagation-Data**](a-dscorepropagationdata.md)                 | False     | **Top**      |
| [**Extension-Name**](a-extensionname.md)                                   | False     | **Top**      |
| [**Flags**](a-flags.md)                                                    | False     | **Top**      |
| [**From-Entry**](a-fromentry.md)                                           | False     | **Top**      |
| [**Frs-Computer-Reference-BL**](a-frscomputerreferencebl.md)               | False     | **Top**      |
| [**FRS-Member-Reference-BL**](a-frsmemberreferencebl.md)                   | False     | **Top**      |
| [**FSMO-Role-Owner**](a-fsmoroleowner.md)                                  | False     | **Top**      |
| [**Instance-Type**](a-instancetype.md)                                     | True      | **Top**      |
| [**Is-Critical-System-Object**](a-iscriticalsystemobject.md)               | False     | **Top**      |
| [**Is-Deleted**](a-isdeleted.md)                                           | False     | **Top**      |
| [**Is-Member-Of-DL**](a-memberof.md)                                       | False     | **Top**      |
| [**Is-Privilege-Holder**](a-isprivilegeholder.md)                          | False     | **Top**      |
| [**Last-Known-Parent**](a-lastknownparent.md)                              | False     | **Top**      |
| [**Managed-Objects**](a-managedobjects.md)                                 | False     | **Top**      |
| [**Mastered-By**](a-masteredby.md)                                         | False     | **Top**      |
| [**Modify-Time-Stamp**](a-modifytimestamp.md)                              | False     | **Top**      |
| [**ms-COM-PartitionSetLink**](a-mscom-partitionsetlink.md)                 | False     | **Top**      |
| [**ms-COM-UserLink**](a-mscom-userlink.md)                                 | False     | **Top**      |
| [**ms-DS-Approx-Immed-Subordinates**](a-msds-approx-immed-subordinates.md) | False     | **Top**      |
| [**MS-DS-Consistency-Child-Count**](a-ms-ds-consistencychildcount.md)      | False     | **Top**      |
| [**MS-DS-Consistency-Guid**](a-ms-ds-consistencyguid.md)                   | False     | **Top**      |
| [**ms-DS-Mastered-By**](a-msds-masteredby.md)                              | False     | **Top**      |
| [**ms-DS-Members-For-Az-Role-BL**](a-msds-membersforazrolebl.md)           | False     | **Top**      |
| [**ms-DS-NC-Repl-Cursors**](a-msds-ncreplcursors.md)                       | False     | **Top**      |
| [**ms-DS-NC-Repl-Inbound-Neighbors**](a-msds-ncreplinboundneighbors.md)    | False     | **Top**      |
| [**ms-DS-NC-Repl-Outbound-Neighbors**](a-msds-ncreploutboundneighbors.md)  | False     | **Top**      |
| [**ms-DS-Non-Members-BL**](a-msds-nonmembersbl.md)                         | False     | **Top**      |
| [**ms-DS-Object-Reference-BL**](a-msds-objectreferencebl.md)               | False     | **Top**      |
| [**ms-DS-Operations-For-Az-Role-BL**](a-msds-operationsforazrolebl.md)     | False     | **Top**      |
| [**ms-DS-Operations-For-Az-Task-BL**](a-msds-operationsforaztaskbl.md)     | False     | **Top**      |
| [**ms-DS-Repl-Attribute-Meta-Data**](a-msds-replattributemetadata.md)      | False     | **Top**      |
| [**ms-DS-Repl-Value-Meta-Data**](a-msds-replvaluemetadata.md)              | False     | **Top**      |
| [**ms-DS-Tasks-For-Az-Role-BL**](a-msds-tasksforazrolebl.md)               | False     | **Top**      |
| [**ms-DS-Tasks-For-Az-Task-BL**](a-msds-tasksforaztaskbl.md)               | False     | **Top**      |
| [**ms-Exch-Owner-BL**](a-ownerbl.md)                                       | False     | **Top**      |
| [**netboot-SCP-BL**](a-netbootscpbl.md)                                    | False     | **Top**      |
| [**Non-Security-Member-BL**](a-nonsecuritymemberbl.md)                     | False     | **Top**      |
| [**NT-Security-Descriptor**](a-ntsecuritydescriptor.md)                    | True      | **Top**      |
| [**Obj-Dist-Name**](a-distinguishedname.md)                                | False     | **Top**      |
| [**Object-Category**](a-objectcategory.md)                                 | True      | **Top**      |
| [**Object-Class**](a-objectclass.md)                                       | True      | **Top**      |
| [**Object-Guid**](a-objectguid.md)                                         | False     | **Top**      |
| [**Object-Version**](a-objectversion.md)                                   | False     | **Top**      |
| [**Other-Well-Known-Objects**](a-otherwellknownobjects.md)                 | False     | **Top**      |
| [**Partial-Attribute-Deletion-List**](a-partialattributedeletionlist.md)   | False     | **Top**      |
| [**Partial-Attribute-Set**](a-partialattributeset.md)                      | False     | **Top**      |
| [**Possible-Inferiors**](a-possibleinferiors.md)                           | False     | **Top**      |
| [**Proxied-Object-Name**](a-proxiedobjectname.md)                          | False     | **Top**      |
| [**Proxy-Addresses**](a-proxyaddresses.md)                                 | False     | **Top**      |
| [**Query-Policy-BL**](a-querypolicybl.md)                                  | False     | **Top**      |
| [**RDN**](a-name.md)                                                       | False     | **Top**      |
| [**Repl-Property-Meta-Data**](a-replpropertymetadata.md)                   | False     | **Top**      |
| [**Repl-UpToDate-Vector**](a-repluptodatevector.md)                        | False     | **Top**      |
| [**Reports**](a-directreports.md)                                          | False     | **Top**      |
| [**Reps-From**](a-repsfrom.md)                                             | False     | **Top**      |
| [**Reps-To**](a-repsto.md)                                                 | False     | **Top**      |
| [**Revision**](a-revision.md)                                              | False     | **Top**      |
| [**SD-Rights-Effective**](a-sdrightseffective.md)                          | False     | **Top**      |
| [**Server-Reference-BL**](a-serverreferencebl.md)                          | False     | **Top**      |
| [**Show-In-Advanced-View-Only**](a-showinadvancedviewonly.md)              | False     | **Top**      |
| [**Site-Object-BL**](a-siteobjectbl.md)                                    | False     | **Top**      |
| [**Structural-Object-Class**](a-structuralobjectclass.md)                  | False     | **Top**      |
| [**Sub-Refs**](a-subrefs.md)                                               | False     | **Top**      |
| [**SubSchemaSubEntry**](a-subschemasubentry.md)                            | False     | **Top**      |
| [**System-Flags**](a-systemflags.md)                                       | False     | **Top**      |
| [**USN-Changed**](a-usnchanged.md)                                         | False     | **Top**      |
| [**USN-Created**](a-usncreated.md)                                         | False     | **Top**      |
| [**USN-DSA-Last-Obj-Removed**](a-usndsalastobjremoved.md)                  | False     | **Top**      |
| [**USN-Intersite**](a-usnintersite.md)                                     | False     | **Top**      |
| [**USN-Last-Obj-Rem**](a-usnlastobjrem.md)                                 | False     | **Top**      |
| [**USN-Source**](a-usnsource.md)                                           | False     | **Top**      |
| [**Wbem-Path**](a-wbempath.md)                                             | False     | **Top**      |
| [**Well-Known-Objects**](a-wellknownobjects.md)                            | False     | **Top**      |
| [**When-Changed**](a-whenchanged.md)                                       | False     | **Top**      |
| [**When-Created**](a-whencreated.md)                                       | False     | **Top**      |
| [**WWW-Home-Page**](a-wwwhomepage.md)                                      | False     | **Top**      |
| [**WWW-Page-Other**](a-url.md)                                             | False     | **Top**      |



## ADAM

-   [Attributes](#adam-attributes)



| Entry | Value |
|-----------------------------|------------------------------------------|
| System-Only                 | True                                     |
| Object-Category             | 2                                        |
| Default-Object-Category     | \-                                       |
| Governs-Id                  | 2.5.6.0                                  |
| Default-Hiding-Value        | 1                                        |
| Rdn-Att-Id                  | [**Common-Name**](a-cn.md)<br/>   |
| Subclass of                 | **Top**<br/>                       |
| Possible Superiors          | [**Lost-And-Found**](c-lostandfound.md) |
| Auxiliary Classes           | \-                                       |
| NT-Security-Descriptor      | O:BAG:BAD:S:                             |
| Default Security Descriptor | D:S:                                     |
| System-Flags                | 0x00000010                               |



## ADAM Attributes

This class contains the following attributes for ADAM:



| Attribute                                                                   | Mandatory | Derived from |
|-----------------------------------------------------------------------------|-----------|--------------|
| [**Admin-Description**](a-admindescription.md)                             | False     | **Top**      |
| [**Admin-Display-Name**](a-admindisplayname.md)                            | False     | **Top**      |
| [**Allowed-Attributes**](a-allowedattributes.md)                           | False     | **Top**      |
| [**Allowed-Attributes-Effective**](a-allowedattributeseffective.md)        | False     | **Top**      |
| [**Allowed-Child-Classes**](a-allowedchildclasses.md)                      | False     | **Top**      |
| [**Allowed-Child-Classes-Effective**](a-allowedchildclasseseffective.md)   | False     | **Top**      |
| [**Bridgehead-Server-List-BL**](a-bridgeheadserverlistbl.md)               | False     | **Top**      |
| [**Canonical-Name**](a-canonicalname.md)                                   | False     | **Top**      |
| [**Common-Name**](a-cn.md)                                                 | False     | **Top**      |
| [**Create-Time-Stamp**](a-createtimestamp.md)                              | False     | **Top**      |
| [**Description**](a-description.md)                                        | False     | **Top**      |
| [**Display-Name**](a-displayname.md)                                       | False     | **Top**      |
| [**DSA-Signature**](a-dsasignature.md)                                     | False     | **Top**      |
| [**DS-Core-Propagation-Data**](a-dscorepropagationdata.md)                 | False     | **Top**      |
| [**From-Entry**](a-fromentry.md)                                           | False     | **Top**      |
| [**FSMO-Role-Owner**](a-fsmoroleowner.md)                                  | False     | **Top**      |
| [**Instance-Type**](a-instancetype.md)                                     | True      | **Top**      |
| [**Is-Critical-System-Object**](a-iscriticalsystemobject.md)               | False     | **Top**      |
| [**Is-Deleted**](a-isdeleted.md)                                           | False     | **Top**      |
| [**Is-Member-Of-DL**](a-memberof.md)                                       | False     | **Top**      |
| [**Last-Known-Parent**](a-lastknownparent.md)                              | False     | **Top**      |
| [**Managed-Objects**](a-managedobjects.md)                                 | False     | **Top**      |
| [**Mastered-By**](a-masteredby.md)                                         | False     | **Top**      |
| [**Modify-Time-Stamp**](a-modifytimestamp.md)                              | False     | **Top**      |
| [**ms-DS-Approx-Immed-Subordinates**](a-msds-approx-immed-subordinates.md) | False     | **Top**      |
| [**MS-DS-Consistency-Child-Count**](a-ms-ds-consistencychildcount.md)      | False     | **Top**      |
| [**MS-DS-Consistency-Guid**](a-ms-ds-consistencyguid.md)                   | False     | **Top**      |
| [**ms-DS-Disable-For-Instances-BL**](a-msds-disableforinstancesbl.md)      | False     | **Top**      |
| [**ms-DS-Mastered-By**](a-msds-masteredby.md)                              | False     | **Top**      |
| [**ms-DS-NC-Repl-Cursors**](a-msds-ncreplcursors.md)                       | False     | **Top**      |
| [**ms-DS-NC-Repl-Inbound-Neighbors**](a-msds-ncreplinboundneighbors.md)    | False     | **Top**      |
| [**ms-DS-NC-Repl-Outbound-Neighbors**](a-msds-ncreploutboundneighbors.md)  | False     | **Top**      |
| [**ms-DS-Repl-Attribute-Meta-Data**](a-msds-replattributemetadata.md)      | False     | **Top**      |
| [**ms-DS-Repl-Value-Meta-Data**](a-msds-replvaluemetadata.md)              | False     | **Top**      |
| [**ms-DS-Service-Account-BL**](a-msds-serviceaccountbl.md)                 | False     | **Top**      |
| [**NT-Security-Descriptor**](a-ntsecuritydescriptor.md)                    | True      | **Top**      |
| [**Obj-Dist-Name**](a-distinguishedname.md)                                | False     | **Top**      |
| [**Object-Category**](a-objectcategory.md)                                 | True      | **Top**      |
| [**Object-Class**](a-objectclass.md)                                       | True      | **Top**      |
| [**Object-Guid**](a-objectguid.md)                                         | False     | **Top**      |
| [**Object-Version**](a-objectversion.md)                                   | False     | **Top**      |
| [**Other-Well-Known-Objects**](a-otherwellknownobjects.md)                 | False     | **Top**      |
| [**Partial-Attribute-Deletion-List**](a-partialattributedeletionlist.md)   | False     | **Top**      |
| [**Partial-Attribute-Set**](a-partialattributeset.md)                      | False     | **Top**      |
| [**Possible-Inferiors**](a-possibleinferiors.md)                           | False     | **Top**      |
| [**Proxied-Object-Name**](a-proxiedobjectname.md)                          | False     | **Top**      |
| [**Proxy-Addresses**](a-proxyaddresses.md)                                 | False     | **Top**      |
| [**Query-Policy-BL**](a-querypolicybl.md)                                  | False     | **Top**      |
| [**RDN**](a-name.md)                                                       | False     | **Top**      |
| [**Repl-Property-Meta-Data**](a-replpropertymetadata.md)                   | False     | **Top**      |
| [**Repl-UpToDate-Vector**](a-repluptodatevector.md)                        | False     | **Top**      |
| [**Reps-From**](a-repsfrom.md)                                             | False     | **Top**      |
| [**Reps-To**](a-repsto.md)                                                 | False     | **Top**      |
| [**Revision**](a-revision.md)                                              | False     | **Top**      |
| [**SD-Rights-Effective**](a-sdrightseffective.md)                          | False     | **Top**      |
| [**Server-Reference-BL**](a-serverreferencebl.md)                          | False     | **Top**      |
| [**Show-In-Advanced-View-Only**](a-showinadvancedviewonly.md)              | False     | **Top**      |
| [**Site-Object-BL**](a-siteobjectbl.md)                                    | False     | **Top**      |
| [**Structural-Object-Class**](a-structuralobjectclass.md)                  | False     | **Top**      |
| [**Sub-Refs**](a-subrefs.md)                                               | False     | **Top**      |
| [**SubSchemaSubEntry**](a-subschemasubentry.md)                            | False     | **Top**      |
| [**System-Flags**](a-systemflags.md)                                       | False     | **Top**      |
| [**USN-Changed**](a-usnchanged.md)                                         | False     | **Top**      |
| [**USN-Created**](a-usncreated.md)                                         | False     | **Top**      |
| [**USN-DSA-Last-Obj-Removed**](a-usndsalastobjremoved.md)                  | False     | **Top**      |
| [**USN-Intersite**](a-usnintersite.md)                                     | False     | **Top**      |
| [**USN-Last-Obj-Rem**](a-usnlastobjrem.md)                                 | False     | **Top**      |
| [**USN-Source**](a-usnsource.md)                                           | False     | **Top**      |
| [**Wbem-Path**](a-wbempath.md)                                             | False     | **Top**      |
| [**Well-Known-Objects**](a-wellknownobjects.md)                            | False     | **Top**      |
| [**When-Changed**](a-whenchanged.md)                                       | False     | **Top**      |
| [**When-Created**](a-whencreated.md)                                       | False     | **Top**      |
| [**WWW-Home-Page**](a-wwwhomepage.md)                                      | False     | **Top**      |
| [**WWW-Page-Other**](a-url.md)                                             | False     | **Top**      |



## Windows Server 2003 R2

-   [Attributes](#windows-server-2003-r2-attributes)



| Entry | Value |
|-----------------------------|----------------------------------------------------------------------------------------------|
| System-Only                 | True                                                                                         |
| Object-Category             | 2                                                                                            |
| Default-Object-Category     | \-                                                                                           |
| Governs-Id                  | 2.5.6.0                                                                                      |
| Default-Hiding-Value        | 1                                                                                            |
| Rdn-Att-Id                  | [**Common-Name**](a-cn.md)<br/>                                                       |
| Subclass of                 | **Top**<br/>                                                                           |
| Possible Superiors          | [**Lost-And-Found**](c-lostandfound.md)                                                     |
| Auxiliary Classes           | \-                                                                                           |
| NT-Security-Descriptor      | O:BAG:BAD:S:                                                                                 |
| Default Security Descriptor | D:(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;DA)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;SY)(A;;RPLCLORC;;;AU) |
| System-Flags                | 0x00000010                                                                                   |



## Windows Server 2003 R2 Attributes

This class contains the following attributes for Windows Server 2003 R2:



| Attribute                                                                   | Mandatory | Derived from |
|-----------------------------------------------------------------------------|-----------|--------------|
| [**Admin-Description**](a-admindescription.md)                             | False     | **Top**      |
| [**Admin-Display-Name**](a-admindisplayname.md)                            | False     | **Top**      |
| [**Allowed-Attributes**](a-allowedattributes.md)                           | False     | **Top**      |
| [**Allowed-Attributes-Effective**](a-allowedattributeseffective.md)        | False     | **Top**      |
| [**Allowed-Child-Classes**](a-allowedchildclasses.md)                      | False     | **Top**      |
| [**Allowed-Child-Classes-Effective**](a-allowedchildclasseseffective.md)   | False     | **Top**      |
| [**Bridgehead-Server-List-BL**](a-bridgeheadserverlistbl.md)               | False     | **Top**      |
| [**Canonical-Name**](a-canonicalname.md)                                   | False     | **Top**      |
| [**Common-Name**](a-cn.md)                                                 | False     | **Top**      |
| [**Create-Time-Stamp**](a-createtimestamp.md)                              | False     | **Top**      |
| [**Description**](a-description.md)                                        | False     | **Top**      |
| [**Display-Name**](a-displayname.md)                                       | False     | **Top**      |
| [**Display-Name-Printable**](a-displaynameprintable.md)                    | False     | **Top**      |
| [**DSA-Signature**](a-dsasignature.md)                                     | False     | **Top**      |
| [**DS-Core-Propagation-Data**](a-dscorepropagationdata.md)                 | False     | **Top**      |
| [**Extension-Name**](a-extensionname.md)                                   | False     | **Top**      |
| [**Flags**](a-flags.md)                                                    | False     | **Top**      |
| [**From-Entry**](a-fromentry.md)                                           | False     | **Top**      |
| [**Frs-Computer-Reference-BL**](a-frscomputerreferencebl.md)               | False     | **Top**      |
| [**FRS-Member-Reference-BL**](a-frsmemberreferencebl.md)                   | False     | **Top**      |
| [**FSMO-Role-Owner**](a-fsmoroleowner.md)                                  | False     | **Top**      |
| [**Instance-Type**](a-instancetype.md)                                     | True      | **Top**      |
| [**Is-Critical-System-Object**](a-iscriticalsystemobject.md)               | False     | **Top**      |
| [**Is-Deleted**](a-isdeleted.md)                                           | False     | **Top**      |
| [**Is-Member-Of-DL**](a-memberof.md)                                       | False     | **Top**      |
| [**Is-Privilege-Holder**](a-isprivilegeholder.md)                          | False     | **Top**      |
| [**Last-Known-Parent**](a-lastknownparent.md)                              | False     | **Top**      |
| [**Managed-Objects**](a-managedobjects.md)                                 | False     | **Top**      |
| [**Mastered-By**](a-masteredby.md)                                         | False     | **Top**      |
| [**Modify-Time-Stamp**](a-modifytimestamp.md)                              | False     | **Top**      |
| [**ms-COM-PartitionSetLink**](a-mscom-partitionsetlink.md)                 | False     | **Top**      |
| [**ms-COM-UserLink**](a-mscom-userlink.md)                                 | False     | **Top**      |
| [**ms-DFSR-ComputerReferenceBL**](a-msdfsr-computerreferencebl.md)         | False     | **Top**      |
| [**ms-DFSR-MemberReferenceBL**](a-msdfsr-memberreferencebl.md)             | False     | **Top**      |
| [**ms-DS-Approx-Immed-Subordinates**](a-msds-approx-immed-subordinates.md) | False     | **Top**      |
| [**MS-DS-Consistency-Child-Count**](a-ms-ds-consistencychildcount.md)      | False     | **Top**      |
| [**MS-DS-Consistency-Guid**](a-ms-ds-consistencyguid.md)                   | False     | **Top**      |
| [**ms-DS-Mastered-By**](a-msds-masteredby.md)                              | False     | **Top**      |
| [**ms-DS-Members-For-Az-Role-BL**](a-msds-membersforazrolebl.md)           | False     | **Top**      |
| [**ms-DS-NC-Repl-Cursors**](a-msds-ncreplcursors.md)                       | False     | **Top**      |
| [**ms-DS-NC-Repl-Inbound-Neighbors**](a-msds-ncreplinboundneighbors.md)    | False     | **Top**      |
| [**ms-DS-NC-Repl-Outbound-Neighbors**](a-msds-ncreploutboundneighbors.md)  | False     | **Top**      |
| [**ms-DS-Non-Members-BL**](a-msds-nonmembersbl.md)                         | False     | **Top**      |
| [**ms-DS-Object-Reference-BL**](a-msds-objectreferencebl.md)               | False     | **Top**      |
| [**ms-DS-Operations-For-Az-Role-BL**](a-msds-operationsforazrolebl.md)     | False     | **Top**      |
| [**ms-DS-Operations-For-Az-Task-BL**](a-msds-operationsforaztaskbl.md)     | False     | **Top**      |
| [**ms-DS-Repl-Attribute-Meta-Data**](a-msds-replattributemetadata.md)      | False     | **Top**      |
| [**ms-DS-Repl-Value-Meta-Data**](a-msds-replvaluemetadata.md)              | False     | **Top**      |
| [**ms-DS-Tasks-For-Az-Role-BL**](a-msds-tasksforazrolebl.md)               | False     | **Top**      |
| [**ms-DS-Tasks-For-Az-Task-BL**](a-msds-tasksforaztaskbl.md)               | False     | **Top**      |
| [**ms-Exch-Owner-BL**](a-ownerbl.md)                                       | False     | **Top**      |
| [**msSFU-30-Posix-Member-Of**](a-mssfu30posixmemberof.md)                  | False     | **Top**      |
| [**netboot-SCP-BL**](a-netbootscpbl.md)                                    | False     | **Top**      |
| [**Non-Security-Member-BL**](a-nonsecuritymemberbl.md)                     | False     | **Top**      |
| [**NT-Security-Descriptor**](a-ntsecuritydescriptor.md)                    | True      | **Top**      |
| [**Obj-Dist-Name**](a-distinguishedname.md)                                | False     | **Top**      |
| [**Object-Category**](a-objectcategory.md)                                 | True      | **Top**      |
| [**Object-Class**](a-objectclass.md)                                       | True      | **Top**      |
| [**Object-Guid**](a-objectguid.md)                                         | False     | **Top**      |
| [**Object-Version**](a-objectversion.md)                                   | False     | **Top**      |
| [**Other-Well-Known-Objects**](a-otherwellknownobjects.md)                 | False     | **Top**      |
| [**Partial-Attribute-Deletion-List**](a-partialattributedeletionlist.md)   | False     | **Top**      |
| [**Partial-Attribute-Set**](a-partialattributeset.md)                      | False     | **Top**      |
| [**Possible-Inferiors**](a-possibleinferiors.md)                           | False     | **Top**      |
| [**Proxied-Object-Name**](a-proxiedobjectname.md)                          | False     | **Top**      |
| [**Proxy-Addresses**](a-proxyaddresses.md)                                 | False     | **Top**      |
| [**Query-Policy-BL**](a-querypolicybl.md)                                  | False     | **Top**      |
| [**RDN**](a-name.md)                                                       | False     | **Top**      |
| [**Repl-Property-Meta-Data**](a-replpropertymetadata.md)                   | False     | **Top**      |
| [**Repl-UpToDate-Vector**](a-repluptodatevector.md)                        | False     | **Top**      |
| [**Reports**](a-directreports.md)                                          | False     | **Top**      |
| [**Reps-From**](a-repsfrom.md)                                             | False     | **Top**      |
| [**Reps-To**](a-repsto.md)                                                 | False     | **Top**      |
| [**Revision**](a-revision.md)                                              | False     | **Top**      |
| [**SD-Rights-Effective**](a-sdrightseffective.md)                          | False     | **Top**      |
| [**Server-Reference-BL**](a-serverreferencebl.md)                          | False     | **Top**      |
| [**Show-In-Advanced-View-Only**](a-showinadvancedviewonly.md)              | False     | **Top**      |
| [**Site-Object-BL**](a-siteobjectbl.md)                                    | False     | **Top**      |
| [**Structural-Object-Class**](a-structuralobjectclass.md)                  | False     | **Top**      |
| [**Sub-Refs**](a-subrefs.md)                                               | False     | **Top**      |
| [**SubSchemaSubEntry**](a-subschemasubentry.md)                            | False     | **Top**      |
| [**System-Flags**](a-systemflags.md)                                       | False     | **Top**      |
| [**USN-Changed**](a-usnchanged.md)                                         | False     | **Top**      |
| [**USN-Created**](a-usncreated.md)                                         | False     | **Top**      |
| [**USN-DSA-Last-Obj-Removed**](a-usndsalastobjremoved.md)                  | False     | **Top**      |
| [**USN-Intersite**](a-usnintersite.md)                                     | False     | **Top**      |
| [**USN-Last-Obj-Rem**](a-usnlastobjrem.md)                                 | False     | **Top**      |
| [**USN-Source**](a-usnsource.md)                                           | False     | **Top**      |
| [**Wbem-Path**](a-wbempath.md)                                             | False     | **Top**      |
| [**Well-Known-Objects**](a-wellknownobjects.md)                            | False     | **Top**      |
| [**When-Changed**](a-whenchanged.md)                                       | False     | **Top**      |
| [**When-Created**](a-whencreated.md)                                       | False     | **Top**      |
| [**WWW-Home-Page**](a-wwwhomepage.md)                                      | False     | **Top**      |
| [**WWW-Page-Other**](a-url.md)                                             | False     | **Top**      |



## Windows Server 2008

-   [Attributes](#windows-server-2008-attributes)



| Entry | Value |
|-----------------------------|----------------------------------------------------------------------------------------------|
| System-Only                 | True                                                                                         |
| Object-Category             | 2                                                                                            |
| Default-Object-Category     | \-                                                                                           |
| Governs-Id                  | 2.5.6.0                                                                                      |
| Default-Hiding-Value        | 1                                                                                            |
| Rdn-Att-Id                  | [**Common-Name**](a-cn.md)<br/>                                                       |
| Subclass of                 | **Top**<br/>                                                                           |
| Possible Superiors          | [**Lost-And-Found**](c-lostandfound.md)                                                     |
| Auxiliary Classes           | \-                                                                                           |
| NT-Security-Descriptor      | O:BAG:BAD:S:                                                                                 |
| Default Security Descriptor | D:(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;DA)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;SY)(A;;RPLCLORC;;;AU) |
| System-Flags                | 0x00000010                                                                                   |



## Windows Server 2008 Attributes

This class contains the following attributes for Windows Server 2008:



| Attribute                                                                      | Mandatory | Derived from |
|--------------------------------------------------------------------------------|-----------|--------------|
| [**Admin-Description**](a-admindescription.md)                                | False     | **Top**      |
| [**Admin-Display-Name**](a-admindisplayname.md)                               | False     | **Top**      |
| [**Allowed-Attributes**](a-allowedattributes.md)                              | False     | **Top**      |
| [**Allowed-Attributes-Effective**](a-allowedattributeseffective.md)           | False     | **Top**      |
| [**Allowed-Child-Classes**](a-allowedchildclasses.md)                         | False     | **Top**      |
| [**Allowed-Child-Classes-Effective**](a-allowedchildclasseseffective.md)      | False     | **Top**      |
| [**Bridgehead-Server-List-BL**](a-bridgeheadserverlistbl.md)                  | False     | **Top**      |
| [**Canonical-Name**](a-canonicalname.md)                                      | False     | **Top**      |
| [**Common-Name**](a-cn.md)                                                    | False     | **Top**      |
| [**Create-Time-Stamp**](a-createtimestamp.md)                                 | False     | **Top**      |
| [**Description**](a-description.md)                                           | False     | **Top**      |
| [**Display-Name**](a-displayname.md)                                          | False     | **Top**      |
| [**Display-Name-Printable**](a-displaynameprintable.md)                       | False     | **Top**      |
| [**DSA-Signature**](a-dsasignature.md)                                        | False     | **Top**      |
| [**DS-Core-Propagation-Data**](a-dscorepropagationdata.md)                    | False     | **Top**      |
| [**Extension-Name**](a-extensionname.md)                                      | False     | **Top**      |
| [**Flags**](a-flags.md)                                                       | False     | **Top**      |
| [**From-Entry**](a-fromentry.md)                                              | False     | **Top**      |
| [**Frs-Computer-Reference-BL**](a-frscomputerreferencebl.md)                  | False     | **Top**      |
| [**FRS-Member-Reference-BL**](a-frsmemberreferencebl.md)                      | False     | **Top**      |
| [**FSMO-Role-Owner**](a-fsmoroleowner.md)                                     | False     | **Top**      |
| [**Instance-Type**](a-instancetype.md)                                        | True      | **Top**      |
| [**Is-Critical-System-Object**](a-iscriticalsystemobject.md)                  | False     | **Top**      |
| [**Is-Deleted**](a-isdeleted.md)                                              | False     | **Top**      |
| [**Is-Member-Of-DL**](a-memberof.md)                                          | False     | **Top**      |
| [**Is-Privilege-Holder**](a-isprivilegeholder.md)                             | False     | **Top**      |
| [**Last-Known-Parent**](a-lastknownparent.md)                                 | False     | **Top**      |
| [**Managed-Objects**](a-managedobjects.md)                                    | False     | **Top**      |
| [**Mastered-By**](a-masteredby.md)                                            | False     | **Top**      |
| [**Modify-Time-Stamp**](a-modifytimestamp.md)                                 | False     | **Top**      |
| [**ms-COM-PartitionSetLink**](a-mscom-partitionsetlink.md)                    | False     | **Top**      |
| [**ms-COM-UserLink**](a-mscom-userlink.md)                                    | False     | **Top**      |
| [**ms-DFSR-ComputerReferenceBL**](a-msdfsr-computerreferencebl.md)            | False     | **Top**      |
| [**ms-DFSR-MemberReferenceBL**](a-msdfsr-memberreferencebl.md)                | False     | **Top**      |
| [**ms-DS-Approx-Immed-Subordinates**](a-msds-approx-immed-subordinates.md)    | False     | **Top**      |
| [**ms-DS-AuthenticatedTo-Accountlist**](a-msds-authenticatedtoaccountlist.md) | False     | **Top**      |
| [**MS-DS-Consistency-Child-Count**](a-ms-ds-consistencychildcount.md)         | False     | **Top**      |
| [**MS-DS-Consistency-Guid**](a-ms-ds-consistencyguid.md)                      | False     | **Top**      |
| [**ms-DS-Is-Domain-For**](a-msds-isdomainfor.md)                              | False     | **Top**      |
| [**ms-DS-Is-Full-Replica-For**](a-msds-isfullreplicafor.md)                   | False     | **Top**      |
| [**ms-DS-Is-Partial-Replica-For**](a-msds-ispartialreplicafor.md)             | False     | **Top**      |
| [**ms-DS-KrbTgt-Link-BL**](a-msds-krbtgtlinkbl.md)                            | False     | **Top**      |
| [**ms-DS-Mastered-By**](a-msds-masteredby.md)                                 | False     | **Top**      |
| [**ms-DS-Members-For-Az-Role-BL**](a-msds-membersforazrolebl.md)              | False     | **Top**      |
| [**ms-DS-NC-Repl-Cursors**](a-msds-ncreplcursors.md)                          | False     | **Top**      |
| [**ms-DS-NC-Repl-Inbound-Neighbors**](a-msds-ncreplinboundneighbors.md)       | False     | **Top**      |
| [**ms-DS-NC-Repl-Outbound-Neighbors**](a-msds-ncreploutboundneighbors.md)     | False     | **Top**      |
| [**ms-DS-NC-RO-Replica-Locations-BL**](a-msds-nc-ro-replica-locations-bl.md)  | False     | **Top**      |
| [**ms-DS-NC-Type**](a-msds-nctype.md)                                         | False     | **Top**      |
| [**ms-DS-Non-Members-BL**](a-msds-nonmembersbl.md)                            | False     | **Top**      |
| [**ms-DS-Object-Reference-BL**](a-msds-objectreferencebl.md)                  | False     | **Top**      |
| [**ms-DS-Operations-For-Az-Role-BL**](a-msds-operationsforazrolebl.md)        | False     | **Top**      |
| [**ms-DS-Operations-For-Az-Task-BL**](a-msds-operationsforaztaskbl.md)        | False     | **Top**      |
| [**ms-DS-Principal-Name**](a-msds-principalname.md)                           | False     | **Top**      |
| [**ms-DS-PSO-Applied**](a-msds-psoapplied.md)                                 | False     | **Top**      |
| [**ms-DS-Repl-Attribute-Meta-Data**](a-msds-replattributemetadata.md)         | False     | **Top**      |
| [**ms-DS-Repl-Value-Meta-Data**](a-msds-replvaluemetadata.md)                 | False     | **Top**      |
| [**ms-DS-Revealed-DSAs**](a-msds-revealeddsas.md)                             | False     | **Top**      |
| [**ms-DS-Revealed-List-BL**](a-msds-revealedlistbl.md)                        | False     | **Top**      |
| [**ms-DS-Tasks-For-Az-Role-BL**](a-msds-tasksforazrolebl.md)                  | False     | **Top**      |
| [**ms-DS-Tasks-For-Az-Task-BL**](a-msds-tasksforaztaskbl.md)                  | False     | **Top**      |
| [**ms-Exch-Owner-BL**](a-ownerbl.md)                                          | False     | **Top**      |
| [**msSFU-30-Posix-Member-Of**](a-mssfu30posixmemberof.md)                     | False     | **Top**      |
| [**netboot-SCP-BL**](a-netbootscpbl.md)                                       | False     | **Top**      |
| [**Non-Security-Member-BL**](a-nonsecuritymemberbl.md)                        | False     | **Top**      |
| [**NT-Security-Descriptor**](a-ntsecuritydescriptor.md)                       | True      | **Top**      |
| [**Obj-Dist-Name**](a-distinguishedname.md)                                   | False     | **Top**      |
| [**Object-Category**](a-objectcategory.md)                                    | True      | **Top**      |
| [**Object-Class**](a-objectclass.md)                                          | True      | **Top**      |
| [**Object-Guid**](a-objectguid.md)                                            | False     | **Top**      |
| [**Object-Version**](a-objectversion.md)                                      | False     | **Top**      |
| [**Other-Well-Known-Objects**](a-otherwellknownobjects.md)                    | False     | **Top**      |
| [**Partial-Attribute-Deletion-List**](a-partialattributedeletionlist.md)      | False     | **Top**      |
| [**Partial-Attribute-Set**](a-partialattributeset.md)                         | False     | **Top**      |
| [**Possible-Inferiors**](a-possibleinferiors.md)                              | False     | **Top**      |
| [**Proxied-Object-Name**](a-proxiedobjectname.md)                             | False     | **Top**      |
| [**Proxy-Addresses**](a-proxyaddresses.md)                                    | False     | **Top**      |
| [**Query-Policy-BL**](a-querypolicybl.md)                                     | False     | **Top**      |
| [**RDN**](a-name.md)                                                          | False     | **Top**      |
| [**Repl-Property-Meta-Data**](a-replpropertymetadata.md)                      | False     | **Top**      |
| [**Repl-UpToDate-Vector**](a-repluptodatevector.md)                           | False     | **Top**      |
| [**Reports**](a-directreports.md)                                             | False     | **Top**      |
| [**Reps-From**](a-repsfrom.md)                                                | False     | **Top**      |
| [**Reps-To**](a-repsto.md)                                                    | False     | **Top**      |
| [**Revision**](a-revision.md)                                                 | False     | **Top**      |
| [**SD-Rights-Effective**](a-sdrightseffective.md)                             | False     | **Top**      |
| [**Server-Reference-BL**](a-serverreferencebl.md)                             | False     | **Top**      |
| [**Show-In-Advanced-View-Only**](a-showinadvancedviewonly.md)                 | False     | **Top**      |
| [**Site-Object-BL**](a-siteobjectbl.md)                                       | False     | **Top**      |
| [**Structural-Object-Class**](a-structuralobjectclass.md)                     | False     | **Top**      |
| [**Sub-Refs**](a-subrefs.md)                                                  | False     | **Top**      |
| [**SubSchemaSubEntry**](a-subschemasubentry.md)                               | False     | **Top**      |
| [**System-Flags**](a-systemflags.md)                                          | False     | **Top**      |
| [**USN-Changed**](a-usnchanged.md)                                            | False     | **Top**      |
| [**USN-Created**](a-usncreated.md)                                            | False     | **Top**      |
| [**USN-DSA-Last-Obj-Removed**](a-usndsalastobjremoved.md)                     | False     | **Top**      |
| [**USN-Intersite**](a-usnintersite.md)                                        | False     | **Top**      |
| [**USN-Last-Obj-Rem**](a-usnlastobjrem.md)                                    | False     | **Top**      |
| [**USN-Source**](a-usnsource.md)                                              | False     | **Top**      |
| [**Wbem-Path**](a-wbempath.md)                                                | False     | **Top**      |
| [**Well-Known-Objects**](a-wellknownobjects.md)                               | False     | **Top**      |
| [**When-Changed**](a-whenchanged.md)                                          | False     | **Top**      |
| [**When-Created**](a-whencreated.md)                                          | False     | **Top**      |
| [**WWW-Home-Page**](a-wwwhomepage.md)                                         | False     | **Top**      |
| [**WWW-Page-Other**](a-url.md)                                                | False     | **Top**      |



## Windows Server 2008 R2

-   [Attributes](#windows-server-2008-r2-attributes)



| Entry | Value |
|-----------------------------|----------------------------------------------------------------------------------------------|
| System-Only                 | True                                                                                         |
| Object-Category             | 2                                                                                            |
| Default-Object-Category     | \-                                                                                           |
| Governs-Id                  | 2.5.6.0                                                                                      |
| Default-Hiding-Value        | 1                                                                                            |
| Rdn-Att-Id                  | [**Common-Name**](a-cn.md)<br/>                                                       |
| Subclass of                 | **Top**<br/>                                                                           |
| Possible Superiors          | [**Lost-And-Found**](c-lostandfound.md)                                                     |
| Auxiliary Classes           | \-                                                                                           |
| NT-Security-Descriptor      | O:BAG:BAD:S:                                                                                 |
| Default Security Descriptor | D:(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;DA)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;SY)(A;;RPLCLORC;;;AU) |
| System-Flags                | 0x00000010                                                                                   |



## Windows Server 2008 R2 Attributes

This class contains the following attributes for Windows Server 2008 R2:



| Attribute                                                                        | Mandatory | Derived from |
|----------------------------------------------------------------------------------|-----------|--------------|
| [**Admin-Description**](a-admindescription.md)                                  | False     | **Top**      |
| [**Admin-Display-Name**](a-admindisplayname.md)                                 | False     | **Top**      |
| [**Allowed-Attributes**](a-allowedattributes.md)                                | False     | **Top**      |
| [**Allowed-Attributes-Effective**](a-allowedattributeseffective.md)             | False     | **Top**      |
| [**Allowed-Child-Classes**](a-allowedchildclasses.md)                           | False     | **Top**      |
| [**Allowed-Child-Classes-Effective**](a-allowedchildclasseseffective.md)        | False     | **Top**      |
| [**Bridgehead-Server-List-BL**](a-bridgeheadserverlistbl.md)                    | False     | **Top**      |
| [**Canonical-Name**](a-canonicalname.md)                                        | False     | **Top**      |
| [**Common-Name**](a-cn.md)                                                      | False     | **Top**      |
| [**Create-Time-Stamp**](a-createtimestamp.md)                                   | False     | **Top**      |
| [**Description**](a-description.md)                                             | False     | **Top**      |
| [**Display-Name**](a-displayname.md)                                            | False     | **Top**      |
| [**Display-Name-Printable**](a-displaynameprintable.md)                         | False     | **Top**      |
| [**DSA-Signature**](a-dsasignature.md)                                          | False     | **Top**      |
| [**DS-Core-Propagation-Data**](a-dscorepropagationdata.md)                      | False     | **Top**      |
| [**Extension-Name**](a-extensionname.md)                                        | False     | **Top**      |
| [**Flags**](a-flags.md)                                                         | False     | **Top**      |
| [**From-Entry**](a-fromentry.md)                                                | False     | **Top**      |
| [**Frs-Computer-Reference-BL**](a-frscomputerreferencebl.md)                    | False     | **Top**      |
| [**FRS-Member-Reference-BL**](a-frsmemberreferencebl.md)                        | False     | **Top**      |
| [**FSMO-Role-Owner**](a-fsmoroleowner.md)                                       | False     | **Top**      |
| [**Instance-Type**](a-instancetype.md)                                          | True      | **Top**      |
| [**Is-Critical-System-Object**](a-iscriticalsystemobject.md)                    | False     | **Top**      |
| [**Is-Deleted**](a-isdeleted.md)                                                | False     | **Top**      |
| [**Is-Member-Of-DL**](a-memberof.md)                                            | False     | **Top**      |
| [**Is-Privilege-Holder**](a-isprivilegeholder.md)                               | False     | **Top**      |
| [**Is-Recycled**](a-isrecycled.md)                                              | False     | **Top**      |
| [**Last-Known-Parent**](a-lastknownparent.md)                                   | False     | **Top**      |
| [**Managed-Objects**](a-managedobjects.md)                                      | False     | **Top**      |
| [**Mastered-By**](a-masteredby.md)                                              | False     | **Top**      |
| [**Modify-Time-Stamp**](a-modifytimestamp.md)                                   | False     | **Top**      |
| [**ms-COM-PartitionSetLink**](a-mscom-partitionsetlink.md)                      | False     | **Top**      |
| [**ms-COM-UserLink**](a-mscom-userlink.md)                                      | False     | **Top**      |
| [**ms-DFSR-ComputerReferenceBL**](a-msdfsr-computerreferencebl.md)              | False     | **Top**      |
| [**ms-DFSR-MemberReferenceBL**](a-msdfsr-memberreferencebl.md)                  | False     | **Top**      |
| [**ms-DS-Approx-Immed-Subordinates**](a-msds-approx-immed-subordinates.md)      | False     | **Top**      |
| [**ms-DS-AuthenticatedTo-Accountlist**](a-msds-authenticatedtoaccountlist.md)   | False     | **Top**      |
| [**MS-DS-Consistency-Child-Count**](a-ms-ds-consistencychildcount.md)           | False     | **Top**      |
| [**MS-DS-Consistency-Guid**](a-ms-ds-consistencyguid.md)                        | False     | **Top**      |
| [**ms-DS-Enabled-Feature-BL**](a-msds-enabledfeaturebl.md)                      | False     | **Top**      |
| [**ms-DS-Host-Service-Account-BL**](a-msds-hostserviceaccountbl.md)             | False     | **Top**      |
| [**ms-DS-Is-Domain-For**](a-msds-isdomainfor.md)                                | False     | **Top**      |
| [**ms-DS-Is-Full-Replica-For**](a-msds-isfullreplicafor.md)                     | False     | **Top**      |
| [**ms-DS-Is-Partial-Replica-For**](a-msds-ispartialreplicafor.md)               | False     | **Top**      |
| [**ms-DS-KrbTgt-Link-BL**](a-msds-krbtgtlinkbl.md)                              | False     | **Top**      |
| [**ms-DS-Last-Known-RDN**](a-msds-lastknownrdn.md)                              | False     | **Top**      |
| [**ms-DS-local-Effective-Deletion-Time**](a-msds-localeffectivedeletiontime.md) | False     | **Top**      |
| [**ms-DS-local-Effective-Recycle-Time**](a-msds-localeffectiverecycletime.md)   | False     | **Top**      |
| [**ms-DS-Mastered-By**](a-msds-masteredby.md)                                   | False     | **Top**      |
| [**ms-DS-Members-For-Az-Role-BL**](a-msds-membersforazrolebl.md)                | False     | **Top**      |
| [**ms-DS-NC-Repl-Cursors**](a-msds-ncreplcursors.md)                            | False     | **Top**      |
| [**ms-DS-NC-Repl-Inbound-Neighbors**](a-msds-ncreplinboundneighbors.md)         | False     | **Top**      |
| [**ms-DS-NC-Repl-Outbound-Neighbors**](a-msds-ncreploutboundneighbors.md)       | False     | **Top**      |
| [**ms-DS-NC-RO-Replica-Locations-BL**](a-msds-nc-ro-replica-locations-bl.md)    | False     | **Top**      |
| [**ms-DS-NC-Type**](a-msds-nctype.md)                                           | False     | **Top**      |
| [**ms-DS-Non-Members-BL**](a-msds-nonmembersbl.md)                              | False     | **Top**      |
| [**ms-DS-Object-Reference-BL**](a-msds-objectreferencebl.md)                    | False     | **Top**      |
| [**ms-DS-OIDToGroup-Link-BL**](a-msds-oidtogrouplinkbl.md)                      | False     | **Top**      |
| [**ms-DS-Operations-For-Az-Role-BL**](a-msds-operationsforazrolebl.md)          | False     | **Top**      |
| [**ms-DS-Operations-For-Az-Task-BL**](a-msds-operationsforaztaskbl.md)          | False     | **Top**      |
| [**ms-DS-Principal-Name**](a-msds-principalname.md)                             | False     | **Top**      |
| [**ms-DS-PSO-Applied**](a-msds-psoapplied.md)                                   | False     | **Top**      |
| [**ms-DS-Repl-Attribute-Meta-Data**](a-msds-replattributemetadata.md)           | False     | **Top**      |
| [**ms-DS-Repl-Value-Meta-Data**](a-msds-replvaluemetadata.md)                   | False     | **Top**      |
| [**ms-DS-Revealed-DSAs**](a-msds-revealeddsas.md)                               | False     | **Top**      |
| [**ms-DS-Revealed-List-BL**](a-msds-revealedlistbl.md)                          | False     | **Top**      |
| [**ms-DS-Tasks-For-Az-Role-BL**](a-msds-tasksforazrolebl.md)                    | False     | **Top**      |
| [**ms-DS-Tasks-For-Az-Task-BL**](a-msds-tasksforaztaskbl.md)                    | False     | **Top**      |
| [**ms-Exch-Owner-BL**](a-ownerbl.md)                                            | False     | **Top**      |
| [**msSFU-30-Posix-Member-Of**](a-mssfu30posixmemberof.md)                       | False     | **Top**      |
| [**netboot-SCP-BL**](a-netbootscpbl.md)                                         | False     | **Top**      |
| [**Non-Security-Member-BL**](a-nonsecuritymemberbl.md)                          | False     | **Top**      |
| [**NT-Security-Descriptor**](a-ntsecuritydescriptor.md)                         | True      | **Top**      |
| [**Obj-Dist-Name**](a-distinguishedname.md)                                     | False     | **Top**      |
| [**Object-Category**](a-objectcategory.md)                                      | True      | **Top**      |
| [**Object-Class**](a-objectclass.md)                                            | True      | **Top**      |
| [**Object-Guid**](a-objectguid.md)                                              | False     | **Top**      |
| [**Object-Version**](a-objectversion.md)                                        | False     | **Top**      |
| [**Other-Well-Known-Objects**](a-otherwellknownobjects.md)                      | False     | **Top**      |
| [**Partial-Attribute-Deletion-List**](a-partialattributedeletionlist.md)        | False     | **Top**      |
| [**Partial-Attribute-Set**](a-partialattributeset.md)                           | False     | **Top**      |
| [**Possible-Inferiors**](a-possibleinferiors.md)                                | False     | **Top**      |
| [**Proxied-Object-Name**](a-proxiedobjectname.md)                               | False     | **Top**      |
| [**Proxy-Addresses**](a-proxyaddresses.md)                                      | False     | **Top**      |
| [**Query-Policy-BL**](a-querypolicybl.md)                                       | False     | **Top**      |
| [**RDN**](a-name.md)                                                            | False     | **Top**      |
| [**Repl-Property-Meta-Data**](a-replpropertymetadata.md)                        | False     | **Top**      |
| [**Repl-UpToDate-Vector**](a-repluptodatevector.md)                             | False     | **Top**      |
| [**Reports**](a-directreports.md)                                               | False     | **Top**      |
| [**Reps-From**](a-repsfrom.md)                                                  | False     | **Top**      |
| [**Reps-To**](a-repsto.md)                                                      | False     | **Top**      |
| [**Revision**](a-revision.md)                                                   | False     | **Top**      |
| [**SD-Rights-Effective**](a-sdrightseffective.md)                               | False     | **Top**      |
| [**Server-Reference-BL**](a-serverreferencebl.md)                               | False     | **Top**      |
| [**Show-In-Advanced-View-Only**](a-showinadvancedviewonly.md)                   | False     | **Top**      |
| [**Site-Object-BL**](a-siteobjectbl.md)                                         | False     | **Top**      |
| [**Structural-Object-Class**](a-structuralobjectclass.md)                       | False     | **Top**      |
| [**Sub-Refs**](a-subrefs.md)                                                    | False     | **Top**      |
| [**SubSchemaSubEntry**](a-subschemasubentry.md)                                 | False     | **Top**      |
| [**System-Flags**](a-systemflags.md)                                            | False     | **Top**      |
| [**USN-Changed**](a-usnchanged.md)                                              | False     | **Top**      |
| [**USN-Created**](a-usncreated.md)                                              | False     | **Top**      |
| [**USN-DSA-Last-Obj-Removed**](a-usndsalastobjremoved.md)                       | False     | **Top**      |
| [**USN-Intersite**](a-usnintersite.md)                                          | False     | **Top**      |
| [**USN-Last-Obj-Rem**](a-usnlastobjrem.md)                                      | False     | **Top**      |
| [**USN-Source**](a-usnsource.md)                                                | False     | **Top**      |
| [**Wbem-Path**](a-wbempath.md)                                                  | False     | **Top**      |
| [**Well-Known-Objects**](a-wellknownobjects.md)                                 | False     | **Top**      |
| [**When-Changed**](a-whenchanged.md)                                            | False     | **Top**      |
| [**When-Created**](a-whencreated.md)                                            | False     | **Top**      |
| [**WWW-Home-Page**](a-wwwhomepage.md)                                           | False     | **Top**      |
| [**WWW-Page-Other**](a-url.md)                                                  | False     | **Top**      |



## Windows Server 2012

-   [Attributes](#windows-server-2012-attributes)



| Entry | Value |
|-----------------------------|----------------------------------------------------------------------------------------------|
| System-Only                 | True                                                                                         |
| Object-Category             | 2                                                                                            |
| Default-Object-Category     | \-                                                                                           |
| Governs-Id                  | 2.5.6.0                                                                                      |
| Default-Hiding-Value        | 1                                                                                            |
| Rdn-Att-Id                  | [**Common-Name**](a-cn.md)<br/>                                                       |
| Subclass of                 | **Top**<br/>                                                                           |
| Possible Superiors          | [**Lost-And-Found**](c-lostandfound.md)                                                     |
| Auxiliary Classes           | \-                                                                                           |
| NT-Security-Descriptor      | O:BAG:BAD:S:                                                                                 |
| Default Security Descriptor | D:(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;DA)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;SY)(A;;RPLCLORC;;;AU) |
| System-Flags                | 0x00000010                                                                                   |



## Windows Server 2012 Attributes

This class contains the following attributes for Windows Server 2012:



| Attribute                                                                                    | Mandatory | Derived from |
|----------------------------------------------------------------------------------------------|-----------|--------------|
| [**Admin-Description**](a-admindescription.md)                                              | False     | **Top**      |
| [**Admin-Display-Name**](a-admindisplayname.md)                                             | False     | **Top**      |
| [**Allowed-Attributes**](a-allowedattributes.md)                                            | False     | **Top**      |
| [**Allowed-Attributes-Effective**](a-allowedattributeseffective.md)                         | False     | **Top**      |
| [**Allowed-Child-Classes**](a-allowedchildclasses.md)                                       | False     | **Top**      |
| [**Allowed-Child-Classes-Effective**](a-allowedchildclasseseffective.md)                    | False     | **Top**      |
| [**Bridgehead-Server-List-BL**](a-bridgeheadserverlistbl.md)                                | False     | **Top**      |
| [**Canonical-Name**](a-canonicalname.md)                                                    | False     | **Top**      |
| [**Common-Name**](a-cn.md)                                                                  | False     | **Top**      |
| [**Create-Time-Stamp**](a-createtimestamp.md)                                               | False     | **Top**      |
| [**Description**](a-description.md)                                                         | False     | **Top**      |
| [**Display-Name**](a-displayname.md)                                                        | False     | **Top**      |
| [**Display-Name-Printable**](a-displaynameprintable.md)                                     | False     | **Top**      |
| [**DSA-Signature**](a-dsasignature.md)                                                      | False     | **Top**      |
| [**DS-Core-Propagation-Data**](a-dscorepropagationdata.md)                                  | False     | **Top**      |
| [**Extension-Name**](a-extensionname.md)                                                    | False     | **Top**      |
| [**Flags**](a-flags.md)                                                                     | False     | **Top**      |
| [**From-Entry**](a-fromentry.md)                                                            | False     | **Top**      |
| [**Frs-Computer-Reference-BL**](a-frscomputerreferencebl.md)                                | False     | **Top**      |
| [**FRS-Member-Reference-BL**](a-frsmemberreferencebl.md)                                    | False     | **Top**      |
| [**FSMO-Role-Owner**](a-fsmoroleowner.md)                                                   | False     | **Top**      |
| [**Instance-Type**](a-instancetype.md)                                                      | True      | **Top**      |
| [**Is-Critical-System-Object**](a-iscriticalsystemobject.md)                                | False     | **Top**      |
| [**Is-Deleted**](a-isdeleted.md)                                                            | False     | **Top**      |
| [**Is-Member-Of-DL**](a-memberof.md)                                                        | False     | **Top**      |
| [**Is-Privilege-Holder**](a-isprivilegeholder.md)                                           | False     | **Top**      |
| [**Is-Recycled**](a-isrecycled.md)                                                          | False     | **Top**      |
| [**Last-Known-Parent**](a-lastknownparent.md)                                               | False     | **Top**      |
| [**Managed-Objects**](a-managedobjects.md)                                                  | False     | **Top**      |
| [**Mastered-By**](a-masteredby.md)                                                          | False     | **Top**      |
| [**Modify-Time-Stamp**](a-modifytimestamp.md)                                               | False     | **Top**      |
| [**ms-COM-PartitionSetLink**](a-mscom-partitionsetlink.md)                                  | False     | **Top**      |
| [**ms-COM-UserLink**](a-mscom-userlink.md)                                                  | False     | **Top**      |
| [**ms-DFSR-ComputerReferenceBL**](a-msdfsr-computerreferencebl.md)                          | False     | **Top**      |
| [**ms-DFSR-MemberReferenceBL**](a-msdfsr-memberreferencebl.md)                              | False     | **Top**      |
| [**ms-DS-Approx-Immed-Subordinates**](a-msds-approx-immed-subordinates.md)                  | False     | **Top**      |
| [**ms-DS-AuthenticatedTo-Accountlist**](a-msds-authenticatedtoaccountlist.md)               | False     | **Top**      |
| [**ms-DS-Claim-Shares-Possible-Values-With-BL**](a-msds-claimsharespossiblevalueswithbl.md) | False     | **Top**      |
| [**MS-DS-Consistency-Child-Count**](a-ms-ds-consistencychildcount.md)                       | False     | **Top**      |
| [**MS-DS-Consistency-Guid**](a-ms-ds-consistencyguid.md)                                    | False     | **Top**      |
| [**ms-DS-Enabled-Feature-BL**](a-msds-enabledfeaturebl.md)                                  | False     | **Top**      |
| [**ms-DS-Host-Service-Account-BL**](a-msds-hostserviceaccountbl.md)                         | False     | **Top**      |
| [**ms-DS-Is-Domain-For**](a-msds-isdomainfor.md)                                            | False     | **Top**      |
| [**ms-DS-Is-Full-Replica-For**](a-msds-isfullreplicafor.md)                                 | False     | **Top**      |
| [**ms-DS-Is-Partial-Replica-For**](a-msds-ispartialreplicafor.md)                           | False     | **Top**      |
| [**ms-DS-Is-Primary-Computer-For**](a-msds-isprimarycomputerfor.md)                         | False     | **Top**      |
| [**ms-DS-KrbTgt-Link-BL**](a-msds-krbtgtlinkbl.md)                                          | False     | **Top**      |
| [**ms-DS-Last-Known-RDN**](a-msds-lastknownrdn.md)                                          | False     | **Top**      |
| [**ms-DS-local-Effective-Deletion-Time**](a-msds-localeffectivedeletiontime.md)             | False     | **Top**      |
| [**ms-DS-local-Effective-Recycle-Time**](a-msds-localeffectiverecycletime.md)               | False     | **Top**      |
| [**ms-DS-Mastered-By**](a-msds-masteredby.md)                                               | False     | **Top**      |
| [**ms-DS-Members-For-Az-Role-BL**](a-msds-membersforazrolebl.md)                            | False     | **Top**      |
| [**ms-DS-Members-Of-Resource-Property-List-BL**](a-msds-membersofresourcepropertylistbl.md) | False     | **Top**      |
| [**ms-DS-NC-Repl-Cursors**](a-msds-ncreplcursors.md)                                        | False     | **Top**      |
| [**ms-DS-NC-Repl-Inbound-Neighbors**](a-msds-ncreplinboundneighbors.md)                     | False     | **Top**      |
| [**ms-DS-NC-Repl-Outbound-Neighbors**](a-msds-ncreploutboundneighbors.md)                   | False     | **Top**      |
| [**ms-DS-NC-RO-Replica-Locations-BL**](a-msds-nc-ro-replica-locations-bl.md)                | False     | **Top**      |
| [**ms-DS-NC-Type**](a-msds-nctype.md)                                                       | False     | **Top**      |
| [**ms-DS-Non-Members-BL**](a-msds-nonmembersbl.md)                                          | False     | **Top**      |
| [**ms-DS-Object-Reference-BL**](a-msds-objectreferencebl.md)                                | False     | **Top**      |
| [**ms-DS-OIDToGroup-Link-BL**](a-msds-oidtogrouplinkbl.md)                                  | False     | **Top**      |
| [**ms-DS-Operations-For-Az-Role-BL**](a-msds-operationsforazrolebl.md)                      | False     | **Top**      |
| [**ms-DS-Operations-For-Az-Task-BL**](a-msds-operationsforaztaskbl.md)                      | False     | **Top**      |
| [**ms-DS-Principal-Name**](a-msds-principalname.md)                                         | False     | **Top**      |
| [**ms-DS-PSO-Applied**](a-msds-psoapplied.md)                                               | False     | **Top**      |
| [**ms-DS-Repl-Attribute-Meta-Data**](a-msds-replattributemetadata.md)                       | False     | **Top**      |
| [**ms-DS-Repl-Value-Meta-Data**](a-msds-replvaluemetadata.md)                               | False     | **Top**      |
| [**ms-DS-Revealed-DSAs**](a-msds-revealeddsas.md)                                           | False     | **Top**      |
| [**ms-DS-Revealed-List-BL**](a-msds-revealedlistbl.md)                                      | False     | **Top**      |
| [**ms-DS-Tasks-For-Az-Role-BL**](a-msds-tasksforazrolebl.md)                                | False     | **Top**      |
| [**ms-DS-Tasks-For-Az-Task-BL**](a-msds-tasksforaztaskbl.md)                                | False     | **Top**      |
| [**ms-DS-TDO-Egress-BL**](a-msds-tdoegressbl.md)                                            | False     | **Top**      |
| [**ms-DS-TDO-Ingress-BL**](a-msds-tdoingressbl.md)                                          | False     | **Top**      |
| [**ms-DS-Value-Type-Reference-BL**](a-msds-valuetypereferencebl.md)                         | False     | **Top**      |
| [**ms-Exch-Owner-BL**](a-ownerbl.md)                                                        | False     | **Top**      |
| [**msSFU-30-Posix-Member-Of**](a-mssfu30posixmemberof.md)                                   | False     | **Top**      |
| [**netboot-SCP-BL**](a-netbootscpbl.md)                                                     | False     | **Top**      |
| [**Non-Security-Member-BL**](a-nonsecuritymemberbl.md)                                      | False     | **Top**      |
| [**NT-Security-Descriptor**](a-ntsecuritydescriptor.md)                                     | True      | **Top**      |
| [**Obj-Dist-Name**](a-distinguishedname.md)                                                 | False     | **Top**      |
| [**Object-Category**](a-objectcategory.md)                                                  | True      | **Top**      |
| [**Object-Class**](a-objectclass.md)                                                        | True      | **Top**      |
| [**Object-Guid**](a-objectguid.md)                                                          | False     | **Top**      |
| [**Object-Version**](a-objectversion.md)                                                    | False     | **Top**      |
| [**Other-Well-Known-Objects**](a-otherwellknownobjects.md)                                  | False     | **Top**      |
| [**Partial-Attribute-Deletion-List**](a-partialattributedeletionlist.md)                    | False     | **Top**      |
| [**Partial-Attribute-Set**](a-partialattributeset.md)                                       | False     | **Top**      |
| [**Possible-Inferiors**](a-possibleinferiors.md)                                            | False     | **Top**      |
| [**Proxied-Object-Name**](a-proxiedobjectname.md)                                           | False     | **Top**      |
| [**Proxy-Addresses**](a-proxyaddresses.md)                                                  | False     | **Top**      |
| [**Query-Policy-BL**](a-querypolicybl.md)                                                   | False     | **Top**      |
| [**RDN**](a-name.md)                                                                        | False     | **Top**      |
| [**Repl-Property-Meta-Data**](a-replpropertymetadata.md)                                    | False     | **Top**      |
| [**Repl-UpToDate-Vector**](a-repluptodatevector.md)                                         | False     | **Top**      |
| [**Reports**](a-directreports.md)                                                           | False     | **Top**      |
| [**Reps-From**](a-repsfrom.md)                                                              | False     | **Top**      |
| [**Reps-To**](a-repsto.md)                                                                  | False     | **Top**      |
| [**Revision**](a-revision.md)                                                               | False     | **Top**      |
| [**SD-Rights-Effective**](a-sdrightseffective.md)                                           | False     | **Top**      |
| [**Server-Reference-BL**](a-serverreferencebl.md)                                           | False     | **Top**      |
| [**Show-In-Advanced-View-Only**](a-showinadvancedviewonly.md)                               | False     | **Top**      |
| [**Site-Object-BL**](a-siteobjectbl.md)                                                     | False     | **Top**      |
| [**Structural-Object-Class**](a-structuralobjectclass.md)                                   | False     | **Top**      |
| [**Sub-Refs**](a-subrefs.md)                                                                | False     | **Top**      |
| [**SubSchemaSubEntry**](a-subschemasubentry.md)                                             | False     | **Top**      |
| [**System-Flags**](a-systemflags.md)                                                        | False     | **Top**      |
| [**USN-Changed**](a-usnchanged.md)                                                          | False     | **Top**      |
| [**USN-Created**](a-usncreated.md)                                                          | False     | **Top**      |
| [**USN-DSA-Last-Obj-Removed**](a-usndsalastobjremoved.md)                                   | False     | **Top**      |
| [**USN-Intersite**](a-usnintersite.md)                                                      | False     | **Top**      |
| [**USN-Last-Obj-Rem**](a-usnlastobjrem.md)                                                  | False     | **Top**      |
| [**USN-Source**](a-usnsource.md)                                                            | False     | **Top**      |
| [**Wbem-Path**](a-wbempath.md)                                                              | False     | **Top**      |
| [**Well-Known-Objects**](a-wellknownobjects.md)                                             | False     | **Top**      |
| [**When-Changed**](a-whenchanged.md)                                                        | False     | **Top**      |
| [**When-Created**](a-whencreated.md)                                                        | False     | **Top**      |
| [**WWW-Home-Page**](a-wwwhomepage.md)                                                       | False     | **Top**      |
| [**WWW-Page-Other**](a-url.md)                                                              | False     | **Top**      |



 

 





