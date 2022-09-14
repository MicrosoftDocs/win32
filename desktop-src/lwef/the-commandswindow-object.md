---
title: The CommandsWindow Object
description: The CommandsWindow Object
ms.assetid: f7f37499-f16b-47fb-85d1-23a68171bf0b
ms.topic: article
ms.date: 05/31/2018
---

# The CommandsWindow Object

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

The [**CommandsWindow**](/windows/desktop/lwef/the-commandswindow-object) object provides access to properties of the Voice Commands Window. The Voice Commands Window is a shared resource primarily designed to enable users to view voice-enabled commands. If speech recognition is disabled, the Voice Commands Window still displays, with the text "Speech input disabled" (in the language of the character). If no speech engine is installed that matches the character's language setting the window displays, "Speech input not available." If the input-active client has not defined voice parameters for its commands and has disabled global voice commands, the window displays, "No voice commands." You can also query the properties of the Voice Commands Window regardless of whether speech input is disabled or a compatible speech engine is installed.

-   [CommandsWindow Properties](commandswindow-properties.md)

 

 