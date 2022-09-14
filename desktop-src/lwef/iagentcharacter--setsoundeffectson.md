---
title: IAgentCharacter SetSoundEffectsOn
description: IAgentCharacter SetSoundEffectsOn
ms.assetid: 141dd9a8-5fd8-42c6-880a-856c61cb8940
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacter::SetSoundEffectsOn

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetSoundEffectsOn(
   long bOn  // character sound effects setting 
);
```

Determines whether the character's sound effects are played.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="bOn"></span><span id="bon"></span><span id="BON"></span>*bOn*
</dt> <dd>

Sound effects setting. If this parameter is **True**, the sound effects for animations are played when the animation plays; if **False**, sound effects are not played.

</dd> </dl>

This setting determines whether sound effects compiled as a part of the character are played when you play an associated animation. This property's setting applies to all clients of the character. The setting is also subject to the user's global sound effects setting in [**IAgentAudioOutputProperties::GetUsingSoundEffects**](iagentaudiooutputproperties--getusingsoundeffects.md).

## See Also

[**IAgentCharacter::GetSoundEffectsOn**](iagentcharacter--getsoundeffectson.md), [**IAgentAudioOutputProperties::GetUsingSoundEffects**](iagentaudiooutputproperties--getusingsoundeffects.md)


 

 




