---
description: Choosing a Compression Filter
ms.assetid: 9a2c3c48-771e-44db-a042-3db0fd9a6c76
title: Choosing a Compression Filter
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Choosing a Compression Filter

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Several types of software components can perform video or audio compression, such as:

-   Native DirectShow filters
-   Video Compression Manager (VCM) codecs
-   Audio Compression Manager (ACM) codecs
-   DirectX Media Objects (DMOs)

In DirectShow, VCM codecs are wrapped by the [AVI Compressor Filter](avi-compressor-filter.md), and ACM codecs are wrapped by the [ACM Wrapper Filter](acm-wrapper-filter.md). DMOs are wrapped by the [DMO Wrapper Filter](dmo-wrapper-filter.md). The system device enumerator provides a consistent way to enumerate and create any of these compressor types, without worrying about the underlying model.

For details about the system device enumerator, see [Using the System Device Enumerator](using-the-system-device-enumerator.md). Briefly, all DirectShow filters are classified by category, and each category is identified by a GUID. For video compressors, the category GUID is CLSID\_VideoCompressorCategory. For audio compressors, it is CLSID\_AudioCompressorCategory. To enumerate a particular category, the system device enumerator creates an *enumerator* object that supports the [**IEnumMoniker**](/windows/desktop/api/objidl/nn-objidl-ienummoniker) interface. The application uses this interface to retrieve device monikers, where each device moniker represents an instance of a DirectShow filter. You can use the moniker to create the filter, or to get the device's friendly name without creating the filter.

To enumerate the video or audio compressors available on the user's system, do the following:

1.  Call [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) to create the system device enumerator, which has a class ID of CLSID\_SystemDeviceEnum.
2.  Call [**ICreateDevEnum::CreateClassEnumerator**](/windows/desktop/api/Strmif/nf-strmif-icreatedevenum-createclassenumerator) with the filter category GUID. The method returns an **IEnumMoniker** interface pointer.
3.  Use the IEnumMoniker::Next method to enumerate the device monikers. This method returns an [**IMoniker**](/windows/desktop/api/objidl/nn-objidl-imoniker) interface, which represents the moniker.

To get the friendly name from a moniker, do the following:

1.  Call the **IMoniker::BindToStorage** method. This method returns an **IPropertyBag** interface pointer.
2.  Use the **IPropertyBag::Read** method to read the **FriendlyName** property.

Typically, an application would display a list of compressors, so that the user could choose one. For example, the following code populates a list box with the names of the available video compressors.


```C++
void OnInitDialog(HWND hDlg)
{
    HRESULT hr;
    ICreateDevEnum *pSysDevEnum = NULL;
    IEnumMoniker *pEnum = NULL;
    IMoniker *pMoniker = NULL;

    hr = CoCreateInstance(CLSID_SystemDeviceEnum, NULL, 
        CLSCTX_INPROC_SERVER, IID_ICreateDevEnum, 
        (void**)&pSysDevEnum);
    if (FAILED(hr))
    {
        // Handle the error.
    }    

    hr = pSysDevEnum->CreateClassEnumerator(
             CLSID_VideoCompressorCategory, &pEnum, 0);
    if (hr == S_OK)  // S_FALSE means nothing in this category.
    {
        while (S_OK == pEnum->Next(1, &pMoniker, NULL))
        {
            IPropertyBag *pPropBag = NULL;
            pMoniker->BindToStorage(0, 0, IID_IPropertyBag, 
                (void **)&pPropBag);
            VARIANT var;
            VariantInit(&var);
            hr = pPropBag->Read(L"FriendlyName", &var, 0);
            if (SUCCEEDED(hr))
            {
                LRESULT iSel = AddString(GetDlgItem(hDlg, 
                    IDC_CODEC_LIST), var.bstrVal);
            }   
            VariantClear(&var); 
            pPropBag->Release();
            pMoniker->Release();
        }
    }

    SendDlgItemMessage(hDlg, IDC_CODEC_LIST, 
                       LB_SETCURSEL, 0, 0);
    pSysDevEnum->Release();
    pEnum->Release();
}
```



To create a filter instance from the moniker, call the **IMoniker::BindToObject** method. The method returns an [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter) pointer.


```C++
IBaseFilter *pFilter = NULL;
hr = pMoniker->BindToObject(NULL, NULL, IID_IBaseFilter, 
                                       (void**)&pFilter);
if (SUCCEEDED(hr))
{
    // Use the filter. 
    // Remember to release the IBaseFilter interface.
}
```



For VCM codecs, each moniker represents one particular codec, even though all of the codecs are wrapped by the same AVI Compression filter. Calling **BindToObject** creates an instance of this filter, initialized for that codec. For this reason, you cannot call **CoCreateInstance** directly on the AVI Compression filter. You must go through the system device enumerator.

## Related topics

<dl> <dt>

[Recompressing an AVI File](recompressing-an-avi-file.md)
</dt> </dl>

 

 
