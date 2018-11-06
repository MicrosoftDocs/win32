---
title: Creating Temporary Streams
description: Creating Temporary Streams
ms.assetid: 8fe75ae1-0111-4b02-a00d-1ef2ca462452
keywords:
- AVIStreamCreate function
- AVIStreamRelease function
- AVIMakeCompressedStream function
ms.topic: article
ms.date: 05/31/2018
---

# Creating Temporary Streams

Temporary streams can be beneficial in several ways. You can use a temporary stream as a work stream, for example, when changing the stream format. Or you can create a temporary stream to hold portions of other streams that have been copied.

You can create a stream in memory that is not associated with any file by using the [**AVIStreamCreate**](/windows/desktop/api/Vfw/nf-vfw-avistreamcreate) function. This function returns the address of the interface to the new stream in a specified location and is used internally by other functions that create temporary streams.

You can create a compressed stream from an uncompressed stream by using the [**AVIMakeCompressedStream**](/windows/desktop/api/Vfw/nf-vfw-avimakecompressedstream) function. You identify the stream to compress, the compression method and compression options, and the handler for the new stream.

When you finish using a stream created with **AVIStreamCreate** or **AVIMakeCompressedStream**, close the stream by using the [**AVIStreamRelease**](/windows/desktop/api/Vfw/nf-vfw-avistreamrelease) function. **AVIStreamRelease** frees the resources the temporary stream used.

 

 




