---
Description: Creating the ASF Splitter Object
ms.assetid: '448e2b38-70f7-4491-aac8-ee988a6f7473'
title: Creating the ASF Splitter Object
---

# Creating the ASF Splitter Object

The ASF *splitter* object is a WMContainer layer object that parses the ASF Data Object of an Advanced Systems Format (ASF) file. To create a new instance of the ASF splitter object, call the [**MFCreateASFSplitter**](mfcreateasfsplitter.md) function. This function returns a pointer to the [**IMFASFSplitter**](imfasfsplitter.md) interface that represents an empty splitter object.

Before the splitter can begin parsing, the application must initialize the splitter with information from the ASF Header Object. To initialize the splitter, call the [**IMFASFSplitter::Initialize**](imfasfsplitter-initialize.md) method. This method takes a pointer to the [ASF ContentInfo Object](asf-contentinfo-object.md) that contains header information of the ASF file to parse. The application must initialize the ContentInfo object before passing it to the splitter so that the characteristics of the media file are known to the application. The splitter's **Initialize** method extracts stream information from the ContentInfo object, such as stream numbers, so the splitter can parse the data packets.

### Example

The following code example shows how to create a splitter and initialize it with an existing ContentInfo object.


```C++
// Create and initialize the ASF splitter.

HRESULT CreateASFSplitter (IMFASFContentInfo* pContentInfo, 
    IMFASFSplitter** ppSplitter)
{
    IMFASFSplitter *pSplitter = NULL;

    // Create the splitter object.
    HRESULT hr = MFCreateASFSplitter(&amp;pSplitter);

    // Initialize the splitter to work with specific ASF data.
    if (SUCCEEDED(hr))
    {
        hr = pSplitter->Initialize(pContentInfo);
    }
    if (SUCCEEDED(hr))
    {
        // Return the object to the caller.
        *ppSplitter = pSplitter;
        (*ppSplitter)->AddRef();
    }
    SafeRelease(&amp;pSplitter);
    return hr;
}
```



> [!Note]  
> This example uses the [SafeRelease](saferelease.md) function to release interface pointers.

 

## Related topics

<dl> <dt>

[ASF Splitter](asf-splitter.md)
</dt> </dl>

 

 



