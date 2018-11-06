---
title: VIDEO Element
description: VIDEO Element
ms.assetid: 817e0d2e-cbc3-4b61-81c0-876104125f39
keywords:
- Windows Media Player skins,VIDEO element
- skins,VIDEO element
- VIDEO element
- reference for skins,VIDEO element
- elements,VIDEO
ms.topic: article
ms.date: 05/31/2018
---

# VIDEO Element

The **VIDEO** element provides a way to manipulate a video window in a skin, using the following attributes and events. A predefined **VIDEO** element is also provided for convenience.

The **VIDEO** element supports the following attributes.



| Attribute                                            | Description                                                                                                                                                                                                                              |
|------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [backgroundColor](video-backgroundcolor.md)         | Specifies or retrieves the background color of the Video control.                                                                                                                                                                        |
| [cursor](video-cursor.md)                           | Specifies or retrieves the cursor value that is used when the mouse is over a clickable area of the video.                                                                                                                               |
| [fullScreen](video-fullscreen.md)                   | Specifies or retrieves a value indicating whether the video is displayed in full-screen mode. Can only be set at run time.                                                                                                               |
| [maintainAspectRatio](video-maintainaspectratio.md) | Specifies or retrieves a value indicating whether the video will maintain the aspect ratio when trying to fit within the width and height defined for the control.                                                                       |
| [shrinkToFit](video-shrinktofit.md)                 | Specifies or retrieves a value indicating whether the video will shrink to the width and height defined for the Video control.                                                                                                           |
| [stretchToFit](video-stretchtofit.md)               | Specifies or retrieves a value indicating whether the video will stretch itself to the width and height defined for the Video control.                                                                                                   |
| [toolTip](video-tooltip.md)                         | Specifies or retrieves the ToolTip text for the video window.                                                                                                                                                                            |
| [windowless](video-windowless.md)                   | Specifies or retrieves a value indicating whether the Video control will be windowed or windowless; that is, whether the entire rectangle of the control will be visible at all times or can be clipped. Can only be set at design time. |
| [zoom](video-zoom.md)                               | Specifies the percentage by which to scale the video.                                                                                                                                                                                    |



 

The **VIDEO** element can implement the following event handlers.



| Event handler                          | Description                                                                  |
|----------------------------------------|------------------------------------------------------------------------------|
| [onvideoend](video-onvideoend.md)     | Handles an event that occurs when the video stops rendering and is unloaded. |
| [onvideostart](video-onvideostart.md) | Handles an event that occurs when the video is loaded and begins to render.  |



 

The **VIDEO** element supports the ambient attributes and can implement the ambient event handlers, except where noted. For more information, see [Ambient Attributes](ambient-attributes.md) and [Ambient Event Handlers](ambient-event-handlers.md).

Predefined video elements are normal **VIDEO** elements with various common attribute settings specified by default. The following predefined video elements are available.



| Predefined VIDEO         | Description                                                |
|--------------------------|------------------------------------------------------------|
| [WMPVIDEO](wmpvideo.md) | A **VIDEO** element that stretches the video when resized. |



 

## Related topics

<dl> <dt>

[**Skin Programming Reference**](skin-programming-reference.md)
</dt> </dl>

 

 




