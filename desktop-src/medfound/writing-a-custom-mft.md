---
description: This section describes how to write a custom Media Foundation Transform (MFT).
ms.assetid: a95828d3-afc5-4f6b-aedd-5b6a72621e0e
title: Writing a Custom MFT
ms.topic: article
ms.date: 05/31/2018
---

# Writing a Custom MFT

This section describes how to write a custom Media Foundation Transform (MFT).

## MFT Checklist

When you implement a custom MFT, use the following checklist to determine the requirements:



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>All MFTs</td>
<td>All MFTs must implement <a href="/windows/desktop/api/mftransform/nn-mftransform-imftransform"><strong>IMFTransform</strong></a>.<br/> The following topics give more information about implementing this interface:
<ul>
<li><a href="basic-mft-processing-model.md">Basic MFT Processing Model</a></li>
<li><a href="time-stamps-and-durations.md">Time Stamps and Durations</a></li>
<li><a href="handling-stream-changes.md">Handling Stream Changes</a></li>
</ul>
<br/></td>
</tr>
<tr class="even">
<td>Encoders and decoders</td>
<td>Requirements: See <a href="implementing-a-codec-mft.md">Implementing a Codec MFT</a>.<br/> Recommended: Implement <a href="/windows/desktop/api/mfidl/nn-mfidl-imfqualityadvise"><strong>IMFQualityAdvise</strong></a> or <a href="/windows/desktop/api/mfidl/nn-mfidl-imfqualityadvise2"><strong>IMFQualityAdvise2</strong></a>, to support quality-of-service (QoS) notifications.<br/></td>
</tr>
<tr class="odd">
<td>Video decoders and video processors</td>
<td>Optional: Support DirectX Video Acceleration.<br/>
<ul>
<li><a href="direct3d-aware-mfts.md">Direct3D-Aware MFTs</a></li>
<li><a href="supporting-dxva-2-0-in-media-foundation.md">Supporting DXVA 2.0 in Media Foundation</a></li>
</ul></td>
</tr>
<tr class="even">
<td>Hardware codecs</td>
<td>See <a href="hardware-mfts.md">Hardware MFTs</a>.</td>
</tr>
<tr class="odd">
<td>To make your MFT discoverable by applications...</td>
<td>See <a href="registering-and-enumerating-mfts.md">Registering and Enumerating MFTs</a>.</td>
</tr>
<tr class="even">
<td>Asynchronous data processing</td>
<td>The default MFT model uses synchronous (blocking) calls to process data. For some MFTs, asynchronous processing can be more efficient. However, it is also more complex to implement.<br/> For more information, see <a href="asynchronous-mfts.md">Asynchronous MFTs</a>.<br/></td>
</tr>
<tr class="odd">
<td>Rate control, trick mode, or reverse playback</td>
<td>See <a href="implementing-rate-control.md">Implementing Rate Control</a>.</td>
</tr>
<tr class="even">
<td>If your MFT creates threads...</td>
<td>Implement the <a href="/windows/desktop/api/mfidl/nn-mfidl-imfrealtimeclient"><strong>IMFRealTimeClient</strong></a> interface.</td>
</tr>
<tr class="odd">
<td>If your MFT has licensing restrictions...</td>
<td>Consider using the field-of-use mechanism. See <a href="field-of-use-restrictions.md">Field of Use Restrictions</a>.</td>
</tr>
<tr class="even">
<td>If you are porting an existing DirectX Media Object (DMO)...</td>
<td>See <a href="comparison-of-mfts-and-dmos.md">Comparison of MFTs and DMOs</a>.</td>
</tr>
</tbody>
</table>



 

This section contains the following topics:

-   [Time Stamps and Durations](time-stamps-and-durations.md)
-   [Handling Stream Changes](handling-stream-changes.md)
-   [Implementing a Codec MFT](implementing-a-codec-mft.md)
-   [Direct3D-Aware MFTs](direct3d-aware-mfts.md)
-   [Hardware MFTs](hardware-mfts.md)
-   [Codec Merit](codec-merit.md)

## Related topics

<dl> <dt>

[Media Foundation Transforms](media-foundation-transforms.md)
</dt> </dl>

 

 




