---
title: The Commands Collection Object
description: The Commands Collection Object
ms.assetid: 8726ce04-77d3-4ae3-bd46-e75f42b36d6f
ms.topic: article
ms.date: 05/31/2018
---

# The Commands Collection Object

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

The Microsoft Agent server maintains a list of commands that are currently available to the user. This list includes commands that the server defines for general interaction (such as Hide and Open The Voice Commands Window), the list of available (but non-input-active) clients, and the commands defined by the current active client. The first two sets of commands are global commands; that is, they are available at any time, regardless of the input-active client. Client-defined commands are available only when that client is input-active and the character is visible.

Each client application can define a collection of commands called the [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection. To add a command to the collection, use the [**Add**](add-method.md) or [**Insert**](insert-method.md) method. Although you can specify a command's properties with separate statements, for optimum code performance, specify all of a command's properties in the **Add** or **Insert** method statement. For each command in the collection, you can determine whether user access to the command appears in the character's pop-up menu, in the Voice Commands Window, in both, or in neither. For example, if you want a command to appear on the pop-up menu for the character, set the command's [**Caption**](caption-property.md) and [**Visible**](visible-property.md) properties. To display the command in the Voice Commands Window, set the command's [**VoiceCaption**](voicecaption-property.md) and [**Voice**](voice-property.md) properties.

A user can access the individual comm[**Commands**](/windows/desktop/lwef/the-commands-collection-object)ands in your collection only when your client application is input-active. Therefore, when you may be sharing the character with other client applications you'll typically want to set the [**Caption**](caption-property.md), [**VoiceCaption**](voicecaption-property.md), and [**Voice**](voice-property.md) properties for the **Commands** collection object as well as for the commands in the collection. This places an entry for your **Commands** collection in a character's pop-up menu and in the Voice Commands Window.

When the user switches to your client by choosing its [**Commands**](/windows/desktop/lwef/the-commands-collection-object) entry, the server automatically makes your client input-active, notifying your client application using the [**ActivateInput**](activateinput-event.md) event and makes the commands in its collection available. The server also notifies the client that it is no longer input-active with the [**DeActivateInput**](deactivateinput-event.md) event. This enables the server to present and accept only the commands that apply to the current input-active client's context. It also serves to avoid command-name collisions between clients.

A client can also explicitly request to make itself the input-active client using the [**Activate**](activate-method.md) method. This method also supports setting your application to not be the input-active client. You may want to use this method when you are sharing a character with another application, setting your application to be input-active when your application window gets focus and not input-active when it loses focus.

Similarly, you can use the [**Activate**](activate-method.md) method to set your application to be (or not be) the active client of the character. The active client is the client that receives input when its character is the topmost character. When this status changes, the server notifies your application with the [**ActiveClientChange**](activeclientchange-event.md) event.

When a character's pop-up menu displays, changes to the properties of a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection or the commands in its collection do not appear until the user redisplays the menu. However, the Commands Window does display changes as they happen.

-   [Commands Object Methods](commands-object-methods.md)
-   [Commands Object Properties](commands-object-properties.md)

 

 