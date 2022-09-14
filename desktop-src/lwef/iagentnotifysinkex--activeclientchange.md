---
title: IAgentNotifySinkEx ActiveClientChange
description: IAgentNotifySinkEx ActiveClientChange
ms.assetid: e953e803-c898-4c07-adc0-8b895b5e8473
ms.topic: article
ms.date: 05/31/2018
---

# IAgentNotifySinkEx::ActiveClientChange

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT ActiveClientChange(
...long dwCharID,  // character ID
   long lStatus    // active state flag
);
```

Notifies a client application if its active client is no longer the active client of a character.

-   No return value.

<dl> <dt>

<span id="dwCharID"></span><span id="dwcharid"></span><span id="DWCHARID"></span>*dwCharID*
</dt> <dd>

Identifier of the character for which active client status changed.

</dd> <dt>

<span id="lStatus"></span><span id="lstatus"></span><span id="LSTATUS"></span>*lStatus*
</dt> <dd>

Active state change of the client, which can be a combination of any of the following values:



| Value                                                              | Description                                                           |
|--------------------------------------------------------------------|-----------------------------------------------------------------------|
| **const unsigned short** **ACTIVATE\_NOTACTIVE = 0;**<br/>   | Your client is not the active client of the character.                |
| **const unsigned short** **ACTIVATE\_ACTIVE = 1;**<br/>      | Your client is the active client of the character.                    |
| **const unsigned short** **ACTIVATE\_INPUTACTIVE = 2;**<br/> | Your client is input-active (active client of the topmost character). |



 

</dd> </dl>

When multiple client applications share the same character, the active client of the character receives mouse input (for example, Microsoft Agent control click or drag events). Similarly, when multiple characters are displayed, the active client of the topmost character (also known as the input-active client) receives [**IAgentNotifySink::Command**](iagentnotifysink--command.md) events.

When the active client of a character changes, this event passes back the ID of that character and **True** if your application has become the active client of the character or **False** if it is no longer the active client of the character.

A client application may receive this event when the user selects another client application's entry in character's pop-up menu or by voice command, the client application changes its active status, or another client application quits its connection to Microsoft Agent. Agent sends this event only to the client applications that are directly affected-those that either become the active client or stop being the active client.

You can use the [**Activate**](iagentcharacter--activate.md) method to set whether your application is the active client of the character or to make your application the input-active client (which also makes the character topmost).

## See Also

[**IAgentCharacter::Activate**](iagentcharacter--activate.md), [**IAgentCharacterEx::GetActive**](iagentcharacterex--getactive.md), [**IAgentNotifySink::ActivateInputState**](iagentnotifysink--activateinputstate.md)


 

 





