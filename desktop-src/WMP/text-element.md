---
title: TEXT Element (Windows Media Player SDK)
description: TEXT Element
ms.assetid: '4523fe7a-a77a-4bf2-9195-3943bff0eb21'
keywords:
- Windows Media Player skins,TEXT element
- skins,TEXT element
- TEXT element
- reference for skins,TEXT element
- elements,TEXT
ms.topic: article
ms.date: 05/31/2018
---

# TEXT Element

The **TEXT** element provides a way to create and control the appearance of text within a skin by using the following attributes. Predefined **TEXT** elements are also provided for convenience.

The **TEXT** element supports the following attributes.



| Attribute                                                   | Description                                                                                                 |
|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| [backgroundColor](text-backgroundcolor.md)                 | Specifies or retrieves the background color for the Text control.                                           |
| [cursor](text-cursor.md)                                   | Specifies or retrieves a value indicating which cursor appears when the mouse is over the Text control.     |
| [disabledBackgroundColor](text-disabledbackgroundcolor.md) | Specifies or retrieves the background color used for the Text control when it is disabled.                  |
| [disabledFontStyle](text-disabledfontstyle.md)             | Specifies or retrieves the font style used for the Text control when it is disabled.                        |
| [disabledForegroundColor](text-disabledforegroundcolor.md) | Specifies or retrieves the text color used when the Text control is disabled.                               |
| [fontFace](text-fontface.md)                               | Specifies or retrieves the typeface for the Text control.                                                   |
| [fontSize](text-fontsize.md)                               | Specifies or retrieves the font size for the Text control.                                                  |
| [fontSmoothing](text-fontsmoothing.md)                     | Specifies or retrieves a value indicating whether font smoothing is enabled.                                |
| [fontStyle](text-fontstyle.md)                             | Specifies or retrieves the font style for the Text control.                                                 |
| [foregroundColor](text-foregroundcolor.md)                 | Specifies or retrieves the text color for the Text control.                                                 |
| [hoverBackgroundColor](text-hoverbackgroundcolor.md)       | Specifies or retrieves the background color used for the Text control when the mouse cursor hovers over it. |
| [hoverFontStyle](text-hoverfontstyle.md)                   | Specifies or retrieves the font style used for the Text control when the mouse cursor hovers over it.       |
| [hoverForegroundColor](text-hoverforegroundcolor.md)       | Specifies or retrieves the text color used for the Text control when the mouse cursor hovers over it.       |
| [justification](text-justification.md)                     | Specifies or retrieves the alignment of the text within the Text control.                                   |
| [scrolling](text-scrolling.md)                             | Specifies or retrieves a value indicating whether the text scrolls.                                         |
| [scrollingAmount](text-scrollingamount.md)                 | Specifies or retrieves the number of pixels that the text moves during each scrolling movement.             |
| [scrollingDelay](text-scrollingdelay.md)                   | Specifies or retrieves the time delay between scrolling movements.                                          |
| [scrollingDirection](text-scrollingdirection.md)           | Specifies or retrieves the direction of the scrolling text.                                                 |
| [textWidth](text-textwidth.md)                             | Retrieves the width in pixels of the string contained in the **value** attribute.                           |
| [toolTip](text-tooltip.md)                                 | Specifies or retrieves the ToolTip text for the text control.                                               |
| [value](text-value.md)                                     | Specifies or retrieves the text that is displayed in the Text control.                                      |
| [wordWrap](text-wordwrap.md)                               | Specifies or retrieves a value indicating whether word wrapping is enabled or disabled.                     |



 

The **TEXT** element supports the ambient attributes and can implement the ambient event handlers. For more information, see [Ambient Attributes](ambient-attributes.md) and [Ambient Event Handlers](ambient-event-handlers.md).

Predefined text elements are normal **TEXT** elements with various common attribute settings specified by default. The following predefined text elements are available.



| Predefined TEXT                                | Description                                                                                |
|------------------------------------------------|--------------------------------------------------------------------------------------------|
| [CURRENTPOSITIONTEXT](currentpositiontext.md) | A **TEXT** element with a built in listener for **player.controls.currentPositionString**. |
| [DURATIONTEXT](durationtext.md)               | A **TEXT** element with a built in listener for **player.currentMedia.DurationString**.    |
| [STATUSTEXT](statustext.md)                   | A **TEXT** element with a built in listener for **player.status**.                         |
| [TRACKNAMETEXT](tracknametext.md)             | A **TEXT** element with a built in listener for **player.currentMedia.name**.              |



 

## Related topics

<dl> <dt>

[**Skin Programming Reference**](skin-programming-reference.md)
</dt> </dl>

 

 




