---
title: IAgentCharacterEx SetTTSModeID
description: IAgentCharacterEx SetTTSModeID
ms.assetid: 66ed792a-1693-45dc-b9a8-eebe772c5af9
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacterEx::SetTTSModeID

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetTTSModeID(
   BSTR bszModeID  // TTS engine ID
);
```

Sets the mode ID of the TTS engine set for the character.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="bszModeID"></span><span id="bszmodeid"></span><span id="BSZMODEID"></span>*bszModeID*
</dt> <dd>

The mode ID setting of the TTS engine for the character.

> [!Note]  
> **IAgentCharacterEx:SetTTSModeID** can fail if Speech.dll is not installed and the engine you specify does not match the character's compiled TTS mode setting.

 

</dd> </dl>

This setting determines the preferred engine mode for a character's spoken TTS output. The mode ID for a TTS (text-to-speech) engine is the GUID defined by the speech vendor that uniquely identifies the mode of the engine (formatted with braces and dashes). For more information, see the [Microsoft Speech SDK documentation](https://msdn.microsoft.com/library/ee705648.aspx).

If you set a TTS mode ID, it overrides the server attempt to match a speech engine based on the character's compiled TTS mode ID, the current system language ID, and the character's current language ID. However, if you attempt to set a mode ID when the user has disabled speech output in the Microsoft Agent property sheet or when the associated engine is not installed, this call will fail.

If you do not set a TTS engine mode ID for the character, the server sets an engine that matches the character's language setting (using Microsoft Speech API interfaces). Setting this property will load the associated engine if it is not already loaded.

This property applies to only your client application's use of the character; the setting does not affect other clients of the character or other characters of your client application.

Microsoft Agent's speech engine requirements are based on the Microsoft Speech API. Engines supporting Microsoft Agent's SAPI requirements can be installed and used with Agent.

## See Also

[**IAgentCharacterEx:GetTTSModeID**](iagentcharacterex--getttsmodeid.md)


 

 




