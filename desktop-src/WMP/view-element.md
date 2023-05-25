---
title: VIEW Element
description: VIEW Element
ms.assetid: 'e1dfde08-33a0-4f12-8db0-ad62e4a1d467'
keywords:
- Windows Media Player skins,VIEW element
- skins,VIEW element
- VIEW element
- reference for skins,VIEW element
- elements,VIEW
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# VIEW Element

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **VIEW** element contains the user interface details of a skin, and uses the attributes, methods, and event handlers shown in the following tables.

Multiple **VIEW** elements can be defined as children of the **THEME** element of a skin to provide different interfaces for different situations. **VIEW** elements cannot be specified as children of any other element, and they contain all other skin elements. Note that each view has its own variable scope, which means it cannot share attribute values with other views.

The **view** global attribute can be used to reference a specific **VIEW** element from anywhere within it. This is an alternative to using its **id** attribute, which must be used from within other **VIEW** elements or from within the **THEME** element.

The **VIEW** element supports the following attributes. Attributes marked with an asterisk (\*) are also supported by the **SUBVIEW** element.



| Attribute                                                       | Description                                                                                                             |
|-----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| [backgroundColor](view-backgroundcolor.md) \*                  | Specifies or retrieves the background color of the **VIEW** or **SUBVIEW**.                                             |
| [backgroundImage](view-backgroundimage.md) \*                  | Specifies or retrieves the background image of the **VIEW** or **SUBVIEW**.                                             |
| [backgroundImageHueShift](view-backgroundimagehueshift.md)     | Specifies or retrieves the amount by which the hue of the background image is shifted.                                  |
| [backgroundImageSaturation](view-backgroundimagesaturation.md) | Specifies or retrieves the saturation value of the background image.                                                    |
| [backgroundTiled](view-backgroundtiled.md) \*                  | Specifies or retrieves a value indicating whether the background image of the **VIEW** or **SUBVIEW** is tiled.         |
| [category](view-category.md)                                   | Specifies or retrieves the category for which the user interface will appear.                                           |
| [focusObjectID](view-focusobjectid.md)                         | Specifies or retrieves a value indicating which element has keyboard focus.                                             |
| [maxHeight](view-maxheight.md)                                 | Specifies or retrieves the maximum height of the **VIEW** when resizing.                                                |
| [maxWidth](view-maxwidth.md)                                   | Specifies or retrieves the maximum width of the **VIEW** when resizing.                                                 |
| [minHeight](view-minheight.md)                                 | Specifies or retrieves the minimum height of the **VIEW** when resizing.                                                |
| [minWidth](view-minwidth.md)                                   | Specifies or retrieves the minimum width of the **VIEW** when resizing.                                                 |
| [resizable](view-resizable.md)                                 | Specifies or retrieves a value indicating whether the **VIEW** can be resized.                                          |
| [resizeBackgroundImage](view-resizebackgroundimage.md)         | Specifies or retrieves a value indicating whether the background image can be resized.                                  |
| [scriptFile](view-scriptfile.md)                               | Specifies the file names of accompanying JScript files.                                                                 |
| [timerInterval](view-timerinterval.md)                         | Specifies or retrieves the interval, in milliseconds, at which the timer fires events to the **ontimer** event handler. |
| [title](view-title.md)                                         | Specifies or retrieves the title of the **VIEW**. Can only be set at design time.                                       |
| [titleBar](view-titlebar.md)                                   | Specifies or retrieves a value indicating whether the window title bar is shown.                                        |
| [transparencyColor](view-transparencycolor.md) \*              | Specifies or retrieves the transparency color of the background image.                                                  |



 

The **VIEW** element supports the following methods.



| Method                                              | Description                                                |
|-----------------------------------------------------|------------------------------------------------------------|
| [close](view-close.md)                             | Closes the **VIEW**.                                       |
| [maximize](view-maximize.md)                       | Maximizes the **VIEW**.                                    |
| [minimize](view-minimize.md)                       | Minimizes the **VIEW**.                                    |
| [restore](view-restore.md)                         | Restores the **VIEW**.                                     |
| [returnToMediaCenter](view-returntomediacenter.md) | Returns the user to the full mode of Windows Media Player. |
| [size](view-size.md)                               | Resizes the **VIEW** on a specified edge.                  |



 

The **VIEW** element can implement the following event handlers.



| Event handler               | Description                                                                |
|-----------------------------|----------------------------------------------------------------------------|
| [onclose](view-onclose.md) | Handles an event that occurs when the **VIEW** is about to be closed.      |
| [onerror](view-onerror.md) | Handles an error event if **Settings.enableErrorDialogs** is set to false. |
| [onload](view-onload.md)   | Handles an event that occurs when the **VIEW** is first displayed.         |
| [ontimer](view-ontimer.md) | Handles timer events.                                                      |



 

The **VIEW** element supports the ambient attributes and can implement the ambient event handlers, except where noted. For more information, see [Ambient Attributes](ambient-attributes.md) and [Ambient Event Handlers](ambient-event-handlers.md),

## Related topics

<dl> <dt>

[**Skin Programming Reference**](skin-programming-reference.md)
</dt> </dl>

 

 




