---
title: Create Training Card Help
description: Create Training Card Help
ms.assetid: 21CAFF93-4288-48ff-BE52-921CC0EC8AB3
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Create Training Card Help

You can [create training cards](creating-a-training-card.md), which are specialized help topics, to send instructions to, and receive instructions from, a program. They are particularly useful in guiding users through a procedure step-by-step. Whenever the user completes a step, the next step can automatically appear. If a user incorrectly performs a step, information can appear that specifically addresses their mistakes. Training card topics appear in a secondary window.

Help authors insert the HTML Help ActiveX control into training card topics to send information to programs. You work with a developer using the [HTML Help API](about-the-html-help-api-reference.md) to make the appropriate API calls.

Training card help is initiated either from a user selection in a help topic or by actions a user takes in a program. These are the actions that take place when a training card is used:

-   The training card help sends messages directly to a software program.
-   The user interacts with HTML Help by answering a question, and then HTML Help sends messages to the program based on the response. The program must process the WM\_TCARD message to receive messages from HTML Help. The help author adds the ActiveX control to the help file to initiate these messages.

## Related topics

<dl> <dt>

[About Hooking Up Help to a Program](hook-up-help-to-a-program.md)
</dt> </dl>

 

 




