---
Description: Starting in Windows 7, Microsoft Media Foundation exposes metadata through the IPropertyStore interface.
ms.assetid: d219d3f1-3940-46ed-9811-3cf8bf1eec55
title: Shell Metadata Providers
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Shell Metadata Providers

Starting in Windows 7, Microsoft Media Foundation exposes metadata through the [**IPropertyStore**](properties.IPropertyStore) interface.

Metadata obtained using the process defined in this topic should only be used for read-only access. Writing data using this process is not supported. You can create an [**IPropertyStore**](properties.IPropertyStore) object for writing purposes using a class identifier (CLSID) obtained from [**PSLookupPropertyHandlerCLSID**](properties.PSLookupPropertyHandlerCLSID).

## Reading Metadata

To read metadata from a media source, perform the following steps:

1.  Get a pointer to the [**IMFMediaSource**](/windows/win32/mfidl/nn-mfidl-imfmediasource?branch=master) interface of the media source. You can use the [**IMFSourceResolver**](/windows/win32/mfidl/nn-mfidl-imfsourceresolver?branch=master) interface to get an **IMFMediaSource** pointer.
2.  Call [**MFGetService**](/windows/win32/mfidl/nf-mfidl-mfgetservice?branch=master) on the media source to get a pointer to the [**IPropertyStore**](properties.IPropertyStore) interface. In the *guidService* parameter of **MFGetService**, specify the value **MF\_PROPERTY\_HANDLER\_SERVICE**. If the source does not support the **IPropertyStore** interface, **MFGetService** returns **MF\_E\_UNSUPPORTED\_SERVICE**.
3.  Call [**IPropertyStore**](properties.IPropertyStore) methods to enumerate the metadata properties.

The following code shows these steps. Assume that `DisplayProperty` is a function that displays a **PROPVARIANT** value.


```C++
HRESULT EnumerateMetadata(IMFMediaSource *pSource)
{
    IPropertyStore *pProps = NULL;

    HRESULT hr = MFGetService(
        pSource, MF_PROPERTY_HANDLER_SERVICE, IID_PPV_ARGS(&amp;pProps));

    if (FAILED(hr))
    {
        goto done;
    }

    DWORD cProps;

    hr = pProps->GetCount(&amp;cProps);
    if (FAILED(hr))
    {
        goto done;
    }

    for (DWORD i = 0; i < cProps; i++)
    {
        PROPERTYKEY key;
        hr = pProps->GetAt(i, &amp;key);
        if (FAILED(hr))
        {
            goto done;
        }

        PROPVARIANT pv;

        hr = pProps->GetValue(key, &amp;pv);
        if (FAILED(hr))
        {
            goto done;
        }

        DisplayProperty(key, pv);
        PropVariantClear(&amp;pv);
    }

done:
    SafeRelease(&amp;pProps);
    return hr;
}
```



For a list of metadata property keys, see [Metadata Properties for Media Files](metadata-properties-for-media-files.md).

## Related topics

<dl> <dt>

[Media Metadata](media-metadata.md)
</dt> </dl>

 

 



