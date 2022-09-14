---
title: ITTSNotifySinkW
description: ITTSNotifySinkW
ms.assetid: 6305dad6-c162-458a-899e-628f6486680e
ms.topic: article
ms.date: 05/31/2018
---

# ITTSNotifySinkW

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

The engine must call out through [**AudioStop**](https://www.bing.com/search?q=**AudioStop**), [**AudioStart**](https://www.bing.com/search?q=**AudioStart**), and [**Visual**](https://www.bing.com/search?q=**Visual**). The **Visual** callback must provide IPA phonemes. (The International Phonetic Alphabet \[IPA\] is a universal notation for describing the phonetic content of spoken communication. All speakable phonemes have representations in IPA. Details of IPA are in the Microsoft Speech API specification \[part of the Speech SDK 4.0 download\] at [https://www.microsoft.com/speech/](https://msdn.microsoft.com/library/ee705648.aspx).)

Although the [**Visual**](https://www.bing.com/search?q=**Visual**) notification is fairly rich, Microsoft Agent uses only the **cIPAPhoneme** value to animate the mouth as the character speaks. Any Microsoft Agent-compatible engine must provide a closely synchronized stream of **Visual** notifications reflecting the phonetic content of the produced utterance. In this case, "relatively timely notification" is not adequate, because speaker-hearers are fairly sensitive to discrepancies between mouth position and acoustic content. **Visual** notifications need to be returned promptly.

 

 




