---
title: DefaultIcon
description: Provides default icon information for iconic presentations of objects.
ms.assetid: 45a3289b-d9c4-4857-bf48-1fd664ce4430
keywords:
- DefaultIcon registry key COM
ms.topic: article
ms.date: 05/31/2018
---

# DefaultIcon

Provides default icon information for iconic presentations of objects.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID
   {CLSID}
      DefaultIcon = path, resourceID
```

## Remarks

This is a **REG\_SZ** value that specifies the full path to the executable name of the object application and the resource index of the icon within the executable.

**DefaultIcon** identifies the icon to use when, for example, a control is minimized to an icon. This entry contains the full path to the executable name of the server application and the resource index of the icon within the executable. Applications can use the information provided by **DefaultIcon** to obtain an icon handle with [**ExtractIcon**](/windows/win32/api/shellapi/nf-shellapi-extracticona).

 

 