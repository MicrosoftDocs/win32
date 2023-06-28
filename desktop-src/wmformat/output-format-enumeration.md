---
title: Output Format Enumeration
description: Output Format Enumeration
ms.assetid: 53d5724b-f875-4b2e-92fa-279f46111f29
keywords:
- Windows Media Format SDK,output format enumerations
- Advanced Systems Format (ASF),output format enumerations
- ASF (Advanced Systems Format),output format enumerations
- Windows Media Format SDK,IWMReaderTypeNegotiation interface
- Advanced Systems Format (ASF),IWMReaderTypeNegotiation interface
- ASF (Advanced Systems Format),IWMReaderTypeNegotiation interface
- output format enumerations
- IWMReaderTypeNegotiation
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Output Format Enumeration

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Both the reader object and the synchronous reader object communicate with the codecs to enumerate the possible output formats for compressed streams. When you read a file containing content compressed with one or more of the Windows Media codecs, you can examine the possible output formats to choose the one that best suits your needs. For convenience, each codec has a default output format which is set to the most commonly used format. For more information about output enumeration, see [Working with Outputs](working-with-outputs.md).

You can make certain changes to an output format depending upon the media type. For video streams, for example, you can change the frame size and color depth. The reading objects both support an interface to test changes you make to the output format, called [**IWMReaderTypeNegotiation**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreadertypenegotiation).

## Related topics

<dl> <dt>

[**File Reading Features**](file-reading-features.md)
</dt> </dl>

 

 




