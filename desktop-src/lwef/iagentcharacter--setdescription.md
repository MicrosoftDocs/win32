---
title: IAgentCharacter SetDescription
description: IAgentCharacter SetDescription
ms.assetid: ae01b9e6-1616-4806-9125-ceb4cb54aab1
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacter::SetDescription

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetDescription(
   BSTR bszDescription   // character description
); 
```

Sets the description of the character.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="bszDescription"></span><span id="bszdescription"></span><span id="BSZDESCRIPTION"></span>*bszDescription*
</dt> <dd>

A BSTR that sets the description for the character. A character's default description is defined when it is compiled with the Microsoft Agent Character Editor. The description setting is optional and may not be supplied for all characters. You can change the character's description using **IAgentCharacter::setDescription**; however, this value is not persistent (stored permanently). The character's description reverts to its default setting whenever the character is first loaded by a client.

</dd> </dl>

## See Also

[**IAgentCharacter::GetDescription**](iagentcharacter--getdescription.md)


 

 




