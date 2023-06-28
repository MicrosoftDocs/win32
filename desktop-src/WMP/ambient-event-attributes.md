---
title: Ambient Event Attributes
description: Ambient Event Attributes
ms.assetid: 56cd2701-53b3-4456-8fcd-d65f8a6aefd7
keywords:
- Windows Media Player skins,ambient event attributes
- skins,ambient event attributes
- reference for skins,ambient event attributes
- ambient event attributes
- attributes,ambient event
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Ambient Event Attributes

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following attributes are common to all skin events. They are accessed with the **event** keyword within an event handler for the element.



| Attribute                              | Description                                                                                                  |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [altKey](event-altkey.md)             | Retrieves a value indicating whether the ALT key was down when the event occurred.                           |
| [button](event-button.md)             | Retrieves a value indicating which mouse buttons were down when the event occurred.                          |
| [clientX](event-clientx.md)           | Retrieves the x-coordinate of the mouse pointer with respect to the client region of the application window. |
| [clientY](event-clienty.md)           | Retrieves the y-coordinate of the mouse pointer with respect to the client region of the application window. |
| [ctrlKey](event-ctrlkey.md)           | Retrieves a value indicating whether the CTRL key was down when the event occurred.                          |
| [fromElement](event-fromelement.md)   | Retrieves the element the event came from.                                                                   |
| [keyCode](event-keycode.md)           | Retrieves the ASCII key code if a key was pressed when the event occurred.                                   |
| [offsetX](event-offsetx.md)           | Retrieves the x-coordinate of the mouse pointer with respect to the element firing the event.                |
| [offsetY](event-offsety.md)           | Retrieves the y-coordinate of the mouse pointer with respect to the element firing the event.                |
| [screenHeight](event-screenheight.md) | Retrieves the height of the available screen size in pixels.                                                 |
| [screenWidth](event-screenwidth.md)   | Retrieves the width of the available screen size in pixels.                                                  |
| [screenX](event-screenx.md)           | Retrieves the absolute x-coordinate of the mouse pointer with respect to the screen.                         |
| [screenY](event-screeny.md)           | Retrieves the absolute y-coordinate of the mouse pointer with respect to the screen.                         |
| [shiftKey](event-shiftkey.md)         | Retrieves a value indicating whether the SHIFT key was down when the event occurred.                         |
| [srcElement](event-srcelement.md)     | Retrieves the element that fired the event.                                                                  |
| [toElement](event-toelement.md)       | Retrieves the element the keyboard focus moved to.                                                           |
| [x](event-x.md)                       | Retrieves the x-coordinate of the mouse pointer with respect to the application window.                      |
| [y](event-y.md)                       | Retrieves the y-coordinate of the mouse pointer with respect to the application window.                      |



 

## Related topics

<dl> <dt>

[**Skin Programming Reference**](skin-programming-reference.md)
</dt> </dl>

 

 




