---
title: IAgentCommandsEx
description: IAgentCommandsEx
ms.assetid: 6c354677-4cdb-4a74-9c41-2d0bf6f8dd55
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommandsEx

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

[**IAgentCommandsEx**](iagentcommandex.md) defines an interface that extends the [**IAgentCommands**](iagentcommands.md) interface.

**Methods in Vtable Order**



| IAgentCommandsEx Methods                                                             | Description                                                                                                   |
|--------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [SetDefaultID](iagentcommandsex--setdefaultid.md)                                   | Sets the default command for the character's pop-up menu.                                                     |
| [GetDefaultID](iagentcommandsex--getdefaultid.md)                                   | Returns the default command for the character's pop-up menu.                                                  |
| [**SetHelpContextID**](iagentcommandex--sethelpcontextid.md)                        | Sets the context-sensitive help topic ID for a [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441) object.                     |
| [**GetHelpContextID**](iagentcommandex--gethelpcontextid.md)                        | Returns the context-sensitive help topic ID for a [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441) object.                  |
| [SetFontName](iagentcommandsex--setfontname.md)                                     | Sets the font to use in the character's pop-up menu.                                                          |
| [GetFontName](iagentcommandsex--getfontname.md)                                     | Returns the font used in the character's pop-up menu.                                                         |
| [SetFontSize](iagentcommandsex--setfontsize.md)                                     | Sets the font size to use in the character's pop-up menu.                                                     |
| [GetFontSize](iagentcommandsex--getfontsize.md)                                     | Returns the font size used in the character's pop-up menu.                                                    |
| [**SetVoiceCaption**](iagentcommandex--setvoicecaption.md)                          | Sets the voice caption for the character's [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441) object.                         |
| [**GetVoiceCaption**](iagentcommandex--getvoicecaption.md)                          | Returns the voice caption for the character's [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441) object.                      |
| [AddEx](iagentcommandsex--addex.md)                                                 | Adds a [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441) object to a [**Commands**](https://msdn.microsoft.com/library/windows/desktop/ms695971) collection.    |
| [InsertEx](iagentcommandsex--insertex.md)                                           | Inserts a [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441) object in a [**Commands**](https://msdn.microsoft.com/library/windows/desktop/ms695971) collection. |
| [SetGlobalVoiceCommandsEnabled](iagentcommandsex--setglobalvoicecommandsenabled.md) | Enables the voice grammar for Agent's global commands.                                                        |
| [GetGlobalVoiceCommandsEnabled](iagentcommandsex--getglobalvoicecommandsenabled.md) | Returns whether the voice grammar for Agent's global commands is enabled.                                     |



 

 

 




