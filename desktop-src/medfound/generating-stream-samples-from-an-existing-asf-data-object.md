---
description: Generating Stream Samples from an Existing ASF Data Object
ms.assetid: eb27f122-d958-495d-98ea-8befd105a9a8
title: Generating Stream Samples from an Existing ASF Data Object
ms.topic: article
ms.date: 05/31/2018
---

# Generating Stream Samples from an Existing ASF Data Object

The ASF *splitter* object is a WMContainer layer component that parses the ASF Data Object of an Advanced Systems Format (ASF) file.

Before passing data packets to the splitter, the application must initialize, configure, and select streams on the splitter in order to prepare it for the parsing process. For information, see [Creating the ASF Splitter Object](creating-the-asf-splitter-object.md) and [Configuring the ASF Splitter Object](configuring-the-asf-splitter-object.md).

The methods required for parsing the ASF Data Object are:

-   [**IMFASFSplitter::ParseData**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfsplitter-parsedata) that starts the parsing process by pushing the buffer containing data packets to the splitter.
-   [**IMFASFSplitter::GetNextSample**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfsplitter-getnextsample) that collects stream samples that were generated from the buffer passed to splitter.

## Finding the Data Offset

Before starting the parsing process, the application must locate the Data Object within the ASF file. There are two ways to get the offset of the Data Object from the start of the file:

-   Before you have initialized the ContentInfo object, you can call the [**IMFASFContentInfo::GetHeaderSize**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-getheadersize) method. This method requires a buffer that contains the first 30 bytes of the ASF header. It returns the size of the entire header that indicates the offset to the first data packet. This value also includes the Data Object header size of 50 bytes.
-   After you have initialized the ContentInfo object, you can get the presentation descriptor by calling [**IMFASFContentInfo::GeneratePresentationDescriptor**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-generatepresentationdescriptor), and then querying the presentation descriptor for the [**MF\_PD\_ASF\_DATA\_START\_OFFSET**](mf-pd-asf-data-start-offset-attribute.md) attribute. The value of this attribute is the header size.
    > [!Note]  
    > The [**MF\_PD\_ASF\_DATA\_LENGTH**](mf-pd-asf-data-length-attribute.md) attribute on the presentation descriptor specifies the length of the ASF Data Object.

     

In both cases, the returned value is the size of the Header Object plus the size of the header section of the Data Object. Therefore, the resulting value is the offset to the start of the data packets in the ASF Data Object. When you begin sending data to the splitter, the data must start at this offset from the beginning of the ASF file.

The offset value is passed as a parameter to **ParseData** that starts the parsing process.

The Data Object is divided into data packets. Each data packet contains a data packet header that provides packet parsing information and the payload data—the actual digital media data. In a seeking scenario, the application might want the splitter to start parsing at a particular data packet. To do this, you can use the ASF Indexer is used to retrieve the offset. The indexer returns an offset value that starts at the packet boundary. If you are not using the indexer, make sure that the offset starts at the start of the data packet header. If an invalid offset is passed to the splitter, such as the value does not point at the packet boundary, **ParseHeader** and **GetNextSample** calls succeed but **GetNextSample** does not retrieve any samples and **NULL** is received in the *pSample* parameter.

If the splitter is configured to parse in the reverse direction, then the splitter always starts parsing at the end of the media buffer that is passed to **ParseData**. Therefore, for reverse parsing in the call to **ParseData**, pass the offset in the *cbLength* parameter, which specifies the length of the data and set *cbBufferOffset* to zero.

## Generating Samples for ASF Data Packets

An application starts the parsing process by passing the data packets to the splitter. The input to the splitter is a series of media buffers that contain the entire or fragments of the Data Object. The output from the splitter is a series of media samples that contain the packet data.

To pass input data to the splitter, create a media buffer and fill it with data from the Data Object section of the ASF file. (For more information about media buffers, see [Media Buffers](media-buffers.md).) Then, pass the media buffer to the [**IMFASFSplitter::ParseData**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfsplitter-parsedata) method. You can also specify:

-   The offset into the buffer where the splitter should start parsing. If the offset is zero, parsing begins at the start of the buffer. For information about setting the data offset, see the "Finding the Data Offset" section in this topic.
-   The amount of data to parse. If this value is zero, the splitter parses until it reaches the end of the buffer, as specified by the [**IMFMediaBuffer::GetCurrentLength**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediabuffer-getcurrentlength) method.

