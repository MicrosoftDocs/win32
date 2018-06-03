---
title: Monitoring Compressor and Decompressor Progress
description: Monitoring Compressor and Decompressor Progress
ms.assetid: 7c87c688-75b6-4d3e-9dd5-5f509ff2e473
keywords:
- video compression manager (VCM),monitoring
- VCM (video compression manager),monitoring
- ICSetStatusProc function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Monitoring Compressor and Decompressor Progress

The following example shows how the [**ICSetStatusProc**](/windows/desktop/api/Vfw/nf-vfw-icsetstatusproc) function is used to inform the compressor or decompressor of the callback function address:


```C++
ICSetStatusProc(compvars.hic, 0, (LPARAM) (UINT) hwndApp, 
    &amp;PreviewStatusProc); 
 
```



The following example shows the callback function installed by the previous fragment:


```C++
LONG CALLBACK export PreviewStatusProc(LPARAM lParam, 
    UINT message, LONG l) 
{ 
    switch (message) 
    { 
        MSG msg; 
        case ICSTATUS_START: 
         
        // Create and display status dialog box. 
         
            break; 
        case ICSTATUS_STATUS: 
            ProSetBarPos((int) l); // sets status bar positions 
 
        // Watch for abort message 
            while(PeekMessage(&amp;msg, NULL, 0, 0, PM_REMOVE)) 
            { 
                if (msg.message == WM_KEYDOWN &amp;&amp; msg.wParam == 
                    VK_ESCAPE) 
                    return 1; 
                if (msg.message == WM_SYSCOMMAND &amp;&amp; 
                    (msg.wParam & 0xFFF0) == SC_CLOSE) 
                    return 1; 
 
                TranslateMessage(&amp;msg); 
                DispatchMessage(&amp;msg); 
            } 
            break; 
        case ICSTATUS_END: 
         
        // Close and destroy status dialog box. 
         
            break; 
        case ICSTATUS_YIELD: 
         
         
         
            break; 
    } 
    return 0; 
} 
 
```



 

 




