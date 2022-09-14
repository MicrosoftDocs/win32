---
title: InprocServer
description: Specifies the path to the in-process server DLL.
ms.assetid: f14cc8f7-e93e-4db8-8b0d-ea77a6301f33
keywords:
- InprocServer registry key COM
ms.topic: article
ms.date: 05/31/2018
---

# InprocServer

Specifies the path to the in-process server DLL.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID
   {CLSID}
      InprocServer
         (Default) = path
```

## Remarks

The **InprocServer** entry is relatively rare for insertable classes.

In-process servers are currently registered using the **InprocServer** registry entry. The 32-bit and 64-bit in-process servers should use the [**InprocServer32**](inprocserver32.md) entry. If a container is searching the registry for an in-process server, the 16-bit version has priority with a 16-bit container and 32-bit version has priority with a 32-bit container.

## Related topics

<dl> <dt>

[**InprocServer32**](inprocserver32.md)
</dt> </dl>

 

 




