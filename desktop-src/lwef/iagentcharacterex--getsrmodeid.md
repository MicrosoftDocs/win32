---
title: IAgentCharacterEx GetSRModeID
description: IAgentCharacterEx GetSRModeID
ms.assetid: 28049680-8245-49f3-9ecd-13c7605f10ed
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacterEx::GetSRModeID

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetSRModeID(
   BSTR * pbszModeID  // address of speech recognition engine ID
);
```

Retrieves the mode ID of the speech recognition engine set for the character.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pbszModeID"></span><span id="pbszmodeid"></span><span id="PBSZMODEID"></span>*pbszModeID*
</dt> <dd>

Address of a BSTR that receives the mode ID setting of the speech recognition engine for the character.

</dd> </dl>

This setting returns the engine set for a character's speech input. The mode ID for a speech recognition engine is a string representation of the GUID (formatted with braces and dashes) by the speech vendor uniquely identifying the engine. For more information, see the [Microsoft Speech SDK documentation](https://msdn.microsoft.com/library/ee705648.aspx).

If you do not set a speech recognition engine mode ID for the character, the server returns an engine that matches the character's language setting (using Microsoft Speech API interfaces). If there is no matching speech recognition engine available for the character, the server returns a null (empty) string.

When speech input is enabled (in the Advanced Character Options window), querying or setting this property will load the associated engine (if it is not already loaded), and start speech services. That is, the Listening key is available, and the Listening Tip is displayable. (The Listening key and Listening Tip are enabled only if they are also enabled in Advanced Character Options.) However, if you query the property when speech is disabled, the server does not start speech services and it returns a null string (empty string).

This function returns only the setting for your client application's use of the character; the setting does not reflect other clients of the character or other characters of your client application.

This function does not fail if the [**IAgentSpeechInputProperties::GetEnabled**](iagentspeechinputproperties--getenabled.md) returns **False**.

Microsoft Agent's speech engine requirements are based on the Microsoft Speech API. Engines supporting Microsoft Agent's SAPI requirements can be installed and used with Agent.

## See Also

[**IAgentCharacterEx::SetSRModeID**](iagentcharacterex--setsrmodeid.md)


 

 




