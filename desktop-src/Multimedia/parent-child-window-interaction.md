---
title: Parent-Child Window Interaction
description: Parent-Child Window Interaction
ms.assetid: de10bf12-4ba4-4c6b-be56-489e4e2b26b1
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Parent-Child Window Interaction

Some system-level messages, such as [**WM\_PALETTECHANGED**](https://msdn.microsoft.com/library/windows/desktop/dd145214) and [**WM\_QUERYNEWPALETTE**](https://msdn.microsoft.com/library/windows/desktop/dd145218), are sent only to top-level and overlapped windows. If a capture window is a child window, its parent must forward these messages.

Similarly, if the parent window changes size, it might need to send notification messages to the capture window. Conversely, if the dimensions of the captured video change, the capture window might need to send notification messages to the parent window. The simplest way to manage this is to always keep the capture window dimensions equal to the size of the captured video stream, notifying the parent whenever these dimensions change.

## Related topics

<dl> <dt>

[Capture Windows](capture-windows.md)
</dt> </dl>

 

 




