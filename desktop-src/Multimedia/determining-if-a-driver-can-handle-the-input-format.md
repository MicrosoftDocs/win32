---
title: Determining If a Driver Can Handle the Input Format
description: Determining If a Driver Can Handle the Input Format
ms.assetid: 456eab43-d830-4a28-b724-3ef35b852372
keywords:
- video compression manager (VCM),input format
- VCM (video compression manager),input format
- ICDrawQuery macro
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Determining If a Driver Can Handle the Input Format

\[The feature associated with this page, [Video Compression Manager](/windows/win32/multimedia/video-compression-manager), is a legacy feature. Microsoft strongly recommends that new code does not use this feature.\]

The following example shows how to check the input format with the [**ICDrawQuery**](/windows/desktop/api/Vfw/nf-vfw-icdrawquery) macro.


```C++
// lpbiIn points to BITMAPINFOHEADER structure indicating the input 
// format. 

if (ICDrawQuery(hIC, lpbiIn) == ICERR_OK) 
{ 
    // Driver recognizes the input format. 
} 
else 
{ 
    // Need a different decompressor. 
} 
 
```



 

 




