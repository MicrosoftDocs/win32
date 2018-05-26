---
title: User-Selected Compressors
description: User-Selected Compressors
ms.assetid: 38569f9c-2df3-4959-990b-5c33203ff916
keywords:
- video compression manager (VCM),user-selected compressors
- VCM (video compression manager),user-selected compressors
- ICCompressorChoose function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# User-Selected Compressors

When compressing data, your application can use the [**ICCompressorChoose**](/windows/win32/Vfw/nf-vfw-iccompressorchoose?branch=master) function to create a dialog box in which the user can select the compressor. You can specify flags for this function to allow the user to specify the key-frame frequency and the movie-data rate, or to display a preview window.

The compressor selected by the user is automatically opened and its handle is returned in the hic member of the [**COMPVARS**](/windows/win32/Vfw/ns-vfw-compvars?branch=master) structure specified in **ICCompressorChoose**.

If you use **ICCompressorChoose**, use the [**ICCompressorFree**](/windows/win32/Vfw/nf-vfw-iccompressorfree?branch=master) function to close the compressor and free any resources associated with the **COMPVARS** structure.

 

 




