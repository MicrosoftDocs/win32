---
title: Status (Windows Media Player SDK)
description: Status
ms.assetid: 'b8d6d026-819c-4889-a894-c82fe81ec922'
keywords:
- Windows Media Player Mobile skins,status display
- skins,status display
- reference for skins,status display
- status display in skins,about
ms.topic: article
ms.date: 05/31/2018
---

# Status (Windows Media Player SDK)

You may want to use a status display in your skin. If so, the status element must be defined in the skin definition file. As an alternative, you may also display this information by using the Status attribute in the Text element.

The Status section of the skin definition file begins with this line:


```C++
[ Status ]

```



You then must add one or more lines that contain information about the status display in your skin.


```C++
    On           45,193,120,13    Left    Tahoma,8,B        0,255,  0

```



You can use the following template for the Status section of your skin definition file:


```C++
//  <Item>       <Location>     <Align>  <Font>          <Color>
//  ------       ----------     -------  ------          -------

```



You must use the order shown in the preceding template for status display information for each line in the Status section. Each part of the line is required. The following sections describe each item:

-   [Status Item](status-item.md)
-   [Status Location](status-location.md)
-   [Status Alignment](status-alignment.md)
-   [Status Font](status-font.md)
-   [Status Color](status-color.md)

For an example of Status code, see [Sample Status Section](sample-status-section.md).

## Related topics

<dl> <dt>

[**Skin Reference**](skin-reference.md)
</dt> </dl>

 

 




