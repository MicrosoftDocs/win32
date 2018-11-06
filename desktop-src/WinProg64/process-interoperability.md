---
title: Process Interoperability
description: You can run Win32-based applications on 64-bit Windows using an emulation layer. Windows 10 on ARM includes an x86-on-ARM64 emulation layer. For more information, see Running 32-bit Applications.
ms.assetid: a573f26c-7577-4ff0-b314-ae0a33274738
keywords:
- process interoperability 64-bit Windows Programming
- interoperability 64-bit Windows Programming
ms.topic: article
ms.date: 05/31/2018
---

# Process Interoperability

You can run Win32-based applications on 64-bit Windows using an emulation layer. Windows 10 on ARM includes an x86-on-ARM64 emulation layer. For more information, see [Running 32-bit Applications](running-32-bit-applications.md).

On 64-bit Windows, a 64-bit process cannot load a 32-bit dynamic-link library (DLL). Additionally, a 32-bit process cannot load a 64-bit DLL. However, 64-bit Windows supports remote procedure calls (RPC) between 64-bit and 32-bit processes (both on the same computer and across computers). On 64-bit Windows, an out-of-process 32-bit COM server can communicate with a 64-bit client, and an out-of-process 64-bit COM server can communicate with a 32-bit client. Therefore, if you have a 32-bit DLL that is not COM-aware, you can wrap it in an out-of-process COM server and use COM to marshal calls to and from a 64-bit process.

In-process servers are currently registered using the **InprocServer** registry entry. On 64-bit Windows, 64- and 32-bit in-process servers should use the **InprocServer32** entry.

To port handles, which by their nature are local to the computer and would never be used across the 32-bit to 64-bit boundary, use the **HANDLE\_PTR** type instead of the **INT\_PTR** or **DWORD\_PTR** type. This includes porting RPC interfaces passing such handles as **DWORD** values. The 64-bit **HANDLE\_PTR** is 64 bits on the wire (not truncated) and thus does not need mapping. (The 32-bit **HANDLE\_PTR** is 32 bits on the wire.)

For more information, see [Designing 64-bit-Compatible Interfaces](designing-64-bit-compatible-interfaces.md).

 

 




