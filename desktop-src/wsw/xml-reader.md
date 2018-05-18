---
title: XML Reader
description: XML Reader is a cursor over an input source of XML. At its core, an XML Reader reads one XML Node at a time, but there are additional helper APIs to make reading a sequence of nodes easier.
ms.assetid: '7acbe407-e91b-435a-82bc-acbbc13cfcfd'
keywords: ["XML Reader Web Services for Windows", "WWSAPI", "WWS"]
---

# XML Reader

XML Reader is a cursor over an input source of XML. At its core, an XML Reader reads one [XML Node](xml-node.md) at a time, but there are additional helper APIs to make reading a sequence of nodes easier.

## 

The following types of readers input are supported:

-   [**An in-memory buffer of encoded bytes**](ws-xml-reader-buffer-input.md)
-   [**A stream**](ws-xml-reader-stream-input.md)
-   An [XML Buffer](xml-buffer.md)

### Security

The reader will verify that the attributes present on an element are unique. The time required to perform this validation is a function of the number of attributes on the element which can be as large as [**WS\_XML\_READER\_PROPERTY\_MAX\_ATTRIBUTES**](ws-xml-reader-property-id.md). Therefore, processing large documents when **WS\_XML\_READER\_PROPERTY\_MAX\_ATTRIBUTES** is set to a large value may present an opportunity for a denial of service attack.

The reader will map prefixes to namespaces for each element and attributes. The time required to perform this mapping is a function of the number of xmlns attributes in scope which may be as large as [**WS\_XML\_READER\_PROPERTY\_MAX\_NAMESPACES**](ws-xml-reader-property-id.md). Therefore, processing large documents when this property is set to a large value may present an opportunity for a denial of service attack.

While the reader will ensure that the document follows the grammatical specification of xml and furthermore that its aspects are within the quotas specified, the content of the document must still be considered untrusted when coming from an untrusted source. Users of the reader should check all element and attribute names and namespaces using [**WsReadToStartElement**](wsreadtostartelement.md), [**WsFindAttribute**](wsfindattribute.md), or by manually inspecting [**nodes**](ws-xml-node.md).

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

-   [**WS\_READ\_CALLBACK**](ws-read-callback.md)

The following enumerations are used with XML readers:

-   [**WS\_XML\_READER\_ENCODING\_TYPE**](ws-xml-reader-encoding-type.md)
-   [**WS\_XML\_READER\_INPUT\_TYPE**](ws-xml-reader-input-type.md)
-   [**WS\_XML\_READER\_PROPERTY\_ID**](ws-xml-reader-property-id.md)

The following functions are used with XML readers:

-   [**WsCreateReader**](wscreatereader.md)
-   [**WsFillReader**](wsfillreader.md)
-   [**WsFindAttribute**](wsfindattribute.md)
-   [**WsFreeReader**](wsfreereader.md)
-   [**WsGetNamespaceFromPrefix**](wsgetnamespacefromprefix.md)
-   [**WsGetReaderNode**](wsgetreadernode.md)
-   [**WsGetReaderPosition**](wsgetreaderposition.md)
-   [**WsGetReaderProperty**](wsgetreaderproperty.md)
-   [**WsGetXmlAttribute**](wsgetxmlattribute.md)
-   [**WsMoveReader**](wsmovereader.md)
-   [**WsReadArray**](wsreadarray.md)
-   [**WsReadBytes**](wsreadbytes.md)
-   [**WsReadChars**](wsreadchars.md)
-   [**WsReadCharsUtf8**](wsreadcharsutf8.md)
-   [**WsReadEndAttribute**](wsreadendattribute.md)
-   [**WsReadEndElement**](wsreadendelement.md)
-   [**WsReadNode**](wsreadnode.md)
-   [**WsReadQualifiedName**](wsreadqualifiedname.md)
-   [**WsReadStartAttribute**](wsreadstartattribute.md)
-   [**WsReadStartElement**](wsreadstartelement.md)
-   [**WsReadToStartElement**](wsreadtostartelement.md)
-   [**WsReadValue**](wsreadvalue.md)
-   [**WsSetInput**](wssetinput.md)
-   [**WsSetInputToBuffer**](wssetinputtobuffer.md)
-   [**WsSetReaderPosition**](wssetreaderposition.md)
-   [**WsSkipNode**](wsskipnode.md)

The following handle is used with XML readers:

-   [WS\_XML\_READER](ws-xml-reader.md)

The following structures are used with XML readers:

-   [**WS\_XML\_READER\_BINARY\_ENCODING**](ws-xml-reader-binary-encoding.md)
-   [**WS\_XML\_READER\_BUFFER\_INPUT**](ws-xml-reader-buffer-input.md)
-   [**WS\_XML\_READER\_ENCODING**](ws-xml-reader-encoding.md)
-   [**WS\_XML\_READER\_INPUT**](ws-xml-reader-input.md)
-   [**WS\_XML\_READER\_MTOM\_ENCODING**](ws-xml-reader-mtom-encoding.md)
-   [**WS\_XML\_READER\_PROPERTIES**](ws-xml-reader-properties.md)
-   [**WS\_XML\_READER\_PROPERTY**](ws-xml-reader-property.md)
-   [**WS\_XML\_READER\_STREAM\_INPUT**](ws-xml-reader-stream-input.md)
-   [**WS\_XML\_READER\_TEXT\_ENCODING**](ws-xml-reader-text-encoding.md)

 

 




