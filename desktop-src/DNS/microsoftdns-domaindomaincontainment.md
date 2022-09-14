---
title: MicrosoftDNS_DomainDomainContainment class
description: The MicrosoftDNS\_DomainDomainContainment class is used for domain containment; DNS domains may contain other DNS domains.
ms.assetid: 43faa046-30bf-4fb3-9698-98d09c424fad
keywords:
- MicrosoftDNS_DomainDomainContainment class DNS
- MicrosoftDNS_DomainDomainContainment class DNS , described
topic_type:
- apiref
api_name:
- MicrosoftDNS_DomainDomainContainment
- MicrosoftDNS_DomainDomainContainment.GroupComponent
- MicrosoftDNS_DomainDomainContainment.PartComponent
api_location:
- Root\MicrosoftDNS
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# MicrosoftDNS\_DomainDomainContainment class

The **MicrosoftDNS\_DomainDomainContainment** class is used for domain containment; DNS domains may contain other DNS domains. Every instance of the [**MicrosoftDNS\_Domain**](microsoftdns-domain.md) class may contain multiple other instances of **MicrosoftDNS\_Domain**. An instance of a **MicrosoftDNS\_Domain** object is directly contained in no more than one higher level **MicrosoftDNS\_Domain**.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
class MicrosoftDNS_DomainDomainContainment : CIM_Component
{
  MicrosoftDNS_Domain REF GroupComponent;
  MicrosoftDNS_Domain REF PartComponent;
};
```

## Members

The **MicrosoftDNS\_DomainDomainContainment** class has these types of members:

-   [Properties](#properties)

### Properties

The **MicrosoftDNS\_DomainDomainContainment** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **MicrosoftDNS\_Domain**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Qualifiers: Key, Max(1), Override("GroupComponent")

Description: A higher level Domain, Zone, Cache, or RootHints.

Inherited from CIM\_Component

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **MicrosoftDNS\_Domain**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Qualifiers: Key, Override("PartComponent")

Description: The Domain contained by a higher level Domain, Zone, Cache or RootHints.

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

[**MicrosoftDNS\_DomainResourceRecordContainment**](microsoftdns-domainresourcerecordcontainment.md)
</dt> <dt>

[**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md)
</dt> <dt>

[**MicrosoftDNS\_ServerDomainContainment**](microsoftdns-serverdomaincontainment.md)
</dt> </dl>

 

 





