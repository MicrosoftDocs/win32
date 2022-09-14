---
title: To Create a Redistribution Setup
description: To Create a Redistribution Setup
ms.assetid: cf2c8fa1-cfd6-47cc-b572-ba1b95d59105
keywords:
- Windows Media Format SDK,software redistribution
- Advanced Systems Format (ASF),software redistribution
- ASF (Advanced Systems Format),software redistribution
- Windows Media Format SDK,redistribution
- Advanced Systems Format (ASF),redistribution
- ASF (Advanced Systems Format),redistribution
- software redistribution,creating
- software redistribution,WMFDist.exe
- redistribution,creating
- redistribution,WMFDist.exe
- WMFDist.exe
ms.topic: article
ms.date: 05/31/2018
---

# To Create a Redistribution Setup

1.  Have your setup routine install your application files and make required settings before invoking the redistribution package.
2.  Install WMFDist.exe. You can use the /Q:A flag to do a quiet, unattended installation and suppress the user interface of the redistribution setup during the installation of your application. Your routine must then detect whether restarting is needed at the end.

    For example:

    ```C++
    WMFDist.exe /Q:A
    ```

    

## Related topics

<dl> <dt>

[**Software Redistribution**](software-redistribution.md)
</dt> </dl>

 

 




