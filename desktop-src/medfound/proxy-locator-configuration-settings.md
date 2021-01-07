---
description: Proxy Locator Configuration Settings
ms.assetid: d74a85cf-293e-4322-9aff-55b06d6fda5e
title: Proxy Locator Configuration Settings
ms.topic: article
ms.date: 05/31/2018
---

# Proxy Locator Configuration Settings

This topic describes the configuration settings for the default proxy locator. For information about creating the proxy locator with custom configuration settings, see [How to Configure the Proxy Locator](how-to-configure-the-proxy-locator.md).

The proxy locator can be configured to operate in three modes: *manual mode*, *auto-detect mode*, and *browser mode*. The values are defined in [**MFNET\_PROXYSETTINGS**](/windows/desktop/api/mfidl/ne-mfidl-mfnet_proxysettings) enumeration. The application can configure the mode by setting the [**MFNETSOURCE\_PROXYSETTINGS**](mfnetsource-proxysettings-property.md) property. The proxy locator can also be configured not to use a proxy server by setting this property to **MFNET\_PROXYSETTING\_NONE**. The proxy server is not used if the media server is a local host or the application requests a class A address (127.x.x.x)—reserved for loopback tests.

> [!Caution]  
> A proxy server is a security barrier between your intranet and the Internet. Not using a proxy server can expose the network to security threats.

 

-   Manual Mode. The application sets this mode by setting the [**MFNETSOURCE\_PROXYSETTING**](mfnetsource-proxysettings-property.md) property to **MFNET\_PROXYSETTING\_MANUAL**. The application must specify the following connection information:

    -   Hostname of the proxy server: [**MFNETSOURCE\_PROXYHOSTNAME**](mfnetsource-proxyhostname-property.md) property.
    -   Port number: [**MFNETSOURCE\_PROXYPORT**](mfnetsource-proxyport-property.md) property.
    -   Whether to use a proxy server for local addresses: [**MFNETSOURCE\_PROXYBYPASSFORLOCAL**](mfnetsource-proxybypassforlocal-property.md) property. This setting is optional. If this is not specified, then the proxy locator uses a default value of **FALSE**.

        > [!Note]  
        > By bypassing the proxy server, the application might be able to connect to media servers on the intranet faster.

         

    -   List of media server addresses that do not require a proxy server to establish a connection: [**MFNETSOURCE\_PROXYEXCEPTIONLIST**](mfnetsource-proxyexceptionlist-property.md) property. This setting is optional.

-   Auto-Detect Mode. The application sets this mode by setting the [**MFNETSOURCE\_PROXYSETTING**](mfnetsource-proxysettings-property.md) property to **MFNET\_PROXYSETTING\_AUTO**. In this mode, the proxy locator uses the WinHTTP AutoProxy mechanism to get the hostname and the port number for the proxy server. This connection information is retrieved by using the WPAD auto proxy script, which is configured by the domain administrator. For more information about this mechanism, see the [Microsoft website](../winhttp/winhttp-autoproxy-support.md).

    The proxy locator caches the connection information in the registry. In subsequent proxy detection calls, the proxy locator reads proxy information from the registry cache to reduce the overhead involved in auto detection. However, the application can force auto proxy redetection by setting the [**MFNETSOURCE\_PROXYRERUNAUTODETECTION**](mfnetsource-proxyrerunautodetection-property.md) property.

-   Browser Mode. The application sets this mode by setting the [**MFNETSOURCE\_PROXYSETTING**](mfnetsource-proxysettings-property.md) property to **MFNET\_PROXYSETTING\_BROWSER**. In this mode, the proxy locator uses the proxy settings of the browser application. This mode is set by default if the protocol is HTTP or HTTPD.

## Related topics

<dl> <dt>

[Proxy Support for Network Sources](proxy-support-for-network-sources.md)
</dt> </dl>

 

 
