---
description: Illustrates which registry key must be set to prevent AutoPlay.
ms.assetid: E0A25DC2-0991-45D6-9185-019DB4C040AD
title: How to Prevent AutoPlay for a Component
ms.topic: article
ms.date: 05/31/2018
---

# How to Prevent AutoPlay for a Component

Illustrates which registry key must be set to prevent AutoPlay.

## Instructions


To prevent AutoPlay from launching in response to an event, add the following **REG\_SZ** value, as shown in this example.

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Microsoft
         Windows
            CurrentVersion
               Explorer
                  AutoplayHandlers
                     CancelAutoplay
                        CLSID
                           00000000-0000-0000-0000-000000000000
```

The value is the class identifier (CLSID) that the component that is generating the event is known by in the running object table (ROT). The value has no data.

> [!IMPORTANT]
> Under this key, the CLSIDs are not enclosed in braces ( {} ).

 

 

 



