---
title: BUTTONGROUP Element
description: BUTTONGROUP Element
ms.assetid: 4756c016-3347-4129-be5e-e822270a24de
keywords:
- Windows Media Player skins,BUTTONGROUP element
- skins,BUTTONGROUP element
- BUTTONGROUP element
- reference for skins,BUTTONGROUP element
- elements,BUTTONGROUP
ms.topic: article
ms.date: 05/31/2018
---

# BUTTONGROUP Element

The **BUTTONGROUP** element provides a way to group several buttons within a skin. These buttons can be specified by using **BUTTONELEMENT** elements as children of the **BUTTONGROUP** element.

The **BUTTONGROUP** element supports the following attributes.



| Attribute                                              | Description                                                                                                                                                                                                                     |
|--------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [buttonCount](buttongroup-buttoncount.md)             | Retrieves the number of buttons in the **BUTTONGROUP**.                                                                                                                                                                         |
| [cursor](buttongroup-cursor.md)                       | Specifies or retrieves the type of cursor that appears when the mouse is over a button in the **BUTTONGROUP**.                                                                                                                  |
| [disabledImage](buttongroup-disabledimage.md)         | Specifies or retrieves the name of the image representing the disabled state of the buttons in the **BUTTONGROUP**.                                                                                                             |
| [downImage](buttongroup-downimage.md)                 | Specifies or retrieves the name of the image representing the down state of the **BUTTONGROUP**.                                                                                                                                |
| [hoverDownImage](buttongroup-hoverdownimage.md)       | Specifies or retrieves the name of the image representing the hover-down state of a button in the **BUTTONGROUP**. The hover-down state occurs when the button is in the down state and the user hovers over it with the mouse. |
| [hoverImage](buttongroup-hoverimage.md)               | Specifies or retrieves the name of the image representing the hover state of a button in the **BUTTONGROUP**. The hover state occurs when the button is in the up state and the user hovers over it with the mouse.             |
| [hueShift](buttongroup-hueshift.md)                   | Specifies or retrieves the amount by which the hue of the **BUTTONGROUP** images is shifted.                                                                                                                                    |
| [image](buttongroup-image.md)                         | Specifies or retrieves the name of the image representing the buttons of a **BUTTONGROUP**.                                                                                                                                     |
| [mappingImage](buttongroup-mappingimage.md)           | Specifies or retrieves the name of the image representing the button map of the **BUTTONGROUP**.                                                                                                                                |
| [radio](buttongroup-radio.md)                         | Specifies or retrieves a value indicating whether the **BUTTONGROUP** is composed of radio buttons.                                                                                                                             |
| [saturation](buttongroup-saturation.md)               | Specifies or retrieves the saturation value of the **BUTTONGROUP** images.                                                                                                                                                      |
| [showBackground](buttongroup-showbackground.md)       | Specifies or retrieves a value indicating whether the **BUTTONGROUP** displays only the buttons, or displays the full bitmap specified in the **image** attribute.                                                              |
| [transparencyColor](buttongroup-transparencycolor.md) | Specifies or retrieves the transparent color of the **BUTTONGROUP** images.                                                                                                                                                     |



 

The **BUTTONGROUP** element supports the following methods.



| Method                                 | Description                                                                                     |
|----------------------------------------|-------------------------------------------------------------------------------------------------|
| [click](buttongroup-click.md)         | Calls the **onclick** event handler defined for the **BUTTONELEMENT** with the specified index. |
| [getButton](buttongroup-getbutton.md) | Retrieves the **BUTTONELEMENT** with the specified index.                                       |



 

The **BUTTONGROUP** element supports the ambient attributes and can implement the ambient event handlers. For more information, see [Ambient Attributes](ambient-attributes.md) and [Ambient Event Handlers](ambient-event-handlers.md).

## Related topics

<dl> <dt>

[**Skin Programming Reference**](skin-programming-reference.md)
</dt> </dl>

 

 




