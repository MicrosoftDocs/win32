---
title: SLIDER Element
description: SLIDER Element
ms.assetid: 'f1da8987-5430-46ef-b7d7-ac92f34a2185'
keywords:
- Windows Media Player skins,SLIDER element
- skins,SLIDER element
- SLIDER element
- reference for skins,SLIDER element
- elements,SLIDER
ms.topic: article
ms.date: 05/31/2018
---

# SLIDER Element

The **SLIDER** element provides a way to create and manipulate a simple horizontal or vertical slider control. It supports the following attributes and event handlers. Predefined **SLIDER** elements are also provided for convenience.

The **SLIDER** element supports the following attributes.



| Attribute                                                 | Description                                                                                                       |
|-----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| [backgroundColor](slider-backgroundcolor.md)             | Specifies or retrieves the background color of the slider control.                                                |
| [backgroundEndColor](slider-backgroundendcolor.md)       | Specifies or retrieves the background ending color of the slider control.                                         |
| [backgroundHoverImage](slider-backgroundhoverimage.md)   | Specifies or retrieves the background image of the slider that appears when hovering over it with the mouse.      |
| [backgroundImage](slider-backgroundimage.md)             | Specifies or retrieves the default background image of the slider.                                                |
| [borderSize](slider-bordersize.md)                       | Specifies or retrieves the border size in pixels.                                                                 |
| [cursor](slider-cursor.md)                               | Specifies or retrieves a value indicating which type of cursor appears when the mouse is over the slider control. |
| [direction](slider-direction.md)                         | Specifies or retrieves the direction that slider images are laid out.                                             |
| [disabledColor](slider-disabledcolor.md)                 | Specifies or retrieves the disabled color of the slider control.                                                  |
| [disabledImage](slider-disabledimage.md)                 | Specifies or retrieves the image of the slider that appears when the control is disabled.                         |
| [foregroundColor](slider-foregroundcolor.md)             | Specifies or retrieves the foreground color of the slider control.                                                |
| [foregroundEndColor](slider-foregroundendcolor.md)       | Specifies or retrieves the foreground ending color of the slider control.                                         |
| [foregroundHoverImage](slider-foregroundhoverimage.md)   | Specifies or retrieves the foreground image of the slider that appears when hovering over it with the mouse.      |
| [foregroundImage](slider-foregroundimage.md)             | Specifies or retrieves the default foreground image of the slider.                                                |
| [foregroundProgress](slider-foregroundprogress.md)       | Specifies or retrieves the current position of the foreground progress bar as a percentage of the slider area.    |
| [max](slider-max.md)                                     | Specifies or retrieves the maximum value of the range defined by the slider control.                              |
| [min](slider-min.md)                                     | Specifies or retrieves the minimum value of the range defined by the slider control.                              |
| [slide](slider-slide.md)                                 | Specifies or retrieves a value indicating whether the foreground image slides over the background image.          |
| [thumbDisabledImage](slider-thumbdisabledimage.md)       | Specifies or retrieves the disabled thumb image of the slider control.                                            |
| [thumbDownImage](slider-thumbdownimage.md)               | Specifies or retrieves the image representing the down state of the thumb.                                        |
| [thumbHoverImage](slider-thumbhoverimage.md)             | Specifies or retrieves the image of the thumb that appears when hovering over it with the mouse.                  |
| [thumbImage](slider-thumbimage.md)                       | Specifies or retrieves the image that will be used to represent the current position of the slider.               |
| [tiled](slider-tiled.md)                                 | Specifies or retrieves a value indicating whether the slider images will be tiled.                                |
| [toolTip](slider-tooltip.md)                             | Specifies or retrieves the ToolTip text for the slider control.                                                   |
| [transparencyColor](slider-transparencycolor.md)         | Specifies or retrieves the transparent color of the slider images.                                                |
| [useForegroundProgress](slider-useforegroundprogress.md) | Specifies or retrieves a value indicating whether the foreground progress bar will be used.                       |
| [value](slider-value.md)                                 | Specifies and retrieves the current position of the slider.                                                       |



 

The **SLIDER** element can implement the following event handlers.



| Event handler                                   | Description                                                                                                          |
|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [onDragBegin](slider-ondragbegin.md)           | Handles an event that occurs when the user clicks and holds the left mouse button down and begins to drag the mouse. |
| [onDragEnd](slider-ondragend.md)               | Handles an event that occurs when the left mouse button is released after a dragging operation.                      |
| [onPositionChange](slider-onpositionchange.md) | Handles an event that occurs when the position of the slider changes as a result of the user clicking or dragging.   |



 

The **SLIDER** element supports the ambient attributes and can implement the ambient event handlers. For more information, see [Ambient Attributes](ambient-attributes.md) and [Ambient Event Handlers](ambient-event-handlers.md).

Predefined sliders are normal **SLIDER** elements with various common attribute settings specified by default. The following predefined sliders are available.



| Predefined SLIDER                  | Description                                                    |
|------------------------------------|----------------------------------------------------------------|
| [BALANCESLIDER](balanceslider.md) | A **SLIDER** used to set audio balance.                        |
| [SEEKSLIDER](seekslider.md)       | A **SLIDER** used to seek to any position within a media file. |
| [VOLUMESLIDER](volumeslider.md)   | A **SLIDER** used to set audio volume.                         |



 

## Related topics

<dl> <dt>

[**Skin Programming Reference**](skin-programming-reference.md)
</dt> </dl>

 

 




