---
Description: Using the Source Resolver
ms.assetid: 94e2a411-96b8-4506-8491-78f4f5f286ce
title: Using the Source Resolver
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using the Source Resolver

The source resolver takes a URL or byte stream and creates the appropriate media source for that content. To create the source resolver, call [**MFCreateSourceResolver**](/windows/win32/mfidl/nf-mfidl-mfcreatesourceresolver?branch=master). This function returns an [**IMFSourceResolver**](/windows/win32/mfidl/nn-mfidl-imfsourceresolver?branch=master) interface pointer.

The source resolver has both synchronous and asynchronous methods. If you are using the source resolver from your main application thread, the asynchronous methods will make your user interface more responsive. The synchronous methods can block for a noticeable amount of time, particularly if the source resolver must open a network resource.

The synchronous methods are:

-   [**IMFSourceResolver::CreateObjectFromURL**](/windows/win32/mfidl/nf-mfidl-imfsourceresolver-createobjectfromurl?branch=master)
-   [**IMFSourceResolver::CreateObjectFromByteStream**](/windows/win32/mfidl/nf-mfidl-imfsourceresolver-createobjectfrombytestream?branch=master)

The asynchronous methods are:

-   [**IMFSourceResolver::BeginCreateObjectFromURL**](/windows/win32/mfidl/nf-mfidl-imfsourceresolver-begincreateobjectfromurl?branch=master)
-   [**IMFSourceResolver::BeginCreateObjectFromByteStream**](/windows/win32/mfidl/nf-mfidl-imfsourceresolver-begincreateobjectfrombytestream?branch=master)

For the asynchronous methods, each method has a corresponding **End...** method to complete the asynchronous request, and a **Cancel...** method to cancel a pending request. For more information about asynchronous methods in Media Foundation, see [Asynchronous Callback Methods](asynchronous-callback-methods.md).

The following code example creates a media source from a URL. This example uses the synchronous method.


```C++
//  Create a media source from a URL.
HRESULT CreateMediaSource(PCWSTR sURL, IMFMediaSource **ppSource)
{
    MF_OBJECT_TYPE ObjectType = MF_OBJECT_INVALID;

    IMFSourceResolver* pSourceResolver = NULL;
    IUnknown* pSource = NULL;

    // Create the source resolver.
    HRESULT hr = MFCreateSourceResolver(&amp;pSourceResolver);
    if (FAILED(hr))
    {
        goto done;
    }

    // Use the source resolver to create the media source.

    // Note: For simplicity this sample uses the synchronous method to create 
    // the media source. However, creating a media source can take a noticeable
    // amount of time, especially for a network source. For a more responsive 
    // UI, use the asynchronous BeginCreateObjectFromURL method.

    hr = pSourceResolver->CreateObjectFromURL(
        sURL,                       // URL of the source.
        MF_RESOLUTION_MEDIASOURCE,  // Create a source object.
        NULL,                       // Optional property store.
        &amp;ObjectType,        // Receives the created object type. 
        &amp;pSource            // Receives a pointer to the media source.
        );
    if (FAILED(hr))
    {
        goto done;
    }

    // Get the IMFMediaSource interface from the media source.
    hr = pSource->QueryInterface(IID_PPV_ARGS(ppSource));

done:
    SafeRelease(&amp;pSourceResolver);
    SafeRelease(&amp;pSource);
    return hr;
}
```



## Related topics

<dl> <dt>

[Source Resolver](source-resolver.md)
</dt> </dl>

 

 



