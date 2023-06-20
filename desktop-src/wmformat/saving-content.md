---
title: Saving Content
description: Saving Content
ms.assetid: 22f4e580-43a4-48b5-8eb3-90e1346a1093
keywords:
- Windows Media Format SDK,saving content
- Windows Media Format SDK,Fast Cache streaming
- Advanced Systems Format (ASF),saving content
- ASF (Advanced Systems Format),saving content
- Advanced Systems Format (ASF),Fast Cache streaming
- ASF (Advanced Systems Format),Fast Cache streaming
- streams,saving content
- Fast Cache streaming,saving content
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Saving Content

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

By using this SDK, an application can save downloaded or streamed content to the user's local computer, by calling the [**IWMReaderAdvanced2::SaveFileAs**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced2-savefileas) method on the reader object. For streamed content, the server must be using Fast Cache streaming, which is described in the section [Enabling Fast Cache Streaming from the Client](enabling-fast-cache-streaming-from-the-client.md). For streamed content, the **SaveFileAs** method creates an ASX file that points to an ASF file containing the saved content. If the reader object is streaming a server-side playlist, each entry is saved as a separate ASF file, and the ASX file points to each of the ASF files. For downloaded content, the **SaveFileAs** method simply creates an ASF file.

To save content to a local file, do the following:

1.  Call [**IWMReader::Open**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreader-open) with the URL. **Open** is an asynchronous call, and returns immediately. Wait for the operation to complete, as described in [To Create a Reader and Open a File](to-create-a-reader-and-open-a-file.md).
2.  Query the reader object for the [**IWMReaderAdvanced4**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced4) interface.
3.  Check whether the content can be saved by calling the [**IWMReaderAdvanced4::CanSaveFileAs**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced4-cansavefileas) method. If the method returns False, the content cannot be saved locally. Otherwise, proceed to step 4.
4.  Call the [**IWMReaderAdvanced4::IsUsingFastCache**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced4-isusingfastcache) method to determine whether the server is using Fast Cache streaming.
5.  Call the [**IWMReaderAdvanced2::SaveFileAs**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced2-savefileas) with a file name for the local file. If the **IsUsingFastCache** method returned True, give the file name an .asx extension. Otherwise, give the file name an .asf, .wma, or .wmv extension.

The application can cancel the save operation while it is in progress, by calling the [**IWMReaderAdvanced4::CancelSaveFileAs**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced4-cancelsavefileas) method.

The saved content might be protected with DRM, so it may not be possible to play the file on another computer. For more information on content protection, see [Digital Rights Management Features](digital-rights-management-features.md).

## Related topics

<dl> <dt>

[**IWMReader Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreader)
</dt> <dt>

[**IWMReaderAdvanced2 Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced2)
</dt> </dl>

 

 




