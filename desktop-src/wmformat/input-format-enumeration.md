---
title: Input Format Enumeration
description: Input Format Enumeration
ms.assetid: 75264598-0226-435a-b71f-6997ff0fcaff
keywords:
- Windows Media Format SDK,input format enumerations
- Windows Media Format SDK,enumerating input formats
- Advanced Systems Format (ASF),input format enumerations
- ASF (Advanced Systems Format),input format enumerations
- Advanced Systems Format (ASF),enumerating input formats
- ASF (Advanced Systems Format),enumerating input formats
- input format enumerations
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Input Format Enumeration

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The writer object gets stream format information from the profile you give it. Stream configuration information in a profile gives the writer all of the information it needs about how the data is to be written in the file. The profile does not provide the writer with any information about the format of the input samples that your application delivers. Input formats will be unknown only for streams compressed with one of the Windows Media codecs; inputs for arbitrary stream types are predictable based on the information in the profile.

The writer object can communicate with the codec for a stream to determine the input types that can be used. Methods are provided to enumerate the possible input types. You should always find the input type that matches your input media by enumerating the supported types rather than setting the input media properties manually. For more information, see [To Enumerate Input Formats](to-enumerate-input-formats.md).

## Related topics

<dl> <dt>

[**File Writing Features**](file-writing-features.md)
</dt> <dt>

[**Working with Inputs**](working-with-inputs.md)
</dt> </dl>

 

 




