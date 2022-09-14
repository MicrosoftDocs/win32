---
description: Using Windows Media With DirectShow Editing Services
ms.assetid: 26a88197-ec80-4443-9d50-e11df40dd1eb
title: Using Windows Media With DirectShow Editing Services
ms.topic: article
ms.date: 05/31/2018
---

# Using Windows Media With DirectShow Editing Services

\[This API is not supported and may be altered or unavailable in the future.\]

This section describes how to use Windows Media–based content in a [DirectShow Editing Services](directshow-editing-services.md) (DES) application. There are two main scenarios:

-   Source clips. A DES project can contain audio and video clips from Windows Media files.
-   Target format. Windows Media is an ideal format for the final output of a video editing project.

To work with Windows Media files, the application must provide a software certificate, also called a key. It does this by implementing a key provider object. The key provider is a COM object the exposes the **IServiceProvider** interface. For information about implementing the key provider, see [Unlocking the Windows Media Format SDK](unlocking-the-windows-media-format-sdk.md).

To use DES with Windows Media files, the following DES objects require the software key:

-   The render engine, for previewing or file writing.
-   The MediaDet object, to get video frames or media types from ASF files.
-   \[!Important\]  
    > Do not use the Smart Render Engine to read or write Windows Media files. Always use the Basic Render Engine (CLSID\_RenderEngine).

     

To give an object the software key, query that object for the **IObjectWithSite** interface and call **IObjectWithSite::SetSite** with a pointer to your key provider. For example, the following code provides the software key to the render engine:


```C++
// Create your key provider, using an application-defined function:
IServiceProvider *pKey;
hr = MyCreateKeyProviderFunction(&pKey);  

// Query the Render Engine for IObjectWithSite.
IObjectWithSite *pOWS;
hr = pRenderEngine->QueryInterface(__uuidof(IObjectWithSite), 
    reinterpret_cast<void**>(&pOWS));
if (SUCCEEDED(hr))
{
    // Give it your key provider.
    hr = pOWS->SetSite(pKey);
    pOWS->Release();
}
pKey->Release();
```



To use Windows Media source clips in a DES project, simply call **IObjectWithSite::SetSite** on the render engine with a pointer to your key provider.

For information about writing Windows Media files, see [Writing a Windows Media File in DES](writing-a-windows-media-file-in-des.md).

## Related topics

<dl> <dt>

[Using DirectShow Editing Services](using-directshow-editing-services.md)
</dt> </dl>

 

 



