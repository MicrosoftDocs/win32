---
title: XPS OM Canvas and Visual Interfaces
description: This topic describes how to use the canvas-related interfaces of the XPS Document API in an XPS OM.
ms.assetid: 368b8c47-9803-42ee-a3a8-681bf55315ad
ms.topic: article
ms.date: 05/31/2018
---

# Working with XPS OM Canvas and Visual Interfaces

This topic describes how to use the canvas-related interfaces of the XPS Document API in an XPS OM.

| Interface name                                  | Logical child interfaces                                                                                                                    | Description                                                                                                                                                                                                             |
|-------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IXpsOMVisual**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomvisual)<br/> | [**IXpsOMCanvas**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomcanvas)<br/> [**IXpsOMGlyphs**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomglyphs)<br/> [**IXpsOMPath**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompath)<br/> | The base class of the interfaces that define visual objects, such as text and graphics.<br/> Visual objects can be collected in an [**IXpsOMVisualCollection**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomvisualcollection) interface.<br/> |
| [**IXpsOMCanvas**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomcanvas)<br/> | [**IXpsOMCanvas**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomcanvas)<br/> [**IXpsOMGlyphs**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomglyphs)<br/> [**IXpsOMPath**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompath)<br/> | A collection of visual objects that can be treated as a single visual object.<br/>                                                                                                                                |

[**IXpsOMVisual**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomvisual) is the base interface; the visible objects of a page inherit from it. [**IXpsOMCanvas**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomcanvas) inherits from [**IXpsOMVisual**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomvisual) and enables many other visual elements to be grouped and acted upon as a single visual element. For example, you could use an [**IXpsOMCanvas**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomcanvas) interface to create a page banner that contains a collection of text and graphical elements. Such a banner might contain a logo, the company slogan, and the company address. You could place all these elements into the [**IXpsOMVisualCollection**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomvisualcollection) of an [**IXpsOMCanvas**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomcanvas) interface, and then apply a single transform to the [**IXpsOMCanvas**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomcanvas) object to resize it to a particular page. This is much simpler than computing and applying a transform to each individual visual component in the banner.

You can also use a canvas to resize the page contents to fit the current page size. To accomplish this, place all contents of the page into a single canvas, then apply the appropriate transform to fit the canvas to the current page size. This is also much simpler than trying to resize each visual element in the collection of visuals in the page.

## Move page contents to a canvas

The following code example moves the contents of a page to a canvas.

```C++
    HRESULT                   hr = S_OK;

    IXpsOMVisualCollection    *pageVisuals;
    IXpsOMVisualCollection    *canvasVisuals;
    IXpsOMVisual              *oneVisual;
    IXpsOMCanvas              *newPageCanvas;

    UINT32 numVisuals = 0;
    UINT32 thisVisual;

    // get the page's visual collection
    // and how many objects it contains
    hr = page->GetVisuals( &pageVisuals );
    hr = pageVisuals->GetCount ( &numVisuals );

    // create the new canvas object and
    // its (empty) visual collection
    hr = xpsFactory->CreateCanvas ( &newPageCanvas );
    hr = newPageCanvas->GetVisuals ( &canvasVisuals );

    // go through the page's list of visual objects,
    //  move each one from the page's list to the canvas' list
    //  release the local pointer
    //  remove it from the page's collection
    thisVisual = 0;
    while (thisVisual < numVisuals) {
        hr = pageVisuals->GetAt (0, &oneVisual);
        hr = canvasVisuals->Append (oneVisual);
        hr = pageVisuals->RemoveAt (0);
        thisVisual++;
    }
    // the page's visual collection should be empty
    hr = pageVisuals->GetCount (&numVisuals);
    _ASSERT (0 == numVisuals);

    // add the new canvas to the page's visual collection
    pageVisuals->Append ( newPageCanvas );

```

## Related topics

<dl> 
  <dt>[**IXpsOMCanvas Interface**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomcanvas)</dt>
  <dt>[**IXpsOMVisual Interface**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomvisual)</dt>
  <dt>[**IXpsOMVisualCollection Interface**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomvisualcollection)</dt>
</dl>
