---
Description: Initializing Media Foundation
ms.assetid: e4db81d3-7a9e-47d7-8611-6dac8026259c
title: Initializing Media Foundation
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Initializing Media Foundation

Before using any Microsoft Media Foundation objects or interfaces, you must call the [**MFStartup**](/windows/win32/mfapi/nf-mfapi-mfstartup?branch=master) function. Pass in the constant **MF\_VERSION**.


```C++
    hr = MFStartup(MF_VERSION);
```



The [**MFStartup**](/windows/win32/mfapi/nf-mfapi-mfstartup?branch=master) function initializes the Media Foundation platform. If **MFStartup** returns MF\_E\_BAD\_STARTUP\_VERSION, it means your application was compiled using a version of the Media Foundation headers that does not match the Media Foundation DLLs on your system.

For every call to [**MFStartup**](/windows/win32/mfapi/nf-mfapi-mfstartup?branch=master), your application must call [**MFShutdown**](/windows/win32/mfapi/nf-mfapi-mfshutdown?branch=master).


```C++
MFShutdown();
```



## Related topics

<dl> <dt>

[Media Foundation Architecture](media-foundation-architecture.md)
</dt> <dt>

[Media Foundation Platform APIs](media-foundation-platform-apis.md)
</dt> </dl>

 

 



