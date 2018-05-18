---
title: XML Node
description: An XML Node represents a single piece of XML, for example, a start element and its attributes, an end element, text, or \ 0034;typed \ 0034; text content such as an integer or byte array. The data in a node varies according to the WS\_XML\_NODE\_TYPE.
ms.assetid: '98c40d57-ee71-40f8-9416-5b29adc30489'
keywords: ["XML Node Web Services for Windows", "WWSAPI", "WWS"]
---

# XML Node

An XML Node represents a single piece of XML, for example, a start element and its attributes, an end element, text, or "typed" text content such as an integer or byte array. The data in a node varies according to the [**WS\_XML\_NODE\_TYPE**](ws-xml-node-type.md).

## 

The following shows an example of an encoding specific xml document represented with encoding independent structures.

``` syntax
<p:PurchaseOrder xmlns:p="http://tempuri.org" p:id="3891">
    <p:Buyer>Joe</p:Buyer>
</p:PurchaseOrder>
```

``` syntax
WS_XML_STRING purchaseOrder = WS_XML_STRING_VALUE("PurchaseOrder");
WS_XML_STRING id            = WS_XML_STRING_VALUE("id");
WS_XML_STRING prefix        = WS_XML_STRING_VALUE("p");
WS_XML_STRING ns            = WS_XML_STRING_VALUE("http://tempuri.org");

WS_XML_ATTRIBUTE xmlnsAttribute =
{
    /* singleQuote */ FALSE,
    /* isXmlNs     */ TRUE,
    /* prefix      */ &prefix,
    /* localName   */ NULL,
    /* ns          */ &ns,
    /* value       */ NULL
};
WS_XML_INT32_TEXT idText =
{
    /* text  */ { WS_XML_TEXT_TYPE_INT32 },
    /* value */ 3891
};
WS_XML_ATTRIBUTE idAttribute =
{
    /* singleQuote */ FALSE,
    /* isXmlNs     */ FALSE,
    /* prefix      */ &prefix,
    /* localName   */ &id,
    /* ns          */ &ns,
    /* value       */ &idText.text,
};
WS_XML_ATTRIBUTE* attributes[2] =
{
    &xmlnsAttribute,
    &idAttribute
};
WS_XML_ELEMENT_NODE elementNode =
{
    /* node           */ { WS_XML_NODE_TYPE_ELEMENT },
    /* prefix         */ &prefix,
    /* localName      */ &purchaseOrder,
    /* ns             */ &ns,
    /* attributeCount */ 2,
    /* attributes     */ attributes,
    /* isEmpty        */ FALSE,
    /* array          */ NULL,
};
WS_XML_UTF8_TEXT joeText =
{
    /* text  */ { WS_XML_TEXT_TYPE_UTF8 },
    /* value */ WS_XML_STRING_VALUE("Joe")
};
WS_XML_TEXT_NODE textNode =
{
    /* node */ { WS_XML_NODE_TYPE_TEXT },
    /* text */ &joeText.text
};
WS_XML_NODE endElementNode =
{
    WS_XML_NODE_TYPE_END_ELEMENT
};
WS_XML_NODE* nodes[3] =
{
    &elementNode.node,
    &textNode.node,
    &endElementNode
};
```

The following enumerations are used with XML nodes:

-   [**WS\_VALUE\_TYPE**](ws-value-type.md)
-   [**WS\_XML\_NODE\_TYPE**](ws-xml-node-type.md)
-   [**WS\_XML\_TEXT\_TYPE**](ws-xml-text-type.md)

The following functions are used with XML nodes:

-   [**WsTrimXmlWhitespace**](wstrimxmlwhitespace.md)
-   [**WsVerifyXmlNCName**](wsverifyxmlncname.md)
-   [**WsXmlStringEquals**](wsxmlstringequals.md)

The following macros are used with XML nodes:

-   [**WS\_XML\_STRING\_DICTIONARY\_VALUE**](ws-xml-string-dictionary-value.md)
-   [**WS\_XML\_STRING\_NULL**](ws-xml-string-null.md)
-   [**WS\_XML\_STRING\_VALUE**](ws-xml-string-value.md)

The following structures are used with XML nodes:

-   [**WS\_XML\_ATTRIBUTE**](ws-xml-attribute.md)
-   [**WS\_XML\_BASE64\_TEXT**](ws-xml-base64-text.md)
-   [**WS\_XML\_BOOL\_TEXT**](ws-xml-bool-text.md)
-   [**WS\_XML\_COMMENT\_NODE**](ws-xml-comment-node.md)
-   [**WS\_XML\_DATETIME\_TEXT**](ws-xml-datetime-text.md)
-   [**WS\_XML\_DECIMAL\_TEXT**](ws-xml-decimal-text.md)
-   [**WS\_XML\_DICTIONARY**](ws-xml-dictionary.md)
-   [**WS\_XML\_DOUBLE\_TEXT**](ws-xml-double-text.md)
-   [**WS\_XML\_ELEMENT\_NODE**](ws-xml-element-node.md)
-   [**WS\_XML\_FLOAT\_TEXT**](ws-xml-float-text.md)
-   [**WS\_XML\_GUID\_TEXT**](ws-xml-guid-text.md)
-   [**WS\_XML\_INT32\_TEXT**](ws-xml-int32-text.md)
-   [**WS\_XML\_INT64\_TEXT**](ws-xml-int64-text.md)
-   [**WS\_XML\_LIST\_TEXT**](ws-xml-list-text.md)
-   [**WS\_XML\_NODE**](ws-xml-node.md)
-   [**WS\_XML\_QNAME**](ws-xml-qname.md)
-   [**WS\_XML\_QNAME\_TEXT**](ws-xml-qname-text.md)
-   [**WS\_XML\_STRING**](ws-xml-string.md)
-   [**WS\_XML\_TEXT**](ws-xml-text.md)
-   [**WS\_XML\_TEXT\_NODE**](ws-xml-text-node.md)
-   [**WS\_XML\_TIMESPAN\_TEXT**](ws-xml-timespan-text.md)
-   [**WS\_XML\_UINT64\_TEXT**](ws-xml-uint64-text.md)
-   [**WS\_XML\_UNIQUE\_ID\_TEXT**](ws-xml-unique-id-text.md)
-   [**WS\_XML\_UTF16\_TEXT**](ws-xml-utf16-text.md)
-   [**WS\_XML\_UTF8\_TEXT**](ws-xml-utf8-text.md)

 

 




