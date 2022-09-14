---
title: /notlb switch
description: The /notlb switch prevents the MIDL compiler from generating a type library (TLB) file.
ms.assetid: 58f4210d-d3c3-42ce-b311-4ddd85bc396a
keywords:
- /notlb switch MIDL
topic_type:
- apiref
api_name:
- /notlb
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /notlb switch

The **/notlb** switch prevents the MIDL compiler from generating a type library (TLB) file.

``` syntax
midl /notlb
```

## Switch Options

This switch has no parameters.

## Remarks

By default, the MIDL compiler will generate a TLB file whenever it encounters a [**LIBRARY**](library.md) statement. This switch overrides the default behavior.

When the **/notlb** option is specified, all other stubs, headers, etc. are generated as usual.

## See also

<dl> <dt>

[**/tlb**](-tlb.md)
</dt> </dl>

 

 




