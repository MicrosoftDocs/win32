---
title: XML Writer
description: XML Writer is an API for emitting XML. At its core, an XML Writer writes one XML Node at a time, but there are additional helper APIs to make writing a sequence of nodes easier.
ms.assetid: '69d50793-1d5b-4fc7-bf69-128f8e23a98d'
keywords:
- XML Writer Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# XML Writer

XML Writer is an API for emitting XML. At its core, an XML Writer writes one [XML Node](xml-node.md) at a time, but there are additional helper APIs to make writing a sequence of nodes easier.


The following types of writer output are supported:

-   [**An in-memory buffer of encoded bytes**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_writer_buffer_output)
-   [**A stream**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_writer_stream_output)
-   An [XML Buffer](xml-buffer.md)

The following callbacks are used with the XML writer:

-   [**WS\_DYNAMIC\_STRING\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_dynamic_string_callback)
-   [**WS\_PULL\_BYTES\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_pull_bytes_callback)
-   [**WS\_PUSH\_BYTES\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_push_bytes_callback)
-   [**WS\_WRITE\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_write_callback)

The following enumerations are used with the XML writer:

-   [**WS\_CHARSET**](/windows/desktop/api/WebServices/ne-webservices-ws_charset)
-   [**WS\_XML\_WRITER\_ENCODING\_TYPE**](/windows/desktop/api/WebServices/ne-webservices-ws_xml_writer_encoding_type)
-   [**WS\_XML\_WRITER\_OUTPUT\_TYPE**](/windows/desktop/api/WebServices/ne-webservices-ws_xml_writer_output_type)
-   [**WS\_XML\_WRITER\_PROPERTY\_ID**](/windows/desktop/api/WebServices/ne-webservices-ws_xml_writer_property_id)

The following functions are used with the XML writer:

-   [**WsCopyNode**](/windows/desktop/api/WebServices/nf-webservices-wscopynode)
-   [**WsCreateWriter**](/windows/desktop/api/WebServices/nf-webservices-wscreatewriter)
-   [**WsFlushWriter**](/windows/desktop/api/WebServices/nf-webservices-wsflushwriter)
-   [**WsFreeWriter**](/windows/desktop/api/WebServices/nf-webservices-wsfreewriter)
-   [**WsGetPrefixFromNamespace**](/windows/desktop/api/WebServices/nf-webservices-wsgetprefixfromnamespace)
-   [**WsGetWriterPosition**](/windows/desktop/api/WebServices/nf-webservices-wsgetwriterposition)
-   [**WsGetWriterProperty**](/windows/desktop/api/WebServices/nf-webservices-wsgetwriterproperty)
-   [**WsMoveWriter**](/windows/desktop/api/WebServices/nf-webservices-wsmovewriter)
-   [**WsPullBytes**](/windows/desktop/api/WebServices/nf-webservices-wspullbytes)
-   [**WsPushBytes**](/windows/desktop/api/WebServices/nf-webservices-wspushbytes)
-   [**WsSetOutput**](/windows/desktop/api/WebServices/nf-webservices-wssetoutput)
-   [**WsSetOutputToBuffer**](/windows/desktop/api/WebServices/nf-webservices-wssetoutputtobuffer)
-   [**WsSetWriterPosition**](/windows/desktop/api/WebServices/nf-webservices-wssetwriterposition)
-   [**WsWriteArray**](/windows/desktop/api/WebServices/nf-webservices-wswritearray)
-   [**WsWriteBytes**](/windows/desktop/api/WebServices/nf-webservices-wswritebytes)
-   [**WsWriteChars**](/windows/desktop/api/WebServices/nf-webservices-wswritechars)
-   [**WsWriteCharsUtf8**](/windows/desktop/api/WebServices/nf-webservices-wswritecharsutf8)
-   [**WsWriteEndAttribute**](/windows/desktop/api/WebServices/nf-webservices-wswriteendattribute)
-   [**WsWriteEndCData**](/windows/desktop/api/WebServices/nf-webservices-wswriteendcdata)
-   [**WsWriteEndElement**](/windows/desktop/api/WebServices/nf-webservices-wswriteendelement)
-   [**WsWriteNode**](/windows/desktop/api/WebServices/nf-webservices-wswritenode)
-   [**WsWriteQualifiedName**](/windows/desktop/api/WebServices/nf-webservices-wswritequalifiedname)
-   [**WsWriteStartAttribute**](/windows/desktop/api/WebServices/nf-webservices-wswritestartattribute)
-   [**WsWriteStartCData**](/windows/desktop/api/WebServices/nf-webservices-wswritestartcdata)
-   [**WsWriteStartElement**](/windows/desktop/api/WebServices/nf-webservices-wswritestartelement)
-   [**WsWriteText**](/windows/desktop/api/WebServices/nf-webservices-wswritetext)
-   [**WsWriteValue**](/windows/desktop/api/WebServices/nf-webservices-wswritevalue)
-   [**WsWriteXmlnsAttribute**](/windows/desktop/api/WebServices/nf-webservices-wswritexmlnsattribute)

The following handle is used with the XML writer:

-   [WS\_XML\_WRITER](ws-xml-writer.md)

The following structures are used with the XML writer:

-   [**WS\_XML\_WRITER\_BINARY\_ENCODING**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_writer_binary_encoding)
-   [**WS\_XML\_WRITER\_BUFFER\_OUTPUT**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_writer_buffer_output)
-   [**WS\_XML\_WRITER\_ENCODING**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_writer_encoding)
-   [**WS\_XML\_WRITER\_MTOM\_ENCODING**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_writer_mtom_encoding)
-   [**WS\_XML\_WRITER\_OUTPUT**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_writer_output)
-   [**WS\_XML\_WRITER\_PROPERTIES**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_writer_properties)
-   [**WS\_XML\_WRITER\_PROPERTY**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_writer_property)
-   [**WS\_XML\_WRITER\_STREAM\_OUTPUT**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_writer_stream_output)
-   [**WS\_XML\_WRITER\_TEXT\_ENCODING**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_writer_text_encoding)

 

 




