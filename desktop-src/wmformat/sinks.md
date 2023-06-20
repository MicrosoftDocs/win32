---
title: Sinks
description: Sinks
ms.assetid: '6781a326-a30a-4d4d-96db-332d0f681a31'
keywords:
- Windows Media Format SDK,sinks
- Windows Media Format SDK,file sinks
- Advanced Systems Format (ASF),sinks
- ASF (Advanced Systems Format),sinks
- Advanced Systems Format (ASF),file sinks
- ASF (Advanced Systems Format),file sinks
- Windows Media Format SDK,network sinks
- Windows Media Format SDK,push sinks
- Advanced Systems Format (ASF),network sinks
- ASF (Advanced Systems Format),network sinks
- Advanced Systems Format (ASF),push sinks
- ASF (Advanced Systems Format),push sinks
- sinks,about
- file sinks,about
- network sinks
- push sinks
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Sinks

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The writer object of the Windows Media Format SDK delivers processed content to sinks. Each sink is an object that delivers data. The point of delivery depends upon the type of sink. There are three types of sinks: file sinks, network sinks, and push sinks.

## File Sinks

File sinks write ASF content to a file on a local or network drive. When you use the writer object to write a file without explicitly adding a file sink, the writer will create one for you using the name you pass to [**IWMWriter::SetOutputFilename**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-setoutputfilename). You can assign multiple file sinks to a writer object to write the content in several files at once.

By using a file sink, you can control many aspects of the file. The following features are available through a file sink.

-   File statistics monitoring. You can monitor the file size and duration as it is being created.
-   Partial content file creation. File sinks can be configured to begin writing content at a specific time and to end writing at a specific time. This enables you to create multiple files containing different sections of the same content in the same writing pass.

## Network Sinks

Network sinks broadcast content to a network address. Reading clients can connect to the address to receive the broadcast.

## Push Sinks

Push sinks deliver content from the writer to a server running Windows Media Services. Push sinks are typically used in scenarios where one computer encodes live content and delivers it to one or more servers for wide distribution. Using a push sink enables you to dedicate computers to specific tasks, saving bandwidth and processing power on each server.

## Related topics

<dl> <dt>

[**File Writing Features**](file-writing-features.md)
</dt> <dt>

[**Working with Writer Sinks**](working-with-writer-sinks.md)
</dt> </dl>

 

 




