---
title: LocalServer32
description: Specifies the full path to a 32-bit local server application.
ms.assetid: 5d922230-f53d-4bf9-be50-c8c00f45b7a8
keywords:
- LocalServer32 registry key COM
ms.topic: article
ms.date: 01/31/2022
---

# LocalServer32

Specifies the full path to a local COM server application of any bitness or architecture.

## Registry entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID
   {CLSID}
      LocalServer32
         (Default) = path
         ServerExecutable = path
```

## Remarks

The default value of the **LocalServer32** Registry key is used to specify the location of the COM server application and, optionally, application-specific command-line arguments. COM appends the string " -Embedding" to this value so that applications can distinguish when COM is launching them from other cases. This information is passed as the *lpCommandLine* parameter of [**CreateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw). See that documentation about the ambiguity, and security issues, that arise if the path isn't properly quoted or not fully specified.

The *ServerExecutable* value, type **REG\_SZ**, first supported with Windows Server 2003, works in conjunction with the default value to prevent ambiguity in identifying the program to launch. It is passed as the *lpApplicationName* parameter to **CreateProcess**, and shouldn't be quoted. If this value isn't specified, then **NULL** is used.

Example *LocalServer32* default value.

"\\"C:\\Program Files\\Company Files\\Application.exe\\" param1 param2"

When COM starts a local server, the server must register a class object within a window of time (by default, 60 seconds), otherwise a timeout occurs.

Local servers can be hosted in Win32 services based on the [**LocalService**](localservice.md) named value of the CLSID key. If present, the **LocalServer32** key is ignored.

## Related topics

[LocalService](localservice.md)
