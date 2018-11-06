---
title: DragStart Event
description: DragStart Event
ms.assetid: fef0ae05-1958-45c6-8260-107c47b5fa92
ms.topic: article
ms.date: 05/31/2018
---

# DragStart Event

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Occurs when the user begins dragging a character.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

**Sub** *agent***\_DragStart** **(ByVal** *CharacterID*, **(ByVal** *Button*, **(ByVal** *Shift*, **(ByVal** *X*, **(ByVal** *Y***)**



| Part          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *CharacterID* | Returns the ID of the clicked character as a string.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| *Button*      | Returns an integer that identifies the button that was pressed and released to cause the event. The button argument is a bitfield with bits corresponding to the left button (bit 0), right button (bit 1), and middle button (bit 2). These bits correspond to the values 1, 2, and 4, respectively. Only one of the bits is set, indicating the button that caused the event.                                                                                                                                                                                                                                                                                |
| *Shift*       | Returns an integer that corresponds to the state of the SHIFT, CTRL, and ALT keys when the button specified in the button argument is pressed or released. A bit is set if the key is down. The shift argument is a bitfield with the least-significant bits corresponding to the SHIFT key (bit 0), the CTRL key (bit 1), and the ALT key (bit 2). These bits correspond to the values 1, 2, and 4, respectively. The shift argument indicates the state of these keys. Some, all, or none of the bits can be set, indicating that some, all, or none of the keys are pressed. For example, if both CTRL and ALT were pressed, the value of shift would be 6. |
| *X,Y*         | Returns an integer that specifies the current location of the mouse pointer. The X and Y values are always expressed in pixels, relative to the upper left corner of the screen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |



 

</dd> </dl>

### Remarks

This event is sent only to the input-active client of a character. When the user drags a character with no input-active client, the server sets its last input-active client as the current input-active client, sending the [**ActivateInput**](activateinput-event.md) event to that client, and then sending the **DragStart** event.

### See Also

[**DragComplete event**](dragcomplete-event.md)


 

 




