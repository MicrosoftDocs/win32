---
title: Synthesized Speech Support
description: Synthesized Speech Support
ms.assetid: 38172e04-a5b6-41e4-9d7c-539d9d4117be
ms.topic: article
ms.date: 05/31/2018
---

# Synthesized Speech Support

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

If you use synthesized speech, your character has the ability to say almost anything, which provides the greatest flexibility. With recorded audio, you can give the character a specific or unique voice. To specify output, provide the spoken text as a parameter of the [**Speak**](speak-method.md) method.

Because Microsoft Agent's architecture uses Microsoft SAPI for synthesized speech output, you can use any engine that conforms to this specification, and supports International Phonetic Alphabet (IPA) output using the [**Visual**](https://www.bing.com/search?q=**Visual**) method of the [**ITTSNotifySinkW**](ittsnotifysinkw.md) interface. For further information on the engine requires, see [Speech Engine Support Requirements](requirements-for-text-to-speech-engines.md).

A character's language ID setting determines its TTS output. If a client does not specify a language ID for the character, the character's language ID is set to the user default language ID. If the character's definition includes a specific engine and that engine can be loaded and it matches the character's language setting, that engine will be used. Otherwise, Microsoft Agent enumerates the other available engines and requests a SAPI best match based on language, gender, and age (in that order). If there is no matching engine available, there is no TTS output for that client's use of the character. Agent attempts to load the TTS engine on the first [**Speak**](speak-method.md) call or when you query or successfully set its mode ID.

A client application can also specify a TTS engine for its character (using the [**TTSModeID**](ttsmodeid-property.md) property). This overrides the server's attempt to automatically find a matching engine based on the character's preferred TTS mode ID or the character's current language ID setting. However, if that engine is not installed (or cannot otherwise be loaded), the call will fail (and raise an error in the control). The server then attempts to load another engine based on the language ID, compiled character TTS setting, and available TTS engines. If there is still no match, TTS is not available for that client, but the character can still speak into its word balloon.

Only the TTS engines in use by any client remain loaded. For example, if a character has a defined preference for a specific engine and that engine is available, but your client application has specified a different engine (by setting a character's language ID differently from the engine or specifying a different mode ID), only the engine specified by your application remains loaded. The engine matching the character's defined preference for a TTS setting is unloaded (unless another client is using the character's compiled engine setting).

 

 




