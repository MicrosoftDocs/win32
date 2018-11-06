---
title: LocalServer
description: Specifies the full path to a 16-bit local server application.
ms.assetid: 6eadadd5-f4d3-4e0d-9491-2ea366861aa7
keywords:
- LocalServer registry key COM
ms.topic: article
ms.date: 05/31/2018
---

# LocalServer

Specifies the full path to a 16-bit local server application.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID
   {CLSID}
      LocalServer = path
```

## Remarks

This is a **REG\_SZ** value that specifies the full path and can include any command-line arguments.

COM appends the "-Embedding" flag to the string, so the application that uses flags must parse the whole string and check for the -Embedding flag.

To run a COM object server in a separate memory space, change the value of **LocalServer** as follows:

**cmd /c start /separate** *path***.exe**

## Related topics

<dl> <dt>

[**LocalServer32**](localserver32.md)
</dt> </dl>

 

 




