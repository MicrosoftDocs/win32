---
title: Configuring File Transfer Streams
description: Configuring File Transfer Streams
ms.assetid: faed54ae-9e80-492a-9602-e726bdb3b54a
keywords:
- streams,configuring file transfer streams
- codecs,configuring file transfer streams
- file transfer streams
- streams,data unit extensions
- codecs,data unit extensions
- data unit extensions,file transfer streams
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Configuring File Transfer Streams

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

File transfer streams do not require any special settings in the [**WM\_MEDIA\_TYPE**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_media_type) structure. They do require a data unit extension to associate a file name with each sample. To send a name with file transfer samples, you must implement a data unit extension system for the stream.

To set a data unit extension for the stream, perform the following steps:

1.  Obtain a pointer to the [**IWMStreamConfig2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstreamconfig2) interface of the stream configuration object by calling **IWMStreamConfig::QueryInterface**.
2.  Add a data unit extension for the stream by calling [**IWMStreamConfig2::AddDataUnitExtension**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstreamconfig2-adddataunitextension) as follows:
    ```C++
    hr = pStreamConfig2->AddDataUnitExtension(CLSID_WMTPropertyFileName,
                                              -1, NULL, 0);
    ```

    

## Related topics

<dl> <dt>

[**Configuration Common to All Streams**](configuration-common-to-all-streams.md)
</dt> <dt>

[**Configuring Arbitrary Stream Types**](configuring-arbitrary-stream-types.md)
</dt> <dt>

[**File Streams**](file-streams.md)
</dt> </dl>

 

 




