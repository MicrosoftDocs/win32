---
title: Source Plug-ins
description: Source Plug-ins
ms.assetid: 9adc2d42-6273-4af0-b57f-2dde5738ed94
keywords:
- Windows Media Format SDK,source plug-ins
- Advanced Systems Format (ASF),source plug-ins
- ASF (Advanced Systems Format),source plug-ins
- source plug-ins
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Source Plug-ins

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A source plug-in is an option available to developers who wish to implement their own storage system for Windows Media® files. A source plug-in enables this through the implementation of a COM interface called **IStream**, which is a standard interface for providing data.

The source plug-in should be written as a dll, and its presence is made known to the SDK through a registry entry. There can be any number of source plug-ins implemented this way. The source plug-in must export the [**WMCreateStreamForURL**](wmcreatestreamforurl.md) function.

To register a source plug-in, the following registry entry should be added:

HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Windows Media\\WMSDK\\sources

Name = "any unique name"

Value = pathname of the source plug-in dll

Once the dll has been registered, the application can use the **IWMReader::Open** method (with the appropriate URL as a parameter) to access stream data, which can be stored in files or user-defined data containers.

## Related topics

<dl> <dt>

[**IWMReader::Open**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreader-open)
</dt> <dt>

[**Programming Reference**](programming-reference.md)
</dt> <dt>

[**WMCreateStreamForURL**](wmcreatestreamforurl.md)
</dt> </dl>

 

 




