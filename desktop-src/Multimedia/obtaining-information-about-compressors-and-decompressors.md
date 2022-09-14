---
title: Obtaining Information About Compressors and Decompressors
description: Obtaining Information About Compressors and Decompressors
ms.assetid: 2f1edfd0-dd30-42ea-a5ae-24265d3f8af3
keywords:
- video compression manager (VCM),getting information about compressors
- VCM (video compression manager),getting information about compressors
- ICGetInfo function
ms.topic: article
ms.date: 05/31/2018
---

# Obtaining Information About Compressors and Decompressors

The following example uses the [**ICGetInfo**](/windows/desktop/api/Vfw/nf-vfw-icgetinfo) function to obtain information about a compressor or decompressor.


```C++
ICINFO ICInfo; 
ICGetInfo(hIC, &ICInfo, sizeof(ICInfo)); 
 
```



The following example uses the [**ICGetDefaultKeyFrameRate**](/windows/desktop/api/Vfw/nf-vfw-icgetdefaultkeyframerate) and [**ICGetDefaultQuality**](/windows/desktop/api/Vfw/nf-vfw-icgetdefaultquality) macros to obtain the default values.


```C++
DWORD dwKeyFrameRate, dwQuality; 
dwKeyFrameRate = ICGetDefaultKeyFrameRate(hIC); 
dwQuality = ICGetDefaultQuality(hIC); 
 
```



The following example uses the [**ICQueryAbout**](/windows/desktop/api/Vfw/nf-vfw-icqueryabout) and [**ICAbout**](/windows/desktop/api/Vfw/nf-vfw-icabout) macros to display an About dialog box for the compressor or decompressor, if the dialog box exists.


```C++
// If the compressor has an About dialog box, display it.

if ( ICQueryAbout(hIC)) ICAbout(hIC, hwndApp); 
 
```



 

 




