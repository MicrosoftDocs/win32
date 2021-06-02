---
title: Object(DS-DN) syntax
description: String that contains a distinguished name (DN).
ms.assetid: 089104c4-ff82-49ea-a8db-a6dadc3a18bc
ms.tgt_platform: multiple
keywords:
- Object(DS-DN) syntax AD Schema
topic_type:
- apiref
api_name:
- Object(DS-DN)
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# Object(DS-DN) syntax

String that contains a distinguished name (DN). For attributes with this syntax, Active Directory handles attribute values as references to the object identified by the DN and automatically updates the value if the object is moved or renamed. For queries that include attributes of DN syntax in a filter, specify full distinguished names. Wildcards (for example, cn=John\*) are not supported.



| Entry | Value |
|--------------|------------------------------------------------------------------------|
| Name         | Object(DS-DN)                                                          |
| Syntax ID    | 2.5.5.1                                                                |
| OM ID        | 127                                                                    |
| MAPI Type    | OBJECT                                                                 |
| ADS Type     | ADSTYPE\_DN\_STRING                                                    |
| Variant Type | VT\_BSTR                                                               |
| SDS Type     | [System.String](/dotnet/api/system.string) |



## See also

<dl> <dt>

[System.String](/dotnet/api/system.string)
</dt> </dl>

 

 
