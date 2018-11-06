---
title: IAgentCharacter GetSoundEffectsOn
description: IAgentCharacter GetSoundEffectsOn
ms.assetid: 11bc074e-7654-4a78-920e-acd56db52c98
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacter::GetSoundEffectsOn

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetSoundEffectsOn(
   long * pbOn  // address of variable for sound effects setting 
);
```

Retrieves whether the character's sound effects setting is enabled.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pbOn"></span><span id="pbon"></span><span id="PBON"></span>*pbOn*
</dt> <dd>

Address of a variable that receives **True** if the character's sound effects setting is enabled, **False** if disabled.

</dd> </dl>

The character's sound effects setting determines whether sound effects compiled as a part of the character are played when you play an associated animation. The setting is subject to the user's global sound effects setting in [**IAgentAudioOutputProperties::GetUsingSoundEffects**](iagentaudiooutputproperties--getusingsoundeffects.md).

## See Also

[**IAgentCharacter::SetSoundEffectsOn**](iagentcharacter--setsoundeffectson.md), [**IAgentAudioOutputProperties::GetUsingSoundEffects**](iagentaudiooutputproperties--getusingsoundeffects.md)


 

 




