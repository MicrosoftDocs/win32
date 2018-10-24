---
title: LocalServer32
description: Specifies the full path to a 32-bit local server application.
ms.assetid: 5d922230-f53d-4bf9-be50-c8c00f45b7a8
keywords:
- LocalServer32 registry key COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LocalServer32

Specifies the full path to a 32-bit local server application.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID
   {CLSID}
      LocalServer32
         (Default) = path
         ServerExecutable = path
```

## Remarks

The **ServerExecutable** value, which is of type **REG\_SZ** and is supported starting with Windows Server 2003, works in conjunction with the **LocalServer32** subkey to prevent any ambiguity when using the [**CreateProcess**](https://msdn.microsoft.com/library/windows/desktop/ms682425) function. **LocalServer32** specifies the location of the COM server application to launch, and this information is passed as the first parameter *lpApplicationName* for **CreateProcess**. Depending on the implementation of **CreateProcess**, this information might be ambiguous. For this reason, if **ServerExecutable** is specified, COM passes the **ServerExecutable** named value to the *lpApplicationName* parameter of **CreateProcess**. If **ServerExecutable** is not specified, COM passes **NULL** as the value for the first parameter of **CreateProcess**.

To help provide system security, use quoted strings in the path to indicate where the executable filename ends and the arguments begin. For example, instead of specifying the following path as the **LocalServer32** entry:

"C:\\Program Files\\Company Files\\Application.exe param1 param2"

specify the path using the following syntax:

"\\"C:\\Program Files\\Company Files\\Application.exe\\" param1 param2"

COM appends the "-Embedding" flag to the string, so the application that uses flags needs to parse the whole string and check for the -Embedding flag.

When COM starts a 32-bit local server, the server must register a class object within an elapsed time set by the user. By default, the elapsed time value must be at least 5 minutes, in milliseconds, but cannot exceed the number of milliseconds in 30 days. Applications typically should not set this value, which is in the **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\COM2\\ServerStartElapsedTime** entry.

The required entries for 32-bit local servers are [**InprocHandler32**](inprochandler32.md), [**LocalServer**](localserver.md), **LocalServer32**, and [**Insertable**](insertable.md).

If a container is searching the registry for a local server, a 32-bit local server has priority over a 16-bit local server.

If you are implementing classes as services, you should be aware that the [**LocalService**](localservice.md) named value is used in preference to the **LocalServer32** key for local and remote activation requestsâ€”if **LocalService** exists and refers to a valid service, the **LocalServer32** key is ignored.

## Related topics

<dl> <dt>

[**LocalServer**](localserver.md)
</dt> <dt>

[**LocalService**](localservice.md)
</dt> </dl>

 

 




