---
title: IAgentCharacter SetName
description: IAgentCharacter SetName
ms.assetid: 4944f910-60e9-446b-82e9-2794f445789a
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacter::SetName

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetName(
   BSTR bszName   // character name
);
```

Sets the name of the character.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="bszName"></span><span id="bszname"></span><span id="BSZNAME"></span>*bszName*
</dt> <dd>

A BSTR that sets the character's name. A character's default name is defined when it is compiled with the Microsoft Agent Character Editor. You can change it using **IAgentCharacter::SetName**; however, this changes the character name for all current clients of the character. This property is not persistent (stored permanently). The character's name reverts to its default name whenever the character is first loaded by a client.

The character's name may also depend on its language ID. Characters can be compiled with different names for different languages.

The server uses the character's name setting in parts of the Microsoft Agent's interface, such as the Voice Commands Window title when the character is input-active and in the Microsoft Agent taskbar pop-up menu.

</dd> </dl>

## See Also

[**IAgentCharacter::GetName**](iagentcharacter--getname.md)


 

 




