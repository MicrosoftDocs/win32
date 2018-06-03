---
title: RootDSE class
description: The RootDSE class provides information about the capabilities of an LDAP server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 8e934dc5-69a2-4097-8df0-14ad162a3996
ms.prod: windows-server-dev
ms.technology:
- active-directory-domain-services
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RootDSE class
- RootDSE class, described
topic_type:
- apiref
api_name:
- RootDSE
- RootDSE.subschemaSubentry
- RootDSE.currentTime
- RootDSE.serverName
- RootDSE.namingContexts
- RootDSE.defaultNamingContext
- RootDSE.schemaNamingContext
- RootDSE.configurationNamingContext
- RootDSE.rootDomainNamingContext
- RootDSE.supportedControl
- RootDSE.supportedLDAPVersion
- RootDSE.dnsHostName
- RootDSE.dsServiceName
- RootDSE.highestCommittedUSN
- RootDSE.LDAPServiceName
- RootDSE.supportedCapabilities
- RootDSE.supportedLDAPPolicies
- RootDSE.supportedSASLMechanisms
api_location:
- Dsprov.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RootDSE class

The **RootDSE** class provides information about the capabilities of an LDAP server.

## Syntax

``` syntax
[singleton, dynamic, provider("Microsoft|DSLDAPInstanceProvider|V1.0"), AMENDMENT]
class RootDSE
{
  string subschemaSubentry;
  string currentTime;
  string serverName;
  string namingContexts[];
  string defaultNamingContext;
  string schemaNamingContext;
  string configurationNamingContext;
  string rootDomainNamingContext;
  string supportedControl[];
  string supportedLDAPVersion[];
  string dnsHostName;
  string dsServiceName;
  string highestCommittedUSN;
  string LDAPServiceName;
  string supportedCapabilities;
  string supportedLDAPPolicies[];
  string supportedSASLMechanisms[];
};
```

## Members

The **RootDSE** class has these types of members:

-   [Properties](#properties)

### Properties

The **RootDSE** class has these properties.

<dl> <dt>

**configurationNamingContext**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Distinguished name for the configuration container.

</dd> <dt>

**currentTime**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current time set on this directory server.

</dd> <dt>

**defaultNamingContext**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

By default, the distinguished name for the domain of which this directory server is a member.

</dd> <dt>

**dnsHostName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

DNS address for this directory server.

</dd> <dt>

**dsServiceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Distinguished name of the NTDS settings object for this directory server.

</dd> <dt>

**highestCommittedUSN**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Highest USN used on this directory server. This property is used by directory replication.

</dd> <dt>

**LDAPServiceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Service principal name (SPN) for the LDAP server. This property is used for mutual authentication.

</dd> <dt>

**namingContexts**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Multivalued. This property represents distinguished names for all naming contexts stored on this directory server. By default, a Windows domain controller contains at least three namespaces: Schema, Configuration, and one for the domain of which the server is a member.

</dd> <dt>

**rootDomainNamingContext**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Distinguished name for the first domain in the forest that contains the domain of which this directory server is a member.

</dd> <dt>

**schemaNamingContext**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Distinguished name for the schema container.

</dd> <dt>

**serverName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Distinguished name for the server object for this directory server in the configuration container.

</dd> <dt>

**subschemaSubentry**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Distinguished name for the [**subSchema**](https://msdn.microsoft.com/library/ms683974) object. The **subSchema** object contains properties that expose the supported attributes (in the [**attributeTypes**](https://msdn.microsoft.com/library/ms675237) property) and classes (in the [**objectClasses**](https://msdn.microsoft.com/library/ms679016) property).

The **subschemaSubentry** property and subschema are defined in LDAP 3.0. For more information, see [RFC 2251](Http://go.microsoft.com/fwlink/p/?linkid=84412).

</dd> <dt>

**supportedCapabilities**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Object identifiers (OID) that identifies the supported capabilities of the server.

</dd> <dt>

**supportedControl**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Multivalued. This property represents OIDs for extension controls supported by this directory server. The controls supported by Active Directory are listed in the following table.

</dd> <dt>

**supportedLDAPPolicies**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supported LDAP management policies.

</dd> <dt>

**supportedLDAPVersion**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Multivalued. This property represents LDAP versions (specified by major version number) supported by this directory server.

</dd> <dt>

**supportedSASLMechanisms**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Security mechanisms supported for SASL negotiation (see LDAP RFCs). By default, GSSAPI is supported.

</dd> </dl>

## Remarks

There is only one instance of **RootDSE** (it is a singleton class).

The series of 1.2.840.113556.1.4.1461 - 1620 OIDs are described at: [LDAP\_SERVER\_SORT\_OID](https://msdn.microsoft.com/library/aa366990) as an extension to the LDAP server sort control that specifies the locale to use for the sort.

A number of the 1.2.840.113556.1.4 OIDs are referred to at [LDAP controls and session support](https://msdn.microsoft.com/library/aa813628).

The [Active Directory Schema site](https://msdn.microsoft.com/library/ms675087) lists the names of some of the subtrees of OIDs.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Namespace<br/>                | Root\\directory\\ldap<br/>                                                      |
| MOF<br/>                      | <dl> <dt>Dsprov.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Dsprov.dll</dt> </dl> |



 

 





