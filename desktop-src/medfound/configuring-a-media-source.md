---
Description: Configuring a Media Source
ms.assetid: '1378bbe6-be94-4be1-b428-5ec58dabd1fa'
title: Configuring a Media Source
---

# Configuring a Media Source

When you use the [Source Resolver](source-resolver.md) to create a media source, you can specify a property store that contains configuration properties. These properties will be used to initialize the media source. The set of supported properties depends on the implementation of the media source. Not every media source defines configuration properties.

The following table lists the configuration properties for the media sources that are provided in Media Foundation. Third-party media sources can define their own custom properties.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Media source</th>
<th>Properties</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Network source</td>
<td>See [Network Source Features](network-source-features.md).</td>
</tr>
<tr class="even">
<td>ASF media source</td>
<td><ul>
<li>[<strong>MFPKEY_ASFMediaSource_ApproxSeek</strong>](mfpkey-asfmediasource-approxseek-property.md)</li>
<li>[MFPKEY_ASFMediaSource_IterativeSeekIfNoIndex](mfpkey-asfmediasource-iterativeseekifnoindex.md)</li>
<li>[MFPKEY_ASFMediaSource_IterativeSeek_Max_Count](mfpkey-asfmediasource-iterativeseek-max-count.md)</li>
<li>[MFPKEY_ASFMediaSource_IterativeSeek_Tolerance_In_MilliSecond](mfpkey-asfmediasource-iterativeseek-tolerance-in-millisecond.md)</li>
</ul></td>
</tr>
</tbody>
</table>



 

To configure a source, perform the following steps.

1.  Call **PSCreateMemoryPropertyStore** to create a new property store. This function returns an **IPropertyStore** pointer.
2.  Call **IPropertyStore::SetValue** to set one or more configuration properties.
3.  Call one of the source resolver's creation functions, such as [**IMFSourceResolver::CreateObjectFromURL**](imfsourceresolver-createobjectfromurl.md), and pass the **IPropertyStore** pointer in the *pProps* parameter.


```C++
// Creates a media source from a URL.

HRESULT CreateMediaSource(
    PCWSTR pszURL, 
    IPropertyStore *pConfig,    // Optional, can be NULL
    IMFMediaSource **ppSource
    )
{
    IMFSourceResolver* pSourceResolver = NULL;
    IUnknown* pSource = NULL;

    // Create the source resolver.
    HRESULT hr = MFCreateSourceResolver(&amp;pSourceResolver);

    // Use the source resolver to create the media source.
    if (SUCCEEDED(hr))
    {
        MF_OBJECT_TYPE ObjectType;

        DbgLog(L"CreateObjectFromURL");

        hr = pSourceResolver->CreateObjectFromURL(
            pszURL,                     
            MF_RESOLUTION_MEDIASOURCE,  // Create a media source.
            pConfig,                    // Configuration properties.
            &amp;ObjectType,                // Receives the object type. 
            &amp;pSource            
            );

        DbgLog(L"CreateObjectFromURL - FINISHED");

    }

    if (SUCCEEDED(hr))
    {
        hr = pSource->QueryInterface(IID_PPV_ARGS(ppSource));
    }

    SafeRelease(&amp;pSourceResolver);
    SafeRelease(&amp;pSource);
    return hr;
}
```



The source resolver passes the **IPropertyStore** pointer directly to the scheme handler or byte-stream handler that creates the source. The source resolver makes no attempt to validate the properties.

Generally, these properties are used for advanced settings. If you don't provide a property store, the media source should still function correctly with default settings.

## Related topics

<dl> <dt>

[Source Resolver](source-resolver.md)
</dt> </dl>

 

 



