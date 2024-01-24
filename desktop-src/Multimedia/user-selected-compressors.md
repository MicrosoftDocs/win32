---
title: User-Selected Compressors
description: User-Selected Compressors
ms.assetid: 38569f9c-2df3-4959-990b-5c33203ff916
keywords:
- video compression manager (VCM),user-selected compressors
- VCM (video compression manager),user-selected compressors
- ICCompressorChoose function
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# User-Selected Compressors

\[The feature associated with this page, [Video Compression Manager](/windows/win32/multimedia/video-compression-manager), is a legacy feature. Microsoft strongly recommends that new code does not use this feature.\]

When compressing data, your application can use the [**ICCompressorChoose**](/windows/desktop/api/Vfw/nf-vfw-iccompressorchoose) function to create a dialog box in which the user can select the compressor. You can specify flags for this function to allow the user to specify the key-frame frequency and the movie-data rate, or to display a preview window.

The compressor selected by the user is automatically opened and its handle is returned in the hic member of the [**COMPVARS**](/windows/desktop/api/Vfw/ns-vfw-compvars) structure specified in **ICCompressorChoose**.

If you use **ICCompressorChoose**, use the [**ICCompressorFree**](/windows/desktop/api/Vfw/nf-vfw-iccompressorfree) function to close the compressor and free any resources associated with the **COMPVARS** structure.

 

 




