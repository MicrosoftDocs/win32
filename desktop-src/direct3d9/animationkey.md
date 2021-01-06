---
description: Defines a set of animation keys. A matrix key is useful for sets of animation data that need to be represented as transformation matrices.
ms.assetid: bf007541-7fea-423e-910b-fa5f45271608
title: AnimationKey
ms.topic: reference
ms.date: 05/31/2018
---

# AnimationKey

Defines a set of animation keys. A matrix key is useful for sets of animation data that need to be represented as transformation matrices.

``` syntax
template AnimationKey
{
    < 10DD46A8-775B-11CF-8F52-0040333594A3 >
    DWORD keyType;
    DWORD nKeys;
    array TimedFloatKeys keys[nKeys];
} 
```

Where:

-   keyType - Specifies whether the keys are rotation, scale, position, or matrix keys (using the integers 0, 1, 2, or 3, respectively).
-   nKeys - Number of keys.
-   keys - An array of keys. See [**TimedFloatKeys**](timedfloatkeys.md).

## See also

<dl> <dt>

[Templates](dx9-graphics-reference-x-file-format-templates.md)
</dt> </dl>

 

 



