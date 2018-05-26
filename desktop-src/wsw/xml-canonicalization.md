---
title: XML Canonicalization
description: XML canonicalization solves the problem of converting a set of XML nodes into bytes in such a way that trivial changes to the XML (such as changing the order of attributes in an element) do not change the resulting byte form.
ms.assetid: a64303a1-efc4-4c91-ab8d-3e389a655b3e
keywords:
- XML Canonicalization Web Services for Windows
- WWSAPI
- WWS
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# XML Canonicalization

XML canonicalization solves the problem of converting a set of XML nodes into bytes in such a way that trivial changes to the XML (such as changing the order of attributes in an element) do not change the resulting byte form. The bytes obtained from canonicalization are commonly used to generate a cryptographic signature over XML content.

## 

The commonly used XML canonicalization algorithms standardize the following aspects:

-   Character encoding (UTF-8 without preamble)
-   Linefeed and other character forms
-   Attribute order in an element
-   Empty element form
-   Rendering namespace declarations

The APIs [**WsStartReaderCanonicalization**](/windows/win32/WebServices/nf-webservices-wsstartreadercanonicalization?branch=master) and [**WsEndReaderCanonicalization**](/windows/win32/WebServices/nf-webservices-wsendreadercanonicalization?branch=master) provide the XML canonicalization functionality while reading a document.

The APIs [**WsStartWriterCanonicalization**](/windows/win32/WebServices/nf-webservices-wsstartwritercanonicalization?branch=master) and [**WsEndWriterCanonicalization**](/windows/win32/WebServices/nf-webservices-wsendwritercanonicalization?branch=master) provide the XML canonicalization functionality while writing a document.

The following enumerations are used with canonicalization:

-   [**WS\_XML\_CANONICALIZATION\_ALGORITHM**](/windows/win32/WebServices/ne-webservices-ws_xml_canonicalization_algorithm?branch=master)
-   [**WS\_XML\_CANONICALIZATION\_PROPERTY\_ID**](/windows/win32/WebServices/ne-webservices-ws_xml_canonicalization_property_id?branch=master)

The following functions are used with canonicalization:

-   [**WsEndReaderCanonicalization**](/windows/win32/WebServices/nf-webservices-wsendreadercanonicalization?branch=master)
-   [**WsEndWriterCanonicalization**](/windows/win32/WebServices/nf-webservices-wsendwritercanonicalization?branch=master)
-   [**WsStartReaderCanonicalization**](/windows/win32/WebServices/nf-webservices-wsstartreadercanonicalization?branch=master)
-   [**WsStartWriterCanonicalization**](/windows/win32/WebServices/nf-webservices-wsstartwritercanonicalization?branch=master)

The following structures are used with canonicalization:

-   [**WS\_XML\_CANONICALIZATION\_INCLUSIVE\_PREFIXES**](/windows/win32/WebServices/ns-webservices-_ws_xml_canonicalization_inclusive_prefixes?branch=master)
-   [**WS\_XML\_CANONICALIZATION\_PROPERTY**](/windows/win32/WebServices/ns-webservices-_ws_xml_canonicalization_property?branch=master)

 

 




