---
title: IAgentNotifySink DragStart
description: IAgentNotifySink DragStart
ms.assetid: b3905b99-69e4-4046-aab9-2322618935aa
ms.topic: article
ms.date: 05/31/2018
---

# IAgentNotifySink::DragStart

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT DragStart(
   long dwCharID,  // character ID
   short fwKeys,   // mouse button and modifier key state
   long x,         // x-coordinate of mouse pointer
   long y          // y-coordinate of mouse pointer
);                          
```

Notifies a client application when the user starts dragging a character.

-   No return value.

<dl> <dt>

<span id="dwCharID"></span><span id="dwcharid"></span><span id="DWCHARID"></span>*dwCharID*
</dt> <dd>

Identifier of the dragged character.

</dd> <dt>

<span id="fwKeys"></span><span id="fwkeys"></span><span id="FWKEYS"></span>*fwKeys*
</dt> <dd>

A parameter that indicates the mouse button and modifier key state. The parameter can return any combination of the following:



| Value  | Description      |
|--------|------------------|
| 0x0001 | Left Button      |
| 0x0010 | Middle Button    |
| 0x0002 | Right Button     |
| 0x0004 | Shift Key Down   |
| 0x0008 | Control Key Down |
| 0x0020 | Alt Key Down     |



 

</dd> <dt>

<span id="x"></span><span id="X"></span>*x*
</dt> <dd>

The x-coordinate of the mouse pointer in pixels, relative to the screen origin (upper left).

</dd> <dt>

<span id="y"></span><span id="Y"></span>*y*
</dt> <dd>

The y-coordinate of the mouse pointer in pixels, relative to the screen origin (upper left).

</dd> </dl>

 

 




