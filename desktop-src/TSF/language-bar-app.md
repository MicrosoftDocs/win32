---
title: Language Bar (TSF Applications)
description: An application cannot add items to the language bar; only a text service can add items to the language bar.
ms.assetid: facb0da1-3f80-4745-b021-c026e7e5356c
keywords:
- Text Services Framework (TSF),language bar
- TSF (Text Services Framework),language bar
- TSF-enabled applications,language bar
- language bar
ms.topic: article
ms.date: 05/31/2018
---

# Language Bar (TSF Applications)

An application cannot add items to the language bar; only a text service can add items to the language bar. An application can affect how certain items on the language bar appear.

The [GUID\_COMPARTMENT\_SPEECH\_DICTATIONSTAT](predefined-compartments.md) compartment is used to indicate the type of speech input that the application can accept: direct text input (dictation) and/or voice commands. By default, dictation is enabled and voice command is disabled. If the application can accept voice commands, it should set the [TF\_COMMANDING\_ENABLED](speech-recognition-constants.md) value in the GUID\_COMPARTMENT\_SPEECH\_DICTATIONSTAT compartment. If the application can accept dictation, it should set the TF\_DICTATION\_ENABLED value in the GUID\_COMPARTMENT\_SPEECH\_DICTATIONSTAT compartment. The TF\_DICTATION\_ON or TF\_COMMANDING\_ON value of this compartment determines which mode (dictation or command) speech input is currently in.

If the application supports persistent storage of property data, it should set the [GUID\_COMPARTMENT\_PERSISTMENUENABLED](predefined-compartments.md) compartment to a nonzero value. This causes the speech text service to enable the **Save Speech Data** menu item.

## Related topics

<dl> <dt>

[How To Set Up Text Services Framework](how-to-set-up-tsf.md)
</dt> <dt>

[Language Bar (Text Services)](language-bar.md)
</dt> </dl>

 

 




