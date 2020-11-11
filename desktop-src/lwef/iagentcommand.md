---
title: IAgentCommand
description: IAgentCommand
ms.assetid: 70873093-df71-4377-9c39-c7528400052f
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommand

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

A [**Command**](/windows/desktop/lwef/the-command-object) object is an item in a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection. The server provides the user access to your commands your client application becomes input active. To retrieve a **Command**, call [**IAgentCommands::GetCommand**](iagentcommands--getcommand.md).

**IAgentCommand** defines an interface that allows applications to set and query properties for [**Command**](/windows/desktop/lwef/the-command-object) objects that can appear in a character's pop-up menu and in the Voice Commands Window. These functions are also available from [**IAgentCommandEx**](iagentcommandex.md). A **Command** object is an item in a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection. The server provides the user access to your commands when your client application becomes input active.

A [**Command**](/windows/desktop/lwef/the-command-object) may appear in either or both the character's pop-up menu and the Voice Commands Window. To appear in the pop-up menu, it must have a [**Caption**](caption-property.md) and have the [**Visible**](visible-property.md) property set to **True**. The **Visible** property for its [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection object must also be set to **True** for the command to appear in the pop-up menu when your client application is input-active. To appear in the Voice Commands Window, a **Command** must have its [**VoiceCaption**](voicecaption-property.md) and [**Voice**](voice-property.md) properties set. (For backward compatibility, if there is no **VoiceCaption**, the **Caption** setting is used.)

A character's pop-up menu entries do not change while the menu is displayed. If you add or remove Commands or change their properties while the character's popup menu is displayed, the menu displays those changes when redisplayed. However, the Voice Commands Window does display changes as you make them.

The following table summarizes how the properties of a command affect its presentation.



| Caption Property | Voice-Caption Property | Voice Property | Visible Property | Appears in Character's Pop-up Menu             | Appears in Voice Commands Window                         |
|------------------|------------------------|----------------|------------------|------------------------------------------------|----------------------------------------------------------|
| Yes              | Yes                    | Yes            | True             | Yes, using [**Caption**](caption-property.md) | Yes, using [**VoiceCaption**](voicecaption-property.md) |
| Yes              | Yes                    | No¹            | True             | Yes, using [**Caption**](caption-property.md) | No                                                       |
| Yes              | Yes                    | Yes            | False            | No                                             | Yes, using [**VoiceCaption**](voicecaption-property.md) |
| Yes              | Yes                    | No¹            | False            | No                                             | No                                                       |
| No¹              | Yes                    | Yes            | True             | No                                             | Yes, using [**VoiceCaption**](voicecaption-property.md) |
| No¹              | Yes                    | Yes            | False            | No                                             | Yes, using [**VoiceCaption**](voicecaption-property.md) |
| No¹              | Yes                    | No¹            | True             | No                                             | No                                                       |
| No¹              | Yes                    | No¹            | False            | No                                             | No                                                       |
| Yes              | No¹                    | Yes            | True             | Yes, using [**Caption**](caption-property.md) | Yes, using [**Caption**](caption-property.md)           |
| Yes              | No¹                    | No¹            | True             | Yes                                            | No                                                       |
| Yes              | No¹                    | Yes            | False            | No                                             | Yes, using [**Caption**](caption-property.md)           |
| Yes              | No¹                    | No¹            | False            | No                                             | No                                                       |
| No¹              | No¹                    | Yes            | True             | No                                             | No²                                                      |
| No¹              | No¹                    | Yes            | False            | No                                             | No²                                                      |
| No¹              | No¹                    | No¹            | True             | No                                             | No                                                       |
| No¹              | No¹                    | No¹            | False            | No                                             | No                                                       |



 

¹If the property setting is null. In some programming languages, an empty string may not be interpreted as the same as a null string.

²The command is still voice-accessible.

Generally, if you define a [**Command**](/windows/desktop/lwef/the-command-object) with a [**Voice**](voice-property.md) setting, you also define [**Caption**](caption-property.md) and **Voice** settings for its associated [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection. If the **Commands** collection for a set of commands has no **Voice** or no **Caption** setting and is currently input-active, but the **Commands** have **Caption** and **Voice** settings, the **Commands** appear in the Voice Commands Window tree view under "(undefined command)" when your client application becomes input-active.

When the server receives input that matches one of the [**Command**](/windows/desktop/lwef/the-command-object) objects you defined for your [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection, it sends a [**IAgentNotifySink::Command**](https://www.bing.com/search?q=**IAgentNotifySink::Command**) event, and passes back the ID of the command as an attribute of the [**IAgentUserInput**](https://www.bing.com/search?q=**IAgentUserInput**) object. You can then use conditional statements to match and process the command.

**Methods in Vtable Order**



| IAgentCommand Methods                                                   | Description                                                                                                                         |
|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| [**SetCaption**](https://www.bing.com/search?q=**SetCaption**)                             | Sets the value for the [**Caption**](caption-property.md) for a [**Command**](/windows/desktop/lwef/the-command-object) object.                         |
| [**GetCaption**](https://www.bing.com/search?q=**GetCaption**)                             | Returns the value of the [**Caption**](caption-property.md) property of a [**Command**](/windows/desktop/lwef/the-command-object) object.               |
| [**SetVoice**](iagentcommand--setvoice.md)                             | Sets the value for the [**Voice**](voice-property.md) text for a [**Command**](/windows/desktop/lwef/the-command-object) object.                        |
| [**GetVoice**](iagentcommand--getvoice.md)                             | Returns the value of the [**Voice**](voice-property.md) property of a [**Command**](/windows/desktop/lwef/the-command-object) object.                   |
| [**SetEnabled**](iagentcommand--setenabled.md)                         | Sets the value of the [**Enabled**](enabled-property.md) property for a [**Command**](/windows/desktop/lwef/the-command-object) object.                 |
| [**GetEnabled**](iagentcommand--getenabled.md)                         | Returns the value of the [**Enabled**](enabled-property.md) property of a [**Command**](/windows/desktop/lwef/the-command-object) object.               |
| [**SetVisible**](iagentcommand--setvisible.md)                         | Sets the value of the [**Visible**](visible-property.md) property for a [**Command**](/windows/desktop/lwef/the-command-object) object.                 |
| [**GetVisible**](iagentcommand--getvisible.md)                         | Returns the value of the [**Visible**](visible-property.md) property of a [**Command**](/windows/desktop/lwef/the-command-object) object.               |
| [**SetConfidenceThreshold**](iagentcommand--setconfidencethreshold.md) | Sets the value of the [**Confidence**](confidence-property.md) property for a [**Command**](/windows/desktop/lwef/the-command-object) object.           |
| [**GetConfidenceThreshold**](iagentcommand--getconfidencethreshold.md) | Returns the value of the [**Confidence**](confidence-property.md) property of a [**Command**](/windows/desktop/lwef/the-command-object) object.         |
| [**SetConfidenceText**](iagentcommand--setconfidencetext.md)           | Sets the value of the [**ConfidenceText**](confidencetext-property.md) property for a [**Command**](/windows/desktop/lwef/the-command-object) object.   |
| [**getConfidenceText**](iagentcommand--getconfidencetext.md)           | Returns the value of the [**ConfidenceText**](confidencetext-property.md) property of a [**Command**](/windows/desktop/lwef/the-command-object) object. |
| [**getID**](iagentcommand--getid.md)                                   | Returns the ID of a [**Command**](/windows/desktop/lwef/the-command-object) object.                                                                      |



 

 

 