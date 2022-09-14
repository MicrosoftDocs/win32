---
description: The XPS Document API implements the XPS object model and enables developers to create an XPS OM, manipulate XPS document content in native Windows \\\\ programs, and save the XPS OM to a file or stream as an XPS document.
ms.assetid: dbb48dae-1ee6-4a8b-9184-8b796755087e
title: About XPS Document API
ms.topic: article
ms.date: 05/31/2018
---

# About XPS Document API

The [XPS Document API](documents-xps.md) implements the XPS object model and enables developers to create an XPS OM, manipulate XPS document content in native Windows \\\\ programs, and save the XPS OM to a file or stream as an XPS document. Developers of XPSDrv filter pipeline modules can also use the XPS Document API to manipulate XPS document content in an XPSDrv printer driver filter.

## XPS Document API Overview

The XPS object model is the information model of an XPS document. The information model of the XPS document is separate from the markup model that is used inside the document parts. The XPS object model describes the organization of the internal components that make up an XPS document, and the markup model describes the contents of those components.

In a program, the XPS object model is instantiated as an XPS OM. The XPS OM is essentially an in-memory version of an XPS document's contents. While similar in logical organization to an XPS document, an XPS OM is not considered an XPS document until it has been serialized to a file or a stream.

The exact structure of the markup is not available to the XPS OM when an XPS document is deserialized from markup to an XPS OM. For example, whether the property was represented as an element or an attribute in the markup, the property value of a document object is presented by the XPS OM in exactly the same way.

The [XPS Document API](documents-xps.md) can be divided into the following categories:

-   [XPS OM Trunk Interfaces](xps-om-trunk-interfaces.md)

    The trunk interfaces provide access to the top-level components of the XPS document structure. These interfaces also provide the means to serialize an XPS OM and deserialize an XPS document.

-   [XPS OM Page Interfaces](xps-object-model-page-interfaces.md)

    The page interfaces provide access to the contents of a page in an XPS document. The interfaces that describe the content of the page are also included with the page interfaces.

-   [XPS OM Digital Signatures](using-the-xps-digital-signatures.md)

    The XPS OM supports digital signatures. However, you can access digital signatures in an XPS document directly without creating an XPS OM. For more information about how to access XPS digital signatures without an XPS OM, see [XPS Digital Signature API](xps-digital-signatures.md).

-   [XPS OM Print Ticket Interfaces](xps-object-model-print-ticket-interfaces.md)

    XPS documents support print tickets at the package (job), document, and page level. Print tickets contain information about how to format document content for printing or viewing.

## Related topics

<dl> <dt>

**In This Section**
</dt> <dt>

[XPS OM Trunk Interfaces](xps-om-trunk-interfaces.md)
</dt> <dt>

[XPS OM Page Interfaces](xps-object-model-page-interfaces.md)
</dt> <dt>

[XPS OM Digital Signatures](using-the-xps-digital-signatures.md)
</dt> <dt>

[XPS OM Print Ticket Interfaces](xps-object-model-print-ticket-interfaces.md)
</dt> <dt>

**Other Related Topics**
</dt> <dt>

[Initialize an XPS OM](xps-object-model-initialization.md)
</dt> <dt>

[XPS OM Digital Signatures](using-the-xps-digital-signatures.md)
</dt> <dt>

[XPS Document API Reference](xps-programming-reference.md)
</dt> <dt>

[XML Paper Specification](https://www.ecma-international.org/activities/XML%20Paper%20Specification/XPS%20Standard%20WD%201.6.pdf)
</dt> </dl>

 

 



