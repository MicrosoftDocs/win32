---
title: Be Non-Exclusive
description: Be Non-Exclusive
ms.assetid: 7a44840d-6bf9-4c12-ba14-66d7067a984d
ms.topic: article
ms.date: 05/31/2018
---

# Be Non-Exclusive

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

Interactive characters can be employed in the user interface as assistants, guides, entertainers, storytellers, sales agents, or in a variety of other roles. A character that automatically performs or assists should not be designed contrary to the design principle of keeping the user in control. When adding a character to the interface of a website or conventional application, use the character as an enhancement, rather than a replacement of, the primary interface. Avoid implementing any feature or operation that exclusively requires a character.

Similarly, let the user choose when they want to interact with your character. A user should be able to dismiss the character and have it return only with the user's permission. Forcing character interaction on users can have a serious negative effect. To support user control of character interaction, Microsoft Agent automatically includes Hide and Show commands. The Microsoft Agent API also supports these methods, so you can include support for these functions in your own interface. In addition, Microsoft Agent's user interface includes global properties that enable the user to override certain character output options. To ensure that the user's preferences are maintained, these properties cannot be overridden through the API.

 

 




