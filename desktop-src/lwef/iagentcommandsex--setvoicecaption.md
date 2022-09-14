---
title: IAgentCommandsEx SetVoiceCaption
description: IAgentCommandsEx SetVoiceCaption
ms.assetid: f13c9ca5-70c9-42d0-b53c-45dc8980a24c
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommandsEx::SetVoiceCaption

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetVoiceCaption(
   BSTR bszVoiceCaption  // voice caption text
);
```

Sets the [**VoiceCaption**](voicecaption-property.md) text displayed for the [**Command**](/windows/desktop/lwef/the-command-object) object.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="bszVoiceCaption"></span><span id="bszvoicecaption"></span><span id="BSZVOICECAPTION"></span>*bszVoiceCaption*
</dt> <dd>

A BSTR that specifies the text for the [**VoiceCaption**](voicecaption-property.md) property for a [**Command**](/windows/desktop/lwef/the-command-object).

</dd> </dl>

If you define a [**Command**](/windows/desktop/lwef/the-command-object) object in a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection and set its [**Voice**](voice-property.md) property, you will typically also set its [**VoiceCaption**](voicecaption-property.md) property. This text will appear in the Voice Commands Window when your client application is input-active and the character is visible. If this property is not set, the setting for the [**Caption**](caption-property.md) property determines the text displayed. When neither the **VoiceCaption** or **Caption** property is set, the command does not appear in the Voice Commands Window.

## See Also

[**IAgentCommandsEx::GetVoiceCaption**](iagentcommandsex--getvoicecaption.md)


 

 