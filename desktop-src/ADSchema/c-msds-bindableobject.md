---
title: ms-DS-Bindable-Object class
description: Auxiliary class to represent a bindable object. Any user-defined class that represents an entity that can be used to bind to the directory (that is, a user), should include this auxiliary class.
ms.assetid: 181b3e2b-9442-4f11-9af7-4697491115f3
ms.tgt_platform: multiple
keywords:
- ms-DS-Bindable-Object class AD Schema
- msDS-BindableObject class AD Schema
topic_type:
- apiref
api_name:
- ms-DS-Bindable-Object
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# ms-DS-Bindable-Object class

Auxiliary class to represent a bindable object. Any user-defined class that represents an entity that can be used to bind to the directory (that is, a user), should include this auxiliary class.



| Entry | Value |
|-------------------|--------------------------------------|
| CN                | ms-DS-Bindable-Object                |
| Ldap-Display-Name | msDS-BindableObject                  |
| Update Privilege  | \-                                   |
| Update Frequency  | \-                                   |
| Schema-Id-Guid    | 89f4a69f-4416-6b49-821d-6e3c4a0ff802 |



## Implementations

-   [**ADAM**](#adam-attributes)

## ADAM

-   [Attributes](#adam-attributes)



| Entry | Value |
|-----------------------------|--------------------------------------------------------------|
| System-Only                 | False                                                        |
| Object-Category             | 3                                                            |
| Default-Object-Category     | \-                                                           |
| Governs-Id                  | 1.2.840.113556.1.5.244                                       |
| Default-Hiding-Value        | 1                                                            |
| Rdn-Att-Id                  | \-                                                           |
| Subclass of                 | [**Security-Principal**](c-securityprincipal.md)<br/> |
| Possible Superiors          | \-                                                           |
| Auxiliary Classes           | \-                                                           |
| NT-Security-Descriptor      | O:BAG:BAD:S:                                                 |
| Default Security Descriptor | \-                                                           |
| System-Flags                | 0x00000010                                                   |



## ADAM Attributes

This class contains the following attributes for ADAM:



| Attribute                                                                                      | Mandatory | Derived from                                                                                 |
|------------------------------------------------------------------------------------------------|-----------|----------------------------------------------------------------------------------------------|
| [**Account-Expires**](a-accountexpires.md)                                                    | False     | **ms-DS-Bindable-Object**                                                                    |
| [**Admin-Description**](a-admindescription.md)                                                | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Admin-Display-Name**](a-admindisplayname.md)                                               | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Allowed-Attributes**](a-allowedattributes.md)                                              | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Allowed-Attributes-Effective**](a-allowedattributeseffective.md)                           | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Allowed-Child-Classes**](a-allowedchildclasses.md)                                         | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Allowed-Child-Classes-Effective**](a-allowedchildclasseseffective.md)                      | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Bad-Password-Time**](a-badpasswordtime.md)                                                 | False     | **ms-DS-Bindable-Object**                                                                    |
| [**Bad-Pwd-Count**](a-badpwdcount.md)                                                         | False     | **ms-DS-Bindable-Object**                                                                    |
| [**Bridgehead-Server-List-BL**](a-bridgeheadserverlistbl.md)                                  | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Canonical-Name**](a-canonicalname.md)                                                      | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Common-Name**](a-cn.md)                                                                    | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Create-Time-Stamp**](a-createtimestamp.md)                                                 | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Description**](a-description.md)                                                           | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Display-Name**](a-displayname.md)                                                          | False     | [**Top**](c-top.md)<br/>                                                              |
| [**DSA-Signature**](a-dsasignature.md)                                                        | False     | [**Top**](c-top.md)<br/>                                                              |
| [**DS-Core-Propagation-Data**](a-dscorepropagationdata.md)                                    | False     | [**Top**](c-top.md)<br/>                                                              |
| [**From-Entry**](a-fromentry.md)                                                              | False     | [**Top**](c-top.md)<br/>                                                              |
| [**FSMO-Role-Owner**](a-fsmoroleowner.md)                                                     | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Instance-Type**](a-instancetype.md)                                                        | True      | [**Top**](c-top.md)<br/>                                                              |
| [**Is-Critical-System-Object**](a-iscriticalsystemobject.md)                                  | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Is-Deleted**](a-isdeleted.md)                                                              | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Is-Member-Of-DL**](a-memberof.md)                                                          | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Last-Known-Parent**](a-lastknownparent.md)                                                 | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Last-Logon-Timestamp**](a-lastlogontimestamp.md)                                           | False     | **ms-DS-Bindable-Object**                                                                    |
| [**Lockout-Time**](a-lockouttime.md)                                                          | False     | **ms-DS-Bindable-Object**                                                                    |
| [**Managed-Objects**](a-managedobjects.md)                                                    | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Mastered-By**](a-masteredby.md)                                                            | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Modify-Time-Stamp**](a-modifytimestamp.md)                                                 | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-DS-Approx-Immed-Subordinates**](a-msds-approx-immed-subordinates.md)                    | False     | [**Top**](c-top.md)<br/>                                                              |
| [**MS-DS-Consistency-Child-Count**](a-ms-ds-consistencychildcount.md)                         | False     | [**Top**](c-top.md)<br/>                                                              |
| [**MS-DS-Consistency-Guid**](a-ms-ds-consistencyguid.md)                                      | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-DS-Disable-For-Instances-BL**](a-msds-disableforinstancesbl.md)                         | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-DS-Mastered-By**](a-msds-masteredby.md)                                                 | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-DS-NC-Repl-Cursors**](a-msds-ncreplcursors.md)                                          | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-DS-NC-Repl-Inbound-Neighbors**](a-msds-ncreplinboundneighbors.md)                       | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-DS-NC-Repl-Outbound-Neighbors**](a-msds-ncreploutboundneighbors.md)                     | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-DS-Repl-Attribute-Meta-Data**](a-msds-replattributemetadata.md)                         | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-DS-Repl-Value-Meta-Data**](a-msds-replvaluemetadata.md)                                 | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-DS-Service-Account-BL**](a-msds-serviceaccountbl.md)                                    | False     | [**Top**](c-top.md)<br/>                                                              |
| [**ms-DS-User-Account-Auto-Locked**](a-ms-ds-useraccountautolocked.md)                        | False     | **ms-DS-Bindable-Object**                                                                    |
| [**ms-DS-User-Account-Control-Computed**](a-msds-user-account-control-computed.md)            | False     | **ms-DS-Bindable-Object**                                                                    |
| [**ms-DS-User-Account-Disabled**](a-msds-useraccountdisabled.md)                              | False     | **ms-DS-Bindable-Object**                                                                    |
| [**ms-DS-User-Dont-Expire-Password**](a-msds-userdontexpirepassword.md)                       | False     | **ms-DS-Bindable-Object**                                                                    |
| [**ms-DS-User-Encrypted-Text-Password-Allowed**](a-ms-ds-userencryptedtextpasswordallowed.md) | False     | **ms-DS-Bindable-Object**                                                                    |
| [**ms-DS-User-Password-Expired**](a-msds-userpasswordexpired.md)                              | False     | **ms-DS-Bindable-Object**                                                                    |
| [**ms-DS-User-Password-Not-Required**](a-ms-ds-userpasswordnotrequired.md)                    | False     | **ms-DS-Bindable-Object**                                                                    |
| [**Nt-Pwd-History**](a-ntpwdhistory.md)                                                       | False     | **ms-DS-Bindable-Object**                                                                    |
| [**NT-Security-Descriptor**](a-ntsecuritydescriptor.md)                                       | True      | [**Security-Principal**](c-securityprincipal.md)<br/> [**Top**](c-top.md)<br/> |
| [**Obj-Dist-Name**](a-distinguishedname.md)                                                   | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Object-Category**](a-objectcategory.md)                                                    | True      | [**Top**](c-top.md)<br/>                                                              |
| [**Object-Class**](a-objectclass.md)                                                          | True      | [**Top**](c-top.md)<br/>                                                              |
| [**Object-Guid**](a-objectguid.md)                                                            | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Object-Sid**](a-objectsid.md)                                                              | True      | [**Security-Principal**](c-securityprincipal.md)<br/>                                 |
| [**Object-Version**](a-objectversion.md)                                                      | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Other-Well-Known-Objects**](a-otherwellknownobjects.md)                                    | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Partial-Attribute-Deletion-List**](a-partialattributedeletionlist.md)                      | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Partial-Attribute-Set**](a-partialattributeset.md)                                         | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Possible-Inferiors**](a-possibleinferiors.md)                                              | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Proxied-Object-Name**](a-proxiedobjectname.md)                                             | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Proxy-Addresses**](a-proxyaddresses.md)                                                    | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Pwd-Last-Set**](a-pwdlastset.md)                                                           | False     | **ms-DS-Bindable-Object**                                                                    |
| [**Query-Policy-BL**](a-querypolicybl.md)                                                     | False     | [**Top**](c-top.md)<br/>                                                              |
| [**RDN**](a-name.md)                                                                          | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Repl-Property-Meta-Data**](a-replpropertymetadata.md)                                      | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Repl-UpToDate-Vector**](a-repluptodatevector.md)                                           | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Reps-From**](a-repsfrom.md)                                                                | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Reps-To**](a-repsto.md)                                                                    | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Revision**](a-revision.md)                                                                 | False     | [**Top**](c-top.md)<br/>                                                              |
| [**SD-Rights-Effective**](a-sdrightseffective.md)                                             | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Server-Reference-BL**](a-serverreferencebl.md)                                             | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Show-In-Advanced-View-Only**](a-showinadvancedviewonly.md)                                 | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Site-Object-BL**](a-siteobjectbl.md)                                                       | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Structural-Object-Class**](a-structuralobjectclass.md)                                     | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Sub-Refs**](a-subrefs.md)                                                                  | False     | [**Top**](c-top.md)<br/>                                                              |
| [**SubSchemaSubEntry**](a-subschemasubentry.md)                                               | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Supplemental-Credentials**](a-supplementalcredentials.md)                                  | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                 |
| [**System-Flags**](a-systemflags.md)                                                          | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Token-Groups**](a-tokengroups.md)                                                          | False     | [**Security-Principal**](c-securityprincipal.md)<br/>                                 |
| [**Unicode-Pwd**](a-unicodepwd.md)                                                            | False     | **ms-DS-Bindable-Object**                                                                    |
| [**USN-Changed**](a-usnchanged.md)                                                            | False     | [**Top**](c-top.md)<br/>                                                              |
| [**USN-Created**](a-usncreated.md)                                                            | False     | [**Top**](c-top.md)<br/>                                                              |
| [**USN-DSA-Last-Obj-Removed**](a-usndsalastobjremoved.md)                                     | False     | [**Top**](c-top.md)<br/>                                                              |
| [**USN-Intersite**](a-usnintersite.md)                                                        | False     | [**Top**](c-top.md)<br/>                                                              |
| [**USN-Last-Obj-Rem**](a-usnlastobjrem.md)                                                    | False     | [**Top**](c-top.md)<br/>                                                              |
| [**USN-Source**](a-usnsource.md)                                                              | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Wbem-Path**](a-wbempath.md)                                                                | False     | [**Top**](c-top.md)<br/>                                                              |
| [**Well-Known-Objects**](a-wellknownobjects.md)                                               | False     | [**Top**](c-top.md)<br/>                                                              |
| [**When-Changed**](a-whenchanged.md)                                                          | False     | [**Top**](c-top.md)<br/>                                                              |
| [**When-Created**](a-whencreated.md)                                                          | False     | [**Top**](c-top.md)<br/>                                                              |
| [**WWW-Home-Page**](a-wwwhomepage.md)                                                         | False     | [**Top**](c-top.md)<br/>                                                              |
| [**WWW-Page-Other**](a-url.md)                                                                | False     | [**Top**](c-top.md)<br/>                                                              |



 

 





