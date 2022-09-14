---
title: IAgentCharacter SetIdleOn
description: IAgentCharacter SetIdleOn
ms.assetid: 397d223a-0970-4535-ad46-2923df6b9975
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacter::SetIdleOn

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetIdleOn(
   long bOn  // idle processing flag
);
```

Sets automatic idle processing for a character.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="bOn"></span><span id="bon"></span><span id="BON"></span>*bOn*
</dt> <dd>

Idle processing flag. If this parameter is **True**, the Microsoft Agent automatically plays **Idling** state animations.

</dd> </dl>

The server automatically sets a time out after the last animation played for a character. When this timer's interval is complete, the server begins the **Idling** states for a character, playing its associated **Idling** animations at regular intervals. If you want to manage the **Idling** state animations yourself, set the property to **False**. This property applies only to your client application's use of the character; the setting does not affect other clients of the character or other characters of your client application.

## See Also

[**IAgentCharacter::GetIdleOn**](iagentcharacter--getidleon.md)


 

 




