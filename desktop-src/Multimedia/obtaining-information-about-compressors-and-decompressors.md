---
title: Obtaining Information About Compressors and Decompressors
description: Obtaining Information About Compressors and Decompressors
ms.assetid: 2f1edfd0-dd30-42ea-a5ae-24265d3f8af3
keywords:
- video compression manager (VCM),getting information about compressors
- VCM (video compression manager),getting information about compressors
- ICGetInfo function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Obtaining Information About Compressors and Decompressors

The following example uses the [**ICGetInfo**](/windows/win32/Vfw/nf-vfw-icgetinfo?branch=master) function to obtain information about a compressor or decompressor.


```C++
ICINFO ICInfo; 
ICGetInfo(hIC, &amp;ICInfo, sizeof(ICInfo)); 
 
```



The following example uses the [**ICGetDefaultKeyFrameRate**](/windows/win32/Vfw/nf-vfw-icgetdefaultkeyframerate?branch=master) and [**ICGetDefaultQuality**](/windows/win32/Vfw/nf-vfw-icgetdefaultquality?branch=master) macros to obtain the default values.


```C++
DWORD dwKeyFrameRate, dwQuality; 
dwKeyFrameRate = ICGetDefaultKeyFrameRate(hIC); 
dwQuality = ICGetDefaultQuality(hIC); 
 
```



The following example uses the [**ICQueryAbout**](/windows/win32/Vfw/nf-vfw-icqueryabout?branch=master) and [**ICAbout**](/windows/win32/Vfw/nf-vfw-icabout?branch=master) macros to display an About dialog box for the compressor or decompressor, if the dialog box exists.


```C++
// If the compressor has an About dialog box, display it.

if ( ICQueryAbout(hIC)) ICAbout(hIC, hwndApp); 
 
```



 

 




