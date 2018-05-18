---
Description: Processing Data in the Encoder
ms.assetid: '7be4c5e7-db2c-4063-8e5c-af6ffb861aa5'
title: Processing Data in the Encoder
---

# Processing Data in the Encoder

After you have negotiated the input type and output type for the encoder MFT, as described in [Media Type Negotiation on the Encoder](media-type-negotiation-on-the-encoder.md), you can start processing media data samples. The data is passed in form of media samples ([**IMFSample**](imfsample.md) interface) and also received from the output as media samples.

Before sending data to the encoder for processing, you must allocate a media sample and add one of more media buffers containing media data that needs to be encoded. Call [**IMFTransform::ProcessInput**](imftransform-processinput.md) and pass a pointer to the allocated media sample. In addition to the media sample, **ProcessInput** also needs the input stream identifier. To get the stream identifier, call [**IMFTransform::GetStreamIDs**](imftransform-getstreamids.md). Because an encoder is designed to have only one and one output, these stream identifiers always have the value of 0.

To get data from the encoder, call [**IMFTransform::ProcessOutput**](imftransform-processoutput.md). Before you call [**ProcessOutput**](imfqualitymanager-notifyprocessoutput.md), you need to find out whether the encoder allocates the output media samples or you must do so explicitly. To do this, call [**IMFTransform::GetOutputStreamInfo**](imftransform-getoutputstreaminfo.md). This returns output media sample information in the [**MFT\_OUTPUT\_STREAM\_INFO**](mft-output-stream-info.md) structure. If the encoder allocates media samples, it returns the MFT\_OUTPUT\_STREAM\_PROVIDES\_SAMPLES flag in the **dwFlags** member and the **cbSize** member contains zero. If the encoder expects you to allocate the output buffer, create the output media sample and the associated media buffer based on the size returned in **cbSize**. When you call [**ProcessSample**](imfasfmultiplexer-processsample.md), pass a pointer to the newly created media sample. During the encoding session, the encoder fills the media buffers, pointed by the output media sample, with the encoded data.

To start the encoding session, pass the input media sample to the encoder by calling [**ProcessInput**](imftransform-processinput.md). The encoder starts processing and the data and produces one or more output media samples that must be retrieved by [**ProcessOutput**](imftransform-processoutput.md) as long as it returns MF\_E\_TRANSFORM\_NEED\_MORE\_INPUT. If you call **ProcessInput** to pass more input as long as there is output data to be retrieved, **ProcessInput** fails with MF\_E\_NOTACCEPTING. The encoder does not accept any more input until the client calls **ProcessOutput** at least once.

You should set accurate time stamps and durations for all input samples passed. Time stamps are not strictly required but help maintain audio/video synchronization. If you do not have the time stamps for your samples it is better to leave them out than to use uncertain values.

## Encoder Processing Example

The following example code shows how to call [**IMFTransform::ProcessOutput**](imftransform-processoutput.md) to get an encoded sample. For the complete context of this example, see [Encoder Example Code](encoder-example-code.md).


```C++
HRESULT CWmaEncoder::ProcessOutput(IMFSample **ppSample)
{
    if (m_pMFT == NULL)
    {
        return MF_E_NOT_INITIALIZED;
    }

    *ppSample = NULL;

    IMFMediaBuffer* pBufferOut = NULL;
    IMFSample* pSampleOut = NULL;

    DWORD dwStatus;
  
    MFT_OUTPUT_STREAM_INFO mftStreamInfo = { 0 };
    MFT_OUTPUT_DATA_BUFFER mftOutputData = { 0 };

    HRESULT hr = m_pMFT->GetOutputStreamInfo(m_dwOutputID, &amp;mftStreamInfo);
    if (FAILED(hr))
    {
        goto done;
    }

    //create a buffer for the output sample
    hr = MFCreateMemoryBuffer(mftStreamInfo.cbSize, &amp;pBufferOut);
    if (FAILED(hr))
    {
        goto done;
    }

    //Create the output sample
    hr = MFCreateSample(&amp;pSampleOut);
    if (FAILED(hr))
    {
        goto done;
    }

    //Add the output buffer 
    hr = pSampleOut->AddBuffer(pBufferOut);
    if (FAILED(hr))
    {
        goto done;
    }
 
    //Set the output sample
    mftOutputData.pSample = pSampleOut;

    //Set the output id
    mftOutputData.dwStreamID = m_dwOutputID;

    //Generate the output sample
    hr = m_pMFT->ProcessOutput(0, 1, &amp;mftOutputData, &amp;dwStatus);
    if (hr == MF_E_TRANSFORM_NEED_MORE_INPUT)
    {
        hr = S_OK;
        goto done;
    }

    // TODO: Handle MF_E_TRANSFORM_STREAM_CHANGE

    if (FAILED(hr))
    {
        goto done;
    }

    *ppSample = pSampleOut;
    (*ppSample)->AddRef();

done:
    SafeRelease(&amp;pBufferOut);
    SafeRelease(&amp;pSampleOut);
    return hr;
};
```



## Related topics

<dl> <dt>

[ASF Multiplexer](asf-multiplexer.md)
</dt> <dt>

[Instantiating an Encoder MFT](instantiating-the-encoder-mft.md)
</dt> <dt>

[Windows Media Encoders](windows-media-encoders.md)
</dt> </dl>

 

 



