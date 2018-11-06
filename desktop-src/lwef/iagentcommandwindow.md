---
title: IAgentCommandWindow
description: IAgentCommandWindow
ms.assetid: 315b24b4-110e-4373-a1ee-0317531e6008
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommandWindow

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

**IAgentCommandWindow** defines an interface that allows applications to set and query the properties of the Voice Commands Window. The Voice Commands Window is a shared resource primarily designed to enable users to view voice-enabled commands. If speech recognition is disabled, the Voice Commands Window still displays, with the text "Speech input disabled" (in the language of the character). If no speech engine is installed that matches the character's language setting, the window displays, "Speech input not available." If the input-active client has not defined voice parameters for its commands and has disabled global voice commands, the window displays, "No voice commands." You can also query the properties of the Voice Commands Window regardless of whether speech input is disabled or a compatible speech engine is installed.

**Methods in Vtable Order**



| IAgentCommandWindow Methods                             | Description                                                                                         |
|---------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [**SetVisible**](iagentcommandwindow--setvisible.md)   | Sets the value of the [**Visible**](visible-property.md) property of the Voice Commands Window.    |
| [**GetVisible**](iagentcommandwindow--getvisible.md)   | Returns the value of the [**Visible**](visible-property.md) property of the Voice Commands Window. |
| [**GetPosition**](iagentcommandwindow--getposition.md) | Returns the position of the Voice Commands Window.                                                  |
| [**GetSize**](iagentcommandwindow--getsize.md)         | Returns the size of the Voice Commands Window.                                                      |



 

 

 




