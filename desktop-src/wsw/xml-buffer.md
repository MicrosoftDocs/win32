---
title: XML Buffer
description: An XML Buffer provides efficient in-memory storage for arbitrary XML data.
ms.assetid: 75f1df70-4dc9-4365-9005-5eaca6688f16
keywords:
- XML Buffer Web Services for Windows
- WWSAPI
- WWS
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# XML Buffer

An XML Buffer provides efficient in-memory storage for arbitrary XML data.

## 

To read data from an XML Buffer, use a [XML Reader](xml-reader.md) and call [**WsSetInputToBuffer**](/windows/win32/WebServices/nf-webservices-wssetinputtobuffer?branch=master) with the XML Buffer. The reader will be positioned at the start of the document.

To insert data into a buffer, use a [XML Writer](xml-writer.md) and call [**WsSetOutputToBuffer**](/windows/win32/WebServices/nf-webservices-wssetoutputtobuffer?branch=master) with the XML Buffer. The writer will be positioned at the end of the document.

Once a reader has been set to an XML Buffer, in addition to all of the XML Reader APIs, [**WsMoveReader**](/windows/win32/WebServices/nf-webservices-wsmovereader?branch=master) may be used to navigate the reader through the document. [**WsGetReaderPosition**](/windows/win32/WebServices/nf-webservices-wsgetreaderposition?branch=master) and [**WsSetReaderPosition**](/windows/win32/WebServices/nf-webservices-wssetreaderposition?branch=master) may also be used to record a position in the document and return to it later.

Once a writer has been set to an XML Buffer, in addition to all of the XML Writer APIs, [**WsMoveWriter**](/windows/win32/WebServices/nf-webservices-wsmovewriter?branch=master) may be used to navigate the writer through the document. [**WsGetWriterPosition**](/windows/win32/WebServices/nf-webservices-wsgetwriterposition?branch=master) and [**WsSetWriterPosition**](/windows/win32/WebServices/nf-webservices-wssetwriterposition?branch=master) may also be used to record a position in the document and return to it later. The writer always inserts data before the node to which it is positioned.

Nodes may be deleted from the XML Buffer by obtaining the position of the node using [**WsGetReaderPosition**](/windows/win32/WebServices/nf-webservices-wsgetreaderposition?branch=master) or [**WsGetWriterPosition**](/windows/win32/WebServices/nf-webservices-wsgetwriterposition?branch=master) and then calling [**WsRemoveNode**](/windows/win32/WebServices/nf-webservices-wsremovenode?branch=master) with that position. For elements, this will delete the element, all its children including its matching end element.

A position is represented by the value [**WS\_XML\_NODE\_POSITION**](/windows/win32/WebServices/ns-webservices-_ws_xml_node_position?branch=master). Positions are specific to a particular XML Buffer, and are only valid as long as the XML Buffer is valid.

The following enumerations are used with XML buffers:

-   [**WS\_MOVE\_TO**](/windows/win32/WebServices/ne-webservices-ws_move_to?branch=master)
-   [**WS\_XML\_BUFFER\_PROPERTY\_ID**](/windows/win32/WebServices/ne-webservices-__unnamed_enum_0?branch=master)

The following functions are used with XML buffers:

-   [**WsCreateXmlBuffer**](/windows/win32/WebServices/nf-webservices-wscreatexmlbuffer?branch=master)
-   [**WsRemoveNode**](/windows/win32/WebServices/nf-webservices-wsremovenode?branch=master)

The following handle is used with XML buffers:

-   [WS\_XML\_BUFFER](ws-xml-buffer.md)

The following structures are used with XML buffers:

-   [**WS\_XML\_BUFFER\_PROPERTY**](/windows/win32/WebServices/ns-webservices-_ws_xml_buffer_property?branch=master)
-   [**WS\_XML\_NODE\_POSITION**](/windows/win32/WebServices/ns-webservices-_ws_xml_node_position?branch=master)

 

 




