---
title: XML Reader
description: XML Reader is a cursor over an input source of XML. At its core, an XML Reader reads one XML Node at a time, but there are additional helper APIs to make reading a sequence of nodes easier.
ms.assetid: '1f99e45c-64ba-42fb-9bf0-35e27f1c5ef2'
keywords:
- XML Reader Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# XML Reader

XML Reader is a cursor over an input source of XML. At its core, an XML Reader reads one [XML Node](xml-node.md) at a time, but there are additional helper APIs to make reading a sequence of nodes easier.


The following types of readers input are supported:

-   [**An in-memory buffer of encoded bytes**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_reader_buffer_input)
-   [**A stream**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_reader_stream_input)
-   An [XML Buffer](xml-buffer.md)

### Security

The reader will verify that the attributes present on an element are unique. The time required to perform this validation is a function of the number of attributes on the element which can be as large as [**WS\_XML\_READER\_PROPERTY\_MAX\_ATTRIBUTES**](/windows/desktop/api/WebServices/ne-webservices-ws_xml_reader_property_id). Therefore, processing large documents when **WS\_XML\_READER\_PROPERTY\_MAX\_ATTRIBUTES** is set to a large value may present an opportunity for a denial of service attack.

The reader will map prefixes to namespaces for each element and attributes. The time required to perform this mapping is a function of the number of xmlns attributes in scope which may be as large as [**WS\_XML\_READER\_PROPERTY\_MAX\_NAMESPACES**](/windows/desktop/api/WebServices/ne-webservices-ws_xml_reader_property_id). Therefore, processing large documents when this property is set to a large value may present an opportunity for a denial of service attack.

While the reader will ensure that the document follows the grammatical specification of xml and furthermore that its aspects are within the quotas specified, the content of the document must still be considered untrusted when coming from an untrusted source. Users of the reader should check all element and attribute names and namespaces using [**WsReadToStartElement**](/windows/desktop/api/WebServices/nf-webservices-wsreadtostartelement), [**WsFindAttribute**](/windows/desktop/api/WebServices/nf-webservices-wsfindattribute), or by manually inspecting [**nodes**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_node).

Some other situations to consider include, but are not limited to:

-   Expected elements may be missing
-   Unexpected elements may appear
-   Expected attributes may be missing
-   Unexpected attributes may appear
-   Elements may appear as empty elements
-   Whitespace may appear in unexpected places

Users of the reader should not allocate memory based simply on values read from the document. For example, consider the following xml document:

``` syntax
<array count='1000000'>
   <!-- malicious document provider didn't actually provide 1000000 array items -->
</array>
```

Allocating an array based soley on the assumption that some number of elements will follow would be a potential attack vector. The user of the reader in this case should instead incrementally allocate the memory as the elements appear.

XML reader does not support DTD. The user of the reader does not need to concern about DTD verification.

The following callback is used with XML readers:

-   [**WS\_READ\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_read_callback)

The following enumerations are used with XML readers:

-   [**WS\_XML\_READER\_ENCODING\_TYPE**](/windows/desktop/api/WebServices/ne-webservices-ws_xml_reader_encoding_type)
-   [**WS\_XML\_READER\_INPUT\_TYPE**](/windows/desktop/api/WebServices/ne-webservices-ws_xml_reader_input_type)
-   [**WS\_XML\_READER\_PROPERTY\_ID**](/windows/desktop/api/WebServices/ne-webservices-ws_xml_reader_property_id)

The following functions are used with XML readers:

-   [**WsCreateReader**](/windows/desktop/api/WebServices/nf-webservices-wscreatereader)
-   [**WsFillReader**](/windows/desktop/api/WebServices/nf-webservices-wsfillreader)
-   [**WsFindAttribute**](/windows/desktop/api/WebServices/nf-webservices-wsfindattribute)
-   [**WsFreeReader**](/windows/desktop/api/WebServices/nf-webservices-wsfreereader)
-   [**WsGetNamespaceFromPrefix**](/windows/desktop/api/WebServices/nf-webservices-wsgetnamespacefromprefix)
-   [**WsGetReaderNode**](/windows/desktop/api/WebServices/nf-webservices-wsgetreadernode)
-   [**WsGetReaderPosition**](/windows/desktop/api/WebServices/nf-webservices-wsgetreaderposition)
-   [**WsGetReaderProperty**](/windows/desktop/api/WebServices/nf-webservices-wsgetreaderproperty)
-   [**WsGetXmlAttribute**](/windows/desktop/api/WebServices/nf-webservices-wsgetxmlattribute)
-   [**WsMoveReader**](/windows/desktop/api/WebServices/nf-webservices-wsmovereader)
-   [**WsReadArray**](/windows/desktop/api/WebServices/nf-webservices-wsreadarray)
-   [**WsReadBytes**](/windows/desktop/api/WebServices/nf-webservices-wsreadbytes)
-   [**WsReadChars**](/windows/desktop/api/WebServices/nf-webservices-wsreadchars)
-   [**WsReadCharsUtf8**](/windows/desktop/api/WebServices/nf-webservices-wsreadcharsutf8)
-   [**WsReadEndAttribute**](/windows/desktop/api/WebServices/nf-webservices-wsreadendattribute)
-   [**WsReadEndElement**](/windows/desktop/api/WebServices/nf-webservices-wsreadendelement)
-   [**WsReadNode**](/windows/desktop/api/WebServices/nf-webservices-wsreadnode)
-   [**WsReadQualifiedName**](/windows/desktop/api/WebServices/nf-webservices-wsreadqualifiedname)
-   [**WsReadStartAttribute**](/windows/desktop/api/WebServices/nf-webservices-wsreadstartattribute)
-   [**WsReadStartElement**](/windows/desktop/api/WebServices/nf-webservices-wsreadstartelement)
-   [**WsReadToStartElement**](/windows/desktop/api/WebServices/nf-webservices-wsreadtostartelement)
-   [**WsReadValue**](/windows/desktop/api/WebServices/nf-webservices-wsreadvalue)
-   [**WsSetInput**](/windows/desktop/api/WebServices/nf-webservices-wssetinput)
-   [**WsSetInputToBuffer**](/windows/desktop/api/WebServices/nf-webservices-wssetinputtobuffer)
-   [**WsSetReaderPosition**](/windows/desktop/api/WebServices/nf-webservices-wssetreaderposition)
-   [**WsSkipNode**](/windows/desktop/api/WebServices/nf-webservices-wsskipnode)

The following handle is used with XML readers:

-   [WS\_XML\_READER](ws-xml-reader.md)

The following structures are used with XML readers:

-   [**WS\_XML\_READER\_BINARY\_ENCODING**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_reader_binary_encoding)
-   [**WS\_XML\_READER\_BUFFER\_INPUT**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_reader_buffer_input)
-   [**WS\_XML\_READER\_ENCODING**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_reader_encoding)
-   [**WS\_XML\_READER\_INPUT**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_reader_input)
-   [**WS\_XML\_READER\_MTOM\_ENCODING**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_reader_mtom_encoding)
-   [**WS\_XML\_READER\_PROPERTIES**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_reader_properties)
-   [**WS\_XML\_READER\_PROPERTY**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_reader_property)
-   [**WS\_XML\_READER\_STREAM\_INPUT**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_reader_stream_input)
-   [**WS\_XML\_READER\_TEXT\_ENCODING**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_reader_text_encoding)

 

 




