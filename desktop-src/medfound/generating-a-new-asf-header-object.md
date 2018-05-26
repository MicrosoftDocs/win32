---
Description: Generating a New ASF Header Object
ms.assetid: cf73306d-156a-45c0-a3d6-ae48734f5709
title: Generating a New ASF Header Object
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Generating a New ASF Header Object

To convert the information contained in the ContentInfo object to a binary ASF Header Object format, the application must call [**IMFASFContentInfo::GenerateHeader**](/windows/win32/wmcontainer/nf-wmcontainer-imfasfcontentinfo-generateheader?branch=master). This call must be made after the data packets are generated and the ContentInfo object contains updated information. **GenerateHeader** returns a pointer to a media buffer that contains the header information in the valid format. The application can then write the data, pointed to by the media buffer, at the beginning of a new ASF file.

## To write a new Header Object by using the ContentInfo object

1.  Call [**MFCreateASFContentInfo**](/windows/win32/wmcontainer/nf-wmcontainer-mfcreateasfcontentinfo?branch=master) to create an empty ContentInfo object.
2.  Call [**IMFASFContentInfo::SetProfile**](/windows/win32/wmcontainer/nf-wmcontainer-imfasfcontentinfo-setprofile?branch=master) to supply the profile object to the ContentInfo object. For information about creating profiles, see [Creating an ASF Profile](creating-an-asf-profile.md).
3.  Call [**IMFASFContentInfo::GenerateHeader**](/windows/win32/wmcontainer/nf-wmcontainer-imfasfcontentinfo-generateheader?branch=master) and pass **NULL** in the *pIHeader* parameter and receive the size of the populated ContentInfo object in the *pcbHeader* parameter. The application can use this value to allocate memory or the media buffer that will contain the Header Object.

    The header size received includes the padding size, which is adjusted depending on the actual size of the header objects. The maximum size of the header objects is 10 MB. If the size exceeds this value, **GenerateHeader** fails with the MF\_E\_ASF\_INVALIDDATA error.

4.  Call [**MFCreateMemoryBuffer**](/windows/win32/mfapi/nf-mfapi-mfcreatememorybuffer?branch=master) to create a media buffer of the received size in step 3.
5.  Call **GenerateHeader** again to generate the new ASF Header Object from the ContentInfo object in the media buffer created in step 4.

    The length of the data in the media buffer is updated and the new size is returned in the *pcbHeader* parameter.

6.  Write the contents of the media buffer at the beginning of the file. The application can use the byte stream to perform the writing operation. For example code, see [**IMFByteStream::Write**](/windows/win32/mfobjects/nf-mfobjects-imfbytestream-write?branch=master).

### Example

The following example code shows how to create a ContentInfo object and generate a media buffer to store the new Header Object. For a complete example that uses this code, see [Tutorial: Copying ASF Streams from One File to Another](tutorial--copying-asf-streams-from-one-file-to-another.md).


```C++
//-------------------------------------------------------------------
// WriteASFFile
//
// Writes the complete ASF file.
//-------------------------------------------------------------------

HRESULT WriteASFFile( 
    IMFASFContentInfo *pContentInfo, // ASF Content Info for the output file.
    IMFByteStream *pDataStream,      // Data stream.
    PCWSTR pszFile                   // Output file name.
    )
{
    
    IMFMediaBuffer *pHeaderBuffer = NULL;
    IMFByteStream *pWmaStream = NULL;

    DWORD cbHeaderSize = 0;
    DWORD cbWritten = 0;

    // Create output file.
    HRESULT hr = MFCreateFile(
        MF_ACCESSMODE_WRITE, 
        MF_OPENMODE_DELETE_IF_EXIST,
        MF_FILEFLAGS_NONE,
        pszFile,
        &amp;pWmaStream
        );

    // Get the size of the ASF Header Object.
    if (SUCCEEDED(hr))
    {
        hr = pContentInfo->GenerateHeader(NULL, &amp;cbHeaderSize);
    }

    // Create a media buffer.
    if (SUCCEEDED(hr))
    {
        hr = MFCreateMemoryBuffer(cbHeaderSize, &amp;pHeaderBuffer);
    }

    // Populate the media buffer with the ASF Header Object.
    if (SUCCEEDED(hr))
    {
        hr = pContentInfo->GenerateHeader(pHeaderBuffer, &amp;cbHeaderSize);
    }
 
    // Write the header contents to the byte stream for the output file.
    if (SUCCEEDED(hr))
    {
        hr = WriteBufferToByteStream(pWmaStream, pHeaderBuffer, &amp;cbWritten);
    }

    if (SUCCEEDED(hr))
    {
        hr = pDataStream->SetCurrentPosition(0);
    }

    // Append the data stream to the file.

    if (SUCCEEDED(hr))
    {
        hr = AppendToByteStream(pDataStream, pWmaStream);
    }

    SafeRelease(&amp;pHeaderBuffer);
    SafeRelease(&amp;pWmaStream);

    return hr;
}
```



## Related topics

<dl> <dt>

[Writing an ASF Header Object for a New File](writing-an-asf-header-object-for-a-new-file.md)
</dt> </dl>

 

 



