---
title: IAgentCharacterEx GetGUID
description: IAgentCharacterEx GetGUID
ms.assetid: 25fb2531-a81c-4add-8134-77b1cd57cfe3
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacterEx::GetGUID

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetGUID(
   BSTR * pbszGUID  // address of character's ID
);
```

Retrieves the unique ID for the character.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pbszGUID"></span><span id="pbszguid"></span><span id="PBSZGUID"></span>*pbszGUID*
</dt> <dd>

Address of a BSTR that receives the ID for the character.

</dd> </dl>

The property returns a string representation of the GUID (formatted with braces and dashes) that the server uses to uniquely identify the character. A character identifier is set when it is compiled with the Microsoft Agent Character Editor. The property is read-only.

 

 




