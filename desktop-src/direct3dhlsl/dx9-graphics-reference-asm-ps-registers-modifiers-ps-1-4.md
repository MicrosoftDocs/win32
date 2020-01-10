---
title: ps\_1\_4 source register modifiers for texld, texcrd
description: Two pixel shader version 1\_4 texture address instructions, texld - ps\_1\_4 and texcrd - ps, have custom syntax.
ms.assetid: bbc8074f-882e-4b67-ae4d-1641ceb7f3ad
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# ps\_1\_4 source register modifiers for texld, texcrd

Two pixel shader version 1\_4 texture address instructions, [texld - ps\_1\_4](texld---ps-1-4.md) and [texcrd - ps](texcrd---ps.md), have custom syntax. These instructions support their own set of source register modifiers, source register selectors, and destination-register write masks, as shown here.

## Source Register Modifiers for texld and texcrd

These modifiers provide projective divide functionality by dividing the x and y values by either the z or w values.



| Source register modifiers | Description                | Syntax       |
|---------------------------|----------------------------|--------------|
| \_dz                      | Divide x,y components by z | register\_dz |
| \_db                      | Divide x,y components by z | register\_db |
| \_dw                      | Divide x,y components by w | register\_dw |
| \_da                      | Divide x,y components by w | register\_da |



 

### Remarks

The \_dz or \_db modifier does the following:


```
x' = x/z ( x' = 1.0 if z == 0)
y' = y/z ( y' = 1.0 if z == 0)
z' is undefined
w' is undefined
```



The \_dw or \_da modifier does the following:


```
x' = x/w ( x' = 1.0 if w == 0)
y' = y/w ( y' = 1.0 if w == 0)
z' is undefined
w' is undefined
```



## Related topics

<dl> <dt>

[Pixel Shader Source Register Modifiers](dx9-graphics-reference-asm-ps-registers-modifiers-source.md)
</dt> </dl>

 

 




