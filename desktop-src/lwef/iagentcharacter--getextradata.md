---
title: IAgentCharacter GetExtraData
description: IAgentCharacter GetExtraData
ms.assetid: 83f69bae-0ae3-45c5-ba0d-71610993da60
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacter::GetExtraData

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetExtraData(
   BSTR * pbszExtraData   // address of buffer for additional character data
); 
```

Retrieves additional data stored as part of the character.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pbszExtraData"></span><span id="pbszextradata"></span><span id="PBSZEXTRADATA"></span>*pbszExtraData*
</dt> <dd>

The address of a BSTR that receives the value of the additional data for the character. A character's additional data is defined when it is compiled with the Microsoft Agent Character Editor. A character developer can supply this string by editing the .ACD file for a character. The setting is optional and may not be supplied for all characters, nor can the data be defined or changed at run time. In addition, the meaning of the data supplied is defined by the character developer.

</dd> </dl>

 

 




