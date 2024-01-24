---
description: Generating New ASF Data Packets
ms.assetid: 7afa9694-c965-40e2-8549-e32ff48def2a
title: Generating New ASF Data Packets
ms.topic: article
ms.date: 05/31/2018
---

# Generating New ASF Data Packets

The ASF *multiplexer* is a WMContainer layer component that works with the [ASF Data Object](asf-file-structure.md) and gives an application the ability to generate ASF data packets for a stream that match the requirements defined in the ContentInfo object.

The multiplexer has one input and one output. It receives a stream sample that contains digital media data and produces one or more data packet that can be written to an ASF container.

The following list summarizes the process of generating ASF data packets:

1.  Pass input data to the multiplexer in [**IMFASFMultiplexer::ProcessSample**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfmultiplexer-processsample).
2.  Collect the data packets by calling [**IMFASFMultiplexer::GetNextPacket**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfmultiplexer-getnextpacket) in a loop until all the complete packets have been retrieved.
3.  After the input data has been converted into complete packets there might be some pending data in the multiplexer, which was not retrieved by [**GetNextPacket**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfmultiplexer-getnextpacket). Call [**IMFASFMultiplexer::Flush**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfmultiplexer-flush) to packetize the pending samples and collect them from the multiplexer by calling **GetNextPacket** again.
4.  Update the associated ASF Header Objects by calling [**IMFASFMultiplexer::End**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfmultiplexer-end) to reflect changes made by the multiplexer during data packet generation.

The following diagram illustrates data packet generation for an ASF file through the multiplexer.

![diagram showing data packet generation for an asf file](images/packet.gif)

## ASF Data Packet Creation

After creating and initializing the multiplexer as described in [Creating the Multiplexer Object](creating-the-multiplexer-object.md), call [**IMFASFMultiplexer::ProcessSample**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfmultiplexer-processsample) to pass input data to the multiplexer for processing into data packets. The specified input must be in a media sample ([**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample) interface) that can have one or more media buffers ([**IMFMediaBuffer**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediabuffer) interface) containing the data for a stream. In case of ASF-to-ASF transcoding, the input media sample can be generated from the splitter that creates packetized stream samples. For more information, see [ASF Splitter](asf-splitter.md).

Before calling [**ProcessSample**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfmultiplexer-processsample), make sure that the time stamp of the input media sample is a valid presentation time; otherwise **ProcessSample** fails and returns the MF\_E\_NO\_SAMPLE\_TIMESTAMP code.

The multiplexer can accept input as compressed or uncompressed media samples through [**ProcessSample**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfmultiplexer-processsample). The multiplexer assigns send times to these samples depending on the bandwidth usage of the stream. During this process, the multiplexer checks the leaky bucket parameters (bit rate and buffer window utilization) and can reject samples that do not adhere to those values. The input media sample can fail the bandwidth check for either of the following reasons:

-   If the input media sample arrived late because the last-assigned send time is greater than the time stamp on this media sample. [**ProcessSample**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfmultiplexer-processsample) fails and returns the **MF\_E\_LATE\_SAMPLE** error code.
-   If the time stamp on the input media sample is earlier than the assigned send time (this indicates buffer overflow). The multiplexer can ignore this situation if it is configured to adjust the bit rate by setting the **MFASF\_MULTIPLEXER\_AUTOADJUST\_BITRATE** flag during multiplexer initialization. For more information, see "Multiplexer Initialization and Leaky Bucket Settings" in [Creating the Multiplexer Object](creating-the-multiplexer-object.md). If this flag is not set and the multiplexer encounters bandwidth overrun, [**ProcessSample**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfmultiplexer-processsample) fails and returns the **MF\_E\_BANDWIDTH\_OVERRUN** error code.

After the multiplexer assigns the send time, the input media sample is added to the *send window*—a list of input media samples ordered by send times and ready to be processed into data packets. During data packet construction, the input media sample is parsed and relevant data is written to a data packet as payload. A complete data packet can contain data from one or more input media samples.

When new input media samples arrive in the send window, they are added to a queue until there are enough media samples to form one complete packet. The data in media buffers contained by the input media sample are not copied to the generated data packet. The data packet hold references to the input media buffers until the input media sample has been fully packetized and the complete packet have been collected from the multiplexer.

When a complete data packet is available, it can be retrieved by calling [**IMFASFMultiplexer::GetNextPacket**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfmultiplexer-getnextpacket). If you call [**ProcessSample**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfmultiplexer-processsample) while there are complete packets ready for retrieval, it fails and returns the **MF\_E\_NOTACCEPTING** error code. This indicates that the multiplexer cannot accept more input and you must call **GetNextPacket** to retrieve the waiting packets. Ideally, every **ProcessSample** call should be followed by one or more **GetNextPacket** calls to get the complete data packets. It may take more than one input media sample to create a complete data packet. Conversely, data in one input media sample might span multiple packets. Therefore, not all calls to **ProcessSample** will yield output media samples.

If the input media sample contains a key frame indicated by the [**MFSampleExtension\_CleanPoint**](mfsampleextension-cleanpoint-attribute.md) attribute, the multiplexer copies the attribute to the packet.

## Getting ASF Data Packets

To collect the output media samples for a complete data packet generated by the multiplexer, call [**IMFASFMultiplexer::GetNextPacket**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfmultiplexer-getnextpacket) in a loop until there are no more output media samples left for the packet. The following lists the success cases:

