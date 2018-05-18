---
Description: 'The following example x86 assembly code gets the Terminal Services session ID associated with the current process.'
ms.assetid: '9fcb35cb-6813-46a5-aa38-e102f1b6b7dc'
title: Getting the Session ID of the Current Process
---

# Getting the Session ID of the Current Process

\[The memory addresses specified by this example code may change in future releases of Windows. To ensure that your application will continue to run correctly in the future, your application must call [**GetCurrentProcessId**](base.getcurrentprocessid) and then [**ProcessIdToSessionId**](termserv.processidtosessionid) instead of the following sample code.\]

The following example x86 assembly code gets the Terminal Services session ID associated with the current process.

``` syntax
mov     eax,fs:[00000018]
mov     eax,[eax+0x30]
mov     eax,[eax+0x1d4]
```

 

 



