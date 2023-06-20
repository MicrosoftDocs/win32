---
title: Configuring Data Unit Extensions
description: Configuring Data Unit Extensions
ms.assetid: 5dc0a596-68ae-409a-9abc-15ca507d6ec7
keywords:
- streams,configuring data unit extensions
- streams,data unit extensions
- data unit extensions,configuring
- profiles,data unit extensions
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Configuring Data Unit Extensions

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Samples written to ASF files can contain additional information apart from the media samples themselves. This information is included using data unit extensions. For more information about data unit extensions, see [Data Unit Extensions](data-unit-extensions.md).

To use data unit extensions, you must configure the stream in the profile to accept them. To configure a data unit extension for a stream, perform the following steps.

1.  Obtain a pointer to the [**IWMStreamConfig2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstreamconfig2) interface by calling the **QueryInterface** method of [**IWMStreamConfig**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstreamconfig).
2.  Call [**IWMStreamConfig2::AddDataUnitExtension**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstreamconfig2-adddataunitextension) to register a type of data unit extension for the stream.

You can examine all of the data unit extension types currently registered for a stream by calling [**IWMStreamConfig2::GetDataUnitExtensionCount**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-iwmstreamconfig2-getdataunitextensioncount) to retrieve the number of registered data unit extension types. Then you can loop through all of the types using calls to [**IWMStreamConfig2::GetDataUnitExtension**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstreamconfig2-getdataunitextension) for each.

Data unit extensions are assigned a size when configured for a stream. Many data unit extension systems use data that is a constant size (usually a structure). However, you can also configure your data unit extensions to be of variable size by setting the size to 0xFFFF. Each data unit extension assigned at encoding time can then be of any size between 1 byte and 65534 bytes. Variably sized data unit extensions are also called dynamic data unit extensions.

The advantage of using dynamic data unit extensions is that you can attach extension data as needed. If you define a data unit extension with a set size, every sample for the stream must contain extension data of that size, even if you have no data for some samples. With dynamic data unit extensions, you can omit data unit extensions from some samples, which saves space and reduces bandwidth requirements. However, if data unit extensions are of variable size, the reading object cannot verify the received extension data against a static size. You must verify that the extension data that you receive is valid, and not malicious distortion of the bit stream.

Individual data unit extensions must be set on samples by using the [**INSSBuffer3::SetProperty**](/previous-versions/windows/desktop/api/Wmsbuffer/nf-wmsbuffer-inssbuffer3-setproperty) method. For more information, see [Setting Data Unit Extensions](setting-data-unit-extensions.md).

## Related topics

<dl> <dt>

[**Configuring Streams**](configuring-streams.md)
</dt> </dl>

 

 




