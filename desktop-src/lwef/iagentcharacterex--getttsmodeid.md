---
title: IAgentCharacterEx GetTTSModeID
description: IAgentCharacterEx GetTTSModeID
ms.assetid: e7b3c576-dc3c-40de-8d09-8e7f4b79250b
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacterEx::GetTTSModeID

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetTTSModeID(
   BSTR * pbszModeID  // address of TTS engine ID
);
```

Retrieves the mode ID of the TTS engine set for the character.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pbszModeID"></span><span id="pbszmodeid"></span><span id="PBSZMODEID"></span>*pbszModeID*
</dt> <dd>

Address of a BSTR that receives the mode ID setting of the TTS engine for the character.

</dd> </dl>

This setting returns the TTS (text-to-speech) engine mode ID for a character's spoken output. The mode ID for a TTS engine is a string representation of the GUID (formatted with braces and dashes) defined by the speech vendor uniquely identifying the engine. For more information, see the [Microsoft Speech SDK documentation](https://msdn.microsoft.com/library/ee705648.aspx). Querying this property will load the associated engine if it is not already loaded.

If you do not set a TTS engine mode ID for the character, the server attempts to return an engine that matches (using Microsoft Speech API interfaces) the character's compiled TTS setting and the character's current language setting. If these are different, then the character's language setting overrides its authored mode setting. If you have not set the character's language setting, the character's language is the user default language ID, and the server attempts the match based on that language ID.

This function does not fail if the [**IAgentAudioObjectProperties::GetEnabled**](https://www.bing.com/search?q=**IAgentAudioObjectProperties::GetEnabled**) returns **False**.

This property applies only to your client application's use of the character; the setting does not affect other clients of the character or other characters of your client application.

Microsoft Agent's speech engine requirements are based on the Microsoft Speech API. Engines supporting Microsoft Agent's SAPI requirements can be installed and used with Agent.

## See Also

[**IAgentCharacterEx::SetTTSModeID**](iagentcharacterex--setttsmodeid.md)


 

 




