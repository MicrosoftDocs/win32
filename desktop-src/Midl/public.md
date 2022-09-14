---
title: public attribute
description: The \ public\ attribute includes an alias declared with the typedef keyword in the type library.
ms.assetid: d4e90165-8b0d-47bb-998d-e515226be935
keywords:
- public attribute MIDL
topic_type:
- apiref
api_name:
- public
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
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

[ODL File Example](/previous-versions/windows/desktop/automat/odl-file-example)
</dt> <dt>

[**interface**](interface.md)
</dt> <dt>

[ODL File Syntax](/previous-versions/windows/desktop/automat/odl-file-syntax)
</dt> <dt>

[**typedef**](typedef.md)
</dt> </dl>

 

 