---
title: XML Writer
description: XML Writer is an API for emitting XML. At its core, an XML Writer writes one XML Node at a time, but there are additional helper APIs to make writing a sequence of nodes easier.
ms.assetid: '8f413e60-8a30-492c-8f2d-80be511fee11'
keywords: ["XML Writer Web Services for Windows", "WWSAPI", "WWS"]
---

# XML Writer

XML Writer is an API for emitting XML. At its core, an XML Writer writes one [XML Node](xml-node.md) at a time, but there are additional helper APIs to make writing a sequence of nodes easier.

## 

The following types of writer output are supported:

-   [**An in-memory buffer of encoded bytes**](ws-xml-writer-buffer-output.md)
-   [**A stream**](ws-xml-writer-stream-output.md)
-   An [XML Buffer](xml-buffer.md)

The following callbacks are used with the XML writer:

-   [**WS\_DYNAMIC\_STRING\_CALLBACK**](ws-dynamic-string-callback.md)
-   [**WS\_PULL\_BYTES\_CALLBACK**](ws-pull-bytes-callback.md)
-   [**WS\_PUSH\_BYTES\_CALLBACK**](ws-push-bytes-callback.md)
-   [**WS\_WRITE\_CALLBACK**](ws-write-callback.md)

The following enumerations are used with the XML writer:

-   [**WS\_CHARSET**](ws-charset.md)
-   [**WS\_XML\_WRITER\_ENCODING\_TYPE**](ws-xml-writer-encoding-type.md)
-   [**WS\_XML\_WRITER\_OUTPUT\_TYPE**](ws-xml-writer-output-type.md)
-   [**WS\_XML\_WRITER\_PROPERTY\_ID**](ws-xml-writer-property-id.md)

The following functions are used with the XML writer:

-   [**WsCopyNode**](wscopynode.md)
-   [**WsCreateWriter**](wscreatewriter.md)
-   [**WsFlushWriter**](wsflushwriter.md)
-   [**WsFreeWriter**](wsfreewriter.md)
-   [**WsGetPrefixFromNamespace**](wsgetprefixfromnamespace.md)
-   [**WsGetWriterPosition**](wsgetwriterposition.md)
-   [**WsGetWriterProperty**](wsgetwriterproperty.md)
-   [**WsMoveWriter**](wsmovewriter.md)
-   [**WsPullBytes**](wspullbytes.md)
-   [**WsPushBytes**](wspushbytes.md)
-   [**WsSetOutput**](wssetoutput.md)
-   [**WsSetOutputToBuffer**](wssetoutputtobuffer.md)
-   [**WsSetWriterPosition**](wssetwriterposition.md)
-   [**WsWriteArray**](wswritearray.md)
-   [**WsWriteBytes**](wswritebytes.md)
-   [**WsWriteChars**](wswritechars.md)
-   [**WsWriteCharsUtf8**](wswritecharsutf8.md)
-   [**WsWriteEndAttribute**](wswriteendattribute.md)
-   [**WsWriteEndCData**](wswriteendcdata.md)
-   [**WsWriteEndElement**](wswriteendelement.md)
-   [**WsWriteNode**](wswritenode.md)
-   [**WsWriteQualifiedName**](wswritequalifiedname.md)
-   [**WsWriteStartAttribute**](wswritestartattribute.md)
-   [**WsWriteStartCData**](wswritestartcdata.md)
-   [**WsWriteStartElement**](wswritestartelement.md)
-   [**WsWriteText**](wswritetext.md)
-   [**WsWriteValue**](wswritevalue.md)
-   [**WsWriteXmlnsAttribute**](wswritexmlnsattribute.md)

The following handle is used with the XML writer:

-   [WS\_XML\_WRITER](ws-xml-writer.md)

The following structures are used with the XML writer:

-   [**WS\_XML\_WRITER\_BINARY\_ENCODING**](ws-xml-writer-binary-encoding.md)
-   [**WS\_XML\_WRITER\_BUFFER\_OUTPUT**](ws-xml-writer-buffer-output.md)
-   [**WS\_XML\_WRITER\_ENCODING**](ws-xml-writer-encoding.md)
-   [**WS\_XML\_WRITER\_MTOM\_ENCODING**](ws-xml-writer-mtom-encoding.md)
-   [**WS\_XML\_WRITER\_OUTPUT**](ws-xml-writer-output.md)
-   [**WS\_XML\_WRITER\_PROPERTIES**](ws-xml-writer-properties.md)
-   [**WS\_XML\_WRITER\_PROPERTY**](ws-xml-writer-property.md)
-   [**WS\_XML\_WRITER\_STREAM\_OUTPUT**](ws-xml-writer-stream-output.md)
-   [**WS\_XML\_WRITER\_TEXT\_ENCODING**](ws-xml-writer-text-encoding.md)

 

 




