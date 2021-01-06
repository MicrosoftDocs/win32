---
description: Consists of an index parameter and an RGBA color and is used for defining mesh vertex colors. The index defines the vertex to which the color is applied.
ms.assetid: 63909c54-c2de-4065-9882-58fca2b4e893
title: IndexedColor
ms.topic: reference
ms.date: 05/31/2018
---

# IndexedColor

Consists of an index parameter and an RGBA color and is used for defining mesh vertex colors. The index defines the vertex to which the color is applied.

``` syntax
template IndexedColor
{
    < 1630B820-7842-11cf-8F52-0040333594A3 >
    DWORD index;
    ColorRGBA indexColor;
} 
```

Where:

-   index - A DWORD. See the description above.
-   indexColor - A ColorRGBA template. See [**ColorRGBA**](colorrgba.md).

## See also

<dl> <dt>

[Templates](dx9-graphics-reference-x-file-format-templates.md)
</dt> </dl>

 

 



