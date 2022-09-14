---
title: IAgentCharacterEx GetActive
description: IAgentCharacterEx GetActive
ms.assetid: b14ae69a-a50e-4488-b5a7-33702e6555eb
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacterEx::GetActive

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetActive(
   short * psState  // address of active state setting
);
```

Retrieves whether your client application is the active client of the character and whether the character is topmost.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="psState"></span><span id="psstate"></span><span id="PSSTATE"></span>*psState*
</dt> <dd>

Address of a variable that receives one of the following values for the state setting:



| Value                                                              | Description                                                           |
|--------------------------------------------------------------------|-----------------------------------------------------------------------|
| **const unsigned short** **ACTIVATE\_NOTACTIVE = 0;**<br/>   | Your client is not the active client of the character.                |
| **const unsigned short** **ACTIVATE\_ACTIVE = 1;**<br/>      | Your client is the active client of the character.                    |
| **const unsigned short** **ACTIVATE\_INPUTACTIVE = 2;**<br/> | Your client is input-active (active client of the topmost character). |



 

</dd> </dl>

This setting lets you know whether you are the active client of the character or whether your character is the input active character. When multiple client applications share the same character, the active client of the character receives mouse input (for example, Microsoft Agent control click or drag events). Similarly, when multiple characters are displayed, the active client of the topmost character (also known as the input-active client) receives [**IAgentNotifySink::Command**](iagentnotifysink--command.md) events.

Use the [**Activate**](iagentcharacter--activate.md) method to set whether your application is the active client of the character or to make your application the input active client (which also makes the character topmost).

## See Also

[**IAgentCharacter::Activate**](iagentcharacter--activate.md), [**IAgentNotifySinkEx::ActiveClientChange**](iagentnotifysinkex--activeclientchange.md)


 

 





