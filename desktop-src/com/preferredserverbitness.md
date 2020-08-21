---
title: PreferredServerBitness
description: Sets the preferred architecture, 32-bit or 64-bit, for this COM server.
ms.assetid: ef770039-1624-4256-aa09-1443695c1a1f
keywords:
- PreferredServerBitness registry value COM
ms.topic: article
ms.date: 05/31/2018
---

# PreferredServerBitness

Sets the preferred architecture, 32-bit or 64-bit, for this COM server.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\AppID
   {AppID_GUID}
      PreferredServerBitness = value
```

## Remarks

This is a **REG\_DWORD** value that is available only on 64-bit versions of Windows.



| Value | Description                                                                                                                                                                                                |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | Match the server architecture to the client architecture. For example, if the client is 32-bit, use a 32-bit version of the server, if it is available. If not, the client's activation request will fail. |
| 2     | Use a 32-bit version of the server. If one does not exist, the client's activation request will fail.                                                                                                      |
| 3     | Use a 64-bit version of the server. If one does not exist, the client's activation request will fail.                                                                                                      |



 

If this value is not present, then:

-   If the computer that hosts the server is running Windows XP or Windows Server 2003 without SP1 or later installed, then COM will prefer a 64-bit version of the server if available; otherwise it will activate a 32-bit version of the server.
-   If the computer that hosts the server is running Windows Server 2003 with SP1 or later installed, then COM will try to match the server architecture to the client architecture. In other words, for a 32-bit client, COM will activate a 32-bit server if available; otherwise it will activate a 64-bit version of the server. For a 64-bit client, COM will activate a 64-bit server if available; otherwise it will activate a 32-bit server.

The client can also specify its own architecture preference via the CLSCTX\_ACTIVATE\_32\_BIT\_SERVER and CLSCTX\_ACTIVATE\_64\_BIT\_SERVER flags, and these will override the server's preference. For more information, and a chart of possible interactions between client and server architecture preferences, see [**CLSCTX**](/windows/win32/api/wtypesbase/ne-wtypesbase-clsctx).

## Related topics

<dl> <dt>

[**CLSCTX**](/windows/win32/api/wtypesbase/ne-wtypesbase-clsctx)
</dt> </dl>

 

 