---
title: Characters
description: Characters
ms.assetid: d3eac94b-7899-4695-b0e5-0276c1f5e9cb
ms.topic: article
ms.date: 05/31/2018
---

# Characters

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

Human communication is fundamentally social. Microsoft Agent enables you to leverage this aspect of interaction using animated characters. Users will expect a character to conform to the same social, though not necessarily physical, rules they use when interacting with other people, even when they understand that the character is synthetic. To the extent that you create characters that meet their expectations, users will find your characters more believable and likable. Therefore, how you design a character can have a dramatic effect on its success.

When designing a character, first consider the profile of your target audience and what appeals to them as well as what tasks they do. Similarly, consider how well your character's design and style matches its purpose in addition to the application it supports. For example, a dog character may work well for a retrieval or security application depending on its overall appearance. Often the success is in the details. Research has shown that changing an animal character's roundness of eyes and ear shape can generate very different reactions to the character.

Also consider your character's basic personality type: dominant or submissive, emotional or reserved, sophisticated or down-to-earth; or perhaps you want to adapt its personality based on user interaction. For example, you can provide a control that enables a user to adjust whether the character volunteers more information or waits to be asked. The former would be more outgoing than the latter.

The name you supply for your character can infer a particular type of personality. For example, "Max" and "Linus" may convey very different personalities. The Microsoft Agent Character Editor enables you to set your character's name and include a short description. These attributes can be queried at run time.

In addition, decide whether you plan to use a synthetic voice (using a text-to-speech engine) or recorded voice (.WAV file). This decision may depend on the type of character you use, the languages you plan to support, and what you want the character to be able to say. For example, a synthesized voice enables your character to say almost anything. Programming what your character will say is easy and quick: You just supply the text the character will speak. However, using a computer-generated speech engine requires some extra overhead for initial installation and will be language-specific. Further, most synthesized voices sound computer-generated; they do not match the clarity and prosody of most human speech. It may be difficult to simulate a voice that matches your character, particularly if you use a character that already has an established identity or one that has a very distinctive voice. In such a case, you may want to use recorded speech files for your output. Microsoft Agent also supports lip-syncing for recorded speech output. Although audio files provide a natural voice and are easier to implement in other languages, they must be copied or downloaded to local machines. Recorded speech files also limit your character to the vocabulary contained in them. Whether you choose synthetic or recorded speech output, keep in mind that a voice carries with it additional social information about the gender, age, and personality of the speaker.

You can also decide to use the word balloon for output and the default settings for the balloon's font and color. Note, however, that the user can change the font and color attributes. In addition, you cannot assume that the word balloon's state remains constant because the user can turn the word balloon off.

 

 




