---
description: The package interfaces represent the top level of the XPS OM, which corresponds to an XPS document file.
ms.assetid: 9e269b18-e5b1-4801-b8e7-473750443c6d
title: XPS OM Package Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# XPS OM Package Interfaces

The package interfaces represent the top level of the XPS OM, which corresponds to an XPS document file. These interfaces contain methods that serialize an XPS OM to an XPS document or stream, and deserialize an XPS package to create an XPS OM that enables a program to access the contents of a document.



| Interface name                                                  | Logical child interfaces                                                                                                            | Description                                                                                    |
|-----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| [**IXpsOMPackage**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompackage)<br/>               | [**IXpsOMDocumentSequence**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomdocumentsequence)<br/> [**IXpsOMCoreProperties**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomcoreproperties)<br/> | The complete XPS OM that corresponds to the package that contains the XPS document.<br/> |
| [**IXpsOMPackageWriter**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompackagewriter)<br/>   | None<br/>                                                                                                                     | Enables incremental serialization of document pages to a package.<br/>                   |
| [**IXpsOMCoreProperties**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomcoreproperties)<br/> | None<br/>                                                                                                                     | Accesses the document metadata. <br/>                                                    |



 

## Code Examples

The code examples that follow illustrate how some of the package interfaces are used by a program. Unless noted otherwise, all italicized items are parameter names.

-   [Read an XPS document into an XPS OM](#read-an-xps-document-into-an-xps-om)
-   [Write an XPS OM to an XPS document file](#write-an-xps-om-to-an-xps-document-file)
-   [Access the document sequence of the XPS OM](#access-the-document-sequence-of-the-xps-om)
-   [Access the document's CoreProperties](#access-the-documents-coreproperties)

### Read an XPS document into an XPS OM

From an existing XPS document whose file name is stored in *xpsDocumentFilename*, this code example creates an XPS OM that is referenced by *xpsPackage*.


```C++
    HRESULT                 hr = S_OK;
    IXpsOMPackage           *xpsPackage;

    hr = xpsFactory->CreatePackageFromFile(
        xpsDocumentFilename,
        FALSE,
        &xpsPackage);

    // xpsPackage now contains a pointer to the IXpsOMPackage
    // object that has been populated with the contents
    // of the XPS document in xpsDocumentFilename.
```



### Write an XPS OM to an XPS document file

The following code example writes the XPS OM that is referenced by *xpsPackage*. The example creates an XPS document in the file whose name is stored in *fileName*.


```C++
    HRESULT hr = S_OK;

    hr = xpsPackage->WriteToFile(
        xpsDocumentFilename,
        NULL,                    // LPSECURITY_ATTRIBUTES
        FILE_ATTRIBUTE_NORMAL,
        FALSE);                  // optimizeMarkupSize
```



### Access the document sequence of the XPS OM

The following code example obtains a pointer to the [**IXpsOMDocumentSequence**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomdocumentsequence) interface, which contains the document sequence of the XPS OM that is represented by *xpsPackage*.


```C++
    HRESULT                         hr = S_OK;
    IXpsOMDocumentSequence          *docSeq;
    IXpsOMDocumentCollection        *docs;

    // get the fixed document sequence of the package
    hr = xpsPackage->GetDocumentSequence(&docSeq);

    // get the collection of fixed documents in 
    //  the fixed document sequence
    hr = docSeq->GetDocuments(&docs);
```



### Access the document's CoreProperties

The following is code example obtains a pointer to the [**IXpsOMCoreProperties**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomcoreproperties) interface, allowing the program to access the contents of the CoreProperties part. In the example, the document is assumed to have been read into an XPS OM that is represented by *xpsPackage*.


```C++
    HRESULT                         hr = S_OK;
    IXpsOMCoreProperties            *coreProps;
    LPWSTR                          title;

    // get the fixed document sequence of the package
    hr = xpsPackage->GetCoreProperties(&coreProps);

    // get the title property 
    hr = coreProps->GetTitle(&title);

    // do something with the title property here...

    // free the string when finished with it
    CoTaskMemFree ( title );
    coreProps->Release();
```



## Related topics

<dl> <dt>

[Using the IXpsOMPackageWriter Interface](using-the-ixpsompackagewriter-interface.md)
</dt> <dt>

[Navigate the XPS OM](navigate-the-xps-om.md)
</dt> <dt>

[**IXpsOMDocumentSequence Interface**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomdocumentsequence)
</dt> <dt>

[**IXpsOMPackage Interface**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompackage)
</dt> <dt>

[**IXpsOMPackageWriter Interface**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompackagewriter)
</dt> <dt>

[**IXpsOMCoreProperties Interface**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomcoreproperties)
</dt> </dl>

 

 




