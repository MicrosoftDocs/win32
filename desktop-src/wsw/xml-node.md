---
title: XML Node
description: An XML Node represents a single piece of XML, for example, a start element and its attributes, an end element, text, or \ 0034;typed \ 0034; text content such as an integer or byte array. The data in a node varies according to the WS\_XML\_NODE\_TYPE.
ms.assetid: 'c514c542-029b-46d1-a796-1f132a41b2ad'
keywords:
- XML Node Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# XML Node

An XML Node represents a single piece of XML, for example, a start element and its attributes, an end element, text, or "typed" text content such as an integer or byte array. The data in a node varies according to the [**WS\_XML\_NODE\_TYPE**](/windows/desktop/api/WebServices/ne-webservices-ws_xml_node_type).


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

-   [**WS\_VALUE\_TYPE**](/windows/desktop/api/WebServices/ne-webservices-ws_value_type)
-   [**WS\_XML\_NODE\_TYPE**](/windows/desktop/api/WebServices/ne-webservices-ws_xml_node_type)
-   [**WS\_XML\_TEXT\_TYPE**](/windows/desktop/api/WebServices/ne-webservices-ws_xml_text_type)

The following functions are used with XML nodes:

-   [**WsTrimXmlWhitespace**](/windows/desktop/api/WebServices/nf-webservices-wstrimxmlwhitespace)
-   [**WsVerifyXmlNCName**](/windows/desktop/api/WebServices/nf-webservices-wsverifyxmlncname)
-   [**WsXmlStringEquals**](/windows/desktop/api/WebServices/nf-webservices-wsxmlstringequals)

The following macros are used with XML nodes:

-   [**WS\_XML\_STRING\_DICTIONARY\_VALUE**](/windows/desktop/api/WebServices/nf-webservices-ws_xml_string_dictionary_value)
-   [**WS\_XML\_STRING\_NULL**](/previous-versions/windows/desktop/legacy/dd323562(v=vs.85))
-   [**WS\_XML\_STRING\_VALUE**](/windows/desktop/api/WebServices/nf-webservices-ws_xml_string_value)

The following structures are used with XML nodes:

-   [**WS\_XML\_ATTRIBUTE**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_attribute)
-   [**WS\_XML\_BASE64\_TEXT**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_base64_text)
-   [**WS\_XML\_BOOL\_TEXT**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_bool_text)
-   [**WS\_XML\_COMMENT\_NODE**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_comment_node)
-   [**WS\_XML\_DATETIME\_TEXT**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_datetime_text)
-   [**WS\_XML\_DECIMAL\_TEXT**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_decimal_text)
-   [**WS\_XML\_DICTIONARY**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_dictionary)
-   [**WS\_XML\_DOUBLE\_TEXT**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_double_text)
-   [**WS\_XML\_ELEMENT\_NODE**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_element_node)
-   [**WS\_XML\_FLOAT\_TEXT**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_float_text)
-   [**WS\_XML\_GUID\_TEXT**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_guid_text)
-   [**WS\_XML\_INT32\_TEXT**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_int32_text)
-   [**WS\_XML\_INT64\_TEXT**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_int64_text)
-   [**WS\_XML\_LIST\_TEXT**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_list_text)
-   [**WS\_XML\_NODE**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_node)
-   [**WS\_XML\_QNAME**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_qname)
-   [**WS\_XML\_QNAME\_TEXT**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_qname_text)
-   [**WS\_XML\_STRING**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_string)
-   [**WS\_XML\_TEXT**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_text)
-   [**WS\_XML\_TEXT\_NODE**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_text_node)
-   [**WS\_XML\_TIMESPAN\_TEXT**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_timespan_text)
-   [**WS\_XML\_UINT64\_TEXT**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_uint64_text)
-   [**WS\_XML\_UNIQUE\_ID\_TEXT**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_unique_id_text)
-   [**WS\_XML\_UTF16\_TEXT**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_utf16_text)
-   [**WS\_XML\_UTF8\_TEXT**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_utf8_text)

 

 