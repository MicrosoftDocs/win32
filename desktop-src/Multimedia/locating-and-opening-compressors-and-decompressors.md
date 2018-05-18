---
title: Locating and Opening Compressors and Decompressors
description: Locating and Opening Compressors and Decompressors
ms.assetid: 'ed931f01-dbfc-4fdc-b725-c062302b037b'
keywords: ["video compression manager (VCM),opening compressors", "VCM (video compression manager),opening compressors", "ICLocate function"]
---

# Locating and Opening Compressors and Decompressors

The following example uses the [**ICLocate**](iclocate.md) function to find a compressor that can compress an 8-bits-per-pixel bitmap.


```C++
BITMAPINFOHEADER bih; 
HIC              hIC 
 
// Initialize the bitmap structure. 
bih.biSize = sizeof(BITMAPINFOHEADER); 
bih.biWidth = bih.biHeight = 0; 
bih.biPlanes = 1; 
bih.biCompression = BI_RGB;      // standard RGB bitmap 
bih.biBitcount = 8;              // 8 bits-per-pixel format 
bih.biSizeImage = 0; 
bih.biXPelsPerMeter = bih.biYPelsPerMeter = 0; 
bih.biClrUsed = bih.biClrImportant = 256; 
 
hIC = ICLocate (ICTYPE_VIDEO, 0L, (LPBITMAPINFOHEADER) &amp;bih, 
    NULL, ICMODE_COMPRESS); 
 
```



The following example enumerates the decompressors in the system to find one that can handle the format of its images. This example uses **ICTYPE\_VIDEO** (which is equivalent to the "VIDC" four-character code) and the [**ICDecompressQuery**](icdecompressquery.md) macro to determine if a compressor or decompressor supports the image format.


```C++
for (i=0; ICInfo(fccType, i, &amp;icinfo); i++) 
{ 
    hic = ICOpen(icinfo.fccType, icinfo.fccHandler, ICMODE_QUERY); 
    if (hic) 
    { 
        // Skip this compressor if it can't handle the format. 
        if (fccType == ICTYPE_VIDEO &amp;&amp; pvIn != NULL &amp;&amp; 
            ICDecompressQuery(hic, pvIn, NULL) != ICERR_OK) 
        { 
            ICClose(hic); 
            continue; 
        } 
 
        // Find out the compressor name. 
        ICGetInfo(hic, &amp;icinfo, sizeof(icinfo)); 
 
        // Add it to the combo box. 
        n = ComboBox_AddString(hwndC,icinfo.szDescription); 
        ComboBox_SetItemData(hwndC, n, hic); 
    } 
} 
 
```



The following example attempts to locate a specific compressor to compress the 8-bit RGB format to an 8-bit RLE format.


```C++
BITMAPINFOHEADER    bihIn, bihOut; 
HIC                 hIC 
 
// Initialize the bitmap structure. 

biSize = bihOut.biSize = sizeof(BITMAPINFOHEADER); 
bihIn.biWidth = bihIn.biHeight = bihOut.biWidth = bihOut.biHeight = 0; 
bihIn.biPlanes = bihOut.biPlanes= 1; 
bihIn.biCompression = BI_RGB;        // standard RGB bitmap for input 
bihOut.biCompression = BI_RLE8;      // 8-bit RLE for output format 
bihIn.biBitcount = bihOut.biBitCount = 8;  // 8 bits-per-pixel format 
bihIn.biSizeImage = bihOut.biSizeImage = 0; 
bihIn.biXPelsPerMeter = bih.biYPelsPerMeter = 
    bihOut.biXPelsPerMeter = bihOut.biYPelsPerMeter = 0; 
bihIn.biClrUsed = bih.biClrImportant = 
    bihOut.biClrUsed = bihOut.biClrImportant = 256; 

hIC = ICLocate (ICTYPE_VIDEO, 0L, 
    (LPBITMAPINFOHEADER)&amp;bihIn, 
    (LPBITMAPINFOHEADER)&amp;bihOut, ICMODE_COMPRESS); 
 
```



## Related topics

<dl> <dt>

[Using the Video Compression Manager](using-the-video-compression-manager.md)
</dt> </dl>

 

 




