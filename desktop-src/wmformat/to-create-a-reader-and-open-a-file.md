---
title: To Create a Reader and Open a File
description: To Create a Reader and Open a File
ms.assetid: '82b194d6-7cb7-4b88-9ed7-944b8b43bc29'
keywords: ["Advanced Systems Format (ASF),creating readers", "ASF (Advanced Systems Format),creating readers", "Advanced Systems Format (ASF),opening files", "ASF (Advanced Systems Format),opening files", "asynchronous readers,creating", "asynchronous readers,opening files"]
---

# To Create a Reader and Open a File

Before you can do any work with the reader, you will need to create a reader object and load a file for reading. To initialize the reader and open a file, perform the following steps.

1.  Create a reader object by calling the [**WMCreateReader**](wmcreatereader.md) function. You must specify the desired level of rights management for the new reader object. The available modes are listed in the [**WMT\_RIGHTS**](wmt-rights.md) enumeration type.
2.  Specify a file to read by calling [**IWMReader::Open**](iwmreader-open.md). You must specify a reader callback interface for the reader to use. For more information about the reader callback, see [To Implement Reader Messages in the OnStatus Callback](to-implement-reader-messages-in-the-onstatus-callback.md).
3.  Wait for the reader to open the file. When you call **Open** to load a file, it returns almost immediately and continues processing on another thread. You should wait for operations to complete, by signaling an event when the **OnStatus** callback receives the WMT\_OPENED status message.

The reader also supports the use of the **IStream** COM interface for opening files. You can implement the **IStream** interface any way you choose. After the desired file is opened in **IStream**, you can follow the steps listed above, except that you must call [**IWMReaderAdvanced2::OpenStream**](iwmreaderadvanced2-openstream.md) instead of **IWMReader::Open** in step 2.

## Related topics

<dl> <dt>

[**IWMReader Interface**](iwmreader.md)
</dt> <dt>

[**IWMReaderAdvanced2 Interface**](iwmreaderadvanced2.md)
</dt> <dt>

[**IWMStatusCallback Interface**](iwmstatuscallback.md)
</dt> <dt>

[**Reading Files with the Asynchronous Reader**](reading-files-with-the-asynchronous-reader.md)
</dt> <dt>

[**Using the Callback Methods**](using-the-callback-methods.md)
</dt> </dl>

 

 




