---
description: File Encoding and Decoding Interfaces
ms.assetid: 5456392d-2557-43b6-93b7-b2ebde218d12
title: File Encoding and Decoding Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# File Encoding and Decoding Interfaces

These interfaces support file encoding and decoding.



| Interface                                                    | Description                                                                                                  |
|--------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**IAMMediaContent**](/previous-versions/windows/desktop/api/Qnetwork/nn-qnetwork-iammediacontent)                   | Retrieve meta-data from a stream, such as the author and title.                                              |
| [**IAMOpenProgress**](/windows/desktop/api/Strmif/nn-strmif-iamopenprogress)                   | Determine the progress of a file-open operation.                                                             |
| [**IAMParse**](/previous-versions/windows/desktop/api/Amparse/nn-amparse-iamparse)                                 | Query and set the parse time for the current position in an MPEG stream.                                     |
| [**IAMStreamSelect**](/windows/desktop/api/Strmif/nn-strmif-iamstreamselect)                   | Control which logical streams are played, and retrieve information about them.                               |
| [**IAMVfwCompressDialogs**](/windows/desktop/api/Strmif/nn-strmif-iamvfwcompressdialogs)       | Display dialog boxes provided by VFW codecs.                                                                 |
| [**IAMVideoCompression**](/windows/desktop/api/Strmif/nn-strmif-iamvideocompression)           | Set video compression parameters.                                                                            |
| [**IConfigAsfWriter**](/previous-versions/windows/desktop/api/Dshowasf/nn-dshowasf-iconfigasfwriter)                 | Control how the [WM ASF Writer](wm-asf-writer-filter.md) filter writes Advanced Systems Format (ASF) files. |
| [**IConfigAviMux**](/windows/desktop/api/Strmif/nn-strmif-iconfigavimux)                       | Control how the [AVI Mux](avi-mux-filter.md) filter writes AVI files.                                       |
| [**IConfigInterleaving**](/windows/desktop/api/Strmif/nn-strmif-iconfiginterleaving)           | Configure interleaving when the AVI Mux filter writes AVI files.                                             |
| [**IDVEnc**](/windows/desktop/api/Strmif/nn-strmif-idvenc)                                     | Set the encoding resolution on the [DV Video Encoder](dv-video-encoder-filter.md) filter.                   |
| [**IDVSplitter**](/windows/desktop/api/Strmif/nn-strmif-idvsplitter)                           | Downgrade the frame rate on a digital video (DV) stream                                                      |
| [**IIPDVDec**](/windows/desktop/api/Strmif/nn-strmif-iipdvdec)                                 | Set the decoding resolution on the [DV Video Decoder](dv-video-decoder-filter.md) filter.                   |
| [**IPersistMediaPropertyBag**](/windows/desktop/api/Strmif/nn-strmif-ipersistmediapropertybag) | Set and retrieve INFO and DISP chunks in AVI streams.                                                        |



 

## Related topics

<dl> <dt>

[Interfaces](interfaces.md)
</dt> </dl>

 

 



