---
title: MicrosoftDNS_DomainResourceRecordContainment class
description: The MicrosoftDNS\_DomainResourceRecordContainment class is used for RR containment; every instance of the MicrosoftDNS\_Domain may contain multiple instances of the MicrosoftDNS\_ResourceRecord class.
ms.assetid: 556c5e8d-58a1-4cb4-b4e9-eebdd86ed6a0
keywords:
- MicrosoftDNS_DomainResourceRecordContainment class DNS
- MicrosoftDNS_DomainResourceRecordContainment class DNS , described
topic_type:
- apiref
api_name:
- MicrosoftDNS_DomainResourceRecordContainment
- MicrosoftDNS_DomainResourceRecordContainment.GroupComponent
- MicrosoftDNS_DomainResourceRecordContainment.PartComponent
api_location:
- Root\MicrosoftDNS
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# MicrosoftDNS\_DomainResourceRecordContainment class

The **MicrosoftDNS\_DomainResourceRecordContainment** class is used for RR containment; every instance of the [**MicrosoftDNS\_Domain**](microsoftdns-domain.md) may contain multiple instances of the [**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md) class. Every instance of the **MicrosoftDNS\_ResourceRecord** class belongs to a single instance of the **MicrosoftDNS\_Domain** class, and is defined to be weak to that instance.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
class MicrosoftDNS_DomainResourceRecordContainment : CIM_Component
{
  MicrosoftDNS_Domain         REF GroupComponent;
  MicrosoftDNS_ResourceRecord REF PartComponent;
};
```

## Members

The **MicrosoftDNS\_DomainResourceRecordContainment** class has these types of members:

-   [Properties](#properties)

### Properties

The **MicrosoftDNS\_DomainResourceRecordContainment** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **MicrosoftDNS\_Domain**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Qualifiers: Key, Override("GroupComponent")

Description: The Zone, Cache, RootHints or Domain directly containing the Resource Record.

Inherited from CIM\_Component

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **MicrosoftDNS\_ResourceRecord**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Qualifiers: Key, Override("PartComponent")

Description: The resource record contained in a Domain, Zone, Cache, or RootHints.

Inherited from CIM\_Component.

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

[**MicrosoftDNS\_ServerDomainContainment**](microsoftdns-serverdomaincontainment.md)
</dt> <dt>

[**MicrosoftDNS\_DomainDomainContainment**](microsoftdns-domaindomaincontainment.md)
</dt> <dt>

[**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md)
</dt> </dl>

 

 





