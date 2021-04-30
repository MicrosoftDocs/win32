---
title: Object(DN-String) syntax
description: An octet string that contains a string value and a DN.
ms.assetid: 7a5ce9f3-ac97-4936-868a-6b18f202972f
ms.tgt_platform: multiple
keywords:
- Object(DN-String) syntax AD Schema
topic_type:
- apiref
api_name:
- Object(DN-String)
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# Object(DN-String) syntax

An octet string that contains a string value and a DN.



| Entry | Value |
|--------------|------------------------------------------------------------------------------------|
| Name         | Object(DN-String)                                                                  |
| Syntax ID    | 2.5.5.14                                                                           |
| OM ID        | 127                                                                                |
| MAPI Type    | \-                                                                                 |
| ADS Type     | ADSTYPE\_DN\_WITH\_STRING                                                          |
| Variant Type | VT\_DISPATCH                                                                       |
| SDS Type     | A COM object that can be cast to an [**IADsDNWithString**](/windows/desktop/api/iads/nn-iads-iadsdnwithstring). |



## Remarks

A value with this syntax has the following format:

``` syntax
S:<char count>:<string value>:<object DN>
```

where "&lt;char count&gt;" is the number of characters in the "&lt;string value&gt;" string, and "&lt;object DN&gt;" is a distinguished name of an object in Active Directory. Active Directory updates the DN if the object that it refers to is moved or renamed.

## See also

<dl> <dt>

[**IADsDNWithString**](/windows/desktop/api/iads/nn-iads-iadsdnwithstring)
</dt> </dl>

 

 
