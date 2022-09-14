---
title: Adding an Information Chunk
description: Adding an Information Chunk
ms.assetid: ebba5079-1f67-4236-9260-e36ff72ad51c
keywords:
- capFileSetInfoChunk macro
ms.topic: article
ms.date: 05/31/2018
---

# Adding an Information Chunk

If you need to include other information in your application in addition to audio and video, you can create information chunks and insert them into a capture file. Information chunks can contain several types of information, including the details of a copyright notice, identification of the video source, or external timing information. The following example stores external timing information a SMPTE (Society of Motion Picture and Television Engineers) timecode in an information chunk and adds the chunk to a capture file using the [**capFileSetInfoChunk**](/windows/desktop/api/Vfw/nf-vfw-capfilesetinfochunk) macro.


```C++
//  This example assumes the application controls 
//  the video source for preroll and postroll. 
CAPINFOCHUNK cic;
// . 
// . 
// . 
cic.fccInfoID = infotypeSMPTE_TIME;
cic.lpData = "00:20:30:12"; 
cic.cbData = strlen (cic.lpData) + 1;
capFileSetInfoChunk (hwndC, &cic); 
 
```



## Related topics

<dl> <dt>

[Using Video Capture](using-video-capture.md)
</dt> </dl>

 

 




