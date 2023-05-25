---
description: Step 10.
ms.assetid: 2959f574-1a39-4db1-9e4a-a303d0c7f8f3
title: Step 10. Support COM Registration
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Step 10. Support COM Registration

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The last remaining task is to support COM registration, so that the property frame can create new instances of your property page. Add another [**CFactoryTemplate**](cfactorytemplate.md) entry to the global *g\_Templates* array, which is used to register all of the COM objects in your DLL. Do not include any filter set-up information for the property page.


```C++
const AMOVIESETUP_FILTER FilterSetupData = 
{ 
    /* Not shown ... */
};

CFactoryTemplate g_Templates[] =
{   
    // This entry is for the filter.
    {
        wszName,
        &CLSID_GrayFilter,
        CGrayFilter::CreateInstance,
        NULL,
        &FilterSetupData 
    },
    // This entry is for the property page.
    { 
        L"Saturation Props",
        &CLSID_SaturationProp,
        CGrayProp::CreateInstance, 
        NULL, NULL
    }
};
```



If you declare *g\_cTemplates* as shown in the following code, then it automatically has the correct value based on the array size:


```C++
int g_cTemplates = sizeof(g_Templates)/sizeof(g_Templates[0]);
```



Also, add a static `CreateInstance` method to the property page class. You can name the method anything that you prefer, but the signature must match the one shown the following example:


```C++
static CUnknown * WINAPI CreateInstance(LPUNKNOWN pUnk, HRESULT *pHr) 
{
    CGrayProp *pNewObject = new CGrayProp(pUnk);
    if (pNewObject == NULL) 
    {
        *pHr = E_OUTOFMEMORY;
    }
    return pNewObject;
} 
```



To test the property page, register the DLL and then load the filter in GraphEdit. Right-click the filter and select **Filter Properties**.

## Related topics

<dl> <dt>

[Creating a Filter Property Page](creating-a-filter-property-page.md)
</dt> <dt>

[How to Create a DirectShow Filter DLL](how-to-create-a-dll.md)
</dt> </dl>

 

 



