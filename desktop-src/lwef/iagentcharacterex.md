---
title: IAgentCharacterEx
description: IAgentCharacterEx
ms.assetid: 8defc836-cc54-40c7-8afc-ec90f941861b
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacterEx

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

**IAgentCharacterEx** derives from the [**IAgentCharacter**](iagentcharacter.md) interface. It includes all the **IAgentCharacter** methods as well as provides access to additional functions.

**Methods in Vtable Order**



| IAgentCharacterEx Methods                                         | Description                                                                    |
|-------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [**ShowPopupMenu**](iagentcharacterex--showpopupmenu.md)         | Displays the pop-up menu for the character.                                    |
| [**SetAutoPopupMenu**](iagentcharacterex--setautopopupmenu.md)   | Sets whether the server automatically displays the character's pop-up menu.    |
| [**GetAutoPopupMenu**](iagentcharacterex--getautopopupmenu.md)   | Returns whether the server automatically displays the character's pop-up menu. |
| [**GetHelpFileName**](iagentcharacterex--gethelpfilename.md)     | Returns the Help filename for the character.                                   |
| [**SetHelpFileName**](iagentcharacterex--sethelpfilename.md)     | Sets the Help filename for the character.                                      |
| [**SetHelpModeOn**](iagentcharacterex--sethelpmodeon.md)         | Sets Help mode on.                                                             |
| [**GetHelpModeOn**](iagentcharacterex--gethelpmodeon.md)         | Returns whether Help mode is on.                                               |
| [**SetHelpContextID**](iagentcharacterex--sethelpcontextid.md)   | Sets the HelpContextID for the character.                                      |
| [**GetHelpContextID**](iagentcharacterex--gethelpcontextid.md)   | Returns the HelpContextID for the character.                                   |
| [**GetActive**](iagentcharacterex--getactive.md)                 | Returns the active state for the character.                                    |
| [**Listen**](iagentcharacterex--listen.md)                       | Sets the listening state for the character.                                    |
| [**SetLanguageID**](iagentcharacterex--setlanguageid.md)         | Sets the language ID for the character.                                        |
| [**getLanguageID**](iagentcharacterex--getlanguageid.md)         | Returns the language ID for the character.                                     |
| [**getTTSModeID**](iagentcharacterex--getttsmodeid.md)           | Returns the TTS mode ID set for the character.                                 |
| [**SetTTSModeID**](iagentcharacterex--setttsmodeid.md)           | Sets the TTS mode ID for the character.                                        |
| [**getSRModeID**](iagentcharacterex--getsrmodeid.md)             | Returns the current speech recognition engine's mode ID.                       |
| [**setSRModeID**](iagentcharacterex--setsrmodeid.md)             | Sets the speech recognition engine.                                            |
| [**GetGUID**](iagentcharacterex--getguid.md)                     | Returns the character's identifier.                                            |
| [**GetOriginalSize**](iagentcharacterex--getoriginalsize.md)     | Returns the original size of the character frame.                              |
| [**Think**](iagentcharacterex--think.md)                         | Displays the specified text in the character's "thought" balloon.              |
| [**GetVersion**](iagentcharacterex--getversion.md)               | Returns the version of the character.                                          |
| [**GetAnimationNames**](iagentcharacterex--getanimationnames.md) | Returns the names of the animations for the character.                         |
| [**getSRStatus**](iagentcharacterex--getsrstatus.md)             | Returns the conditions necessary to support speech input.                      |



 

 

 




