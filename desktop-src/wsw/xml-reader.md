---
title: XML Reader
description: XML Reader is a cursor over an input source of XML. At its core, an XML Reader reads one XML Node at a time, but there are additional helper APIs to make reading a sequence of nodes easier.
ms.assetid: 7acbe407-e91b-435a-82bc-acbbc13cfcfd
keywords:
- XML Reader Web Services for Windows
- WWSAPI
- WWS
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# XML Reader

XML Reader is a cursor over an input source of XML. At its core, an XML Reader reads one [XML Node](xml-node.md) at a time, but there are additional helper APIs to make reading a sequence of nodes easier.

## 

The following types of readers input are supported:

-   [**An in-memory buffer of encoded bytes**](/windows/win32/WebServices/ns-webservices-_ws_xml_reader_buffer_input?branch=master)
-   [**A stream**](/windows/win32/WebServices/ns-webservices-_ws_xml_reader_stream_input?branch=master)
-   An [XML Buffer](xml-buffer.md)

### Security

The reader will verify that the attributes present on an element are unique. The time required to perform this validation is a function of the number of attributes on the element which can be as large as [**WS\_XML\_READER\_PROPERTY\_MAX\_ATTRIBUTES**](/windows/win32/WebServices/ne-webservices-ws_xml_reader_property_id?branch=master). Therefore, processing large documents when **WS\_XML\_READER\_PROPERTY\_MAX\_ATTRIBUTES** is set to a large value may present an opportunity for a denial of service attack.

The reader will map prefixes to namespaces for each element and attributes. The time required to perform this mapping is a function of the number of xmlns attributes in scope which may be as large as [**WS\_XML\_READER\_PROPERTY\_MAX\_NAMESPACES**](/windows/win32/WebServices/ne-webservices-ws_xml_reader_property_id?branch=master). Therefore, processing large documents when this property is set to a large value may present an opportunity for a denial of service attack.

While the reader will ensure that the document follows the grammatical specification of xml and furthermore that its aspects are within the quotas specified, the content of the document must still be considered untrusted when coming from an untrusted source. Users of the reader should check all element and attribute names and namespaces using [**WsReadToStartElement**](/windows/win32/WebServices/nf-webservices-wsreadtostartelement?branch=master), [**WsFindAttribute**](/windows/win32/WebServices/nf-webservices-wsfindattribute?branch=master), or by manually inspecting [**nodes**](/windows/win32/WebServices/ns-webservices-_ws_xml_node?branch=master).

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

-   [**WS\_READ\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_read_callback?branch=master)

The following enumerations are used with XML readers:

-   [**WS\_XML\_READER\_ENCODING\_TYPE**](/windows/win32/WebServices/ne-webservices-ws_xml_reader_encoding_type?branch=master)
-   [**WS\_XML\_READER\_INPUT\_TYPE**](/windows/win32/WebServices/ne-webservices-ws_xml_reader_input_type?branch=master)
-   [**WS\_XML\_READER\_PROPERTY\_ID**](/windows/win32/WebServices/ne-webservices-ws_xml_reader_property_id?branch=master)

The following functions are used with XML readers:

