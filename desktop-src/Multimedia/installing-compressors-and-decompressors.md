---
title: Installing Compressors and Decompressors
description: Installing Compressors and Decompressors
ms.assetid: 8bcca000-c4c7-47e7-a4c0-5d0d1750176f
keywords:
- video compression manager (VCM),installing compressors
- VCM (video compression manager),installing compressors
- ICInstall function
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Installing Compressors and Decompressors

\[The feature associated with this page, [Video Compression Manager](/windows/win32/multimedia/video-compression-manager), is a legacy feature. Microsoft strongly recommends that new code does not use this feature.\]

The following example shows how an application can install a function as a compressor or decompressor using the [**ICInstall**](/windows/desktop/api/Vfw/nf-vfw-icinstall) function.


```C++
// This function looks like a DriverProc entry point. 

LRESULT MyCodecFunction(DWORD dwID, HDRVR hDriver, 
    UINT uiMessage, LPARAM lParam1, LPARAM lParam2); 
 
// This function installs the MyCodecFunction as a compressor. 

result = ICInstall ( ICTYPE_VIDEO, mmioFOURCC('s','a','m','p'), 
    (LPARAM)(FARPROC)&MyCodecFunction, NULL, ICINSTALL_FUNCTION); 
 
```



 

 




