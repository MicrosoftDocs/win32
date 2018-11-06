---
title: IAgentCharacter GetName
description: IAgentCharacter GetName
ms.assetid: 6c013a18-8c56-42a8-8723-31d83b3230cb
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacter::GetName

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetName(
   BSTR * pbszName   // address of buffer for character name
);
```

Retrieves the name of the character.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pbszName"></span><span id="pbszname"></span><span id="PBSZNAME"></span>*pbszName*
</dt> <dd>

The address of a BSTR that receives the value of the name for the character.

</dd> </dl>

A character's default name is defined when it is compiled with the Microsoft Agent Character Editor. A character's name may vary based on the character's language ID. Characters can be compiled with different names for different languages.

You can also set the character's name using **IAgentCharacter:SetName**; however, this changes the name for all current clients of the character.

## See Also

[**IAgentCharacter::SetName**](iagentcharacter--setname.md)


 

 




