---
description: Reading the ASF Header Object of an Existing File
ms.assetid: 0e37f0d3-a37b-4f36-a133-7b1922e9944b
title: Reading the ASF Header Object of an Existing File
ms.topic: article
ms.date: 05/31/2018
---

# Reading the ASF Header Object of an Existing File

The ASF ContentInfo object stores information that represents the ASF Header Objects of a media file. A populated ContentInfo object is required in order to read and parse an existing ASF file.

After creating the ContentInfo object by calling the [**MFCreateASFContentInfo**](/windows/desktop/api/wmcontainer/nf-wmcontainer-mfcreateasfcontentinfo) function, the application must initialize it with header information from the ASF file that is to be read. To populate the object, call [**IMFASFContentInfo::ParseHeader**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-parseheader).

**ParseHeader** requires a media buffer that contains the Header Object of the ASF file. One option is to fill a media buffer with the Header Object to create a byte stream for the file and then read the first 30 bytes of data from the byte stream into a media buffer. You can then get the size by passing the first 24 bytes of the Header Object to the [**IMFASFContentInfo::GetHeaderSize**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-getheadersize) method. After getting the size, you can read the entire Header Object in a media buffer and pass it to **ParseHeader**. The method starts parsing at the offset from the start of the media buffer specified in the *cbOffsetWithinHeader* parameter.

The following example code creates and initializes a ContentInfo object for reading an existing ASF file contained in a byte stream. First, we define a helper function that reads data from a byte stream and allocates a media buffer to hold the data:


```C++
// Read the ASF Header Object from a byte stream and return a pointer to the 
// populated ASF ContentInfo object.
//
// The current read position of the byte stream must be at the start of the
// ASF Header Object.

HRESULT CreateContentInfo(IMFByteStream *pStream, 
    IMFASFContentInfo **ppContentInfo)
{
    const DWORD MIN_ASF_HEADER_SIZE = 30;
    
    QWORD cbHeader = 0;
    DWORD cbBuffer = 0;

    IMFASFContentInfo *pContentInfo = NULL;
    IMFMediaBuffer *pBuffer = NULL;

    // Create the ASF ContentInfo object.
    HRESULT hr = MFCreateASFContentInfo(&pContentInfo);
    
    // Read the first 30 bytes to find the total header size.

    if (SUCCEEDED(hr))
    {
        hr = MFCreateMemoryBuffer(MIN_ASF_HEADER_SIZE, &pBuffer);
    }
    if (SUCCEEDED(hr))
    {
        hr = ReadFromByteStream(pStream, pBuffer,MIN_ASF_HEADER_SIZE);
    }
    if (SUCCEEDED(hr))
    {
        hr = pContentInfo->GetHeaderSize(pBuffer, &cbHeader);
    }

    // Pass the first 30 bytes to the ContentInfo object.
    if (SUCCEEDED(hr))
    {
        hr = pContentInfo->ParseHeader(pBuffer, 0);
    }

    SafeRelease(&pBuffer);

    if (SUCCEEDED(hr))
    {
        cbBuffer = (DWORD)(cbHeader - MIN_ASF_HEADER_SIZE);

        hr = MFCreateMemoryBuffer(cbBuffer, &pBuffer);
    }

    // Read the rest of the header and finish parsing the header.
    if (SUCCEEDED(hr))
    {
        hr = ReadFromByteStream(pStream, pBuffer, cbBuffer);
    }
    if (SUCCEEDED(hr))
    {
        hr = pContentInfo->ParseHeader(pBuffer, MIN_ASF_HEADER_SIZE);
    }
    if (SUCCEEDED(hr))
    {
        // Return the pointer to the caller.
        *ppContentInfo = pContentInfo;
        (*ppContentInfo)->AddRef();
    }
    SafeRelease(&pBuffer);
    SafeRelease(&pContentInfo);
    return hr;
} 
```



The next example reads the ASF Header Object from a byte stream and populates an ASF ContentInfo object.


```C++
// Read the ASF Header Object from a byte stream and return a pointer to the 
// populated ASF ContentInfo object.
//
// The current read position of the byte stream must be at the start of the
// ASF Header Object.

HRESULT CreateContentInfo(IMFByteStream *pStream, 
    IMFASFContentInfo **ppContentInfo)
{
    const DWORD MIN_ASF_HEADER_SIZE = 30;
    
    QWORD cbHeader = 0;
    DWORD cbBuffer = 0;

    IMFASFContentInfo *pContentInfo = NULL;
    IMFMediaBuffer *pBuffer = NULL;

    // Create the ASF ContentInfo object.
    HRESULT hr = MFCreateASFContentInfo(&pContentInfo);
    
    // Read the first 30 bytes to find the total header size.

    if (SUCCEEDED(hr))
    {
        hr = MFCreateMemoryBuffer(MIN_ASF_HEADER_SIZE, &pBuffer);
    }
    if (SUCCEEDED(hr))
    {
        hr = ReadFromByteStream(pStream, pBuffer,MIN_ASF_HEADER_SIZE);
    }
    if (SUCCEEDED(hr))
    {
        hr = pContentInfo->GetHeaderSize(pBuffer, &cbHeader);
    }

    // Pass the first 30 bytes to the ContentInfo object.
    if (SUCCEEDED(hr))
    {
        hr = pContentInfo->ParseHeader(pBuffer, 0);
    }

    SafeRelease(&pBuffer);

    if (SUCCEEDED(hr))
    {
        cbBuffer = (DWORD)(cbHeader - MIN_ASF_HEADER_SIZE);

        hr = MFCreateMemoryBuffer(cbBuffer, &pBuffer);
    }

    // Read the rest of the header and finish parsing the header.
    if (SUCCEEDED(hr))
    {
        hr = ReadFromByteStream(pStream, pBuffer, cbBuffer);
    }
    if (SUCCEEDED(hr))
    {
        hr = pContentInfo->ParseHeader(pBuffer, MIN_ASF_HEADER_SIZE);
    }
    if (SUCCEEDED(hr))
    {
        // Return the pointer to the caller.
        *ppContentInfo = pContentInfo;
        (*ppContentInfo)->AddRef();
    }
    SafeRelease(&pBuffer);
    SafeRelease(&pContentInfo);
    return hr;
} 
```



> [!Note]  
> These examples use the [SafeRelease](saferelease.md) function to release interface pointers.

 

## Related topics

<dl> <dt>

[ASF ContentInfo Object](asf-contentinfo-object.md)
</dt> <dt>

[ASF Header Object](asf-file-structure.md)
</dt> <dt>

[ASF Support in Media Foundation](asf-support-in-media-foundation.md)
</dt> <dt>

[Getting Information from ASF Header Objects](getting-information-from-asf-header-objects.md)
</dt> </dl>

 

 



