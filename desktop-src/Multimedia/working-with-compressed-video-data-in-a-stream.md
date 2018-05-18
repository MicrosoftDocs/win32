---
title: Working with Compressed Video Data in a Stream
description: Working with Compressed Video Data in a Stream
ms.assetid: 'b701e072-f162-438f-b607-aea7491a02f9'
---

# Working with Compressed Video Data in a Stream

AVIFile provides several ways for you to access compressed video streams.

If you want to display one or more frames of a compressed video stream, you can retrieve the frames by using the [**AVIStreamRead**](avistreamread.md) function and forwarding the compressed frame data to DrawDib functions to display them. DrawDib functions can display images of several image depths and automatically dither images for displays that cannot handle certain types of device-independent bitmaps (DIBs). These functions work with uncompressed and compressed images. For more information about DrawDib functions, see [DrawDib Functions](drawdib-functions.md).

AVIFile provides functions for decompressing a single video frame. To allocate resources, use the [**AVIStreamGetFrameOpen**](avistreamgetframeopen.md) function. This function creates a buffer for the decompressed data.

You can decompress a single video frame by using the [**AVIStreamGetFrame**](avistreamgetframe.md) function. This function decompresses the frame and retrieves a complete frame of image data, returning the address of the DIB in the [BITMAPINFOHEADER](http://go.microsoft.com/fwlink/p/?linkid=16915) structure. Your application can display the DIB by using standard drawing functions or by using the DrawDib functions.

If your application makes successive calls to **AVIStreamGetFrame**, the function overwrites its buffer with each retrieved frame.

When you finish using **AVIStreamGetFrame** and the decompressed DIB is in its buffer, you can release the allocated resources by using the [**AVIStreamGetFrameClose**](avistreamgetframeclose.md) function.

For more information about decompressing images, see [Video Compression Manager](video-compression-manager.md).

 

 




