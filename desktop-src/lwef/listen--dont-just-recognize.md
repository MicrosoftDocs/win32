---
title: Listen, Dont Just Recognize
description: Listen, Dont Just Recognize
ms.assetid: 74bb2122-98c1-4a51-b894-93e1481aa46b
ms.topic: article
ms.date: 05/31/2018
---

# Listen, Dont Just Recognize

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

Successful communication involves more than recognition of words. The process of dialogue implies exchanging cues to signal turn-taking and understanding. Characters can improve conversational interfaces by providing cues like head tilts, nods, or shakes to indicate when the speech engine is in the listening state and when something is recognized. For example, Microsoft Agent plays animations assigned to the **Listening** state when a user presses the push-to-talk listening key and animations assigned to the **Hearing** state when an utterance is detected. When defining your own character, make sure you create and assign appropriate animations to these states. For more information on designing characters, see [Designing Characters for Microsoft Agent](designing-characters-for-microsoft-agent.md).

In addition to non-verbal cues, a conversation involves a common context between the conversing parties. Similarly, speech input scenarios with characters are more likely to succeed when the context is well established. Establishing the context enables you to better interpret similar-sounding phrases like "check's in the mail" and "check my mail." You may also want to enable the user to query the context by providing a command, such as "Help" or "Where am I," to which you respond by restating the current context, such as the last action your application performed.

Microsoft Agent provides interfaces that enable you access the best match and the two next best alternatives returned by the speech recognition engine. In addition, you can access confidence scores for all matches. You can use this information to better determine what was spoken. For example, if the confidence scores of the best match and first alternative are close, it may indicate that the speech engine had difficulty discerning the difference between them. In such a case, you may want to ask the user to repeat or rephrase the request in an effort to improve performance. However, if the best match and first or second alternatives return the same command, it strengthens the indication of the correct recognition.

The nature of a conversation or dialogue implies that there should be a response to spoken input. Therefore, a user's input should always be responded to with verbal or visual feedback that indicates an action was performed or a problem was encountered, or provides an appropriate reply.

 

 




