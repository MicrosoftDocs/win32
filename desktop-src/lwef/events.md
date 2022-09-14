---
title: IAgentNotifySink
description: IAgentNotifySink
ms.assetid: 'vs|msagent|~\paface_2xet.htm'
ms.topic: article
ms.date: 05/31/2018
---

# IAgentNotifySink

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

IAgentNotifySink notifies clients when certain state changes occur. These functions are also available from [IAgentNotifySinkEx](iagentnotifysinkex.md).

**Methods in Vtable Order**



| IAgentNotifySink                                                      | Description                                                                              |
|-----------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| [**Command**](command-method.md)                                     | Occurs when the server processes a client-defined command.                               |
| [**ActivateInputState**](iagentnotifysink--activateinputstate.md)    | Occurs when a character becomes or ceases to be input-active.                            |
| [**BalloonVisibleState**](iagentnotifysink---balloonvisiblestate.md) | Occurs when the character's **Visible** state changes.                                   |
| [**Click Event**](click-event.md)                                    | Occurs when a character is clicked.                                                      |
| [**DblClick Event**](dblclick-event.md)                              | Occurs when a character is double-clicked.                                               |
| [**DragStart**](/windows/desktop/lwef/dragstart-event)                                | Occurs when a user starts dragging a character.                                          |
| [**DragComplete**](https://www.bing.com/search?q=**DragComplete**)                          | Occurs when a user stops dragging a character.                                           |
| [**RequestStart**](iagentnotifysink--requeststart.md)                | Occurs when the server begins processing a [**Request**](/windows/desktop/lwef/the-request-object) object.    |
| [**RequestComplete**](iagentnotifysink--requestcomplete.md)          | Occurs when the server completes processing a [**Request**](/windows/desktop/lwef/the-request-object) object. |
| [**Bookmark**](iagentnotifysink--bookmark.md)                        | Occurs when the server processes a bookmark.                                             |
| [**Idle**](iagentnotifysink--idle.md)                                | Occurs when the server starts or ends idle processing.                                   |
| [**Move**](iagentnotifysink--move.md)                                | Occurs when a character has been moved.                                                  |
| [**Size**](iagentnotifysink---size.md)                               | Occurs when a character has been resized.                                                |
| [**BalloonVisibleState**](iagentnotifysink---balloonvisiblestate.md) | Occurs when the visibility state of a character's word balloon changes.                  |



 

The IAgentNotifySink::Restart and IAgentNotifySink::Shutdown events, supported in earlier versions of Microsoft Agent, are now obsolete. While supported for backward compatibility, the server no longer sends these events.

 

 