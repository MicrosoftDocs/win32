---
title: Sequence Compression
description: Sequence Compression
ms.assetid: ea24088d-6a52-4d4e-8496-5b6a6616f684
keywords:
- video compression manager (VCM),sequence compression
- VCM (video compression manager),sequence compression
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Sequence Compression

\[The feature associated with this page, [Video Compression Manager](/windows/win32/multimedia/video-compression-manager), is a legacy feature. Microsoft strongly recommends that new code does not use this feature.\]

Your application can use the [**ICSeqCompressFrame**](/windows/desktop/api/Vfw/nf-vfw-icseqcompressframe), [**ICSeqCompressFrameStart**](/windows/desktop/api/Vfw/nf-vfw-icseqcompressframestart), and [**ICSeqCompressFrameEnd**](/windows/desktop/api/Vfw/nf-vfw-icseqcompressframeend) functions to compress a sequence of frames. These functions use the data stored in the [**COMPVARS**](/windows/desktop/api/Vfw/ns-vfw-compvars) structure. Applications use the [**ICCompressorChoose**](/windows/desktop/api/Vfw/nf-vfw-iccompressorchoose) function to allow the user to select a compressor, open it, and set the compression parameters in the **COMPVARS** structure; however, applications can set the parameters in the structure manually.

Before an application can begin compressing a sequence of frames, it must use **ICSeqCompressFrameStart** to allocate the necessary resources. After the resources are allocated, the application can use **ICSeqCompressFrame** to compress each frame individually. The frame rate and key-frame frequency used in compressing the sequence are specified in members of the **COMPVARS** structure. The return value for **ICSeqCompressFrame** points to the compressed data.

When an application finishes compressing a sequence, it can use **ICSeqCompressFrameEnd** to free system resources allocated for **ICSeqCompressFrameStart**. To free the resources allocated for the **COMPVARS** structure, the application can use the [**ICCompressorFree**](/windows/desktop/api/Vfw/nf-vfw-iccompressorfree) function.

 

 




