---
title: SUBVIEW Element
description: SUBVIEW Element
ms.assetid: 6201df82-8688-4ada-a660-b66e93723f63
keywords:
- Windows Media Player skins,SUBVIEW element
- skins,SUBVIEW element
- SUBVIEW element
- reference for skins,SUBVIEW element
- elements,SUBVIEW
ms.topic: article
ms.date: 05/31/2018
---

# SUBVIEW Element

The **SUBVIEW** element provides a way to manipulate a portion of a skin, for example, to provide a control panel that can be hidden when it is not being used. **SUBVIEW** elements are always children of parent **VIEW** elements, and can contain other skin element except for **VIEW**, **THEME**, and other **SUBVIEW** elements.

The **SUBVIEW** element supports the following attributes, which are defined under the **VIEW** element.



| Attribute                                                       | Description                                                                                                 |
|-----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| [backgroundColor](view-backgroundcolor.md)                     | Specifies or retrieves the background color of the **SUBVIEW** control. The default value is "none".        |
| [backgroundImage](view-backgroundimage.md)                     | Specifies or retrieves the background image of the **SUBVIEW** control.                                     |
| [backgroundImageHueShift](view-backgroundimagehueshift.md)     | Specifies or retrieves the amount by which the hue of the background image is shifted.                      |
| [backgroundImageSaturation](view-backgroundimagesaturation.md) | Specifies or retrieves the saturation value of the background image.                                        |
| [backgroundTiled](view-backgroundtiled.md)                     | Specifies or retrieves a value indicating whether the background image of the **SUBVIEW** control is tiled. |
| [resizeBackgroundImage](view-resizebackgroundimage.md)         | Specifies or retrieves a value indicating whether the background image can be resized.                      |
| [transparencyColor](view-transparencycolor.md)                 | Specifies or retrieves the transparency color of the background image.                                      |



 

The **SUBVIEW** element supports the ambient attributes, except where noted. For more information, see [Ambient Attributes](ambient-attributes.md).

The **SUBVIEW** element can implement the following ambient event handlers: [onendmove](onendmove.md) and [onresize](onresize.md).

## Related topics

<dl> <dt>

[**Skin Programming Reference**](skin-programming-reference.md)
</dt> <dt>

[**VIEW Element**](view-element.md)
</dt> </dl>

 

 




