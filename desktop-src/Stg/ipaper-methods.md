---
title: IPaper Methods
description: Provides COPaper objects that are controlled primarily by their native IPaper interface.
ms.assetid: 3b77a6b3-8ec3-4a91-82cd-1f08d10fbf73
keywords:
- IPaper
ms.topic: reference
ms.date: 05/31/2018
---

# IPaper Methods

**StoServe**provides COPaper objects that are controlled primarily by their native **IPaper** interface.

The following table lists **IPaper** methods from IPAPER.H in the sibling \\INC directory.



| Method    | Description                                                         |
|-----------|---------------------------------------------------------------------|
| InitPaper | Initializes paper object and create ink data array.                 |
| Lock      | Gives client control of the paper and locks out other clients.      |
| Unlock    | Relinquishes client control of the paper.                           |
| Load      | Loads paper content from client's compound file and notifies sinks. |
| Save      | Saves paper content to client's compound file.                      |
| InkStart  | Starts color ink drawing to the paper surface.                      |
| InkDraw   | Puts ink data points on the electronic paper surface.               |
| InkStop   | Stops ink drawing to the paper surface.                             |
| Erase     | Erase the current paper content and notifies sinks.                 |
| Resize    | Resizes the drawing paper rectangle size and notifies sinks.        |
| Redraw    | Redraws contents of paper object and notifies sinks.                |



 

Methods of interest for this code sample on compound files are [**Load**](ipaper--load.md), [**Save**](ipaper--save.md), and [**Redraw**](ipaper--redraw.md).

[**InkStart**](inkstart-method.md), [**InkDraw**](inkdraw-method.md), and [**InkStop**](cguipaper-methods.md) are methods used by clients to command COPaper to record ink drawing sequences. The client will typically respond to a WM\_LBUTTONDOWN message as the start of an ink drawing sequence by calling **InkStart** on COPaper. As the user moves the mouse or pen to draw while holding down the left button, the client will respond to repeated WM\_MOUSEMOVE messages with corresponding calls to **InkDraw**. When the user releases the left mouse button, the client will respond to a WM\_LBUTTONUP message with a call to **InkStop**, which marks the end of the ink drawing sequence.

[**InkStart**](inkstart-method.md) tells COPaper the start position for the drawing sequence in client window coordinates. It also passes the currently selected ink color and width. The client maintains these selections; COPaper merely records them when the **InkStart** call is made. [**InkDraw**](inkdraw-method.md) is called repeatedly to tell COPaper the succession of window coordinates that represent the drawing motion of the mouse or pen. [**InkStop**](cguipaper-methods.md) instructs COPaper to mark the end of a drawing sequence.

 

 




