---
title: Bitmaps Section
description: Bitmaps Section
ms.assetid: db2801e5-c55a-4681-9fe9-6027f28653e0
keywords:
- Windows Media Player Mobile skins,bitmaps
- skins,bitmaps
- creating skins,Bitmaps section
- writing code for skins,Bitmaps section
- bitmaps in skins,Bitmaps section
- skin definition files,Bitmaps section
ms.topic: article
ms.date: 05/31/2018
---

# Bitmaps Section

Next, you must have a section that defines each of your bitmap files. Each type of bitmap you will use must have a file assigned to it, though you can have more than one type using the same bitmap.


```C++
[ Bitmaps ]

//  <Name>      <File name>     <X,Y>
//  ------      -----------     -----
    Background  Background.bmp  0,0
    Disabled    Disabled.bmp    0,0
    Pushed      Pushed.bmp      0,0
    Region      Region.bmp      0,0
    Super       Super.bmp       0,0

```



The Bitmaps section must begin with the word Bitmaps in brackets and then a line for each bitmap type you want to define. In this example, five types of bitmaps were defined. For more about the Bitmaps section, see [Bitmaps](bitmaps.md) in the Skin Reference.

> [!Note]  
> The Region and Super bitmaps are deprecated in Windows Media Player 10 Mobile or later skins.

 

## Related topics

<dl> <dt>

[**Writing the Code**](writing-the-code.md)
</dt> </dl>

 

 




