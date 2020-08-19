---
title: IAgentCommands
description: IAgentCommands
ms.assetid: a171a2f0-7c1c-440f-9b19-28447cc68b95
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommands

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

The Microsoft Agent server maintains a list of commands that are currently available to the user. This list includes commands that the server defines for general interaction, such as Hide and Microsoft Agent Properties, the list of available (but non-input-active) clients, and the commands defined by the current active client. The first two sets of commands are global commands; that is, they are available at any time, regardless of the input-active client. Client-defined commands are available only when that client is input-active.

Retrieve an **IAgentCommands** interface by querying the [**IAgentCharacter**](https://www.bing.com/search?q=**IAgentCharacter**) interface for **IAgentCommands**. Each Microsoft Agent client application can define a collection of commands called a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection. To add a [**Command**](/windows/desktop/lwef/the-command-object) to the collection, use the [**Add**](add-method.md) or [**Insert**](insert-method.md) method. Although you can specify a **Command's** properties using [**IAgentCommand**](iagentcommand.md) methods, for optimum code performance, specify all of a **Command**'s properties in the [**IAgentCommands::Add**](iagentcommands--add.md) or [**IAgentCommands::Insert**](iagentcommands--insert.md) methods when initially setting the properties for a new **Command**. You can use the **IAgentCommand** methods to query or change the property settings.

For each [**Command**](/windows/desktop/lwef/the-command-object) in the [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection, you can determine whether the command appears on the character's pop-up menu, in the Voice Commands Window, in both, or in neither. For example, if you want a command to appear on the pop-up menu for the character, set the command's [**Caption**](caption-property.md) and [**Visible**](visible-property.md) properties. To display the command in the **Voice Commands Window**, set the command's **Caption** and [**Voice**](voice-property.md) properties.

A user can access the individual commands in your Commands collection only when your client application is input-active and the character is visible. Therefore, you will typically want to set the [**Caption**](caption-property.md), [**VoiceCaption**](voicecaption-property.md), and [**Voice**](voice-property.md) properties for the [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection object as well as for the commands in the collection, because this places an entry for your **Commands** collection on a character's pop-up menu and in the Voice Commands Window. When the user switches to your client by choosing its **Commands** entry, the server automatically makes your client input-active, notifying your client application using the [**IAgentNotifySink::ActivateInputState**](https://www.bing.com/search?q=**IAgentNotifySink::ActivateInputState**) and makes the **Commands** in its collection available. The server also notifies the client that is no longer input-active with the **IAgentNotifySink::ActivateInputState** event. This enables the server to present and accept only the **Commands** that apply to the current input-active client's context. It also serves to avoid [**Command**](/windows/desktop/lwef/the-command-object)-name collisions between clients.

A client can also explicitly request to make itself the input-active client using the [**IAgentCharacter::Activate**](iagentcharacter--activate.md) method. This method also supports setting your application to not be the input-active client. You may want to use this method when sharing a character with another application, setting your application to be input-active when your application window gets focus and not input-active when it loses focus.

Similarly, you can use [**IAgentCharacter::Activate**](iagentcharacter--activate.md) to set your application to be (or not be) the active client of the character. The active client is the client that receives input when its character is the topmost character. When this status changes, the server notifies your application with the [**IAgentNotifySinkEx::ActiveClientChange**](iagentnotifysinkex--activeclientchange.md) event.

When a character's pop-up menu is displayed, changes to the properties of a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection or the commands in its collection do not appear until the user redisplays the menu. However, when open, the Voice Commands Window does display changes as they happen.

**IAgentCommands** defines an interface that allows applications to add, remove, set, and query properties for a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection. These functions are also available from [**IAgentCommandsEx**](iagentcommandsex.md).

A [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection can appear as a command in both the pop-up menu and the Voice Commands Window for a character. To make the **Commands** collection appear, you must set its [**Caption**](caption-property.md) property. The following table summarizes how the properties of a **Commands** collection affect its presentation.



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



 

¹If the property setting is null. In some programming languages, an empty string may not be interpreted the same as a null string.

²The command is still voice-accessible.

**Methods in Vtable Order**



| IAgentCommands Methods                           | Description                                                                                                                      |
|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [**GetCommand**](iagentcommands--getcommand.md) | Retrieves a [**Command**](/windows/desktop/lwef/the-command-object) object from the [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection.              |
| [**GetCount**](iagentcommands--getcount.md)     | Returns the value of the number of [**Commands**](/windows/desktop/lwef/the-command-object) in a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection. |
| [**SetCaption**](iagentcommands--setcaption.md) | Sets the value of the [**Caption**](caption-property.md) property for a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection.    |
| [**GetCaption**](iagentcommands--getcaption.md) | Returns the value of the [**Caption**](caption-property.md) property of a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection.  |
| [**SetVoice**](iagentcommands--setvoice.md)     | Sets the value of the [**Voice**](voice-property.md) property for a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection.        |
| [**GetVoice**](iagentcommands--getvoice.md)     | Returns the value of the [**Voice**](voice-property.md) property of a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection.      |
| [**SetVisible**](iagentcommands--setvisible.md) | Sets the value of the [**Visible**](visible-property.md) property for a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection.    |
| [**GetVisible**](iagentcommands--getvisible.md) | Returns the value of the [**Visible**](visible-property.md) property of a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection.  |
| [**Add**](iagentcommands--add.md)               | Adds a [**Command**](/windows/desktop/lwef/the-command-object) object to a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection.                       |
| [**Insert**](iagentcommands--insert.md)         | Inserts a [**Command**](/windows/desktop/lwef/the-command-object) object in a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection.                    |
| [**Remove**](iagentcommands--remove.md)         | Removes a [**Command**](/windows/desktop/lwef/the-command-object) object in a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection.                    |
| [**RemoveAll**](iagentcommands--removeall.md)   | Removes all [**Command**](/windows/desktop/lwef/the-command-object) objects from a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection.               |



 

 

 