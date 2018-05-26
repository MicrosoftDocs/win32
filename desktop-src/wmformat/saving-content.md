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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Saving Content

By using this SDK, an application can save downloaded or streamed content to the user's local computer, by calling the [**IWMReaderAdvanced2::SaveFileAs**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced2-savefileas?branch=master) method on the reader object. For streamed content, the server must be using Fast Cache streaming, which is described in the section [Enabling Fast Cache Streaming from the Client](enabling-fast-cache-streaming-from-the-client.md). For streamed content, the **SaveFileAs** method creates an ASX file that points to an ASF file containing the saved content. If the reader object is streaming a server-side playlist, each entry is saved as a separate ASF file, and the ASX file points to each of the ASF files. For downloaded content, the **SaveFileAs** method simply creates an ASF file.

To save content to a local file, do the following:

1.  Call [**IWMReader::Open**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmreader-open?branch=master) with the URL. **Open** is an asynchronous call, and returns immediately. Wait for the operation to complete, as described in [To Create a Reader and Open a File](to-create-a-reader-and-open-a-file.md).
2.  Query the reader object for the [**IWMReaderAdvanced4**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced4?branch=master) interface.
3.  Check whether the content can be saved by calling the [**IWMReaderAdvanced4::CanSaveFileAs**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced4-cansavefileas?branch=master) method. If the method returns False, the content cannot be saved locally. Otherwise, proceed to step 4.
4.  Call the [**IWMReaderAdvanced4::IsUsingFastCache**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced4-isusingfastcache?branch=master) method to determine whether the server is using Fast Cache streaming.
5.  Call the [**IWMReaderAdvanced2::SaveFileAs**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced2-savefileas?branch=master) with a file name for the local file. If the **IsUsingFastCache** method returned True, give the file name an .asx extension. Otherwise, give the file name an .asf, .wma, or .wmv extension.

The application can cancel the save operation while it is in progress, by calling the [**IWMReaderAdvanced4::CancelSaveFileAs**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced4-cancelsavefileas?branch=master) method.

The saved content might be protected with DRM, so it may not be possible to play the file on another computer. For more information on content protection, see [Digital Rights Management Features](digital-rights-management-features.md).

## Related topics

<dl> <dt>

[**IWMReader Interface**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmreader?branch=master)
</dt> <dt>

[**IWMReaderAdvanced2 Interface**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced2?branch=master)
</dt> </dl>

 

 




