---
title: Opening Streams in an AVI File and Closing the File
description: Opening Streams in an AVI File and Closing the File
ms.assetid: 3c6afa04-3d95-48cd-b468-7167bac07d46
keywords:
- AVIFileGetStream function
ms.topic: article
ms.date: 05/31/2018
---

# Opening Streams in an AVI File and Closing the File

The following example opens all the streams in an AVI file using the [**AVIFileGetStream**](/windows/desktop/api/Vfw/nf-vfw-avifilegetstream) function. If an error is encountered, the file is closed.


```C++
// InsertAVIFile - opens the streams in an AVI file. 
// 
// pfile - file-interface pointer from AVIFileOpen 
// 
// Global variables 
// gcpavi - count of the number of streams in an AVI file 
// gapavi[] = array of stream-interface pointers 
 
void InsertAVIFile(PAVIFILE pfile, HWND hwnd, LPSTR lpszFile) 
{ 
    int    i; 
    gcpavi = 0; 
 
    // Open the streams until a stream is not available. 
    for (i = gcpavi; i < MAXNUMSTREAMS; i++) { 
        gapavi[i] = NULL; 
        if (AVIFileGetStream(pfile, &gapavi[i], 0L, i - gcpavi) 
            != AVIERR_OK) 
        break; 
 
    if (gapavi[i] == NULL) 
        break; 
    } 
    // Display error message-stream not found. 
    if (gcpavi == i) 
    { 
        // Handle failure.
        if (pfile) // If file is open, close it 
            AVIFileRelease(pfile); 
        return; 
    } 
    else { 
        gcpavi = i - 1; 
    } 
 
//  . 
//  . Place functions to process data here. 
//  . 
} 
 
```



 

 




