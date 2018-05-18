---
Description: 'Function Discovery provides a programmatic interface for enumerating system resources.'
ms.assetid: '014011ff-f41e-48d9-99c1-ad9dd1d2f62e'
title: Architectural Description
---

# Architectural Description

\[Function Discovery is available for use in the following versions of Windows: Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008, and Windows Vista. It may be altered or unavailable in subsequent versions.\]

Function Discovery provides a programmatic interface for enumerating system resources. This interface serves as an abstraction layer over device- and network-specific programming interfaces. The following diagram illustrates the Function Discovery architecture.

![function discovery architecture](images/fdarchitecture.png)

Function Discovery supports an extensible discovery provider model. All enumerated resources are discovered through one of the [built-in providers](built-in-providers.md) or a custom provider. For more information about implementing a custom provider, see [Function Discovery Providers](portal-providers.md).

Function Discovery supports a query service, through which a client application can obtain a pointer to a COM interface that it can use to use or control the device or resource.

## Related topics

<dl> <dt>

[Unifying the Discovery Process](unifying-the-discovery-process.md)
</dt> </dl>

 

 



