---
title: Video Compression Manager Reference
description: Video Compression Manager Reference
ms.assetid: dd678b24-62af-495f-bdd6-3082c1a753dd
keywords:
- Video for Windows (VFW),video compression manager (VCM)
- VFW (Video for Windows),video compression manager (VCM)
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Video Compression Manager Reference

\[The feature associated with this page, [Video Compression Manager](/windows/win32/multimedia/video-compression-manager), is a legacy feature. Microsoft strongly recommends that new code does not use this feature.\]

This section describes the functions, structures, messages, and macros, associated with VCM. These elements are grouped as follows.

## Compressor Installation and Removal

-   [**ICInstall**](/windows/desktop/api/Vfw/nf-vfw-icinstall)
-   [**ICLocate**](/windows/desktop/api/Vfw/nf-vfw-iclocate)
-   [**ICOPEN**](/windows/desktop/api/Vfw/ns-vfw-icopen)
-   [**ICClose**](/windows/desktop/api/Vfw/nf-vfw-icclose)
-   [**ICRemove**](/windows/desktop/api/Vfw/nf-vfw-icremove)
-   [**ICOpenFunction**](/windows/desktop/api/Vfw/nf-vfw-icopenfunction)

## Locating and Opening a Compressor

-   [**ICLocate**](/windows/desktop/api/Vfw/nf-vfw-iclocate)
-   [**ICOPEN**](/windows/desktop/api/Vfw/ns-vfw-icopen)
-   [**ICDecompressOpen**](/windows/desktop/api/Vfw/nf-vfw-icdecompressopen)
-   [**ICDrawOpen**](/windows/desktop/api/Vfw/nf-vfw-icdrawopen)
-   [**ICINFO**](/windows/desktop/api/Vfw/ns-vfw-icinfo)
-   [**ICClose**](/windows/desktop/api/Vfw/nf-vfw-icclose)

## Selecting Compressors

-   [**ICCompressorChoose**](/windows/desktop/api/Vfw/nf-vfw-iccompressorchoose)
-   [**ICCompressorFree**](/windows/desktop/api/Vfw/nf-vfw-iccompressorfree)
-   [**COMPVARS**](/windows/desktop/api/Vfw/ns-vfw-compvars)

## Configuring Compressors

-   [**ICM\_CONFIGURE**](icm-configure.md)
-   [**ICM\_GETSTATE**](icm-getstate.md)
-   [**ICM\_SETSTATE**](icm-setstate.md)
-   [**ICSendMessage**](/windows/desktop/api/Vfw/nf-vfw-icsendmessage)

## Compressor Information

-   [**ICGetInfo**](/windows/desktop/api/Vfw/nf-vfw-icgetinfo)
-   [**ICINFO**](/windows/desktop/api/Vfw/ns-vfw-icinfo)
-   [**ICM\_GETDEFAULTKEYFRAMERATE**](icm-getdefaultkeyframerate.md)
-   [**ICGetDisplayFormat**](/windows/desktop/api/Vfw/nf-vfw-icgetdisplayformat)
-   [**ICM\_GETDEFAULTQUALITY**](icm-getdefaultquality.md)
-   [**ICM\_ABOUT**](icm-about.md)

## Single Image Compression

-   [**ICImageCompress**](/windows/desktop/api/Vfw/nf-vfw-icimagecompress)

## Sequence Compression

-   [**ICSeqCompressFrame**](/windows/desktop/api/Vfw/nf-vfw-icseqcompressframe)
-   [**ICSeqCompressFrameStart**](/windows/desktop/api/Vfw/nf-vfw-icseqcompressframestart)
-   [**ICSeqCompressFrameEnd**](/windows/desktop/api/Vfw/nf-vfw-icseqcompressframeend)

## COMPVARS

-   [**ICCompressorChoose**](/windows/desktop/api/Vfw/nf-vfw-iccompressorchoose)

## Image Data Compression

-   [**ICCOMPRESS**](/windows/desktop/api/Vfw/ns-vfw-iccompress)
-   [**ICM\_COMPRESS\_GET\_FORMAT**](icm-compress-get-format.md)
-   [**ICM\_COMPRESS\_QUERY**](icm-compress-query.md)
-   [**ICM\_COMPRESS\_GET\_SIZE**](icm-compress-get-size.md)
-   [**ICM\_COMPRESS\_BEGIN**](icm-compress-begin.md)
-   [**ICM\_COMPRESS\_END**](icm-compress-end.md)

## Compressor Monitoring

-   [**ICSETSTATUSPROC**](/windows/desktop/api/Vfw/ns-vfw-icsetstatusproc)

## Decompressing Single Images

-   [**ICImageDecompress**](/windows/desktop/api/Vfw/nf-vfw-icimagedecompress)

## Decompressing Image Data

-   [**ICDECOMPRESSEX**](/windows/desktop/api/Vfw/ns-vfw-icdecompressex)
-   [**ICDecompressExBegin**](/windows/desktop/api/Vfw/nf-vfw-icdecompressexbegin)
-   [**ICM\_DECOMPRESSEX\_END**](icm-decompressex-end.md)
-   [**ICM\_DECOMPRESS\_GET\_FORMAT**](icm-decompress-get-format.md)
-   [**ICM\_DECOMPRESS\_GET\_PALETTE**](icm-decompress-get-palette.md)
-   [**ICDecompressExQuery**](/windows/desktop/api/Vfw/nf-vfw-icdecompressexquery)
-   [**ICDECOMPRESS**](/windows/desktop/api/Vfw/ns-vfw-icdecompress)
-   [**ICM\_DECOMPRESS\_BEGIN**](icm-decompress-begin.md)
-   [**ICM\_DECOMPRESS\_END**](icm-decompress-end.md)
-   [**ICM\_DECOMPRESS\_QUERY**](icm-decompress-query.md)

## Using Hardware-Drawing Capabilities

-   [**ICGetInfo**](/windows/desktop/api/Vfw/nf-vfw-icgetinfo)
-   [**ICDRAWBEGIN**](/windows/desktop/api/Vfw/ns-vfw-icdrawbegin)
-   [**ICM\_DRAW\_END**](icm-draw-end.md)
-   [**ICM\_DRAW\_FLUSH**](icm-draw-flush.md)
-   [**ICM\_DRAW\_QUERY**](icm-draw-query.md)
-   [**ICDrawSuggestFormat**](/windows/desktop/api/Vfw/nf-vfw-icdrawsuggestformat)
-   [**ICM\_DRAW\_START**](icm-draw-start.md)
-   [**ICM\_DRAW\_STOP**](icm-draw-stop.md)
-   [**ICM\_GETBUFFERSWANTED**](icm-getbufferswanted.md)
-   [**ICM\_DRAW\_REALIZE**](icm-draw-realize.md)
-   [**ICDrawOpen**](/windows/desktop/api/Vfw/nf-vfw-icdrawopen)
-   [**ICDRAW**](/windows/desktop/api/Vfw/ns-vfw-icdraw)
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

 

 