-   If there is a complete data packet available, [**GetNextPacket**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfmultiplexer-getnextpacket) receives the **ASF\_STATUS\_FLAGS\_INCOMPLETE** flag in the *pdwStatusFlags* parameter; the *ppIPacket* parameter receives a pointer to the first data packet. You must call this method as long it receives this flag. With every iteration, *ppIPacket* points to the next packet in the queue.
-   If there is only one data packet, *ppIPacket* points to it and the **ASF\_STATUS\_FLAGS\_INCOMPLETE** flag is not received in *pdwStatusFlags*.
-   [**GetNextPacket**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfmultiplexer-getnextpacket) can succeed without yielding any data packets if the multiplexer is still in the process of packetizing and adding data packets. In this case, *ppIPacket* points to **NULL**. To proceed, you must provide the multiplexer with more input media samples by calling [**ProcessSample**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfmultiplexer-processsample).

The following example code shows a function that generates data packets by using the multiplexer. The generated data packet contents will be written to the data byte stream allocated by the caller.


```C++
//-------------------------------------------------------------------
// GenerateASFDataPackets
// 
// Gets data packets from the mux. This function is called after 
// calling IMFASFMultiplexer::ProcessSample. 
//-------------------------------------------------------------------

HRESULT GenerateASFDataPackets( 
    IMFASFMultiplexer *pMux, 
    IMFByteStream *pDataStream
    )
{
    HRESULT hr = S_OK;

    IMFSample *pOutputSample = NULL;
    IMFMediaBuffer *pDataPacketBuffer = NULL;

    DWORD dwMuxStatus = ASF_STATUSFLAGS_INCOMPLETE;

    while (dwMuxStatus & ASF_STATUSFLAGS_INCOMPLETE)
    {
        hr = pMux->GetNextPacket(&dwMuxStatus, &pOutputSample);

        if (FAILED(hr))
        {
            break;
        }

        if (pOutputSample)
        {
            //Convert to contiguous buffer
            hr = pOutputSample->ConvertToContiguousBuffer(&pDataPacketBuffer);
            
            if (FAILED(hr))
            {
                break;
            }

            //Write buffer to byte stream
            hr = WriteBufferToByteStream(pDataStream, pDataPacketBuffer, NULL);

            if (FAILED(hr))
            {
                break;
            }
        }

        SafeRelease(&pDataPacketBuffer);
        SafeRelease(&pOutputSample);
    }

    SafeRelease(&pOutputSample);
    SafeRelease(&pDataPacketBuffer);
    return hr;
}
```



The `WriteBufferToByteStream` function is shown in the topic [**IMFByteStream::Write**](/windows/desktop/api/mfobjects/nf-mfobjects-imfbytestream-write).

To see a complete application that uses this code example, see [Tutorial: Copying ASF Streams from One File to Another](tutorial--copying-asf-streams-from-one-file-to-another.md).

## Post Packet-Generation Calls

To make sure that there are no complete data packets waiting in the multiplexer, call [**IMFASFMultiplexer::Flush**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfmultiplexer-flush). This forces the multiplexer to packetize all the media samples that are in progress. The application can collect these packets in form of media samples through **GetNextPacket** in a loop until there are no more packets left to be retrieved.

After all the media samples are generated, call [**IMFASFMultiplexer::End**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfmultiplexer-end) to update the ASF Header Object that is associated with these data packets. The Header Object is specified by passing the ContentInfo object that was used to initialize the multiplexer. This call updates various Header Objects to reflect changes made by the multiplexer during data packet generation. This information includes packet count, send duration, play duration, and stream numbers of all the streams. The overall header size is also updated.

You must ensure that [**End**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfmultiplexer-end) is called after all the data packets have been retrieved. If there are any packets waiting in the multiplexer, **End** will fail and return the **MF\_E\_FLUSH\_NEEDED** error code. In this case, get the waiting packet by calling [**Flush**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfmultiplexer-flush) and [**GetNextPacket**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfmultiplexer-getnextpacket) in a loop.

> [!Note]  
> For VBR encoding, after calling **End**, you must set the encoding statistics in the ContentInfo object's encoding properties. For information about this process, see "Configuring the ContentInfo Object with Encoder Settings" in [Setting Properties in the ContentInfo Object](setting-properties-in-the-contentinfo-object.md). The following list shows the specific properties to set:
>
> -   [**MFPKEY\_RAVG**](mfpkey-ravgproperty.md) is the average bit rate of the VBR content.
> -   [**MFPKEY\_BAVG**](mfpkey-bavgproperty.md) is the buffer window for the average bit rate.
> -   [**MFPKEY\_RMAX**](mfpkey-rmaxproperty.md) is the peak bit rate of the VBR content.
> -   [**MFPKEY\_BMAX**](mfpkey-bmaxproperty.md) is the peak buffer window.

 

## Related topics

<dl> <dt>

[ASF Multiplexer](asf-multiplexer.md)
</dt> <dt>

[Tutorial: Copying ASF Streams from One File to Another](tutorial--copying-asf-streams-from-one-file-to-another.md)
</dt> <dt>

[Tutorial: Writing a WMA File by Using CBR Encoding](tutorial--writing-a-wma-file-by-using-cbr-encoding.md)
</dt> </dl>

 

 



