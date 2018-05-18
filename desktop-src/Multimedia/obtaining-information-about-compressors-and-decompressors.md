---
title: Obtaining Information About Compressors and Decompressors
description: Obtaining Information About Compressors and Decompressors
ms.assetid: '2f1edfd0-dd30-42ea-a5ae-24265d3f8af3'
keywords: ["video compression manager (VCM),getting information about compressors", "VCM (video compression manager),getting information about compressors", "ICGetInfo function"]
---

# Obtaining Information About Compressors and Decompressors

The following example uses the [**ICGetInfo**](icgetinfo.md) function to obtain information about a compressor or decompressor.


```C++
ICINFO ICInfo; 
ICGetInfo(hIC, &amp;ICInfo, sizeof(ICInfo)); 
 
```



The following example uses the [**ICGetDefaultKeyFrameRate**](icgetdefaultkeyframerate.md) and [**ICGetDefaultQuality**](icgetdefaultquality.md) macros to obtain the default values.


```C++
DWORD dwKeyFrameRate, dwQuality; 
dwKeyFrameRate = ICGetDefaultKeyFrameRate(hIC); 
dwQuality = ICGetDefaultQuality(hIC); 
 
```



The following example uses the [**ICQueryAbout**](icqueryabout.md) and [**ICAbout**](icabout.md) macros to display an About dialog box for the compressor or decompressor, if the dialog box exists.


```C++
// If the compressor has an About dialog box, display it.

if ( ICQueryAbout(hIC)) ICAbout(hIC, hwndApp); 
 
```



 

 




