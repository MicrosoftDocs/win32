---
Description: Enumerating Effects and Transitions
ms.assetid: 364b7bfb-5d6e-4ca6-b0c8-7a0180c3f61a
title: Enumerating Effects and Transitions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Enumerating Effects and Transitions

\[This API is not supported and may be altered or unavailable in the future.\]

DirectShow provides a [System Device Enumerator](system-device-enumerator.md) object for enumerating devices. You can use it to retrieve monikers for effects or transitions installed on the user's system.

The system device enumerator exposes the [**ICreateDevEnum**](/windows/win32/Strmif/nn-strmif-icreatedevenum?branch=master) interface. It returns category enumerators for specified device categories. A category enumerator, in turn, exposes the [**IEnumMoniker**](https://msdn.microsoft.com/library/windows/desktop/ms692852) interface and returns monikers for each device in the category. For a detailed discussion of using **ICreateDevEnum**, see [Enumerating Devices and Filters](enumerating-devices-and-filters.md). The following is a brief summary, specific to DirectShow Editing Services.

To enumerate effects or transitions, perform the following steps.

1.  Create an instance of the system device enumerator.
2.  Call the [**ICreateDevEnum::CreateClassEnumerator**](/windows/win32/Strmif/nf-strmif-icreatedevenum-createclassenumerator?branch=master) method to retrieve a category enumerator. Categories are defined by class identifiers (CLSIDs). Use CLSID\_VideoEffects1Category for effects or CLSID\_VideoEffects2Category for transitions.
3.  Call **IEnumMoniker::Next** to retrieve each moniker in the enumeration.
4.  For each moniker, call **IMoniker::BindToStorage** to retrieve its associated property bag.

The property bag contains the friendly name and the globally unique identifier (GUID) for the effect or transition. An application can display a list of friendly names and then obtain the corresponding GUID.

The following code example illustrates these steps.


```C++
ICreateDevEnum *pCreateDevEnum = NULL;
IEnumMoniker *pEnumMoniker = NULL;

// Create the System Device Enumerator.
HRESULT hr = CoCreateInstance(CLSID_SystemDeviceEnum, NULL, 
    CLSCTX_INPROC_SERVER, IID_ICreateDevEnum, (void**)&amp;pCreateDevEnum);
if (FAILED(hr))
{
    // Error handling omitted for clarity.
}

// Create an enumerator for the video effects category.
hr = pCreateDevEnum->CreateClassEnumerator(
    CLSID_VideoEffects1Category,  // Video effects category. 
    &amp;pEnumMoniker, 0);               

// Note: Use CLSID_VideoEffects2Category for video transitions.

if (hr == S_OK)  // S_FALSE means the category is empty.
{
    // Enumerate each video effect.
    IMoniker *pMoniker;
    while (S_OK == pEnumMoniker->Next(1, &amp;pMoniker, NULL))
    {
        IPropertyBag *pBag;
        hr = pMoniker->BindToStorage(0, 0, IID_IPropertyBag, 
            (void **)&amp;pBag);
        if(FAILED(hr))
        {
            pMoniker->Release();
            continue; // Maybe the next one will work.
        }
        VARIANT var;
        VariantInit(&amp;var);
        hr = pBag->Read(OLESTR("FriendlyName"), &amp;var, NULL);
        if (SUCCEEDED(hr))
        {
            if ( ... )  // Check if var.bstrVal is the name you want.
            {
                VARIANT var2;
                GUID guid;
                var2.vt = VT_BSTR;
                pBag->Read(OLESTR("guid"), &amp;var2, NULL);
                CLSIDFromString(var2.bstrVal, &amp;guid);
                VariantClear(&amp;var2);
                // GUID is now the CLSID for the effect.
            }
        }
        VariantClear(&amp;var);
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

 

 



