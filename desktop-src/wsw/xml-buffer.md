---
title: XML Buffer
description: An XML Buffer provides efficient in-memory storage for arbitrary XML data.
ms.assetid: 'e379628b-c6f8-48b1-8109-59fb604f2bcb'
keywords:
- XML Buffer Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# XML Buffer

An XML Buffer provides efficient in-memory storage for arbitrary XML data.


To read data from an XML Buffer, use a [XML Reader](xml-reader.md) and call [**WsSetInputToBuffer**](/windows/desktop/api/WebServices/nf-webservices-wssetinputtobuffer) with the XML Buffer. The reader will be positioned at the start of the document.

To insert data into a buffer, use a [XML Writer](xml-writer.md) and call [**WsSetOutputToBuffer**](/windows/desktop/api/WebServices/nf-webservices-wssetoutputtobuffer) with the XML Buffer. The writer will be positioned at the end of the document.

Once a reader has been set to an XML Buffer, in addition to all of the XML Reader APIs, [**WsMoveReader**](/windows/desktop/api/WebServices/nf-webservices-wsmovereader) may be used to navigate the reader through the document. [**WsGetReaderPosition**](/windows/desktop/api/WebServices/nf-webservices-wsgetreaderposition) and [**WsSetReaderPosition**](/windows/desktop/api/WebServices/nf-webservices-wssetreaderposition) may also be used to record a position in the document and return to it later.

Once a writer has been set to an XML Buffer, in addition to all of the XML Writer APIs, [**WsMoveWriter**](/windows/desktop/api/WebServices/nf-webservices-wsmovewriter) may be used to navigate the writer through the document. [**WsGetWriterPosition**](/windows/desktop/api/WebServices/nf-webservices-wsgetwriterposition) and [**WsSetWriterPosition**](/windows/desktop/api/WebServices/nf-webservices-wssetwriterposition) may also be used to record a position in the document and return to it later. The writer always inserts data before the node to which it is positioned.

Nodes may be deleted from the XML Buffer by obtaining the position of the node using [**WsGetReaderPosition**](/windows/desktop/api/WebServices/nf-webservices-wsgetreaderposition) or [**WsGetWriterPosition**](/windows/desktop/api/WebServices/nf-webservices-wsgetwriterposition) and then calling [**WsRemoveNode**](/windows/desktop/api/WebServices/nf-webservices-wsremovenode) with that position. For elements, this will delete the element, all its children including its matching end element.

A position is represented by the value [**WS\_XML\_NODE\_POSITION**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_node_position). Positions are specific to a particular XML Buffer, and are only valid as long as the XML Buffer is valid.

The following enumerations are used with XML buffers:

-   [**WS\_MOVE\_TO**](/windows/desktop/api/WebServices/ne-webservices-ws_move_to)
-   [**WS\_XML\_BUFFER\_PROPERTY\_ID**](/windows/win32/api/webservices/ne-webservices-ws_xml_reader_property_id)

The following functions are used with XML buffers:

-   [**WsCreateXmlBuffer**](/windows/desktop/api/WebServices/nf-webservices-wscreatexmlbuffer)
-   [**WsRemoveNode**](/windows/desktop/api/WebServices/nf-webservices-wsremovenode)

The following handle is used with XML buffers:

-   [WS\_XML\_BUFFER](ws-xml-buffer.md)

The following structures are used with XML buffers:

-   [**WS\_XML\_BUFFER\_PROPERTY**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_buffer_property)
-   [**WS\_XML\_NODE\_POSITION**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_node_position)

 

 




