---
title: Codec Features
description: Codec Features
ms.assetid: e0bbdf75-2369-4080-ae8e-aabaa8401dcf
keywords:
- Windows Media Format SDK,codec features
- Windows Media Format SDK,features
- codecs,features
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Codec Features

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Windows Media Format SDK is delivered with several audio and video codecs. You can use the codecs provided to compress and decompress content to suit a variety of needs. The codec that is used by the writer to compress data is specified by stream configuration information in the profile. Information from the profile is then stored in the header of the file created by the writer. Then, when the file is opened by the reader or synchronous reader, the profile information in the header identifies the codec needed to decompress the data.

The following features are discussed in this section.

-   [Supported Codecs](supported-codecs.md)
-   [Constant Bit Rate (CBR) Encoding](constant-bit-rate--cbr--encoding.md)
-   [Variable Bit Rate (VBR) Encoding](variable-bit-rate--vbr--encoding.md)
-   [Two-Pass Encoding](two-pass-encoding.md)
-   [High-Resolution Audio Support](high-resolution-audio-support.md)
-   [Low-Delay Audio](low-delay-audio.md)
-   [S/PDIF Audio Output](s-pdif-audio-output.md)
-   [Video Image](video-image.md)
-   [Device Conformance Templates](device-conformance-templates.md)
-   [Video Complexity Settings](video-complexity-settings.md)
-   [Frame Interpolation](frame-interpolation.md)

## Related topics

<dl> <dt>

[**Features**](features.md)
</dt> </dl>

 

 




