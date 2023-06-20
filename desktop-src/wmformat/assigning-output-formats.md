---
title: Assigning Output Formats
description: Assigning Output Formats
ms.assetid: 47697ffb-51cb-44cd-a0b0-7d85625a38f9
keywords:
- Windows Media Format SDK,assigning output formats
- Advanced Systems Format (ASF),assigning output formats
- ASF (Advanced Systems Format),assigning output formats
- Advanced Systems Format (ASF),output numbers and formats
- ASF (Advanced Systems Format),output numbers and formats
- output numbers and formats,assigning
- codecs,output numbers and formats
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Assigning Output Formats

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Some codecs can decompress digital media data into several uncompressed formats. You can find all of the supported formats for a specific output using either the asynchronous reader or the synchronous reader.

To examine all of the available formats for an output, perform the following steps. These procedures are identical for both the asynchronous reader and the synchronous reader. Where interface names vary, the synchronous reader methods are listed in parentheses after the methods of the asynchronous reader.

1.  Create a reader object and load a file for reading. For more information, see [To Create a Reader and Open a File](to-create-a-reader-and-open-a-file.md) (or [To Create a Synchronous Reader and Open a File](to-create-a-synchronous-reader-and-open-a-file.md)).
2.  Determine the output for which you want to find the available formats. If you don't already know which output you want to use, you can identify the outputs in the file using the procedures in [To Identify Output Numbers](to-identify-output-numbers.md).
3.  Retrieve the total number of available formats for the desired output by calling [**IWMReader::GetOutputFormatCount**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-iwmreader-getoutputformatcount) (or [**IWMSyncReader::GetOutputFormatCount**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-iwmsyncreader-getoutputformatcount)).
4.  Loop through the available formats one at a time, performing the following steps for each:
    -   Retrieve the [**IWMOutputMediaProps**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmoutputmediaprops) interface for the current output format by calling [**IWMReader::GetOutputFormat**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreader-getoutputformat) (or [**IWMSyncReader::GetOutputFormat**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmsyncreader-getoutputformat)).
    -   Retrieve the [**WM\_MEDIA\_TYPE**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_media_type) structure for the output format by making two calls to [**IWMMediaProps::GetMediaType**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmmediaprops-getmediatype). Make the first call to get the size of the structure, then allocate memory for it and pass a pointer to the allocated memory on the second call.
    -   Find the media subtype of the output format in **WM\_MEDIA\_TYPE.subtype**.
    -   For video, if the current subtype is the format you want to use for output, break out of the loop. Otherwise go to the next iteration.

        For audio, you must check the values in the **WAVEFORMATEX** structure against your requirements. **WM\_MEDIA\_TYPE.pbFormat** points to the **WAVEFORMATEX** structure for audio outputs.

5.  When you have found the output desired, set it for use with the reader by calling [**IWMReader::SetOutputProps**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreader-setoutputprops) (or [**IWMSyncReader::SetOutputProps**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmsyncreader-setoutputprops)). You must pass a pointer to the **IWMOutputMediaProps** interface obtained in the first step of the loop.

## Related topics

<dl> <dt>

[**IWMMediaProps Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmmediaprops)
</dt> <dt>

[**IWMOutputMediaProps Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmoutputmediaprops)
</dt> <dt>

[**IWMReader Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreader)
</dt> <dt>

[**IWMSyncReader Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmsyncreader)
</dt> <dt>

[**Working with Outputs**](working-with-outputs.md)
</dt> </dl>

 

 




