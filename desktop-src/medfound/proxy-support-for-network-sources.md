---
description: Proxy Support for Network Sources
ms.assetid: e739746d-2a09-4237-a7c1-0aed4e4516d7
title: Proxy Support for Network Sources
ms.topic: article
ms.date: 05/31/2018
---

# Proxy Support for Network Sources

A proxy server is an intermediate server between your intranet and the Internet, which routes requests from the client application to the media server and retrieves files from the media server.

Media Foundation implicitly creates a *proxy locator* object when a client application tries to access a source URL. The proxy locator object exposes the [**IMFNetProxyLocator**](/windows/desktop/api/mfidl/nn-mfidl-imfnetproxylocator) interface. During source resolution, Media Foundation checks the property store passed to the source resolver method.

If the property store contains the [MFNETSOURCE\_PROXYLOCATORFACTORY](mfnetsource-proxylocatorfactory-property.md) property set to a proxy locator factory object implemented by the application then, it invokes the [**IMFNetProxyLocatorFactory::CreateProxyLocator**](/windows/desktop/api/mfidl/nf-mfidl-imfnetproxylocatorfactory-createproxylocator) method to create a proxy locator with custom configuration settings.

If the property store is not set, then Media Foundation creates the proxy locator with default configuration. These settings are as follows:

-   If user policy is set, then the proxy locator uses settings specified in the registry.

-   For HTTP, the proxy locator uses browser proxy settings.

-   For RTSP, the proxy locator is configured to bypass proxy servers when connecting to the media server.

This default configuration can be changed by the application. The following topics contain information about the configuration settings for a proxy locator:

-   [Proxy Locator Configuration Settings](proxy-locator-configuration-settings.md)

-   [How to Configure the Proxy Locator](how-to-configure-the-proxy-locator.md)

Media Foundation initializes the proxy locator for the source URL specified to the [Source Resolver](source-resolver.md). The proxy locator detects a proxy server to use based on configuration settings. When the proxy locator attempts the set a proxy server, it records the success or failure result in the registry. This value is checked during the next proxy detection process. If a certain proxy server is known to have caused failures in the past, the proxy locator skips it.

## Related topics

<dl> <dt>

[Attributes and Properties](attributes-and-properties.md)
</dt> <dt>

[Networking in Media Foundation](networking-in-media-foundation.md)
</dt> </dl>

 

 



