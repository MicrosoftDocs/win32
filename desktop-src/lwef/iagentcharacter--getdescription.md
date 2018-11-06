---
title: IAgentCharacter GetDescription
description: IAgentCharacter GetDescription
ms.assetid: 729f54ac-1c60-4a7b-b993-5682a6ea2b3c
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacter::GetDescription

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetDescription(
   BSTR * pbszDescription   // address of buffer for character description
); 
```

Retrieves the description of the character.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pbszDescription"></span><span id="pbszdescription"></span><span id="PBSZDESCRIPTION"></span>*pbszDescription*
</dt> <dd>

The address of a BSTR that receives the value of the description for the character. A character's description is defined when it is compiled with the Microsoft Agent Character Editor. The description setting is optional and may not be supplied for all characters.

</dd> </dl>

 

 




