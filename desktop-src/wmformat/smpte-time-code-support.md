---
title: SMPTE Time Code Support
description: SMPTE Time Code Support
ms.assetid: 047bda0d-142d-4eed-9b59-c0c36b97ed45
keywords:
- Windows Media Format SDK,SMPTE time codes
- Advanced Systems Format (ASF),SMPTE time codes
- ASF (Advanced Systems Format),SMPTE time codes
- Windows Media Format SDK,IWMReaderTimecode interface
- Advanced Systems Format (ASF),IWMReaderTimecode interface
- ASF (Advanced Systems Format),IWMReaderTimecode interface
- SMPTE time codes,about
- IWMReaderTimecode
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# SMPTE Time Code Support

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Windows Media Format SDK provides limited support for SMPTE time code, which is a standard time code format for movies and television. You can include SMPTE time code data with samples as data unit extensions. The data portion of the extension is a [**WMT\_TIMECODE\_EXTENSION\_DATA**](/previous-versions/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-wmt_timecode_extension_data) structure containing the information from the original SMPTE time stamp.

Maintaining SMPTE time code in your ASF files comes with performance limits. Each sample with an associated SMPTE time stamp requires transport of the 14 bytes in the time stamp structure. In a streaming scenario, this increased bandwidth requirement could be catastrophic. As a result, it is suggested that SMPTE time codes only be persisted in ASF files during the video editing process, which is typically done with local files. When the final file is created, you should remove the data unit extensions.

You can read SMPTE time stamps just as you would read any other data unit extension, but the reading objects provide integrated support for searching by SMPTE time code. To be able to search for SMPTE time stamps, you must first index the file by SMPTE time code. You can configure the indexer to index time codes by using the [**IWMIndexer2::Configure**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmindexer2-configure) method.

Using the asynchronous reader, you can navigate a file by SMPTE time stamps using the methods of the [**IWMReaderTimecode**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreadertimecode) interface and the [**IWMReaderAdvanced3::StartAtPosition**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced3-startatposition) method. With the synchronous reader, use [**IWMSyncReader2::SetRangeByTimecode**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmsyncreader2-setrangebytimecode).

## Related topics

<dl> <dt>

[**ASF File Features**](asf-file-features.md)
</dt> <dt>

[**Configuring Data Unit Extensions**](configuring-data-unit-extensions.md)
</dt> </dl>

 

 




