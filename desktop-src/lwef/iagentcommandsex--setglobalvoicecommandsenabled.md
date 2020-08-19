---
title: IAgentCommandsEx SetGlobalVoiceCommandsEnabled
description: IAgentCommandsEx SetGlobalVoiceCommandsEnabled
ms.assetid: f456b1d3-60aa-4b90-90d0-6c695947fa8a
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommandsEx::SetGlobalVoiceCommandsEnabled

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetGlobalVoiceCommandsEnabled(
 long bEnable  // Enabled setting for Agent's global voice commands
);
```

Sets the [**Enabled**](enabled-property.md) property for the voice grammar of Microsoft Agent's global commands.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="bEnable"></span><span id="benable"></span><span id="BENABLE"></span>*bEnable*
</dt> <dd>

A Boolean value that sets whether the voice grammar of Agent's global commands is enabled. **True** enables the voice grammar; **False** disables it.

</dd> </dl>

Microsoft Agent automatically adds voice parameters (grammar) for opening and closing the Voice Commands Window and for showing and hiding the character. When set to **False**, Agent disables any voice parameters for these commands as well as the voice parameters for the [**Caption**](caption-property.md) of other client's [**Command**](/windows/desktop/lwef/the-command-object) objects. This enables you to eliminate these from your client's current active grammar. However, because this potentially blocks voice access to other clients, reset this property to **True** after processing the user's voice input.

Disabling the property does not affect the character's pop-up menu. The global commands added by the server will still appear. You cannot remove them from the pop-up menu.

## See Also

[**IAgentCommandsEx::GetGlobalVoiceCommandsEnabled**](iagentcommandsex--getglobalvoicecommandsenabled.md)


 

 