---
title: MicrosoftDNS_RootHints class
description: The MicrosoftDNS\_RootHints class describes the RootHints stored in a Cache file on a DNS Server. This class simplifies visualizing the containment of DNS objects, rather than representing a real object.
ms.assetid: d6dbce97-cffd-476a-ba61-c070d8245f0a
keywords:
- MicrosoftDNS_RootHints class DNS
- MicrosoftDNS_RootHints class DNS , described
topic_type:
- apiref
api_name:
- MicrosoftDNS_RootHints
- MicrosoftDNS_RootHints.WriteBackRootHintDatafile
- MicrosoftDNS_RootHints.GetDistinguishedName
api_location:
- Root\MicrosoftDNS
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# MicrosoftDNS\_RootHints class

The **MicrosoftDNS\_RootHints** class describes the RootHints stored in a Cache file on a DNS Server. This class simplifies visualizing the containment of DNS objects, rather than representing a real object.

**MicrosoftDNS\_RootHints** is a container for the resource records stored by the DNS Server in a Cache file. Every instance of the **MicrosoftDNS\_RootHints** class must be assigned to exactly one DNS Server. It may be associated with multiple instances of the [**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md) class.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
class MicrosoftDNS_RootHints : MicrosoftDNS_Domain
{
};
```

## Members

The **MicrosoftDNS\_RootHints** class has these types of members:

-   [Methods](#methods)

### Methods

The **MicrosoftDNS\_RootHints** class has these methods.



| Method                        | Description                                                                                     |
|:------------------------------|:------------------------------------------------------------------------------------------------|
| **GetDistinguishedName**      | Retrieves the distinguished name for the zone. <br/> Qualifiers: Implemented<br/>   |
| **WriteBackRootHintDatafile** | Writes the RootHints back to the DNS Cache file. <br/> Qualifiers: Implemented<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\MicrosoftDNS<br/>                                                          |
| MOF<br/>                      | <dl> <dt>Dnsprov.mof</dt> </dl> |



## See also

<dl> <dt>

[**MicrosoftDNS\_Domain**](microsoftdns-domain.md)
</dt> <dt>

[**WriteBackRootHintDatafile Method of the MicrosoftDNS\_RootHints Class**](microsoftdns-roothints-writebackroothintdatafile.md)
</dt> <dt>

[**GetDistinguishedName Method of the MicrosoftDNS\_RootHints Class**](microsoftdns-roothints-getdistinguishedname.md)
</dt> </dl>

 

 





