---
title: MicrosoftDNS_Cache class
description: The MicrosoftDNS\_Cache class describes a cache existing on a DNS Server.
ms.assetid: 139406eb-70f2-4614-9662-703ada032298
keywords:
- MicrosoftDNS_Cache class DNS
- MicrosoftDNS_Cache class DNS , described
topic_type:
- apiref
api_name:
- MicrosoftDNS_Cache
- MicrosoftDNS_Cache.ClearCache
- MicrosoftDNS_Cache.GetDistinguishedName
api_location:
- Root\MicrosoftDNS
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# MicrosoftDNS\_Cache class

The **MicrosoftDNS\_Cache** class describes a cache existing on a DNS Server. This class simplifies visualizing the containment of DNS objects, rather than representing a real object. The **MicrosoftDNS\_Cache** class is a container for the resource records cached by the DNS Server. Do not confuse this with a Cache file that contains root hints.

Every instance of the class **MicrosoftDNS\_Cache** must be assigned to exactly one DNS Server. It may be associated with multiple instances of [**MicrosoftDNS\_Domain**](microsoftdns-domain.md) or [**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md) classes.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
class MicrosoftDNS_Cache : MicrosoftDNS_Domain
{
};
```

## Members

The **MicrosoftDNS\_Cache** class has these types of members:

-   [Methods](#methods)

### Methods

The **MicrosoftDNS\_Cache** class has these methods.



| Method                   | Description                                                                                     |
|:-------------------------|:------------------------------------------------------------------------------------------------|
| **ClearCache**           | Clears the DNS Server cache of resource records. <br/> Qualifiers: Implemented<br/> |
| **GetDistinguishedName** | Retrieves the distinguished name for the zone. <br/> Qualifiers: Implemented<br/>   |



 

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

[**ClearCache Method of the MicrosoftDNS\_Cache Class**](microsoftdns-cache-clearcache.md)
</dt> <dt>

[**GetDistinguishedName Method of the MicrosoftDNS\_Cache Class**](microsoftdns-cache-getdistinguishedname.md)
</dt> </dl>

 

 





