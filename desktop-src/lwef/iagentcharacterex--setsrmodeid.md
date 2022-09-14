---
title: IAgentCharacterEx SetSRModeID
description: IAgentCharacterEx SetSRModeID
ms.assetid: 8f9072ec-1f64-4f5c-972d-cd6799ce028c
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacterEx::SetSRModeID

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetSRModeID(
   BSTR bszModeID  // speech recognition engine ID
);
```

Sets the mode ID of the speech recognition engine set for the character.

-   Returns S\_OK to indicate the operation was successful.

bszModeID

The mode ID setting of the speech recognition engine for the character.

This setting sets the engine for a character's speech input. The mode ID for a speech recognition engine is the GUID defined by the speech vendor that uniquely identifies the engine's mode (formatted with braces and dashes). For more information, see the [Microsoft Speech SDK documentation](https://msdn.microsoft.com/library/ee705648.aspx).

If you specify a mode ID that does not match the character's language setting, if the user has disabled speech recognition (in the Microsoft Agent property sheet), or the engine is not installed, this call will fail. If you do not set a speech recognition engine mode ID for the character, the server sets one that matches the character's language setting (using Microsoft Speech API interfaces).

When speech input is enabled in the Agent property sheet (Advanced Character Options), setting this property will load the associated engine (if it is not already loaded), and start speech services. That is, the Listening key is available, and the Listening Tip is displayable. (The Listening key and Listening tip are enabled only if they are also enabled in Advanced Character Options.) However, if you query the property when speech is disabled, the server does not start speech services.

This property applies to only the client of the character; the setting does not reflect the setting for other clients of the character or other characters of the client.

Microsoft Agent's speech engine requirements are based on the Microsoft Speech API. Engines supporting Microsoft Agent's SAPI requirements can be installed and used with Agent.

## See Also

[**IAgentCharacterEx::GetSRModeID**](iagentcharacterex--getsrmodeid.md)


 

 




