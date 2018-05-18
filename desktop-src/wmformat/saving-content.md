---
title: Saving Content
description: Saving Content
ms.assetid: '22f4e580-43a4-48b5-8eb3-90e1346a1093'
keywords: ["Windows Media Format SDK,saving content", "Windows Media Format SDK,Fast Cache streaming", "Advanced Systems Format (ASF),saving content", "ASF (Advanced Systems Format),saving content", "Advanced Systems Format (ASF),Fast Cache streaming", "ASF (Advanced Systems Format),Fast Cache streaming", "streams,saving content", "Fast Cache streaming,saving content"]
---

# Saving Content

By using this SDK, an application can save downloaded or streamed content to the user's local computer, by calling the [**IWMReaderAdvanced2::SaveFileAs**](iwmreaderadvanced2-savefileas.md) method on the reader object. For streamed content, the server must be using Fast Cache streaming, which is described in the section [Enabling Fast Cache Streaming from the Client](enabling-fast-cache-streaming-from-the-client.md). For streamed content, the **SaveFileAs** method creates an ASX file that points to an ASF file containing the saved content. If the reader object is streaming a server-side playlist, each entry is saved as a separate ASF file, and the ASX file points to each of the ASF files. For downloaded content, the **SaveFileAs** method simply creates an ASF file.

To save content to a local file, do the following:

1.  Call [**IWMReader::Open**](iwmreader-open.md) with the URL. **Open** is an asynchronous call, and returns immediately. Wait for the operation to complete, as described in [To Create a Reader and Open a File](to-create-a-reader-and-open-a-file.md).
2.  Query the reader object for the [**IWMReaderAdvanced4**](iwmreaderadvanced4.md) interface.
3.  Check whether the content can be saved by calling the [**IWMReaderAdvanced4::CanSaveFileAs**](iwmreaderadvanced4-cansavefileas.md) method. If the method returns False, the content cannot be saved locally. Otherwise, proceed to step 4.
4.  Call the [**IWMReaderAdvanced4::IsUsingFastCache**](iwmreaderadvanced4-isusingfastcache.md) method to determine whether the server is using Fast Cache streaming.
5.  Call the [**IWMReaderAdvanced2::SaveFileAs**](iwmreaderadvanced2-savefileas.md) with a file name for the local file. If the **IsUsingFastCache** method returned True, give the file name an .asx extension. Otherwise, give the file name an .asf, .wma, or .wmv extension.

The application can cancel the save operation while it is in progress, by calling the [**IWMReaderAdvanced4::CancelSaveFileAs**](iwmreaderadvanced4-cancelsavefileas.md) method.

The saved content might be protected with DRM, so it may not be possible to play the file on another computer. For more information on content protection, see [Digital Rights Management Features](digital-rights-management-features.md).

## Related topics

<dl> <dt>

[**IWMReader Interface**](iwmreader.md)
</dt> <dt>

[**IWMReaderAdvanced2 Interface**](iwmreaderadvanced2.md)
</dt> </dl>

 

 




