---
title: XML Canonicalization
description: XML canonicalization solves the problem of converting a set of XML nodes into bytes in such a way that trivial changes to the XML (such as changing the order of attributes in an element) do not change the resulting byte form.
ms.assetid: 'a64303a1-efc4-4c91-ab8d-3e389a655b3e'
keywords: ["XML Canonicalization Web Services for Windows", "WWSAPI", "WWS"]
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

The APIs [**WsStartReaderCanonicalization**](wsstartreadercanonicalization.md) and [**WsEndReaderCanonicalization**](wsendreadercanonicalization.md) provide the XML canonicalization functionality while reading a document.

The APIs [**WsStartWriterCanonicalization**](wsstartwritercanonicalization.md) and [**WsEndWriterCanonicalization**](wsendwritercanonicalization.md) provide the XML canonicalization functionality while writing a document.

The following enumerations are used with canonicalization:

-   [**WS\_XML\_CANONICALIZATION\_ALGORITHM**](ws-xml-canonicalization-algorithm.md)
-   [**WS\_XML\_CANONICALIZATION\_PROPERTY\_ID**](ws-xml-canonicalization-property-id.md)

The following functions are used with canonicalization:

-   [**WsEndReaderCanonicalization**](wsendreadercanonicalization.md)
-   [**WsEndWriterCanonicalization**](wsendwritercanonicalization.md)
-   [**WsStartReaderCanonicalization**](wsstartreadercanonicalization.md)
-   [**WsStartWriterCanonicalization**](wsstartwritercanonicalization.md)

The following structures are used with canonicalization:

-   [**WS\_XML\_CANONICALIZATION\_INCLUSIVE\_PREFIXES**](ws-xml-canonicalization-inclusive-prefixes.md)
-   [**WS\_XML\_CANONICALIZATION\_PROPERTY**](ws-xml-canonicalization-property.md)

 

 




