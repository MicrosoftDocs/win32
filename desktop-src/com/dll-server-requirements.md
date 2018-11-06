---
title: DLL Server Requirements
description: While most DLLs can run in a surrogate, some DLLs cannot.
ms.assetid: f89dabe6-f65f-4d90-ad0e-c680d4b08ba5
ms.topic: article
ms.date: 05/31/2018
---

# DLL Server Requirements

While most DLLs can run in a surrogate, some DLLs cannot.

The DLL must be well-behaved if you want to use the system-supplied surrogate. For example, a DLL that calls methods that register callbacks from the client would try to invoke those callbacks as if the function pointers it received were for instructions in its address space, which is not the case. Similarly, a DLL that uses a global variable that it expects the client to access would not work. In general, parameters that cannot be properly marshaled will prevent the DLL server from running outside the client process. In many cases, you can write a custom surrogate specifically designed to compensate for "bad" behavior. (For more information, see [Writing a Custom Surrogate](writing-a-custom-surrogate.md).)

If the DLL server uses custom interfaces, you would have to ensure that marshaling code is available for those interfaces. For example, you could build and register a proxy DLL or provide and register a type library that would allow the server to function correctly while running in a surrogate.

DLL servers will be loaded only into a surrogate process running in the proper security context. The security context for the DLL server surrogate is determined in the same way as for EXE servers. The DLL server surrogate runs in the same security context as the client, unless a **RunAs** value, which determines the security context, is set in the [AppID](appid-clsid.md) registry section for the server.

## Related topics

<dl> <dt>

[DLL Surrogates](dll-surrogates.md)
</dt> </dl>

 

 




