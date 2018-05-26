---
title: XML Writer
description: XML Writer is an API for emitting XML. At its core, an XML Writer writes one XML Node at a time, but there are additional helper APIs to make writing a sequence of nodes easier.
ms.assetid: 8f413e60-8a30-492c-8f2d-80be511fee11
keywords:
- XML Writer Web Services for Windows
- WWSAPI
- WWS
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# XML Writer

XML Writer is an API for emitting XML. At its core, an XML Writer writes one [XML Node](xml-node.md) at a time, but there are additional helper APIs to make writing a sequence of nodes easier.

## 

The following types of writer output are supported:

-   [**An in-memory buffer of encoded bytes**](/windows/win32/WebServices/ns-webservices-_ws_xml_writer_buffer_output?branch=master)
-   [**A stream**](/windows/win32/WebServices/ns-webservices-_ws_xml_writer_stream_output?branch=master)
-   An [XML Buffer](xml-buffer.md)

The following callbacks are used with the XML writer:

-   [**WS\_DYNAMIC\_STRING\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_dynamic_string_callback?branch=master)
-   [**WS\_PULL\_BYTES\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_pull_bytes_callback?branch=master)
-   [**WS\_PUSH\_BYTES\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_push_bytes_callback?branch=master)
-   [**WS\_WRITE\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_write_callback?branch=master)

The following enumerations are used with the XML writer:

-   [**WS\_CHARSET**](/windows/win32/WebServices/ne-webservices-ws_charset?branch=master)
-   [**WS\_XML\_WRITER\_ENCODING\_TYPE**](/windows/win32/WebServices/ne-webservices-ws_xml_writer_encoding_type?branch=master)
-   [**WS\_XML\_WRITER\_OUTPUT\_TYPE**](/windows/win32/WebServices/ne-webservices-ws_xml_writer_output_type?branch=master)
-   [**WS\_XML\_WRITER\_PROPERTY\_ID**](/windows/win32/WebServices/ne-webservices-ws_xml_writer_property_id?branch=master)

The following functions are used with the XML writer:

-   [**WsCopyNode**](/windows/win32/WebServices/nf-webservices-wscopynode?branch=master)
-   [**WsCreateWriter**](/windows/win32/WebServices/nf-webservices-wscreatewriter?branch=master)
-   [**WsFlushWriter**](/windows/win32/WebServices/nf-webservices-wsflushwriter?branch=master)
-   [**WsFreeWriter**](/windows/win32/WebServices/nf-webservices-wsfreewriter?branch=master)
-   [**WsGetPrefixFromNamespace**](/windows/win32/WebServices/nf-webservices-wsgetprefixfromnamespace?branch=master)
-   [**WsGetWriterPosition**](/windows/win32/WebServices/nf-webservices-wsgetwriterposition?branch=master)
-   [**WsGetWriterProperty**](/windows/win32/WebServices/nf-webservices-wsgetwriterproperty?branch=master)
-   [**WsMoveWriter**](/windows/win32/WebServices/nf-webservices-wsmovewriter?branch=master)
-   [**WsPullBytes**](/windows/win32/WebServices/nf-webservices-wspullbytes?branch=master)
-   [**WsPushBytes**](/windows/win32/WebServices/nf-webservices-wspushbytes?branch=master)
-   [**WsSetOutput**](/windows/win32/WebServices/nf-webservices-wssetoutput?branch=master)
-   [**WsSetOutputToBuffer**](/windows/win32/WebServices/nf-webservices-wssetoutputtobuffer?branch=master)
-   [**WsSetWriterPosition**](/windows/win32/WebServices/nf-webservices-wssetwriterposition?branch=master)
-   [**WsWriteArray**](/windows/win32/WebServices/nf-webservices-wswritearray?branch=master)
-   [**WsWriteBytes**](/windows/win32/WebServices/nf-webservices-wswritebytes?branch=master)
-   [**WsWriteChars**](/windows/win32/WebServices/nf-webservices-wswritechars?branch=master)
-   [**WsWriteCharsUtf8**](/windows/win32/WebServices/nf-webservices-wswritecharsutf8?branch=master)
-   [**WsWriteEndAttribute**](/windows/win32/WebServices/nf-webservices-wswriteendattribute?branch=master)
-   [**WsWriteEndCData**](/windows/win32/WebServices/nf-webservices-wswriteendcdata?branch=master)
-   [**WsWriteEndElement**](/windows/win32/WebServices/nf-webservices-wswriteendelement?branch=master)
-   [**WsWriteNode**](/windows/win32/WebServices/nf-webservices-wswritenode?branch=master)
-   [**WsWriteQualifiedName**](/windows/win32/WebServices/nf-webservices-wswritequalifiedname?branch=master)
-   [**WsWriteStartAttribute**](/windows/win32/WebServices/nf-webservices-wswritestartattribute?branch=master)
-   [**WsWriteStartCData**](/windows/win32/WebServices/nf-webservices-wswritestartcdata?branch=master)
-   [**WsWriteStartElement**](/windows/win32/WebServices/nf-webservices-wswritestartelement?branch=master)
-   [**WsWriteText**](/windows/win32/WebServices/nf-webservices-wswritetext?branch=master)
-   [**WsWriteValue**](/windows/win32/WebServices/nf-webservices-wswritevalue?branch=master)
-   [**WsWriteXmlnsAttribute**](/windows/win32/WebServices/nf-webservices-wswritexmlnsattribute?branch=master)

The following handle is used with the XML writer:

-   [WS\_XML\_WRITER](ws-xml-writer.md)

The following structures are used with the XML writer:

-   [**WS\_XML\_WRITER\_BINARY\_ENCODING**](/windows/win32/WebServices/ns-webservices-_ws_xml_writer_binary_encoding?branch=master)
-   [**WS\_XML\_WRITER\_BUFFER\_OUTPUT**](/windows/win32/WebServices/ns-webservices-_ws_xml_writer_buffer_output?branch=master)
-   [**WS\_XML\_WRITER\_ENCODING**](/windows/win32/WebServices/ns-webservices-_ws_xml_writer_encoding?branch=master)
-   [**WS\_XML\_WRITER\_MTOM\_ENCODING**](/windows/win32/WebServices/ns-webservices-_ws_xml_writer_mtom_encoding?branch=master)
-   [**WS\_XML\_WRITER\_OUTPUT**](/windows/win32/WebServices/ns-webservices-_ws_xml_writer_output?branch=master)
-   [**WS\_XML\_WRITER\_PROPERTIES**](/windows/win32/WebServices/ns-webservices-_ws_xml_writer_properties?branch=master)
-   [**WS\_XML\_WRITER\_PROPERTY**](/windows/win32/WebServices/ns-webservices-_ws_xml_writer_property?branch=master)
-   [**WS\_XML\_WRITER\_STREAM\_OUTPUT**](/windows/win32/WebServices/ns-webservices-_ws_xml_writer_stream_output?branch=master)
-   [**WS\_XML\_WRITER\_TEXT\_ENCODING**](/windows/win32/WebServices/ns-webservices-_ws_xml_writer_text_encoding?branch=master)

 

 




