---
Description: Function Discovery providers are used internally by Function Discovery to perform the discovery process.
ms.assetid: fa8956eb-2582-4e75-8f0f-e256b697791d
title: About Function Discovery Providers
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# About Function Discovery Providers

\[Function Discovery is available for use in the following versions of Windows: Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008, and Windows Vista. It may be altered or unavailable in subsequent versions.\]

Function Discovery providers are used internally by Function Discovery to perform the discovery process. Clients of Function Discovery normally use the [**IFunctionDiscovery**](/windows/desktop/api/FunctionDiscoveryAPI/nn-functiondiscoveryapi-ifunctiondiscovery) interface, which delegates queries to the installed provider objects. You can write a provider for new base-level resources similar to Plug and Play (PnP) instances or Simple Service Discovery Protocol (SSDP) network instances. Service providers can expose new functionality for function instances through the Function Discovery API.

Each provider is responsible for discovering resources and creating the function instances used to represent them. Each resource type supported by Function Discovery (for example, PnP, printers, and WS-Discovery network devices) has an underlying provider that abstracts the details of searching for that type of resource. As new resource types are defined, Function Discovery can discover them as new providers are added. This allows clients to continue using the uniform Function Discovery interfaces without sacrificing support for new resource types.

Function Discovery includes a number of built-in providers. Before writing a custom provider, check and see if a built-in provider can provide the required functionality. For more information, see [Built-in Providers](built-in-providers.md).

## Related topics

<dl> <dt>

[Provider\_Manifest\_Entries](provider-manifest-entries.md)
</dt> </dl>

 

 



