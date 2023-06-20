---
title: Working with Outputs
description: Working with Outputs
ms.assetid: e2e14e88-dddc-496d-8087-1455da0821e3
keywords:
- Windows Media Format SDK,working with outputs
- Advanced Systems Format (ASF),working with outputs
- ASF (Advanced Systems Format),working with outputs
- Advanced Systems Format (ASF),output numbers and formats
- ASF (Advanced Systems Format),output numbers and formats
- output numbers and formats,about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Working with Outputs

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

As a default, every sample you receive from either reader object is associated with an output number. Each output number corresponds to a stream in the ASF file. The reader assigns output numbers to the streams in the file when the file is opened. Normally there is one output for each stream in a file. If the file uses mutual exclusion, however, each group of mutually exclusive streams is assigned a single output number. The stream that corresponds to the output number of the mutually exclusive streams is determined either by the reader, in the case of multiple bit rate (MBR) files, or by your application, if you are using manual stream selection.

Because the connection name set in the profile is not persisted in the file, the reader creates a default connection name for each output that is simply a string representation of the output number, for example "1", "2", "3" and so on. The connection names enable applications, and the reader itself, to correlate outputs to streams. In a multiple bit rate file, several streams share a connection name. This does not matter to the reader, because the output properties for each MBR stream are identical.

Each output has one or more supported output formats. An output format is the format that the uncompressed samples delivered by the reader use. When the reader opens a file, it sets the format of each output to the default for the media subtype. The number and type of output formats supported is determined by the codec that decompresses the media data.

The following topics explain how to work with outputs:

-   [To Identify Output Numbers](to-identify-output-numbers.md)
-   [Assigning Output Formats](assigning-output-formats.md)

## Related topics

<dl> <dt>

[**IWMReader Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreader)
</dt> <dt>

[**IWMSyncReader Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmsyncreader)
</dt> <dt>

[**Reading ASF Files**](reading-asf-files.md)
</dt> </dl>

 

 




