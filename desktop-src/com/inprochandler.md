---
title: InprocHandler
description: InprocHandler specifies whether an application uses a custom handler in the HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID registry key.
ms.assetid: b371b331-148b-46f2-a21e-b88b285bcfc9
keywords:
- InprocHandler registry key COM
ms.topic: article
ms.date: 05/31/2018
---

# InprocHandler

Specifies whether an application uses a custom handler.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID
   {CLSID}
      InprocHandler = handler.dll
```

## Remarks

This is a **REG\_SZ** value that specifies the custom handler used by the application. If a custom handler is not used, the entry should be set to Ole32.dll.

If a container is searching the registry for a custom handler, the 16-bit version has priority with a 16-bit container and the 32-bit version has priority with a 32-bit container.

## Related topics

<dl> <dt>

[**InprocHandler32**](inprochandler32.md)
</dt> </dl>

 

 




