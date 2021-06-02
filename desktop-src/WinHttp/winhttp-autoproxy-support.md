---
description: To ease the configuration of proxy settings, WinHTTP 5.1 implements the Web Proxy Auto-Discovery (WPAD) protocol, also known as autoproxy.
ms.assetid: f766f37b-a1aa-420f-ac3b-d03485630d88
title: WinHTTP AutoProxy Support
ms.topic: article
ms.date: 05/31/2018
---

# WinHTTP AutoProxy Support

To ease the configuration of proxy settings, WinHTTP 5.1 implements the Web Proxy Auto-Discovery (WPAD) protocol, also known as autoproxy.

## Overview of AutoProxy

Applications and components that use WinHTTP to send HTTP requests should ensure that the proxy configuration is set correctly. Unless the client has a direct Internet connection, an HTTP request should normally be sent through a web proxy server that connects the client's local network to the Internet (for example, this is often the case for Web clients on a corporate LAN). For server-based applications, the proxy configuration is normally managed by the server's administrator using the WinHTTP ProxyCfg.exe utility. The server administrator knows the name of the proxy server in advance and uses ProxyCfg.exe to record this setting in the registry where WinHTTP can look it up. However, requiring client desktop end-users to manually configure WinHTTP proxy settings is problematic. The end-user may not know the name of the proxy server; requiring the end-user to run the ProxyCfg.exe utility can be a support burden for an organization. To support a good user experience, a web-enabled client application should determine the proxy configuration without user intervention.

To make configuring the proxy settings for WinHTTP-based applications easier, WinHTTP now implements the [Web Proxy Auto-Discovery (WPAD) protocol](https://tools.ietf.org/html/draft-ietf-wrec-wpad-01), often referred to as *autoproxy*. This is the same protocol that web browsers implement to automatically discover the proxy configuration without requiring an end-user to specify a proxy server manually. This feature is available starting with WinHTTP version 5.1 in Windows 2000 Service Pack 3, Windows XP Service Pack 1 and Windows Server 2003. Note that although both Microsoft Internet Explorer and Microsoft WinHTTP support WPAD, the specification never progressed beyond the "Internet-Draft" stage, and expired in May 2001.

The WPAD protocol works as follows:

1.  Using the DHCP and/or DNS network protocols, the URL of a Proxy Auto-Configuration (PAC) file is discovered. The URL identifies a PAC file on the client's local network. WinHTTP supports only "http:" and "https:" PAC URLs; it does not, for example, support "file:" URLS.
2.  The PAC file is downloaded and optionally cached on the client's computer. The PAC file is an executable script that generates a list of one or more proxy servers given a target host name and URL. WinHTTP supports only ECMAScript-based PAC files.
3.  On each HTTP request, the PAC script code is executed, with the host name and URL of the HTTP request passed in as parameters. WinHTTP expects the PAC script code to contain a function called **FindProxyForURL**, in the form:
4.  ``` syntax
    FindProxyForURL( url, host );
    ```

    This function computes a list of one or more proxy servers that can be used by the HTTP client in order to transmit the request. If the PAC script determines that the HTTP client can reach the target server directly without going through a proxy server at all, it indicates this using a special return value.

## AutoProxy Topics

-   [WinHTTP AutoProxy Functions](winhttp-autoproxy-api.md)
-   [Discovery Without an Auto-Config File](discovery-without-an-auto-config-file.md)
-   [AutoProxy Issues in WinHTTP](autoproxy-issues-in-winhttp.md)
-   [Setting WinInet Proxy Configurations in WinHTTP](setting-wininet-proxy-configurations-in-winhttp.md)
-   [AutoProxy Cache](autoproxy-cache.md)
-   [IPv6 Extensions to Navigator Auto-Config File Format](ipv6-extensions-to-navigator-auto-config-file-format.md)

 

 



