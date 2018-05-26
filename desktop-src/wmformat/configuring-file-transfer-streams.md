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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Configuring File Transfer Streams

File transfer streams do not require any special settings in the [**WM\_MEDIA\_TYPE**](/windows/win32/Wmsdkidl/ns-wmsdkidl-_wmmediatype?branch=master) structure. They do require a data unit extension to associate a file name with each sample. To send a name with file transfer samples, you must implement a data unit extension system for the stream.

To set a data unit extension for the stream, perform the following steps:

1.  Obtain a pointer to the [**IWMStreamConfig2**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmstreamconfig2?branch=master) interface of the stream configuration object by calling **IWMStreamConfig::QueryInterface**.
2.  Add a data unit extension for the stream by calling [**IWMStreamConfig2::AddDataUnitExtension**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmstreamconfig2-adddataunitextension?branch=master) as follows:
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

 

 




