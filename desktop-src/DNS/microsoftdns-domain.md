---
title: MicrosoftDNS_Domain class
description: The MicrosoftDNS\_Domain class represents a Domain in a DNS hierarchy.
ms.assetid: 4b3124d6-aa5c-4950-b461-c6dd7bc96945
keywords:
- MicrosoftDNS_Domain class DNS
- MicrosoftDNS_Domain class DNS , described
topic_type:
- apiref
api_name:
- MicrosoftDNS_Domain
- MicrosoftDNS_Domain.GetDistinguishedName
- MicrosoftDNS_Domain.DnsServerName
- MicrosoftDNS_Domain.ContainerName
- MicrosoftDNS_Domain.Name
api_location:
- Root\MicrosoftDNS
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# MicrosoftDNS\_Domain class

The **MicrosoftDNS\_Domain** class represents a Domain in a DNS hierarchy.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
class MicrosoftDNS_Domain : CIM_LogicalElement
{
  string DnsServerName;
  string ContainerName;
  string Name;
};
```

## Members

The **MicrosoftDNS\_Domain** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MicrosoftDNS\_Domain** class has these methods.



| Method                   | Description                                                                                |
|:-------------------------|:-------------------------------------------------------------------------------------------|
| **GetDistinguishedName** | Obtains DS distinguished Name for the zone. <br/> Qualifiers: Implemented<br/> |



 

### Properties

The **MicrosoftDNS\_Domain** class has these properties.

<dl> <dt>

**ContainerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the container of the domain, which could be a Zone, Cache, or RootHints.

In cases where the Container is a Zone (an instance of the [**MicrosoftDNS\_Zone**](microsoftdns-zone.md) class), this property contains the FQDN of the Zone.

When the Container is the root zone, the string \\.\\ should be used.

In cases where the Container is the DNS cache of resource records (an instance of the [**MicrosoftDNS\_Cache**](microsoftdns-cache.md) class), this property is set to the string \\..Cache\\.

If the Container is RootHints (an instance of the [**MicrosoftDNS\_RootHints**](microsoftdns-roothints.md) class), this property should be set to \\..RootHints\\.

</dd> <dt>

**DnsServerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

FQDN or IP address of the DNS Server that contains the domain.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

FQDN of the domain.

For instances of DNS Cache or RootHints, the strings \\..Cache\\ and \\..RootHints\\ should be used, respectively.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\MicrosoftDNS<br/>                                                          |
| MOF<br/>                      | <dl> <dt>Dnsprov.mof</dt> </dl> |



## See also

<dl> <dt>

[**GetDistinguishedName Method of the MicrosoftDNS\_Domain Class**](microsoftdns-domain-getdistinguishedname.md)
</dt> </dl>

 

 