The splitter generates media samples by referencing the data in the media buffers. The client can retrieve the output samples by calling [**IMFASFSplitter::GetNextSample**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfsplitter-getnextsample) in a loop until there is no more data to parse. If **GetNextSample** returns the ASF\_STATUSFLAGS\_INCOMPLETE flag in the *pdwStatusFlags* parameter, it means there are more samples to retrieve, and the application can call **GetNextSample** again. Otherwise, call **ParseData** to pass more data to the splitter. For the generated samples, the splitter sets the following information:

-   The splitter sets a time stamp on all the samples that it generates. The sample time represents the presentation time and does not include the preroll time. The application can call [**IMFSample::GetSampleTime**](/windows/desktop/api/mfobjects/nf-mfobjects-imfsample-getsampletime) to get the presentation time, in 100-nanosecond units.
-   If a break occurs during sample generation, the splitter sets the [**MFSampleExtension\_Discontinuity**](mfsampleextension-discontinuity-attribute.md) attribute on the first sample after the discontinuity. Discontinuities are usually caused by dropped packets on a network connection, corrupt file data, or the splitter switching from one source stream to another.
-   For video, the splitter checks whether the sample contains a key frame. If it does, the splitter sets the [**MFSampleExtension\_CleanPoint**](mfsampleextension-cleanpoint-attribute.md) attribute on the sample.

If the splitter is parsing data packets that are received from a media server, it is possible that the packet length is variable. In this case, the client must call **ParseData** for each packet and set the [**MFASFSPLITTER\_PACKET\_BOUNDARY**](mfasfsplitter-packet-boundary-attribute.md) attribute on each buffer that is sent to the splitter. This attribute indicates to the splitter whether the media buffer contains the start of an ASF packet. Set the attribute to **TRUE** if the buffer contains the start of a new packet. If the buffer contains a continuation of the previous packet, set the attribute to **FALSE**. The buffers cannot span multiple packets.

Before passing new media buffers to the splitter, the application must call [**IMFASFSplitter::Flush**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfsplitter-flush). This method resets the splitter and clears any partial frame that is waiting to be completed. This is useful in a seeking scenario where the offset is at a different location.

### Example

The following code example shows how to parse data packets. This example parses from the beginning of the Data Object to the end of the stream and displays information about the samples that contain key frames. For a complete example that uses this code, see [Tutorial: Reading an ASF File](tutorial--reading-an-asf-file.md).


```C++
// Parse the video stream and display information about the video samples.
//
// The current read position of the byte stream must be at the start of the ASF
// Data Object.

HRESULT DisplayKeyFrames(IMFByteStream *pStream, IMFASFSplitter *pSplitter)
{
    const DWORD cbReadSize = 2048;  // Read size (arbitrary value)

    IMFMediaBuffer *pBuffer = NULL;
    IMFSample *pSample = NULL;

    HRESULT hr = S_OK;
    while (SUCCEEDED(hr))
    {
        // The parser must get a newly allocated buffer each time.
        hr = MFCreateMemoryBuffer(cbReadSize, &pBuffer);
        if (FAILED(hr))
        {
            break;
        }

        // Read data into the buffer.
        hr = ReadFromByteStream(pStream, pBuffer, cbReadSize);
        if (FAILED(hr)) 
        {
            break; 
        }

        // Get the amound of data that was read.
        DWORD cbData;
        hr = pBuffer->GetCurrentLength(&cbData);
        if (FAILED(hr)) 
        { 
            break; 
        }

        if (cbData == 0)
        {
            break; // End of file.
        }

        // Send the data to the ASF splitter.
        hr = pSplitter->ParseData(pBuffer, 0, 0);
        SafeRelease(&pBuffer);
        if (FAILED(hr)) 
        { 
            break; 
        }

        // Pull samples from the splitter.
        DWORD parsingStatus = 0;
        do
        {
            WORD streamID;
            hr = pSplitter->GetNextSample(&parsingStatus, &streamID, &pSample);
            if (FAILED(hr)) 
            { 
                break; 
            }
            if (pSample == NULL)
            {
                // No samples yet. Parse more data.
                break;
            }
            if (IsRandomAccessPoint(pSample))
            {
                DisplayKeyFrame(pSample);
            }
            SafeRelease(&pSample);
            
        } while (parsingStatus & ASF_STATUSFLAGS_INCOMPLETE);
    }
    SafeRelease(&pSample);
    SafeRelease(&pBuffer);
    return hr;
}
```



## Related topics

<dl> <dt>

[ASF Splitter](asf-splitter.md)
</dt> </dl>

 

 



