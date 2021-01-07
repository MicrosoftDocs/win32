---
description: This topic describes how to use the page-level interfaces that provide access to the contents of a page in an XPS OM.
ms.assetid: 7127ee28-eca9-4e0e-a27a-9051eb105b27
title: Working with XPS OM Page Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Working with XPS OM Page Interfaces

This topic describes how to use the page-level interfaces that provide access to the contents of a page in an XPS OM.



| Interface name                                                                                                                                                                              | Logical child interfaces                                                                                                                                                                                            | Description                                                                                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IXpsOMPage**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompage)<br/>                                                                                                                                                 | [**IXpsOMCanvas**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomcanvas)<br/> [**IXpsOMGlyphs**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomglyphs)<br/> [**IXpsOMPath**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompath)<br/>                                                                         | The root object of the page contents.<br/> This object represents a document part.<br/>                                                |
| [**IXpsOMShareable**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomshareable)<br/>                                                                                                                                       | [**IXpsOMVisual**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomvisual)<br/> [**IXpsOMMatrixTransform**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsommatrixtransform)<br/> [**IXpsOMGeometry**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomgeometry)<br/> [**IXpsOMBrush**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsombrush)<br/> | Interfaces that derive from the [**IXpsOMShareable**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomshareable) interface can be stored in a resource dictionary and shared.<br/> |
| [**IXpsOMRemoteDictionaryResource**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomremotedictionaryresource)<br/> [**IXpsOMRemoteDictionaryResourceCollection**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomremotedictionaryresourcecollection)<br/> | [**IXpsOMDictionary**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomdictionary)<br/>                                                                                                                                                             | Contains a resource dictionary.<br/>                                                                                                         |
| [**IXpsOMDictionary**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomdictionary)<br/>                                                                                                                                     | None<br/>                                                                                                                                                                                                     | References the resources that are shared by other objects.<br/>                                                                              |
| [**IXpsOMStoryFragmentsResource**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomstoryfragmentsresource)<br/>                                                                                                             | None<br/>                                                                                                                                                                                                     | Provides access to the content of the resource stream of the StoryFragments part of the document.<br/>                                       |



 

## Related topics

<dl> <dt>

[**IXpsOMDictionary Interface**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomdictionary)
</dt> <dt>

[**IXpsOMDocumentStructureResource**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomdocumentstructureresource)
</dt> <dt>

[**IXpsOMPage Interface**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompage)
</dt> <dt>

[**IXpsOMRemoteDictionaryResource Interface**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomremotedictionaryresource)
</dt> <dt>

[**IXpsOMRemoteDictionaryResourceCollection Interface**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomremotedictionaryresourcecollection)
</dt> <dt>

[**IXpsOMStoryFragmentsResource Interface**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomstoryfragmentsresource)
</dt> </dl>

 

 




