---
title: Object(DN-Binary) syntax
description: An octet string that contains a binary value and a distinguished name (DN).
ms.assetid: 1d7efc17-a99a-41bf-9812-9e8a2b2b6644
ms.tgt_platform: multiple
keywords:
- Object(DN-Binary) syntax AD Schema
topic_type:
- apiref
api_name:
- Object(DN-Binary)
api_type:
- Schema
ms.topic: article
ms.date: 05/31/2018
---

# Object(DN-Binary) syntax

An octet string that contains a binary value and a distinguished name (DN).



|              |                                                                                    |
|--------------|------------------------------------------------------------------------------------|
| Name         | Object(DN-Binary)                                                                  |
| Syntax ID    | 2.5.5.7                                                                            |
| OM ID        | 127                                                                                |
| MAPI Type    | TSTRING                                                                            |
| ADS Type     | ADSTYPE\_DN\_WITH\_BINARY                                                          |
| Variant Type | VT\_DISPATCH                                                                       |
| SDS Type     | A COM object that can be cast to an [**IADsDNWithBinary**](https://docs.microsoft.com/windows/desktop/api/iads/nn-iads-iadsdnwithbinary). |



## Remarks

A value with this syntax has the following format:

``` syntax
B:<char count>:<binary value>:<object DN>
```

where "<char count>" is the number of hexadecimal digits in "<binary value>", "<binary value>" is the hexadecimal representation of the binary value, and "<object DN>" is a distinguished name. Active Directory automatically updates the DN if the object that it refers to is moved or renamed. For more information and a code example that uses this syntax, see [Enabling Rename-safe Binding with the otherWellKnownObjects Property](https://docs.microsoft.com/windows/desktop/AD/enabling-rename-safe-binding-with-the-otherwellknownobjects-property).

## See also

<dl> <dt>

[**IADsDNWithBinary**](https://docs.microsoft.com/windows/desktop/api/iads/nn-iads-iadsdnwithbinary)
</dt> </dl>

 

 




