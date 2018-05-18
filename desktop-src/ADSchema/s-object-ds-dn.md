---
title: Object(DS-DN) syntax
description: String that contains a distinguished name (DN).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '089104c4-ff82-49ea-a8db-a6dadc3a18bc'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-schema'
ms.tgt_platform: multiple
keywords: ["Object(DS-DN) syntax AD Schema"]
topic_type:
- apiref
api_name:
- Object(DS-DN)
api_type:
- Schema
---

# Object(DS-DN) syntax

String that contains a distinguished name (DN). For attributes with this syntax, Active Directory handles attribute values as references to the object identified by the DN and automatically updates the value if the object is moved or renamed. For queries that include attributes of DN syntax in a filter, specify full distinguished names. Wildcards (for example, cn=John\*) are not supported.



|              |                                                                        |
|--------------|------------------------------------------------------------------------|
| Name         | Object(DS-DN)                                                          |
| Syntax ID    | 2.5.5.1                                                                |
| OM ID        | 127                                                                    |
| MAPI Type    | OBJECT                                                                 |
| ADS Type     | ADSTYPE\_DN\_STRING                                                    |
| Variant Type | VT\_BSTR                                                               |
| SDS Type     | [System.String](https://msdn.microsoft.com/library/system.string.aspx) |



## See also

<dl> <dt>

[System.String](https://msdn.microsoft.com/library/system.string.aspx)
</dt> </dl>

 

 




