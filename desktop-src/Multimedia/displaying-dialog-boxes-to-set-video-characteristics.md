---
title: Displaying Dialog Boxes to Set Video Characteristics
description: Displaying Dialog Boxes to Set Video Characteristics
ms.assetid: 8074f7d1-e8ab-46c3-acc2-a18be0eb4cc7
keywords:
- CAPDRIVERCAPS structure
- capDriverGetCaps macro
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Displaying Dialog Boxes to Set Video Characteristics

Each capture driver can provide up to three different dialog boxes used to control aspects of the video digitization and capture process. The following example demonstrates how to display these dialog boxes. Before displaying each dialog box, the example calls the [**capDriverGetCaps**](/windows/win32/Vfw/nf-vfw-capdrivergetcaps?branch=master) macro and checks the [**CAPDRIVERCAPS**](/windows/win32/Vfw/ns-vfw-tagcapdrivercaps?branch=master) structure returned to see if the capture driver can display it.


```C++
HWND hWndC = capCreateCaptureWindow(TEXT("My Capture Window"),
    WS_CHILD | WS_VISIBLE, 0, 0, 160, 120, hwndParent, nID);

CAPDRIVERCAPS CapDriverCaps = { }; 
CAPSTATUS     CapStatus = { };

capDriverGetCaps(hWndC, &amp;CapDriverCaps, sizeof(CAPDRIVERCAPS)); 
 
// Video source dialog box. 
if (CapDriverCaps.fHasDlgVideoSource)
{
    capDlgVideoSource(hWndC); 
}
 
// Video format dialog box. 
if (CapDriverCaps.fHasDlgVideoFormat) 
{
    capDlgVideoFormat(hWndC); 

    // Are there new image dimensions?
    capGetStatus(hWndC, &amp;CapStatus, sizeof (CAPSTATUS));

    // If so, notify the parent of a size change.
} 
 
// Video display dialog box. 
if (CapDriverCaps.fHasDlgVideoDisplay)
{
    capDlgVideoDisplay(hWndC); 
}
```



## Related topics

<dl> <dt>

[Using Video Capture](using-video-capture.md)
</dt> <dt>

[**capDriverGetCaps**](/windows/win32/Vfw/nf-vfw-capdrivergetcaps?branch=master)
</dt> </dl>

 

 




