---
title: Capturing Data
description: Capturing Data
ms.assetid: de029673-9929-40f9-b29b-2598e1e5c988
keywords:
- capCaptureSequence macro
- capFileSaveAs macro
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Capturing Data

The following example uses the [**capCaptureSequence**](/windows/win32/Vfw/nf-vfw-capcapturesequence?branch=master) macro to start video capture and the [**capFileSaveAs**](/windows/win32/Vfw/nf-vfw-capfilesaveas?branch=master) macro to copy the captured data from the capture file to the file NEWFILE.AVI.


```C++
char szNewName[] = "NEWFILE.AVI";

// Set up the capture operation.

capCaptureSequence(hWndC); 

// Capture.

capFileSaveAs(hWndC, szNewName); 
 
```



## Related topics

<dl> <dt>

[Using Video Capture](using-video-capture.md)
</dt> </dl>

 

 




