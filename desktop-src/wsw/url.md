---
title: Url
description: The WWSAPI URL API elements provide mechanisms to split and unescape URLs into component parts, and to escape and combine component parts back into a URL.
ms.assetid: 2904fee0-d92b-4054-8ad9-51c409756f33
keywords:
- Url Web Services for Windows
- WWSAPI
- WWS
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Url

The WWSAPI URL API elements provide mechanisms to split and unescape URLs into component parts, and to escape and combine component parts back into a URL.

-   To split and unescape URLs into component parts, use the [**WsDecodeUrl**](/windows/win32/WebServices/nf-webservices-wsdecodeurl?branch=master) function.
-   To escape and combine component parts back into a URL, use the [**WsEncodeUrl**](/windows/win32/WebServices/nf-webservices-wsencodeurl?branch=master) function.
-   To combine relative URLs with an absolute base URL forming an absolute URL, use the [**WsCombineUrl**](/windows/win32/WebServices/nf-webservices-wscombineurl?branch=master) function.

The following enumerations are part of the URL:

-   [**WS\_URL\_FLAGS**](/windows/win32/WebServices/?branch=master)
-   [**WS\_URL\_SCHEME\_TYPE**](/windows/win32/WebServices/ne-webservices-ws_url_scheme_type?branch=master)

The following functions are part of the URL:

-   [**WsCombineUrl**](/windows/win32/WebServices/nf-webservices-wscombineurl?branch=master)
-   [**WsDecodeUrl**](/windows/win32/WebServices/nf-webservices-wsdecodeurl?branch=master)
-   [**WsEncodeUrl**](/windows/win32/WebServices/nf-webservices-wsencodeurl?branch=master)

The following structures are part of the URL:

-   [**WS\_HTTPS\_URL**](/windows/win32/WebServices/ns-webservices-_ws_https_url?branch=master)
-   [**WS\_HTTP\_URL**](/windows/win32/WebServices/ns-webservices-_ws_http_url?branch=master)
-   [**WS\_NETPIPE\_URL**](/windows/win32/WebServices/ns-webservices-_ws_namedpipe_sspi_transport_security_binding?branch=master)
-   [**WS\_NETTCP\_URL**](/windows/win32/WebServices/ns-webservices-_ws_nettcp_url?branch=master)
-   [**WS\_SOAPUDP\_URL**](/windows/win32/WebServices/ns-webservices-_ws_soapudp_url?branch=master)
-   [**WS\_URL**](/windows/win32/WebServices/ns-webservices-_ws_url?branch=master)

 

 




