---
title: Working with Writer Sinks
description: Working with Writer Sinks
ms.assetid: 1ad28684-47d2-4ddb-bf18-22310f0392a0
keywords:
- Advanced Systems Format (ASF),writer sinks
- ASF (Advanced Systems Format),writer sinks
- Advanced Systems Format (ASF),sinks
- ASF (Advanced Systems Format),sinks
- sinks,writer sinks
- writer sinks,about
ms.topic: article
ms.date: 05/31/2018
---

# Working with Writer Sinks

The writer object of the Windows Media Format SDK processes input media data into a bit stream. However, the writer object does not deliver the bit stream to its final destination (either to a file or a network location). To write the ASF content to a usable format, you must use writer sinks.

The writer object supports three types of sinks: file sinks, network sinks, and push sinks. A file sink writes ASF content to an ASF file on disk. A network sink broadcasts ASF content from a network address. A push sink delivers data to a server running Windows Media Services so that the server can make the content available to its intended audience. You can also create your own sinks to deliver ASF data in whatever way is required by your application. For information about network sinks and push sinks, see [Sending ASF Data Over a Network](sending-asf-data-over-a-network.md). The remainder of this section discusses writer sinks.

You can configure one or more sinks for each instance of the writer you use. Each sink handles only a single destination. For example, if you want to write three files at once, you must create and configure a separate file sink for each.

The following sections describe the use of writer sinks.



| Section                                                                      | Description                                                                      |
|------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| [Adding Sinks to the Writer](adding-sinks-to-the-writer.md)                 | Describes how to add sinks to the writer.                                        |
| [Enumerating Sinks](enumerating-sinks.md)                                   | Describes how to enumerate the sinks that have been added to the writer.         |
| [Getting Error Messages from a Sink](getting-error-messages-from-a-sink.md) | Describes how to configure sinks to deliver status messages to your application. |
| [Using File Sinks](using-file-sinks.md)                                     | Describes how to use a writer file sink to create an ASF file on disk.           |
| [Using Custom Sinks](using-custom-sinks.md)                                 | Describes how to create and use your own custom sinks to deliver ASF data.       |



 

## Related topics

<dl> <dt>

[**IWMWriterAdvanced Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwriteradvanced)
</dt> <dt>

[**IWMWriterSink Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwritersink)
</dt> <dt>

[**Writing ASF Files**](writing-asf-files.md)
</dt> </dl>

 

 




