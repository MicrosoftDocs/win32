---
title: Use Natural Variation
description: Use Natural Variation
ms.assetid: 5d5750e4-cf30-43dc-9419-7e6bbdb9aa5a
ms.topic: article
ms.date: 05/31/2018
---

# Use Natural Variation

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

While consistency of presentation in your application's conventional interface, such as menus and dialog boxes, makes the interface more predictable, vary the animation and spoken output in the character's interface. Appropriately varying the character's responses provides a more natural interface. If a character always addresses the user exactly the same way; for example, always saying the same words, the user is likely to consider the character boring, disinterested, or even rude. Human communication rarely involves precise repetition. Even when repeating something in a similar situation, we may change wording, gestures, or facial expression.

Microsoft Agent enables you to build in some variation for a character. When defining a character's animations, you can use branching probabilities on any animation frame to change an animation when it plays. You can also assign multiple animations to each state. Microsoft Agent randomly chooses one of the assigned animations each time it initiates a state. For speech output, you can also include vertical bar characters in your output text to automatically vary the text spoken. For example, Microsoft Agent will randomly select one of the following statements when processing this text as part of the [**Speak**](speak-method.md) method:

"I can say this.\|I can say that.\|I can say something else."

 

 




