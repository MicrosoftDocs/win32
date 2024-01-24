---
title: MicrosoftDNS_ServerDomainContainment class
description: Every instance of the MicrosoftDNS\_Server association WMI class may contain multiple instances of the MicrosoftDNS\_Domain class.
ms.assetid: a16a11fb-65fc-4f12-903c-b3a61f6a4720
keywords:
- MicrosoftDNS_ServerDomainContainment class DNS
- MicrosoftDNS_ServerDomainContainment class DNS , described
topic_type:
- apiref
api_name:
- MicrosoftDNS_ServerDomainContainment
- MicrosoftDNS_ServerDomainContainment.GroupComponent
- MicrosoftDNS_ServerDomainContainment.PartComponent
api_location:
- Root\MicrosoftDNS
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# MicrosoftDNS\_ServerDomainContainment class

Every instance of the [**MicrosoftDNS\_Server**](microsoftdns-server.md) association WMI class may contain multiple instances of the [**MicrosoftDNS\_Domain**](microsoftdns-domain.md) class. Every instance of the **MicrosoftDNS\_Domain** class belongs to a single instance of the **MicrosoftDNS\_Server** class, and is defined to be weak to that server.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MicrosoftDNS_ServerDomainContainment : CIM_Component
{
  MicrosoftDNS_Server REF GroupComponent;
  MicrosoftDNS_Domain REF PartComponent;
};
```

## Members

The **MicrosoftDNS\_ServerDomainContainment** class has these types of members:

-   [Properties](#properties)

### Properties

The **MicrosoftDNS\_ServerDomainContainment** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **MicrosoftDNS\_Server**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Qualifiers: Key, Override ("GroupComponent"), Min (1), Max (1)

Description: The DNS Server.

Inherited from **CIM\_Component**.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **MicrosoftDNS\_Domain**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Qualifiers: Key, Override("PartComponent")

Description: A Domain, Zone, Cache, or RootHints managed by the DNS Server.

Inherited from **CIM\_Component**.

</dd> </dl>

## Remarks

The **MicrosoftDNS\_ServerDomainContainment** class is derived from the **CIM\_Component** class.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\MicrosoftDNS<br/>                                                          |
| MOF<br/>                      | <dl> <dt>Dnsprov.mof</dt> </dl> |



## See also

<dl> <dt>

[**MicrosoftDNS\_DomainDomainContainment**](microsoftdns-domaindomaincontainment.md)
</dt> <dt>

[**MicrosoftDNS\_DomainResourceRecordContainment**](microsoftdns-domainresourcerecordcontainment.md)
</dt> <dt>

[**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md)
</dt> </dl>

 

 





