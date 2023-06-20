---
description: Implementing DllRegisterServer
ms.assetid: aaa4069e-0b6a-4a76-b950-1a85a9ed969d
title: Implementing DllRegisterServer
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Implementing DllRegisterServer

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The final step is to implement the **DllRegisterServer** function. The DLL that contains the component must export this function. The function will be called by a set-up application, or when the user runs the Regsvr32.exe tool.

The following example shows a minimal implementation of **DlLRegisterServer**:


```C++
STDAPI DllRegisterServer(void)
{
    return AMovieDllRegisterServer2(TRUE);
}
```



The [**AMovieDllRegisterServer2**](amoviedllregisterserver2.md) function creates registry entries for every component in the


```
g_Templates
```



array. However, this function has some limitations. First, it assigns every filter to the "DirectShow Filters" category (CLSID\_LegacyAmFilterCategory), but not every filter belongs in this category. Capture filters and compression filters, for example, have their own categories. Second, if your filter supports a hardware device, you might need to register two additional pieces of information that **AMovieDLLRegisterServer2** does not handle: the *medium* and the *pin category*. A medium defines a method of communication in a hardware device, such as a bus. The pin category defines the function of a pin. For information on mediums, see "KSPIN\_MEDIUM" in the Microsoft Windows Driver Development Kit (DDK). For a list of pin categories, see [Pin Property Set](pin-property-set.md).

If you want to specify a filter category, a medium, or a pin category, call the [**IFilterMapper2::RegisterFilter**](/windows/desktop/api/Strmif/nf-strmif-ifiltermapper2-registerfilter) method from within **DllRegisterServer**. This method takes a pointer to a [**REGFILTER2**](/windows/desktop/api/strmif/ns-strmif-regfilter2) structure, which specifies information about the filter.

To complicate matters somewhat, the **REGFILTER2** structure supports two different formats for registering pins. The **dwVersion** member specifies the format:

-   If **dwVersion** is 1, the pin format is **AMOVIESETUP\_PIN** (described previously).
-   If **dwVersion** is 2, the pin format is [**REGFILTERPINS2**](/windows/desktop/api/strmif/ns-strmif-regfilterpins2).

The **REGFILTERPINS2** structure includes entries for pin mediums and pin categories. Also, it uses bit flags for some items that **AMOVIESETUP\_PIN** declares as Boolean values.

The following example shows how to call **IFilterMapper2::RegisterFilter** from inside **DllRegisterServer**:


```C++
REGFILTER2 rf2FilterReg = {
    1,              // Version 1 (no pin mediums or pin category).
    MERIT_NORMAL,   // Merit.
    1,              // Number of pins.
    &sudPins        // Pointer to pin information.
};

STDAPI DllRegisterServer(void)
{
    HRESULT hr;
    IFilterMapper2 *pFM2 = NULL;

    hr = AMovieDllRegisterServer2(TRUE);
    if (FAILED(hr))
        return hr;

    hr = CoCreateInstance(CLSID_FilterMapper2, NULL, CLSCTX_INPROC_SERVER,
            IID_IFilterMapper2, (void **)&pFM2);

    if (FAILED(hr))
        return hr;

    hr = pFM2->RegisterFilter(
        CLSID_SomeFilter,                // Filter CLSID. 
        g_wszName,                       // Filter name.
        NULL,                            // Device moniker. 
        &CLSID_VideoCompressorCategory,  // Video compressor category.
        g_wszName,                       // Instance data.
        &rf2FilterReg                    // Pointer to filter information.
    );
    pFM2->Release();
    return hr;
}
```



 

 



