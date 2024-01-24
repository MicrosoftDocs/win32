---
title: Ambient Event Handlers
description: Ambient Event Handlers
ms.assetid: ec806b92-a66d-499d-9bb3-cea7e82676bb
keywords:
- Windows Media Player skins,ambient event handlers
- skins,ambient event handlers
- reference for skins,ambient event handlers
- ambient event handlers
- events,ambient
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Ambient Event Handlers

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following event handlers can be implemented for most skin elements. The ambient event attributes accessed with the **event** keyword can be used within an event handler to determine the state of the keyboard and mouse at the time of the event.



| Event handler                                   | Description                                                                                                                                                                                                                   |
|-------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [*attribute*\_onchange](attribute-onchange.md) | When a skin attribute changes value, an event occurs that can be handled by an event handler. The name of the event handler is the name of the attribute followed by an underscore and "onchange", such as "value\_onchange". |
| [onblur](onblur.md)                            | Handles an event that occurs when the element loses the keyboard focus.                                                                                                                                                       |
| [onclick](onclick.md)                          | Handles an event that occurs when the user clicks the element.                                                                                                                                                                |
| [ondblclick](ondblclick.md)                    | Handles an event that occurs when the user double-clicks the element.                                                                                                                                                         |
| [onendalphablend](onendalphablend.md)          | Handles an event that occurs when an element completes an **alphaBlendTo** operation.                                                                                                                                         |
| [onendmove](onendmove.md)                      | Handles an event that occurs when an element completes a **moveTo** operation.                                                                                                                                                |
| [onfocus](onfocus.md)                          | Handles an event that occurs when the element receives the keyboard focus.                                                                                                                                                    |
| [onkeydown](onkeydown.md)                      | Handles an event that occurs when a key is pressed.                                                                                                                                                                           |
| [onkeypress](onkeypress.md)                    | Handles an event that occurs when the user presses an alphanumeric key.                                                                                                                                                       |
| [onkeyup](onkeyup.md)                          | Handles an event that occurs when a key is released.                                                                                                                                                                          |
| [onmousedown](onmousedown.md)                  | Handles an event that occurs when the user clicks a mouse button.                                                                                                                                                             |
| [onmousemove](onmousemove.md)                  | Handles an event that occurs when the user moves the mouse pointer while it is over an element.                                                                                                                               |
| [onmouseout](onmouseout.md)                    | Handles an event that occurs when the user moves the pointer off the element.                                                                                                                                                 |
| [onmouseover](onmouseover.md)                  | Handles an event that occurs when the user first places the pointer over the element.                                                                                                                                         |
| [onmouseup](onmouseup.md)                      | Handles an event that occurs when the user releases a mouse button while the pointer is over the element.                                                                                                                     |
| [onresize](onresize.md)                        | Handles an event that occurs when a control resizes.                                                                                                                                                                          |



 

## Related topics

<dl> <dt>

[**Ambient Event Attributes**](ambient-event-attributes.md)
</dt> <dt>

[**Skin Programming Reference**](skin-programming-reference.md)
</dt> </dl>

 

 




