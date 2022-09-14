---
title: Reading from One Stream and Writing to Another
description: Reading from One Stream and Writing to Another
ms.assetid: 035a8862-9a0f-49d2-a060-5131ff2b7887
ms.topic: article
ms.date: 05/31/2018
---

# Reading from One Stream and Writing to Another

The following example reads data from a stream, does something with the data, and writes the compressed data into a stream of a new file.


```C++
// SaveSmall - copies a stream of data from one file, compresses 
// the stream, and writes the compressed stream to a new file. 
// 
// ps stream interface pointer 
// lpFilename - new AVI file to build 
// 
 
void SaveSmall(PAVISTREAM ps, LPSTR lpFilename) 
{ 
    PAVIFILE         pf; 
    PAVISTREAM       psSmall; 
    HRESULT          hr; 
    AVISTREAMINFO    strhdr; 
    BITMAPINFOHEADER bi; 
    BITMAPINFOHEADER biNew; 
    LONG             lStreamSize; 
    LPVOID           lpOld; 
    LPVOID           lpNew; 
 
    // Determine the size of the format data using 
    // AVIStreamFormatSize. 
    AVIStreamFormatSize(ps, 0, &lStreamSize); 
    if (lStreamSize > sizeof(bi)) // Format too large? 
        return; 
 
    lStreamSize = sizeof(bi); 
    hr = AVIStreamReadFormat(ps, 0, &bi, &lStreamSize); // Read format 
    if (bi.biCompression != BI_RGB) // Wrong compression format? 
        return; 
 
    hr = AVIStreamInfo(ps, &strhdr, sizeof(strhdr)); 
 
    // Create new AVI file using AVIFileOpen. 
    hr = AVIFileOpen(&pf, lpFilename, OF_WRITE | OF_CREATE, NULL); 
    if (hr != 0) 
        return; 
 
    // Set parameters for the new stream. 
    biNew = bi; 
    biNew.biWidth /= 2; 
    biNew.biHeight /= 2; 
    biNew.biSizeImage = ((((UINT)biNew.biBitCount * biNew.biWidth 
                        + 31)&~31) / 8) * biNew.biHeight; 
    SetRect(&strhdr.rcFrame, 0, 0, (int) biNew.biWidth, 
            (int) biNew.biHeight); 
 
    // Create a stream using AVIFileCreateStream. 
    hr = AVIFileCreateStream(pf, &psSmall, &strhdr); 
    if (hr != 0) {            //Stream created OK? If not, close file. 
        AVIFileRelease(pf); 
        return; 
    } 
 
    // Set format of new stream using AVIStreamSetFormat. 
    hr = AVIStreamSetFormat(psSmall, 0, &biNew, sizeof(biNew)); 
    if (hr != 0) { 
        AVIStreamRelease(psSmall); 
        AVIFileRelease(pf); 
        return; 
    } 
 
    // Allocate memory for the bitmaps. 
    lpOld = GlobalAllocPtr(GMEM_MOVEABLE, bi.biSizeImage); 
    lpNew = GlobalAllocPtr(GMEM_MOVEABLE, biNew.biSizeImage); 
 
    // Read the stream data using AVIStreamRead. 
    for (lStreamSize = AVIStreamStart(ps); lStreamSize <
        AVIStreamEnd(ps); lStreamSize++) { 
        hr = AVIStreamRead(ps, lStreamSize, 1, lpOld, bi.biSizeImage,
            NULL, NULL); 
        // 
        // Place error check here. 
        // 
 
        // Do something with the data and write it to lpNew buffer. 
 
        // Save the compressed data using AVIStreamWrite. 
        hr = AVIStreamWrite(psSmall, lStreamSize, 1, lpNew,
            biNew.biSizeImage, AVIIF_KEYFRAME, NULL, NULL); 
    } 
 
     // Close the stream and file. 
    AVIStreamRelease(psSmall); 
    AVIFileRelease(pf); 
} 
 
```



 

 




