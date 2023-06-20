---
description: Pin Property Set
ms.assetid: 0c01bd51-353d-4f48-b33c-796f740915e2
title: Pin Property Set
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Pin Property Set

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The pin property set returns the pin category for a pin on a filter. The category is set by the filter when it creates the pin; the category indicates what type of data the pin is delivered or receives by this pin.



| Label | Value |
|-------------------|----------------------|
| Property Set GUID | **AMPROPSETID\_Pin** |



 



| Property ID                   | Description                      |
|-------------------------------|----------------------------------|
| **AMPROPERTY\_PIN\_CATEGORY** | Specifies the category of a pin. |



 

DirectShow defines the following pin categories in the Uuids.h header file.



| Category GUID                     | Description                                                                                                                                                                                                                                                                                                             |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **PIN\_CATEGORY\_ANALOGVIDEOIN**  | Input pin of the capture filter that takes analog and digitizes it.                                                                                                                                                                                                                                                     |
| **PIN\_CATEGORY\_CAPTURE**        | Capture pin.                                                                                                                                                                                                                                                                                                            |
| **PIN\_CATEGORY\_CC**             | Pin providing closed captioning data from Line 21.                                                                                                                                                                                                                                                                      |
| **PIN\_CATEGORY\_EDS**            | Pin providing Extended Data Services (Line 21, even fields).                                                                                                                                                                                                                                                            |
| **PIN\_CATEGORY\_NABTS**          | Pin providing North American Videotext Standard data.                                                                                                                                                                                                                                                                   |
| **PIN\_CATEGORY\_PREVIEW**        | Preview pin.                                                                                                                                                                                                                                                                                                            |
| **PIN\_CATEGORY\_STILL**          | Pin that provides a still image. The filter's capture pin must be connected before the still-image pin is connected.                                                                                                                                                                                                    |
| **PIN\_CATEGORY\_TELETEXT**       | Pin providing teletext (a closed captioning variant).                                                                                                                                                                                                                                                                   |
| **PIN\_CATEGORY\_TIMECODE**       | Pin providing timecode data.                                                                                                                                                                                                                                                                                            |
| **PIN\_CATEGORY\_VBI**            | Pin providing vertical blanking interval data.                                                                                                                                                                                                                                                                          |
| **PIN\_CATEGORY\_VIDEOPORT**      | Video output pin to be connected to input pin zero on the [Overlay Mixer](overlay-mixer-filter.md).                                                                                                                                                                                                                    |
| **PIN\_CATEGORY\_VIDEOPORT\_VBI** | Pin to be connected to the [VBI Surface Allocator](vbi-surface-allocator.md), the VBI surface allocator filter that is needed to allocate the correct video memory for things like closed captioning overlays in scenarios where a video port is being used. PCI, IEEE 1394, and USB scenarios do not use this filter. |
| **PINNAME\_VIDEO\_CC\_CAPTURE**   | Hardware slicing closed-captioning pin                                                                                                                                                                                                                                                                                  |



 

This property is read-only.

### Example Code

The following code shows how to check whether a pin supports this property set, and if so, how to obtain the pin category:


```C++
HRESULT GetPinCategory(IPin *pPin, GUID *pPinCategory)
{
    IKsPropertySet *pKs = NULL;

    HRESULT hr = pPin->QueryInterface(IID_PPV_ARGS(&pKs));
    if (FAILED(hr))
    {
        return hr;
    }

    // Try to retrieve the pin category.
    DWORD cbReturned = 0;
    hr = pKs->Get(AMPROPSETID_Pin, AMPROPERTY_PIN_CATEGORY, NULL, 0, 
        pPinCategory, sizeof(GUID), &cbReturned);
    
    // If this succeeded, pPinCategory now contains the category GUID.

    SafeRelease(&pKs);
    return hr;
}
```



> [!Note]  
> This example uses the [SafeRelease](../medfound/saferelease.md) function to release interface pointers.

 

## Related topics

<dl> <dt>

[Pin Requirements for Capture Filters](pin-requirements-for-capture-filters.md)
</dt> <dt>

[Property Sets](property-sets.md)
</dt> <dt>

[Working with Pin Categories](working-with-pin-categories.md)
</dt> </dl>

 

 
