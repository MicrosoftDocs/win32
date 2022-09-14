---
title: Interval syntax
description: Represents a time interval value.
ms.assetid: e41b71da-cd05-4a4a-8b97-9210dbe314de
ms.tgt_platform: multiple
keywords:
- Interval syntax AD Schema
topic_type:
- apiref
api_name:
- Interval
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# Interval syntax

Represents a time interval value. The actual time units depend on which attribute is using this syntax. This syntax is identical to the [**LargeInteger**](s-largeinteger.md) syntax, except the high and low values are unsigned integers.



| Entry | Value |
|--------------|------------------------------------------------------------------------------------|
| Name         | Interval                                                                           |
| Syntax ID    | 2.5.5.16                                                                           |
| OM ID        | 65                                                                                 |
| MAPI Type    | \-                                                                                 |
| ADS Type     | ADSTYPE\_LARGE\_INTEGER                                                            |
| Variant Type | VT\_DISPATCH                                                                       |
| SDS Type     | A COM object that can be cast to an [**IADsLargeInteger**](/windows/desktop/api/iads/nn-iads-iadslargeinteger). |



## See also

<dl> <dt>

[**IADsLargeInteger**](/windows/desktop/api/iads/nn-iads-iadslargeinteger)
</dt> <dt>

[**LargeInteger**](s-largeinteger.md)
</dt> </dl>

 

 