-   [**WsCreateReader**](/windows/win32/WebServices/nf-webservices-wscreatereader?branch=master)
-   [**WsFillReader**](/windows/win32/WebServices/nf-webservices-wsfillreader?branch=master)
-   [**WsFindAttribute**](/windows/win32/WebServices/nf-webservices-wsfindattribute?branch=master)
-   [**WsFreeReader**](/windows/win32/WebServices/nf-webservices-wsfreereader?branch=master)
-   [**WsGetNamespaceFromPrefix**](/windows/win32/WebServices/nf-webservices-wsgetnamespacefromprefix?branch=master)
-   [**WsGetReaderNode**](/windows/win32/WebServices/nf-webservices-wsgetreadernode?branch=master)
-   [**WsGetReaderPosition**](/windows/win32/WebServices/nf-webservices-wsgetreaderposition?branch=master)
-   [**WsGetReaderProperty**](/windows/win32/WebServices/nf-webservices-wsgetreaderproperty?branch=master)
-   [**WsGetXmlAttribute**](/windows/win32/WebServices/nf-webservices-wsgetxmlattribute?branch=master)
-   [**WsMoveReader**](/windows/win32/WebServices/nf-webservices-wsmovereader?branch=master)
-   [**WsReadArray**](/windows/win32/WebServices/nf-webservices-wsreadarray?branch=master)
-   [**WsReadBytes**](/windows/win32/WebServices/nf-webservices-wsreadbytes?branch=master)
-   [**WsReadChars**](/windows/win32/WebServices/nf-webservices-wsreadchars?branch=master)
-   [**WsReadCharsUtf8**](/windows/win32/WebServices/nf-webservices-wsreadcharsutf8?branch=master)
-   [**WsReadEndAttribute**](/windows/win32/WebServices/nf-webservices-wsreadendattribute?branch=master)
-   [**WsReadEndElement**](/windows/win32/WebServices/nf-webservices-wsreadendelement?branch=master)
-   [**WsReadNode**](/windows/win32/WebServices/nf-webservices-wsreadnode?branch=master)
-   [**WsReadQualifiedName**](/windows/win32/WebServices/nf-webservices-wsreadqualifiedname?branch=master)
-   [**WsReadStartAttribute**](/windows/win32/WebServices/nf-webservices-wsreadstartattribute?branch=master)
-   [**WsReadStartElement**](/windows/win32/WebServices/nf-webservices-wsreadstartelement?branch=master)
-   [**WsReadToStartElement**](/windows/win32/WebServices/nf-webservices-wsreadtostartelement?branch=master)
-   [**WsReadValue**](/windows/win32/WebServices/nf-webservices-wsreadvalue?branch=master)
-   [**WsSetInput**](/windows/win32/WebServices/nf-webservices-wssetinput?branch=master)
-   [**WsSetInputToBuffer**](/windows/win32/WebServices/nf-webservices-wssetinputtobuffer?branch=master)
-   [**WsSetReaderPosition**](/windows/win32/WebServices/nf-webservices-wssetreaderposition?branch=master)
-   [**WsSkipNode**](/windows/win32/WebServices/nf-webservices-wsskipnode?branch=master)

The following handle is used with XML readers:

-   [WS\_XML\_READER](ws-xml-reader.md)

The following structures are used with XML readers:

-   [**WS\_XML\_READER\_BINARY\_ENCODING**](/windows/win32/WebServices/ns-webservices-_ws_xml_reader_binary_encoding?branch=master)
-   [**WS\_XML\_READER\_BUFFER\_INPUT**](/windows/win32/WebServices/ns-webservices-_ws_xml_reader_buffer_input?branch=master)
-   [**WS\_XML\_READER\_ENCODING**](/windows/win32/WebServices/ns-webservices-_ws_xml_reader_encoding?branch=master)
-   [**WS\_XML\_READER\_INPUT**](/windows/win32/WebServices/ns-webservices-_ws_xml_reader_input?branch=master)
-   [**WS\_XML\_READER\_MTOM\_ENCODING**](/windows/win32/WebServices/ns-webservices-_ws_xml_reader_mtom_encoding?branch=master)
-   [**WS\_XML\_READER\_PROPERTIES**](/windows/win32/WebServices/ns-webservices-_ws_xml_reader_properties?branch=master)
-   [**WS\_XML\_READER\_PROPERTY**](/windows/win32/WebServices/ns-webservices-_ws_xml_reader_property?branch=master)
-   [**WS\_XML\_READER\_STREAM\_INPUT**](/windows/win32/WebServices/ns-webservices-_ws_xml_reader_stream_input?branch=master)
-   [**WS\_XML\_READER\_TEXT\_ENCODING**](/windows/win32/WebServices/ns-webservices-_ws_xml_reader_text_encoding?branch=master)

 

 




