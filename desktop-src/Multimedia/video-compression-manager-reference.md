---
title: Video Compression Manager Reference
description: Video Compression Manager Reference
ms.assetid: dd678b24-62af-495f-bdd6-3082c1a753dd
keywords:
- Video for Windows (VFW),video compression manager (VCM)
- VFW (Video for Windows),video compression manager (VCM)
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Video Compression Manager Reference

This section describes the functions, structures, messages, and macros, associated with VCM. These elements are grouped as follows.

## Compressor Installation and Removal

-   [**ICInstall**](/windows/win32/Vfw/nf-vfw-icinstall?branch=master)
-   [**ICLocate**](/windows/win32/Vfw/nf-vfw-iclocate?branch=master)
-   [**ICOPEN**](/windows/win32/Vfw/ns-vfw-icopen?branch=master)
-   [**ICClose**](/windows/win32/Vfw/nf-vfw-icclose?branch=master)
-   [**ICRemove**](/windows/win32/Vfw/nf-vfw-icremove?branch=master)
-   [**ICOpenFunction**](/windows/win32/Vfw/nf-vfw-icopenfunction?branch=master)

## Locating and Opening a Compressor

-   [**ICLocate**](/windows/win32/Vfw/nf-vfw-iclocate?branch=master)
-   [**ICOPEN**](/windows/win32/Vfw/ns-vfw-icopen?branch=master)
-   [**ICDecompressOpen**](/windows/win32/Vfw/nf-vfw-icdecompressopen?branch=master)
-   [**ICDrawOpen**](/windows/win32/Vfw/nf-vfw-icdrawopen?branch=master)
-   [**ICINFO**](/windows/win32/Vfw/ns-vfw-icinfo?branch=master)
-   [**ICClose**](/windows/win32/Vfw/nf-vfw-icclose?branch=master)

## Selecting Compressors

-   [**ICCompressorChoose**](/windows/win32/Vfw/nf-vfw-iccompressorchoose?branch=master)
-   [**ICCompressorFree**](/windows/win32/Vfw/nf-vfw-iccompressorfree?branch=master)
-   [**COMPVARS**](/windows/win32/Vfw/ns-vfw-compvars?branch=master)

## Configuring Compressors

-   [**ICM\_CONFIGURE**](icm-configure.md)
-   [**ICM\_GETSTATE**](icm-getstate.md)
-   [**ICM\_SETSTATE**](icm-setstate.md)
-   [**ICSendMessage**](/windows/win32/Vfw/nf-vfw-icsendmessage?branch=master)

## Compressor Information

-   [**ICGetInfo**](/windows/win32/Vfw/nf-vfw-icgetinfo?branch=master)
-   [**ICINFO**](/windows/win32/Vfw/ns-vfw-icinfo?branch=master)
-   [**ICM\_GETDEFAULTKEYFRAMERATE**](icm-getdefaultkeyframerate.md)
-   [**ICGetDisplayFormat**](/windows/win32/Vfw/nf-vfw-icgetdisplayformat?branch=master)
-   [**ICM\_GETDEFAULTQUALITY**](icm-getdefaultquality.md)
-   [**ICM\_ABOUT**](icm-about.md)

## Single Image Compression

-   [**ICImageCompress**](/windows/win32/Vfw/nf-vfw-icimagecompress?branch=master)

## Sequence Compression

-   [**ICSeqCompressFrame**](/windows/win32/Vfw/nf-vfw-icseqcompressframe?branch=master)
-   [**ICSeqCompressFrameStart**](/windows/win32/Vfw/nf-vfw-icseqcompressframestart?branch=master)
-   [**ICSeqCompressFrameEnd**](/windows/win32/Vfw/nf-vfw-icseqcompressframeend?branch=master)

## COMPVARS

-   [**ICCompressorChoose**](/windows/win32/Vfw/nf-vfw-iccompressorchoose?branch=master)

## Image Data Compression

