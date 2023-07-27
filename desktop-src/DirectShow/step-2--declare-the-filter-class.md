---
description: Declare a C++ class that inherits the base class that your chose as part of writing a transform filter.
ms.assetid: 74fbfc16-541f-4f80-a72f-26b67dc09a93
title: Step 2. Declare the Filter Class
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Step 2. Declare the Filter Class

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This is step 2 of the tutorial [Writing Transform Filters](writing-transform-filters.md).

Start by declaring a C++ class that inherits the base class:


```C++
class CRleFilter : public CTransformFilter
{
    /* Declarations will go here. */
};
```



Each of the filter classes has associated pin classes. Depending on the specific needs of your filter, you might need to override the pin classes. In the case of **CTransformFilter**, the pins delegate most of their work to the filter, so you probably don't need to override the pins.

You must generate a unique CLSID for the filter. You can use the Guidgen or Uuidgen utility; never copy an existing GUID. There are several ways to declare a CLSID. The following example uses the **DEFINE\_GUID** macro:


```C++
[RleFilt.h]
// {1915C5C7-02AA-415f-890F-76D94C85AAF1}
DEFINE_GUID(CLSID_RLEFilter, 
0x1915c5c7, 0x2aa, 0x415f, 0x89, 0xf, 0x76, 0xd9, 0x4c, 0x85, 0xaa, 0xf1);

[RleFilt.cpp]
#include <initguid.h>
#include "RleFilt.h"
```



Next, write a constructor method for the filter:


```C++
CRleFilter::CRleFilter()
  : CTransformFilter(NAME("My RLE Encoder"), 0, CLSID_RLEFilter)
{ 
   /* Initialize any private variables here. */
}
```



Notice that one of the parameters to the [**CTransformFilter**](ctransformfilter-ctransformfilter.md) constructor is the CLSID defined earlier.

Next: [Step 3. Support Media Type Negotiation](step-3--support-media-type-negotiation.md).

## Related topics

<dl> <dt>

[Writing DirectShow Filters](writing-directshow-filters.md)
</dt> </dl>

 

 



