---
description: A network provider is a DLL that enables the Windows operating system to support a specific network protocol.
ms.assetid: 21dfa941-72fd-4f2c-8bc4-379ed6ca2a4c
title: Implementing a Network Provider
ms.topic: article
ms.date: 05/31/2018
---

# Implementing a Network Provider

A network provider is a DLL that enables the Windows operating system to support a specific network protocol. It does this by implementing the Network Provider API. This API is a set of functions the [*Multiple Provider Router*](../secgloss/m-gly.md) (MPR) calls to communicate with the network. The network provider then translates these calls into network-specific API calls to perform the action specified by the MPR. In this way, the Windows operating system can interact with new network protocols without having to understand their network-specific APIs.

To create a network provider, write a DLL that exports the [**NPGetCaps**](/windows/desktop/api/Npapi/nf-npapi-npgetcaps) function.

Support of the other functions in the Network Provider API is optional. If your network provider does not require a function, your DLL does not need to implement it or provide a stub implementation. For more information, see the individual function topics in [Network Provider Functions](authentication-functions.md).

The exception is that if you support one of the following enumeration functions, you must support the other two functions as well: [**NPOpenEnum**](/windows/desktop/api/Npapi/nf-npapi-npopenenum), [**NPEnumResource**](/windows/desktop/api/Npapi/nf-npapi-npenumresource), and [**NPCloseEnum**](/windows/desktop/api/Npapi/nf-npapi-npcloseenum).

The following guidelines describe how to write a network provider that interacts well with the MPR and the Windows operating system. Whenever possible, your provider should adhere to the following guidelines for speed, validation, and routing.

## Speed

A network provider should quickly determine whether a network resource is its own. This is because the MPR may have to cycle through many providers to find the owner of a resource.

If the network provider does not own the resource, it should immediately return the WN\_BAD\_NETNAME status code.

It is also important that providers that support [**NPGetDirectoryType**](/windows/desktop/api/Npapi/nf-npapi-npgetdirectorytype) return results for this function quickly because it is called while WinFile is painting the directory tree.

## Validation

The order of validation is important. A network provider should first determine whether its network is started and then determine whether the network and network provider support the operation. If, after these checks, the network provider receives any network resources, it should determine whether it owns them. Finally, it should validate other parameters.

## Routing

If the MPR has to cycle through network providers, it will try all providers until one accepts the call. In other words, the MPR always continues to try to find a network provider.

It does, however, take note of the first significant error reported by a provider. Errors such as ERROR\_BAD\_NETPATH, ERROR\_BAD\_NET\_NAME, ERROR\_INVALID\_PARAMETER, ERROR\_INVALID\_LEVEL are considered insignificant because they simply mean that the provider does not manage the resource. However, if the provider fails with the error ERROR\_INVALID\_PASSWORD or some other significant error, MPR records this error and continues cycling through the network providers. In general, when routing, if no provider accepts the call, the MPR reports the first significant error it encounters while cycling through the network providers.

Your network provider should take this behavior of the MPR into account when deciding what error message to return.

## Implementation note

When implementing Network Provider DLL’s, the provider must not call into other [Windows Networking Functions](../wnet/windows-networking-functions.md), [Shell APIs](../shell/samples-usingthumbnailproviders.md), or other UNC path-based queries that could cause reentry into the MPR subsystem. If you make such calls from a Network Provider DLL, the application, or other operating system components may experience contention, poor performance, or deadlocks inside the MPR subsystem.

 

 
