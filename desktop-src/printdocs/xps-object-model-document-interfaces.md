---
description: The document interfaces provide access to the XPS package components that determine the structure of a document in an XPS OM.
ms.assetid: 3302d164-81ad-4198-a116-f967e7a14147
title: XPS OM Document Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# XPS OM Document Interfaces

The document interfaces provide access to the XPS package components that determine the structure of a document in an XPS OM. The following table lists the document interfaces.



| Interface name                                                      | Logical child interfaces                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                   |
|---------------------------------------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IXpsOMDocumentSequence**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomdocumentsequence)<br/> | [**IXpsOMDocument**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomdocument)<br/>           | Represents a set of documents that are bound together in an ordered list.<br/> Child interfaces are collected in an [**IXpsOMDocumentCollection**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomdocumentcollection) interface.<br/>                                                                                                                                                                                                  |
| [**IXpsOMDocument**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomdocument)<br/>                 | [**IXpsOMPageReference**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompagereference)<br/> | Represents a single FixedDocument part and binds together the collection of page references of the pages in a document.<br/> Child interfaces are collected in an [**IXpsOMPageReferenceCollection**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompagereferencecollection) interface.<br/> The document structure is exposed in an [**IXpsOMDocumentStructureResource**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomdocumentstructureresource) interface.<br/> |
| [**IXpsOMPageReference**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompagereference)<br/>       | [**IXpsOMPage**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompage)<br/>                   | A light-weight virtualized version of a page in the document. A page reference describes the core characteristics of the page (such as its dimensions) but does not include any of the page's content.<br/>                                                                                                                                                                                             |
| [**IXpsOMNameCollection**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomnamecollection)<br/>     | None<br/>                                               | A collection of the page's objects that are hyperlink targets.<br/>                                                                                                                                                                                                                                                                                                                                     |
| [**IXpsOMPartResources**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompartresources)<br/>       | None<br/>                                               | A collection of the part resources that are associated with a page.<br/>                                                                                                                                                                                                                                                                                                                                |



 

## Contents

-   [Working with IXpsOMDocumentSequence Interfaces](working-with-xpsomdocumentsequence-interfaces.md) contains information about using the following interfaces:
    -   [**IXpsOMDocumentSequence**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomdocumentsequence)
    -   [**IXpsOMDocumentCollection**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomdocumentcollection)
-   [Working with IXpsOMDocument Interfaces](working-with-xpsomdocument-interfaces.md) contains information about using the following interfaces:
    -   [**IXpsOMDocument**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomdocument)
    -   [**IXpsOMPageReferenceCollection**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompagereferencecollection)
    -   [**IXpsOMDocumentStructureResource**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomdocumentstructureresource)
-   [Working with IXpsOMPageReference Interfaces](working-with-xpsompagereference-interfaces.md) contains information about using the following interfaces:
    -   [**IXpsOMPageReference**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompagereference)
    -   [**IXpsOMPage**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompage)
    -   [**IXpsOMNameCollection**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomnamecollection)
    -   [**IXpsOMPartResources**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompartresources)

 

 




