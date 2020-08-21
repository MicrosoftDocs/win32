---
title: IAgentCommandsEx GetGlobalVoiceCommandsEnabled
description: IAgentCommandsEx GetGlobalVoiceCommandsEnabled
ms.assetid: 9c8fa978-a02b-4dfc-8cf7-e066c5b75122
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommandsEx::GetGlobalVoiceCommandsEnabled

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetGlobalVoiceCommandsEnabled(
   long * pbEnabled  // address of the global voice command setting
);
```

Retrieves whether the voice grammar for Agent's global commands is enabled.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pbEnabled"></span><span id="pbenabled"></span><span id="PBENABLED"></span>*pbEnabled*
</dt> <dd>

The address that receives **True** if the voice grammar for Agent's global commands is enabled, **False** if disabled.

</dd> </dl>

Microsoft Agent automatically adds voice parameters (grammar) for opening and closing the Voice Commands Window and for showing and hiding the character. When this method returns **False**, any voice parameters for these commands as well as the voice parameters for the [**Caption**](caption-property.md) of other clients' [**Command**](/windows/desktop/lwef/the-command-object) objects are not included in the grammar. This enables you to eliminate these from your client's current active grammar. However, this setting does not reflect the inclusion of these commands in the character's pop-up menu.

## See Also

[**IAgentCommandsEx::SetGlobalVoiceCommandsEnabled**](iagentcommandsex--setglobalvoicecommandsenabled.md)


 

 