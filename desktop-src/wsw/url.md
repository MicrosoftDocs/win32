---
title: Url
description: The WWSAPI URL API elements provide mechanisms to split and unescape URLs into component parts, and to escape and combine component parts back into a URL.
ms.assetid: 2904fee0-d92b-4054-8ad9-51c409756f33
keywords:
- Url Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# Url

The WWSAPI URL API elements provide mechanisms to split and unescape URLs into component parts, and to escape and combine component parts back into a URL.

-   To split and unescape URLs into component parts, use the [**WsDecodeUrl**](/windows/desktop/api/WebServices/nf-webservices-wsdecodeurl) function.
-   To escape and combine component parts back into a URL, use the [**WsEncodeUrl**](/windows/desktop/api/WebServices/nf-webservices-wsencodeurl) function.
-   To combine relative URLs with an absolute base URL forming an absolute URL, use the [**WsCombineUrl**](/windows/desktop/api/WebServices/nf-webservices-wscombineurl) function.

The following enumerations are part of the URL:

-   [**WS\_URL\_FLAGS**](/windows/win32/api/webservices/ne-webservices-ws_xml_writer_encoding_type)
-   [**WS\_URL\_SCHEME\_TYPE**](/windows/desktop/api/WebServices/ne-webservices-ws_url_scheme_type)

The following functions are part of the URL:

-   [**WsCombineUrl**](/windows/desktop/api/WebServices/nf-webservices-wscombineurl)
-   [**WsDecodeUrl**](/windows/desktop/api/WebServices/nf-webservices-wsdecodeurl)
-   [**WsEncodeUrl**](/windows/desktop/api/WebServices/nf-webservices-wsencodeurl)

The following structures are part of the URL:

-   [**WS\_HTTPS\_URL**](/windows/desktop/api/WebServices/ns-webservices-ws_https_url)
-   [**WS\_HTTP\_URL**](/windows/desktop/api/WebServices/ns-webservices-ws_http_url)
-   [**WS\_NETPIPE\_URL**](/windows/desktop/api/WebServices/ns-webservices-ws_namedpipe_sspi_transport_security_binding)
-   [**WS\_NETTCP\_URL**](/windows/desktop/api/WebServices/ns-webservices-ws_nettcp_url)
-   [**WS\_SOAPUDP\_URL**](/windows/desktop/api/WebServices/ns-webservices-ws_soapudp_url)
-   [**WS\_URL**](/windows/desktop/api/WebServices/ns-webservices-ws_url)

 

 




