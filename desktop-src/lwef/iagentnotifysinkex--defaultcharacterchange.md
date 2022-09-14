---
title: IAgentNotifySinkEx DefaultCharacterChange
description: IAgentNotifySinkEx DefaultCharacterChange
ms.assetid: 13acb502-e247-433f-abf3-2d78a2d6a4a7
ms.topic: article
ms.date: 05/31/2018
---

# IAgentNotifySinkEx::DefaultCharacterChange

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT DefaultCharacterChange(
   BSTR bszGUID  // character identifier
);
```

Notifies a client application when the default character changes.

-   No return value.

<dl> <dt>

<span id="bszGUID"></span><span id="bszguid"></span><span id="BSZGUID"></span>*bszGUID*
</dt> <dd>

The unique identifier for the character.

</dd> </dl>

When the user changes the character assigned as the user's default character, the server sends this event to clients that have loaded the default character. The event returns the character's unique identifier (GUID) formatted with braces and dashes, which is defined when the character is built with the Microsoft Agent Character Editor.

When the new character appears, it assumes the same size as any already loaded instance of the character or the previous default character (in that order).

## See Also

[**IAgent::Load**](iagent--load.md)


 

 




