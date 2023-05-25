---
title: Bit Rate
description: Bit Rate
ms.assetid: 7c35a07b-03d3-42d7-aefc-8e6a0033ac48
keywords:
- Windows Media Format SDK,bit rates
- Advanced Systems Format (ASF),bit rates
- ASF (Advanced Systems Format),bit rates
- bit rates,about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Bit Rate

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Bit rate refers to the amount of data per second that is delivered from an ASF file. Bit rate measurements are in bits per second (bps) or kilobits per second (Kbps). Bit rate is often confused with bandwidth, which is a measurement of the data transfer capacity of a network. Bandwidth is also measured in bps and Kbps.

The Windows Media Format SDK can be used to create applications that deliver streaming Windows Media-based content from Internet or intranet locations. When you are streaming data across a network or the Internet, the bit rate is of vital importance to the end-user experience. If the bandwidth available to the network is less than the bit rate of the ASF file, the playback of the file will be interrupted in some way. Usually, insufficient bandwidth will result in either samples being skipped, or a pause in playback while more data is buffered.

Every ASF file is assigned a bit rate value at the time of creation, based upon the type and number of streams that are included in the profile used. Individual streams have their own bit rates. Bit rates can be constant (the original data is compressed in such a way as to maintain a constant flow of data at approximately the same rate) or variable (the original data is compressed in such a way as to maintain the same quality throughout, even though this may mean uneven data flow). Different bit rate types can be applied to different streams within the same file.

You can encode the same content to several different streams, each with a different bit rate. Then you can configure the streams so that they are mutually exclusive. This enables you to create a single file that can be streamed to users with different bandwidths. This feature is called multiple bit rate, or MBR.

## Related topics

<dl> <dt>

[**Concepts**](concepts.md)
</dt> <dt>

[**Constant Bit Rate (CBR) Encoding**](constant-bit-rate--cbr--encoding.md)
</dt> <dt>

[**Inputs, Streams and Outputs**](inputs-streams-and-outputs.md)
</dt> <dt>

[**Profiles**](profiles.md)
</dt> <dt>

[**Variable Bit Rate (VBR) Encoding**](variable-bit-rate--vbr--encoding.md)
</dt> </dl>

 

 




