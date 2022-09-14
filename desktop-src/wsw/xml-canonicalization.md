---
title: XML Canonicalization
description: XML canonicalization solves the problem of converting a set of XML nodes into bytes in such a way that trivial changes to the XML (such as changing the order of attributes in an element) do not change the resulting byte form.
ms.assetid: a64303a1-efc4-4c91-ab8d-3e389a655b3e
keywords:
- XML Canonicalization Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# XML Canonicalization

XML canonicalization solves the problem of converting a set of XML nodes into bytes in such a way that trivial changes to the XML (such as changing the order of attributes in an element) do not change the resulting byte form. The bytes obtained from canonicalization are commonly used to generate a cryptographic signature over XML content.


The commonly used XML canonicalization algorithms standardize the following aspects:

-   Character encoding (UTF-8 without preamble)
-   Linefeed and other character forms
-   Attribute order in an element
-   Empty element form
-   Rendering namespace declarations

The APIs [**WsStartReaderCanonicalization**](/windows/desktop/api/WebServices/nf-webservices-wsstartreadercanonicalization) and [**WsEndReaderCanonicalization**](/windows/desktop/api/WebServices/nf-webservices-wsendreadercanonicalization) provide the XML canonicalization functionality while reading a document.

The APIs [**WsStartWriterCanonicalization**](/windows/desktop/api/WebServices/nf-webservices-wsstartwritercanonicalization) and [**WsEndWriterCanonicalization**](/windows/desktop/api/WebServices/nf-webservices-wsendwritercanonicalization) provide the XML canonicalization functionality while writing a document.

The following enumerations are used with canonicalization:

-   [**WS\_XML\_CANONICALIZATION\_ALGORITHM**](/windows/desktop/api/WebServices/ne-webservices-ws_xml_canonicalization_algorithm)
-   [**WS\_XML\_CANONICALIZATION\_PROPERTY\_ID**](/windows/desktop/api/WebServices/ne-webservices-ws_xml_canonicalization_property_id)

The following functions are used with canonicalization:

-   [**WsEndReaderCanonicalization**](/windows/desktop/api/WebServices/nf-webservices-wsendreadercanonicalization)
-   [**WsEndWriterCanonicalization**](/windows/desktop/api/WebServices/nf-webservices-wsendwritercanonicalization)
-   [**WsStartReaderCanonicalization**](/windows/desktop/api/WebServices/nf-webservices-wsstartreadercanonicalization)
-   [**WsStartWriterCanonicalization**](/windows/desktop/api/WebServices/nf-webservices-wsstartwritercanonicalization)

The following structures are used with canonicalization:

-   [**WS\_XML\_CANONICALIZATION\_INCLUSIVE\_PREFIXES**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_canonicalization_inclusive_prefixes)
-   [**WS\_XML\_CANONICALIZATION\_PROPERTY**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_canonicalization_property)

 

 