-   [**ICCOMPRESS**](/windows/win32/Vfw/ns-vfw-iccompress?branch=master)
-   [**ICM\_COMPRESS\_GET\_FORMAT**](icm-compress-get-format.md)
-   [**ICM\_COMPRESS\_QUERY**](icm-compress-query.md)
-   [**ICM\_COMPRESS\_GET\_SIZE**](icm-compress-get-size.md)
-   [**ICM\_COMPRESS\_BEGIN**](icm-compress-begin.md)
-   [**ICM\_COMPRESS\_END**](icm-compress-end.md)

## Compressor Monitoring

-   [**ICSETSTATUSPROC**](/windows/win32/Vfw/ns-vfw-icsetstatusproc?branch=master)

## Decompressing Single Images

-   [**ICImageDecompress**](/windows/win32/Vfw/nf-vfw-icimagedecompress?branch=master)

## Decompressing Image Data

-   [**ICDECOMPRESSEX**](/windows/win32/Vfw/ns-vfw-icdecompressex?branch=master)
-   [**ICDecompressExBegin**](/windows/win32/Vfw/nf-vfw-icdecompressexbegin?branch=master)
-   [**ICM\_DECOMPRESSEX\_END**](icm-decompressex-end.md)
-   [**ICM\_DECOMPRESS\_GET\_FORMAT**](icm-decompress-get-format.md)
-   [**ICM\_DECOMPRESS\_GET\_PALETTE**](icm-decompress-get-palette.md)
-   [**ICDecompressExQuery**](/windows/win32/Vfw/nf-vfw-icdecompressexquery?branch=master)
-   [**ICDECOMPRESS**](/windows/win32/Vfw/ns-vfw-icdecompress?branch=master)
-   [**ICM\_DECOMPRESS\_BEGIN**](icm-decompress-begin.md)
-   [**ICM\_DECOMPRESS\_END**](icm-decompress-end.md)
-   [**ICM\_DECOMPRESS\_QUERY**](icm-decompress-query.md)

## Using Hardware-Drawing Capabilities

-   [**ICGetInfo**](/windows/win32/Vfw/nf-vfw-icgetinfo?branch=master)
-   [**ICDRAWBEGIN**](/windows/win32/Vfw/ns-vfw-icdrawbegin?branch=master)
-   [**ICM\_DRAW\_END**](icm-draw-end.md)
-   [**ICM\_DRAW\_FLUSH**](icm-draw-flush.md)
-   [**ICM\_DRAW\_QUERY**](icm-draw-query.md)
-   [**ICDrawSuggestFormat**](/windows/win32/Vfw/nf-vfw-icdrawsuggestformat?branch=master)
-   [**ICM\_DRAW\_START**](icm-draw-start.md)
-   [**ICM\_DRAW\_STOP**](icm-draw-stop.md)
-   [**ICM\_GETBUFFERSWANTED**](icm-getbufferswanted.md)
-   [**ICM\_DRAW\_REALIZE**](icm-draw-realize.md)
-   [**ICDrawOpen**](/windows/win32/Vfw/nf-vfw-icdrawopen?branch=master)
-   [**ICDRAW**](/windows/win32/Vfw/ns-vfw-icdraw?branch=master)
-   [**ICM\_DRAW\_GETTIME**](icm-draw-gettime.md)
-   [**ICM\_DRAW\_SETTIME**](icm-draw-settime.md)
-   [**ICM\_DRAW\_WINDOW**](icm-draw-window.md)
-   [**ICM\_DRAW\_REALIZE**](icm-draw-realize.md)
-   [**ICM\_DRAW\_CHANGEPALETTE**](icm-draw-changepalette.md)
-   [**ICM\_DRAW\_RENDERBUFFER**](icm-draw-renderbuffer.md)

## Related topics

<dl> <dt>

[Video Compression Manager](video-compression-manager.md)
</dt> </dl>

 

 




