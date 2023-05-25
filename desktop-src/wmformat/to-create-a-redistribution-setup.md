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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# To Create a Redistribution Setup

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




