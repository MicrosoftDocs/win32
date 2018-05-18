---
title: public attribute
description: The \ public\ attribute includes an alias declared with the typedef keyword in the type library.
ms.assetid: d4e90165-8b0d-47bb-998d-e515226be935
keywords: ["public attribute MIDL"]
topic_type:
- apiref
api_name:
- public
api_type:
- NA
---

# public attribute

The **\[public\]** attribute includes an alias declared with the [**typedef**](typedef.md) keyword in the type library.

``` syntax
typedef [public] data-type identifier;
```

## Parameters

<dl> <dt>

*data-type* 
</dt> <dd>

The data type that the identifier will be an alias for.

</dd> <dt>

*identifier* 
</dt> <dd>

Another name by which *data-type* will be known in the software.

</dd> </dl>

## Remarks

By default, an alias that is declared with [**typedef**](typedef.md) and has no other attributes is treated as a **\#define** and is not included in the type library. Using the **\[public\]** attribute ensures that the alias becomes part of the type library.

> [!Note]  
> The MIDL compiler requires that you explicitly apply the **\[public\]** attribute to each typedef that you want public.

 

## Examples

``` syntax
typedef [public] long MEMBERID;
```

## See also

<dl> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> <dt>

[ODL File Example](86d64a4f-08eb-422a-bb1d-dfa868094645)
</dt> <dt>

[**interface**](interface.md)
</dt> <dt>

[ODL File Syntax](df7aa86f-1453-4409-939e-788d469d611e)
</dt> <dt>

[**typedef**](typedef.md)
</dt> </dl>

 

 




