---
title: pointer_default attribute
description: The \ pointer\_default\ attribute specifies the default pointer attribute for all pointers except top-level pointers that appear in parameter lists.
ms.assetid: a6e83034-8adb-483d-8d1e-432a1aed22c6
keywords:
- pointer_default attribute MIDL
topic_type:
- apiref
api_name:
- pointer_default
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# pointer\_default attribute

The **\[pointer\_default\]** attribute specifies the default pointer attribute for all pointers except top-level pointers that appear in parameter lists.

``` syntax
pointer_default ( ptr | ref | unique )
```

## Parameters

This attribute has no parameters.

## Examples

``` syntax
[
    uuid(6B29FC40-CA47-1067-B31D-00DD010662DA), 
    version(3.3), 
    pointer_default(unique)
] 
interface dictionary 
{
    // Interface definition statements.
}
```

## See also

<dl> <dt>

[**interface**](interface.md)
</dt> <dt>

[Array and Sized-Pointer Attributes](array-and-sized-pointer-attributes.md)
</dt> <dt>

[**arrays**](arrays-1.md)
</dt> <dt>

[Arrays and Pointers](/windows/desktop/Rpc/arrays-and-pointers)
</dt> <dt>

[**ptr**](ptr.md)
</dt> <dt>

[**ref**](ref.md)
</dt> <dt>

[**unique**](unique.md)
</dt> <dt>

[Default Pointer Types](/windows/desktop/Rpc/default-pointer-types)
</dt> </dl>

 

 