---
title: IAgentCommandsEx GetVoiceCaption
description: IAgentCommandsEx GetVoiceCaption
ms.assetid: 0e505295-386a-421f-a43c-6da03c8a2b6a
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommandsEx::GetVoiceCaption

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetVoiceCaption(
   BSTR * pbszVoiceCaption  // address of command's voice caption
);
```

Retrieves the [**VoiceCaption**](voicecaption-property.md) for a [**Command**](/windows/desktop/lwef/the-command-object) object.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pbszVoiceCaption"></span><span id="pbszvoicecaption"></span><span id="PBSZVOICECAPTION"></span>*pbszVoiceCaption*
</dt> <dd>

The address of a BSTR that receives the value of the [**Caption**](caption-property.md) text displayed for a [**Command**](/windows/desktop/lwef/the-command-object).

</dd> </dl>

The text returned is that set for your [**Command**](/windows/desktop/lwef/the-command-object) object and appears in the Voice Commands window when your client application is input-active.

This property applies only to your client application's use of the character; the setting does not affect other clients of the character or other characters of your client application.

## See Also

[**IAgentCommandsEx::SetVoiceCaption**](iagentcommandsex--setvoicecaption.md)


 

 