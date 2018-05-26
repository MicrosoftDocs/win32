---
Description: Function Discovery includes a number of built-in providers. In most cases, it is not necessary to write your own provider. If you must write a provider, adhere to the guidelines provided below.
ms.assetid: 26660093-0d02-4eef-bf5b-18ff07748540
title: Using Function Discovery Providers
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using Function Discovery Providers

\[Function Discovery is available for use in the following versions of Windows: Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008, and Windows Vista. It may be altered or unavailable in subsequent versions.\]

Function Discovery includes a number of [built-in providers](built-in-providers.md). In most cases, it is not necessary to write your own provider. If you must write a provider, adhere to the guidelines provided below.

## Activation contexts

Function Discovery providers must be free threaded.

By default, the PnP-X subsystem activates providers using the CLSCTX\_LOCAL\_SERVER activation context; however, some clients may activate the provider using the CLSCTX\_INPROC\_SERVER activation context. Therefore, providers must support activation in both contexts.

The [Function Discovery Provider Sample](function-discovery-provider-sample.md) implements the provider as a DLL to support in-proc activation and a host process running as an EXE file that loads the DLL to support out-of-proc activation. An EXE host is used in the sample because it is simpler and consumes fewer resources than a Windows service. The sample host process will automatically be started by COM when a client activates a provider and will exit once all clients have disconnected.

If you are writing a provider that must maintain state even when no clients are connected to the provider, then you should use a Windows service to host the provider.

## Security considerations

PnP-X Function Discovery providers typically communicate on the network, often using multicast. For this reason, providers are attack vectors which, if exploited, can result in remote compromise of the system. To mitigate security risks and as a defense-in-depth strategy, providers should run with the least privilege required. It is recommended that all provider hosts run as LocalService.

Because providers do not run as the same user account as the client process, they need to cache the caller's impersonation token and use it to call **CoSetSecurityBlanket** on client interfaces. There are two points to note about this:

-   The provider must call **CoSetSecurityBlanket**, even if it will not use the interface passed to it. Failure to do so will result in the interface not being released until COM rundown occurs.
-   Because the provider caches the impersonation token as well as some interfaces on which **CoSetSecurityBlanket** has been called using the token, the provider host must register for logoff notifications and free the cached token and interfaces for all providers that were in use by the client for which a logoff has been received. A logon session is only completely ended when all tokens for the session have been closed, so failure to close the cached token and interfaces effectively prevents the session from ending until COM rundown occurs.

## Preservation of Add / Remove notification order

Network enumeration protocols generally have a mechanism to order events on the network and detect and discard older information. Function Discovery providers must take care that [**OnUpdate**](ifunctiondiscoverynotification-onevent.md) events are communicated to the client in the same order that events occurred on the network.

The [Function Discovery Provider Sample](function-discovery-provider-sample.md) keeps a per-provider instance queue of notification data and will only deliver one notification to a client at a time. All the queues are serviced by a thread pool, so multiple clients may concurrently receive notifications. This is an efficient and scalable approach.

## Related topics

<dl> <dt>

[Function Discovery Provider Sample](function-discovery-provider-sample.md)
</dt> </dl>

 

 



