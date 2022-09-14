---
title: Ambient Attributes
description: Ambient Attributes
ms.assetid: 9dc8c770-4de3-42d8-b388-4426a4b0e788
keywords:
- Windows Media Player skins,ambient attributes
- skins,ambient attributes
- reference for skins,ambient attributes
- ambient attributes
- attributes,ambient
ms.topic: article
ms.date: 05/31/2018
---

# Ambient Attributes

The ambient attributes and methods are supported by all appropriate skin elements, except where noted.

The following attributes are ambient.



| Attribute                                                        | Description                                                                                                                               |
|------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| [accName](ambientattributes-accname.md)                         | Specifies or retrieves a name for any element.                                                                                            |
| [accDescription](ambientattributes-accdescription.md)           | Specifies or retrieves a description for any element.                                                                                     |
| [accKeyboardShortcut](ambientattributes-acckeyboardshortcut.md) | Specifies or retrieves a keyboard shortcut description for any element.                                                                   |
| [alphaBlend](ambientattributes-alphablend.md)                   | Specifies or retrieves a value for alpha blending any **VIEW**, **SUBVIEW**, or UI widget.                                                |
| [bottom](ambientattributes-bottom.md)                           | Specifies or retrieves the bottom coordinate of the control.                                                                              |
| [clippingColor](ambientattributes-clippingcolor.md)             | Specifies or retrieves the color to clip out from the **clippingImage** bitmap.                                                           |
| [clippingImage](ambientattributes-clippingimage.md)             | Specifies or retrieves the region to clip the control to.                                                                                 |
| [elementType](ambientattributes-elementtype.md)                 | Retrieves the type of the element (for instance, **BUTTON**).                                                                             |
| [enabled](ambientattributes-enabled.md)                         | Specifies or retrieves a value indicating whether the control is enabled or disabled.                                                     |
| [height](ambientattributes-height.md)                           | Specifies or retrieves the height of the control.                                                                                         |
| [horizontalAlignment](ambientattributes-horizontalalignment.md) | Specifies or retrieves a value that indicates the horizontal placement of the control when the **VIEW** or parent **SUBVIEW** is resized. |
| [id](ambientattributes-id.md)                                   | Specifies or retrieves the identifier of a control. Can only be set at design time.                                                       |
| [left](ambientattributes-left.md)                               | Specifies or retrieves the left coordinate of the control.                                                                                |
| [nineGridMargins](ambientattributes-ninegridmargins.md)         | Specifies margin widths for non-uniform scaling of the skin element.                                                                      |
| [passThrough](ambientattributes-passthrough.md)                 | Specifies or retrieves a value indicating whether the control will pass all mouse events through to the control under it.                 |
| [resizeImages](ambientattributes-resizeimages.md)               | Specifies or retrieves a value indicating whether images contained in the control resize automatically when the control size changes.     |
| [right](ambientattributes-right.md)                             | Specifies or retrieves the right coordinate of the control.                                                                               |
| [tabStop](ambientattributes-tabstop.md)                         | Specifies or retrieves a value indicating whether the control will be in the tabbing order.                                               |
| [top](ambientattributes-top.md)                                 | Specifies or retrieves the top coordinate of the control.                                                                                 |
| [verticalAlignment](ambientattributes-verticalalignment.md)     | Specifies or retrieves a value that indicates the vertical placement of the control when the **VIEW** or parent **SUBVIEW** is resized.   |
| [visible](ambientattributes-visible.md)                         | Specifies or retrieves the visibility of the control.                                                                                     |
| [width](ambientattributes-width.md)                             | Specifies or retrieves the width of the control.                                                                                          |
| [zIndex](ambientattributes-zindex.md)                           | Specifies or retrieves the order in which the control is rendered.                                                                        |



 

The following methods are ambient.



| Method                                             | Description                                                                                                                                                          |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [alphaBlendTo](ambientattributes-alphablendto.md) | Adjusts the **alphaBlend** property over a period of time.                                                                                                           |
| [moveSizeTo](ambientattributes-movesizeto.md)     | Moves the control and specifies a new size for the control in the new location. The control moves and resizes in an animated fashion over the specified time period. |
| [moveTo](ambientattributes-moveto.md)             | Moves the control to a new location at a linear speed.                                                                                                               |
| [slideTo](ambientattributes-slideto.md)           | Moves the control to a new location. The control moves in a non-linear fashion over the specified time period.                                                       |



 

## Related topics

<dl> <dt>

[**Skin Programming Reference**](skin-programming-reference.md)
</dt> </dl>

 

 




