---
title: Implementing In-Place Activation
description: Implementing In-Place Activation
ms.assetid: 5fd67d1c-1dc5-4d83-a41e-b64d84cbf212
ms.topic: article
ms.date: 05/31/2018
---

# Implementing In-Place Activation

In-place activation enables a user to interact with an embedded object without leaving the container document. When a user activates the object, a *composite menu bar* comprising elements from both the container application's and server application's menu bars replaces the container's main menu bar. Commands and features from both applications are thus available to the user, including context sensitive help for the active object. When a user begins working with some non-object portion of the document, the object is deactivated, causing the container document's original menu to replace the composite menu.

This capability originally went by the name of *in-place editing*. The name was changed because editing is only one way for a user to interact with a running object. Sound clips, for example, can be listened to instead of editing. Video clips can be viewed instead of editing. In-place activation is particularly apt in the case of video clips because it allows them to run in place, without calling up a separate window. This could be critical if the video were to be viewed, say, in conjunction with adjacent text data in the container document.

Implementing in-place activation is strictly optional for both container and server applications. OLE still supports the model in which activating an object causes the server application to open a separate window. Linked objects always open in a separate window to emphasize that they reside in a separate document.

In-place activation begins with the object in response to an [**IOleObject::DoVerb**](/windows/desktop/api/OleIdl/nf-oleidl-ioleobject-doverb) call from its container. This call usually happens in response to a user double-clicking the object or selecting a command (verb) from the container application's Edit menu.

The in-place window receives keyboard and mouse input while the embedded object is active. When a user selects commands from the composite menu bar, the command and associated menu messages are sent to the container or object application, depending on which owns the particular drop-down menu selected. Input by means of an object's rulers, toolbars, or frame adornments go directly to the embedded object, which owns these windows.

An in-place-activated embedded object remains active until either the container deactivates it in response to user input or the object voluntarily gives up the active state, as a video clip might do, for example. A user can deactivate an object by clicking inside the container document but outside the object's in-place-activation window, or simply by clicking another object. An in-place-activated object remains active, however, if the user clicks the container's title bar, scroll bar or, in particular, menu bar.

You can implement an in-place-activation-object server either as an in-process server (DLL) or a local server (EXE). In both cases, the composite menu bar contains items (typically drop-down menus) from both the server and container processes. In the case of a in-process server, the in-place activation window is simply another child window in the container's window hierarchy, receiving its input through the container application's message pump.

In the case of a local server, the in-place activation window belongs to the embedded object's server application process, but its parent window belongs to the container. Input for the in-place-activation window appears in the server's message queue and is dispatched by the server's message loop. The OLE libraries are responsible for seeing to it that menu commands and messages are dispatched correctly.

## Related topics

<dl> <dt>

[Compound Documents](compound-documents.md)
</dt> </dl>

 

 




