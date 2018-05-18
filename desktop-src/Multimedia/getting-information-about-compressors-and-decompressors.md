---
title: Getting Information About Compressors and Decompressors
description: Getting Information About Compressors and Decompressors
ms.assetid: 'bb9773dc-a706-40e6-8703-1cd47101992c'
keywords: ["video compression manager (VCM),getting information about compressors", "VCM (video compression manager),getting information about compressors", "ICGetInfo function"]
---

# Getting Information About Compressors and Decompressors

To get general information about a compressor or decompressor, your application can use the [**ICGetInfo**](icgetinfo.md) function. This function fills an [**ICINFO**](icinfo-struct.md) structure with information about the compressor or decompressor. Your application must allocate the memory for the **ICINFO** structure and pass a pointer to it in **ICGetInfo**. Unless your application searches for a particular compressor or decompressor, the flags in the **ICINFO** structure provide the most useful information about the capabilities of a compressor or decompressor.

To get the default key-frame rate and default quality value of a compressor or decompressor, your application can send the [**ICM\_GETDEFAULTKEYFRAMERATE**](icm-getdefaultkeyframerate.md) and [**ICM\_GETDEFAULTQUALITY**](icm-getdefaultquality.md) messages (or use the [**ICGetDefaultKeyFrameRate**](icgetdefaultkeyframerate.md) and [**ICGetDefaultQuality**](icgetdefaultquality.md) macros).

To determine the best display format of a compressor or decompressor, your application can use the [**ICGetDisplayFormat**](icgetdisplayformat.md) function.

To determine if a compressor or decompressor can display an About dialog box, send the [**ICM\_ABOUT**](icm-about.md) message (or use the [**ICQueryAbout**](icqueryabout.md) macro). You can also display the About dialog box of a compressor or decompressor by sending the ICM\_ABOUT message and changing the value of the *wParam* parameter (or by using the [**ICAbout**](icabout.md) macro).

 

 




