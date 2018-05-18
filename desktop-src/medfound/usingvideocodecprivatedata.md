---
Description: Using Video Codec Private Data
ms.assetid: '0cc24fe4-a5b6-4805-8c8e-3066d12ec4bd'
title: Using Video Codec Private Data
---

# Using Video Codec Private Data

The compressed output produced by the Windows Media Video 9 codecs cannot be properly decompressed without some data provided by the encoder. This data, called codec private data, must be appended to the output media type. You can get the codec private data by calling the methods of the [IWMCodecPrivateData](iwmcodecprivatedatainterface.md) interface. Pass the otherwise complete [**DMO\_MEDIA\_TYPE**](dshow.dmo_media_type) structure to [IWMCodecPrivateData::SetPartialOutputType](iwmcodecprivatedatasetpartialoutputtype.md). Then call [IWMCodecPrivateData::GetPrivateData](iwmcodecprivatedatagetprivatedata.md) twice, once to get the size of the data, and then again to copy the data to a buffer of that size. Create a new buffer to hold the [**VIDEOINFOHEADER**](dshow.videoinfoheader) structure with the private data appended, and copy the structure and the data to that buffer. Finally, set the **pbFormat** member of the **DMO\_MEDIA\_TYPE** structure to the address of the newly created buffer and set the **cbFormat** member to the combined size, in bytes, of the **VIDEOINFOHEADER** and the private data.

If you are using MediaFoundation you can construct a [**DMO\_MEDIA\_TYPE**](dshow.dmo_media_type) structure from an [**IMFMediaType**](imfmediatype.md) interface by calling [**MFCreateAMMediaTypeFromMFMediaType**](mfcreateammediatypefrommfmediatype.md).

You must use the codec private data obtained after first setting the properties on the encoder. If any properties are changed, you must get new private data. If you do not use the private data obtained after all the properties are set for the encoding session, the decoder may not be able to decompress the data.

The following code example demonstrates how to obtain the private data for a video type:


```
HRESULT GetFinalOutputType(DMO_MEDIA_TYPE* pMedia, IMediaObject* pDMO)
{
    // WARNING //
    // This function does not deallocate the memory pointed to by 
    // pMedia->pbFormat. If the VIDEOINFOHEADER referenced by pbFormat
    // was dynamically allocated, a reference to it must be kept before
    //  calling this function so that it can be freed.

    // Perform simple parameter checks.
    if(pMedia == NULL || pDMO == NULL)
        return E_POINTER;
    if(pMedia->formattype != MEDIATYPE_VideoInfo)
        return E_INVALIDARG;

    HRESULT hr = S_OK;

    IWMCodecPrivateData* pPrivData = NULL;
    BYTE* pbData = NULL;
    DWORD cbData = 0;

    BYTE* pbNewVidInf  = NULL;
    DWORD cbNewVidInf  = 0;
    BYTE* pbNewPriv    = NULL;

    // Get the private data interface.
    hr = pDMO->QueryInterface(IID_IWMCodecPrivateData,
                              (void**)&amp;pPrivData);
    GOTO_EXIT_IF_FAILED(hr);

    // Set the partial media type.
    hr = pPrivData->SetPartialOutputType(pMedia);
    GOTO_EXIT_IF_FAILED(hr);

    // Get the size of the private data.
    hr = pPrivData->GetPrivateData(NULL, &amp;cbData);
    GOTO_EXIT_IF_FAILED(hr);

    // Allocate memory for the private data.
    pbData = new BYTE[cbData];
    if(pbData == NULL)
    {
        hr = E_OUTOFMEMORY;
        goto Exit:
    }

    // Get the private data.
    hr = pPrivData->GetPrivateData(pbData, &amp;cbData);

    // Allocate memory for the new VIDEOINFOHEADER.
    cbNewVidInf = pMedia->cbFormat + cbData;
    pbNewVidInf = new BYTE[cbNewVidInf];

    // Copy the VIDEOINFOHEADER to the new buffer.
    memcpy((void*)pbNewVidInf, (void*)pMedia->pbFormat, pMedia->cbFormat);

    // Get the address of the first byte following the VIDEOINFOHEADER.
    pbNewPriv = pbNewVidInf + pMedia->cbFormat;

    // Copy the private data to the new buffer.
    memcpy((void*)pbNewPriv, (void*)pbData, cbData);

    // Set the new VIDEOINFOHEADER in the DMO_MEDIA_TYPE.
    pMedia->pbFormat = pbNewVidInf;
    pMedia->cbFormat = cbNewVidInf;

Exit:
    SAFE_RELEASE(pPrivData);
    SAFE_ARRAY_DELETE(pbData);
    pbNewPriv = NULL;
    return hr;
}
```



> [!Note]  
> The codec private data delivered by a video encoder is not guaranteed to be the same as the private data delivered by a different implementation of the same codec for the same configuration. You must always generate this value using the steps in this topic; never copy the private data from another file.

 

## Related topics

<dl> <dt>

[Configuring Video Encoding](configuringvideoencoding.md)
</dt> <dt>

[Working with Video](workingwithvideo.md)
</dt> </dl>

 

 



