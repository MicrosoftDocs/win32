---
description: Enumerating Effects and Transitions
ms.assetid: 364b7bfb-5d6e-4ca6-b0c8-7a0180c3f61a
title: Enumerating Effects and Transitions
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Enumerating Effects and Transitions

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

\[This API is not supported and may be altered or unavailable in the future.\]

DirectShow provides a [System Device Enumerator](system-device-enumerator.md) object for enumerating devices. You can use it to retrieve monikers for effects or transitions installed on the user's system.

The system device enumerator exposes the [**ICreateDevEnum**](/windows/desktop/api/Strmif/nn-strmif-icreatedevenum) interface. It returns category enumerators for specified device categories. A category enumerator, in turn, exposes the [**IEnumMoniker**](/windows/desktop/api/objidl/nn-objidl-ienummoniker) interface and returns monikers for each device in the category. For a detailed discussion of using **ICreateDevEnum**, see [Enumerating Devices and Filters](enumerating-devices-and-filters.md). The following is a brief summary, specific to DirectShow Editing Services.

To enumerate effects or transitions, perform the following steps.

1.  Create an instance of the system device enumerator.
2.  Call the [**ICreateDevEnum::CreateClassEnumerator**](/windows/desktop/api/Strmif/nf-strmif-icreatedevenum-createclassenumerator) method to retrieve a category enumerator. Categories are defined by class identifiers (CLSIDs). Use CLSID\_VideoEffects1Category for effects or CLSID\_VideoEffects2Category for transitions.
3.  Call **IEnumMoniker::Next** to retrieve each moniker in the enumeration.
4.  For each moniker, call **IMoniker::BindToStorage** to retrieve its associated property bag.

The property bag contains the friendly name and the globally unique identifier (GUID) for the effect or transition. An application can display a list of friendly names and then obtain the corresponding GUID.

The following code example illustrates these steps.


```C++
ICreateDevEnum *pCreateDevEnum = NULL;
IEnumMoniker *pEnumMoniker = NULL;

// Create the System Device Enumerator.
HRESULT hr = CoCreateInstance(CLSID_SystemDeviceEnum, NULL, 
    CLSCTX_INPROC_SERVER, IID_ICreateDevEnum, (void**)&pCreateDevEnum);
if (FAILED(hr))
{
    // Error handling omitted for clarity.
}

// Create an enumerator for the video effects category.
hr = pCreateDevEnum->CreateClassEnumerator(
    CLSID_VideoEffects1Category,  // Video effects category. 
    &pEnumMoniker, 0);               

// Note: Use CLSID_VideoEffects2Category for video transitions.

if (hr == S_OK)  // S_FALSE means the category is empty.
{
    // Enumerate each video effect.
    IMoniker *pMoniker;
    while (S_OK == pEnumMoniker->Next(1, &pMoniker, NULL))
    {
        IPropertyBag *pBag;
        hr = pMoniker->BindToStorage(0, 0, IID_IPropertyBag, 
            (void **)&pBag);
        if(FAILED(hr))
        {
            pMoniker->Release();
            continue; // Maybe the next one will work.
        }
        VARIANT var;
        VariantInit(&var);
        hr = pBag->Read(OLESTR("FriendlyName"), &var, NULL);
        if (SUCCEEDED(hr))
        {
            if ( ... )  // Check if var.bstrVal is the name you want.
            {
                VARIANT var2;
                GUID guid;
                var2.vt = VT_BSTR;
                pBag->Read(OLESTR("guid"), &var2, NULL);
                CLSIDFromString(var2.bstrVal, &guid);
                VariantClear(&var2);
                // GUID is now the CLSID for the effect.
            }
        }
        VariantClear(&var);
        pBag->Release();
        pMoniker->Release();
    }
    pEnumMoniker->Release();
}
pCreateDevEnum->Release();
```



## Related topics

<dl> <dt>

[Working with Effects and Transitions](working-with-effects-and-transitions.md)
</dt> </dl>

 

 
