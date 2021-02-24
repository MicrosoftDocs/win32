---
description: I have an AVI file containing a Windows Media Video stream.
ms.assetid: 0b4c5bf2-caa6-4e14-be5f-9e25ec918cf0
title: I have an AVI file containing a Windows Media Video stream. How can I convert it to a WMV file?
ms.topic: article
ms.date: 05/31/2018
---

# I have an AVI file containing a Windows Media Video stream. How can I convert it to a WMV file?

The Windows Media Audio and Video codec interfaces do not provide methods to create files using the Advanced Systems Format (ASF), which is the format used for WMV files. If you want to convert a file (using any container) to an ASF file, you must use the objects of the Windows Media Format SDK.

Retrieve the compressed Windows Media samples from the source file and pass them to the writer object as stream samples. For more information, see the Windows Media Format 9 Series SDK documentation.

## Related topics

<dl> <dt>

[Frequently Asked Questions](frequentlyaskedquestions.md)
</dt> </dl>

 

 



