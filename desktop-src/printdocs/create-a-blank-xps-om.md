---
Description: This topic describes how to create a blank XPS OM.
ms.assetid: 5b6f12ba-9a41-4252-96c4-391bb8d75cd4
title: Create a Blank XPS OM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Create a Blank XPS OM

This topic describes how to create a blank XPS OM. It presents the code examples that illustrate how to use an XPS OM to build the document structure of an XPS document that has one blank page.

To be saved as an XPS document, the XPS OM requires at least the following components:

-   An [**IXpsOMPackage**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompackage) that describes the XPS document package
-   An [**IXpsOMDocumentSequence**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomdocumentsequence) that contains the framework of the package contents
-   An [**IXpsOMDocument**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomdocument) that contains the framework of a document within the package
-   An [**IXpsOMPageReference**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompagereference) that contains the collection of pages in the document
-   An [**IXpsOMPage**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompage) that contains a blank page

When these interfaces are used, the XPS OM will contain a document that has one blank page. To create this document in an XPS OM, the program must first create the individual components and then link them together.

Before using the following code examples, read the disclaimer in [Common XPS Document Programming Tasks](common-xps-document-tasks.md).

## Code Examples

The following code example assumes that the initialization, described in [Initialize an XPS OM](xps-object-model-initialization.md), has succeeded.


```C++
    // Declare the variables used in this section.
    HRESULT                       hr = S_OK;
    IOpcPartUri                   *opcPartUri = NULL;
    IXpsOMPackage                 *xpsPackage = NULL;
    IXpsOMDocumentSequence        *xpsFDS = NULL;
    IXpsOMDocumentCollection      *fixedDocuments = NULL;
    IXpsOMDocument                *xpsFD = NULL;
    IXpsOMPage                    *xpsPage = NULL;
    IXpsOMPageReferenceCollection *pageRefs = NULL;
    IXpsOMPageReference           *xpsPageRef = NULL;
    // These values are set outside of this code example.
    XPS_SIZE pageSize = {width, height}; 
    
    // Create the package.
    hr = xpsFactory->CreatePackage( &amp;xpsPackage );

    // Create the URI for the fixed document sequence part and then  
    //  create the fixed document sequence
    hr = xpsFactory->CreatePartUri( 
        L"/FixedDocumentSequence.fdseq", &amp;opcPartUri );
    hr = xpsFactory->CreateDocumentSequence( opcPartUri, &amp;xpsFDS );
    // Release this URI to reuse the interface pointer.
    if (NULL != opcPartUri) {opcPartUri->Release(); opcPartUri = NULL;}

    // Create the URI for the document part and then create the document.
    hr = xpsFactory->CreatePartUri( 
        L"/Documents/1/FixedDocument.fdoc", &amp;opcPartUri );
    hr = xpsFactory->CreateDocument( opcPartUri, &amp;xpsFD );
    // Release this URI to reuse the interface pointer.
    if (NULL != opcPartUri) {opcPartUri->Release(); opcPartUri = NULL;}

    // Create a blank page.
    hr = xpsFactory->CreatePartUri( 
        L"/Documents/1/Pages/1.fpage", &amp;opcPartUri );
    hr = xpsFactory->CreatePage(
        &amp;pageSize,                  // Page size
        L"en-US",                   // Page language
        opcPartUri,                 // Page part name
        &amp;xpsPage);                
    // Release this URI to reuse the interface pointer.
    if (NULL != opcPartUri) {opcPartUri->Release(); opcPartUri = NULL;}

    // Create a page reference for the page.
    hr = xpsFactory->CreatePageReference( &amp;pageSize, &amp;xpsPageRef );

    // Add the fixed document sequence to the package.
    hr = xpsPackage->SetDocumentSequence( xpsFDS );

    // Get the document collection of the fixed document sequence
    //  and then add the document to the collection.
    hr = xpsFDS->GetDocuments( &amp;fixedDocuments );
    hr = fixedDocuments->Append( xpsFD );

    // Get the page reference collection from the document
    //  and add the page reference and blank page.
    hr = xpsFD->GetPageReferences( &amp;pageRefs );
    hr = pageRefs->Append( xpsPageRef );
    hr = xpsPageRef->SetPage( xpsPage );

    // Release interface pointer
    if (NULL != xpsPage) xpsPage->Release();
    if (NULL != pageRefs) pageRefs->Release();
    if (NULL != fixedDocuments) fixedDocuments->Release();
    if (NULL != xpsPageRef) xpsPageRef->Release();
    if (NULL != xpsFD) xpsFD->Release();
    if (NULL != xpsFDS) xpsFDS->Release();
    if (NULL != xpsPackage) xpsPackage->Release();

```



## Best Practices

After you have used an [**IOpcPartUri**](https://msdn.microsoft.com/library/windows/desktop/dd371083) interface to create a component (such as after calling the **CreateDocument** method in the code example), release the pointer to that interface—unless you need it for another call.

## Related topics

<dl> <dt>

**Next Steps**
</dt> <dt>

[Navigate the XPS OM](navigate-the-xps-om.md)
</dt> <dt>

[Write Text to an XPS OM](write-text-to-an-xps-om.md)
</dt> <dt>

[Draw Graphics in an XPS OM](draw-graphics-in-an-xps-om.md)
</dt> <dt>

[Place Images in an XPS OM](place-images-in-an-xps-om.md)
</dt> <dt>

**Used in This Page**
</dt> <dt>

[**IOpcPartUri**](https://msdn.microsoft.com/library/windows/desktop/dd371083)
</dt> <dt>

[**IXpsOMObjectFactory**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomobjectfactory)
</dt> <dt>

[**IXpsOMPackage**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompackage)
</dt> <dt>

[**IXpsOMDocumentSequence**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomdocumentsequence)
</dt> <dt>

[**IXpsOMDocumentCollection**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomdocumentcollection)
</dt> <dt>

[**IXpsOMDocument**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomdocument)
</dt> <dt>

[**IXpsOMPage**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompage)
</dt> <dt>

[**IXpsOMPageReference**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompagereference)
</dt> <dt>

[**IXpsOMPageReferenceCollection**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompagereferencecollection)
</dt> <dt>

[**XPS\_SIZE**](/windows/desktop/api/xpsobjectmodel/ns-xpsobjectmodel-__midl___midl_itf_xpsobjectmodel_0000_0000_0018)
</dt> <dt>

**For More Information**
</dt> <dt>

[Initialize an XPS OM](xps-object-model-initialization.md)
</dt> <dt>

[Packaging API](https://msdn.microsoft.com/library/windows/desktop/dd371623)
</dt> <dt>

[XPS Document API Reference](xps-programming-reference.md)
</dt> <dt>

[XML Paper Specification](http://go.microsoft.com/?linkid=8435939)
</dt> </dl>

 

 



