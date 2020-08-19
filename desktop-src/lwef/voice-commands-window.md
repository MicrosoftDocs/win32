---
title: Voice Commands Window
description: Voice Commands Window
ms.assetid: 'vs|msagent|~\guidlin_12gn.htm'
ms.topic: article
ms.date: 05/31/2018
---

# Voice Commands Window

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

The Voice Commands Window displays the current active voice commands available for the character. The window appears when the Open Commands Window command is chosen or the [**Visible**](visible-property.md) property of the [**CommandsWindow**](/windows/desktop/lwef/the-commandswindow-object) object is set to **True**. If the speech engine has not yet been loaded, querying or setting this property will cause Microsoft Agent to attempt to initialize the engine. If the user disables speech, the window can still display; however, it will include a text message that informs the user that speech is currently disabled.

The input-active client's commands appear in the Voice Commands Window based on the [**Voice**](voice-property.md)[**Caption**](caption-property.md) and **Voice** property settings listed under the [**VoiceCaption**](voicecaption-property.md) of their [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection.

**Figure 1. Voice Commands Window**

The Voice Commands Window appears when the Open Commands Window command is chosen. The input-active client's commands appear in the Voice Commands Window based on the [**Voice**](voice-property.md)[**Caption**](caption-property.md) and **Voice** property settings listed under **Voice** of the [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection.

The Voice Commands Window also lists the [**VoiceCaption**](voicecaption-property.md) of the [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection for other clients of the character, and the following server-generated voice commands for general interaction under the Global Commands entry:



| Voice Caption                       | Voice Grammar                                                                                                                                            |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Open \| Close Voice Commands Window | (open \| show) \[the\] commands \[window\] \| what can I say \[now\] <br/> toggles with: <br/> close \[the\] commands \[window\] <br/> |
| Hide                                | hide \*                                                                                                                                                  |
| *CharacterName*                     | *CharacterName*\*\*                                                                                                                                      |
| Global Commands                     | \[show\] \[me\] global commands                                                                                                                          |



 

\* A character is listed here only if it is currently visible.

\*\* All loaded characters are listed.

Speaking the voice command for another client's [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection switches to that client, and the Voice Commands Window displays the commands of that client. No other entries are expanded. Similarly, if the user switches characters, the Voice Commands Window changes to display the commands of its input-active client. If the client is already input-active, speaking one of its voice commands has no effect. (However, if the user collapses the active client's subtree with the mouse, speaking the client name redisplays the client's subtree.)

If a client has voice commands, but no [**Voice**](voice-property.md) setting for its [**Commands**](/windows/desktop/lwef/the-commands-collection-object) object (or no **Voice**[**Caption**](caption-property.md)), the tree displays "(command undefined)" as the parent entry -- but only when that client is input-active and the client has commands in its collection that have **Caption** and **Voice** settings.

The server automatically displays the commands of the current input-active client and, if necessary, scrolls the window to display as many of the client's commands as possible, based on the size of the window. If the character has no client entries, the Global Commands entry is expanded.

If the user speaks "Global Commands," the Voice Commands Window always displays its associated subtree entries. If they are already displayed, the command has no effect.

Although you can also display or hide the Voice Commands Window from your application's code using the [**Visible**](visible-property.md) property, you cannot change the Voice Commands Window size or location. The server maintains the Voice Commands Window's properties based on the user's interaction with the window. Its initial location is immediately adjacent to the character's taskbar icon.

The Voice Commands Window is included in the ALT+TAB window order. This enables a user to switch to the window to scroll, resize, or reposition the window with the keyboard.

-   [The Listening Tip](the-listening-tip.md)
-   [The Advanced Character Options Window](https://www.bing.com/search?q=The+Advanced+Character+Options+Window)

 

