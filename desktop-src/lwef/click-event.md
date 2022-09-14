---
title: Click Event
description: Click Event
ms.assetid: 772029d5-97b6-49d8-a989-04f0fc429aca
ms.topic: article
ms.date: 05/31/2018
---

# Click Event

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Occurs when the user clicks a character or the character's icon.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

**Sub** *agent***\_Click** **(ByVal** *CharacterID*, **ByVal** *Button*, **ByVal** *Shift*, **ByVal** *X*, **ByVal** *Y***)**



| Part          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *CharacterID* | Returns the ID of the clicked character as a string.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| *Button*      | Returns an integer that identifies the button that was pressed and released to cause the event. The button argument is a bitfield with bits corresponding to the left button (bit 0), right button (bit 1), and middle button (bit 2). These bits correspond to the values 1, 2, and 4, respectively. Only one of the bits is set, indicating the button that caused the event. If the character includes a taskbar icon, and bit 13 is also set, the click occurred on the taskbar icon.                                                                                                                                                                      |
| *Shift*       | Returns an integer that corresponds to the state of the SHIFT, CTRL, and ALT keys when the button specified in the button argument is pressed or released. A bit is set if the key is down. The shift argument is a bitfield with the least-significant bits corresponding to the SHIFT key (bit 0), the CTRL key (bit 1), and the ALT key (bit 2). These bits correspond to the values 1, 2, and 4, respectively. The shift argument indicates the state of these keys. Some, all, or none of the bits can be set, indicating that some, all, or none of the keys are pressed. For example, if both CTRL and ALT were pressed, the value of shift would be 6. |
| *X,Y*         | Returns an integer that specifies the current location of the mouse pointer. The X and Y values are always expressed in pixels, relative to the upper-left corner of the screen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |



 

</dd> </dl>

### Remarks

This event is sent only to the input-active client of a character. When the user clicks a character or its taskbar icon with no input-active client, the server sends the event to its active client. If the character is visible ([**Visible**](visible-property.md) = **True**), the user's action also sets the character's last input-active client as the current input-active client, sending the [**ActivateInput**](activateinput-event.md) event to that client, and then sending the **Click** event. If the character is hidden (**Visible** = **False**), and the user clicks the character's taskbar icon using button 1, the character is also automatically shown.

> [!Note]  
> Clicking a character does not disable all other character output (all characters). However, pressing the Listening key does flush the input-active character's output and triggers the [**RequestComplete**](requestcomplete-event.md) event, passing a [Request.Status](status-property.md) that indicates that the client's queue was interrupted.

 

 

 




