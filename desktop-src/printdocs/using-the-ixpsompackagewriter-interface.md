---
description: The IXpsOMPackageWriter interface creates an XPS document file into which applications can write the contents of the IXpsOMPage interfaces of an XPS OM.
ms.assetid: eff1ab1e-2205-4f5c-9e32-199e073f5dbf
title: Using the IXpsOMPackageWriter Interface
ms.topic: article
ms.date: 05/31/2018
---

# Using the IXpsOMPackageWriter Interface

The [**IXpsOMPackageWriter**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompackagewriter) interface creates an XPS document file into which applications can write the contents of the [**IXpsOMPage**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompage) interfaces of an XPS OM. The [**IXpsOMPackageWriter**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompackagewriter) interface is most useful when document contents are being processed or created sequentially. Unlike the [**WriteToFile**](/windows/desktop/api/xpsobjectmodel/nf-xpsobjectmodel-ixpsompackage-writetofile) and [**WriteToStream**](/windows/desktop/api/xpsobjectmodel/nf-xpsobjectmodel-ixpsompackage-writetostream) methods of the [**IXpsOMPackage**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompackage) interface, for the **IXpsOMPackageWriter** interface to be used neither the entire FixedDocument nor the FixedDocumentSequence has to be finished.

## Overview

The [**IXpsOMPackageWriter**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompackagewriter) interface writes one page at a time, from the first page of an XPS document to the last. The interface can be used to create simple XPS document files and also complex XPS document files that contain more than one FixedDocument in the FixedDocumentSequence. In complex XPS document files, the FixedDocuments are also created in sequence, starting with the first FixedDocument in the FixedDocumentSequence. The **IXpsOMPackageWriter** interface does not support the creation of document contents in random order. Use it, for example, to create a sequential report or to perform processing in a device driver filter where the document contents are fed to the driver in sequence.

## Terminology Review

An *XPS document file* is an Open Packaging Conventions (OPC) package that conforms to the XML Paper Specification. So, technically, the [**IXpsOMPackageWriter**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompackagewriter) interface creates an *OPC package*, but it is an OPC package that conforms to the XML Paper Specification. For this reason, in discussions about XPS documents, the terms *XPS document* and *package* are often used interchangeably.

The *package* created by the [**IXpsOMPackageWriter**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompackagewriter) interface will contain the required XPS document components: a FixedDocumentSequence, at least one FixedDocument, and at least one FixedPage. The FixedDocumentSequence is created when the **IXpsOMPackageWriter** interface is instantiated. A FixedDocument is created every time [**IXpsOMPackageWriter::StartNewDocument**](/windows/desktop/api/xpsobjectmodel/nf-xpsobjectmodel-ixpsompackagewriter-startnewdocument) is called, and a FixedPage is created every time [**IXpsOMPackageWriter::AddPage**](/windows/desktop/api/xpsobjectmodel/nf-xpsobjectmodel-ixpsompackagewriter-addpage) is called. Because the interface writes the document contents sequentially, the **AddPage** method adds the page to the most recently created FixedDocument.

## Using the IXpsOMPackageWriter Interface

The following procedure describes how to create an XPS document file by using the [**IXpsOMPackageWriter**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompackagewriter) interface. The procedure does not describe how to instantiate an [**IXpsOMPage**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompage) interface and its contents. For more information about **IXpsOMPage** and adding content to a page, see [XPS OM Page Interfaces](xps-object-model-page-interfaces.md) and the topics listed in the See Also section.

 **Creating a document**

1.  Instantiate an [**IXpsOMPackageWriter**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompackagewriter) interface.

    This creates an empty FixedDocumentSequence in the package.

    -   To create an XPS document in a file, call [**IXpsOMObjectFactory::CreatePackageWriterOnFile**](/windows/desktop/api/xpsobjectmodel/nf-xpsobjectmodel-ixpsomobjectfactory-createpackagewriteronfile).
    -   To create an XPS document in a stream, call [**IXpsOMObjectFactory::CreatePackageWriterOnStream**](/windows/desktop/api/xpsobjectmodel/nf-xpsobjectmodel-ixpsomobjectfactory-createpackagewriteronstream).

2.  Start a new document in the package by calling [**IXpsOMPackageWriter::StartNewDocument**](/windows/desktop/api/xpsobjectmodel/nf-xpsobjectmodel-ixpsompackagewriter-startnewdocument).

    Before adding a page, call [**IXpsOMPackageWriter::StartNewDocument**](/windows/desktop/api/xpsobjectmodel/nf-xpsobjectmodel-ixpsompackagewriter-startnewdocument) to add a FixedDocument to the FixedDocumentSequence that was created in step 1.

3.  Add content.
    -   To add a new FixedPage to the document, call [**IXpsOMPackageWriter::AddPage**](/windows/desktop/api/xpsobjectmodel/nf-xpsobjectmodel-ixpsompackagewriter-addpage), passing it a pointer to the [**IXpsOMPage**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompage) interface that has the contents of the FixedPage that you want to add.
    -   To create a new FixedDocument in the FixedDocumentSequence, call [**IXpsOMPackageWriter::StartNewDocument**](/windows/desktop/api/xpsobjectmodel/nf-xpsobjectmodel-ixpsompackagewriter-startnewdocument).
4.  Close the package and its contents by calling [**IXpsOMPackageWriter::Close**](/windows/desktop/api/xpsobjectmodel/nf-xpsobjectmodel-ixpsompackagewriter-close).

## Advanced Features

The methods of the [**IXpsOMPackageWriter**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompackagewriter) interface also support the adding of resources, thumbnails, and print tickets. These document components can be added at the package, FixedDocumentSequence, FixedDocument, and FixedPage levels. For more information about using this interface for printing, see [Print an XPS OM](print-an-xps-om.md).

## Related topics

<dl> <dt>

[Using XPS Digital Signature API](using-digital-signatures-in-xps-documents.md)
</dt> <dt>

[XPS OM Page Interfaces](xps-object-model-page-interfaces.md)
</dt> <dt>

[Navigate the XPS OM](navigate-the-xps-om.md)
</dt> <dt>

[Working with XPS OM Canvas and Visual Interfaces](working-with-xpsomcanvas-interfaces.md)
</dt> <dt>

[Working with XPS OM Path Interfaces](working-with-xps-object-model-path-interfaces.md)
</dt> <dt>

[Working with XPS OM Text, Graphics, and Image Interfaces](working-with-xps-object-model-text-and-image-interfaces.md)
</dt> <dt>

[XPS OM Print Ticket Interfaces](xps-object-model-print-ticket-interfaces.md)
</dt> <dt>

[**IXpsOMThumbnailGenerator**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomthumbnailgenerator)
</dt> <dt>

[XPS Document API Reference](xps-programming-reference.md)
</dt> <dt>

[XML Paper Specification](https://www.ecma-international.org/activities/XML%20Paper%20Specification/XPS%20Standard%20WD%201.6.pdf)
</dt> </dl>

 

 



