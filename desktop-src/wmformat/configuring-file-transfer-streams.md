---
title: Configuring File Transfer Streams
description: Configuring File Transfer Streams
ms.assetid: 'faed54ae-9e80-492a-9602-e726bdb3b54a'
keywords: ["streams,configuring file transfer streams", "codecs,configuring file transfer streams", "file transfer streams", "streams,data unit extensions", "codecs,data unit extensions", "data unit extensions,file transfer streams"]
---

# Configuring File Transfer Streams

File transfer streams do not require any special settings in the [**WM\_MEDIA\_TYPE**](wm-media-type.md) structure. They do require a data unit extension to associate a file name with each sample. To send a name with file transfer samples, you must implement a data unit extension system for the stream.

To set a data unit extension for the stream, perform the following steps:

1.  Obtain a pointer to the [**IWMStreamConfig2**](iwmstreamconfig2.md) interface of the stream configuration object by calling **IWMStreamConfig::QueryInterface**.
2.  Add a data unit extension for the stream by calling [**IWMStreamConfig2::AddDataUnitExtension**](iwmstreamconfig2-adddataunitextension.md) as follows:
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

 

 




