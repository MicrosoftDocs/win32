---
description: Enables you to set animation options.
ms.assetid: 727b4d87-4164-4915-b158-d21fe7d1b729
title: AnimationOptions
ms.topic: reference
ms.date: 05/31/2018
---

# AnimationOptions

Enables you to set animation options.

``` syntax
template AnimationOptions
{
    < E2BF56C0-840F-11cf-8F52-0040333594A3 >
    DWORD openclosed;
    DWORD positionquality;
} 
```

Where:

-   openclosed - Use 0 for a closed animation, or 1 for an open animation. By default, an animation is closed.
-   positionquality - Set the position quality for any position keys specified. Use 0 for spline positions or 1 for linear positions.

## See also

<dl> <dt>

[Templates](dx9-graphics-reference-x-file-format-templates.md)
</dt> </dl>

 

 



