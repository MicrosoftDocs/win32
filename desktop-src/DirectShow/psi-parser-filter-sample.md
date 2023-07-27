---
description: PSI Parser Filter Sample
ms.assetid: e815d57f-25e5-4a71-8f40-e7abec0db236
title: PSI Parser Filter Sample
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PSI Parser Filter Sample

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

## Description

The PSI Parser filter receives Program Specific Information (PSI) from an MPEG-2 transport stream and extracts program information from the Program Association Table (PAT) and Program Map Tables (PMT). This information enables an application to configure the MPEG-2 Demultiplexer. The filter supports a custom interface, [**IMpeg2PsiParser**](impeg2psiparser.md), for retrieving the PSI information.

This filter is designed for MPEG-2 devices, such as IEEE 1394 MPEG-2 camcorders and D-VHS devices. See [MSTape Driver](mstape-driver.md) for more information. Digital television broadcast sources should use a TIF filter to get program information.

## Usage

You can test the PSI Parser filter in GraphEdit as follows:

1.  Launch GraphEdit.
2.  Insert an MPEG-2 transport source. MPEG-2 camcorders and D-VHS devices appear as "Microsoft AV/C Tape Subunit Device" in the Video Capture Sources category.
3.  Connect the source filter to the MPEG-2 Demultiplexer filter.
4.  Use the property page on the demux to create an output pin with an "MPEG-2 PSI" media type. This pin will deliver the PAT and PMT sections.
5.  Use the demux property page to map PID 0x00 to the output pin. Set the content type to "MPEG2 PSI Sections".
6.  Connect the demux output pin to PSI Parser, as shown in the following diagram.

    ![psi parser filter graph](images/psi-parser.png)

7.  Run the graph, in order to feed PSI data to the PSI Parser filter. As the filter decodes the PAT sections, it automatically maps the PMT PIDs to the same output pin on the demux, so that it receives the PMT sections.
8.  Use the PSI Parser property page to select a program number. The elementary stream list in the property page will show the PID and stream type associated with each elementary stream in the selected program. The property page is designed to recognize stream types defined in ISO/IEC 13818-1.
9.  Enter the audio PID number in the **Audio PID** edit box, and the video PID number in the **Video PID** edit box.
10. Click the **View Program** button. The PSI Parser will configure the output pins on the demux to match the program stream information and render the pins.

> [!Note]  
> The PSI Parser property page is provided to make testing easier, and to provide sample code that configures the MPEG-2 Demultiplexer. It is not recommended for applications to use. Applications should configure the demux programmatically.

 

To use the PSI Parser filter in an application, start by building the filter graph from the MPEG-2 source to the MPEG-2 demux. Code for this step is not shown here, because the exact graph configuration will depend on the source.

Next, create an output pin on the demux for the PSI data. Map PID 0x00, which is reserved for PAT sections, to this pin, as shown in the following code:


```C++
// Set the media type to MPEG-2 table sections.
AM_MEDIA_TYPE mt;
ZeroMemory(&mt, sizeof(AM_MEDIA_TYPE));
mt.majortype = KSDATAFORMAT_TYPE_MPEG2_SECTIONS;

// Create the pin.
IPin *pPsiPin;
hr = pDemux->CreateOutputPin(&mt, L"PSI", &pPsiPin);
if (SUCCEEDED(hr))
{
    // Map to PID 0.
    ULONG Pid = 0x00;
    hr = pPid->MapPID(1, &Pid, MEDIA_MPEG2_PSI);
}
```



For more information, see [Using the MPEG-2 Demultiplexer](using-the-mpeg-2-demultiplexer.md).

Add the PSI Parser filter to the graph and connect it to the output pin on the demux. Query the PSI Parser for the [**IMpeg2PsiParser**](impeg2psiparser.md) interface. Now run the graph and wait for EC\_PROGRAM\_CHANGED events, which signal a new PAT or PMT section. This event is a custom event defined by the PSI Parser filter. When you receive an EC\_PROGRAM\_CHANGED event, you can get the available PSI information by calling **IMpeg2PsiParser** methods. This section describes the methods you will need most often.

To get the number of programs, use the [**IMpeg2PsiParser::GetCountOfPrograms**](impeg2psiparser-getcountofprograms.md) method:


```C++
int NumProgs = 0;
hr = pPsi->GetCountOfPrograms(&NumProgs);
```



To get the program number for a specific program, use the [**IMpeg2PsiParser::GetRecordProgramNumber**](impeg2psiparser-getrecordprogramnumber.md) method:


```C++
WORD ProgNum = 0;
for (int i = 0; i < NumProgs; i++)
{
    hr = pPsi->GetRecordProgramNumber(i, &ProgNum);
    ...
}
```



The program number is used to obtain the PMT entries for individual programs. To get the number of elementary streams in a program, use the [**GetCountOfElementaryStreams**](impeg2psiparser-getcountofelementarystreams.md) method:


```C++
WORD cElemStreams = 0;
hr = pPsi->GetCountOfElementaryStreams(ProgNum, &cElemStreams);
```



For each elementary stream, the [**IMpeg2PsiParser::GetRecordElementaryPid**](/previous-versions/windows/desktop/legacy/dd376623(v=vs.85)) method returns the PID, and the [**IMpeg2PsiParser::GetRecordStreamType**](/previous-versions/windows/desktop/legacy/dd376626(v=vs.85)) method returns the stream type:


```C++
BYTE ESType = 0;
WORD ESPid = 0;
for (WORD j = 0; j < cElemStreams; j++)
{
    hr = pPsi->GetRecordElementaryPid(ProgNum, j, &ESPid);
    hr = pPsi->GetRecordStreamType(ProgNum, j, &ESType);
}
```



The PID and the stream type enable you to configure new output pins on the MPEG-2 Demultiplexer. This may require some knowledge of the original source. For example, ISO/IEC 13818-1 defines stream types 0x80 through 0xFF as "user private," but other standards that are based on MPEG-2 may assign other meanings to these types.

The MPEG-2 Demultiplexer can create new pins and new PID mappings while the graph is running, but you must stop the graph to connect pins.

## Downloading the Sample

To download the DirectShow SDK samples, install the latest version of the [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx).

This sample is installed under the following path: *\[SDK Root\]*\\Samples\\Multimedia\\DirectShow\\Filters\\PSIParser.

## Related topics

<dl> <dt>

[DirectShow Samples](directshow-samples.md)
</dt> <dt>

[**IMpeg2PsiParser Interface**](impeg2psiparser.md)
</dt> </dl>

 

 
