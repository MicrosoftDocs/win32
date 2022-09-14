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
ms.date: 05/31/2018
---

# To Edit Metadata with the Writer

You can access, directly from the writer, the metadata that will go into the header of the file. Call the **QueryInterface** method of any interface in the writer object to obtain a pointer to the [**IWMHeaderInfo**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo) or [**IWMHeaderInfo2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo2) interface. After you have a pointer to the appropriate interface, you can manipulate the metadata just as you would if you had loaded the file in the metadata editor object. For more information about editing metadata, see [Working with Metadata](working-with-metadata.md).

You must make all changes to the metadata before calling [**IWMWriter::BeginWriting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-beginwriting).

> [!Note]  
> If you set metadata for a file, write the file, and then prepare to write a new file without releasing the writer, some metadata that was set for the first file will remain set and will be included with subsequent files. When writing several files with the same instance of the writer object, you have two options: check all the metadata before writing each file, or only write in the writer metadata that applies to all of the files you are writing.

 

## Related topics

<dl> <dt>

[**Writing ASF Files**](writing-asf-files.md)
</dt> </dl>

 

 




