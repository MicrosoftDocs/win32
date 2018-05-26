---
title: Sequence Compression
description: Sequence Compression
ms.assetid: ea24088d-6a52-4d4e-8496-5b6a6616f684
keywords:
- video compression manager (VCM),sequence compression
- VCM (video compression manager),sequence compression
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Sequence Compression

Your application can use the [**ICSeqCompressFrame**](/windows/win32/Vfw/nf-vfw-icseqcompressframe?branch=master), [**ICSeqCompressFrameStart**](/windows/win32/Vfw/nf-vfw-icseqcompressframestart?branch=master), and [**ICSeqCompressFrameEnd**](/windows/win32/Vfw/nf-vfw-icseqcompressframeend?branch=master) functions to compress a sequence of frames. These functions use the data stored in the [**COMPVARS**](/windows/win32/Vfw/ns-vfw-compvars?branch=master) structure. Applications use the [**ICCompressorChoose**](/windows/win32/Vfw/nf-vfw-iccompressorchoose?branch=master) function to allow the user to select a compressor, open it, and set the compression parameters in the **COMPVARS** structure; however, applications can set the parameters in the structure manually.

Before an application can begin compressing a sequence of frames, it must use **ICSeqCompressFrameStart** to allocate the necessary resources. After the resources are allocated, the application can use **ICSeqCompressFrame** to compress each frame individually. The frame rate and key-frame frequency used in compressing the sequence are specified in members of the **COMPVARS** structure. The return value for **ICSeqCompressFrame** points to the compressed data.

When an application finishes compressing a sequence, it can use **ICSeqCompressFrameEnd** to free system resources allocated for **ICSeqCompressFrameStart**. To free the resources allocated for the **COMPVARS** structure, the application can use the [**ICCompressorFree**](/windows/win32/Vfw/nf-vfw-iccompressorfree?branch=master) function.

 

 




