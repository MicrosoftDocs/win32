---
title: Description Section
description: Description Section
ms.assetid: 280a9a4d-935f-440d-a606-94aeba0007db
keywords:
- Windows Media Player Mobile skins,Description section
- skins,Description section
- creating skins,Description section
- writing code for skins,Description section
- Description section in skins
- skin definition files,Description section
ms.topic: article
ms.date: 05/31/2018
---

# Description Section

Next, you must provide a section that describes the size and orientation of the skin when creating a skin for Windows Media Player 9 Series for Windows Mobile 2003 and later versions:


```C++
[ Description ]
//              <X,Y>       <DPI>
//              ------      -----
    Dimensions  240, 320    96

//    <Orientation>
//    -------------
    Orientation Portrait

```



The Description section must begin with the word Description in brackets, and then include a line that specifies the dimensions and display resolution for the skin.

Lines beginning with two forward slashes are not processed, and can be used for comments or, as shown in the previous code, a template to help you remember what goes in a section. You can also use templates to help align everything into columns.

For more information about the Description section, see [Description](description.md) in the Skin Reference.

## Related topics

<dl> <dt>

[**Writing the Code**](writing-the-code.md)
</dt> </dl>

 

 




