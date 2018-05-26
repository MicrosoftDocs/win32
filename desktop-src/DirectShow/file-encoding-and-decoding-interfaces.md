---
Description: File Encoding and Decoding Interfaces
ms.assetid: 5456392d-2557-43b6-93b7-b2ebde218d12
title: File Encoding and Decoding Interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# File Encoding and Decoding Interfaces

These interfaces support file encoding and decoding.



| Interface                                                    | Description                                                                                                  |
|--------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**IAMMediaContent**](/windows/win32/Qnetwork/nn-qnetwork-iammediacontent?branch=master)                   | Retrieve meta-data from a stream, such as the author and title.                                              |
| [**IAMOpenProgress**](/windows/win32/Strmif/nn-strmif-iamopenprogress?branch=master)                   | Determine the progress of a file-open operation.                                                             |
| [**IAMParse**](/windows/win32/Amparse/nn-amparse-iamparse?branch=master)                                 | Query and set the parse time for the current position in an MPEG stream.                                     |
| [**IAMStreamSelect**](/windows/win32/Strmif/nn-strmif-iamstreamselect?branch=master)                   | Control which logical streams are played, and retrieve information about them.                               |
| [**IAMVfwCompressDialogs**](/windows/win32/Strmif/nn-strmif-iamvfwcompressdialogs?branch=master)       | Display dialog boxes provided by VFW codecs.                                                                 |
| [**IAMVideoCompression**](/windows/win32/Strmif/nn-strmif-iamvideocompression?branch=master)           | Set video compression parameters.                                                                            |
| [**IConfigAsfWriter**](/windows/win32/Dshowasf/nn-dshowasf-iconfigasfwriter?branch=master)                 | Control how the [WM ASF Writer](wm-asf-writer-filter.md) filter writes Advanced Systems Format (ASF) files. |
| [**IConfigAviMux**](/windows/win32/Strmif/nn-strmif-iconfigavimux?branch=master)                       | Control how the [AVI Mux](avi-mux-filter.md) filter writes AVI files.                                       |
| [**IConfigInterleaving**](/windows/win32/Strmif/nn-strmif-iconfiginterleaving?branch=master)           | Configure interleaving when the AVI Mux filter writes AVI files.                                             |
| [**IDVEnc**](/windows/win32/Strmif/nn-strmif-idvenc?branch=master)                                     | Set the encoding resolution on the [DV Video Encoder](dv-video-encoder-filter.md) filter.                   |
| [**IDVSplitter**](/windows/win32/Strmif/nn-strmif-idvsplitter?branch=master)                           | Downgrade the frame rate on a digital video (DV) stream                                                      |
| [**IIPDVDec**](/windows/win32/Strmif/nn-strmif-iipdvdec?branch=master)                                 | Set the decoding resolution on the [DV Video Decoder](dv-video-decoder-filter.md) filter.                   |
| [**IPersistMediaPropertyBag**](/windows/win32/Strmif/nn-strmif-ipersistmediapropertybag?branch=master) | Set and retrieve INFO and DISP chunks in AVI streams.                                                        |



 

## Related topics

<dl> <dt>

[Interfaces](interfaces.md)
</dt> </dl>

 

 



