---
title: ms-DS-Service-Connection-Point-Publication-Service class
description: Stores configuration options for the Service Connection Point publication service in ADAM.
ms.assetid: 30b4df70-a03b-4d42-b200-75bfa6cf8273
ms.tgt_platform: multiple
keywords:
- ms-DS-Service-Connection-Point-Publication-Service class AD Schema
- msDS-ServiceConnectionPointPublicationService class AD Schema
topic_type:
- apiref
api_name:
- ms-DS-Service-Connection-Point-Publication-Service
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# ms-DS-Service-Connection-Point-Publication-Service class

Stores configuration options for the Service Connection Point publication service in ADAM.



| Entry | Value |
|-------------------|----------------------------------------------------|
| CN                | ms-DS-Service-Connection-Point-Publication-Service |
| Ldap-Display-Name | msDS-ServiceConnectionPointPublicationService      |
| Update Privilege  | \-                                                 |
| Update Frequency  | \-                                                 |
| Schema-Id-Guid    | d33f5da6-b009-7e48-8268-b2305529e933               |



## Implementations

-   [**ADAM**](#adam-attributes)

## ADAM

-   [Attributes](#adam-attributes)



| Entry | Value |
|-----------------------------|----------------------------------------|
| System-Only                 | True                                   |
| Object-Category             | 1                                      |
| Default-Object-Category     | \-                                     |
| Governs-Id                  | 1.2.840.113556.1.5.247                 |
| Default-Hiding-Value        | 1                                      |
| Rdn-Att-Id                  | [**Common-Name**](a-cn.md)<br/> |
| Subclass of                 | [**Top**](c-top.md)<br/>        |
| Possible Superiors          | [**NTDS-Service**](c-ntdsservice.md)  |
| Auxiliary Classes           | \-                                     |
| NT-Security-Descriptor      | O:BAG:BAD:S:                           |
| Default Security Descriptor | D:S:                                   |
| System-Flags                | 0x00000000                             |



## ADAM Attributes

This class contains the following attributes for ADAM:



| Attribute                                                                   | Mandatory | Derived from                                           |
|-----------------------------------------------------------------------------|-----------|--------------------------------------------------------|
| [**Admin-Description**](a-admindescription.md)                             | False     | [**Top**](c-top.md)<br/>                        |
| [**Admin-Display-Name**](a-admindisplayname.md)                            | False     | [**Top**](c-top.md)<br/>                        |
| [**Allowed-Attributes**](a-allowedattributes.md)                           | False     | [**Top**](c-top.md)<br/>                        |
| [**Allowed-Attributes-Effective**](a-allowedattributeseffective.md)        | False     | [**Top**](c-top.md)<br/>                        |
| [**Allowed-Child-Classes**](a-allowedchildclasses.md)                      | False     | [**Top**](c-top.md)<br/>                        |
| [**Allowed-Child-Classes-Effective**](a-allowedchildclasseseffective.md)   | False     | [**Top**](c-top.md)<br/>                        |
| [**Bridgehead-Server-List-BL**](a-bridgeheadserverlistbl.md)               | False     | [**Top**](c-top.md)<br/>                        |
| [**Canonical-Name**](a-canonicalname.md)                                   | False     | [**Top**](c-top.md)<br/>                        |
| [**Common-Name**](a-cn.md)                                                 | False     | [**Top**](c-top.md)<br/>                        |
| [**Create-Time-Stamp**](a-createtimestamp.md)                              | False     | [**Top**](c-top.md)<br/>                        |
| [**Description**](a-description.md)                                        | False     | [**Top**](c-top.md)<br/>                        |
| [**Display-Name**](a-displayname.md)                                       | False     | [**Top**](c-top.md)<br/>                        |
| [**DSA-Signature**](a-dsasignature.md)                                     | False     | [**Top**](c-top.md)<br/>                        |
| [**DS-Core-Propagation-Data**](a-dscorepropagationdata.md)                 | False     | [**Top**](c-top.md)<br/>                        |
| [**Enabled**](a-enabled.md)                                                | False     | **ms-DS-Service-Connection-Point-Publication-Service** |
| [**From-Entry**](a-fromentry.md)                                           | False     | [**Top**](c-top.md)<br/>                        |
| [**FSMO-Role-Owner**](a-fsmoroleowner.md)                                  | False     | [**Top**](c-top.md)<br/>                        |
| [**Instance-Type**](a-instancetype.md)                                     | True      | [**Top**](c-top.md)<br/>                        |
| [**Is-Critical-System-Object**](a-iscriticalsystemobject.md)               | False     | [**Top**](c-top.md)<br/>                        |
| [**Is-Deleted**](a-isdeleted.md)                                           | False     | [**Top**](c-top.md)<br/>                        |
| [**Is-Member-Of-DL**](a-memberof.md)                                       | False     | [**Top**](c-top.md)<br/>                        |
| [**Keywords**](a-keywords.md)                                              | False     | **ms-DS-Service-Connection-Point-Publication-Service** |
| [**Last-Known-Parent**](a-lastknownparent.md)                              | False     | [**Top**](c-top.md)<br/>                        |
| [**Managed-Objects**](a-managedobjects.md)                                 | False     | [**Top**](c-top.md)<br/>                        |
| [**Mastered-By**](a-masteredby.md)                                         | False     | [**Top**](c-top.md)<br/>                        |
| [**Modify-Time-Stamp**](a-modifytimestamp.md)                              | False     | [**Top**](c-top.md)<br/>                        |
| [**ms-DS-Approx-Immed-Subordinates**](a-msds-approx-immed-subordinates.md) | False     | [**Top**](c-top.md)<br/>                        |
| [**MS-DS-Consistency-Child-Count**](a-ms-ds-consistencychildcount.md)      | False     | [**Top**](c-top.md)<br/>                        |
| [**MS-DS-Consistency-Guid**](a-ms-ds-consistencyguid.md)                   | False     | [**Top**](c-top.md)<br/>                        |
| [**ms-DS-Disable-For-Instances**](a-msds-disableforinstances.md)           | False     | **ms-DS-Service-Connection-Point-Publication-Service** |
| [**ms-DS-Disable-For-Instances-BL**](a-msds-disableforinstancesbl.md)      | False     | [**Top**](c-top.md)<br/>                        |
| [**ms-DS-Mastered-By**](a-msds-masteredby.md)                              | False     | [**Top**](c-top.md)<br/>                        |
| [**ms-DS-NC-Repl-Cursors**](a-msds-ncreplcursors.md)                       | False     | [**Top**](c-top.md)<br/>                        |
| [**ms-DS-NC-Repl-Inbound-Neighbors**](a-msds-ncreplinboundneighbors.md)    | False     | [**Top**](c-top.md)<br/>                        |
| [**ms-DS-NC-Repl-Outbound-Neighbors**](a-msds-ncreploutboundneighbors.md)  | False     | [**Top**](c-top.md)<br/>                        |
| [**ms-DS-Repl-Attribute-Meta-Data**](a-msds-replattributemetadata.md)      | False     | [**Top**](c-top.md)<br/>                        |
| [**ms-DS-Repl-Value-Meta-Data**](a-msds-replvaluemetadata.md)              | False     | [**Top**](c-top.md)<br/>                        |
| [**ms-DS-SCP-Container**](a-msds-scpcontainer.md)                          | False     | **ms-DS-Service-Connection-Point-Publication-Service** |
| [**ms-DS-Service-Account-BL**](a-msds-serviceaccountbl.md)                 | False     | [**Top**](c-top.md)<br/>                        |
| [**NT-Security-Descriptor**](a-ntsecuritydescriptor.md)                    | True      | [**Top**](c-top.md)<br/>                        |
| [**Obj-Dist-Name**](a-distinguishedname.md)                                | False     | [**Top**](c-top.md)<br/>                        |
| [**Object-Category**](a-objectcategory.md)                                 | True      | [**Top**](c-top.md)<br/>                        |
| [**Object-Class**](a-objectclass.md)                                       | True      | [**Top**](c-top.md)<br/>                        |
| [**Object-Guid**](a-objectguid.md)                                         | False     | [**Top**](c-top.md)<br/>                        |
| [**Object-Version**](a-objectversion.md)                                   | False     | [**Top**](c-top.md)<br/>                        |
| [**Other-Well-Known-Objects**](a-otherwellknownobjects.md)                 | False     | [**Top**](c-top.md)<br/>                        |
| [**Partial-Attribute-Deletion-List**](a-partialattributedeletionlist.md)   | False     | [**Top**](c-top.md)<br/>                        |
| [**Partial-Attribute-Set**](a-partialattributeset.md)                      | False     | [**Top**](c-top.md)<br/>                        |
| [**Possible-Inferiors**](a-possibleinferiors.md)                           | False     | [**Top**](c-top.md)<br/>                        |
| [**Proxied-Object-Name**](a-proxiedobjectname.md)                          | False     | [**Top**](c-top.md)<br/>                        |
| [**Proxy-Addresses**](a-proxyaddresses.md)                                 | False     | [**Top**](c-top.md)<br/>                        |
| [**Query-Policy-BL**](a-querypolicybl.md)                                  | False     | [**Top**](c-top.md)<br/>                        |
| [**RDN**](a-name.md)                                                       | False     | [**Top**](c-top.md)<br/>                        |
| [**Repl-Property-Meta-Data**](a-replpropertymetadata.md)                   | False     | [**Top**](c-top.md)<br/>                        |
| [**Repl-UpToDate-Vector**](a-repluptodatevector.md)                        | False     | [**Top**](c-top.md)<br/>                        |
| [**Reps-From**](a-repsfrom.md)                                             | False     | [**Top**](c-top.md)<br/>                        |
| [**Reps-To**](a-repsto.md)                                                 | False     | [**Top**](c-top.md)<br/>                        |
| [**Revision**](a-revision.md)                                              | False     | [**Top**](c-top.md)<br/>                        |
| [**SD-Rights-Effective**](a-sdrightseffective.md)                          | False     | [**Top**](c-top.md)<br/>                        |
| [**Server-Reference-BL**](a-serverreferencebl.md)                          | False     | [**Top**](c-top.md)<br/>                        |
| [**Show-In-Advanced-View-Only**](a-showinadvancedviewonly.md)              | False     | [**Top**](c-top.md)<br/>                        |
| [**Site-Object-BL**](a-siteobjectbl.md)                                    | False     | [**Top**](c-top.md)<br/>                        |
| [**Structural-Object-Class**](a-structuralobjectclass.md)                  | False     | [**Top**](c-top.md)<br/>                        |
| [**Sub-Refs**](a-subrefs.md)                                               | False     | [**Top**](c-top.md)<br/>                        |
| [**SubSchemaSubEntry**](a-subschemasubentry.md)                            | False     | [**Top**](c-top.md)<br/>                        |
| [**System-Flags**](a-systemflags.md)                                       | False     | [**Top**](c-top.md)<br/>                        |
| [**USN-Changed**](a-usnchanged.md)                                         | False     | [**Top**](c-top.md)<br/>                        |
| [**USN-Created**](a-usncreated.md)                                         | False     | [**Top**](c-top.md)<br/>                        |
| [**USN-DSA-Last-Obj-Removed**](a-usndsalastobjremoved.md)                  | False     | [**Top**](c-top.md)<br/>                        |
| [**USN-Intersite**](a-usnintersite.md)                                     | False     | [**Top**](c-top.md)<br/>                        |
| [**USN-Last-Obj-Rem**](a-usnlastobjrem.md)                                 | False     | [**Top**](c-top.md)<br/>                        |
| [**USN-Source**](a-usnsource.md)                                           | False     | [**Top**](c-top.md)<br/>                        |
| [**Wbem-Path**](a-wbempath.md)                                             | False     | [**Top**](c-top.md)<br/>                        |
| [**Well-Known-Objects**](a-wellknownobjects.md)                            | False     | [**Top**](c-top.md)<br/>                        |
| [**When-Changed**](a-whenchanged.md)                                       | False     | [**Top**](c-top.md)<br/>                        |
| [**When-Created**](a-whencreated.md)                                       | False     | [**Top**](c-top.md)<br/>                        |
| [**WWW-Home-Page**](a-wwwhomepage.md)                                      | False     | [**Top**](c-top.md)<br/>                        |
| [**WWW-Page-Other**](a-url.md)                                             | False     | [**Top**](c-top.md)<br/>                        |



 

 





