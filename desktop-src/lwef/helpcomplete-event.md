---
title: HelpComplete Event
description: HelpComplete Event
ms.assetid: d805f089-154f-4b39-9d78-a02b732f87ed
ms.topic: article
ms.date: 05/31/2018
---

# HelpComplete Event

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Indicates that context-sensitive Help mode has been exited.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

**Sub** *agent.***(ByVal** *CharacterID***, ByVal** *Name***, ByVal** *Cause***)**



| Part          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *CharacterID* | Returns the ID of the clicked character as a string.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| *Name*        | Returns a string value identifying the name (ID) of the command.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| *Cause*       | Returns a value that indicates what caused the Help mode to complete. 1 The user selected a command supplied by your application.<br/> 2 The user selected the [**Commands**](/windows/desktop/lwef/the-commands-collection-object) object of another client.<br/> 3 The user selected the Open Voice Commands command.<br/> 4 The user selected the Close Voice Commands command.<br/> 5 The user selected the Show *CharacterName* command.<br/> 6 The user selected the Hide *CharacterName* command.<br/> 7 The user selected (clicked) the character.<br/> |



 

</dd> </dl>

### Remarks

Typically, Help mode completes when the user clicks or drags the character or selects a command from the character's pop-up menu. Clicking on another character or elsewhere on the screen does not cancel Help mode. The client that set Help mode for the character can cancel Help mode by setting [**HelpModeOn**](helpmodeon-property.md) to **False**. (This does not trigger the **HelpComplete** event.)

When the user selects a command from the character's pop-up menu in Help mode, the server removes the menu, calls Help with the command's specified [**HelpContextID**](helpcontextid-property.md), and sends this event. The context-sensitive (also known as What's This?) Help window is displayed at the pointer location. If the user selects the command by voice input, the Help window is displayed over the character. If the character is off-screen, the window is displayed on-screen nearest to the character's current position.

If the server returns Name as an empty string (""), it indicates that the user selected a server-supplied command.

This event is sent only to the client application that places the character in Help mode.

### See Also

[**HelpModeOn property**](helpmodeon-property.md), [**HelpContextID property**](helpcontextid-property.md)


 

