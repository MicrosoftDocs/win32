---
title: IAgentNotifySinkEx AgentPropertyChange
description: IAgentNotifySinkEx AgentPropertyChange
ms.assetid: 8293cd77-320a-4b57-b3d8-52bc450d6aa0
ms.topic: article
ms.date: 05/31/2018
---

# IAgentNotifySinkEx::AgentPropertyChange

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT AgentPropertyChange(
);
```

Notifies a client application when the user changes a Microsoft Agent property setting.

-   No return value.

When the user changes a Microsoft Agent property setting in the Microsoft Agent property sheet, the server sends this event to all clients unless the server is currently suspended.

## See Also

[**IAgentNotifySinkEx::DefaultCharacterChange**](iagentnotifysinkex--defaultcharacterchange.md)


 

 




