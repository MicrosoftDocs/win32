---
title: Output Protection Levels
description: Output Protection Levels
ms.assetid: 6232ecd4-9829-4de3-9810-70e3d3c129a9
keywords:
- Windows Media Format SDK,output protection levels (OPL)
- digital rights management (DRM),output protection levels (OPL)
- DRM (digital rights management),output protection levels (OPL)
- output protection levels (OPL)
- OPL (output protection levels)
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Output Protection Levels

Output protection levels (OPLs) are numerical ratings associated with various technologies that receive digital media content. The level a technology supports depends upon how secure it is. The OPL system, introduced in Windows Media DRM 10, enables licenses to be created with more flexibility than in previous versions. You can specify minimum OPLs required for playback and for copying. In addition, you can specify exceptions to the minimum OPL, either to allow a technology not rated high enough, or to disallow a technology with an OPL that exceeds the minimum.

By specifying restrictions to licenses using OPLs, a content owner need only use two actions (Copy and Play), where previous versions had separate actions defined for the various kinds of devices supported for copying (SDMI, non-SDMI, and Red Book audio CD).

**Note** DRM is not supported by the x64-based version of this SDK.

## Related topics

<dl> <dt>

[**Digital Rights Management Features**](digital-rights-management-features.md)
</dt> <dt>

[**Working with Output Protection Levels**](working-with-output-protection-levels.md)
</dt> </dl>

 

 




