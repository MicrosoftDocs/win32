---
title: RootDSE
description: In LDAP 3.0, rootDSE is defined as the root of the directory data tree on a directory server.
ms.assetid: dd5a160d-6604-43ca-878c-6b19e90d3adb
ms.tgt_platform: multiple
keywords:
- rootDSE Active Directory Schema
ms.topic: article
ms.date: 05/31/2018
---

# RootDSE

In LDAP 3.0, rootDSE is defined as the root of the directory data tree on a directory server. The rootDSE is not part of any namespace. The purpose of the rootDSE is to provide data about the directory server. For more information about rootDSE, see [Serverless Binding and RootDSE](https://msdn.microsoft.com/library/ms677945) in the Active Directory SDK documentation.

rootDSE contains the following attributes. All attributes are single-valued unless otherwise noted.



| Attribute                                    | Syntax                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                            |
|----------------------------------------------|--------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **configurationNamingContext**<br/>    | [**String(Teletex)**](s-string-teletex.md)<br/> | Contains the distinguished name for the configuration container.<br/>                                                                                                                                                                                                                                                                                                                                            |
| **currentTime**<br/>                   | [**String(Teletex)**](s-string-teletex.md)<br/> | Contains the current time set on this directory server in Coordinated Universal Time format.<br/>                                                                                                                                                                                                                                                                                                                |
| **defaultNamingContext**<br/>          | [**String(Teletex)**](s-string-teletex.md)<br/> | Contains the distinguished name for the domain of which this directory server is a member.<br/>                                                                                                                                                                                                                                                                                                                  |
| **dnsHostName**<br/>                   | [**String(Teletex)**](s-string-teletex.md)<br/> | Contains the DNS address for this directory server.<br/>                                                                                                                                                                                                                                                                                                                                                         |
| **domainControllerFunctionality**<br/> | [**String(Teletex)**](s-string-teletex.md)<br/> | Indicates the functional level of the domain controller. This can be one of the following values.<br/> "0" - Windows 2000 Mode<br/> "2" - Windows Server 2003 Mode<br/> "3" - Windows Server 2008 Mode<br/>                                                                                                                                                                                    |
| **domainFunctionality**<br/>           | [**String(Teletex)**](s-string-teletex.md)<br/> | Indicates the functional level of the domain. This can be one of the following values.<br/> "0" - Windows 2000 Domain Mode<br/> "1" - Windows Server 2003 Interim Domain Mode<br/> "2" - Windows Server 2003 Domain Mode<br/> "3" - Windows Server 2008 Domain Mode<br/> "4" - Windows Server 2008 R2 Domain Mode<br/>                                                             |
| **dsServiceName**<br/>                 | [**String(Teletex)**](s-string-teletex.md)<br/> | Contains the distinguished name of the NTDS settings object for this directory server.<br/>                                                                                                                                                                                                                                                                                                                      |
| **forestFunctionality**<br/>           | [**String(Teletex)**](s-string-teletex.md)<br/> | Indicates the functional level of the forest. This can be one of the following values.<br/> "0" - Windows 2000 Forest Mode<br/> "1" - Windows Server 2003 Interim Forest Mode<br/> "2" - Windows Server 2003 Forest Mode<br/> "3" - Windows Server 2008 Forest Mode<br/> "4" - Windows Server 2008 R2 Forest Mode<br/>                                                             |
| **highestCommittedUSN**<br/>           | [**String(Teletex)**](s-string-teletex.md)<br/> | Contains the highest update sequence number (USN) on this directory server. Used by directory replication.<br/>                                                                                                                                                                                                                                                                                                  |
| **isGlobalCatalogReady**<br/>          | [**String(Teletex)**](s-string-teletex.md)<br/> | Indicates if the global catalog is fully operational. Contains either "TRUE" or "FALSE".<br/>                                                                                                                                                                                                                                                                                                                    |
| **isSynchronized**<br/>                | [**String(Teletex)**](s-string-teletex.md)<br/> | Indicates if the directory server is fully synchronized. Contains either "TRUE" or "FALSE".<br/>                                                                                                                                                                                                                                                                                                                 |
| **ldapServiceName**<br/>               | [**String(Teletex)**](s-string-teletex.md)<br/> | Contains the Service Principal Name (SPN) for the LDAP server. Used for mutual authentication.<br/>                                                                                                                                                                                                                                                                                                              |
| **namingContexts**<br/>                | [**String(Teletex)**](s-string-teletex.md)<br/> | A multiple-valued attribute that contains the distinguished names for all naming contexts stored on this directory server. By default, a Windows 2000 domain controller contains at least three naming contexts: Schema, Configuration, and one for the domain of which the server is a member.<br/>                                                                                                             |
| **rootDomainNamingContext**<br/>       | [**String(Teletex)**](s-string-teletex.md)<br/> | Contains the distinguished name for the first domain in the forest that contains the domain of which this directory server is a member.<br/>                                                                                                                                                                                                                                                                     |
| **schemaNamingContext**<br/>           | [**String(Teletex)**](s-string-teletex.md)<br/> | Contains the distinguished name for the schema container.<br/>                                                                                                                                                                                                                                                                                                                                                   |
| **serverName**<br/>                    | [**String(Teletex)**](s-string-teletex.md)<br/> | Contains the distinguished name for the server object for this directory server in the configuration container.<br/>                                                                                                                                                                                                                                                                                             |
| **subschemaSubentry**<br/>             | [**String(Teletex)**](s-string-teletex.md)<br/> | Contains the distinguished name for the [**subSchema**](c-subschema.md) object. The **subSchema** object contains properties that expose the supported attributes (in the [**attributeTypes**](a-attributetypes.md) property) and classes (in the [**objectClasses**](a-objectclasses.md) property).<br/> The **subschemaSubentry** property and subschema are defined in LDAP 3.0 (see RFC 2251).<br/> |
| **supportedCapabilities**<br/>         | [**String(Teletex)**](s-string-teletex.md)<br/> | A multiple-valued attribute that contains the capabilities supported by this directory server.<br/>                                                                                                                                                                                                                                                                                                              |
| **supportedControl**<br/>              | [**String(Teletex)**](s-string-teletex.md)<br/> | A multiple-valued attribute that contains the OIDs for extension controls supported by this directory server. See the table below for a list of the possible control OIDs.<br/>                                                                                                                                                                                                                                  |
| **supportedLDAPPolicies**<br/>         | [**String(Teletex)**](s-string-teletex.md)<br/> | A multiple-valued attribute that contains the names of the supported LDAP management policies.<br/>                                                                                                                                                                                                                                                                                                              |
| **supportedLDAPVersion**<br/>          | [**String(Teletex)**](s-string-teletex.md)<br/> | A multiple-valued attribute that contains the LDAP versions (specified by major version number) supported by this directory server.<br/>                                                                                                                                                                                                                                                                         |
| **supportedSASLMechanisms**<br/>       | [**String(Teletex)**](s-string-teletex.md)<br/> | Contains the security mechanisms supported for SASL negotiation (see LDAP RFCs). By default, GSSAPI is supported.<br/>                                                                                                                                                                                                                                                                                           |



 

Active Directory supports the following control OIDs in the **supportedControl** attribute. For more information, see [**LDAPControl**](https://msdn.microsoft.com/library/aa366118) and [**ldap\_search\_init\_page**](https://msdn.microsoft.com/library/aa366973).



| Control OID                        | String constant                                                                                   |
|------------------------------------|---------------------------------------------------------------------------------------------------|
| 1.2.840.113556.1.4.319<br/>  | [LDAP\_PAGED\_RESULT\_OID\_STRING](https://msdn.microsoft.com/library/aa366953)<br/>                  |
| 1.2.840.113556.1.4.473<br/>  | [LDAP\_SERVER\_SORT\_OID](https://msdn.microsoft.com/library/aa366990)<br/>                                   |
| 1.2.840.113556.1.4.474<br/>  | [LDAP\_SERVER\_RESP\_SORT\_OID](https://msdn.microsoft.com/library/aa366986)<br/>                        |
| 1.2.840.113556.1.4.801<br/>  | [LDAP\_SERVER\_SD\_FLAGS\_OID](https://msdn.microsoft.com/library/aa366987)<br/>                          |
| 1.2.840.113556.1.4.528<br/>  | [LDAP\_SERVER\_NOTIFICATION\_OID](https://msdn.microsoft.com/library/aa366983)<br/>                   |
| 1.2.840.113556.1.4.417<br/>  | [LDAP\_SERVER\_SHOW\_DELETED\_OID](https://msdn.microsoft.com/library/aa366989)<br/>                  |
| 1.2.840.113556.1.4.619<br/>  | [LDAP\_SERVER\_LAZY\_COMMIT\_OID](https://msdn.microsoft.com/library/aa366982)<br/>                    |
| 1.2.840.113556.1.4.841<br/>  | [LDAP\_SERVER\_DIRSYNC\_OID](https://msdn.microsoft.com/library/aa366978)<br/>                             |
| 1.2.840.113556.1.4.529<br/>  | [LDAP\_SERVER\_EXTENDED\_DN\_OID](https://msdn.microsoft.com/library/aa366980)<br/>                    |
| 1.2.840.113556.1.4.805<br/>  | [LDAP\_SERVER\_TREE\_DELETE\_OID](https://msdn.microsoft.com/library/aa366991)<br/>                    |
| 1.2.840.113556.1.4.521<br/>  | [LDAP\_SERVER\_CROSSDOM\_MOVE\_TARGET\_OID](https://msdn.microsoft.com/library/aa366977)<br/> |
| 1.2.840.113556.1.4.1338<br/> | [LDAP\_SERVER\_VERIFY\_NAME\_OID](https://msdn.microsoft.com/library/aa366992)<br/>                    |
| 1.2.840.113556.1.4.1339<br/> | [LDAP\_SERVER\_DOMAIN\_SCOPE\_OID](https://msdn.microsoft.com/library/aa366979)<br/>                  |
| 1.2.840.113556.1.4.1340<br/> | [LDAP\_SERVER\_SEARCH\_OPTIONS\_OID](https://msdn.microsoft.com/library/aa366988)<br/>              |
| 1.2.840.113556.1.4.1413<br/> | [LDAP\_SERVER\_PERMISSIVE\_MODIFY\_OID](https://msdn.microsoft.com/library/aa366984)<br/>        |



 

 

 





