---
title: XML Buffer
description: An XML Buffer provides efficient in-memory storage for arbitrary XML data.
ms.assetid: '75f1df70-4dc9-4365-9005-5eaca6688f16'
keywords: ["XML Buffer Web Services for Windows", "WWSAPI", "WWS"]
---

# XML Buffer

An XML Buffer provides efficient in-memory storage for arbitrary XML data.

## 

To read data from an XML Buffer, use a [XML Reader](xml-reader.md) and call [**WsSetInputToBuffer**](wssetinputtobuffer.md) with the XML Buffer. The reader will be positioned at the start of the document.

To insert data into a buffer, use a [XML Writer](xml-writer.md) and call [**WsSetOutputToBuffer**](wssetoutputtobuffer.md) with the XML Buffer. The writer will be positioned at the end of the document.

Once a reader has been set to an XML Buffer, in addition to all of the XML Reader APIs, [**WsMoveReader**](wsmovereader.md) may be used to navigate the reader through the document. [**WsGetReaderPosition**](wsgetreaderposition.md) and [**WsSetReaderPosition**](wssetreaderposition.md) may also be used to record a position in the document and return to it later.

Once a writer has been set to an XML Buffer, in addition to all of the XML Writer APIs, [**WsMoveWriter**](wsmovewriter.md) may be used to navigate the writer through the document. [**WsGetWriterPosition**](wsgetwriterposition.md) and [**WsSetWriterPosition**](wssetwriterposition.md) may also be used to record a position in the document and return to it later. The writer always inserts data before the node to which it is positioned.

Nodes may be deleted from the XML Buffer by obtaining the position of the node using [**WsGetReaderPosition**](wsgetreaderposition.md) or [**WsGetWriterPosition**](wsgetwriterposition.md) and then calling [**WsRemoveNode**](wsremovenode.md) with that position. For elements, this will delete the element, all its children including its matching end element.

A position is represented by the value [**WS\_XML\_NODE\_POSITION**](ws-xml-node-position.md). Positions are specific to a particular XML Buffer, and are only valid as long as the XML Buffer is valid.

The following enumerations are used with XML buffers:

-   [**WS\_MOVE\_TO**](ws-move-to.md)
-   [**WS\_XML\_BUFFER\_PROPERTY\_ID**](ws-xml-buffer-property-id.md)

The following functions are used with XML buffers:

-   [**WsCreateXmlBuffer**](wscreatexmlbuffer.md)
-   [**WsRemoveNode**](wsremovenode.md)

The following handle is used with XML buffers:

-   [WS\_XML\_BUFFER](ws-xml-buffer.md)

The following structures are used with XML buffers:

-   [**WS\_XML\_BUFFER\_PROPERTY**](ws-xml-buffer-property.md)
-   [**WS\_XML\_NODE\_POSITION**](ws-xml-node-position.md)

 

 




