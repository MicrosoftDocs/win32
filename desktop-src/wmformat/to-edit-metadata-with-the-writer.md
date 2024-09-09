---
title: To Edit Metadata with the Writer
description: To Edit Metadata with the Writer
ms.assetid: 86badfe3-64bc-4285-a231-f6c0ebf4f262
keywords:
- Windows Media Format SDK,editing metadata with the writer
- Windows Media Format SDK,metadata editing
- Advanced Systems Format (ASF),editing metadata with the writer
- ASF (Advanced Systems Format),editing metadata with the writer
- Advanced Systems Format (ASF),metadata editing
- ASF (Advanced Systems Format),metadata editing
- metadata,editing with the writer
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# To Edit Metadata with the Writer

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can access, directly from the writer, the metadata that will go into the header of the file. Call the **QueryInterface** method of any interface in the writer object to obtain a pointer to the [**IWMHeaderInfo**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo) or [**IWMHeaderInfo2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo2) interface. After you have a pointer to the appropriate interface, you can manipulate the metadata just as you would if you had loaded the file in the metadata editor object. For more information about editing metadata, see [Working with Metadata](working-with-metadata.md).

You must make all changes to the metadata before calling [**IWMWriter::BeginWriting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-beginwriting).

> [!Note]  
> If you set metadata for a file, write the file, and then prepare to write a new file without releasing the writer, some metadata that was set for the first file will remain set and will be included with subsequent files. When writing several files with the same instance of the writer object, you have two options: check all the metadata before writing each file, or only write in the writer metadata that applies to all of the files you are writing.

 

## Related topics

<dl> <dt>

[**Writing ASF Files**](writing-asf-files.md)
</dt> </dl>

 

 




