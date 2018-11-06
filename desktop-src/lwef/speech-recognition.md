---
title: Speech Recognition
description: Speech Recognition
ms.assetid: cb5ac509-12a4-4ca4-8776-424568cf780d
ms.topic: article
ms.date: 05/31/2018
---

# Speech Recognition

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

Speech recognition provides a very natural and familiar interface for interacting with characters. However, speech input also presents many challenges. Speech engines currently operate without substantial parts of the human speech communication repertoire, such as gestures, intonation, and facial expressions. Further, natural speech is typically unbounded. It is easy for the speaker to exceed the current vocabulary, or *grammar*, of the engine. Similarly, wording or word order can vary for any given request or response. In addition, speech recognition engines must often deal with large variations in the speaker's environment. For example, background noise, microphone quality, and location can affect input quality. Similarly, different speaker pronunciations or even same-speaker variations, such as when the speaker has a cold, make it a challenge to convert the acoustic data into representational understanding. Finally, speech engines must also deal with similar sounding words or phrases in a language, such as "new," "knew," and "gnu," or "wreck a nice beach" and "recognize speech."

Speech isn't always the best form of input for a task. Because of the turn-taking nature of speech, it can often be slower than other forms of input. Like the keyboard, speech input is a poor interface for pointing unless some type of mnemonic representation is provided. Therefore, always consider whether speech is the most appropriate input for a task. It is best to avoid using speech as the exclusive interface to any task. Provide other ways to access any basic functionality using methods such as the mouse or keyboard. In addition, take advantage of the multi-modal nature of using speech in the visual interface by combining speech input with visual information that helps specify the context and options.

Finally, the successful use of speech input is due only in part to the quality of the technology. Even human recognition, which exceeds any current recognition technology, sometimes fails. However, in human communication we use strategies that improve the probability of success and that provide error recovery when something goes wrong. Therefore, the effectiveness of speech input also depends on the quality of the user interface that presents it.

Studying human models of speech interaction can be useful when designing more natural speech interfaces. Recording actual human speech dialogues for particular scenarios may help you better understand the constructs and patterns used as well as effective forms of feedback and error recovery. It can help determine the appropriate vocabulary to use (for input and output). It is better to design a speech interface based on how people actually speak than to simply derive it from the graphical interface in which it operates.

Note that Microsoft Agent uses the Microsoft Speech API (SAPI) to support speech recognition. This enables Microsoft Agent to be used with a variety of compatible engines. Although Microsoft Agent specifies certain basic interfaces, the performance requirements and quality of an engine may vary.

Speech is not the only means of supporting conversational interfaces. You can also use natural-language processing of keyboard input in place of or in addition to speech. In those situations, you can still generally apply guidelines for speech input.

-   [Listen, Don't Just Recognize](listen--dont-just-recognize.md)
-   [Clarify and Limit Choices](clarify-and-limit-choices.md)
-   [Provide Good Error Recovery](provide-good-error-recovery.md)

 

 




