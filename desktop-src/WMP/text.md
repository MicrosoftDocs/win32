---
title: Text (Windows Media Player SDK)
description: Text
ms.assetid: '8c10cefb-d0d0-4214-8712-d171a76de95d'
keywords:
- Windows Media Player Mobile skins,text
- skins,text
- reference for skins,text
- text in skins,about
ms.topic: article
ms.date: 05/31/2018
---

# Text (Windows Media Player SDK)

You may want to use one or more text display boxes in your skin. Each text display box you use must be defined in the skin definition file. If you do not define a text display box in this section, your skin will not be able to use it.

The Text section of the skin definition file begins with this line:


```C++
[ Text ]

```



You then must add one or more lines that contain information about each of the text display boxes in your skin


```C++
    Time         180,46,50,30   Right    Tahoma,16,N     255,255,255

```



You can use the following template for the Text section of your skin definition file:


```C++
//  <Type>       <Location>     <Align> <Font>          <Color>
//  ------       ----------     ------- ------          -------

```



You must use the order shown in the preceding template for text display box information for each line in the Text section. Each part of the line is required. The following sections describe each item in detail.

1.  [Text Type](text-type.md)
2.  [Text Location](text-location.md)
3.  [Text Alignment](text-alignment.md)
4.  [Text Font](text-font.md)
5.  [Text Color](text-color.md)

For an example of Text code, see [Sample Text Section](sample-text-section.md).

## Related topics

<dl> <dt>

[**Skin Reference**](skin-reference.md)
</dt> </dl>

 

 




