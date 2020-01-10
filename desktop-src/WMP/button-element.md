---
title: BUTTON Element (WMP)
description: BUTTON Element
ms.assetid: 2818ff6a-4fc5-4150-9ff9-ff143feb9204
keywords:
- Windows Media Player skins,BUTTON element
- skins,BUTTON element
- BUTTON element
- reference for skins,BUTTON element
- elements,BUTTON
ms.topic: article
ms.date: 05/31/2018
---

# BUTTON Element

The **BUTTON** element provides a way to create a button within a skin. The attributes below can be used to customize the behavior of a button, or a predefined button can be used for convenience.

The **BUTTON** element supports the following attributes.



| Attribute                                         | Description                                                                                                                                      |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| [cursor](button-cursor.md)                       | Specifies or retrieves the cursor that appears when the mouse pointer hovers over the **BUTTON**.                                                |
| [disabledImage](button-disabledimage.md)         | Specifies or retrieves the image that displays when the **BUTTON** is disabled.                                                                  |
| [down](button-down.md)                           | Specifies or retrieves a value indicating whether the **BUTTON** is in the up or down position.                                                  |
| [downImage](button-downimage.md)                 | Specifies or retrieves the image representing the down state of the **BUTTON**.                                                                  |
| [downToolTip](button-downtooltip.md)             | Specifies or retrieves the ToolTip text that appears when the mouse is over the **BUTTON** and the **BUTTON** is in the down or depressed state. |
| [hoverDownImage](button-hoverdownimage.md)       | Specifies or retrieves the image displayed when the **BUTTON** is in the down state and the user hovers over it with the mouse pointer.          |
| [hoverImage](button-hoverimage.md)               | Specifies or retrieves the image displayed when the **BUTTON** is in the up state and the user hovers over it with the mouse pointer.            |
| [image](button-image.md)                         | Specifies or retrieves the default image of the **BUTTON**.                                                                                      |
| [sticky](button-sticky.md)                       | Specifies or retrieves a value indicating whether the **BUTTON** is a toggle, that is, whether it is a two-state or single-state button.         |
| [tiled](button-tiled.md)                         | Specifies or retrieves a value indicating whether the **BUTTON** image will be tiled.                                                            |
| [transparencyColor](button-transparencycolor.md) | Specifies or retrieves the color that will be transparent in the **BUTTON** image.                                                               |
| [upToolTip](button-uptooltip.md)                 | Specifies or retrieves the ToolTip text that appears when the mouse is over the **BUTTON** and the **BUTTON** is in the up state.                |



 

The **BUTTON** element supports the ambient attributes and can implement the ambient event handlers. For more information, see [Ambient Attributes](ambient-attributes.md) and [Ambient Event Handlers](ambient-event-handlers.md).

Predefined buttons are normal **BUTTON** elements with various common attribute settings specified by default. The following predefined buttons are available.



| Predefined BUTTON                    | Description                                                                        |
|--------------------------------------|------------------------------------------------------------------------------------|
| [CLOSEBUTTON](closebutton.md)       | A **BUTTON** used to close the Player.                                             |
| [FFWDBUTTON](ffwdbutton.md)         | A **BUTTON** with a built in call to **player.controls.fastForward** when clicked. |
| [IMAGEBUTTON](imagebutton.md)       | A **BUTTON** used to display an image.                                             |
| [MINIMIZEBUTTON](minimizebutton.md) | A **BUTTON** used to minimize the Player.                                          |
| [MUTEBUTTON](mutebutton.md)         | A **BUTTON** used to mute and un-mute the audio.                                   |
| [NEXTBUTTON](nextbutton.md)         | A **BUTTON** with a built in call to **player.controls.next** when clicked.        |
| [PAUSEBUTTON](pausebutton.md)       | A **BUTTON** with a built in call to **player.controls.pause** when clicked.       |
| [PLAYBUTTON](playbutton.md)         | A **BUTTON** with a built in call to **player.controls.play** when clicked.        |
| [PREVBUTTON](prevbutton.md)         | A **BUTTON** with a built in call to **player.controls.previous** when clicked.    |
| [REPEATBUTTON](repeatbutton.md)     | A **BUTTON** that toggles the Repeat option.                                       |
| [RETURNBUTTON](returnbutton.md)     | A **BUTTON** that returns Windows Media Player to the media center.                |
| [REWBUTTON](rewbutton.md)           | A **BUTTON** with a built in call to **player.controls.fastReverse** when clicked. |
| [SHUFFLEBUTTON](shufflebutton.md)   | A **BUTTON** that toggles the Shuffle option.                                      |
| [STOPBUTTON](stopbutton.md)         | A **BUTTON** with a built in call to **player.controls.stop** when clicked.        |



 

## Related topics

<dl> <dt>

[**Skin Programming Reference**](skin-programming-reference.md)
</dt> </dl>

 

 




