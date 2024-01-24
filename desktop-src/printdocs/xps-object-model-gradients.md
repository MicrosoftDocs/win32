---
description: This topic provides an example of using gradients in an XPS OM.
ms.assetid: c58c9e5a-c871-4b44-a1be-0aceafa2f805
title: XPS OM Gradients
ms.topic: article
ms.date: 05/31/2018
---

# XPS OM Gradients

This topic provides an example of using gradients in an XPS OM.

## Add a new stop to an existing gradient

The following code example adds a new stop to the gradient of a linear-gradient brush.


```C++
    // brush is the pointer to the gradient brush that will get 
    //  the new gradient and is initialized outside of this code example

    // this is the start of the method that updates the brush
    HRESULT                           hr = S_OK;
    XPS_COLOR                         xpsColorStop;
    IXpsOMGradientStopCollection      *stops;
    IXpsOMGradientStop                *xpsNewGradientStop = NULL, *thisStop = NULL, *nextStop = NULL;
    UINT32                            thisStopIdx, numStops;
    FLOAT                             thisStopOffset, nextStopOffset, newStopOffset;
    BOOL                              bUpdated = FALSE;

    // define the new stop color to be yellow
    xpsColorStop.colorType        = XPS_COLOR_TYPE_SRGB;
    xpsColorStop.value.sRGB.alpha = 0xFF;
    xpsColorStop.value.sRGB.red   = 0xFF;
    xpsColorStop.value.sRGB.green = 0xFF;
    xpsColorStop.value.sRGB.blue  = 0x00;
    
    // create a new gradient stop by setting the color and location 
    // this stop will be half way between the start and end point
    newStopOffset = 0.5f;
    hr = xpsFactory->CreateGradientStop(&xpsColorStop, NULL, newStopOffset, &xpsNewGradientStop);

    // get the collection of gradient stops from the brush
    hr = brush->GetGradientStops (&stops);

    hr = stops->GetCount (&numStops);
    // there will never be less than two stops
    
    // insert the new stop so that the stops are sorted by offset
    // if an existing stop has the same offset as the new one,
    // overwrite the existing stop with the new stop.
    for (thisStopIdx = 0; thisStopIdx < (numStops-1); thisStopIdx++) {
        hr = stops->GetAt(thisStopIdx, &thisStop);
        hr = stops->GetAt(thisStopIdx+1, &nextStop);
    
        hr = thisStop->GetOffset (&thisStopOffset);
        hr = nextStop->GetOffset (&nextStopOffset);

        if (newStopOffset < thisStopOffset) {
            // insert at thisStopIdx
            stops->InsertAt(thisStopIdx, xpsNewGradientStop);
            bUpdated = TRUE;
            break; // done, so leave loop
        } 
        if ((newStopOffset > thisStopOffset) && (newStopOffset < nextStopOffset)) {
            // the new stop goes in between them
            stops->InsertAt (thisStopIdx+1, xpsNewGradientStop);
            bUpdated = TRUE;
            break; // done, so leave loop
        } 

        if (newStopOffset == thisStopOffset ) {
            // then overwrite the old one
            stops->SetAt (thisStopIdx, xpsNewGradientStop);
            bUpdated = TRUE;
            break; // done, so leave loop
        }

        if (newStopOffset == nextStopOffset ) {
            // then overwrite the old one
            stops->SetAt (thisStopIdx+1, xpsNewGradientStop);
            bUpdated = TRUE;
            break; // done, so leave loop
        }

        // on the last entry, see if this stop is greater than the last entry
        // in the collection. If so, append the new one to the end.
        if ((thisStopIdx == (numStops-2)) && (newStopOffset > nextStopOffset )) {
            // then overwrite the old one
            stops->Append ( xpsNewGradientStop );
            bUpdated = TRUE;
            break; // done, so leave loop
        }
        if (NULL != thisStop) {thisStop->Release(); thisStop = NULL;}
        if (NULL != nextStop) {nextStop->Release(); nextStop = NULL;}
    }
    if (NULL != thisStop) {thisStop->Release(); thisStop = NULL;}
    if (NULL != nextStop) {nextStop->Release(); nextStop = NULL;}

    // make sure that the new stop was put somewhere in the collection
    _ASSERT (bUpdated);
    return S_OK;
```



## Related topics

<dl> <dt>

[**IXpsOMGradientStop Interface**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomgradientstop)
</dt> <dt>

[**IXpsOMGradientStopCollection Interface**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomgradientstopcollection)
</dt> </dl>

 

 



