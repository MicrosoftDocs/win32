---
title: optimize attribute
description: The \ optimize\ ACF attribute is used to fine tune the level of gradation for marshaling data.
ms.assetid: d636d940-0550-417f-a21a-065bdeaeb5d9
keywords:
- optimize attribute MIDL
topic_type:
- apiref
api_name:
- optimize
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# optimize attribute

The **\[optimize\]** ACF attribute is used to fine tune the level of gradation for marshaling data.

> [!Note]  
> This keyword is superceeded and should not be used. Current MIDL compilations should use [**/Oicf**](-oi.md)[**/robust**](-robust.md) instead.

 

``` syntax
optimize ("optimization-options")
```

## Parameters

<dl> <dt>

*optimization-options* 
</dt> <dd>

Specifies the method of marshaling data. Use either "s" for mixed-mode marshaling or "i" for interpreted marshaling.

</dd> </dl>

## Remarks

This version of RPC provides two methods for marshaling data: mixed-mode ("s") and interpreted ("i"). These methods correspond to the [**/Os**](-os.md) and [**/Oi**](-oi.md) command-line switches. The interpreted method marshals data completely offline. While this can reduce the size of the stub considerably, performance can be affected.

If performance is a concern, the mixed-mode method can be the best approach. Mixed-mode allows the MIDL compiler to make the determination between which data will be marshaled inline and which will be marshaled by a call to an offline dynamic-link library. If many procedures use the same data types, a single procedure can be called repeatedly to marshal the data. In this way, data that is most suited to inline marshaling is processed inline while other data can be more efficiently marshaled offline.

Note that the **\[optimize\]** attribute can be used as an interface attribute or as an operation attribute. If it is used as an interface attribute, it sets the default for the entire interface, overriding command-line switches. If, however, it is used as an operation attribute, it affects only that operation, overriding command-line switches and the interface default.

## Examples

``` syntax
optimize ("s") HRESULT FasterProcedure(...); 
optimize ("i") HRESULT SmallerProcedure(...);
```

## See also

<dl> <dt>

[Application Configuration File (ACF)](application-configuration-file-acf-.md)
</dt> <dt>

[**/Oi**](-oi.md)
</dt> <dt>

[**/Os**](-os.md)
</dt> <dt>

[**/robust**](-robust.md)
</dt> </dl>

 

 




