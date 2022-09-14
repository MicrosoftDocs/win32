---
title: IAgentNotifySink DblClick
description: IAgentNotifySink DblClick
ms.assetid: 7e86cc9b-8bc3-405e-9bbf-764cec9c3130
ms.topic: article
ms.date: 05/31/2018
---

# IAgentNotifySink::DblClick

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT DblClick(
   long dwCharID,  // character ID
   short fwKeys,   // mouse button and modifier key state
   long x,         // x coordinate of mouse pointer
   long y          // y coordinate of mouse pointer
);                          
```

Notifies a client application when the user double-clicks a character.

-   No return value.

<dl> <dt>

<span id="dwCharID"></span><span id="dwcharid"></span><span id="DWCHARID"></span>*dwCharID*
</dt> <dd>

Identifier of the double-clicked character.

</dd> <dt>

<span id="fwKeys"></span><span id="fwkeys"></span><span id="FWKEYS"></span>*fwKeys*
</dt> <dd>

A parameter that indicates the mouse button and modifier key state. The parameter can return any combination of the following:



| Value  | Description                               |
|--------|------------------------------------------------|
| 0x0001 | Left Button                                    |
| 0x0010 | Middle Button                                  |
| 0x0002 | Right Button                                   |
| 0x0004 | Shift Key Down                                 |
| 0x0008 | Control Key Down                               |
| 0x0020 | Alt Key Down                                   |
| 0x1000 | Event occurred on the character's taskbar icon |



 

</dd> <dt>

<span id="x"></span><span id="X"></span>*x*
</dt> <dd>

The x-coordinate of the mouse pointer in pixels, relative to the screen origin (upper left).

</dd> <dt>

<span id="y"></span><span id="Y"></span>*y*
</dt> <dd>

The y-coordinate of the mouse pointer in pixels, relative to the screen origin (upper left).

</dd> </dl>

This event is sent to the input-active client of the character. If none of the character's clients are input-active, the server notifies the character's active client. If the character is visible, the server also makes that client input-active and sends the [**IAgentNotifySink::ActivateInputState**](iagentnotifysink--activateinputstate.md). If the character is hidden, the character is also automatically shown.

 

 




