---
title: IAgentNotifySink
description: IAgentNotifySink
ms.assetid: 70a3b011-0290-4df4-9b66-23b27bcb14e9
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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
| [**DragStart**](https://msdn.microsoft.com/library/windows/desktop/ms696427)                                | Occurs when a user starts dragging a character.                                          |
| [**DragComplete**](lwef-dragcomplete_method)                          | Occurs when a user stops dragging a character.                                           |
| [**RequestStart**](iagentnotifysink--requeststart.md)                | Occurs when the server begins processing a [**Request**](https://msdn.microsoft.com/library/windows/desktop/ms696325) object.    |
| [**RequestComplete**](iagentnotifysink--requestcomplete.md)          | Occurs when the server completes processing a [**Request**](https://msdn.microsoft.com/library/windows/desktop/ms696325) object. |
| [**Bookmark**](iagentnotifysink--bookmark.md)                        | Occurs when the server processes a bookmark.                                             |
| [**Idle**](iagentnotifysink--idle.md)                                | Occurs when the server starts or ends idle processing.                                   |
| [**Move**](iagentnotifysink--move.md)                                | Occurs when a character has been moved.                                                  |
| [**Size**](iagentnotifysink---size.md)                               | Occurs when a character has been resized.                                                |
| [**BalloonVisibleState**](iagentnotifysink---balloonvisiblestate.md) | Occurs when the visibility state of a character's word balloon changes.                  |



 

The IAgentNotifySink::Restart and IAgentNotifySink::Shutdown events, supported in earlier versions of Microsoft Agent, are now obsolete. While supported for backward compatibility, the server no longer sends these events.

 

 




