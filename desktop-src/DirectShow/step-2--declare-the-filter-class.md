---
description: Declare a C++ class that inherits the base class that your chose as part of writing a transform filter.
ms.assetid: 74fbfc16-541f-4f80-a72f-26b67dc09a93
title: Step 2. Declare the Filter Class
ms.topic: article
ms.date: 05/31/2018
---

# Step 2. Declare the Filter Class

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

 

 



