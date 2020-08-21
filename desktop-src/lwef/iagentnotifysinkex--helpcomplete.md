---
title: IAgentNotifySinkEx HelpComplete
description: IAgentNotifySinkEx HelpComplete
ms.assetid: f8285d05-3b96-4046-a058-0e001e47b54b
ms.topic: article
ms.date: 05/31/2018
---

# IAgentNotifySinkEx::HelpComplete

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT HelpComplete(
   long dwCharID,     // character ID
   long dwCommandID,  // command ID
   long dwCause       // cause 
);
```

Notifies a client application when the user selects a command or character to complete Help mode.

-   No return value.

<dl> <dt>

<span id="dwCharID"></span><span id="dwcharid"></span><span id="DWCHARID"></span>*dwCharID*
</dt> <dd>

Identifier of the character for which Help mode completed.

</dd> <dt>

<span id="dwCommandID"></span><span id="dwcommandid"></span><span id="DWCOMMANDID"></span>*dwCommandID*
</dt> <dd>

Identifier of the command the user selected.

</dd> <dt>

<span id="dwCause"></span><span id="dwcause"></span><span id="DWCAUSE"></span>*dwCause*
</dt> <dd>

The cause for the event, which may be the following values:



| Value                                                                         | Description                                                                          |
|-------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| **const unsigned short** **CSHELPCAUSE\_COMMAND = 1;**<br/>             | The user selected a command supplied by your application.                            |
| **const unsigned short** **CSHELPCAUSE\_OTHERPROGRAM = 2;**<br/>        | The user selected the [**Commands**](/windows/desktop/lwef/the-commands-collection-object) object of another client. |
| **const unsigned short** **CSHELPCAUSE\_OPENCOMMANDSWINDOW = 3;**<br/>  | The user selected the Open Voice Commands command.                                   |
| **const unsigned short** **CSHELPCAUSE\_CLOSECOMMANDSWINDOW = 4;**<br/> | The user selected the Close Voice Commands command.                                  |
| **const unsigned short** **CSHELPCAUSE\_SHOWCHARACTER = 5;**<br/>       | The user selected the Show *CharacterName* command.                                  |
| **const unsigned short** **CSHELPCAUSE\_HIDECHARACTER = 6;**<br/>       | The user selected the Hide *CharacterName* command.                                  |
| **const unsigned short** **CSHELPCAUSE\_CHARACTER = 7;**<br/>           | The user selected (clicked) the character.                                           |



 

</dd> </dl>

Typically Help mode completes when the user clicks or drags the character or selects a command from the character's pop-up menu. Clicking on another character or elsewhere on the screen does not cancel Help mode. The client that set Help mode for the character can cancel Help mode by setting [**IAgentCharacter::HelpModeOn**](https://www.bing.com/search?q=**IAgentCharacter::HelpModeOn**) to **False**. (This does not trigger the **IAgentNotifySinkEx::HelpComplete** event.)

When the user selects a command from the character's pop-up menu in Help mode, the server removes the menu, calls Help with the command's specified [**HelpContextID**](helpcontextid-property.md), and sends this event. The context-sensitive (also known as What's This?) Help window is displayed at the pointer location. If the user selects the command by voice input, the Help window is displayed over the character. If the character is off-screen, the window is displayed on-screen nearest to the character's current position.

If the server returns *dwCommandID* as an empty string (""), it indicates that the user selected a server-supplied command.

This event is sent only to the client application that places the character into Help mode.

## See Also

[**IAgentCharacterEx::SetHelpModeOn**](iagentcharacterex--sethelpmodeon.md), [**IAgentCharacterEx::SetHelpFileName**](iagentcharacterex--sethelpfilename.md), [**IAgentCharacterEx::SetHelpContextID**](iagentcharacterex--sethelpcontextid.md), [**IAgentCommandsEx::SetHelpContextID**](iagentcommandsex--sethelpcontextid.md)


 

