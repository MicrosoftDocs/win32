---
title: Compressor and Decompressor Basics
description: Compressor and Decompressor Basics
ms.assetid: 49a958c1-1798-4c6c-913c-5bf5869f926b
keywords:
- video compression manager (VCM),opening compressors
- VCM (video compression manager),opening compressors
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Compressor and Decompressor Basics

\[The feature associated with this page, [Video Compression Manager](/windows/win32/multimedia/video-compression-manager), is a legacy feature. Microsoft strongly recommends that new code does not use this feature.\]

To open and locate a compressor, you can use the [**ICLocate**](/windows/desktop/api/Vfw/nf-vfw-iclocate) and [**ICOpen**](/windows/desktop/api/Vfw/nf-vfw-icopen) functions. You can use **ICLocate** to find a compressor of a specific type and to obtain a handle of it for use in other VCM functions. To open a compressor, you can use **ICOpen**. Your application uses the handle returned by this function to identify the opened compressor when it uses other VCM functions.

To open and locate a decompressor, applications can use the [**ICDecompressOpen**](/windows/desktop/api/Vfw/nf-vfw-icdecompressopen) and [**ICDrawOpen**](/windows/desktop/api/Vfw/nf-vfw-icdrawopen) macros. These macros use **ICLocate** for operation.

When your application has finished using a compressor or decompressor, it must close it to free any resources used for compression or decompression. Your application can use the [**ICClose**](/windows/desktop/api/Vfw/nf-vfw-icclose) function to close the compressor or decompressor.

Also, your application can enumerate the compressors or decompressors on a system by using the [**ICInfo**](/windows/desktop/api/Vfw/nf-vfw-icinfo) function.

> [!Note]  
> The stream header in an AVI file contains information about the stream type and the specific handler for that stream. Within the stream header, the **fccType** and **fccHandler** members identify the stream type and the stream handler specified for the stream.

 

 

 




