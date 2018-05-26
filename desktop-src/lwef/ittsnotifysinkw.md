---
title: ITTSNotifySinkW
description: ITTSNotifySinkW
ms.assetid: 6305dad6-c162-458a-899e-628f6486680e
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ITTSNotifySinkW

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

The engine must call out through [**AudioStop**](lwef-audiostop_function), [**AudioStart**](lwef-audiostart_function), and [**Visual**](lwef-visual_function). The **Visual** callback must provide IPA phonemes. (The International Phonetic Alphabet \[IPA\] is a universal notation for describing the phonetic content of spoken communication. All speakable phonemes have representations in IPA. Details of IPA are in the Microsoft Speech API specification \[part of the Speech SDK 4.0 download\] at [http://www.microsoft.com/speech/](http://go.microsoft.com/fwlink/p/?linkid=198367).)

Although the [**Visual**](lwef-visual_function) notification is fairly rich, Microsoft Agent uses only the **cIPAPhoneme** value to animate the mouth as the character speaks. Any Microsoft Agent-compatible engine must provide a closely synchronized stream of **Visual** notifications reflecting the phonetic content of the produced utterance. In this case, "relatively timely notification" is not adequate, because speaker-hearers are fairly sensitive to discrepancies between mouth position and acoustic content. **Visual** notifications need to be returned promptly.

 

 




